---
name: lightact
description: Use when a task involves the LightAct media server - programming or reviewing a LightAct show, its layers, layer variables, layer templates, nodes, timelines, sections, markers, cues, assets, asset versioning, LightNet clusters, OSC, DMX or timecode; writing code, tools or plugins against the LightAct JSON-RPC API; designing a content pipeline around LightAct; or translating disguise or Pixera concepts into LightAct.
---

# LightAct

## Overview

LightAct questions get answered from the manual, never from memory. Memory of LightAct is thin and gets mixed up with other media servers, which produces confident wrong answers: node names that do not exist, API parameters that are not there, limits nobody documented.

This skill carries 21 digests of the LightAct 4 manual, one per section. Each digest entry names the manual page it came from.

## Method

1. Read `digests/INDEX.md` in this skill's folder. It maps kinds of question to digests.
2. Read the digest or digests it points to. For tools and pipelines, read each one's closing section, "For automation and pipelines", first.
3. For anything you will state as fact about an exact name, parameter, value or limit, open the manual page the digest cites and check it there. The manual copy is in `docs/` at the repository root (see Finding the files). For the API page, read the whole section for each method you use. If the digest does not have the fact, search the manual before saying it is not covered: `grep -ril "<term>" "$ROOT/docs"`.
4. Say which page each key fact came from.
5. When the manual does not cover something, say "the manual does not say". Mark anything you worked out yourself as an inference.

## Finding the files

`digests/` and `scripts/` in this folder are links into the repository this skill ships in. The manual copy lives beside them:

```sh
# One command, so it works in shells that reset the working directory.
# Replace SKILL_DIR with the folder this SKILL.md is in.
SKILL_DIR="/path/to/this/skill"; ROOT=$(cd "$(dirname "$(realpath "$SKILL_DIR/digests/INDEX.md")")/.." && pwd); echo "$ROOT"; cat "$ROOT/FETCHED"; ls "$ROOT/docs" >/dev/null || (cd "$ROOT" && sh scripts/fetch.sh)
```

`FETCHED` is the date the digests were last checked against the live manual. The manual is not in git; the fetch script copies it and takes about a minute.

- `docs/` missing: run the fetch script from `$ROOT`.
- `FETCHED` more than a month old, or the question is about a release newer than the newest changelog page: run the fetch script, then `git -C "$ROOT" diff manifest.sha256` lists pages that changed since the digests were written. Read those pages directly.
- `digests/` missing (the skill was copied without its links): get the repository from https://github.com/sbavila/lightact-agent-docs and read `digests/` there.
- No network and no `docs/`: answer from the digests and say the exact wording was not checked.

## Quick reference

| Question | Start with |
|---|---|
| API methods, parameters, subscriptions, plugins | `digests/api.md`, then always `docs/api/lightact-api.md` itself |
| Layer templates and their variables, fades, curve editor | `digests/layers-and-layouts.md` |
| One node's pins and properties | `digests/node-reference.md` |
| File formats, codecs, naming, versions, ingestion | `digests/assets.md`, `digests/video-playback.md` |
| Sections, markers, cues, timecode | `digests/timelines.md` |
| Several servers, roles, asset transfer | `digests/lightnet.md` |
| OSC, MIDI, DMX control | `digests/osc-and-midi.md`, `digests/dmx.md` |
| When a feature arrived or changed | `digests/release-changelogs.md` |

Everything else is in the index.

## Common mistakes

| Mistake | What to do |
|---|---|
| Answering from a summary of the API page | The API page changes fastest and its parameter tables matter. Read `docs/api/lightact-api.md` before writing any call. |
| Assuming a layer is "a video clip" as in other servers | A layer is a node graph made from a layer template. Its media, mapping and in and out points are layer variables. Check the template's variable list. |
| Treating an absent feature as a limit | "Not in the manual" and "not possible" are different. Report the first, do not claim the second. |
| Carrying disguise or Pixera behaviour across | Use the transitioning digest for the mapping of terms, then confirm the LightAct behaviour in its own section. |
| Using a layer's name as a stable ID | Auto rename changes layer names from their asset or mapping. |
| Trusting a digest over the page | Digests are summaries written by agents. The page wins. |
