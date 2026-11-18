# Index of LightAct digests

Read this first. Pick the digest that matches the question, read it, then open the manual page it cites in `docs/` when exact wording matters.

LightAct in one paragraph: a Windows media server. A project holds one or more **Timelines** (grouped in **Timeline groups**). A Timeline has **Tracks**, and on them **Layers**, **Sections** and **Markers**. Every Layer is a node graph (a **Layer Layout**) made from a **Layer template** such as Video, Audio or Notch, and is controlled through its **Layer variables**. Layers render to **Mappings**: Viewport objects, **Canvases** or **Throwers**. **Output Maps** send those to physical outputs. Media files are **Assets**. Several servers work together as a **LightNet** cluster with one **Primary**.

## By question

| If the question is about | Read |
|---|---|
| Driving LightAct from code, plugins, JSON-RPC, subscriptions | [api.md](api.md), then the page itself: `docs/api/lightact-api.md` |
| What a layer can do, layer variables, templates, fades, crossfades, curve editor, layer connections | [layers-and-layouts.md](layers-and-layouts.md) |
| A specific node, its pins and properties | [node-reference.md](node-reference.md) |
| Media formats, codecs, file naming, versions, ingestion, FileWatcher | [assets.md](assets.md) |
| Playback smoothness, buffering, proxy files, server performance figures | [video-playback.md](video-playback.md) |
| Timelines, sections, markers, cues, cue list, chasing timecode | [timelines.md](timelines.md) |
| Triggering cues or setting variables from outside by OSC or MIDI | [osc-and-midi.md](osc-and-midi.md) |
| DMX, Art-Net, sACN, fixtures, pixel mapping, DMX cue triggering | [dmx.md](dmx.md) |
| More than one server, Primary and Secondary roles, Backup, asset transfer, sync | [lightnet.md](lightnet.md) |
| Getting content from layers onto screens, canvases, throwers | [content-mapping.md](content-mapping.md) |
| Video outputs, Output Maps, displays, GPU and Mosaic setup | [output-setup.md](output-setup.md) |
| Projectors, calibration, warping, blending | [projection-mapping.md](projection-mapping.md) |
| Notch, Unreal Engine, TouchDesigner | [real-time-content-playback.md](real-time-content-playback.md) |
| Audio, LTC, TCP and UDP, capture cards, NDI, camera and object tracking | [integrations.md](integrations.md) |
| LightTrack | [lighttrack.md](lighttrack.md) |
| Launch arguments, WebUI and REST | [miscellaneous.md](miscellaneous.md) |
| Keyboard shortcuts, interface, terms, support requests, troubleshooting | [quick-start.md](quick-start.md) |
| Translating disguise or Pixera concepts | [transitioning-to-lightact-from-other-media-servers.md](transitioning-to-lightact-from-other-media-servers.md) |
| Building or preparing a server, Windows and GPU settings | [preparing-your-hardware-for-lightact.md](preparing-your-hardware-for-lightact.md) |
| Licence tiers and activation | [licensing.md](licensing.md) |
| When a feature arrived or how behaviour changed between versions | [release-changelogs.md](release-changelogs.md) |

## Questions that span several digests

- **Building a tool that programs a show from data** (a database, a cue sheet, an EDL): [api.md](api.md) for what code can do, [layers-and-layouts.md](layers-and-layouts.md) for the layer variables that hold the asset, mapping and in and out points, [timelines.md](timelines.md) for sections, cues and timecode, [assets.md](assets.md) for naming and versions.
- **Designing a content delivery pipeline**: [assets.md](assets.md) for formats and version naming, [video-playback.md](video-playback.md) for codecs, proxies and performance, [lightnet.md](lightnet.md) for how files reach every server.
- **Remote control during a show**: [osc-and-midi.md](osc-and-midi.md), [dmx.md](dmx.md), [api.md](api.md), [miscellaneous.md](miscellaneous.md) for WebUI, and [timelines.md](timelines.md) for the Cue list.
- **A redundant or multi-server system**: [lightnet.md](lightnet.md), [output-setup.md](output-setup.md), [licensing.md](licensing.md) for which tiers allow which roles.

## Every digest ends the same way

Each digest closes with a section called "For automation and pipelines". If you are building a tool, read those sections across the digests you need before anything else.
