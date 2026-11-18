# Transitioning to LightAct from other media servers (digest)

What this section covers:
- Concept maps from Disguise and Pixera to LightAct windows and features.
- For Disguise: GUI, content mapping (Direct, Perspective, Sphere, Parallel), sequencing (layers, Art-Net and OSC control, keyframing, cues, multiple transports) and projector calibration.
- For Pixera: one page mapping its four tabs to LightAct windows.
- The pages are short and mostly point to other sections. LightAct states it is not an expert on the other products.

## Switching to LightAct
`docs/transitioning-to-lightact-from-other-media-servers/switching-to-lightact.md`
- Index page. Only Disguise and Pixera are covered. Nothing else useful.

## LightAct for Disguise Operators
`docs/transitioning-to-lightact-from-other-media-servers/lightact-for-disguise-operators.md`
- Disguise has three levels (Timeline, Stage, Feed). LightAct uses separate windows instead.
- Mapping table:
  - Stage level: Stage -> Viewport
  - Timeline level: Manipulator Editor -> Viewport Toolbar
  - Timeline level: Track Editor -> Timelines Window, Timeline Editor Window
  - Feed level -> Output Maps Window

## GUI Overview
`docs/transitioning-to-lightact-from-other-media-servers/lightact-for-disguise-operators/gui-overview.md`
- LightAct uses dockable windows saved into Workspaces.
- Dashboard -> Top Bar (where all windows can be reached).
- Track Editor -> Timeline. In LightAct a Track is a lane inside a Timeline where layers are placed. A Timeline has one or more tracks. A project can have several Timelines, managed in the Timelines window.
- Layers in LightAct are not strictly defined and are fully customisable.
- Stage -> Viewport window.
- Feed -> Output Maps Window.
- Devices: in LightAct devices are nodes in the Devices window. They cover Network devices, Trackers, MIDI, Content I/O and Audio devices, for both receiving and sending.
- DMX is the exception: there is no DMX device node. Use the dedicated DMX In and DMX Out windows.
- Transport: timecode (such as LTC or MIDI) is received in the Devices window.
- Unclear: several links on this page are broken, and the timecode sync link points to an internal GitBook editor URL.

## Content Mapping
`docs/transitioning-to-lightact-from-other-media-servers/lightact-for-disguise-operators/content-mapping.md`
- Since LightAct 4.8, layers can be mapped: directly to viewport objects such as video screens; to canvases (similar to Disguise Feed Maps); to throwers (similar to Disguise Mappings such as Perspective or Spherical).
- Fast workflow: most mappings are made by dragging an arrow from the viewport object or canvas to a layer.
- Direct mapping: a Layer can map to any Viewport object, any Canvas or a Device.
- Perspective mapping -> Perspective Thrower.
- Sphere mapping -> Spherical Thrower.
- Cubic mapping is also possible -> Cubic Thrower.
- Parallel mapping -> Orthogonal thrower.

## Content Sequencing
`docs/transitioning-to-lightact-from-other-media-servers/lightact-for-disguise-operators/content-sequencing.md`
- Layers sit in Timeline tracks. All layers, including stock templates, are built from nodes and can be customised, but normal use only needs the layer variables.
- Art-Net or sACN control of a layer variable: click the variable's DMX icon. Incoming DMX data is set and viewed in the DMX In window.
- OSC control of a layer variable: click the variable's OSC icon. First set up an OSC Receiver device node, then map values to Layer variables in the OSC In window.
- Keyframing -> Curve Editor. Enable the Curve Editing icon on the variable, select it in the Curve Editor, then add and move keyframes.
- Cues: a Disguise Cue equals a LightAct Marker or Section with "Use as Cue" enabled.
- Multi-transport Manager -> several Timelines in one project, run independently, managed in the Timelines window.
- Timecode sync: create a Device that receives the timecode, then select it in the Sync dropdown of the Timeline in the Timelines window.

## Projection Mapping
`docs/transitioning-to-lightact-from-other-media-servers/lightact-for-disguise-operators/projection-mapping.md`
- Manual calibration: map a Projector to an Object in the Viewport and adjust the Projector's properties. Many of these controls are reached by double-clicking a projector and opening its Layout tab.
- Quick Cal -> 3D Cal Projector Calibration, found in the Setup window of any Projector under the 3D Cal tab.
- OmniCal -> Iris.

## LightAct for Pixera Operators
`docs/transitioning-to-lightact-from-other-media-servers/lightact-for-pixera-operators.md`
- Pixera tab to LightAct window:
  - Screens -> Viewport
  - Mapping -> Viewport, Output Maps, Canvas Maps
  - Compositing -> Timelines Window, Timeline Editor
  - Control -> Layer Layouts, WebUI, Devices
- The Control tab's job (reacting to external inputs) is done with Layer Layouts and WebUI.

## For automation and pipelines
- External control of a layer variable is enabled per variable: a DMX icon (Art-Net or sACN, configured in DMX In) and an OSC icon (needs an OSC Receiver device node, mapped in OSC In). There is no expression language like Disguise's.
- A cue is a Marker or a Section with "Use as Cue" enabled. Build cue lists from those two object types.
- Timelines run independently. Timecode chase is set per Timeline through its Sync dropdown in the Timelines window, pointing at a receiving Device node (LTC or MIDI).
- Devices are nodes in the Devices window, except DMX, which has its own DMX In and DMX Out windows.
- Mapping targets for a layer: a Viewport object, a Canvas, a Thrower (Perspective, Spherical, Cubic, Orthogonal) or a Device. Layer-to-object direct mapping arrived in LightAct 4.8.
- Custom control logic that Pixera users would put in the Control tab belongs in Layer Layouts and WebUI.
