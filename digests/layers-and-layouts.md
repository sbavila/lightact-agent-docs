# Layers and Layouts (digest)

What this section covers:
- What a Layer is, its fixed properties (End, State, Locked, Fades, Notes) and how layers are created from templates.
- Layer Layouts, LightAct's node-based visual scripting system: nodes, Lifeline action flow, execution order, a few Computer Vision and Texture Processing nodes.
- Variables: Layer variables vs Global variables, the full list of variable types, variable groups (Private, static, Dynamic), getters and setters.
- Layer connections (passing textures and data between layers), fades, cross-fades and the Curve Editor.
- Every Stock Layer Template (Content, Generative, Control) with its variable groups and variables. These variables are what gets set from the Properties window, DMX, OSC, curves and layer connections.

Note on names: variable and group names below are copied as the manual prints them. This section does not say how the API addresses a variable (by group, name or index), so treat these as display names.

## Overview
`docs/layers-and-layouts/overview.md`
- A Layer is built from nodes. The node graph lives in a Layer Layout. Layer Layouts is LightAct's node-based visual scripting system.
- A variable is a placeholder for a value (integer, float, boolean and more).
- A layer saved for reuse is a Layer Template. Two kinds: Stock Layer Templates (shipped with every install) and User Layer Templates (made by users).
- The manual uses "layer templates", "templates" and "layers" interchangeably.
- In most projects the stock templates are enough and no node editing is needed.

## Layers
`docs/layers-and-layouts/layers.md`
- Two ways to create a layer: Blank layers (advanced, built from scratch) or Layer templates (normal route).
- Every layer has the same Properties:
  - End (HMSF): time of the end of the layer.
  - State: Enabled (executes when the playhead is on it in an active timeline), Disabled (never executes), Preview only (executes, but Render Texture nodes do not render to mappings, so content shows in the track thumbnail but not on mappings or outputs).
  - Locked: if checked the layer cannot be edited.
  - Fades: see Fade in and Fade out, and Cross-fade.
- Layer Notes: check the Notes checkbox, then type. A `*` appears next to the Layer name and the note shows on hover.

## Fast layer workflows
`docs/layers-and-layouts/fast-layer-workflows.md`
- Insert a layer by: right-click menu in the Timeline; right-click then type the template name or a search keyword and press Enter; a shortcut; or dragging an asset onto the Timeline.
- Shortcut forms: hold the template key and click with left mouse button (video: V+LMB), or hold Alt and press the key (video: Alt+V). The mouse must be in the Timeline editor window.
- Unclear: the Shortcuts page in quick-start says "V + right click", this page says V + left mouse button.
- Dragging an asset onto the Timeline opens a popup listing every template that has the asset type in its name (a video asset offers all templates with "Video" in the name).
- Dragging any object or asset onto an existing layer sets all variables of the matching type. A video asset sets all video asset variables. A mapping (for example a video screen) sets all Mapping variables.

## Layer Connections
`docs/layers-and-layouts/layer-connections.md`
- Layer connections share data and content between Layer variables in different layers. Described as more streamlined than Global variables. Mostly used to pass textures.
- Alt + drag from one layer to another creates a connection that copies all Texture variables of the Source layer to all Texture variables of the Destination layer.
- Connections for non-texture variables must be made in the Layer connections window (Window top menu).
- Layer connections window: a table with Source and Destination columns, each with 3 sub-columns that pick the source or destination variable.
- Disable a connection temporarily with the eye icon. Delete it in the window or by right-clicking a layer and choosing Delete layer connections.
- Example in the manual: drag from the Video screen to a Scroll texture layer (sets its mapping), then Alt + drag from a Color grid layer to the Scroll texture layer.

## Fade in and Fade out
`docs/layers-and-layouts/fade-in-and-fade-out.md`
- Timelines, Sections and Layers all have Fade in and Fade out, but they behave differently.
- Timeline fade in/out does not act at the start or end of the Timeline. It applies when the Timeline switches play modes. Example: fade in 3 seconds, timeline stopped, pressing play fades content in over 3 seconds wherever the playhead is.
- Apply fade to Pause (Timeline): checked means the fade applies when switching between any play state and Pause or Stop. Unchecked means only between any play state and Stop.
- Section Fade in/out applies to all layers at the beginning and end of the section.
- Layer Fade in/out applies to that layer only.
- Layer fades and Section fades multiply with each other.

## Cross-fade
`docs/layers-and-layouts/cross-fade.md`
- Cross-fade applies when jumping from one part of the timeline to another. Set on Timeline, Section or Layer.
- The Timeline's Cross-fade applies to sections and layers only where their Cross-fade is set to Inherit.
- Section and Layer options:
  - Inherit: a Section inherits from the Timeline, a Layer inherits from its Section.
  - FadeDip: outgoing layer fades down while incoming fades up. Slight dip in overall brightness/opacity.
  - FadeHold: origin layer stays at its opacity while the destination fades up over it. Overall brightness/opacity unchanged.
- Cross-fade time can be typed only when Cross-fade is not Inherit.
- Cross-fade does not work when jumping from one point to another on the same layer.
- For sections, LightAct always uses the cross-fade time of the destination section.

## Curve Editor
`docs/layers-and-layouts/curve-editor.md`
- Animates variable values over time.
- Enable: select the Layer in the Timeline Editor, find the variable in the Variables section of the Properties window, click the curve icon next to it (works on one or several variables). Click the second icon next to an enabled variable to view and edit its curve.
- Add points: right-click in the Curve Editor, then "Add point on playhead" or "Add point here". Changing the variable value in Properties with the Playhead at a position also creates or edits a point.
- Multi-component variables: click a point on one curve first, then right-click and add, to edit only that component.
- Move a selected point vertically with Scroll, horizontally with Shift + Scroll.
- Color variables can be set in the Curve Editor with the color picker.
- Delete a point: right-click Delete, the Del key, or double-click it. "Reset curve" in the right-click menu removes all user-added points.
- Unclear: this page says double-click deletes a point, the Shortcuts page says double-click in the Curve Editor adds a point.

## User Layer Templates
`docs/layers-and-layouts/user-layer-templates.md`
- Any layer becomes a template via right-click, Template -> Create from layer. Name it and click Create. It then appears in the Timeline track right-click menu under User templates.
- To be offered in the Asset suggestion menu (the popup when an asset is dragged to the Timeline), the template name must contain at least one of: Video, Image, Audio, Notch.
- Manage in Edit -> Preferences Window, Files tab, Layer Templates section: Duplicate, Rename, Delete, and assign shortcuts.
- After adding or deleting a template, click Refresh list to see the change.

## Layer Layouts
`docs/layers-and-layouts/layer-layouts.md`
- Open the Layer Layout window by double-clicking a Layer in the Timeline. Layer Variables are on the right-hand side.
- Right-click the empty area to browse the node library, with a Search field.
- Drag from a node's input or output and drop on empty space to get node recommendations.
- Layouts let you modify stock templates or build new ones.

## Nodes
`docs/layers-and-layouts/layer-layouts/nodes.md`
- Inputs on the left, outputs on the right.
- Action nodes have at least one Lifeline pin (lime, square). Basic nodes have none.
- Three special action nodes exist in every layer by default:
  - Tick: executes every frame while the playhead is on the layer.
  - On Begin: executes once when the layer first becomes active, usually when the playhead touches the left side of the layer.
  - On End: same, at the end of the layer.
- Node controls: Preview icon (on some nodes) and Bypass icon (node does not execute at all, handy on texture processing nodes).

## Node Action Flow
`docs/layers-and-layouts/layer-layouts/nodes/node-action-flow.md`
- Action flow decides which nodes execute. It is set by Lifeline connections, and every Lifeline starts at a Lifeline generator node.
- Default generators: Tick, On Begin, On End.
- Other generators: many nodes have a "New message" lifeline output. They are meant for receiving network messages together with receiving Device nodes.
- Blinking connection lines show that a layer is active.

## Node Connections
`docs/layers-and-layouts/layer-layouts/nodes/node-connections.md`
- Lifeline: lime, square pins. One lifeline output connects to only one lifeline input. One lifeline input can take several lifeline outputs. This is the reverse of most other connection types.
- Two chain types: lifeline chain (nodes joined by lifeline) and sub-chain (nodes joined by other connection types). A sub-chain only executes if it is connected to the lifeline chain.
- Connection colour shows the data type. Examples: dark red is float, light blue is string.
- Only pins of the same colour connect, and only output to input.
- A connection is active only while the Playhead is on the layer and the connection leads back to a lifeline generator.

## Order of Node Execution
`docs/layers-and-layouts/layer-layouts/nodes/order-of-node-execution.md`
- With Tick as generator: (1) execute the node connected to Tick, (2) to do so, first execute all sub-chains connected to that node, (3) move to the next node on the lifeline, (4) finish when all connected nodes are done.
- Nodes not connected are not executed.
- The lifeline can be split with conditional nodes (the If node, with a boolean Input) or delayed.

## Computer Vision
`docs/layers-and-layouts/layer-layouts/nodes/computer-vision.md`
- Special variable type: CV Mat, also called CV. All Computer Vision nodes take CV in and give CV out.
- Convert nodes (Search menu, Utilities -> General, "Convert"): Texture to CV (drag from a Texture output pin) and CV to Texture (drag from a CV output pin). A typical CV workflow uses both.
- Keep the resolution of CV streams low to save system resources.
- Unclear: the variable types table calls this type "OpenCV", this page calls it "CV Mat" or "CV".

## Optical Flow
`docs/layers-and-layouts/layer-layouts/nodes/computer-vision/optical-flow.md`
- Compares current and previous frame. Output is a CV image in HSV: H is movement direction, V is velocity.
- Input pins: CV input; Scales number (higher is more detail, lower it if slow); Scales step (a ratio); Median filter size (higher is blurrier, raise for fast objects); Threshold magnitude (if the max magnitude in the image is below it, output is black); Dynamic magnitude (off: per-pixel magnitude divided by the Normalize magnitude parameter and stored in V. On: max magnitude maps to 255, min to 0, linear in between); Dynamic Flow (on: also uses results from the previous detection).
- Output pins: Output; Max magnitude (max velocity of detected parts, not normalised).
- For small fast objects, Scales number and Scales step can be reduced.

## Find Blobs
`docs/layers-and-layouts/layer-layouts/nodes/computer-vision/find-blobs.md`
- Finds groups of connected pixels in a CV input.
- Input pins: Input (CV Mat with 1, 3 or 4 channels); Filter by threshold (uses Min threshold and Max threshold); Filter by area (uses Min area and Max area); Min distance (blobs closer than this are merged); Max track count (max blobs in the output).
- Output pin: Relative X, Y, area. Formatted as x position/image width, y position/image height, blob area/image area.

## Mog2 Background Subtraction
`docs/layers-and-layouts/layer-layouts/nodes/computer-vision/mog2-background-subtraction.md`
- Separates foreground from background.
- Input pins: Input (CV Mat, 1, 3 or 4 channels); History (number of frames used to build the background image); Learn rate (below 0: chosen automatically. Equal to 0 or above 1: background is not updated. Exactly 1: background always updates with the last input); Threshold variance; Detect Shadows (shadows shown grey).
- Output pins: Output (foreground white, background black, shadows grey); Background (the background image).

## Combine
`docs/layers-and-layouts/layer-layouts/nodes/computer-vision/combine.md`
- Merges several CV Mats into one, for example overlapping cameras.
- Input pins: Resolution (width and height of the output CV Mat); Inputs (one pin per CV stream). Output pin: Output.
- Node properties: Add input and Remove input buttons. Minimum two inputs.
- Setup button opens the Setup window: each input is a polygon to reposition, reshape or rescale. Overlap combining modes: Max, Min, Sum, None. Selecting a polygon shows an Edit collapsible with Polygon points position (X and Y), Reset, Flip X, Flip Y. Right-click a polygon to scale or rotate.

## Subtract
`docs/layers-and-layouts/layer-layouts/nodes/computer-vision/subtract.md`
- Subtracts two CV inputs into one output that takes the resolution of the first input. A node property lets it output the absolute value.

## Convert CV Color
`docs/layers-and-layouts/layer-layouts/nodes/computer-vision/convert-cv-color.md`
- Node property Type converts the CV stream to grayscale, RGB or RGBA.

## Texture Processing
`docs/layers-and-layouts/layer-layouts/nodes/texture-processing.md`
- Texture processing nodes are under Utilities -> Texture in the Layer Layout search. Only LUT, Luma Key and Rotate are documented here.

## LUT
`docs/layers-and-layouts/layer-layouts/nodes/texture-processing/lut.md`
- Texture LUT node. Give it a Texture input and connect it to an active lifeline. In Node properties click Browse, pick the LUT file, then click Generate LUT.
- Supported: `*.3dl` and `*.cube` files, or a Texture as the LUT input.

## Luma Key
`docs/layers-and-layouts/layer-layouts/nodes/texture-processing/luma-key.md`
- Texture Luma Key node masks all pixels whose brightness is above the Luminance value. Needs a Texture input and an active Lifeline. Often paired with the Texture Blend node.

## Rotate
`docs/layers-and-layouts/layer-layouts/nodes/texture-processing/rotate.md`
- Texture Rotate node rotates a Texture around its centre by the Angle value. Needs a Texture input and an active Lifeline.

## Variables
`docs/layers-and-layouts/layer-layouts/variables.md`
- Two categories: Layer variables (accessible only within one layer) and Global variables (accessible throughout LightAct and also WebUI).
- Each variable holds one type of information. Types:
  - Float: number with a decimal point (1.6314)
  - Integer: whole number (5)
  - Boolean: true or false, shown as a checkbox
  - String: text
  - Color: RGBA, each 0 to 1, for example [1.0,1.0,1.0,1.0] is white
  - Texture: pointer to a texture in GPU VRAM
  - OpenCV: image for computer vision processing
  - Vec2: 2 floats, for example [1.231, 10.231]
  - Vec3: 3 floats, for example [543.12,-1.231,5.000]
  - Vec2 array, Vec3 array
  - Transform: Vec3 Position, Vec3 Rotation, Vec3 Scale
  - Transform array
  - Resolution: 2 integers, for example [1920,1080]
  - Timecode: HMSF, for example [00:02:12:32]
  - Canvas: reference to a canvas (marked obsolete)
  - Mapping: reference to a mapping
  - Viewport object: reference to a viewport object
  - LA Object: reference to a Timeline, Section, Layer, Marker or Video output
  - Device: reference to a Device node
  - Camera properties: Position, Rotation, FOV, Aspect ratio, Near clip, Far clip
  - Asset: reference to an Asset. Kinds: Video, 3D model, Audio, Notch block, Unreal, TouchDesigner component
  - Event: a Lifeline type
- Almost every type has a matching connection colour in Layouts.
- Unclear: the table describes "Vec3 array" as "An array of Vec2", which looks like a typo.

## Layer variables
`docs/layers-and-layouts/layer-layouts/variables/layer-variables.md`
- Seen on the right of the Layer Layout window (double-click a layer). Most also show under the Layer variables collapsible of the Layer properties.
- Individual Layer Variables can be hidden from the Properties window.
- Every layer has predetermined Layer variables in the General and DMX Variable groups. They cannot be deleted.
- Unclear: the variables inside General and DMX are not listed anywhere in this section.

## Global variables
`docs/layers-and-layouts/layer-layouts/variables/global-variables.md`
- Managed in the Global variables collapsible of any Layer Layout window, or in the Global variables window.
- Accessible throughout the program. Suited to global show control and passing data between layers.
- Create with the + icon in the Global variables section, pick a type, rename it. Example: one Float named Opacity driving two video layers. It appears with the same value in every layer's Layout.

## Variable groups
`docs/layers-and-layouts/layer-layouts/variables/variable-groups.md`
- Add a group with the Add button in the Layer Layout window.
- Private: a Layer Variable group marked Private is not visible in the Properties window.
- Static group from a node: right-click the node header, Create variable group. This makes a group named after the node, one variable per input pin, and Reference nodes wired to those pins. It keeps no link to the node afterwards.
- Dynamic Variable Group: keeps its link to the source node. For nodes whose input pins change, such as Play Notch: when the Notch asset changes, the pins and the group's variables change to match the Notch block's Exposed parameters.

## Variable management
`docs/layers-and-layouts/layer-layouts/variables/variable-management.md`
- Identical for layer and global variables.
- Create: + icon of the Custom variable group, pick a type. New variables land in Custom. "Add group" at the bottom of the Layer variables or Global variables collapsible adds a group.
- Reorder by dragging the variable icon. Move to another group by dragging onto that group's collapsible icon.
- Delete with the Trash icon, or right-click the Variable icon and Delete.
- Numeric variables: "Min and max" setting limits the range, and drag rate is adjustable.
- Appearance (right-click the Variable icon): Integer can show "As Integer" or "As Dropdown" (to name each integer). Float used for time can show "As Time" or "As Float".
- Use in a Layout: drag the variable in and choose Getter or Setter. Hold Shift or Ctrl while dragging to skip the menu. Getter reads the current value, Setter writes it.
- Reference Node Replacement: drag from a Variable icon onto an existing Reference node to repoint it. Useful after copying Reference nodes to other layers.
- Unclear: the manual does not say which of Shift or Ctrl gives a Getter and which a Setter.

## Stock Layer Templates
`docs/layers-and-layouts/stock-layer-templates.md`
- Shipped and updated with every install. Categories: Content, Generative, Control.
- All Content and Generative templates render a texture, except Audio. Control templates render nothing and play no audio.
- Variable group **Render** (stated as identical in all Content and Generative templates apart from Audio):
  - Blend mode: blend used when rendering onto the mapping. Options include Normal, Screen, Multiply "etc." (full list not given).
  - Opacity: opacity of the texture on the mapping.
  - Mapping: the mapping the texture is rendered on.
  - Clip mode: Pixel perfect (no stretching, scaling or cropping), Fit (scaled proportionally, may leave empty areas), Crop (fills the mapping, may crop), Stretch (fills the mapping, may distort).
  - Angle: rotation in degrees.
  - Anchor at center: unchecked rotates around the top left corner, checked around the centre.
  - X: horizontal move in pixels.
  - Y: vertical move in pixels.
  - Scale X: horizontal scale.
  - Scale Y: vertical scale.
  - Scale proportionally: if checked, Scale X is also used for the Y axis.
- Unclear: ranges and units for Opacity and Scale are not stated.

## Content Layer Templates
`docs/layers-and-layouts/stock-layer-templates/content-layer-templates.md`
- Content templates: Audio, Content input, Multi-layer, Notch, Video.
- All except Audio share the groups below and differ only in the group about the asset itself.
- **Render**: see Stock Layer Templates.
- **Resize**: Resize (checkbox, enables resizing); New resolution (target resolution when Resize is checked).
- **Flip**: Flip horizontal; Flip vertical.
- **Color adjustment**: Vibrance; Hue; Contrast; Brightness; Saturation.
- **Channel multiply**: multiplies each channel (Red, Green, Blue, Alpha) by a chosen factor.
- **Channel invert**: inverts each channel (Red, Green, Blue, Alpha).
- **Blur**: Blur strength (strength of the blur algorithm); Blur size (size of the area blurred).
- **Crop**: crop level "for every corner separately" in pixels.
- **Softedge**: softedge for all 4 corners. The Softedge node in the Layout allows finer control.
- **Warp**: 4 perspective warp points. The Warp node in the Layout allows finer control.
- Unclear: exact variable names inside Channel multiply, Channel invert, Crop, Softedge and Warp are not given in text (only in screenshots). Value ranges for all of these groups are not stated.
- Unclear: the Shortcuts page mentions an image layer and an "NDI or Spout" layer, but no Image template is listed here.

## Video
`docs/layers-and-layouts/stock-layer-templates/content-layer-templates/video-1.md`
- Category: Content. Plays video assets. (The file is `video-1.md`. `video.md` is the Multi-layer page.)
- **Render**: see Stock Layer Templates.
- **Media**:
  - Video asset: the video asset to play.
  - Speed multiplier: playback speed. 1 means unchanged.
  - Play mode: Normal (video follows the playhead position relative to the start of the layer); Free run (ignores playhead position, plays even when the timeline is paused, and if the playhead leaves and returns it resumes from where it was when the playhead left); Free run & restart (as Free run, but on return restarts from the Begin at position); Timecode (follows the Timecode device).
  - Loop: loop at the end.
  - Hold last frame: if checked and Loop is unchecked, holds the last frame after the end. Otherwise a black texture.
  - Begin at: start timecode within the asset. Earlier parts are never played.
  - End at: end timecode within the asset. Later parts are never played.
  - Loop in: with Loop checked, the timecode LightAct jumps back to.
  - Loop out: with Loop checked, the timecode it jumps from. Effectively overrides End at.
  - Frame blending: blends 2 consecutive frames when the video framerate differs from the project framerate. Leave checked in 99% of cases.
  - Timecode device: external timecode source, used only when Play mode is Timecode.
  - Video texture: the video frame is stored here and then passed through all texture processing steps. Useful as a Layer connection source.
  - Auto rename: layer always takes the name of the video asset currently playing.
- **Audio**: Audio output (Audio output device for embedded audio); Volume (volume of embedded audio).
- Other groups: see Content Layer Templates.

## Multi-layer
`docs/layers-and-layouts/stock-layer-templates/content-layer-templates/video.md`
- Category: Content. One layer that switches between Video, Notch or Device sources.
- **Render**: see Stock Layer Templates.
- **Media**: Source (Video asset, Notch asset or a Device node); Device texture (texture grabbed from the selected Device node, used as a Source texture for Layer connections).
- **Video**: same variables as the Video template.
- **Notch**: same variables as the Notch template.
- **Device**: same variables as the Content input template.
- Other groups: see Content Layer Templates.
- Unclear: here "Media" holds Source and Device texture, while in the Video template "Media" holds the video variables. Check the real layer before relying on group names.

## Notch
`docs/layers-and-layouts/stock-layer-templates/content-layer-templates/notch-layer-template.md`
- Category: Content. Plays Notch blocks. (The page intro says "video files", a copy-paste slip.)
- **Render**: see Stock Layer Templates.
- **Notch** (a Dynamic variable group, so extra variables appear to match the Exposed properties of the selected Notch block):
  - Asset: the Notch asset.
  - Resolution: resolution the Notch block renders at.
  - Layer: the Notch layer to play.
  - Render: whether the block renders every LightAct frame, or every second, third and so on. For machines that cannot hold framerate.
  - Play mode: Normal; Free run; Free run & restart (restarts from 0 on re-entry); Timecode. Same meanings as Video.
  - Timecode: external timecode source, used only when Play mode is Timecode.
- Other groups: see Content Layer Templates.

## Content input
`docs/layers-and-layouts/stock-layer-templates/content-layer-templates/content-input-template.md`
- Category: Content. Renders textures from Device nodes (for example NDI or live video input).
- **Render**: see Stock Layer Templates.
- **Device**:
  - Device: the Device this layer sources the texture from.
  - Device texture: the texture grabbed from that Device node. Used as a Source texture for Layer connections.
  - Auto rename: layer name shows the state of the variables.
- Other groups: see Content Layer Templates.
- Unclear: the page says "Notch variable group is a dynamic one" under the Device group. Probably copied from the Notch page.

## Audio
`docs/layers-and-layouts/stock-layer-templates/content-layer-templates/audio-template.md`
- Category: Content. Plays audio files. Renders nothing and has no Render group.
- **Audio**:
  - Audio: the audio asset to play.
  - Output: the Audio output device node to play through.
  - Volume: playback volume.
  - Loop: loop at the end.
  - Pan: for stereo, pans between the 2 channels.
  - Auto rename: described as taking the name of "the video asset that's currently playing" (copied text, presumably the audio asset).

## Generative Layer Templates
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates.md`
- Generate content in real time and render it. Listed: Channel mixer, Color grid, Gradient, Solid color, Checkerboard, Mapping ID, Text, Render time, Strobe, Texture to mapping, Scroll texture.
- Unclear: Send Texture has a page with "Category: Generative" but is missing from this list.

## Solid Color
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/solid-color.md`
- **Render**: see Stock Layer Templates.
- **Solid color**: Resolution mode (adapt to the mapping's resolution, or Custom); Resolution (used when Resolution mode is Custom); Color; Auto rename (layer name shows the state of the variables).

## Color grid
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/color-grid.md`
- **Render**: see Stock Layer Templates.
- **Color grid**: Resolution mode (adapt to mapping, or Custom); Resolution (when Custom); Columns; Rows; Grid line width (thickness of the line between cells); Auto rename (renames the layer based on the selected Mapping).

## Checkerboard
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/checkerboard.md`
- **Render**: see Stock Layer Templates.
- **Checkerboard**: Resolution mode (adapt to mapping, or Custom); Resolution (when Custom); Color; Auto rename (renames the layer based on the selected Mapping).

## Gradient
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/gradient.md`
- **Render**: see Stock Layer Templates.
- **Gradient**: Resolution mode (adapt to mapping, or Custom); Resolution (when Custom); Start color; End color; Start point (relative coordinates); End point (relative coordinates); Auto rename (renames the layer based on the selected Mapping).

## Text
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/text.md`
- Creates a small texture from typed text.
- **Render**: see Stock Layer Templates.
- **Text**: Text; Font color; Background color; Font size (sets the height of the texture); Auto rename.

## Render Time
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/render-time.md`
- Creates a small texture showing a time in seconds.
- **Render**: see Stock Layer Templates.
- **Time**:
  - Time: which time to show. Options: From beginning of timeline; From the end of timeline; From beginning of layer; From the end of layer.
  - Timeline: which timeline. Ignored for the layer options.
  - Layer: which layer. Ignored for the timeline options.
  - Seconds: the time value. Set by the layer itself (an output, readable).
  - Text before: text placed before the value.
  - Text after: text placed after the value.
  - Font color; Background color.
  - Font size: sets the height of the texture.
  - Auto rename.

## Mapping ID
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/mapping-id.md`
- Creates a texture for identifying screens.
- **Render**: the standard group plus Auto rename (renames the layer based on the selected Mapping).
- Unclear: the page's description is cut off mid-sentence ("It takes all the data from").

## Texture to Mapping
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/texture-to-mapping.md`
- Renders an incoming texture to a chosen mapping. Use several to send one texture to several mappings.
- **Render**: the standard group plus Texture (the texture to render, a Destination variable for a Layer connection) and Auto rename (renames the layer based on the selected Mapping).
- Needs a Layer connection: Texture must be the destination of another Source layer.

## Scroll Texture
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/scroll-texture.md`
- Scrolls a texture that arrives through Layer Connections.
- **Render**: see Stock Layer Templates.
- **Scroll**: Texture (destination of a Layer connection from the source layer); Speed; Vertical (checked scrolls vertically, otherwise horizontally); Auto rename.

## Channel mixer
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/channel-mixer.md`
- Takes 2 textures and reroutes their channels into one output texture.
- **Render**: see Stock Layer Templates.
- **Texture channel mixer**: Input 1 and Input 2 (both must come from other layers through Layer connections); R source, G source, B source, A source (dropdowns that choose which channel of the 2 inputs feeds each output channel).
- All generative layers feeding a Channel mixer must have Resolution mode set to Custom.
- For a black and white matte without alpha (white fully transparent, black fully opaque), set A source to that texture's R, G or B, not A.

## Strobe
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/strobe.md`
- **Strobe**: Mapping (must be a canvas set up as below); Delay (time between flashes, lower is faster); Spread (higher means more screens flash at once); Number of screens; Strobe color; Auto rename.
- Setup: map the Strobe layer to a canvas (resolution does not matter), create one sub-area per screen on that canvas, map each sub-area to a video screen with "Stretch to target". Number of screens must match the number of sub-areas.
- Unclear: the page lists no Render group and puts Mapping inside the Strobe group, although the Stock Layer Templates page says all Generative templates have Render.

## Send Texture
`docs/layers-and-layouts/stock-layer-templates/generative-layer-templates/send-texture.md`
- Sends a texture through a texture sender device in the Devices window, for example NDI or Spout.
- **Send texture**: Device (the sender device); Texture (the texture to stream, must be the destination of a Layer connection).
- No Render group is listed.

## Control Layer Templates
`docs/layers-and-layouts/stock-layer-templates/control-layer-templates.md`
- For data processing and show control. Listed: Receive message, Send message, Set timeline state, Go to marker, Go to section, Send DMX, Set fade, Set volume, Send PJLink.
- Unclear: Send PJLink is listed but has no page.
- All documented control templates keep their variables in a group called **Default**. Send message adds an **OSC** group.

## Receive message
`docs/layers-and-layouts/stock-layer-templates/control-layer-templates/receive-message.md`
- Receives messages from receivers such as UDP, TCP or OSC and triggers actions.
- **Default**: Device (the receiver device).
- Setup order: (1) in the Devices window create a Receiver device node and check its Receive checkbox, (2) insert the layer (Timeline right-click, Control, Receive message), (3) set Device, (4) open the Layout. In the Logic group of nodes there are Switch Case nodes. Wire the wanted Case output to an action node such as Go to marker or Go to section.
- The actions are wired in the Layout, not set by variables.

## Send message
`docs/layers-and-layouts/stock-layer-templates/control-layer-templates/send-message.md`
- Sends messages through sender nodes such as UDP, TCP or OSC.
- **Default**:
  - Device: the sender device to use.
  - Type: the type of the selected device. Decides whether a UDP, TCP or OSC message is sent. OSC options named in the text: OSC Float, OSC Int, OSC String.
  - Frequency: Run once (sent once each time the playhead enters the layer) or Delay (sent repeatedly with a delay while the playhead is on the layer).
  - Delay: delay duration when Frequency is Delay.
  - Message: the message to send.
- **OSC** (only used when Type is one of the OSC options): OSC Address; OSC Float; OSC Int; OSC String (the value sent for the matching Type).
- Setup: create a Sender device node in the Devices window and check its Send checkbox, then insert the layer and pick the device.
- Unclear: the full list of Type options and the unit of Delay are not given.

## Set Timeline State
`docs/layers-and-layouts/stock-layer-templates/control-layer-templates/set-timeline-state.md`
- Changes the play state of a Timeline.
- **Default**: Timeline; Play state; Auto rename.
- Unclear: the Play state description is cut off and its options are not listed.

## Go to Marker
`docs/layers-and-layouts/stock-layer-templates/control-layer-templates/go-to-marker.md`
- Jumps a Timeline to a Marker.
- **Default**:
  - Mode: Go to selected; Go to next; Go to previous.
  - Timeline: the timeline that jumps.
  - Marker: target marker. Ignored unless Mode is Go to selected.
  - Auto rename.
  - Print to console: prints a message to the Console window on every jump.

## Go to Section
`docs/layers-and-layouts/stock-layer-templates/control-layer-templates/go-to-section.md`
- Jumps a Timeline to a Section.
- **Default**: Timeline; Section (the target); Play state (the timeline's play state after the change, default "No change"); Auto rename; Print to console.
- Unclear: the Section description mentions a marker and a Mode variable that this template does not list (copied from Go to Marker). Play state options other than "No change" are not listed.

## Send DMX
`docs/layers-and-layouts/stock-layer-templates/control-layer-templates/send-dmx.md`
- Sends a DMX value without creating a DMX fixture.
- **Default**: Universe; Channel index; Channel value; Auto rename (layer name shows the variables' values).
- Requires the Send DMX checkbox to be enabled in the DMX Out window. The value can be checked there.

## Set Fade
`docs/layers-and-layouts/stock-layer-templates/control-layer-templates/set-fade.md`
- Changes the fade of a video output, a section or a layer.
- **Default**:
  - Mode: Video output Fade; Section Fade; Layer Fade.
  - Fade: target value. 1 is 100% (fully on), 0 is 0% (fully dimmed).
  - Speed: 1 means real-time. Small values such as 0.2 move slowly towards the target.
  - Auto rename.
- Unclear: the variable that selects which Video output, Section or Layer is not listed.

## Set Volume
`docs/layers-and-layouts/stock-layer-templates/control-layer-templates/set-volume.md`
- Changes the audio volume of a section or a layer.
- **Default**:
  - Mode: Section Volume; Layer Volume.
  - Master volume: target value. 1 is 100%, 0 is silent.
  - Speed: 1 means real-time. Small values such as 0.2 move slowly towards the target.
  - Auto rename.
- Unclear: the variable that selects which Section or Layer is not listed.

## For automation and pipelines
- Layers are the unit of everything: playback, generation and control. What you drive from outside is a layer's variables. Layer variables are scoped to one layer. Global variables are visible everywhere and in WebUI, so they are the natural shared control surface.
- Every layer also has fixed properties that are not variables: End (HMSF), State (Enabled, Disabled, Preview only), Locked, Fades, Cross-fade, Notes. "Preview only" runs the layer but sends nothing to mappings or outputs.
- Every layer has undeletable General and DMX variable groups. Their contents are not documented in this section.
- Private variable groups and hidden variables do not show in the Properties window. Expect variables to exist that an operator cannot see there.
- The Notch group is Dynamic: its variable list changes when the Notch asset changes, to match the block's Exposed parameters. Do not hard-code that list. The same applies to Notch variables inside Multi-layer.
- Common variable names across render templates, safe to target on any Content or Generative layer (except Audio, and possibly Strobe and Send Texture): Blend mode, Opacity, Mapping, Clip mode, Angle, Anchor at center, X, Y, Scale X, Scale Y, Scale proportionally.
- Video playback from a database: set Video asset, Play mode, Loop, Hold last frame, Begin at, End at, Loop in, Loop out, Speed multiplier. Timecodes are HMSF. With Loop on, Loop out overrides End at. Without Loop and without Hold last frame the layer shows black after the end.
- Play mode decides whether a jump restarts media: Normal follows the playhead, Free run resumes where it left off, Free run & restart starts from Begin at (video) or 0 (Notch), Timecode follows an external source.
- Auto rename changes the layer's name to match its asset, mapping or variable state. Do not use layer names as stable identifiers on layers with Auto rename checked.
- Dropdown variables (Play mode, Clip mode, Blend mode, Mode, Frequency, Source, R/G/B/A source and so on) are documented by option label only. The manual says Integer variables can be shown "As Dropdown", but does not state that these stock dropdowns are integers or give an index for each option. Confirm on a real layer.
- Textures move between layers only through Layer connections. Alt + drag wires all Texture variables at once. Templates that need an incoming connection: Scroll texture, Texture to mapping, Send Texture, Channel mixer. Source texture variables: Video texture (Video), Device texture (Content input, Multi-layer).
- Show control without code: Send message (UDP, TCP, OSC with OSC Address plus OSC Float, OSC Int or OSC String), Send DMX (Universe, Channel index, Channel value), Go to Marker, Go to Section, Set Timeline State, Set Fade, Set Volume. Receive message needs its actions wired in the Layout with Switch Case nodes.
- Send message with Frequency "Run once" fires each time the playhead enters the layer, not once per show. "Delay" repeats while the playhead stays on the layer.
- Dragging an asset onto the Timeline only offers templates whose names contain the asset type. User templates need Video, Image, Audio or Notch in the name to be suggested.
- Cross-fades do not happen for jumps within the same layer, and section jumps always use the destination section's cross-fade time. Section and Layer fades multiply.
- LUT files accepted by the Texture LUT node: `*.3dl` and `*.cube`.
- Render Time exposes Seconds as a variable the layer writes itself. This is a readable clock for "time from beginning or end of timeline or layer".
