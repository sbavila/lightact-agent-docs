---
name: lightact
description: Use for any question or task about the LightAct media server, including programming a show, layers and layer variables, nodes, timelines and cues, assets and versioning, LightNet clusters, OSC, DMX, the LightAct 4.18 JSON-RPC API and plugins, and designing a content pipeline around LightAct.
---

# LightAct 4

1. Find the checkout from this skill's own location. If a sibling file named `checkout-path` exists, read its first line as the absolute checkout path. Otherwise resolve symlinks in the path to this `SKILL.md` and go up three directories from its containing folder. Verify the checkout has `digests/INDEX.md` and `scripts/fetch.sh`. If the path is broken, ask where the checkout moved.
2. Check `docs/` and the date in the checkout's `FETCHED`. If `docs/` is missing or `FETCHED` is more than a month old, run `./scripts/fetch.sh` from the checkout root. If fetching is unavailable or network access is prohibited, use the local sources and say what you could verify.
3. Read `digests/INDEX.md` and then the matching digests. Open the cited page in `docs/` for exact wording or details the digest leaves out. Always read `docs/api/lightact-api.md` for API questions when available. After a refresh, check the relevant manual pages directly. Treat `docs/` as the authority if it disagrees with a digest.
4. Cite the relevant sources. Never answer LightAct questions from memory. If the manual does not cover something, say so plainly. If you only had access to a digest, say that.
