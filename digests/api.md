# api

## What this section covers

One long page: the reference manual for the "LightAct4 Public API v1", a JSON-RPC 2.0 API on port 9899 reachable over WebSocket, raw TCP and HTTP POST.
It covers the handshake, performance metrics, project save, timeline transport, sections (cues), layers, markers, projectors, master output opacity and volume, variables, undo/redo, and pub/sub subscriptions.
Available in LightAct 4.18 and higher.
This digest is deliberately not shortened: every method, parameter, type, required flag, response field, Undo marker, subscription topic and inconsistency on the page is listed.

## LightAct API
`docs/api/lightact-api.md`

### Availability and transports

- "This feature is available in LightAct 4.18 and higher."
- Name on the page: "LightAct4 Public API v1 Reference Manual".
- Protocol: JSON-RPC 2.0.
- Default Port: `9899`.
- Three supported transports, all on the same port:
  1. WebSocket: `ws://127.0.0.1:9899/api` (recommended for plugins, Python SDK, WebUI).
  2. Raw TCP Socket: `127.0.0.1:9899` (direct connection for Hercules Setup Utility, Telnet, Crestron, Q-Sys).
  3. HTTP POST: `http://127.0.0.1:9899/api` (Postman, curl, web fetch).
- Raw TCP: "No HTTP framing or WebSocket handshakes are needed." The connection is persistent and commands can be sent one after another. The Hercules walkthrough says to click Send "or press Enter with `<CR><LF>` enabled".
- The server processes each command "on LightAct's main thread" and replies immediately.
- Unclear: the page does not say how the API is switched on, whether it listens on addresses other than 127.0.0.1 (all examples use loopback), or whether there is any authentication. None is shown.
- Unclear: the exact message delimiter for raw TCP is not specified. CR LF is only implied by the Hercules step.
- Unclear: the page does not say how subscription notifications are delivered to an HTTP POST client. Notifications are only shown as unsolicited messages, which fits WebSocket and raw TCP.

### Protocol conventions

- Request: `{"jsonrpc": "2.0", "id": 1, "method": "domain.action", "params": { ... }}`
- Success: `{"jsonrpc": "2.0", "id": 1, "result": { ... }}`
- Error: `{"jsonrpc": "2.0", "id": 1, "error": {"code": -32602, "message": "Invalid parameters", "data": {"fields": [...]}}}`
- Only error code shown on the page: `-32602` "Invalid parameters", with `data.fields` as an array. No other error codes are listed.
- Single requests only: "Batch/array execution is currently deferred." Do not send JSON-RPC batch arrays.
- Object identifiers (`id`): 32-bit unsigned integer (`unsigned int` / `LAId`), sent as a plain JSON integer.
- Time: floating point seconds (`float`) relative to the beginning of the timeline.
- Distances: meters, `[x, y, z]`.
- Angles: degrees, `[pan, tilt, roll]`.
- Colors: normalized RGBA array `[r, g, b, a]`, each component `0.0` to `1.0`.
- Method names are `domain.action`, except `subscribe` and `unsubscribe`, which have no domain prefix.

### Method index

38 methods, plus 3 alias names (`output.get`, `output.set`, `variable.update`).

| Method | Marker on the page | Supports Undo |
| --- | --- | --- |
| `system.hello` | none | no |
| `system.ping` | none | no |
| `system.performance` | none | no |
| `system.describe` | none | no |
| `project.getInfo` | none | no |
| `project.save` | Mutates state | not marked |
| `timeline.list` | none | no |
| `timeline.play` | none | not marked |
| `timeline.pause` | none | not marked |
| `timeline.stop` | none | not marked |
| `timeline.seek` | none | not marked |
| `timeline.gotoLandmark` | none | not marked |
| `section.list` | none | no |
| `section.create` | Mutates state, supports Undo | **yes** |
| `section.update` | Mutates state | not marked |
| `section.delete` | Mutates state | not marked |
| `section.trigger` | none | not marked |
| `layer.list` | none | no |
| `layer.create` | Mutates state, supports Undo | **yes** |
| `layer.update` | Mutates state | not marked |
| `layer.delete` | Mutates state | not marked |
| `marker.list` | none | no |
| `marker.create` | Mutates state, supports Undo | **yes** |
| `marker.update` | Mutates state | not marked |
| `marker.delete` | Mutates state | not marked |
| `projector.list` | none | no |
| `projector.create` | Mutates state | not marked |
| `projector.update` | Mutates state | not marked |
| `projector.delete` | Mutates state | not marked |
| `output.getMaster` (alias `output.get`) | none | no |
| `output.setMaster` (alias `output.set`) | none | not marked |
| `variable.list` | none | no |
| `variable.get` | none | no |
| `variable.set` / `variable.update` | Mutates state | not marked |
| `undo.undo` | none | n/a |
| `undo.redo` | none | n/a |
| `subscribe` | none | no |
| `unsubscribe` | none | no |

Methods marked as supporting Undo: exactly three, `section.create`, `layer.create`, `marker.create`. No update, no delete, no projector method and no variable method carries the Undo marker.

### 2.1 System methods (`system.*`)

**`system.hello`**: initial handshake, client registration and API version negotiation.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `apiVersion` | `int` | Required | API version expected by the client (version 1 = `1`) |
| `client` | `string` | Required | Client identifier and version, for example `"Hercules/1.0"`, `"lightact-python/1.0"` |
| `pluginId` | `string` | Optional | Registered plugin identifier, for example `"com.customer.myplugin"` |

- Response fields: `apiVersion` (int, example `1`), `supportedApiVersions` (array of int, example `[1]`), `lightactVersion` (string, example `"4.1.0"`), `sessionId` (string, example `"1"`).
- Request example: `{"jsonrpc":"2.0","id":1,"method":"system.hello","params":{"apiVersion":1,"client":"Hercules/1.0","pluginId":"com.test.hercules"}}`
- Unclear: the page does not say whether `system.hello` must be sent before other methods. The Hercules walkthrough sends `system.performance` as its first command with no hello.

**`system.ping`**: heartbeat / liveness check.

- Parameters: none documented.
- Response: empty object `{}`.

**`system.performance`**: real-time engine performance metrics and system resource use.

- Parameters: none (stated explicitly).
- Response fields (all numbers): `fps` (example `60.0`), `frameTimeMs` (`16.66`), `ramUsedMb` (`512.4`, process RAM), `ramPeakMb` (`780.2`), `systemRamTotalMb` (`32768.0`), `systemRamAvailableMb` (`18450.0`).
- The description mentions FPS, frame time, process RAM usage, total and available system RAM. It does not mention `ramPeakMb`, which only appears in the example.

**`system.describe`**: returns schema definitions, parameter types, mutation flags and documentation for all registered API methods.

- Parameters: none documented.
- Response fields: `apiVersion` (int), `methods` (array). Each method: `name` (string), `mutates` (bool), `description` (string), `params` (array of `{name, type, required}`).
- Response example: `{"apiVersion":1,"methods":[{"name":"timeline.play","mutates":false,"description":"Start playback","params":[{"name":"id","type":"int64","required":false}]}]}`
- This is the way to get the live schema from a running LightAct instead of trusting this page.

### 2.2 Project information (`project.*`)

**`project.getInfo`**: metadata about the currently open project.

- Parameters: none documented.
- Response fields: `name` (string, example `"MainStage"`), `path` (string, example `"C:/Projects/MainStage.la"`), `dirty` (bool, example `false`).

**`project.save`**: saves the currently open project to disk, or to a given path. Mutates state.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | Optional | Absolute or relative file path to save as. If omitted, a standard save on the current project file. |

- Response: `{}`.
- Save As example: `{"jsonrpc":"2.0","id":6,"method":"project.save","params":{"path":"C:/Projects/Backup.la"}}`
- Unclear: what a relative path is relative to is not stated.

### 2.3 Timeline playback (`timeline.*`)

**`timeline.list`**: lists all timelines with playback state, duration and playhead position.

- Parameters: none documented.
- Response: `result` is a bare array. Each item: `id` (int), `name` (string), `duration` (float seconds), `state` (string, example `"playing"`), `time` (float seconds, playhead).
- Unclear: `"playing"` is the only `state` value shown. The other state strings are not listed.

**`timeline.play`**: starts playback on the given timeline, or the active timeline if omitted.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Optional | Timeline ID (`LAId`). Defaults to active timeline if omitted. |

- Response: `{}`.

**`timeline.pause`**: pauses playback on the given timeline, or the active timeline if omitted.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Optional | Timeline ID. Defaults to active timeline if omitted. |

- Response: `{}`.

**`timeline.stop`**: stops playback and rewinds the playhead to `0.0` seconds.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Optional | Timeline ID. Defaults to active timeline if omitted. |

- Response: `{}`.

**`timeline.seek`**: moves the playhead to a timestamp in seconds.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `time` | `float` | Required | Target playhead position in seconds, for example `24.5` |
| `id` | `int` | Optional | Timeline ID. Defaults to active timeline if omitted. |

- Response: `{}`.

**`timeline.gotoLandmark`**: jumps the playhead to the next or previous landmark or cue on the timeline.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `direction` | `string` | Required | `"next"` or `"prev"` |
| `id` | `int` | Optional | Timeline ID. Defaults to active timeline if omitted. |
| `cue` | `bool` | Optional | If `true`, jumps exclusively to cue sections. Default: `false`. |

- Response: `{}`.
- Unclear: "landmark" is not defined on this page.
- Unclear: "active timeline" is not defined on this page.
- Note: the timeline methods name the timeline parameter `id`. Section, layer and marker methods name it `timelineId`.

### 2.4 Sections / Cues (`section.*`)

**`section.list`**: lists all cue sections for a timeline.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `timelineId` | `int` | Optional | Timeline ID (0 or omitted lists all sections) |

- Response: bare array. Each item: `id` (int), `timelineId` (int), `name` (string), `start` (float s), `end` (float s), `fadeIn` (float s), `fadeOut` (float s), `masterFade` (float), `masterVolume` (float), `color` (`[r,g,b,a]`).

**`section.create`**: creates a new cue section on a timeline. Mutates state, **supports Undo**.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Required | Section name, for example `"Chorus"` |
| `start` | `float` | Required | Start time in seconds |
| `end` | `float` | Required | End time in seconds |
| `timelineId` | `int` | Optional | Timeline ID (defaults to active timeline if omitted) |
| `color` | `array` | Optional | RGBA `[r, g, b, a]`, 0.0 to 1.0 |
| `fadeIn` | `float` | Optional | Fade-in duration in seconds (default `0.0`) |
| `fadeOut` | `float` | Optional | Fade-out duration in seconds (default `0.0`) |
| `masterFade` | `float` | Optional | Master fade multiplier `0.0` to `1.0` (default `1.0`) |
| `masterVolume` | `float` | Optional | Master volume multiplier `0.0` to `1.0` (default `1.0`) |

- Response fields: `id` (int, the new section ID, example `1002`).

**`section.update`**: updates a section's name, timestamps, color, fade or volume properties. Mutates state.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Required | Section ID to update |
| `name` | `string` | Optional | New section name |
| `start` | `float` | Optional | New start time in seconds |
| `end` | `float` | Optional | New end time in seconds |
| `color` | `array` | Optional | New RGBA `[r, g, b, a]` |
| `fadeIn` | `float` | Optional | Fade-in duration in seconds |
| `fadeOut` | `float` | Optional | Fade-out duration in seconds |
| `masterFade` | `float` | Optional | Master fade multiplier `0.0` to `1.0` |
| `masterVolume` | `float` | Optional | Master volume multiplier `0.0` to `1.0` |

- Response: `{}`. No `timelineId` parameter, so the page gives no way to move a section to another timeline.

**`section.delete`**: deletes a cue section by ID. Mutates state.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Required | Section ID to delete |

- Response: `{}`.

**`section.trigger`**: triggers / jumps to a cue section by ID or name, optionally starting playback.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Optional | Section ID to trigger (must provide either `id` or `name`) |
| `name` | `string` | Optional | Section name to trigger (case-insensitive search) |
| `play` | `bool` | Optional | If `true`, immediately resumes playback from the section start time. Default: `true`. |
| `timelineId` | `int` | Optional | Timeline ID (defaults to active timeline if omitted) |

- Response: `{}`.
- Both `id` and `name` are listed as Optional, but one of them must be given.
- Examples: `{"method":"section.trigger","params":{"name":"Chorus","play":true}}` and `{"method":"section.trigger","params":{"id":1002,"play":false}}`.
- Unclear: behaviour when several sections share a name, or when both `id` and `name` are sent, is not stated.

### 2.5 Timeline layers (`layer.*`)

**`layer.list`**: lists all layers for a timeline, or across all timelines.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `timelineId` | `int` | Optional | Timeline ID (0 or omitted lists all layers) |

- Response: bare array. Each item: `id` (int), `timelineId` (int), `name` (string), `start` (float s), `end` (float s), `fadeIn` (float s), `fadeOut` (float s), `color` (`[r,g,b,a]`).

**`layer.create`**: creates a new layer on a timeline. Mutates state, **supports Undo**.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Required | Layer name |
| `start` | `float` | Required | Start time in seconds |
| `end` | `float` | Required | End time in seconds |
| `timelineId` | `int` | Optional | Timeline ID (defaults to active timeline if omitted) |
| `color` | `array` | Optional | RGBA `[r, g, b, a]`, 0.0 to 1.0 |
| `fadeIn` | `float` | Optional | Fade-in duration in seconds (default `0.0`) |
| `fadeOut` | `float` | Optional | Fade-out duration in seconds (default `0.0`) |

- Response fields: `id` (int, the new layer ID, example `101`).
- Unclear: there is no parameter for layer template, asset, mapping or vertical position, and the page does not say what kind of layer is created or what it contains.

**`layer.update`**: updates a layer's name, timestamps, color or fade duration. Mutates state.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Required | Layer ID to update |
| `name` | `string` | Optional | New layer name |
| `start` | `float` | Optional | New start time in seconds |
| `end` | `float` | Optional | New end time in seconds |
| `color` | `array` | Optional | New RGBA `[r, g, b, a]` |
| `fadeIn` | `float` | Optional | Fade-in duration in seconds |
| `fadeOut` | `float` | Optional | Fade-out duration in seconds |

- Response: `{}`.

**`layer.delete`**: deletes a layer by ID. Mutates state.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Required | Layer ID to delete |

- Response: `{}`.

### 2.6 Timeline markers (`marker.*`)

**`marker.list`**: lists all markers for a timeline, or across all timelines.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `timelineId` | `int` | Optional | Timeline ID (0 or omitted lists markers across all timelines) |

- Response: bare array. Each item: `id` (int), `timelineId` (int), `name` (string), `start` (float s), `color` (`[r,g,b,a]`).

**`marker.create`**: creates a new marker on a timeline. Mutates state, **supports Undo**.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Required | Marker name / label |
| `start` | `float` | Required | Timestamp position in seconds |
| `timelineId` | `int` | Optional | Target timeline ID (defaults to active timeline if omitted) |
| `color` | `array` | Optional | RGBA `[r, g, b, a]`, 0.0 to 1.0. Default yellow `[1.0, 1.0, 0.0, 1.0]`. |

- Response fields: `id` (int, the new marker ID, example `301`).

**`marker.update`**: updates a marker's name, timestamp or color. Mutates state.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Required | Marker ID to update |
| `name` | `string` | Optional | New marker name |
| `start` | `float` | Optional | New timestamp in seconds |
| `color` | `array` | Optional | New RGBA `[r, g, b, a]` |

- Response: `{}`.

**`marker.delete`**: deletes a marker by ID. Mutates state.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Required | Marker ID to delete |

- Response: `{}`.
- Unclear: markers and sections have a "Use as cue" checkbox and play state actions in the UI (see the timelines digest). None of that is exposed in the documented `marker.*` or `section.*` parameters.

### 2.7 Projectors (`projector.*`)

**`projector.list`**: lists all projectors in the scene.

- Parameters: none documented.
- Response: bare array. Each item: `id` (int), `name` (string), `position` (`[x,y,z]` meters), `rotation` (`[pan,tilt,roll]` degrees), `resolution` (`[width,height]` pixels), `throwRatio` (float), `lensShift` (`[shiftH,shiftV]`), `parentId` (int or `null`).
- Example item: `{"id":1005,"name":"PJ_Main","position":[0.0,3.5,-6.0],"rotation":[0.0,12.0,0.0],"resolution":[1920,1080],"throwRatio":1.6,"lensShift":[0.0,0.5],"parentId":null}`

**`projector.create`**: creates a new projector in the scene. Mutates state. Not marked as supporting Undo.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Required | Projector identifier/name |
| `position` | `array` | Required | `[x, y, z]` in meters |
| `rotation` | `array` | Required | Euler angles `[pan, tilt, roll]` in degrees |
| `resolution` | `array` | Required | `[width, height]` in pixels, for example `[1920, 1080]` |
| `throwRatio` | `float` | Required | Lens throw ratio, for example `1.6` |
| `lensShift` | `array` | Required | Lens shift `[shiftH, shiftV]` |
| `parentId` | `int` | Optional | Optional parent object ID |

- Response fields: `id` (int, the new projector ID, example `1006`).
- Unclear: the unit or range of `lensShift` is not given.

**`projector.update`**: updates a projector's name, position, rotation, resolution, throw ratio or lens shift. Mutates state.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Required | Projector ID |
| `name` | `string` | Optional | New name |
| `position` | `array` | Optional | `[x, y, z]` in meters |
| `rotation` | `array` | Optional | `[pan, tilt, roll]` in degrees |
| `resolution` | `array` | Optional | `[width, height]` in pixels |
| `throwRatio` | `float` | Optional | Lens throw ratio |
| `lensShift` | `array` | Optional | Lens shift `[shiftH, shiftV]` |

- Response: `{}`. `parentId` cannot be changed through the documented parameters.

**`projector.delete`**: deletes a projector from the scene. Mutates state.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Required | Projector ID to delete |

- Response: `{}`.

### 2.8 Video output master (`output.*`), VideoOutputController

Controls the master output canvas fade opacity and master audio volume "across the entire LightAct installation".

**`output.getMaster`** (alias `output.get`): returns current master output opacity and master volume.

- Parameters: none documented.
- Response fields: `opacity` (float `0.0` to `1.0`), `volume` (float `0.0` to `1.0`).

**`output.setMaster`** (alias `output.set`): sets master output opacity and/or master volume. Both are normalized floats clamped between `0.0` and `1.0`.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `opacity` | `float` | Optional | Canvas blackout / fade level (`0.0` = black, `1.0` = full output) |
| `volume` | `float` | Optional | Master volume level (`0.0` = muted, `1.0` = 100%) |

- Response: `{}`.
- Not marked "Mutates state" on the page, although it changes output.

### 2.9 Hierarchical variables (`variable.*`)

Variables are organized into Containers:

1. Global Variables: Container ID `0`.
2. Layer Variables: Container ID = Layer ID.
3. Projector Variables: Container ID = Projector ID.

**`variable.list`**: two modes.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Optional | Container ID. `< 0` or omitted = list containers. `0` = global. `> 0` = layer or projector. |

- Container Listing Mode (`id` omitted or `< 0`): returns all variable containers. Bare array of `{id (int), name (string), type (string)}`. `type` values shown: `"global"`, `"layer"`, `"projector"`. Example: `[{"id":0,"name":"Global Variables","type":"global"},{"id":100,"name":"Layer 1","type":"layer"},{"id":1005,"name":"PJ_Main","type":"projector"}]`.
- Variables Query Mode (`id >= 0`): `id == 0` lists all global variables. `id > 0` checks whether the id matches a Layer; if not, whether it matches a Projector; returns the variables in that container.
- Variables Query response: bare array of `{id (int), name (string), type (string), value}`. Examples: `{"id":10,"name":"MasterFader","type":"float","value":"1.0"}` and `{"id":101,"name":"LayerOpacity","type":"float","value":"0.9"}`. Note `value` is a JSON string here even for type `float`.

**`variable.get`**: gets current values for a list of variable IDs, across any container.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | `array` | Required | List of variable IDs, for example `[10, 101]` |

- Response fields: `values` (object keyed by the variable ID as a string). Example: `{"values":{"10":1.0,"101":0.9}}`. Values are JSON numbers here.

**`variable.set` / `variable.update`**: sets or updates one or more variables. Supports `float`, `int`, `bool`, `string`. Mutates state. Accepts either a single variable (`id` and `value`) or a batch map (`values`).

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int` | Optional | Variable ID (required if updating a single variable) |
| `value` | `any` | Optional | New value (`float`, `string`, `int`, `bool`) |
| `values` | `object` | Optional | Key-value dictionary `{ "<id>": value }` for batch updates |

- Response: `{}`.
- Single string: `{"method":"variable.update","params":{"id":10,"value":"Welcome to Stage A"}}`
- Single float: `{"method":"variable.update","params":{"id":11,"value":42.5}}`
- Batch map: `{"method":"variable.set","params":{"values":{"10":"Main Stage","11":0.8}}}`
- The page writes the two names with a slash and uses both in examples, with the same parameters. It does not describe any difference between them.
- Unclear: only `float`, `int`, `bool` and `string` are listed. The page does not say how, or whether, other variable types (for example the Event type used for Global Cues) can be set or triggered.
- Unclear: whether a batch `values` update is applied atomically in one frame is not stated.

### 2.10 Undo / Redo (`undo.*`)

**`undo.undo`**: reverts the last action, equivalent to pressing Ctrl+Z in LightAct.

- Parameters: none. Response: `{}`.

**`undo.redo`**: redoes the last reverted operation, equivalent to pressing Ctrl+Y in LightAct.

- Parameters: none. Response: `{}`.
- Unclear: the page only says these equal Ctrl+Z / Ctrl+Y. It does not say whether they can revert actions made by an operator in the UI or by another client, and it gives no way to see what will be undone.

### 2.11 Real-time subscriptions (`subscribe`, `unsubscribe`)

**`subscribe`**: subscribes to live parameter updates or event notifications without polling.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `topic` | `string` | Required | Topic name (see list below) |
| `ids` | `array` | Optional | Specific object IDs to monitor (empty or omitted monitors all) |
| `maxRate` | `float` | Optional | Maximum notification rate in Hz. Default `30`, clamped between 1 and 120 Hz. |

- Response fields: `subscriptionId` (int, example `1`).
- Every subscription topic on the page (five):
  1. `"variable.changed"`
  2. `"timeline.state"`
  3. `"timeline.time"`
  4. `"output.changed"`
  5. `"layer.changed"`
- Request example: `{"jsonrpc":"2.0","id":30,"method":"subscribe","params":{"topic":"variable.changed","ids":[10],"maxRate":30}}`
- Notification (no `id`, sent automatically when the value changes): `{"jsonrpc":"2.0","method":"variable.changed","params":{"subscriptionId":1,"values":{"10":0.72}}}`
- Notification fields for `variable.changed`: `method` = the topic name, `params.subscriptionId` (int), `params.values` (object keyed by variable ID as a string).
- Unclear: the notification payload is shown only for `variable.changed`. The payloads for `timeline.state`, `timeline.time`, `output.changed` and `layer.changed` are not documented.
- There is no topic for sections, markers, projectors or project changes.

**`unsubscribe`**: cancels an active subscription.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `subscriptionId` | `int` | Required | Subscription identifier received from `subscribe` |

- Response: `{}`.

### 3. Testing with Hercules Setup Utility (raw TCP)

1. Launch Hercules Setup Utility and open the TCP Client tab.
2. Module IP `127.0.0.1` (or `localhost`), Port `9899`.
3. Click Connect. Status shows `Connected`.
4. Type a JSON-RPC command, for example `{"jsonrpc":"2.0","id":1,"method":"system.performance"}`.
5. Click Send, or press Enter with `<CR><LF>` enabled.
6. The response comes back on the same connection, which stays open for further commands.

### Inconsistencies and gaps in the page's own examples

1. Version: the page says the API needs LightAct 4.18 or higher, but the `system.hello` response example shows `"lightactVersion":"4.1.0"`.
2. ID type: the conventions say IDs are 32-bit unsigned integers and the tables say `int`, but the `system.describe` example reports the `timeline.play` `id` parameter as type `"int64"`.
3. Variable value types: `variable.list` returns `"value":"1.0"` and `"value":"0.9"` (strings) for variables of type `"float"`, while `variable.get` returns the same variables as numbers (`1.0`, `0.9`) and the notification sends a number (`0.72`).
4. Variable 10: listed as `MasterFader`, type `float`, value `"1.0"`. The `variable.update` example then sets ID 10 to the string `"Welcome to Stage A"`, and the batch example sets `"10":"Main Stage"`. The subscription example reports it as `0.72`.
5. Variable 11: set in two examples (`42.5` and `0.8`) but never appears in any `variable.list` response.
6. ID overlap: `variable.list` shows variable `LayerOpacity` with ID `101` inside layer container `100`, while `layer.create` returns a new layer with ID `101`. The page does not say whether variable IDs and object IDs share one number space. `variable.list` resolving `id > 0` as "Layer, else Projector" implies layer and projector IDs do not collide, but that is not stated either.
7. Required flags that are not really optional: `section.trigger` lists `id` and `name` both as Optional but needs one of them. `variable.set` lists `id`, `value` and `values` all as Optional but needs either `id` + `value` or `values`.
8. Mutation markers: `output.setMaster`, all `timeline.*` transport methods, `section.trigger` and `undo.*` carry no "Mutates state" marker even though they change state. The `system.describe` example shows `timeline.play` with `"mutates":false`. What counts as "mutates" is not defined.
9. Undo coverage: only the three timeline create methods are marked "supports Undo". `projector.create` and every update and delete are marked "Mutates state" only. The page does not say whether `undo.undo` reverts those.
10. Request `id` values are reused across examples for different methods (6 for `project.save` and `timeline.list`; 16 for `section.trigger` and `layer.list`; 20 for `marker.list` and `projector.list`; 21 for `marker.create` and `projector.create`; 22 for `marker.update`, `projector.update` and `projector.delete`; 23 for `marker.delete`, `output.getMaster` and `variable.list`; 24 for `output.setMaster` and `variable.list`; 28 for `variable.update` and `undo.undo`; 29 for `variable.set` and `undo.redo`). The three `variable.set` requests use ids 27, 28, 29 but only one response (id 27) is shown. These are client-chosen numbers, so this is harmless, but do not read meaning into them.
11. Timeline parameter naming: `id` in `timeline.*`, `timelineId` in `section.*`, `layer.*`, `marker.*`.
12. Omitted timeline means different things: in the `*.list` methods "0 or omitted" lists everything across all timelines; in create and trigger methods omitted means the active timeline.
13. Parameter tables: `system.performance` has an explicit "none" table. `system.ping`, `system.describe`, `project.getInfo`, `timeline.list`, `projector.list`, `output.getMaster`, `undo.undo` and `undo.redo` have no table at all.
14. Wording: `output.getMaster` is described as returning "master volume opacity"; the field is `volume`.
15. Terminology: the section is titled "Sections / Cues" and methods speak of "cue sections", but no field or parameter says whether a section is used as a cue. `timeline.gotoLandmark` has `cue: true` to jump "exclusively to cue sections".
16. Play states: the Timelines UI has Play, Play and pause, Play and loop, Pause and Stop. The API documents only `timeline.play`, `timeline.pause` and `timeline.stop`.
17. `projector.list` returns `parentId` and `projector.create` accepts it, but `projector.update` does not list it.

### What the page does not document at all

- No methods for assets, canvases, Canvas Maps, throwers, video screens or other Viewport objects, Output Maps, LightNet, devices, DMX, OSC or MIDI.
- No methods to create, rename or delete timelines or timeline groups, or to set the Speed multiplier.
- No way to read or set a layer's content, template or mapping other than through its variables.
- No authentication, permissions, rate limits (other than `maxRate` on subscriptions) or error code list.

## For automation and pipelines

- Connect to port `9899`. WebSocket at `/api` is the transport the page recommends for plugins, the Python SDK and WebUI. How subscriptions work over HTTP POST is not documented. Raw TCP on the same port suits control systems (Crestron, Q-Sys). HTTP POST at `/api` suits one-shot calls.
- Requires LightAct 4.18 or higher. Call `system.hello` with `apiVersion: 1` and a `client` string first, and check `supportedApiVersions`. Whether hello is mandatory is not stated.
- Call `system.describe` at startup and build against what it returns. The page has enough internal contradictions (types, version string, value encoding) that the live schema should win.
- One request per message. JSON-RPC batch arrays are not supported yet.
- All times are float seconds from the start of the timeline, not frames or timecode. Colors are 0.0 to 1.0 RGBA. Positions are meters, rotations are degrees.
- IDs are integers handed out by LightAct. Get them from the `*.list` methods; create methods return `{"id": ...}`. Names are only accepted by `section.trigger` (case-insensitive).
- The route for feeding data into a show (text, numbers, switches from a database) is variables: find the container with `variable.list`, then push values with `variable.set` using the batch `values` map. Global Variables are container `0`; a layer's variables are in the container whose ID is the layer ID.
- Parse variable values defensively: `variable.list` gives strings, `variable.get` and notifications give numbers.
- Use `subscribe` instead of polling: topics `variable.changed`, `timeline.state`, `timeline.time`, `output.changed`, `layer.changed`, default 30 Hz, range 1 to 120 Hz. Only the `variable.changed` payload is documented, so log the others before relying on them.
- Cue firing from code: `section.trigger` by `id` or `name`, with `play` defaulting to `true`. `timeline.gotoLandmark` with `direction` `"next"`/`"prev"` and `cue: true` steps through cue sections.
- `timeline.stop` rewinds to 0.0. Use `timeline.pause` to hold position.
- `output.setMaster` is the blackout and master volume control (`opacity` 0.0 = black).
- Nothing is saved unless you call `project.save`. `project.getInfo` returns `dirty`.
- `undo.undo` is described as the same as Ctrl+Z in the application. The page does not say it is limited to your own client's actions, so do not assume it is. Only `section.create`, `layer.create` and `marker.create` are documented as undoable.
- Commands run on LightAct's main thread. The page gives no guidance on call rates, so keep bursts small during a show and watch `system.performance` (`fps`, `frameTimeMs`).
- No authentication is documented. Treat port 9899 as open to anything that can reach it.
