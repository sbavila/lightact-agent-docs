# LightAct docs for agents

A local copy of the LightAct 4 media server manual, plus digests, so agents can answer LightAct questions without crawling the website.

Source: https://docs.lightact.com (index at `/llms.txt`; every page is served as markdown when `.md` is added to its URL). This is LightAct's documentation, copied for private reference. It is not ours to republish.

## How to use it

0. If there is no `docs/` folder, run `scripts/fetch.sh` once. It copies the manual from the live site and takes about a minute. The manual is not stored in this repository.
1. Read `digests/INDEX.md`. It says which digest covers what.
2. Read the digest for your topic in `digests/`. Each digest has one heading per manual page with the source path under it.
3. When you need exact wording or a detail the digest left out, open the page in `docs/`, or search it: `grep -ril "asset version" docs/`.
4. Treat `docs/` as the authority. A digest is a summary written by an agent and can be wrong or out of date.

## Layout

- `docs/` : the manual, one folder per section, one markdown file per page. Not in git; made by `scripts/fetch.sh`. Images and GitBook tags are stripped. `docs/llms.txt` is the live index at the date of the copy.
- `FETCHED` and `manifest.sha256` : the date the digests were last checked against the live manual, and a checksum of every page at that date. After a refresh, `git diff manifest.sha256` lists the pages that changed since the digests were written.
- `digests/` : one digest per section, and `INDEX.md`.
- `scripts/fetch.sh` : refreshes `docs/` from the live site. It overwrites pages in place and deletes nothing; pages removed upstream are listed in `docs/STALE.txt`.
- `scripts/digest-brief.md` : the brief used to write the digests. Reuse it when a section changes.
- `scripts/verify-digests.py` : checks every digest line against the manual page it cites, using TypeSafe's Jev model. It needs the `TYPESAFE_API_KEY` environment variable. See "Verification" in the README.
- `verification/` : the last report (`report.md`), every result, the answer cache, and the flags a reviewer has read and accepted (`reviewed.json`).

## Keeping it current

- Check `FETCHED`. If it is more than a month old, or the question is about a release newer than the newest page in `docs/release-changelogs/`, run `scripts/fetch.sh` first.
- After a refresh, `git diff manifest.sha256` shows which pages changed. Read those pages directly; their digests may be behind. Redo only the digests for sections that changed.
- The API page (`docs/api/lightact-api.md`) changes fastest. For API work, read the page itself, not only the digest.
- After redoing a digest, run `python3 scripts/verify-digests.py` and read every line under "Flagged statements to read" in `verification/report.md` against its page. Fix the digest if it is wrong. If it is right, add the key to `verification/reviewed.json` with a note. Do not change a line only because it was flagged.

## Things the manual does not cover

- The plugin format for the 4.18 API (manifest, loading, window size) is not documented as of the copy date.
- If the manual does not say something, tell the person so. Do not fill the gap from memory of other media servers.
