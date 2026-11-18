#!/usr/bin/env python3
"""Check every statement in the digests against the manual page it cites.

The digests in digests/ are summaries of the LightAct manual written by AI
agents. This script reads each digest, pairs every statement with the manual
page named under its heading, and asks TypeSafe's Jev model one Choice
question per statement: does the page support it, contradict it, or not
mention it? Anything that is not a confident "supports" is listed in
verification/report.md for a person or an agent to read against the page.

Files in verification/:
    report.md      what to read, written by a full run
    results.json   every statement with its verdict, written by a full run
                   (local only, not kept in git)
    cache.json     answers keyed by a hash of model, question, statement and page
                   text, so a later run only pays for what changed (local only,
                   not kept in git)
    reviewed.json  flags a reviewer has read and accepted, keyed by statement
                   and page text; edited by hand

Standard library only. The API key is read from the TYPESAFE_API_KEY
environment variable and is never printed or written anywhere.

    python3 scripts/verify-digests.py --dry-run          # plan and token estimate, no API call
    python3 scripts/verify-digests.py --digest assets    # one digest, results on screen
    python3 scripts/verify-digests.py                    # everything, writes verification/

API reference used: https://docs.typesafe.ai/api.md and
https://docs.typesafe.ai/cookbooks/citation_check.md
"""

from __future__ import annotations

import argparse
import collections
import concurrent.futures
import dataclasses
import datetime
import hashlib
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

API_URL = "https://api.typesafe.ai/v1/systemone"
API_KEY_VARIABLE = "TYPESAFE_API_KEY"

# A pinned model, so a monthly run compares like with like and the cache stays valid.
DEFAULT_MODEL = "jev-1.14.0"

# Same starting threshold as the TypeSafe citation-check cookbook.
AUTO_ACCEPT = 0.8

# Documented limits for Jev 1.14: 64k tokens per request (page plus all
# questions) and 32k per question (page plus one question). There is no
# tokenizer in the standard library, so tokens are estimated from characters
# and the budgets below leave room for the estimate being wrong.
REQUEST_TOKEN_BUDGET = 44_000
QUESTION_TOKEN_BUDGET = 22_000
CHARS_PER_TOKEN = 3.0
# Not an API limit. It keeps a single request, and a single failure, small.
MAX_QUESTIONS = 80
# Pages longer than this are split at headings and every part is asked.
MAX_STATE_CHARS = 24_000
# US dollars per million input tokens when this was written. Output is free.
PRICE_PER_MILLION_TOKENS = 0.042

VERDICTS = ("supports", "contradicts", "not_mentioned")

QUESTION = (
    "The statement is one line from a condensed summary of the manual text in `source_pages`. "
    "How does the manual text relate to the statement? If `lines_above_the_statement` is given, "
    "it holds the summary lines the statement continues from. Use them only to understand the "
    "statement. Judge the statement itself."
)
CRITERIA = {
    "supports": (
        "The manual text states every fact in the statement, or the statement follows directly "
        "from it. Paraphrase, shortened wording and a different order are fine. A statement that "
        "the manual text does not list, show or say something is supported when the manual text "
        "really does not."
    ),
    "contradicts": (
        "The manual text says something that conflicts with the statement, such as a different "
        "name, value, number, unit, order or behaviour."
    ),
    "not_mentioned": (
        "The statement asserts a fact that cannot be found in the manual text, and nothing in "
        "the manual text conflicts with it."
    ),
}


# --------------------------------------------------------------------------
# Reading the digests
# --------------------------------------------------------------------------


@dataclasses.dataclass(frozen=True)
class Statement:
    digest: str  # digest file name, for example "assets.md"
    line: int  # line number in the digest, starting at 1
    text: str  # the statement
    section: tuple  # digest headings it sits under; for the reader, not sent to the model
    context: tuple  # lines above it that it needs to make sense: a lead line, parent bullets
    pages: tuple  # cited manual pages, for example ("docs/assets/3d-model.md",)


HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
BULLET = re.compile(r"^(\s*)(?:[-*+]|\d+[.)])\s+(.*)$")
RULE = re.compile(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$")
TICK = re.compile(r"`([^`]+)`")
DOCS_PAGE = re.compile(r"^docs/\S+\.md$")
LEADING_DOCS_PAGE = re.compile(r"^`(docs/[^`\s]+\.md)`\s*:?\s*(.*)$")
LEADING_FILE = re.compile(r"^`([^`\s]+\.md)`")
NODE_FILE = re.compile(r"\(`([^`\s]+\.md)`\)")
TAG = r"(?:[A-Z]{1,3}\d*|\d+)"
TAG_GROUP = re.compile(r"\[(%s(?:\s*,\s*%s)*)\]" % (TAG, TAG))
TRAILING_TAG = re.compile(r"(?:\s*\bTag)?\s*\[(%s)\]\.?\s*$" % TAG)
UNCLEAR_START = re.compile(r"^\**Unclear\b", re.IGNORECASE)
UNCLEAR_INSIDE = re.compile(r"\s+\**Unclear:")
BASE_DECLARATION = re.compile(r"All source paths are under `([^`]+)`")
ABBREVIATION = re.compile(r'"(\w+)" = (?:the page\'s )?"([^"]+)"')
TABLE_DIVIDER = re.compile(r"^\|[\s:|-]+\|?\s*$")
SUMMARY_TITLE = re.compile(r"^(what this section covers|how to read this digest)", re.IGNORECASE)
CLOSING_TITLE = re.compile(r"^for automation and pipelines", re.IGNORECASE)


def _source_line(line):
    """Return the backticked paths if the line is only a source reference, else None.

    A source reference is one or more backticked paths, optionally followed
    by a note in brackets: `docs/a.md` or `.../udp-node-category/` (one folder).
    """
    text = line.strip()
    if not text.startswith("`"):
        return None
    outside = re.sub(r"\([^)]*\)", "", text)
    if re.sub(r"[\s,;.]|\band\b", "", TICK.sub("", outside)):
        return None
    return TICK.findall(outside)


def _split_row(line):
    cells = re.split(r"(?<!\\)\|", line.strip())
    if cells and not cells[0].strip():
        cells = cells[1:]
    if cells and not cells[-1].strip():
        cells = cells[:-1]
    return [c.strip() for c in cells]


def parse_digest(name, text, known_pages=None, skipped=None):
    """Turn one digest into a list of Statement objects.

    known_pages is the set of manual pages that exist ("docs/..."), used to
    find node pages that sit in a subfolder. skipped, if given, is a Counter
    that receives the reasons lines were left out.
    """
    if skipped is None:
        skipped = collections.Counter()
    known = set(known_pages) if known_pages is not None else None
    base = "docs"
    base_declared = False
    abbreviations = {}
    statements = []

    headings = []  # open headings: dicts with level, title, source, tags, pages
    bullets = []  # open bullets: (indent, text, pages, skip)
    lead = None  # the last plain line: context for the bullets and table under it
    table = None  # header cells of the table being read
    expecting_source = False

    def nearest(key):
        for heading in reversed(headings):
            if heading[key]:
                return heading[key]
        return None

    def resolve_node(folder, token):
        direct = folder + "/" + token
        if known is None or direct in known:
            return direct
        for prefix in (folder + "/", base + "/"):
            found = sorted(p for p in known if p.startswith(prefix) and p.endswith("/" + token))
            if len(found) == 1:
                return found[0]
        return direct

    def titles():
        deep = tuple(h["title"] for h in headings if h["level"] >= 2)
        return deep or tuple(h["title"] for h in headings[-1:])

    for number, raw in enumerate(text.split("\n"), 1):
        line = raw.rstrip()

        found = BASE_DECLARATION.search(line)
        if found:
            base = found.group(1).rstrip("/")
            base_declared = True
        for short, full in ABBREVIATION.findall(line):
            abbreviations[short] = full

        heading = HEADING.match(line)
        if heading:
            level = len(heading.group(1))
            while headings and headings[-1]["level"] >= level:
                headings.pop()
            headings.append({"level": level, "title": heading.group(2), "source": None, "tags": {}, "pages": []})
            bullets, lead, table = [], None, None
            expecting_source = True
            continue

        if not line.strip():
            table = None
            continue
        if RULE.match(line):
            continue

        if expecting_source:
            expecting_source = False
            tokens = _source_line(line)
            if tokens and headings:
                if all(DOCS_PAGE.match(t) for t in tokens):
                    headings[-1]["source"] = ("pages", tuple(tokens))
                    continue
                if tokens[0].endswith("/"):
                    token = tokens[0].rstrip("/")
                    if token.startswith(".../"):
                        parent = next((h["source"][1] for h in reversed(headings[:-1])
                                       if h["source"] and h["source"][0] == "folder"), base)
                        folder = parent + "/" + token[4:]
                    elif token.startswith("docs/"):
                        folder = token
                    else:
                        folder = base + "/" + token
                    headings[-1]["source"] = ("folder", folder)
                    continue

        title = headings[-1]["title"] if headings else ""
        summary = any(SUMMARY_TITLE.match(h["title"]) for h in headings)
        closing = any(CLOSING_TITLE.match(h["title"]) for h in headings)
        source = None if (summary or closing) else nearest("source")

        # Tables: the first row names the columns, every later row is a statement.
        if line.lstrip().startswith("|"):
            if TABLE_DIVIDER.match(line.strip()):
                continue
            cells = _split_row(line)
            if table is None:
                table = cells
                continue
            if not source or source[0] != "pages":
                skipped["no page to check against"] += 1
                continue
            body = "; ".join("%s: %s" % (h, c) for h, c in zip(table, cells) if c)
            statements.append(Statement(name, number, body, titles(), (lead,) if lead else (), source[1]))
            continue
        table = None

        bullet = BULLET.match(line)
        if bullet:
            indent = len(bullet.group(1).expandtabs(4))
            body = bullet.group(2).strip()
            while bullets and bullets[-1][0] >= indent:
                bullets.pop()
        else:
            indent = -1
            body = line.strip()
            bullets, lead = [], None
        parent = bullets[-1] if bullets else None

        def remember(pages, skip=False):
            if bullet:
                bullets.append((indent, body, pages, skip))

        if UNCLEAR_START.match(body) or (parent and parent[3]):
            skipped["Unclear note"] += 1
            remember(None, skip=True)
            continue
        cut = UNCLEAR_INSIDE.search(body)
        if cut:
            body = body[: cut.start()].rstrip()

        pages = None
        own_page = LEADING_DOCS_PAGE.match(body)
        if closing:
            # Closing sections mix facts from many pages. Keep a line only
            # when it names exactly one page.
            named = sorted({t for t in TICK.findall(body) if DOCS_PAGE.match(t)})
            if len(named) == 1:
                pages = (named[0],)
        elif summary:
            pass
        elif own_page:
            # "`docs/x.md`: fact about that page [TAG]"
            page, body = own_page.group(1), own_page.group(2).strip()
            holder = headings[-1] if headings else None
            tag = TRAILING_TAG.search(body)
            if tag:
                body = body[: tag.start()].rstrip()
                if holder is not None:
                    holder["tags"][tag.group(1)] = page
            if holder is not None and page not in holder["pages"]:
                holder["pages"].append(page)
            pages = (page,)
        elif not bullet and base_declared and LEADING_FILE.match(body):
            pages = (base + "/" + LEADING_FILE.match(body).group(1),)
        elif source and source[0] == "folder":
            folder = source[1]
            node = NODE_FILE.search(body)
            if node:
                # "**Name** (`file.md`): facts". The file name is the citation, not a fact.
                pages = (resolve_node(folder, node.group(1)),)
                body = (body[: node.start()].rstrip() + body[node.end():]).strip()
                body = re.sub(r"^\*\*([^*]+)\*\*", r"\1", body)
            elif parent and parent[2]:
                pages = parent[2]
            elif known is None or folder + ".md" in known:
                pages = (folder + ".md",)
        else:
            tags = nearest("tags") or {}
            used = []
            for group in TAG_GROUP.findall(body):
                for tag in re.split(r"\s*,\s*", group):
                    if tag in tags and tags[tag] not in used:
                        used.append(tags[tag])
            if used:
                pages = tuple(used)
            elif parent and parent[2]:
                pages = parent[2]
            elif nearest("pages"):
                pages = tuple(nearest("pages"))
            elif source and source[0] == "pages":
                pages = source[1]

        for short, full in abbreviations.items():
            body = re.sub(r"(?<![\w`])%s:" % re.escape(short), full + ":", body)

        if body.endswith(":"):
            # An introduction to the lines below it, not a fact by itself.
            if bullet:
                remember(pages)
            else:
                lead = body
            continue
        if not body:
            continue
        if not pages:
            skipped["opening summary or closing section" if (summary or closing or not headings or not source)
                    else "no page to check against"] += 1
            remember(None)
            continue

        context = ((lead,) if lead and bullet else ()) + tuple(b[1] for b in bullets)
        statements.append(Statement(name, number, body, titles() or (title,), context, tuple(pages)))
        remember(tuple(pages))
        if not bullet:
            lead = body if len(body) <= 300 else body[:300] + " ..."

    return statements


def list_digests(folder, only=None):
    """Digest files in the folder, without the index. only picks one by name."""
    files = sorted(p for p in Path(folder).glob("*.md") if p.name != "INDEX.md")
    if only:
        wanted = only if only.endswith(".md") else only + ".md"
        files = [p for p in files if p.name == wanted]
        if not files:
            sys.exit("No digest called %s in %s" % (wanted, folder))
    return files


# --------------------------------------------------------------------------
# Building requests
# --------------------------------------------------------------------------

_SPLIT_POINTS = (
    re.compile(r"(?m)^(?=#{1,6}\s)"),  # before a heading
    re.compile(r"(?<=\n\n)"),  # after a blank line
    re.compile(r"(?<=\n)"),  # after any line
)


def split_text(text, max_chars, _level=0):
    """Split text into pieces of at most max_chars, at headings where possible.

    Joining the pieces gives the original text back.
    """
    if len(text) <= max_chars:
        return [text]
    if _level >= len(_SPLIT_POINTS):
        return [text[i : i + max_chars] for i in range(0, len(text), max_chars)]
    pieces, current = [], ""
    for unit in (u for u in _SPLIT_POINTS[_level].split(text) if u):
        if len(unit) > max_chars:
            if current:
                pieces.append(current)
                current = ""
            pieces.extend(split_text(unit, max_chars, _level + 1))
        elif len(current) + len(unit) > max_chars:
            pieces.append(current)
            current = unit
        else:
            current += unit
    if current:
        pieces.append(current)
    return pieces


def build_states(pages, page_texts, max_chars=MAX_STATE_CHARS):
    """The `state` values to send for one set of cited pages: one, or several if long."""
    if sum(len(page_texts[p]) for p in pages) <= max_chars:
        return [{"source_pages": [{"path": p, "text": page_texts[p]} for p in pages]}]
    states, current, size = [], [], 0
    for page in pages:
        pieces = split_text(page_texts[page], max_chars)
        for i, piece in enumerate(pieces, 1):
            if current and size + len(piece) > max_chars:
                states.append({"source_pages": current})
                current, size = [], 0
            entry = {"path": page}
            if len(pieces) > 1:
                entry["part"] = "%d of %d" % (i, len(pieces))
            entry["text"] = piece
            current.append(entry)
            size += len(piece)
    if current:
        states.append({"source_pages": current})
    return states


def _plain(text):
    return text.replace("**", "")


def build_question(statement):
    """One Choice question. Digest headings are left out: the model judged them as facts."""
    instructions = {"question": QUESTION, "statement": _plain(statement.text)}
    if statement.context:
        instructions["lines_above_the_statement"] = [_plain(c) for c in statement.context]
    return {"type": "choice", "instructions": instructions, "criteria": dict(CRITERIA)}


def estimate_tokens(value):
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
    return math.ceil(len(text) / CHARS_PER_TOKEN)


def cache_key(model, question, state):
    """Hash of the model, the question (wording and statement) and the page text."""
    blob = json.dumps([model, question, state], sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:32]


def review_key(statement, page_texts):
    """Identifies a statement and the page text it was checked against, for reviewed.json.

    It does not depend on the line number, the model or the question wording, so an
    accepted flag stays accepted until the statement or the cited page changes.
    """
    if any(p not in page_texts for p in statement.pages):
        return None
    blob = json.dumps([statement.text, statement.context, [[p, page_texts[p]] for p in statement.pages]],
                      ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def pack_batches(sizes, state_tokens, request_budget=REQUEST_TOKEN_BUDGET,
                 question_budget=QUESTION_TOKEN_BUDGET, max_questions=MAX_QUESTIONS):
    """Group questions into requests. Returns lists of indexes into sizes.

    Every request carries the page once (state_tokens) plus its questions.
    """
    batches, current, used = [], [], state_tokens
    for index, size in enumerate(sizes):
        if state_tokens + size > min(question_budget, request_budget):
            raise ValueError("a page and one question do not fit in a request (%d tokens)" % (state_tokens + size))
        if current and (used + size > request_budget or len(current) >= max_questions):
            batches.append(current)
            current, used = [], state_tokens
        current.append(index)
        used += size
    if current:
        batches.append(current)
    return batches


@dataclasses.dataclass
class Request:
    body: dict  # what is posted: model, state, questions
    keys: dict  # question id -> cache key
    tokens: int  # estimated input tokens
    digest: str  # digest of the first statement, for the summary table


@dataclasses.dataclass
class Plan:
    requests: list
    keys: list  # per statement: cache keys, one per page part, or None if a page is missing


def plan_requests(statements, page_texts, model, cache, max_state_chars=MAX_STATE_CHARS,
                  request_budget=REQUEST_TOKEN_BUDGET, question_budget=QUESTION_TOKEN_BUDGET,
                  max_questions=MAX_QUESTIONS):
    """Work out which requests are needed for everything the cache cannot answer."""
    groups = collections.OrderedDict()
    for index, statement in enumerate(statements):
        groups.setdefault(statement.pages, []).append(index)
    keys = [None] * len(statements)
    requests = []
    for pages, indexes in groups.items():
        if any(p not in page_texts for p in pages):
            continue
        for index in indexes:
            keys[index] = []
        for state in build_states(pages, page_texts, max_state_chars):
            pending = collections.OrderedDict()
            for index in indexes:
                question = build_question(statements[index])
                key = cache_key(model, question, state)
                keys[index].append(key)
                if key not in cache and key not in pending:
                    pending[key] = question
            if not pending:
                continue
            order = list(pending)
            sizes = [estimate_tokens(pending[k]) for k in order]
            state_tokens = estimate_tokens(state)
            for batch in pack_batches(sizes, state_tokens, request_budget, question_budget, max_questions):
                ids = {"q%d" % n: order[i] for n, i in enumerate(batch)}
                body = {"model": model, "state": state, "questions": {q: pending[k] for q, k in ids.items()}}
                tokens = state_tokens + sum(sizes[i] for i in batch)
                requests.append(Request(body, ids, tokens, statements[indexes[0]].digest))
    return Plan(requests, keys)


# --------------------------------------------------------------------------
# Verdicts
# --------------------------------------------------------------------------


def combine(answers, threshold=AUTO_ACCEPT):
    """One verdict and confidence from the answers for each part of a page."""
    if len(answers) == 1:
        return answers[0]["choice"], answers[0]["confidence"]

    def best(choice, clear):
        found = [a["confidence"] for a in answers
                 if a["choice"] == choice and (a["confidence"] >= threshold or not clear)]
        return max(found) if found else None

    for choice, clear in (("contradicts", True), ("supports", True), ("supports", False), ("contradicts", False)):
        confidence = best(choice, clear)
        if confidence is not None:
            return choice, confidence
    return "not_mentioned", min(a["confidence"] for a in answers)


def is_flagged(verdict, confidence, threshold=AUTO_ACCEPT):
    """A verdict other than supports, or low confidence, needs a reader."""
    return verdict != "supports" or confidence is None or confidence < threshold


# --------------------------------------------------------------------------
# Calling the API
# --------------------------------------------------------------------------


class ApiError(Exception):
    def __init__(self, status, detail):
        super().__init__("TypeSafe API error %s: %s" % (status, detail))
        self.status = status
        self.detail = detail


def post_request(body, api_key, attempts=6):
    """POST one request to /v1/systemone and return the decoded response."""
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    delay = 2.0
    for attempt in range(1, attempts + 1):
        request = urllib.request.Request(
            API_URL,
            data=data,
            method="POST",
            headers={
                "Authorization": "Bearer " + api_key,
                "Content-Type": "application/json",
                "User-Agent": "digest-verifier/1.0",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", "replace")[:600]
            if error.code in (429, 500, 502, 503, 504, 529) and attempt < attempts:
                wait = error.headers.get("retry-after") if error.headers else None
                time.sleep(float(wait) if wait and wait.replace(".", "", 1).isdigit() else delay)
                delay *= 2
                continue
            raise ApiError(error.code, detail)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as error:
            if attempt < attempts:
                time.sleep(delay)
                delay *= 2
                continue
            raise ApiError("network", str(getattr(error, "reason", error)))


def _ask(request, api_key):
    """Send one request. If the API says it is too long, halve it and try again."""
    try:
        response = post_request(request.body, api_key)
    except ApiError as error:
        too_long = error.status == 400 and "max_tokens" in error.detail
        if not too_long or len(request.keys) < 2:
            raise
        ids = list(request.keys)
        results = []
        for half in (ids[: len(ids) // 2], ids[len(ids) // 2 :]):
            body = dict(request.body, questions={q: request.body["questions"][q] for q in half})
            results.extend(_ask(Request(body, {q: request.keys[q] for q in half}, 0, request.digest), api_key))
        return results
    return [(request, response)]


def run_requests(requests, api_key, cache, workers=8, progress=None):
    """Send every request, store the answers in cache, return usage totals."""
    usage = {"requests": 0, "input_tokens": 0, "output_tokens": 0, "models": set()}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(_ask, request, api_key) for request in requests]
        try:
            for done, future in enumerate(concurrent.futures.as_completed(futures), 1):
                for request, response in future.result():
                    usage["requests"] += 1
                    usage["input_tokens"] += response.get("usage", {}).get("input_tokens") or 0
                    usage["output_tokens"] += response.get("usage", {}).get("output_tokens") or 0
                    usage["models"].add(response.get("model", ""))
                    for question_id, key in request.keys.items():
                        answer = response["answers"][question_id]
                        cache[key] = {
                            "choice": answer["choice"],
                            "confidence": round(answer["confidence"], 4),
                            "probabilities": {v: round(answer["probabilities"].get(v, 0.0), 4) for v in VERDICTS},
                        }
                if progress and (done % 25 == 0 or done == len(futures)):
                    progress("  %d of %d requests done" % (done, len(futures)))
        except BaseException:
            for future in futures:
                future.cancel()
            raise
    usage["models"] = sorted(m for m in usage["models"] if m)
    return usage


def load_cache(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}


def save_cache(path, cache):
    """One entry per line, sorted, so a monthly run gives a small readable diff."""
    lines = ["%s: %s" % (json.dumps(k), json.dumps(cache[k], sort_keys=True)) for k in sorted(cache)]
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text("{\n" + ",\n".join(lines) + "\n}\n", encoding="utf-8")


# --------------------------------------------------------------------------
# Results and report
# --------------------------------------------------------------------------


def _note(entry):
    """A reviewed.json entry is a note, or an object with a "note" field."""
    if isinstance(entry, dict):
        return entry.get("note") or "Accepted."
    return entry or None


def judge(statements, plan, cache, threshold, page_texts=None, reviewed=None):
    rows = []
    for statement, keys in zip(statements, plan.keys):
        key = review_key(statement, page_texts or {})
        if keys is None:
            verdict, confidence, parts = "page_missing", None, []
        else:
            parts = [cache[k] for k in keys]
            verdict, confidence = combine(parts, threshold)
        rows.append({
            "digest": statement.digest,
            "line": statement.line,
            "pages": list(statement.pages),
            "statement": statement.text,
            "section": list(statement.section),
            "context": list(statement.context),
            "verdict": verdict,
            "confidence": confidence,
            "flagged": is_flagged(verdict, confidence, threshold),
            "review_key": key,
            "accepted_note": _note((reviewed or {}).get(key)),
            "answers": parts,
        })
    return rows


def kind(row):
    """How a row is counted in the tables."""
    if not row["flagged"]:
        return "supported"
    return "low_confidence" if row["verdict"] == "supports" else row["verdict"]


KINDS = ("supported", "contradicts", "not_mentioned", "low_confidence", "page_missing")


def count(rows):
    counts = collections.Counter(kind(r) for r in rows)
    totals = {"statements": len(rows), "supported": counts["supported"], "flagged": len(rows) - counts["supported"]}
    totals.update({k: counts[k] for k in KINDS[1:]})
    totals["accepted"] = sum(1 for r in rows if r["flagged"] and r["accepted_note"])
    totals["to_read"] = totals["flagged"] - totals["accepted"]
    return totals


def write_report(path, rows, meta):
    totals = count(rows)
    by_digest = collections.OrderedDict()
    for row in rows:
        by_digest.setdefault(row["digest"], []).append(row)
    out = [
        "# Digest verification report",
        "",
        "Made by `scripts/verify-digests.py`. Each digest statement was checked against the manual page it cites.",
        "A flag means a person or an agent should read the statement against the page. It does not mean the digest is wrong.",
        "",
        "- Date: %s" % meta["date"],
        "- Model: %s (TypeSafe Jev)" % meta["model"],
        "- Flag rule: verdict other than `supports`, or confidence below %.2f" % meta["threshold"],
        "- Statements checked: %d" % totals["statements"],
        "- Supported: %d" % totals["supported"],
        "- Flagged: %d (contradicts %d, not mentioned %d, supports with low confidence %d, cited page missing %d)"
        % (totals["flagged"], totals["contradicts"], totals["not_mentioned"], totals["low_confidence"],
           totals["page_missing"]),
        "- To read: %d. Read before and accepted (see `reviewed.json`): %d" % (totals["to_read"], totals["accepted"]),
        "- Lines not checked: %s" % (", ".join("%s %d" % (k, v) for k, v in sorted(meta["skipped"].items())) or "none"),
        "- This run: %d requests, %d input tokens, %d of %d checks answered from the cache"
        % (meta["requests"], meta["input_tokens"], meta["from_cache"], meta["checks"]),
        "",
        "## Counts per digest",
        "",
        "| Digest | Statements | Supported | Flagged | To read | Contradicts | Not mentioned | Low confidence | Page missing |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for digest, group in by_digest.items():
        c = count(group)
        out.append("| %s | %d | %d | %d | %d | %d | %d | %d | %d |" % (
            digest, c["statements"], c["supported"], c["flagged"], c["to_read"], c["contradicts"],
            c["not_mentioned"], c["low_confidence"], c["page_missing"]))
    sections = (
        ("Flagged statements to read", False,
         "Read each one against its page. If the digest is wrong, fix the digest. If the digest is right, "
         "add the key and a short note to `verification/reviewed.json`."),
        ("Flagged statements read before and accepted", True,
         "A reviewer read these against the page and found the digest correct. They come back here if the "
         "statement or the cited page changes."),
    )
    for title, accepted, intro in sections:
        out += ["", "## %s" % title, "", intro, ""]
        chosen = [r for r in rows if r["flagged"] and bool(r["accepted_note"]) == accepted]
        if not chosen:
            out.append("None.")
        for digest, group in by_digest.items():
            flagged = [r for r in group if r in chosen]
            if not flagged:
                continue
            out += ["### digests/%s" % digest, ""]
            for row in flagged:
                out.append(flag_line(row))
                out.append("  > %s" % row["statement"])
                if accepted:
                    out.append("  Reviewer: %s" % row["accepted_note"])
            out.append("")
    Path(path).write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def flag_line(row):
    confidence = "none" if row["confidence"] is None else "%.2f" % row["confidence"]
    label = "supports, low confidence" if kind(row) == "low_confidence" else row["verdict"].replace("_", " ")
    return "- `digests/%s:%d` cites %s. Verdict: %s. Confidence: %s. Key: `%s`" % (
        row["digest"], row["line"], ", ".join("`%s`" % p for p in row["pages"]), label, confidence,
        row["review_key"])


def print_dry_run(statements, plan, cache, model):
    checks = len({k for keys in plan.keys if keys for k in keys})
    to_ask = sum(len(r.keys) for r in plan.requests)
    tokens = sum(r.tokens for r in plan.requests)
    missing = sorted({p for s, k in zip(statements, plan.keys) if k is None for p in s.pages})
    print("Dry run. Nothing is sent to the API.")
    print("Model: %s" % model)
    print("Statements: %d in %d digests, citing %d different pages"
          % (len(statements), len({s.digest for s in statements}), len({p for s in statements for p in s.pages})))
    print("Checks needed: %d (a statement on a split page is checked once per part; "
          "identical lines are checked once)" % checks)
    print("Answered from the cache: %d" % (checks - to_ask))
    print("To send: %d questions in %d requests" % (to_ask, len(plan.requests)))
    print("Estimated input tokens: %d (about $%.3f at $%.3f per million tokens)"
          % (tokens, tokens / 1e6 * PRICE_PER_MILLION_TOKENS, PRICE_PER_MILLION_TOKENS))
    if missing:
        print("Cited pages not found in the manual copy: %d" % len(missing))
        for page in missing[:20]:
            print("  %s" % page)
    print("")
    print("%-58s %10s %9s %11s" % ("digest", "statements", "requests", "est tokens"))
    per = collections.OrderedDict((s.digest, [0, 0, 0]) for s in statements)
    for s in statements:
        per[s.digest][0] += 1
    for r in plan.requests:
        per[r.digest][1] += 1
        per[r.digest][2] += r.tokens
    for digest, (n, requests, t) in per.items():
        print("%-58s %10d %9d %11d" % (digest, n, requests, t))
    if plan.requests:
        sample = json.loads(json.dumps(plan.requests[0].body))
        for page in sample["state"]["source_pages"]:
            if len(page["text"]) > 600:
                page["text"] = page["text"][:600] + " ... [%d more characters]" % (len(page["text"]) - 600)
        print("")
        print("First request (page text shortened here, sent in full):")
        print("POST %s" % API_URL)
        print(json.dumps(sample, indent=2, ensure_ascii=False))


def main(argv=None):
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--digest", metavar="NAME", help="check one digest, for example assets. Prints the "
                        "result and updates the cache, but leaves report.md and results.json alone")
    parser.add_argument("--dry-run", action="store_true", help="print the plan, a token estimate and the first "
                        "request without calling the API")
    parser.add_argument("--docs", type=Path, default=root / "docs", help="folder holding the manual copy "
                        "(default: docs/ in this repository)")
    parser.add_argument("--digests", type=Path, default=root / "digests", help="folder holding the digests")
    parser.add_argument("--out", type=Path, default=root / "verification", help="folder for the report, "
                        "results and cache")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="TypeSafe model id (default: %(default)s)")
    parser.add_argument("--threshold", type=float, default=AUTO_ACCEPT, help="confidence below this is "
                        "flagged (default: %(default)s)")
    parser.add_argument("--max-page-chars", type=int, default=MAX_STATE_CHARS, help="split cited pages longer "
                        "than this (default: %(default)s)")
    parser.add_argument("--workers", type=int, default=8, help="requests in flight at once (default: %(default)s)")
    args = parser.parse_args(argv)

    if not args.docs.is_dir():
        sys.exit("No manual copy at %s. Run scripts/fetch.sh, or pass --docs <path>." % args.docs)
    known_pages = {"docs/" + p.relative_to(args.docs).as_posix() for p in args.docs.rglob("*.md")}

    statements, skipped = [], collections.Counter()
    for path in list_digests(args.digests, args.digest):
        statements += parse_digest(path.name, path.read_text(encoding="utf-8"), known_pages, skipped)
    page_texts = {}
    for page in sorted({p for s in statements for p in s.pages} & known_pages):
        page_texts[page] = (args.docs / page[len("docs/"):]).read_text(encoding="utf-8")

    cache_path = args.out / "cache.json"
    cache = load_cache(cache_path)
    plan = plan_requests(statements, page_texts, args.model, cache, max_state_chars=args.max_page_chars)

    if args.dry_run:
        print_dry_run(statements, plan, cache, args.model)
        return 0

    usage = {"requests": 0, "input_tokens": 0, "output_tokens": 0, "models": []}
    to_ask = sum(len(r.keys) for r in plan.requests)
    if plan.requests:
        api_key = os.environ.get(API_KEY_VARIABLE, "").strip()
        if not api_key:
            sys.exit("%s is not set. Put your TypeSafe API key in that environment variable and run again. "
                     "Use --dry-run to see the plan without a key." % API_KEY_VARIABLE)
        print("Sending %d questions in %d requests to %s" % (to_ask, len(plan.requests), args.model), flush=True)
        try:
            usage = run_requests(plan.requests, api_key, cache, args.workers,
                                 progress=lambda message: print(message, flush=True))
        except ApiError as error:
            save_cache(cache_path, cache)
            hint = " Check the value of %s." % API_KEY_VARIABLE if error.status == 401 else ""
            sys.exit("Stopped: %s%s Answers received so far are in the cache." % (error, hint))

    used = {k for keys in plan.keys if keys for k in keys}
    if not args.digest:
        cache = {k: v for k, v in cache.items() if k in used}  # drop answers nothing refers to any more
    save_cache(cache_path, cache)

    reviewed = load_cache(args.out / "reviewed.json")
    rows = judge(statements, plan, cache, args.threshold, page_texts, reviewed)
    stale = set(reviewed) - {r["review_key"] for r in rows if r["flagged"]}
    if stale and not args.digest:
        print("%d entries in reviewed.json no longer match a flagged statement and can be removed." % len(stale))
    totals = count(rows)
    print("Used %d requests and %d input tokens (about $%.4f). %d of %d checks came from the cache."
          % (usage["requests"], usage["input_tokens"], usage["input_tokens"] / 1e6 * PRICE_PER_MILLION_TOKENS,
             len(used) - to_ask, len(used)))
    for digest in collections.OrderedDict((r["digest"], 1) for r in rows):
        c = count([r for r in rows if r["digest"] == digest])
        print("%s: %d statements, %d supported, %d flagged, %d to read"
              % (digest, c["statements"], c["supported"], c["flagged"], c["to_read"]))

    if args.digest:
        for row in rows:
            if row["flagged"] and not row["accepted_note"]:
                print(flag_line(row))
                print("  > %s" % row["statement"])
        return 0

    meta = {
        "date": datetime.date.today().isoformat(),
        "model": args.model,
        "threshold": args.threshold,
        "skipped": dict(skipped),
        "requests": usage["requests"],
        "input_tokens": usage["input_tokens"],
        "from_cache": len(used) - to_ask,
        "checks": len(used),
    }
    write_report(args.out / "report.md", rows, meta)
    results = {
        "date": meta["date"],
        "model": args.model,
        "answered_by": usage["models"],
        "threshold": args.threshold,
        "question": {"instructions": QUESTION, "criteria": CRITERIA},
        "totals": totals,
        "digests": {d: count([r for r in rows if r["digest"] == d]) for d in sorted({r["digest"] for r in rows})},
        "lines_not_checked": dict(skipped),
        "this_run": {"requests": usage["requests"], "input_tokens": usage["input_tokens"],
                     "output_tokens": usage["output_tokens"], "checks_from_cache": meta["from_cache"]},
    }
    # Summary first, then one statement per line, so a monthly run gives a readable diff.
    head = json.dumps(results, indent=1, ensure_ascii=False)[:-2]
    body = ",\n".join("  " + json.dumps(row, ensure_ascii=False) for row in rows)
    (args.out / "results.json").write_text(head + ',\n "statements": [\n' + body + "\n ]\n}\n", encoding="utf-8")
    print("Wrote %s and %s" % (args.out / "report.md", args.out / "results.json"))
    print("Total: %d statements, %d supported, %d flagged, %d to read"
          % (totals["statements"], totals["supported"], totals["flagged"], totals["to_read"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
