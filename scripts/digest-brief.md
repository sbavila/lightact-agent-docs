You are writing a digest of part of the LightAct 4 media server manual so that other AI agents can use LightAct knowledge without reading the whole manual. Do the work yourself, no subagents.

The manual is mirrored as markdown at docs/ (one folder per manual section, one .md file per page). Your sections: SECTIONS

For each of your sections, write one file: digests/<section-folder-name>.md

Rules:
- Read every page of your sections in full with the Read tool before writing about it. Do not summarise from titles or from a search. If a page is too long for one read, page through it.
- The digest is for an agent that will program LightAct, build tools against its API, or design a content pipeline around it. Keep what such an agent needs: exact names of windows, properties, variables, nodes, pins and settings; exact values, limits, defaults, units; file naming rules; shortcuts; OSC/DMX addresses; step orders that matter; stated limitations and "Good to know" warnings; version numbers where a feature arrived.
- Drop marketing, screenshots references, and repeated boilerplate.
- Never invent or infer facts. If the manual is vague, contradictory or looks out of date, say so in a line starting "Unclear:".
- Use the manual's own terms exactly (for example Primary, Secondary, Layer Layout, Canvas Maps).
- Structure: start the file with a 3 to 6 line "What this section covers" summary, then one "## <page title>" heading per page with the source path in backticks on the next line (for example `docs/assets/asset-versioning.md`), then tight bullet points. Pages with nothing useful get one line.
- Aim for roughly a fifth to a quarter of the source length. Plain English, no em dashes.
- End each file with "## For automation and pipelines": the facts from this section that matter most to someone driving LightAct from code or feeding it content from a database.

Do not edit anything outside digests/. Do not run git commands. Do not touch any network or live system.

Final reply, under 150 words: files written, pages read (count), and up to five things in your sections that would surprise someone building automation around LightAct.
