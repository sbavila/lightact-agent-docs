"""Tests for scripts/verify-digests.py.

Run from the repository root:

    python3 -m unittest discover -s tests

No test calls the TypeSafe API. Network access is replaced with a function
that fails the test if it is ever reached.
"""

import dataclasses
import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("verify_digests", ROOT / "scripts" / "verify-digests.py")
vd = importlib.util.module_from_spec(SPEC)
sys.modules["verify_digests"] = vd
SPEC.loader.exec_module(vd)


def no_network(*args, **kwargs):
    raise AssertionError("a test tried to reach the network")


STANDARD = """# assets

## What this section covers

Which file types can be ingested.
Seven short pages.

## 3D models
`docs/assets/3d-model.md`

- Supported 3D formats: **.fbx** and **.obj**.
- FBX is the preferred format.
- Unclear: the page does not say where the folder is.

## Video, images and image sequences
`docs/assets/video-formats-and-codecs.md`

- Containers: **.mp4** and **.mov**.
- Image sequence rules:
  - All frames must have the same file extension.
  - Numbering must start at 0. Unclear: whether gaps are tolerated.
- A single image file is treated as a video file with one frame.

## For automation and pipelines

- Deliverable formats to target: video as .mov or .mp4.
- Per `docs/assets/audio-files.md`, audio is stereo only.
- Compare `docs/assets/3d-model.md` with `docs/assets/audio-files.md`.
"""


class StandardDigestTests(unittest.TestCase):
    def setUp(self):
        self.statements = vd.parse_digest("assets.md", STANDARD)
        self.by_text = {s.text: s for s in self.statements}

    def test_pairs_each_bullet_with_the_page_under_its_heading(self):
        s = self.by_text["Supported 3D formats: **.fbx** and **.obj**."]
        self.assertEqual(s.pages, ("docs/assets/3d-model.md",))
        self.assertEqual(s.digest, "assets.md")
        self.assertEqual(s.line, 11)
        self.assertEqual(s.section, ("3D models",))
        self.assertEqual(s.context, ())
        s = self.by_text["Containers: **.mp4** and **.mov**."]
        self.assertEqual(s.pages, ("docs/assets/video-formats-and-codecs.md",))

    def test_skips_the_opening_summary(self):
        texts = " ".join(self.by_text)
        self.assertNotIn("Which file types", texts)
        self.assertNotIn("Seven short pages", texts)

    def test_skips_lines_starting_unclear(self):
        self.assertFalse([t for t in self.by_text if t.startswith("Unclear")])

    def test_cuts_a_trailing_unclear_note_off_a_statement(self):
        self.assertIn("Numbering must start at 0.", self.by_text)

    def test_a_bullet_ending_in_a_colon_is_context_for_its_children(self):
        self.assertNotIn("Image sequence rules:", self.by_text)
        child = self.by_text["All frames must have the same file extension."]
        self.assertEqual(child.section, ("Video, images and image sequences",))
        self.assertEqual(child.context, ("Image sequence rules:",))
        self.assertEqual(child.line, 20)
        after = self.by_text["A single image file is treated as a video file with one frame."]
        self.assertEqual(after.context, ())

    def test_closing_section_lines_count_only_when_they_name_one_page(self):
        self.assertNotIn("Deliverable formats to target: video as .mov or .mp4.", self.by_text)
        s = self.by_text["Per `docs/assets/audio-files.md`, audio is stereo only."]
        self.assertEqual(s.pages, ("docs/assets/audio-files.md",))
        self.assertFalse([t for t in self.by_text if t.startswith("Compare")])

    def test_statement_count(self):
        self.assertEqual(len(self.statements), 7)


INLINE_SUMMARY = """# Quick Start (digest)

What this section covers:
- The content pipeline in one page.
- Core terminology.

Note on names: copied as the manual prints them.

## Content flow
`docs/quick-start/overview-of-content-pipeline.md`
- Content comes in two ways.

### Mappings

- Layers render to 3 types of mappings.

1. Direct mappings.
2. Canvases.

## Empty page
`docs/quick-start/empty.md`
"""


class InlineSummaryTests(unittest.TestCase):
    def setUp(self):
        self.statements = vd.parse_digest("quick-start.md", INLINE_SUMMARY)

    def test_text_before_the_first_cited_heading_is_skipped(self):
        self.assertEqual(
            [s.text for s in self.statements],
            ["Content comes in two ways.", "Layers render to 3 types of mappings.", "Direct mappings.", "Canvases."],
        )

    def test_subheadings_keep_the_page_and_add_context(self):
        s = self.statements[1]
        self.assertEqual(s.pages, ("docs/quick-start/overview-of-content-pipeline.md",))
        self.assertEqual(s.section, ("Content flow", "Mappings"))
        self.assertEqual(s.context, ())

    def test_numbered_items_are_statements(self):
        self.assertEqual(self.statements[2].line, 17)


TABLE = """# api

## LightAct API
`docs/api/lightact-api.md`

38 methods, plus 3 alias names.

Parameters:

| Method | Marker on the page | Supports Undo |
| --- | --- | --- |
| `system.hello` | none | no |
| `project.save` | Mutates state | not marked |

- Default Port: `9899`.
"""


class TableTests(unittest.TestCase):
    def setUp(self):
        self.statements = vd.parse_digest("api.md", TABLE)

    def test_plain_lines_are_statements_and_lead_lines_are_not(self):
        texts = [s.text for s in self.statements]
        self.assertIn("38 methods, plus 3 alias names.", texts)
        self.assertNotIn("Parameters:", texts)

    def test_each_table_row_becomes_one_statement_with_its_headers(self):
        rows = [s for s in self.statements if s.text.startswith("Method:")]
        self.assertEqual(
            [r.text for r in rows],
            [
                "Method: `system.hello`; Marker on the page: none; Supports Undo: no",
                "Method: `project.save`; Marker on the page: Mutates state; Supports Undo: not marked",
            ],
        )
        self.assertEqual([r.line for r in rows], [12, 13])
        self.assertEqual(rows[0].pages, ("docs/api/lightact-api.md",))

    def test_bullets_after_a_table_still_parse(self):
        self.assertEqual(self.statements[-1].text, "Default Port: `9899`.")

    def test_a_plain_line_is_context_for_the_table_and_bullets_under_it(self):
        text = (
            "# api\n\n## LightAct API\n`docs/api/lightact-api.md`\n\n### Layers\n\n"
            "**`layer.list`**: lists all layers.\n\n"
            "| Parameter | Type |\n| --- | --- |\n| `timelineId` | `int` |\n\n"
            "- Response: bare array.\n\n"
            "**`layer.create`**: creates a new layer.\n\n"
            "| Parameter | Type |\n| --- | --- |\n| `name` | `string` |\n"
        )
        parsed = vd.parse_digest("api.md", text)
        self.assertEqual({s.section for s in parsed}, {("LightAct API", "Layers")})
        got = [(s.text, s.context) for s in parsed]
        under = ()
        self.assertEqual(
            got,
            [
                ("**`layer.list`**: lists all layers.", under),
                ("Parameter: `timelineId`; Type: `int`", under + ("**`layer.list`**: lists all layers.",)),
                ("Response: bare array.", under + ("**`layer.list`**: lists all layers.",)),
                ("**`layer.create`**: creates a new layer.", under),
                ("Parameter: `name`; Type: `string`", under + ("**`layer.create`**: creates a new layer.",)),
            ],
        )


NODE_REFERENCE = """# Node reference (digest)

## How to read this digest

- All source paths are under `docs/node-reference/node-reference/`. Each node gives its file name in backticks.
- "In" = the page's "Default inputs", "Out" = "Default outputs", "Types" = "Supported types", "kw" = the page's "Search keywords".

---

# Layout nodes

`layout-nodes.md` lists 14 categories, in this order.

## Lifeline and actions
`layout-nodes/lifeline-and-actions-node-category/`

- **Sequence** (`fork.md`): Splits lifeline impulse. In: Lifeline. Out: Lifeline. kw: fork.
- **Run every** (`run-every.md`): Runs on a set interval. In: Float. Unclear: interval unit not stated.
- Color to texture is filed here, not under Texture generators.
- Unclear: Timeline play points to a deprecated node.

## Data I/O
`layout-nodes/data-io-node-category/`

### UDP
`.../udp-node-category/`

- **Send UDP** (`send-udp.md`): In: Lifeline, Device, String. Out: Lifeline.

# Device nodes

## Content I/O (devices)
`device-nodes/content-io-node-category/`

### Video
`.../video-node-category/` (subfolders `ndi-`, `spout-node-category/`)

- **NDI receiver** (`ndi-receiver-device.md`): Receives an NDI stream. kw: read.

## Deprecated nodes (all in one place)

- Lifeline and actions: Set layer state.

## For automation and pipelines

- This section is a catalogue, not a spec.
"""

NODE_PAGES = {
    "docs/node-reference/node-reference/layout-nodes.md",
    "docs/node-reference/node-reference/layout-nodes/lifeline-and-actions-node-category.md",
    "docs/node-reference/node-reference/layout-nodes/lifeline-and-actions-node-category/fork.md",
    "docs/node-reference/node-reference/layout-nodes/lifeline-and-actions-node-category/run-every.md",
    "docs/node-reference/node-reference/layout-nodes/data-io-node-category.md",
    "docs/node-reference/node-reference/layout-nodes/data-io-node-category/udp-node-category.md",
    "docs/node-reference/node-reference/layout-nodes/data-io-node-category/udp-node-category/send-udp.md",
    "docs/node-reference/node-reference/device-nodes/content-io-node-category/video-node-category.md",
    "docs/node-reference/node-reference/device-nodes/content-io-node-category/video-node-category/ndi-node-category.md",
    "docs/node-reference/node-reference/device-nodes/content-io-node-category/video-node-category/ndi-node-category/ndi-receiver-device.md",
}


class NodeReferenceTests(unittest.TestCase):
    def setUp(self):
        self.statements = vd.parse_digest("node-reference.md", NODE_REFERENCE, NODE_PAGES)
        self.by_line = {s.line: s for s in self.statements}

    def test_a_node_bullet_cites_its_own_page(self):
        s = self.by_line[17]
        self.assertEqual(
            s.pages,
            ("docs/node-reference/node-reference/layout-nodes/lifeline-and-actions-node-category/fork.md",),
        )

    def test_node_lines_lose_the_file_name_and_abbreviations_are_written_out(self):
        self.assertEqual(
            self.by_line[17].text,
            "Sequence: Splits lifeline impulse. Default inputs: Lifeline. "
            "Default outputs: Lifeline. Search keywords: fork.",
        )
        self.assertEqual(
            self.by_line[18].text, "Run every: Runs on a set interval. Default inputs: Float."
        )

    def test_a_bullet_without_a_file_cites_the_category_page(self):
        self.assertEqual(
            self.by_line[19].pages,
            ("docs/node-reference/node-reference/layout-nodes/lifeline-and-actions-node-category.md",),
        )

    def test_relative_folders_hang_off_the_parent_heading(self):
        self.assertEqual(
            self.by_line[28].pages,
            ("docs/node-reference/node-reference/layout-nodes/data-io-node-category/udp-node-category/send-udp.md",),
        )
        self.assertEqual(self.by_line[28].section, ("Data I/O", "UDP"))

    def test_a_file_in_a_subfolder_is_found_by_name(self):
        self.assertEqual(
            self.by_line[38].pages,
            ("docs/node-reference/node-reference/device-nodes/content-io-node-category/video-node-category/"
             "ndi-node-category/ndi-receiver-device.md",),
        )

    def test_a_plain_line_that_opens_with_a_file_name_cites_that_file(self):
        s = self.by_line[12]
        self.assertEqual(s.pages, ("docs/node-reference/node-reference/layout-nodes.md",))

    def test_sections_without_a_source_are_skipped(self):
        self.assertEqual(sorted(self.by_line), [12, 17, 18, 19, 28, 38])


CHANGELOG = """# Release changelogs

## How are Changelogs generated
`docs/release-changelogs/how-are-changelogs-generated.md`

- Generated semi-automatically.

---

## LightAct 4.17
`docs/release-changelogs/lightact-4.17.md` (index, links only)

Pages read:
- `docs/release-changelogs/lightact-4.17/lightact-4.17.0.md`: 18 November 2026, 1 Epic, 6 upgrades. Tag [0].
- `docs/release-changelogs/lightact-4.17/lightact-4.17.rc1.md`: "There were no new features introduced in this version."
- `docs/release-changelogs/lightact-4.17/lightact-4.17.b1.md`: 23 October 2026, 9 Epics, 67 upgrades. [B1]
- No ticket repeats across the three pages.

### Crossfade
- LA4-7358 [B1]: layer crossfade controls removed.
- LA4-7287 [B1]: layer grouping. LA4-7526 [0]: new layers land above a group.
- LA4-6865 [B1, 0]: Timeline no longer has crossfade properties.
- LA4-7331: connections can span timelines.
- LA4-6636 [B1]: CueXYZ rules. Examples as written:
  - 5,-1,-1: DMX needs X=5.

## LightAct 4.16
`docs/release-changelogs/lightact-4.16.md` (index, links only)

Pages read:
- `docs/release-changelogs/lightact-4.16/lightact-4.16.b1.md`: 20 July 2026. [B1]

### Nodes
- LA4-1 [B1]: a new node.
"""

V417 = "docs/release-changelogs/lightact-4.17/lightact-4.17."


class ChangelogTests(unittest.TestCase):
    def setUp(self):
        self.statements = vd.parse_digest("release-changelogs.md", CHANGELOG)
        self.by_line = {s.line: s for s in self.statements}

    def test_ordinary_sections_still_work(self):
        self.assertEqual(self.by_line[6].pages, ("docs/release-changelogs/how-are-changelogs-generated.md",))

    def test_a_bullet_that_opens_with_a_page_path_is_about_that_page(self):
        s = self.by_line[14]
        self.assertEqual(s.pages, (V417 + "0.md",))
        self.assertEqual(s.text, "18 November 2026, 1 Epic, 6 upgrades.")
        self.assertEqual(self.by_line[15].pages, (V417 + "rc1.md",))
        self.assertEqual(self.by_line[16].text, "23 October 2026, 9 Epics, 67 upgrades.")

    def test_a_tag_points_a_bullet_at_the_build_page(self):
        self.assertEqual(self.by_line[20].pages, (V417 + "b1.md",))
        self.assertEqual(self.by_line[20].section, ("LightAct 4.17", "Crossfade"))
        self.assertEqual(self.by_line[20].context, ())

    def test_two_tags_cite_two_pages(self):
        self.assertEqual(self.by_line[21].pages, (V417 + "b1.md", V417 + "0.md"))
        self.assertEqual(self.by_line[22].pages, (V417 + "b1.md", V417 + "0.md"))

    def test_an_untagged_bullet_cites_every_build_page_of_the_version(self):
        expected = (V417 + "0.md", V417 + "rc1.md", V417 + "b1.md")
        self.assertEqual(self.by_line[23].pages, expected)
        self.assertEqual(self.by_line[17].pages, expected)

    def test_children_inherit_the_tag_of_their_parent(self):
        self.assertNotIn(24, self.by_line)
        self.assertEqual(self.by_line[25].pages, (V417 + "b1.md",))
        self.assertEqual(self.by_line[25].context, ("LA4-6636 [B1]: CueXYZ rules. Examples as written:",))

    def test_tags_do_not_leak_into_the_next_version(self):
        self.assertEqual(
            self.by_line[34].pages, ("docs/release-changelogs/lightact-4.16/lightact-4.16.b1.md",)
        )


class IndexTests(unittest.TestCase):
    def test_a_file_with_no_cited_pages_gives_no_statements(self):
        text = "# Index\n\n## By question\n\n- API calls: `api.md`\n- Assets: `assets.md`\n"
        self.assertEqual(vd.parse_digest("INDEX.md", text), [])

    def test_the_index_is_not_listed_as_a_digest(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in ("INDEX.md", "assets.md", "api.md", "notes.txt"):
                Path(tmp, name).write_text("x")
            self.assertEqual([p.name for p in vd.list_digests(Path(tmp))], ["api.md", "assets.md"])
            self.assertEqual([p.name for p in vd.list_digests(Path(tmp), "assets")], ["assets.md"])
            self.assertEqual([p.name for p in vd.list_digests(Path(tmp), "assets.md")], ["assets.md"])
            with self.assertRaises(SystemExit):
                vd.list_digests(Path(tmp), "nope")


class SplitTextTests(unittest.TestCase):
    def test_a_short_page_is_one_piece(self):
        self.assertEqual(vd.split_text("# A\n\nshort\n", 100), ["# A\n\nshort\n"])

    def test_a_long_page_splits_at_headings_and_loses_nothing(self):
        sections = ["## Part %d\n\n%s\n\n" % (i, "word " * 40) for i in range(10)]
        text = "# Title\n\nintro\n\n" + "".join(sections)
        pieces = vd.split_text(text, 600)
        self.assertGreater(len(pieces), 1)
        self.assertEqual("".join(pieces), text)
        for piece in pieces:
            self.assertLessEqual(len(piece), 600)
        for piece in pieces[1:]:
            self.assertTrue(piece.startswith("## Part"), piece[:20])

    def test_a_section_longer_than_the_limit_splits_at_paragraphs_then_lines(self):
        text = "## Big\n\n" + "\n\n".join("para %d " % i + "x" * 80 for i in range(20)) + "\n"
        pieces = vd.split_text(text, 300)
        self.assertEqual("".join(pieces), text)
        self.assertTrue(all(len(p) <= 300 for p in pieces))
        one_line = "y" * 1000
        pieces = vd.split_text(one_line, 300)
        self.assertEqual("".join(pieces), one_line)
        self.assertTrue(all(len(p) <= 300 for p in pieces))


class PackBatchesTests(unittest.TestCase):
    def test_everything_in_one_request_when_it_fits(self):
        self.assertEqual(vd.pack_batches([10, 10, 10], state_tokens=100, request_budget=1000), [[0, 1, 2]])

    def test_a_new_request_starts_when_the_budget_is_full(self):
        batches = vd.pack_batches([40, 40, 40, 40, 40], state_tokens=100, request_budget=200)
        self.assertEqual(batches, [[0, 1], [2, 3], [4]])

    def test_the_question_count_cap_applies(self):
        batches = vd.pack_batches([1] * 7, state_tokens=10, request_budget=1000, max_questions=3)
        self.assertEqual(batches, [[0, 1, 2], [3, 4, 5], [6]])

    def test_every_question_is_asked_exactly_once(self):
        sizes = [(i * 37) % 90 + 5 for i in range(200)]
        batches = vd.pack_batches(sizes, state_tokens=300, request_budget=1000, max_questions=40)
        self.assertEqual(sorted(i for b in batches for i in b), list(range(200)))
        for b in batches:
            self.assertLessEqual(300 + sum(sizes[i] for i in b), 1000)
            self.assertLessEqual(len(b), 40)

    def test_a_question_that_cannot_fit_with_the_page_is_refused(self):
        with self.assertRaises(ValueError):
            vd.pack_batches([10, 950], state_tokens=100, request_budget=2000, question_budget=1000)
        with self.assertRaises(ValueError):
            vd.pack_batches([10], state_tokens=100, request_budget=105)

    def test_default_budgets_sit_inside_the_documented_limits(self):
        self.assertLess(vd.REQUEST_TOKEN_BUDGET, 64_000)
        self.assertLess(vd.QUESTION_TOKEN_BUDGET, 32_000)


def statement(text, pages=("docs/a.md",), line=1, context=(), digest="d.md", section=("Title",)):
    return vd.Statement(digest=digest, line=line, text=text, section=section, context=context, pages=pages)


class PlanTests(unittest.TestCase):
    def setUp(self):
        self.pages = {"docs/a.md": "# A\n\nAlpha is 1.\n", "docs/b.md": "# B\n\nBeta is 2.\n"}
        self.statements = [
            statement("Alpha is 1.", line=1),
            statement("Alpha is 3.", line=2),
            statement("Beta is 2.", pages=("docs/b.md",), line=3),
            statement("Gone.", pages=("docs/missing.md",), line=4),
        ]

    def plan(self, cache=None, **kwargs):
        return vd.plan_requests(self.statements, self.pages, "jev-test", cache or {}, **kwargs)

    def test_statements_for_one_page_share_one_request(self):
        plan = self.plan()
        self.assertEqual(len(plan.requests), 2)
        first = plan.requests[0]
        self.assertEqual(len(first.body["questions"]), 2)
        self.assertEqual(first.body["state"], {"source_pages": [{"path": "docs/a.md", "text": self.pages["docs/a.md"]}]})

    def test_request_body_follows_the_documented_shape(self):
        body = self.plan().requests[0].body
        self.assertEqual(set(body), {"model", "state", "questions"})
        self.assertEqual(body["model"], "jev-test")
        for question in body["questions"].values():
            self.assertEqual(question["type"], "choice")
            self.assertEqual(list(question["criteria"]), ["supports", "contradicts", "not_mentioned"])
            self.assertIn("statement", question["instructions"])
        json.dumps(body)

    def test_digest_headings_are_not_sent_but_parent_lines_are(self):
        self.statements = [statement("All frames share one extension.", context=("Image sequence rules:",),
                                     section=("Video and images",))]
        question = self.plan().requests[0].body["questions"]["q0"]
        sent = json.dumps(question)
        self.assertNotIn("Video and images", sent)
        self.assertIn("Image sequence rules:", sent)
        self.assertEqual(question["instructions"]["statement"], "All frames share one extension.")

    def test_a_missing_page_is_reported_and_not_sent(self):
        plan = self.plan()
        self.assertEqual(plan.keys[3], None)
        sent = json.dumps([r.body for r in plan.requests])
        self.assertNotIn("Gone.", sent)

    def test_cached_statements_are_not_sent_again(self):
        plan = self.plan()
        cache = {key: {"choice": "supports"} for key in plan.keys[0] + plan.keys[2]}
        again = self.plan(cache)
        self.assertEqual(len(again.requests), 1)
        self.assertEqual(len(again.requests[0].body["questions"]), 1)
        full = {key: {} for keys in plan.keys if keys for key in keys}
        self.assertEqual(self.plan(full).requests, [])

    def test_the_review_key_follows_statement_and_page_but_not_the_model(self):
        first = vd.review_key(self.statements[0], self.pages)
        self.assertNotEqual(first, vd.review_key(self.statements[1], self.pages))
        self.assertEqual(first, vd.review_key(dataclasses.replace(self.statements[0], line=99), self.pages))
        self.pages["docs/a.md"] += "More.\n"
        self.assertNotEqual(first, vd.review_key(self.statements[0], self.pages))
        self.assertIsNone(vd.review_key(self.statements[3], self.pages))

    def test_the_cache_key_follows_statement_page_and_model(self):
        base = self.plan().keys
        self.assertNotEqual(base[0], base[1])
        self.pages["docs/a.md"] += "More.\n"
        changed = self.plan().keys
        self.assertNotEqual(base[0], changed[0])
        self.assertEqual(base[2], changed[2])
        other_model = vd.plan_requests(self.statements, self.pages, "jev-other", {}).keys
        self.assertNotEqual(changed[2], other_model[2])

    def test_a_long_page_is_split_and_each_part_is_asked(self):
        self.pages["docs/a.md"] = "".join("## S%d\n\n%s\n\n" % (i, "w " * 100) for i in range(6))
        plan = self.plan(max_state_chars=500)
        parts = [r for r in plan.requests if r.body["state"]["source_pages"][0]["path"] == "docs/a.md"]
        self.assertGreater(len(parts), 1)
        self.assertEqual(len(plan.keys[0]), len(parts))
        joined = "".join(r.body["state"]["source_pages"][0]["text"] for r in parts)
        self.assertEqual(joined, self.pages["docs/a.md"])
        self.assertIn("part", parts[0].body["state"]["source_pages"][0])

    def test_requests_respect_the_token_budget(self):
        self.statements = [statement("Fact number %d about alpha." % i, line=i) for i in range(60)]
        plan = self.plan(request_budget=1500)
        self.assertGreater(len(plan.requests), 1)
        asked = [q for r in plan.requests for q in r.body["questions"]]
        self.assertEqual(len(asked), 60)
        for r in plan.requests:
            self.assertLessEqual(vd.estimate_tokens(r.body["state"]) + sum(
                vd.estimate_tokens(q) for q in r.body["questions"].values()), 1500)

    def test_two_cited_pages_travel_together(self):
        self.statements = [statement("Alpha and beta.", pages=("docs/a.md", "docs/b.md"))]
        plan = self.plan()
        self.assertEqual([p["path"] for p in plan.requests[0].body["state"]["source_pages"]], ["docs/a.md", "docs/b.md"])


class VerdictTests(unittest.TestCase):
    def answer(self, choice, confidence):
        return {"choice": choice, "confidence": confidence, "probabilities": {}}

    def test_single_answer_passes_through(self):
        self.assertEqual(vd.combine([self.answer("supports", 0.95)], 0.8), ("supports", 0.95))
        self.assertEqual(vd.combine([self.answer("contradicts", 0.6)], 0.8), ("contradicts", 0.6))

    def test_any_part_that_clearly_supports_settles_a_split_page(self):
        answers = [self.answer("not_mentioned", 0.99), self.answer("supports", 0.9)]
        self.assertEqual(vd.combine(answers, 0.8), ("supports", 0.9))

    def test_a_clear_contradiction_in_any_part_wins(self):
        answers = [self.answer("supports", 0.9), self.answer("contradicts", 0.85)]
        self.assertEqual(vd.combine(answers, 0.8), ("contradicts", 0.85))

    def test_no_support_anywhere_is_not_mentioned_at_the_weakest_confidence(self):
        answers = [self.answer("not_mentioned", 0.99), self.answer("not_mentioned", 0.7)]
        self.assertEqual(vd.combine(answers, 0.8), ("not_mentioned", 0.7))

    def test_flagging_follows_the_cookbook(self):
        self.assertFalse(vd.is_flagged("supports", 0.8, 0.8))
        self.assertTrue(vd.is_flagged("supports", 0.79, 0.8))
        self.assertTrue(vd.is_flagged("contradicts", 0.99, 0.8))
        self.assertTrue(vd.is_flagged("not_mentioned", 0.99, 0.8))
        self.assertTrue(vd.is_flagged("page_missing", None, 0.8))


class CommandLineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        (root / "digests").mkdir()
        (root / "docs" / "assets").mkdir(parents=True)
        (root / "digests" / "assets.md").write_text(STANDARD)
        (root / "digests" / "INDEX.md").write_text("# Index\n")
        for name in ("3d-model", "video-formats-and-codecs", "audio-files"):
            (root / "docs" / "assets" / (name + ".md")).write_text("# %s\n\nSome text.\n" % name)
        self.root = root
        self.argv = ["--digests", str(root / "digests"), "--docs", str(root / "docs"), "--out", str(root / "verification")]
        patcher = mock.patch.object(vd.urllib.request, "urlopen", no_network)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self.tmp.cleanup)

    def run_main(self, *extra, env=None):
        out, err = io.StringIO(), io.StringIO()
        code = 0
        with mock.patch.dict(os.environ, env or {}, clear=True), redirect_stdout(out), redirect_stderr(err):
            try:
                code = vd.main(self.argv + list(extra)) or 0
            except SystemExit as exc:
                code = exc.code
        return code, out.getvalue(), err.getvalue()

    def test_missing_key_stops_with_a_clear_message_before_any_call(self):
        code, out, err = self.run_main()
        self.assertNotEqual(code, 0)
        self.assertIn("TYPESAFE_API_KEY", str(code) + err)
        self.assertFalse((self.root / "verification" / "report.md").exists())

    def test_dry_run_needs_no_key_and_prints_the_plan(self):
        code, out, err = self.run_main("--dry-run")
        self.assertEqual(code, 0)
        self.assertIn("requests", out)
        self.assertIn("tokens", out)
        self.assertIn('"type": "choice"', out)
        self.assertFalse((self.root / "verification").exists())

    def test_the_key_never_appears_in_output_or_files(self):
        secret = "sk-test-do-not-print-0123456789"
        code, out, err = self.run_main("--dry-run", env={"TYPESAFE_API_KEY": secret})
        self.assertNotIn(secret, out + err)

    def test_a_full_run_writes_report_results_and_cache(self):
        def fake_post(body, api_key):
            answers = {}
            for qid, question in body["questions"].items():
                wrong = "preferred" in json.dumps(question["instructions"])
                answers[qid] = {
                    "type": "choice",
                    "choice": "contradicts" if wrong else "supports",
                    "confidence": 0.97,
                    "probabilities": {"supports": 0.02 if wrong else 0.98, "contradicts": 0.98 if wrong else 0.01,
                                      "not_mentioned": 0.0 if wrong else 0.01},
                }
            return {"model": "jev-test-1", "answers": answers, "usage": {"input_tokens": 100, "output_tokens": 5}}

        secret = "sk-test-do-not-print-0123456789"
        with mock.patch.object(vd, "post_request", side_effect=fake_post) as post:
            code, out, err = self.run_main(env={"TYPESAFE_API_KEY": secret})
            self.assertEqual(code, 0, err)
            first_calls = post.call_count
            self.assertEqual(first_calls, 3)
            out_dir = self.root / "verification"
            report = (out_dir / "report.md").read_text()
            results = json.loads((out_dir / "results.json").read_text())
            self.assertTrue((out_dir / "cache.json").exists())
            self.assertEqual(results["totals"]["statements"], 7)
            self.assertEqual(results["totals"]["flagged"], 1)
            self.assertIn("digests/assets.md:12", report)
            self.assertIn("docs/assets/3d-model.md", report)
            self.assertIn("contradicts", report)
            self.assertIn("0.97", report)
            for path in out_dir.iterdir():
                self.assertNotIn(secret, path.read_text())
            self.assertNotIn(secret, out + err)
            # A second run is answered from the cache: no calls, no key needed.
            code, out, err = self.run_main()
            self.assertEqual(code, 0, err)
            self.assertEqual(post.call_count, first_calls)
            self.assertIn("To read: 1", (out_dir / "report.md").read_text())

            # A flag a reviewer has accepted moves to its own list, with the note.
            flagged = [r for r in results["statements"] if r["flagged"]]
            self.assertIn(flagged[0]["review_key"], report)
            (out_dir / "reviewed.json").write_text(json.dumps({
                flagged[0]["review_key"]: {"digest": "assets.md", "note": "Checked: the page says so."},
                "0000000000000000": "An entry that matches nothing is ignored.",
            }))
            code, out, err = self.run_main()
            self.assertEqual(code, 0, err)
            report = (out_dir / "report.md").read_text()
            results = json.loads((out_dir / "results.json").read_text())
            self.assertIn("To read: 0", report)
            self.assertIn("Checked: the page says so.", report)
            self.assertEqual(results["totals"]["flagged"], 1)
            self.assertEqual(results["totals"]["accepted"], 1)
            self.assertEqual(results["totals"]["to_read"], 0)

            # The acceptance lapses when the cited page changes.
            page = self.root / "docs" / "assets" / "3d-model.md"
            page.write_text(page.read_text() + "\nA new line.\n")
            code, out, err = self.run_main(env={"TYPESAFE_API_KEY": secret})
            self.assertEqual(code, 0, err)
            self.assertIn("To read: 1", (out_dir / "report.md").read_text())

    def test_one_digest_run_leaves_the_full_report_alone(self):
        def fake_post(body, api_key):
            return {
                "model": "jev-test-1",
                "answers": {q: {"type": "choice", "choice": "supports", "confidence": 1.0,
                                "probabilities": {"supports": 1.0, "contradicts": 0.0, "not_mentioned": 0.0}}
                            for q in body["questions"]},
                "usage": {"input_tokens": 10, "output_tokens": 1},
            }

        with mock.patch.object(vd, "post_request", side_effect=fake_post):
            code, out, err = self.run_main("--digest", "assets", env={"TYPESAFE_API_KEY": "k"})
        self.assertEqual(code, 0, err)
        self.assertTrue((self.root / "verification" / "cache.json").exists())
        self.assertFalse((self.root / "verification" / "report.md").exists())
        self.assertIn("7 statements", out)


if __name__ == "__main__":
    unittest.main()
