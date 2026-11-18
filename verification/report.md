# Digest verification report

Made by `scripts/verify-digests.py`. Each digest statement was checked against the manual page it cites.
A flag means a person or an agent should read the statement against the page. It does not mean the digest is wrong.

- Date: 2026-11-18
- Model: jev-1.14.0 (TypeSafe Jev)
- Flag rule: verdict other than `supports`, or confidence below 0.80
- Statements checked: 1880
- Supported: 1720
- Flagged: 160 (contradicts 9, not mentioned 58, supports with low confidence 93, cited page missing 0)
- To read: 0. Read before and accepted (see `reviewed.json`): 160
- Lines not checked: Unclear note 125, opening summary or closing section 274
- This run: 0 requests, 0 input tokens, 2178 of 2178 checks answered from the cache

## Counts per digest

| Digest | Statements | Supported | Flagged | To read | Contradicts | Not mentioned | Low confidence | Page missing |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api.md | 287 | 232 | 55 | 0 | 4 | 21 | 30 | 0 |
| assets.md | 39 | 37 | 2 | 0 | 1 | 0 | 1 | 0 |
| content-mapping.md | 25 | 24 | 1 | 0 | 0 | 0 | 1 | 0 |
| dmx.md | 66 | 62 | 4 | 0 | 0 | 0 | 4 | 0 |
| integrations.md | 53 | 45 | 8 | 0 | 0 | 0 | 8 | 0 |
| layers-and-layouts.md | 283 | 271 | 12 | 0 | 0 | 3 | 9 | 0 |
| licensing.md | 12 | 12 | 0 | 0 | 0 | 0 | 0 | 0 |
| lightnet.md | 85 | 81 | 4 | 0 | 0 | 1 | 3 | 0 |
| lighttrack.md | 21 | 21 | 0 | 0 | 0 | 0 | 0 | 0 |
| miscellaneous.md | 25 | 25 | 0 | 0 | 0 | 0 | 0 | 0 |
| node-reference.md | 275 | 242 | 33 | 0 | 0 | 21 | 12 | 0 |
| osc-and-midi.md | 29 | 25 | 4 | 0 | 0 | 2 | 2 | 0 |
| output-setup.md | 53 | 53 | 0 | 0 | 0 | 0 | 0 | 0 |
| preparing-your-hardware-for-lightact.md | 28 | 28 | 0 | 0 | 0 | 0 | 0 | 0 |
| projection-mapping.md | 73 | 71 | 2 | 0 | 0 | 0 | 2 | 0 |
| quick-start.md | 97 | 94 | 3 | 0 | 0 | 1 | 2 | 0 |
| real-time-content-playback.md | 52 | 49 | 3 | 0 | 0 | 1 | 2 | 0 |
| release-changelogs.md | 225 | 199 | 26 | 0 | 2 | 8 | 16 | 0 |
| timelines.md | 57 | 56 | 1 | 0 | 1 | 0 | 0 | 0 |
| transitioning-to-lightact-from-other-media-servers.md | 37 | 36 | 1 | 0 | 1 | 0 | 0 | 0 |
| video-playback.md | 58 | 57 | 1 | 0 | 0 | 0 | 1 | 0 |

## Flagged statements to read

Read each one against its page. If the digest is wrong, fix the digest. If the digest is right, add the key and a short note to `verification/reviewed.json`.

None.

## Flagged statements read before and accepted

A reviewer read these against the page and found the digest correct. They come back here if the statement or the cited page changes.

### digests/api.md

- `digests/api.md:16` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.77. Key: `155540b89d72fe8b`
  > Name on the page: "LightAct4 Public API v1 Reference Manual".
  Reviewer: Read against the page: the digest line is correct.
- `digests/api.md:45` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.73. Key: `678634bc0e9b2d10`
  > 38 methods, plus 3 alias names (`output.get`, `output.set`, `variable.update`).
  Reviewer: Counted on the page: 38 methods and the 3 alias names.
- `digests/api.md:49` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.19. Key: `7755a59bfc3a5803`
  > Method: `system.hello`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:50` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.16. Key: `877cd176bf7803aa`
  > Method: `system.ping`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:51` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.20. Key: `c014abbc8fd43ae8`
  > Method: `system.performance`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:52` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.22. Key: `9cd9982d6bd5666c`
  > Method: `system.describe`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:53` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.20. Key: `ff611f5cf26ef7f9`
  > Method: `project.getInfo`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:55` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.24. Key: `82d617f20e88a3ea`
  > Method: `timeline.list`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:56` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.76. Key: `af19ab7c3be0aa30`
  > Method: `timeline.play`; Marker on the page: none; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:57` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.74. Key: `0cf1a7ae9c592e23`
  > Method: `timeline.pause`; Marker on the page: none; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:58` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.79. Key: `87d264634ded3aeb`
  > Method: `timeline.stop`; Marker on the page: none; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:59` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.68. Key: `271c0392aff11003`
  > Method: `timeline.seek`; Marker on the page: none; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:60` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.58. Key: `f81791be711ff67b`
  > Method: `timeline.gotoLandmark`; Marker on the page: none; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:61` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.24. Key: `d45733a963cdae7f`
  > Method: `section.list`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:64` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.77. Key: `5d144deffd7fcd0b`
  > Method: `section.delete`; Marker on the page: Mutates state; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:65` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.68. Key: `5a3aae7f8df41274`
  > Method: `section.trigger`; Marker on the page: none; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:66` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.26. Key: `7795b45035d9a661`
  > Method: `layer.list`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:69` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.73. Key: `5226bfd77e6206ca`
  > Method: `layer.delete`; Marker on the page: Mutates state; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:70` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.14. Key: `6a6564c7f2f0f200`
  > Method: `marker.list`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:72` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.74. Key: `4a98c0a06f06b0ea`
  > Method: `marker.update`; Marker on the page: Mutates state; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:73` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.37. Key: `12df34eea9d6d80f`
  > Method: `marker.delete`; Marker on the page: Mutates state; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:74` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.24. Key: `9bd6072315ab8a30`
  > Method: `projector.list`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:76` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.79. Key: `246aed70e16829e0`
  > Method: `projector.update`; Marker on the page: Mutates state; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:78` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.58. Key: `5951782180fa19c4`
  > Method: `output.getMaster` (alias `output.get`); Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:79` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.20. Key: `04b196a8bb034982`
  > Method: `output.setMaster` (alias `output.set`); Marker on the page: none; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:80` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.48. Key: `19cc63c64125785d`
  > Method: `variable.list`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:81` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.56. Key: `48bfbccf709022ca`
  > Method: `variable.get`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:82` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.30. Key: `28c9cc170560e2f8`
  > Method: `variable.set` / `variable.update`; Marker on the page: Mutates state; Supports Undo: not marked
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:83` cites `docs/api/lightact-api.md`. Verdict: contradicts. Confidence: 0.38. Key: `2f996c68028d527b`
  > Method: `undo.undo`; Marker on the page: none; Supports Undo: n/a
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:84` cites `docs/api/lightact-api.md`. Verdict: contradicts. Confidence: 0.34. Key: `d0c4d8c860fe24c1`
  > Method: `undo.redo`; Marker on the page: none; Supports Undo: n/a
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:85` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.53. Key: `051a6f304fa29477`
  > Method: `subscribe`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:86` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.53. Key: `3ae1feaad78a0f3e`
  > Method: `unsubscribe`; Marker on the page: none; Supports Undo: no
  Reviewer: Read against the page: the marker next to this method is as stated. The Undo column is the digest's own reading of the markers.
- `digests/api.md:113` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.66. Key: `717dc9185d3e815c`
  > The description mentions FPS, frame time, process RAM usage, total and available system RAM. It does not mention `ramPeakMb`, which only appears in the example.
  Reviewer: Read against the page: the digest line is correct.
- `digests/api.md:233` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.52. Key: `2657a18a47202e9b`
  > Response: `{}`. No `timelineId` parameter, so the page gives no way to move a section to another timeline.
  Reviewer: Read against the page: the digest line is correct.
- `digests/api.md:350` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.73. Key: `8c021c403d894af2`
  > Response: bare array. Each item: `id` (int), `name` (string), `position` (`[x,y,z]` meters), `rotation` (`[pan,tilt,roll]` degrees), `resolution` (`[width,height]` pixels), `throwRatio` (float), `lensShift` (`[shiftH,shiftV]`), `parentId` (int or `null`).
  Reviewer: Read against the page: the digest line is correct.
- `digests/api.md:377` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.66. Key: `f7a11646aac79582`
  > Parameter: `throwRatio`; Type: `float`; Required: Optional; Description: Lens throw ratio
  Reviewer: Read against the page: the digest line is correct.
- `digests/api.md:380` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.60. Key: `1947164e71649171`
  > Response: `{}`. `parentId` cannot be changed through the documented parameters.
  Reviewer: Read against the page: the digest line is correct.
- `digests/api.md:407` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.74. Key: `2590395727393f6e`
  > Not marked "Mutates state" on the page, although it changes output.
  Reviewer: Read against the page: the digest line is correct.
- `digests/api.md:425` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.79. Key: `563e8fa022924bb7`
  > Variables Query response: bare array of `{id (int), name (string), type (string), value}`. Examples: `{"id":10,"name":"MasterFader","type":"float","value":"1.0"}` and `{"id":101,"name":"LayerOpacity","type":"float","value":"0.9"}`. Note `value` is a JSON string here even for type `float`.
  Reviewer: Read against the page: the digest line is correct.
- `digests/api.md:444` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.74. Key: `bd8ed1e21f3298e0`
  > Single string: `{"method":"variable.update","params":{"id":10,"value":"Welcome to Stage A"}}`
  Reviewer: Read against the page: the digest line is correct.
- `digests/api.md:447` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.79. Key: `bfa8ba823d7a7352`
  > The page writes the two names with a slash and uses both in examples, with the same parameters. It does not describe any difference between them.
  Reviewer: Read against the page: the digest line is correct.
- `digests/api.md:469` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.66. Key: `d296c53848c9d88e`
  > Parameter: `ids`; Type: `array`; Required: Optional; Description: Specific object IDs to monitor (empty or omitted monitors all)
  Reviewer: Read against the page: the digest line is correct.
- `digests/api.md:483` cites `docs/api/lightact-api.md`. Verdict: contradicts. Confidence: 0.96. Key: `c67c64acfa77e4e7`
  > There is no topic for sections, markers, projectors or project changes.
  Reviewer: Read against the page: the digest line is correct.
- `digests/api.md:509` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.49. Key: `fd3bfecb16e21f3a`
  > ID overlap: `variable.list` shows variable `LayerOpacity` with ID `101` inside layer container `100`, while `layer.create` returns a new layer with ID `101`. The page does not say whether variable IDs and object IDs share one number space. `variable.list` resolving `id > 0` as "Layer, else Projector" implies layer and projector IDs do not collide, but that is not stated either.
  Reviewer: The digest's own cross-check of the page's examples. Each part was confirmed on the page.
- `digests/api.md:510` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.35. Key: `a0158ed9e85d169f`
  > Required flags that are not really optional: `section.trigger` lists `id` and `name` both as Optional but needs one of them. `variable.set` lists `id`, `value` and `values` all as Optional but needs either `id` + `value` or `values`.
  Reviewer: The digest's own cross-check of the page's examples. Each part was confirmed on the page.
- `digests/api.md:511` cites `docs/api/lightact-api.md`. Verdict: contradicts. Confidence: 0.20. Key: `d2b09422878a2a61`
  > Mutation markers: `output.setMaster`, all `timeline.*` transport methods, `section.trigger` and `undo.*` carry no "Mutates state" marker even though they change state. The `system.describe` example shows `timeline.play` with `"mutates":false`. What counts as "mutates" is not defined.
  Reviewer: The digest's own cross-check of the page's examples. Each part was confirmed on the page.
- `digests/api.md:513` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.34. Key: `f709713c1c197659`
  > Request `id` values are reused across examples for different methods (6 for `project.save` and `timeline.list`; 16 for `section.trigger` and `layer.list`; 20 for `marker.list` and `projector.list`; 21 for `marker.create` and `projector.create`; 22 for `marker.update`, `projector.update` and `projector.delete`; 23 for `marker.delete`, `output.getMaster` and `variable.list`; 24 for `output.setMaster` and `variable.list`; 28 for `variable.update` and `undo.undo`; 29 for `variable.set` and `undo.redo`). The three `variable.set` requests use ids 27, 28, 29 but only one response (id 27) is shown. These are client-chosen numbers, so this is harmless, but do not read meaning into them.
  Reviewer: The digest's own cross-check of the page's examples. Each part was confirmed on the page.
- `digests/api.md:515` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.74. Key: `1d5b0a5f8b4432e2`
  > Omitted timeline means different things: in the `*.list` methods "0 or omitted" lists everything across all timelines; in create and trigger methods omitted means the active timeline.
  Reviewer: The digest's own cross-check of the page's examples. Each part was confirmed on the page.
- `digests/api.md:516` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.37. Key: `d88f76b9e0059c64`
  > Parameter tables: `system.performance` has an explicit "none" table. `system.ping`, `system.describe`, `project.getInfo`, `timeline.list`, `projector.list`, `output.getMaster`, `undo.undo` and `undo.redo` have no table at all.
  Reviewer: The digest's own cross-check of the page's examples. Each part was confirmed on the page.
- `digests/api.md:519` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.58. Key: `4a9b737a3cc52e60`
  > Play states: the Timelines UI has Play, Play and pause, Play and loop, Pause and Stop. The API documents only `timeline.play`, `timeline.pause` and `timeline.stop`.
  Reviewer: The API part is on the page. The Timelines play states are on docs/timelines/overview.md.
- `digests/api.md:520` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.61. Key: `f24072315be3ebef`
  > `projector.list` returns `parentId` and `projector.create` accepts it, but `projector.update` does not list it.
  Reviewer: The digest's own cross-check of the page's examples. Each part was confirmed on the page.
- `digests/api.md:524` cites `docs/api/lightact-api.md`. Verdict: supports, low confidence. Confidence: 0.16. Key: `1487a61a5ebe9eaa`
  > No methods for assets, canvases, Canvas Maps, throwers, video screens or other Viewport objects, Output Maps, LightNet, devices, DMX, OSC or MIDI.
  Reviewer: A statement that the page leaves something out. Confirmed: nothing on the page covers it.
- `digests/api.md:525` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.46. Key: `a0e9aa1499748630`
  > No methods to create, rename or delete timelines or timeline groups, or to set the Speed multiplier.
  Reviewer: A statement that the page leaves something out. Confirmed: nothing on the page covers it.
- `digests/api.md:526` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.79. Key: `78b74f223b8e547d`
  > No way to read or set a layer's content, template or mapping other than through its variables.
  Reviewer: A statement that the page leaves something out. Confirmed: nothing on the page covers it.
- `digests/api.md:527` cites `docs/api/lightact-api.md`. Verdict: not mentioned. Confidence: 0.38. Key: `9488801c6ab7c063`
  > No authentication, permissions, rate limits (other than `maxRate` on subscriptions) or error code list.
  Reviewer: A statement that the page leaves something out. Confirmed: nothing on the page covers it.

### digests/assets.md

- `digests/assets.md:25` cites `docs/assets/3d-model/uv-mapping-of-3d-models.md`. Verdict: contradicts. Confidence: 0.67. Key: `d1585612e8ec9c6e`
  > A grid image can be exported from LightAct with a **Color Grid** node: right-click its output pin.
  Reviewer: Read against the page: the digest line is correct.
- `digests/assets.md:73` cites `docs/assets/video-formats-and-codecs.md`. Verdict: supports, low confidence. Confidence: 0.79. Key: `04f47d84b48f4511`
  > Filenames (without extension) must be identical apart from an incrementing number at the end.
  Reviewer: Read against the page: the digest line is correct.

### digests/content-mapping.md

- `digests/content-mapping.md:16` cites `docs/content-mapping/content-mapping-overview.md`. Verdict: supports, low confidence. Confidence: 0.35. Key: `9df29106142a9fe9`
  > Direct mapping: select the Viewport object in the layer's **Mapping** variable, or drag from the Viewport object to the layer.
  Reviewer: Read against the page: the digest line is correct.

### digests/dmx.md

- `digests/dmx.md:29` cites `docs/dmx/dmx-in/index-manager.md`. Verdict: supports, low confidence. Confidence: 0.76. Key: `9927fd14fb8327c3`
  > **Autofill** (properties icon) analyses the names of objects (assets, mappings or devices) and asset collections. In the examples, the slot is the number at the start of the object name and the collection is the number at the start of the *Asset collection* name. Assets not in any Asset collection go to collection 0.
  Reviewer: Read against the page: the digest line is correct.
- `digests/dmx.md:30` cites `docs/dmx/dmx-in/index-manager.md`. Verdict: supports, low confidence. Confidence: 0.67. Key: `796e4f72af7560f9`
  > Examples: *005_theSnacks.mp4* outside any Asset collection goes to collection 0, slot 5. *002_syncTest_opus_HAP.mov* inside Asset collection *001_intro* goes to collection 1, slot 2.
  Reviewer: Read against the page: the digest line is correct.
- `digests/dmx.md:35` cites `docs/dmx/dmx-in/controlling-timelines-with-dmx.md`. Verdict: supports, low confidence. Confidence: 0.72. Key: `ef2cc7879dd38a0a`
  > Each timeline has DMX properties in the Properties window. Set Universe and starting Channel first. Easiest: drag from the channel (in DMX In) to the properties button of the Timeline.
  Reviewer: Read against the page: the digest line is correct.
- `digests/dmx.md:71` cites `docs/dmx/dmx-out.md`. Verdict: supports, low confidence. Confidence: 0.58. Key: `bd9ee8d17becd33e`
  > sACN forbids universe 0. sACN universes start from 1. Art-Net can use universe 0.
  Reviewer: Read against the page: the digest line is correct.

### digests/integrations.md

- `digests/integrations.md:50` cites `docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/freed.md`. Verdict: supports, low confidence. Confidence: 0.61. Key: `a88feb8fec33752f`
  > Device **FreeD Receiver** (set *Stream*, tick **Listen**). Node **Read FreeD**. Outputs not listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/integrations.md:54` cites `docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/mo-sys.md`. Verdict: supports, low confidence. Confidence: 0.56. Key: `d019601930f9c128`
  > Device **MoSys Receiver** (set *Stream*, tick **Listen**). Node **Read MoSys**. Outputs not listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/integrations.md:60` cites `docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/ncam.md`. Verdict: supports, low confidence. Confidence: 0.72. Key: `d4ced41d15a3faf9`
  > Device **Ncam Receiver** (tick **Listen**). Node **Read Ncam**. Outputs not listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/integrations.md:71` cites `docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/psn.md`. Verdict: supports, low confidence. Confidence: 0.48. Key: `bec4670baa048c58`
  > Receive: device **PSN Receiver** (tick **Listen**), node **Read PSN**. Outputs not listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/integrations.md:75` cites `docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/spnet.md`. Verdict: supports, low confidence. Confidence: 0.58. Key: `db1daca08bde9001`
  > Device **SPNet Receiver** with **Multicast address** (tick **Listen**). Node **Read SPNet**. Also offers object tracking. Outputs not listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/integrations.md:79` cites `docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/stype.md`. Verdict: supports, low confidence. Confidence: 0.61. Key: `15008f711a9426f4`
  > Device **Stype Receiver** (set *Stream*, tick **Listen**). Node **Read Stype**. Outputs not listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/integrations.md:87` cites `docs/integrations/camera-and-object-tracking/tracking-visualizer.md`. Verdict: supports, low confidence. Confidence: 0.40. Key: `83f290f5bfa911c0`
  > A Viewport object dragged from the toolbar. *Content*: **Tracker device** dropdown. *Source*: **Add tracker**, then type unique tracker names. *Rendering*: **Show trackers**, and for BlackTrax **Show LEDs** and **Show LED connections**.
  Reviewer: Read against the page: the digest line is correct.
- `digests/integrations.md:113` cites `docs/integrations/content-io/deltacast-setup/flex-management.md`. Verdict: supports, low confidence. Confidence: 0.52. Key: `9cd538e9a93917c3`
  > reActor servers use a PCI Express gateway card (**DELTA-gwy** in Device Manager) with FLEX modules, one per gateway port. Modules exist for DisplayPort, HDMI and SDI, input and output.
  Reviewer: Read against the page: the digest line is correct.

### digests/layers-and-layouts.md

- `digests/layers-and-layouts.md:71` cites `docs/layers-and-layouts/curve-editor.md`. Verdict: supports, low confidence. Confidence: 0.53. Key: `ebe9a4a1583320f3`
  > Enable: select the Layer in the Timeline Editor, find the variable in the Variables section of the Properties window, click the curve icon next to it (works on one or several variables). Click the second icon next to an enabled variable to view and edit its curve.
  Reviewer: Read against the page: the digest line is correct.
- `digests/layers-and-layouts.md:167` cites `docs/layers-and-layouts/layer-layouts/nodes/texture-processing.md`. Verdict: supports, low confidence. Confidence: 0.40. Key: `3761b951916e7953`
  > Texture processing nodes are under Utilities -> Texture in the Layer Layout search. Only LUT, Luma Key and Rotate are documented here.
  Reviewer: Read against the page: the digest line is correct.
- `digests/layers-and-layouts.md:213` cites `docs/layers-and-layouts/layer-layouts/variables/layer-variables.md`. Verdict: supports, low confidence. Confidence: 0.67. Key: `842565ebad1e03f6`
  > Seen on the right of the Layer Layout window (double-click a layer). Most also show under the Layer variables collapsible of the Layer properties.
  Reviewer: Read against the page: the digest line is correct.
- `digests/layers-and-layouts.md:280` cites `docs/layers-and-layouts/stock-layer-templates/content-layer-templates/video-1.md`. Verdict: not mentioned. Confidence: 0.38. Key: `748c9b266f867545`
  > Category: Content. Plays video assets. (The file is `video-1.md`. `video.md` is the Multi-layer page.)
  Reviewer: Correct. The note about file names describes the manual copy, not the page text.
- `digests/layers-and-layouts.md:295` cites `docs/layers-and-layouts/stock-layer-templates/content-layer-templates/video-1.md`. Verdict: supports, low confidence. Confidence: 0.60. Key: `c4b9878c6cb899bf`
  > Auto rename: layer always takes the name of the video asset currently playing.
  Reviewer: Read against the page: the digest line is correct.
- `digests/layers-and-layouts.md:312` cites `docs/layers-and-layouts/stock-layer-templates/content-layer-templates/notch-layer-template.md`. Verdict: supports, low confidence. Confidence: 0.26. Key: `2569df905572aa95`
  > Category: Content. Plays Notch blocks. (The page intro says "video files", a copy-paste slip.)
  Reviewer: Read against the page: the digest line is correct.
- `digests/layers-and-layouts.md:319` cites `docs/layers-and-layouts/stock-layer-templates/content-layer-templates/notch-layer-template.md`. Verdict: not mentioned. Confidence: 0.20. Key: `5d5c44b15d7158e8`
  > Play mode: Normal; Free run; Free run & restart (restarts from 0 on re-entry); Timecode. Same meanings as Video.
  Reviewer: Read against the page: the digest line is correct.
- `digests/layers-and-layouts.md:325` cites `docs/layers-and-layouts/stock-layer-templates/content-layer-templates/content-input-template.md`. Verdict: supports, low confidence. Confidence: 0.38. Key: `6841810f49152d5a`
  > Category: Content. Renders textures from Device nodes (for example NDI or live video input).
  Reviewer: Correct. The example is given on the parent page, content-layer-templates.md.
- `digests/layers-and-layouts.md:389` cites `docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/render-time.md`. Verdict: supports, low confidence. Confidence: 0.79. Key: `3e16f3beefcaaf38`
  > Auto rename.
  Reviewer: Read against the page: the digest line is correct.
- `digests/layers-and-layouts.md:427` cites `docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/send-texture.md`. Verdict: supports, low confidence. Confidence: 0.33. Key: `d4aa7bf2be05a903`
  > No Render group is listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/layers-and-layouts.md:433` cites `docs/layers-and-layouts/stock-layer-templates/control-layer-templates.md`. Verdict: not mentioned. Confidence: 0.97. Key: `70f498e100716e43`
  > All documented control templates keep their variables in a group called **Default**. Send message adds an **OSC** group.
  Reviewer: Checked on each control template page: all use a Default group and Send message adds OSC.
- `digests/layers-and-layouts.md:467` cites `docs/layers-and-layouts/stock-layer-templates/control-layer-templates/go-to-marker.md`. Verdict: supports, low confidence. Confidence: 0.19. Key: `0a080025b994fd62`
  > Timeline: the timeline that jumps.
  Reviewer: Read against the page: the digest line is correct.

### digests/lightnet.md

- `digests/lightnet.md:49` cites `docs/lightnet/network-setup.md`. Verdict: supports, low confidence. Confidence: 0.48. Key: `62a1651a300b07d5`
  > Create a folder named exactly **LightNetProjects** on every machine in the cluster. On non-Primary machines it receives all project files and assets, so it needs enough space and a fast enough drive.
  Reviewer: Read against the page: the digest line is correct.
- `digests/lightnet.md:53` cites `docs/lightnet/network-setup.md`. Verdict: supports, low confidence. Confidence: 0.77. Key: `d1af2aba8b5048a0`
  > by computer shared name (the manual's example reads `LA5\\LightNetProjects\`),
  Reviewer: Read against the page: the digest line is correct.
- `digests/lightnet.md:71` cites `docs/lightnet/lightnet-clusters.md`. Verdict: not mentioned. Confidence: 0.62. Key: `2bbb1eb63bc9b6c4`
  > A launch argument also enables LightNet (see the miscellaneous digest: `-lightnet`).
  Reviewer: Correct. The argument is listed on docs/miscellaneous/launching-lightact-with-arguments.md.
- `digests/lightnet.md:124` cites `docs/lightnet/server-workload-distribution.md`. Verdict: supports, low confidence. Confidence: 0.50. Key: `cd3b1877f69b5cd4`
  > Most objects and assets have a **Run on** property: the server(s) that object runs on. Applies to Viewport objects, Layers, Devices and Assets.
  Reviewer: Read against the page: the digest line is correct.

### digests/node-reference.md

- `digests/node-reference.md:48` cites `docs/node-reference/node-reference/layout-nodes/lifeline-and-actions-node-category/set-device-status.md`. Verdict: not mentioned. Confidence: 0.52. Key: `56a561725b1a7d76`
  > Set device status: Sets device status information. Default inputs: Lifeline, Device, Boolean. Default outputs: Lifeline. Not marked deprecated.
  Reviewer: Read against the page: the digest line is correct.
- `digests/node-reference.md:49` cites `docs/node-reference/node-reference/layout-nodes/lifeline-and-actions-node-category/get-timeline-state.md`. Verdict: supports, low confidence. Confidence: 0.37. Key: `cb5eba89071d6769`
  > Get timeline state, Deprecated: Gets timeline state. No pins listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:51` cites `docs/node-reference/node-reference/layout-nodes/lifeline-and-actions-node-category/get-timeline-time.md`. Verdict: supports, low confidence. Confidence: 0.44. Key: `b4fbbe2742baa013`
  > Timeline time, Deprecated: Returns timeline timecode. No pins listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:52` cites `docs/node-reference/node-reference/layout-nodes/lifeline-and-actions-node-category/set-timeline-state.md`. Verdict: supports, low confidence. Confidence: 0.38. Key: `6b0eabdd22d37cc8`
  > Set timeline state, Deprecated: Sets timeline time and state. No pins listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:53` cites `docs/node-reference/node-reference/layout-nodes/lifeline-and-actions-node-category/set-timeline-play.md`. Verdict: supports, low confidence. Confidence: 0.60. Key: `5db217adb95df2c0`
  > Timeline play, Deprecated, use Set timeline state: Controls timeline playback state. No pins listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:55` cites `docs/node-reference/node-reference/layout-nodes/lifeline-and-actions-node-category/on-project-loaded.md`. Verdict: not mentioned. Confidence: 0.91. Key: `8f2b186abc26e351`
  > On project loaded: Default outputs: Event (the only node with an Event pin).
  Reviewer: Checked across all node pages: no other page lists an Event pin.
- `digests/node-reference.md:67` cites `docs/node-reference/node-reference/layout-nodes/texture-generators-node-category.md`. Verdict: not mentioned. Confidence: 0.86. Key: `7da018de94eb18ac`
  > Color to texture (solid colour) is filed under Lifeline and actions, not here.
  Reviewer: Checked: Color to texture is listed on the Lifeline and actions category page.
- `digests/node-reference.md:72` cites `docs/node-reference/node-reference/layout-nodes/texture-processing-node-category.md`. Verdict: not mentioned. Confidence: 0.94. Key: `ea7d4256e3f05696`
  > All output Texture unless noted.
  Reviewer: A summary of the node pages in this category. True for all but Texture resize, which now says so on its own line.
- `digests/node-reference.md:79` cites `docs/node-reference/node-reference/layout-nodes/texture-processing-node-category/texture-resize.md`. Verdict: supports, low confidence. Confidence: 0.22. Key: `3fa830daff452a1e`
  > Texture resize: Resizes input by given width and height. Default inputs: Resolution. No outputs listed. Supported types: Texture -> Texture, OpenCV -> OpenCV.
  Reviewer: Correct: the page lists no Default outputs.
- `digests/node-reference.md:107` cites `docs/node-reference/node-reference/layout-nodes/computer-vision-node-category.md`. Verdict: not mentioned. Confidence: 0.98. Key: `ff42d4f47913f348`
  > Most of these take and return the OpenCV type, not Texture. Convert (Utilities) lists Texture -> OpenCV and OpenCV -> Texture.
  Reviewer: A summary of the node pages in this category, checked page by page.
- `digests/node-reference.md:125` cites `docs/node-reference/node-reference/layout-nodes/math-node-category/divide.md`. Verdict: not mentioned. Confidence: 0.73. Key: `c7bf6540bb9c3a23`
  > Divide: Divides values. Supported types: same four as Add. Search keywords: /.
  Reviewer: Correct: the page lists the same four types as the Add page.
- `digests/node-reference.md:126` cites `docs/node-reference/node-reference/layout-nodes/math-node-category/multiply.md`. Verdict: not mentioned. Confidence: 0.38. Key: `58b9561ddcefea0f`
  > Multiply: Multiplies values together. Supported types: same four as Add. Search keywords: *.
  Reviewer: Correct: the page lists the same four types as the Add page.
- `digests/node-reference.md:128` cites `docs/node-reference/node-reference/layout-nodes/math-node-category/smooth-value.md`. Verdict: not mentioned. Confidence: 0.62. Key: `50c93e97af9b741f`
  > Smooth value: Smooths input value change over time. Supported types: same four as Add. Search keywords: ease.
  Reviewer: Correct: the page lists the same four types as the Add page.
- `digests/node-reference.md:129` cites `docs/node-reference/node-reference/layout-nodes/math-node-category/increment.md`. Verdict: not mentioned. Confidence: 0.73. Key: `86d510c9325b9fc4`
  > Increment: Increments a variable value by an amount. Default inputs: Lifeline. Default outputs: Lifeline. Supported types: same four as Add. Search keywords: ++.
  Reviewer: Correct: the page lists the same four types as the Add page.
- `digests/node-reference.md:235` cites `docs/node-reference/node-reference/layout-nodes/data-io-node-category/write-to-file.md`. Verdict: supports, low confidence. Confidence: 0.79. Key: `f339ab8be968ab9f`
  > Write to file: Writes file stream from string. Default inputs: Lifeline, String, Boolean. No outputs listed. Search keywords: print.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:241` cites `docs/node-reference/node-reference/layout-nodes/trackers-node-category.md`. Verdict: not mentioned. Confidence: 0.97. Key: `67f42ff846223921`
  > Most take a Device and output Lifeline plus Vec3 values.
  Reviewer: A summary of the node pages in this category, checked page by page.
- `digests/node-reference.md:244` cites `docs/node-reference/node-reference/layout-nodes/trackers-node-category/psn-node-category/send-psn.md`. Verdict: supports, low confidence. Confidence: 0.76. Key: `3812c28fe3dc9bc6`
  > Send PSN: Sends PSN messages. Default inputs: Lifeline, String, Vec3. Default outputs: Lifeline. Supported types: Integer -> Integer, String -> String. No Device input is listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:249` cites `docs/node-reference/node-reference/layout-nodes/trackers-node-category/optitrack-node-category/read-prime-coordinates.md`. Verdict: not mentioned. Confidence: 0.25. Key: `13fdb7f56da93782`
  > Read Prime: Reads Prime camera data. Default inputs: Device, Integer. Default outputs: Boolean, Vec3 (no Lifeline). Search keywords: receive.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:254` cites `docs/node-reference/node-reference/layout-nodes/trackers-node-category/vive-node-category/read-vive.md`. Verdict: not mentioned. Confidence: 0.26. Key: `6c165c8d1b426821`
  > Read vive: Reads vive tracker device. Default inputs: Device, Integer. Default outputs: Vec3, Boolean (no Lifeline). Search keywords: receive.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:257` cites `docs/node-reference/node-reference/layout-nodes/trackers-node-category.md`. Verdict: not mentioned. Confidence: 0.89. Key: `8d6ca1390288d1dc`
  > No layout read node is documented for the SICK device. ZED, RealSense and OAK read nodes sit under Content I/O, not Trackers.
  Reviewer: Checked: no layout node page mentions SICK.
- `digests/node-reference.md:299` cites `docs/node-reference/node-reference/layout-nodes/utilities-node-category/lightnet-node-category.md`. Verdict: not mentioned. Confidence: 0.94. Key: `d039aee5a72ada5f`
  > All four are event sources with Default outputs: Lifeline and Search keywords: lightnet.
  Reviewer: Checked on the four node pages.
- `digests/node-reference.md:319` cites `docs/node-reference/node-reference/layout-nodes/utilities-node-category/float-to-vec2.md`. Verdict: not mentioned. Confidence: 0.88. Key: `2e82925f209a624d`
  > Float to vec2, Deprecated: Packages float values into vec2. No replacement named (Merge covers Float -> Vec2).
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:320` cites `docs/node-reference/node-reference/layout-nodes/utilities-node-category/float-to-vec3.md`. Verdict: not mentioned. Confidence: 0.91. Key: `0b4eea7d002b39ba`
  > Float to vec3, Deprecated: Packages float values into vec3. No replacement named (Merge covers Float -> Vec3).
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:321` cites `docs/node-reference/node-reference/layout-nodes/utilities-node-category/integer-to-resolution.md`. Verdict: not mentioned. Confidence: 0.88. Key: `9866f6b03fe30a6e`
  > To resolution, Deprecated: Creates resolution value from inputs. No replacement named (Merge covers Integer -> Resolution).
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:325` cites `docs/node-reference/node-reference/layout-nodes/utilities-node-category/get-object-data.md`. Verdict: supports, low confidence. Confidence: 0.48. Key: `990481832c191f6c`
  > Machine data, Performance data (no source type listed)
  Reviewer: Read against the page: the digest line is correct.
- `digests/node-reference.md:329` cites `docs/node-reference/node-reference/layout-nodes/utilities-node-category/texture-resolution.md`. Verdict: supports, low confidence. Confidence: 0.56. Key: `d7552ef2dd078914`
  > Texture resolution: Returns texture resolution. No pins listed. Search keywords: size px.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:343` cites `docs/node-reference/node-reference/layout-nodes/utilities-node-category/get-object-transform.md`. Verdict: not mentioned. Confidence: 0.89. Key: `86356f06ecf59d26`
  > Get object transform: Gets object's transform. Default inputs: Viewport object. Default outputs: Transform. Not deprecated.
  Reviewer: Read against the page: the digest line is correct.
- `digests/node-reference.md:345` cites `docs/node-reference/node-reference/layout-nodes/utilities-node-category/object-name.md`. Verdict: supports, low confidence. Confidence: 0.38. Key: `c16c42a87f9ce872`
  > Get name: Returns object's name. No pins listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:346` cites `docs/node-reference/node-reference/layout-nodes/utilities-node-category/fade-in.md`. Verdict: supports, low confidence. Confidence: 0.60. Key: `dab9d3c37aa1d62a`
  > Fade in: Fades in from layer begin to target timestamp (page says "layer being"). Default inputs: Float. Default outputs: Float.
  Reviewer: Read against the page: the digest line is correct.
- `digests/node-reference.md:348` cites `docs/node-reference/node-reference/layout-nodes/utilities-node-category/json-pack.md`. Verdict: supports, low confidence. Confidence: 0.72. Key: `d145b166b74e0ecb`
  > JSON Pack: Packs inputs into JSON formatted string. Default outputs: String. No inputs listed.
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:362` cites `docs/node-reference/node-reference/layout-nodes/miscellaneous-node-category/enable-or-disable-video-output.md`. Verdict: not mentioned. Confidence: 0.50. Key: `738ff1dbaf416a05`
  > Set video output state, Deprecated: Enables or disables video output. Default inputs: Lifeline, Boolean. Default outputs: Lifeline. No replacement named (Set data has Video output State).
  Reviewer: Correct. The line says the page leaves something out, and it does.
- `digests/node-reference.md:381` cites `docs/node-reference/node-reference/device-nodes.md`. Verdict: not mentioned. Confidence: 0.92. Key: `359b9486f466004c`
  > `device-nodes.md` lists 3 categories: Content I/O, Data I/O, Trackers. Device node pages have a Description and sometimes Search keywords only. No pins, properties, ports, addresses or formats are listed for any device. Many layout nodes list a Device input.
  Reviewer: A summary of the device node pages.
- `digests/node-reference.md:420` cites `docs/node-reference/node-reference/device-nodes/data-io-node-category.md`. Verdict: not mentioned. Confidence: 0.70. Key: `95789ab89b34a649`
  > No DMX, Art-Net or sACN device node is listed in this section; DMX appears only as layout nodes (Get DMX, Set DMX, DMX by UV and the Art-Net / sACN in status and state nodes).
  Reviewer: Checked against the category page list.

### digests/osc-and-midi.md

- `digests/osc-and-midi.md:30` cites `docs/osc-and-midi/receiving-osc/master-control-and-cue-triggering-with-osc.md`. Verdict: not mentioned. Confidence: 0.25. Key: `594a42077c87959b`
  > Master control: example address `/la/playctrl/master/fade`. LightAct reads the float argument and sets *Master fade*. Master volume is controlled the same way (its address is not written out in the text).
  Reviewer: Read against the page: the digest line is correct.
- `digests/osc-and-midi.md:37` cites `docs/osc-and-midi/receiving-osc/master-control-and-cue-triggering-with-osc.md`. Verdict: supports, low confidence. Confidence: 0.70. Key: `fd72f08257295400`
  > `/la/playctrl/cue/0.77.0` does.
  Reviewer: Read against the page: the digest line is correct.
- `digests/osc-and-midi.md:38` cites `docs/osc-and-midi/receiving-osc/master-control-and-cue-triggering-with-osc.md`. Verdict: not mentioned. Confidence: 0.79. Key: `0ee0b23bf0eed2ae`
  > Default cue numbers (from the changelog, LA4-6636, not on this page): a new cue has CueXYZ `-1,-1,-1`, which OSC and DMX cannot trigger. `-1` switches an axis off and shortens the address: `5,-1,-1` is `/la/playctrl/cue/5`, `5,10,-1` is `/la/playctrl/cue/5.10`, `-1,-1,2` is `/la/playctrl/cue/2`. Source: `docs/release-changelogs/lightact-4.16/lightact-4.16.b1.md`.
  Reviewer: A cross-reference to the 4.16 changelog, confirmed on that page.
- `digests/osc-and-midi.md:49` cites `docs/osc-and-midi/sending-osc.md`. Verdict: supports, low confidence. Confidence: 0.66. Key: `c296b216c283289b`
  > The receiver reads individual values from the bundle with the **Index** input of a **Read OSC** node.
  Reviewer: Read against the page: the digest line is correct.

### digests/projection-mapping.md

- `digests/projection-mapping.md:80` cites `docs/projection-mapping/iris/irisvirtual.md`. Verdict: supports, low confidence. Confidence: 0.76. Key: `7a1bc80c8b657f95`
  > A positive result (below 1 px for all projectors) can still fail in reality. LightAct asks you to send the project file for review before deciding.
  Reviewer: Read against the page: the digest line is correct.
- `digests/projection-mapping.md:115` cites `docs/projection-mapping/iris/calibrating-optitrack-cameras-with-active-or-passive-markers.md`. Verdict: supports, low confidence. Confidence: 0.58. Key: `f942889f24a55bd9`
  > Active Tags need an OptiTrack Active BaseStation. Also needs a PoE switch. Contact LightAct before buying.
  Reviewer: Read against the page: the digest line is correct.

### digests/quick-start.md

- `digests/quick-start.md:12` cites `docs/quick-start/overview-of-content-pipeline.md`. Verdict: supports, low confidence. Confidence: 0.79. Key: `b25dfbfca005f792`
  > Content comes in two ways: through the Assets repository (assets are then played back in Layers), or through Device nodes such as NDI, Spout or Unreal Texture Share. Device content also goes through the layer system.
  Reviewer: Read against the page: the digest line is correct.
- `digests/quick-start.md:90` cites `docs/quick-start/shortcuts.md`. Verdict: not mentioned. Confidence: 0.42. Key: `83e14933842bac53`
  > Timelines (the window listing timelines)
  Reviewer: A sub-heading for the shortcut list below it, with the digest's own gloss.
- `digests/quick-start.md:97` cites `docs/quick-start/shortcuts.md`. Verdict: supports, low confidence. Confidence: 0.55. Key: `b6def3e20b05c478`
  > Timeline (the editor)
  Reviewer: A sub-heading for the shortcut list below it, with the digest's own gloss.

### digests/real-time-content-playback.md

- `digests/real-time-content-playback.md:11` cites `docs/real-time-content-playback/notch.md`. Verdict: supports, low confidence. Confidence: 0.42. Key: `43fec15c12c69b59`
  > Unity has no native integration. Users run it on another machine, bring content in over NDI or live video input, and exchange data over UDP, OSC or TCP.
  Reviewer: Read against the page: the digest line is correct.
- `digests/real-time-content-playback.md:46` cites `docs/real-time-content-playback/unreal-engine-integration-overview/required-unreal-engine-plugins/setting-up-the-plugin.md`. Verdict: not mentioned. Confidence: 0.70. Key: `fbbed8948254fee8`
  > Three steps, detailed in the next three pages: LightAct Runtime actor, LightActTimeStep as Custom Time Step, LightActTimeCode as Timecode provider.
  Reviewer: Read against the page: the digest line is correct.
- `digests/real-time-content-playback.md:73` cites `docs/real-time-content-playback/unreal-engine-integration-overview/unreallink.md`. Verdict: supports, low confidence. Confidence: 0.67. Key: `ba82b75d187b3cdd`
  > With Every frame, real-time UE stats appear a few seconds after launch. No stats means the LightAct plugin is not set up correctly.
  Reviewer: Read against the page: the digest line is correct.

### digests/release-changelogs.md

- `digests/release-changelogs.md:14` cites `docs/release-changelogs/changelogs-before-4.13.md`. Verdict: supports, low confidence. Confidence: 0.52. Key: `93d7c45a5532b6d3`
  > Older changelogs live on LightAct Answerhub: https://answerhub.lightact.com/c/changelog/17. Nothing else on the page.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:19` cites `docs/release-changelogs/how-are-changelogs-generated.md`. Verdict: not mentioned. Confidence: 0.56. Key: `1fb45d03bb90bc86`
  > Generated semi-automatically from the LightAct 4 Jira project, grouped by Epic. Tickets outside any Epic are listed at the end (the build pages head that part "Other Upgrades").
  Reviewer: Correct. The name Other Upgrades comes from the build pages, not this page.
- `digests/release-changelogs.md:34` cites `docs/release-changelogs/lightact-4.17/lightact-4.17.0.md`, `docs/release-changelogs/lightact-4.17/lightact-4.17.rc1.md`, `docs/release-changelogs/lightact-4.17/lightact-4.17.b1.md`. Verdict: contradicts. Confidence: 0.22. Key: `cc1e25bad382db54`
  > No ticket repeats across the three pages; 4.17 is the sum of all three.
  Reviewer: Checked by listing the ticket numbers on each build page: none repeats.
- `digests/release-changelogs.md:38` cites `docs/release-changelogs/lightact-4.17/lightact-4.17.b1.md`. Verdict: contradicts. Confidence: 0.25. Key: `394b37fd27b11477`
  > LA4-7357, LA4-6920 [B1]: two defaults. Project Settings holds the project-wide default crossfade and duration, used only for newly created timelines. Timeline Properties holds a timeline default, used only for newly created sections on that timeline. Neither changes existing timelines or sections.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:83` cites `docs/release-changelogs/lightact-4.17/lightact-4.17.b1.md`, `docs/release-changelogs/lightact-4.17/lightact-4.17.rc1.md`. Verdict: not mentioned. Confidence: 0.67. Key: `94aeb71846a9f52b`
  > LA4-3752 [B1]: Shared Memory Handle size and Name are editable (ticket "UE Data Handle Size"). LA4-7427 [RC1]: TouchDesigner features lose the Beta label.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:90` cites `docs/release-changelogs/lightact-4.17/lightact-4.17.rc1.md`, `docs/release-changelogs/lightact-4.17/lightact-4.17.b1.md`. Verdict: not mentioned. Confidence: 0.83. Key: `6897709be05ff109`
  > LA4-7503 [RC1]: NDI accepts interlaced and progressive inputs; NDI Sender nodes output audio. LA4-7364 [B1]: NDI SDK 6.3.2.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:111` cites `docs/release-changelogs/lightact-4.17/lightact-4.17.0.md`, `docs/release-changelogs/lightact-4.17/lightact-4.17.rc1.md`, `docs/release-changelogs/lightact-4.17/lightact-4.17.b1.md`. Verdict: supports, low confidence. Confidence: 0.74. Key: `8c6e76c15474842c`
  > Shortcuts confirmed by fixes: Shift+F is Look at Target (LA4-7307); Ctrl+Shift+G in the Objects window puts the selection under one Null (LA4-7575).
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:123` cites `docs/release-changelogs/lightact-4.16/lightact-4.16.0.md`. Verdict: supports, low confidence. Confidence: 0.68. Key: `35c1e4be7f15263e`
  > 10 August 2026, 1 upgrade.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:126` cites `docs/release-changelogs/lightact-4.16/lightact-4.16.4.md`, `docs/release-changelogs/lightact-4.16/lightact-4.16.3.md`, `docs/release-changelogs/lightact-4.16/lightact-4.16.2.md`, `docs/release-changelogs/lightact-4.16/lightact-4.16.1.md`, `docs/release-changelogs/lightact-4.16/lightact-4.16.0.md`, `docs/release-changelogs/lightact-4.16/lightact-4.16.rc1.md`, `docs/release-changelogs/lightact-4.16/lightact-4.16.b1.md`. Verdict: not mentioned. Confidence: 0.72. Key: `186d8a862b1bcf49`
  > Carried over: LA4-7034 (right-click a locked layer, single option "Unlock") is in 4.16.B1 and was already in 4.15.2.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:135` cites `docs/release-changelogs/lightact-4.16/lightact-4.16.1.md`. Verdict: supports, low confidence. Confidence: 0.22. Key: `af5dcdc0a3d8e9e8`
  > LA4-7229 [1]: previous-cue logic while playing: within n seconds after a cue, jump two cues back; otherwise jump to the nearest cue before the current time. (n is not stated here; 4.17 calls it the one-second jump threshold.)
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:143` cites `docs/release-changelogs/lightact-4.16/lightact-4.16.b1.md`. Verdict: supports, low confidence. Confidence: 0.52. Key: `e1e4b91293c0785e`
  > LA4-6886 [B1]: Audio In device node gets a Volume control (clipped audio stopped LTC parsing). Order: "Parse LTC", "Min consecutive frames", "Timecode offset".
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:161` cites `docs/release-changelogs/lightact-4.16/lightact-4.16.b1.md`. Verdict: supports, low confidence. Confidence: 0.72. Key: `71ddbbd331025e66`
  > LA4-6931 [B1]: Iris 2.0, calibration rebuilt; can output a point cloud of the projection object to verify the 3D model. No detail given.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:172` cites `docs/release-changelogs/lightact-4.16/lightact-4.16.1.md`, `docs/release-changelogs/lightact-4.16/lightact-4.16.2.md`, `docs/release-changelogs/lightact-4.16/lightact-4.16.b1.md`. Verdict: supports, low confidence. Confidence: 0.79. Key: `061e95e7119b9bbc`
  > LA4-7228 [1], LA4-7318 [2]: a layer spanning both sections of a crossfade (Dip/Hold) is rendered to a texture on the source side and reused on the destination so the background stays continuous. LA4-6984 [B1]: crossfades work across different tracks.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:177` cites `docs/release-changelogs/lightact-4.16/lightact-4.16.b1.md`. Verdict: supports, low confidence. Confidence: 0.25. Key: `63a4874099492258`
  > LA4-6641 [B1]: Collection dropdown lists up to 255 collections (was 15), matching the Index Manager. LA4-6989: right-click "Remove" on a single missing asset or collection.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:192` cites `docs/release-changelogs/lightact-4.15/lightact-4.15.2.md`, `docs/release-changelogs/lightact-4.15/lightact-4.15.1.md`, `docs/release-changelogs/lightact-4.15/lightact-4.15.0.md`, `docs/release-changelogs/lightact-4.15/lightact-4.15.b1.md`. Verdict: supports, low confidence. Confidence: 0.20. Key: `60e10e5d9e7e0705`
  > No ticket repeats inside 4.15.
  Reviewer: Checked by listing the ticket numbers on each build page: none repeats.
- `digests/release-changelogs.md:216` cites `docs/release-changelogs/lightact-4.15/lightact-4.15.b1.md`. Verdict: not mentioned. Confidence: 0.60. Key: `e1a1702e1ad1029a`
  > LA4-6900 [B1]: Project settings "Default section crossfade time" beside "Default layer crossfade time", each with "Apply to all existing". (Layer crossfade is removed in 4.17.)
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:231` cites `docs/release-changelogs/lightact-4.14/lightact-4.14.0.md`. Verdict: supports, low confidence. Confidence: 0.79. Key: `51fb4e7deb97cac8`
  > 21 April 2026, 1 Epic, 3 upgrades.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:232` cites `docs/release-changelogs/lightact-4.14/lightact-4.14.rc2.md`. Verdict: supports, low confidence. Confidence: 0.52. Key: `00a5ada81646cb4c`
  > 27 March 2026, 2 upgrades.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:233` cites `docs/release-changelogs/lightact-4.14/lightact-4.14.rc1.md`. Verdict: supports, low confidence. Confidence: 0.62. Key: `c34e2c15262f1a0b`
  > 26 March 2026, 2 Epics, 8 upgrades, mostly mapping and workspace crash fixes.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:246` cites `docs/release-changelogs/lightact-4.14/lightact-4.14.1.md`, `docs/release-changelogs/lightact-4.14/lightact-4.14.0.md`, `docs/release-changelogs/lightact-4.14/lightact-4.14.rc2.md`, `docs/release-changelogs/lightact-4.14/lightact-4.14.rc1.md`, `docs/release-changelogs/lightact-4.14/lightact-4.14.b1.md`. Verdict: supports, low confidence. Confidence: 0.67. Key: `d22bc125cf010c06`
  > LA4-5772: "Duplicate multiple" makes an array of subareas. LA4-6660: right-click menu: Add to output/objects, Unmap from outputs/objects, Duplicate, Duplicate multiple, Delete. LA4-5776: unmap options reduced to "Unmap from objects" (CanvasMaps) and "Unmap from outputs" (OutputMaps).
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:266` cites `docs/release-changelogs/lightact-4.14/lightact-4.14.b1.md`. Verdict: supports, low confidence. Confidence: 0.53. Key: `52799a9c1a462a9d`
  > LA4-6638 [B1]: Timeline properties "Elements" panel (below DMX) lists sections, markers, layers. Columns: Trigger, Time Point, Position, Type, Update. Active items green, others "Inactive". Enter jumps to the top result.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:286` cites `docs/release-changelogs/lightact-4.13/lightact-4.13.1.md`. Verdict: supports, low confidence. Confidence: 0.58. Key: `808ed6c4195a1498`
  > 01 February 2026, 3 upgrades.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:291` cites `docs/release-changelogs/lightact-4.13/lightact-4.13.4.md`, `docs/release-changelogs/lightact-4.13/lightact-4.13.3.md`, `docs/release-changelogs/lightact-4.13/lightact-4.13.2.md`, `docs/release-changelogs/lightact-4.13/lightact-4.13.1.md`, `docs/release-changelogs/lightact-4.13/lightact-4.13.0.md`, `docs/release-changelogs/lightact-4.13/lightact-4.13-rc1.md`, `docs/release-changelogs/lightact-4.13/lightact-4.13.b2.md`, `docs/release-changelogs/lightact-4.13/lightact-4.13.b1.md`. Verdict: not mentioned. Confidence: 0.67. Key: `e4122f9adfa2efb4`
  > Carried over: LA4-6137 (LightSync no longer drops machines from the session prematurely, status Testing) is in B1 and B2. LA4-6481 and LA4-6482 are the same node (6482 is the 4.12 backport).
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:315` cites `docs/release-changelogs/lightact-4.13/lightact-4.13.b2.md`. Verdict: not mentioned. Confidence: 0.74. Key: `bd477b1ff2f824c0`
  > LA4-6343, LA4-3781, LA4-6342 [B2]: Timeline "Cross-fade time [s]"; Section and Layer dropdowns Inherit or Fade. Crossfade time comes from the destination (section or layer) only, never combined. Superseded in 4.14 and 4.17.
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:353` cites `docs/release-changelogs/lightact-4.13/lightact-4.13.b1.md`. Verdict: supports, low confidence. Confidence: 0.76. Key: `e792e3227b644ac2`
  > New [B1]: "Run on Shutdown" (LA4-5767), absolute value (LA4-5580), "Texture Vignette" (LA4-6171), JSON Parser and Packager (LA4-5706), Expression with dynamic float inputs (LA4-5634), "Set DMX Out State", a boolean toggling "Send DMX" in the DMX Out window (LA4-6481).
  Reviewer: Read against the ticket text on the cited build page: correct.
- `digests/release-changelogs.md:356` cites `docs/release-changelogs/lightact-4.13/lightact-4.13.b1.md`, `docs/release-changelogs/lightact-4.13/lightact-4.13.b2.md`. Verdict: not mentioned. Confidence: 0.68. Key: `d0937f1b3de95b53`
  > LA4-6070 [B1]: "Restore to default" for unconnected inputs in variable groups. LA4-6476 [B2]: watches on dropdown integers show "label [value]". LA4-6496 [B2]: "Undo Stack" viewer under Redo.
  Reviewer: Read against the ticket text on the cited build page: correct.

### digests/timelines.md

- `digests/timelines.md:44` cites `docs/timelines/cue-list.md`. Verdict: contradicts. Confidence: 0.53. Key: `7fbc4dcd71b7b8b2`
  > A Cue placed beyond the timeline duration shows its position in a yellow warning color. This can only happen when **Auto duration** is disabled in the Timeline's properties.
  Reviewer: Read against the page: the digest line is correct.

### digests/transitioning-to-lightact-from-other-media-servers.md

- `digests/transitioning-to-lightact-from-other-media-servers.md:11` cites `docs/transitioning-to-lightact-from-other-media-servers/switching-to-lightact.md`. Verdict: contradicts. Confidence: 0.64. Key: `c57b70ab219c699d`
  > Index page. Only Disguise and Pixera are covered. Nothing else useful.
  Reviewer: Read against the page: the digest line is correct.

### digests/video-playback.md

- `digests/video-playback.md:31` cites `docs/video-playback/frame-buffering.md`. Verdict: supports, low confidence. Confidence: 0.70. Key: `bbe8ba4be53360b1`
  > Worked example on the page: Video buffer 20 frames, Video preload time 5 seconds, Always ready buffer 50% = 10 frames. More than 5 seconds before the layer, the Play Video node holds 10 frames. At the 5 second mark it loads the full buffer.
  Reviewer: Read against the page: the digest line is correct.
