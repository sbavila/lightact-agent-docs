# Node reference (digest)

## What this section covers

The LightAct 4 node reference: 316 pages, one per node plus one index page per category. There are 2 types of nodes: the ones in the *Devices* window (Device nodes) and the ones in the *Layouts* (Layout nodes). "Layouts" means *Layer Layouts*, *Projector Layouts* or *Mapping Layouts*.
Every node page is a stub: a one-line Description, then optional "Default inputs", "Default outputs", "Supported types" and "Search keywords". This digest groups nodes under the manual's own categories, in the manual's order, instead of one heading per page.
The pages give pin *types* only. No pin names, no properties, no defaults, no ranges, no units, no version numbers and no examples appear anywhere in this section.

## How to read this digest

- All source paths are under `docs/node-reference/node-reference/`. Each category heading gives its folder; each node gives its file name in backticks. Category index pages (`<category>.md` next to each folder) only list their nodes and are covered by the headings here.
- File names often differ from node titles (for example Sequence is `fork.md`, Render texture is `render-to-canvas-or-object.md`, Get data is `get-object-data.md`). The page title is the node name the manual uses.
- "In" = the page's "Default inputs", "Out" = "Default outputs", "Types" = "Supported types", "kw" = the page's "Search keywords". A field that is missing was not on the page.
- Pin types used: Lifeline, Event, Integer, Float, Boolean, String, String array, Color, Timecode, Vec2, Vec3, Vec2 array, Vec3 array, Transform, Transform array, Resolution, Texture, OpenCV, Audio, Camera properties, Asset, Device, Canvas, Mapping, Viewport object, LA Object.
- Unclear: no page lists properties, so the "properties" of every node are undocumented here.
- Unclear: the manual never explains "Supported types". Entries like `Vec2 -> Float` read as input type to output type for nodes whose pins change with the chosen type; plain entries like `Integer` read as the types the node accepts. This is not stated.
- Unclear: the type lists cannot be trusted as pin counts. Most pages list a type once even when the description needs two pins (Texture blend "blends two textures" but lists Texture once), yet Send MTC lists Timecode twice and Get System Date lists Integer four times.
- Unclear: "LA Object" is written "LAObject" on the Get marker and Get section pages.

---

# Layout nodes

`layout-nodes.md` lists 14 categories, in this order.

## Lifeline and actions
`layout-nodes/lifeline-and-actions-node-category/`

- **Tick** (`on-layer-tick.md`): Triggered every frame when layer is active. Out: Lifeline.
- **On Begin** (`on-layer-begin.md`): Triggered once when layer is started. Out: Lifeline.
- **On End** (`on-layer-end.md`): Triggered once when layer is ended. Out: Lifeline.
- **Sequence** (`fork.md`): Splits lifeline impulse. In: Lifeline. Out: Lifeline. kw: fork.
- **On shutdown** (`on-shutdown.md`): Triggered once when application is shutting down. Out: Lifeline. kw: close exit.
- **Key up/down** (`key-down.md`): Triggers event on key press. Out: Lifeline. kw: keypress, key press.
- **Switch case** (`switch-case.md`): Classic switch-case checker. In: Lifeline. Out: Lifeline. Types: Integer, Float, String, Vec2, Vec3, Timecode.
- **Run once** (`run-once.md`): Forwards tick until reset. In: Lifeline. Out: Lifeline.
- **Run every** (`run-every.md`): Runs on a set interval. In: Float. Out: Lifeline. Unclear: interval unit not stated.
- **Delayed tick** (`delayed-tick.md`): Delays tick trigger. In: Lifeline, Integer. Out: Lifeline. Unclear: delay unit not stated.
- **Cycle** (`cycle.md`): Cycles between outputs. In: Lifeline. Out: Lifeline.
- **For loop** (`for-loop.md`): Repeats until a condition is false. In: Integer, Lifeline. Out: Integer, Lifeline.
- **Foreach** (`foreach.md`): Executes for each element in an array. In: Integer, Lifeline. Out: Integer, Lifeline. kw: loop.
- **Run on marker** (`run-on-marker.md`): Runs when selected marker is reached. Out: Lifeline.
- **Go to marker** (`go-to-marker.md`): Moves the playhead to the selected marker. Looping is possible if "Go to next" or "Go to previous" is selected. In: Lifeline, Integer, LA Object. Out: Lifeline. kw: jump.
- **Go to section** (`go-to-section.md`): Jumps to specified section. In: Lifeline, LA Object, Integer. Out: Lifeline. kw: jump.
- **Go to landmark** (`go-to-landmark.md`): Jumps to next or previous timeline landmark. In: Lifeline. Out: Lifeline.
- **Set layer state** (`set-layer-state.md`), Deprecated: Sets layer state. In: Lifeline, Boolean. Out: Lifeline.
- **Get device status** (`get-device-status.md`), Deprecated, use Get data: Returns device status information. In: Device. Out: Boolean.
- **Set device status** (`set-device-status.md`): Sets device status information. In: Lifeline, Device, Boolean. Out: Lifeline. Not marked deprecated.
- **Get timeline state** (`get-timeline-state.md`), Deprecated: Gets timeline state. No pins listed.
- **Set timeline time** (`set-timeline-time.md`), Deprecated, use Set data: Sets timeline time. In: Lifeline, Timecode. Out: Lifeline.
- **Timeline time** (`get-timeline-time.md`), Deprecated: Returns timeline timecode. No pins listed.
- **Set timeline state** (`set-timeline-state.md`), Deprecated: Sets timeline time and state. No pins listed.
- **Timeline play** (`set-timeline-play.md`), Deprecated, use Set timeline state: Controls timeline playback state. No pins listed.
- **Color to texture** (`color-to-texture.md`): Constructs a texture based on input color. In: Resolution, Color. Out: Texture. kw: solid matte.
- **On project loaded** (`on-project-loaded.md`): Out: Event (the only node with an Event pin).
- Unclear: On project loaded's description reads "Unpacks JSON formatted string", which looks copied from JSON Unpack. Its real behaviour is implied by the title only.
- Unclear: Timeline play points to Set timeline state as its replacement, but Set timeline state is itself deprecated with no replacement named. Set data lists Timeline State and Timeline Time as targets.

## Texture generators
`layout-nodes/texture-generators-node-category/`

- **String to texture** (`string-to-texture.md`): Constructs a texture based on input string. In: String, Color, Integer. Out: Texture.
- **Texture label** (`texture-label.md`): Creates labeled texture. In: Resolution, String. Out: Texture.
- **Color grid** (`color-grid.md`): Creates grid texture. In: Resolution, Integer. Out: Texture.
- **Checkerboard** (`checker-board.md`): Renders checkerboard. In: Resolution, Color, Integer. Out: Texture.
- **Texture Gradient** (`gradient.md`): Creates gradient texture. In: Resolution, Color, Vec2. Out: Texture. kw: linear radial.
- Color to texture (solid colour) is filed under Lifeline and actions, not here.

## Texture processing
`layout-nodes/texture-processing-node-category/`

All output Texture unless noted.

- **Texture warp & blend** (`texture-warp.md`), Deprecated: Warps texture. In: Texture.
- **Texture blend** (`texture-blend.md`): Blends two textures together. In: Texture, Float, Boolean, Integer. kw: add, subtract, multiply, difference, lighten, darken, average, color burn, dodge, exclusion, glow, overlay, hard light, soft, screen, phoenix, negation, premultiplied alpha, hsv, hue, saturation.
- **Edge detection** (`texture-sobel-ed.md`): Finds edges by calculating the gradient of image intensity using the Sobel operator. In: Texture. kw: sobel.
- **Texture invert** (`texture-invert.md`): Inverts selected texture channels. In: Texture, Boolean.
- **Texture channel multiply** (`texture-channel-multiply.md`): Multiplies texture channels. In: Texture, Float.
- **Texture resize** (`texture-resize.md`): Resizes input by given width and height. In: Resolution. No outputs listed. Types: Texture -> Texture, OpenCV -> OpenCV.
- **Texture flip** (`texture-flip.md`): Flips input horizontally or vertically. In: Texture, Boolean.
- **Texture Blur** (`texture-blur.md`): Blurs a texture. In: Texture, Integer, Float.
- **Texture Modify** (`texture-adjust.md`): Adjusts hue, contrast, brightness, saturation and vibrance. In: Texture, Float. kw: hue brightness saturation vibrance contrast gamma.
- **To equirectangular map** (`cube-map-to-equirectangular-map.md`): Generates equirectangular projection texture. In: Resolution, Texture.
- **Texture rotate** (`texture-rotate.md`): Rotates texture. In: Texture, Float.
- **To cube map** (`to-cube-map.md`): Generates cube map projection texture. In: Resolution, Texture.
- **Texture crop** (`texture-crop.md`): Crops texture. In: Texture, Vec2.
- **Texture mask** (`texture-mask.md`): Creates texture mask. In: Resolution, Texture.
- **Texture softedge** (`texture-softedge.md`): Applies softedge on a texture. In: Texture, Vec2.
- **Texture perspective warp** (`texture-warp-perspective.md`): Applies perspective warp. In: Texture, Vec2.
- **Texture mesh warp** (`texture-warp-mesh.md`): Applies mesh warp. In: Texture.
- **Texture Luma Key** (`texture-luma.md`): Masks pixels if their luminance is above the specific value. In: Texture, Integer.
- **Texture LUT** (`texture-lut.md`): Applies LUT to an image. In: Texture. Unclear: how the LUT is supplied is not stated.
- **Texture distort** (`texture-distort.md`): Distorts input with k1, k2, p1, p2 and k3 arguments. In: Texture, Float.
- **Texture Chromakey** (`texture-chromakey.md`): "Block of a particular color in a texture". In: Texture, Color, Vec2, Integer.
- **Texture scroll** (`texture-scroll.md`): Cyclically scrolls a texture. In: Texture, Float, Boolean.
- **Texture swap** (`texture-swap.md`): Swaps textures based on ratio. In: Texture, Float.
- **Texture erode** (`texture-erode.md`): Erodes texture contents. In: Texture, Integer, Boolean.
- **Texture channel mixer** (`texture-channel-mixer.md`): Combines two textures with selected channels. In: Texture, Integer.
- **Vignette** (`vignette.md`): Applies vignetting effect on input. In: Texture, Color, Float.
- **Add frame delay** (`add-frame-delay.md`): Adds frame delay. In: Texture, Resolution, Integer. kw: latency sync.
- **Lens distort** (`lens-distort.md`): Lens distort. In: Texture, Float. kw: k1 k2 k3.
- **Texture to Monochrome** (`texture-to-monochrome.md`): Texture to Monochrome. In: Texture, Integer.

## Computer vision
`layout-nodes/computer-vision-node-category/`

Most of these take and return the OpenCV type, not Texture. Convert (Utilities) lists Texture -> OpenCV and OpenCV -> Texture.

- **MOG2 Background Subtraction** (`cv-background-subtraction-mog2.md`): Subtracts background from input and returns foreground mask. In: OpenCV, Integer, Float, Boolean. Out: OpenCV.
- **Find blobs** (`cv-find-blobs.md`): Finds all groups of connected pixels (blobs) in the image. In: OpenCV, Boolean, Float, Integer. Out: OpenCV, Vec3 array.
- **Optical flow** (`cv-optical-flow.md`): Optical flow. In: OpenCV, Float, Integer, Boolean. Out: OpenCV, Float.
- **Threshold** (`cv-threshold.md`): Performs thresholding on input. In: OpenCV, Integer. Out: OpenCV.
- **Erode** (`cv-erode.md`): Erodes input image. In: OpenCV, Integer. Out: OpenCV.
- **Dilate** (`cv-dilate.md`): Dilates input image. In: OpenCV, Integer. Out: OpenCV.
- **Convert CV color** (`cv-color-convert.md`): Converts input to a different color space. In: OpenCV. Out: OpenCV.
- **Combine** (`cv-combine.md`): Combines multiple images by performing perspective warp transformation on them. In: Resolution, OpenCV. Out: OpenCV.
- **Get LightTrack data** (`get-light-track-data.md`), Deprecated: Returns current LightTrack data in a transform array. In: Viewport object. Out: Transform array.
- **DepthImage** (`depth-image.md`): Returns scene depth texture. Out: Texture.

## Math
`layout-nodes/math-node-category/`

- **Waveform generator** (`waveform-generator.md`): Generates float value. In: Float. Out: Float. kw: wave sine square triangular sawtooth.
- **Add** (`sum.md`): Adds values together. Types: Integer -> Integer, Float -> Float, Vec2 -> Vec2, Vec3 -> Vec3. kw: sum.
- **Divide** (`divide.md`): Divides values. Types: same four as Add. kw: /.
- **Multiply** (`multiply.md`): Multiplies values together. Types: same four as Add. kw: *.
- **Negative** (`negative.md`): Returns negative value. Types: Integer, Float, Color, Vec2, Vec3 (each to itself).
- **Smooth value** (`smooth-value.md`): Smooths input value change over time. Types: same four as Add. kw: ease.
- **Increment** (`increment.md`): Increments a variable value by an amount. In: Lifeline. Out: Lifeline. Types: same four as Add. kw: ++.
- **Mod** (`mod.md`): Remainder of an integer division. In: Integer. Out: Integer. kw: %.
- **Remap** (`float-remap.md`): Remaps input to output. In: Float, Vec2. Out: Float.
- **Lerp** (`float-lerp.md`): Linear interpolation between two values based on alpha. In: Float. Out: Float.
- **Clamp** (`float-clamp.md`): Clamps value between min and max. In: Float, Vec2. Out: Float.
- **Trigonometry** (`float-trigonometry.md`): Calculates trigonometry based on the selected function. In: Float. Out: Float. kw: sin cos tan asin acos atan.
- **Subtract** (`subtract.md`): Types: OpenCV -> OpenCV, Integer -> Integer, Float -> Float, Vec2 -> Vec2, Vec3 -> Vec3. Unclear: the Description field holds keywords ("subtract + - math integer float vec2 vec3") and the keyword field holds "*"; the page looks mis-filled. Subtract is the only arithmetic node that lists OpenCV.
- **Generate value** (`value.md`): Generates a value. Types: Float, Integer, Boolean, String, Color, Timecode, Vec2, Vec3, Camera properties, Resolution. kw: simple construct.
- **Random float in range** (`rand.md`): Returns a random floating point number in range. In: Vec2. Out: Float.
- **Pose offset** (`pose-offset.md`): Applies additional transform to pose. In: Vec3, Boolean. Out: Vec3.
- **Coordinate system transform** (`coordinate-system-transform.md`): Transforms coordinate system values from one environment to another. In: Vec3. Out: Vec3. Unclear: which environments are supported is not stated.
- **Vector length** (`vector-length.md`): Returns vector length. Out: Float. Types: Vec2, Vec3. kw: size.
- **Float round** (`float-round.md`): Rounds a float to selected number of decimals. In: Float, Integer. Out: Float.
- **Float sqrt** (`float-sqrt.md`): Square root of a single-precision float. In: Float. Out: Float. kw: square root.
- **Absolute value** (`absolute-value.md`): Value of a number without its sign. Types: Float, Integer, Vec2, Vec3, Vec2 array, Vec3 array (each to itself). kw: abs.
- **Expression** (`expression.md`): Solves math expression with inputs. In: Float. Out: Float. Unclear: expression syntax is not documented.

## Logic
`layout-nodes/logic-node-category/`

- **If** (`if.md`): Condition node. In: Lifeline, Boolean. Out: Lifeline.
- **Not** (`bool-invert.md`): Inverts boolean input. In: Boolean. Out: Boolean.
- **Equals** (`equals.md`): Compares inputs. Out: Boolean. Types: Integer, Float, Boolean, String, Color, Texture, Timecode, Vec2, Vec3, Viewport object, Canvas, Mapping, Asset. kw: ==.
- **Larger** (`larger.md`): Compares inputs. In: Boolean (annotated "or equal"). Out: Boolean. Types: Integer, Float, Timecode. kw: >.
- **Larger or equal** (`larger-or-equal.md`), Deprecated, use Larger: Types: Integer, Float, Timecode. kw: >=.
- **Smaller** (`smaller.md`): Compares inputs. In: Boolean (annotated "or equal"). Out: Boolean. Types: Integer, Float, Timecode. kw: <.
- **Smaller or equal** (`smaller-or-equal.md`), Deprecated, use Smaller: Types: Integer, Float, Timecode. kw: <=.
- **In range** (`larger-or-equal-to-a-and-smaller-or-equal-to-b.md`): Returns true if X >= A and X <= B, false otherwise. In: Boolean. Out: Boolean. Types: Integer, Float, Timecode. Unclear: the Boolean default input is not explained.
- **Boolean logic** (`bool-logic.md`): Returns boolean output from two boolean inputs based on the selected logic operator. In: Boolean. Out: Boolean. kw: and or nand nor xor xnor.

## Content I/O
`layout-nodes/content-io-node-category/`

### Audio
`layout-nodes/content-io-node-category/audio-node-category/`

- **Play audio** (`play-audio.md`): Plays audio. In: Lifeline, Boolean, Float. Out: Lifeline, Float. Types: Audio, Device, Asset.
- **Get audio** (`get-audio.md`): Gets audio buffer from source audio. Out: Audio. Types: Asset.
- **Set audio** (`set-audio.md`), Deprecated: Sets audio buffer for target. In: Lifeline, Audio. Out: Lifeline. Types: Device.

### Nodes directly under Content I/O

- **Render texture** (`render-to-canvas-or-object.md`): Renders content to mapping. In: Lifeline, Mapping, Texture, Integer, Float. Out: Lifeline.
- **Play Video** (`video-player.md`): Plays video file or image sequence. In: Asset, String, Boolean, Float. Out: Texture, Timecode, Integer. kw: image sequence.
- **Play Notch block** (`play-notch-block.md`): Plays notch block contents. In: Asset. Out: Texture.
- **Set ndi stream** (`set-ndi-stream.md`): Sets ndi stream. In: Lifeline, Device, String, Boolean. Out: Lifeline.
- **Read ZED** (`read-zed.md`): Gets n-dimensional dense array from ZED device. In: Device. Out: Lifeline, OpenCV, Resolution. kw: receive.
- **Read RealSense** (`read-real-sense.md`): Same for RealSense device. In: Device. Out: Lifeline, OpenCV, Resolution. kw: receive.
- **Read OAK** (`read-oak.md`): Same for OAK device. In: Device. Out: Lifeline, OpenCV, Resolution. kw: receive.
- **Get texture** (`get-texture.md`): Gets texture from misc sources. Out: Texture. Types: Asset, Viewport object, Canvas, Mapping, Device, LA Object (each -> Texture).
- **Set texture** (`set-texture.md`): Sets object texture. In: Lifeline, Texture. Out: Lifeline. Types: Viewport object, Mapping, Device. kw: ndi spout deltacast.
- **Play TouchDesigner component** (`play-tox-file.md`): Plays TouchDesigner component file. In: Asset. Out: Texture. kw: touch designer engine.

## Data I/O
`layout-nodes/data-io-node-category/`

### UDP
`.../udp-node-category/`

- **Send UDP** (`send-udp.md`): In: Lifeline, Device, String. Out: Lifeline. Unclear: the page's description says "Sends TCP messages".
- **Read UDP** (`read-udp.md`): Reads UDP messages. In: Device. Out: Lifeline, String. kw: receive.

### TCP
`.../tcp-node-category/`

- **Send TCP** (`send-tcp.md`): Sends TCP messages. In: Lifeline, Device, String. Out: Lifeline.
- **Read TCP** (`read-tcp.md`): Reads TCP messages. In: Device. Out: Lifeline, String. kw: receive.

### OSC
`.../osc-node-category/`

- **Send OSC** (`send-osc.md`): Sends OSC message. In: Lifeline, Device. Out: Lifeline. Types: Integer, Float, String.
- **Read OSC** (`read-osc.md`): Reads OSC message. In: Device. Out: Lifeline. Types: Integer, Float, String. kw: receive.
- Unclear: where the OSC address is set is not shown (no String pin listed).

### Unreal Engine
`.../unreal-engine-node-category/`

- **Read UE data** (`read-ue-data.md`): Reads data from ue. In: Device, String. Out: Lifeline, Float. kw: receive.
- **Send UE data** (`send-ue-data.md`): Sends data to ue. In: Lifeline, Device, String, Integer. Out: Lifeline.

### DMX
`.../dmx-node-category/`

- **Get DMX** (`get-dmx.md`): Returns DMX universe channel value. In: Integer. Out: Integer.
- **Set DMX** (`set-dmx.md`): Sets DMX universe channel value. In: Lifeline, Integer. Out: Lifeline.
- **DMX by UV** (`dmx-by-uv.md`): Sends DMX data from absolute UV coordinates from CSV file. In: Lifeline, Texture, String. Out: Lifeline. kw: csv. Unclear: CSV format is not described here.
- **Get Art-Net in status** (`get-art-net-in-status.md`): Returns Art-Net boolean status. Out: Boolean. kw: dmx.
- **Get sACN in status** (`gets-acn-in-status.md`): Returns sACN boolean status. Out: Boolean. kw: dmx.
- **Set Art-Net in state** (`set-art-net-in-state.md`): Sets Art-Net in state. In: Lifeline, Boolean. Out: Lifeline. kw: dmx.
- **Set sACN in state** (`sets-acn-in-state.md`): Sets sACN in state. In: Lifeline, Boolean. Out: Lifeline. kw: dmx.
- Unclear: Get DMX and Set DMX list a single Integer type, so how universe, channel and value are split across pins is not shown.

### MIDI
`.../midi-node-category/`

- **Read MIDI** (`read-midi.md`): Reads MIDI messages. In: Device. Out: Integer. kw: receive.
- **Send MTC** (`send-mtc.md`): Sends midi timecode signal. In: Timecode, Device, Timecode. Out: Lifeline. Unclear: no Lifeline input is listed although Lifeline is an output.
- **Read MIDI CC** (`read-midicc.md`): Reads MIDI messages on Channel and Control. In: Device, Integer, Float. Out: Lifeline. kw: receive.
- **Read MIDI Note** (`read-midi-note.md`): Reads MIDI Note messages. In: Device, Integer, Float. Out: Lifeline. kw: receive.
- Unclear: Read MIDI CC and Read MIDI Note list Float as an input and no value output.

### Nodes directly under Data I/O

- **Read TUIO** (`read-tuio.md`): Reads TUIO messages. In: Device, Integer. Out: Lifeline, Vec2, Float. kw: receive.
- **Read from file** (`read-from-file.md`): Reads file stream into string. In: String. Out: String.
- **Write to file** (`write-to-file.md`): Writes file stream from string. In: Lifeline, String, Boolean. No outputs listed. kw: print.
- **Set string** (`set-string.md`): Sets string. In: Lifeline, Device, String. Out: Lifeline. Unclear: which device types accept a string is not stated.

## Trackers
`layout-nodes/trackers-node-category/`

Most take a Device and output Lifeline plus Vec3 values.

- **Read PSN** (`psn-node-category/read-psn.md`): Reads PSN messages. In: Device. Out: Lifeline, Vec3. Types: Integer -> Integer, String -> String. kw: receive.
- **Send PSN** (`psn-node-category/send-psn.md`): Sends PSN messages. In: Lifeline, String, Vec3. Out: Lifeline. Types: Integer -> Integer, String -> String. No Device input is listed.
- **Read MoSys** (`mo-sys-node-category/read-mo-sys.md`): Reads MoSys messages. In: Device, Integer. Out: Lifeline, Vec3, Integer, Float. kw: receive.
- **Read Stype** (`stype-node-category/read-stype.md`): Reads Stype messages. In: Device. Out: Lifeline, Vec3, Float. kw: receive.
- **Read FreeD** (`freed-node-category/read-free-d.md`): Reads FreeD messages. In: Device. Out: Lifeline, Vec3, Float. kw: receive.
- **Read OptiTrack** (`optitrack-node-category/read-opti-track.md`): Reads OptiTrack messages. In: Device, Integer. Out: Lifeline, Vec3. kw: receive.
- **Read Prime** (`optitrack-node-category/read-prime-coordinates.md`): Reads Prime camera data. In: Device, Integer. Out: Boolean, Vec3 (no Lifeline). kw: receive.
- **Read BlackTrax** (`blacktrax-node-category/read-rt-tr-p.md`): Reads BlackTrax messages. In: Device, String. Out: Lifeline, Vec3, Vec3 array. kw: rttrp.
- **Read Ncam** (`ncam-node-category/read-ncam.md`): Reads Ncam messages. In: Device, Integer. Out: Lifeline, Vec3, Float. kw: receive.
- **Read SPNet camera** (`spnet-node-category/read-sp-net-camera.md`): Reads spnet camera data. In: Device, Integer. Out: Lifeline, Vec3, Float. kw: receive.
- **Read SPNet object** (`spnet-node-category/read-sp-net-object.md`): Reads spnet movable object data. In: Device, Integer. Out: Lifeline, Vec3. kw: receive.
- **Read vive** (`vive-node-category/read-vive.md`): Reads vive tracker device. In: Device, Integer. Out: Vec3, Boolean (no Lifeline). kw: receive.
- **Read Antilatency** (`antilatency-node-category/read-antilatency.md`): Reads Antilatency data. In: Device, String. Out: Lifeline, Vec3. kw: receive.
- **Read tracker** (`read-tracker.md`): Reads tracker device (generic). In: Device, Integer. Out: Lifeline, Vec3. kw: receive.
- No layout read node is documented for the SICK device. ZED, RealSense and OAK read nodes sit under Content I/O, not Trackers.

## Array operations
`layout-nodes/array-operations-node-category/`

- **Viewport object by index** (`object-by-index.md`): Gets viewport object reference by index. In: Integer. Out: Viewport object.
- **Mapping by index** (`mapping-by-index.md`): Gets mapping reference by index. In: Integer. Out: Canvas. Unclear: the output is typed Canvas, not Mapping.
- **Array item by index** (`array-item-by-index.md`): Gets array item by index. In: Integer. Types: Vec2 array -> Vec2, Vec3 array -> Vec3, String array -> String, Transform array -> Transform.
- **Asset by index** (`asset-by-index.md`): Gets asset reference by index. In: Integer. Out: Asset.
- **Device by index** (`device-by-index.md`): Gets device reference by index. In: Integer. Out: Device.
- **Append** (`append.md`): Appends elements of same type. Types: String -> String, Vec2 array -> Vec2 array, Vec3 array -> Vec3 array, Vec2 -> Vec2 array, Vec3 -> Vec3 array, Transform -> Transform array, Transform array -> Transform array.
- **Size** (`size.md`): Returns array or string size. Out: Integer. Types: String, String array, Vec2 array, Vec3 array, Transform array. kw: length.
- Unclear: whether indexes start at 0 or 1 is not stated.

## Camera
`layout-nodes/camera-node-category/`

- **Get camera properties** (`capture-properties.md`): In: Viewport object. Out: Camera properties.
- **Create camera properties** (`create-capture-properties.md`): Creates camera properties object. In: Viewport object, Camera properties. No outputs listed. Unclear: Camera properties is probably the output, but the page lists it as an input.
- **Calculate FOV** (`calc-fov.md`): Calculates FOV. In: Float. Out: Float.
- **Set camera properties** (`set-capture-properties.md`): Sets camera properties for object. In: Lifeline, Viewport object, Camera properties. Out: Lifeline.
- **Camera offset** (`camera-offset.md`): Offsets camera position and rotation. In: Camera properties, Vec3. Out: Camera properties.

## Utilities
`layout-nodes/utilities-node-category/`

### Time
`.../time-node-category/`

- **Get system time** (`get-system-time.md`): Returns system time. Out: Timecode.
- **Get timecode time** (`get-timecode-time.md`): Returns timecode time. In: Device. Out: Timecode.
- **Get System Date** (`get-system-date.md`): Returns system date. Out: Integer x4. Day of week 0 means Sunday. Unclear: order of the four outputs is not given.

### String
`.../string-node-category/`

- **Split string** (`split-string.md`): Splits string by specified delimiter. In: String. Out: String array.
- **Substring** (`string-substring.md`): Returns substring by specified offset and length. In: String, Integer. Out: String.

### LightNet
`.../lightnet-node-category/`

All four are event sources with Out: Lifeline and kw: lightnet.

- **On LightSync session join** (`on-light-sync-session-join.md`): Triggers when machine joins LightSync session.
- **On LightSync session leave** (`on-light-sync-session-leave.md`): Triggers when machine leaves LightSync session.
- **On backup to primary** (`on-backup-to-primary.md`): Triggers when machine becomes primary (from backup).
- **On backup to secondary** (`on-backup-to-secondary.md`): Triggers when machine becomes secondary (from backup).

### Nodes directly under Utilities

- **Application tick** (`application-tick.md`): Gets current application tick. Out: Integer.
- **Write to log** (`write-to-log.md`): Writes string input to log. In: Lifeline, String, Integer. Out: Lifeline. kw: print.
- **Print to console** (`print-to-console.md`): Prints string input to console window. In: Lifeline, String, Color, Float. Out: Lifeline. kw: write.
- **Convert** (`converter.md`): Converts types. Types:
  - to Integer: from Float, Boolean, String
  - to Float: from Integer, Boolean, String, Timecode
  - to String: from Integer, Float, Asset, Boolean, Timecode, Vec2, Vec3, Resolution
  - to Boolean: from Integer, Float, String
  - Vec2 -> Resolution, Float -> Timecode, OpenCV -> Texture, Texture -> OpenCV
- **Explode** (`explode.md`): Explodes values. Types: Color -> Float, Vec2 -> Float, Vec3 -> Float, Timecode -> Integer, Resolution -> Integer, Camera properties -> Vec3, Camera properties -> Float, String -> String array, Transform -> Vec3, Transform array -> Vec3 array. kw: break.
- **Merge** (`merge.md`): Merges values. Types: Float -> Color, Float -> Vec2, Float -> Vec3, Integer -> Timecode, Integer -> Resolution, Vec3 -> Transform, Vec3 array -> Transform array. kw: join make.
- **Float to vec2** (`float-to-vec2.md`), Deprecated: Packages float values into vec2. No replacement named (Merge covers Float -> Vec2).
- **Float to vec3** (`float-to-vec3.md`), Deprecated: Packages float values into vec3. No replacement named (Merge covers Float -> Vec3).
- **To resolution** (`integer-to-resolution.md`), Deprecated: Creates resolution value from inputs. No replacement named (Merge covers Integer -> Resolution).
- **Get data** (`get-object-data.md`): Returns data. The general read node. Types:
  - Viewport object -> Video screen, Thrower, Projector, Iris, Fixture, Primitive, Imported 3D object, Null object, CalTrack system, Marker, Prop, LightTrack, Iris system
  - Asset -> Video, Audio, Image, Imported 3D model, Unreal engine project, Notch block, TouchDesigner component file
  - Machine data, Performance data (no source type listed)
  - Canvas -> Canvas, Mapping -> Mapping, Device -> Device
  - LA Object -> Layer, Section, Timeline, Timeline group data, Marker, Video output
  - Unclear: the fields returned for each type are not listed.
- **Texture resolution** (`texture-resolution.md`): Returns texture resolution. No pins listed. kw: size px.
- **Set data** (`set-object-data.md`): Sets data. The general write node. In: Lifeline. Out: Lifeline. Types:
  - Canvas -> Canvas Name, Canvas Resolution
  - Viewport object -> Name, Position, Transform, Rotation, Size, general data, Output opacity, 3D model mesh path
  - Asset -> Asset Name
  - LA Object (Timeline) -> Timeline Name, Duration, Fade in, Fade out, State, Time, master fade, volume, speed multiplier, Timeline group data
  - LA Object (Section) -> Section Name, Master fade, Master volume, Fade in, Fade out
  - LA Object (Layer) -> Layer Name, Master fade, Master volume, Fade in, Fade out, State, Start time, Duration
  - LA Object (Marker) -> Marker Name, Time, Action on playhead pass, Use as cue
  - LA Object (Video output) -> Video output Name, State, Fade
  - LA Object -> Prime camera params
  - Send Dmx (listed without a source type)
  - Unclear: value types, units and allowed values for each target are not listed.
- **Set object transform** (`set-object-transform.md`), Deprecated, use Set data: Sets object's transform. In: Viewport object.
- **Get object transform** (`get-object-transform.md`): Gets object's transform. In: Viewport object. Out: Transform. Not deprecated.
- **Get layer data** (`get-layer-data.md`), Deprecated, use Get data: Reads parent layer data.
- **Get name** (`object-name.md`): Returns object's name. No pins listed.
- **Fade in** (`fade-in.md`): Fades in from layer begin to target timestamp (page says "layer being"). In: Float. Out: Float.
- **Fade out** (`fade-out.md`): Fades out from target timestamp to layer end. In: Float. Out: Float.
- **JSON Pack** (`json-pack.md`): Packs inputs into JSON formatted string. Out: String. No inputs listed.
- **JSON Unpack** (`json-unpack.md`): Unpacks JSON formatted string. In: String. No outputs listed.
- **Get section** (`get-section.md`): Get section. In: LA Object (timeline), Integer (type). Out: LA Object (object or null).
- **Get marker** (`get-marker.md`): Get marker. In: LA Object (timeline), Integer (type). Out: LA Object (object or null).
- Unclear: how JSON Pack and JSON Unpack define their keys and pins is not documented. What the Integer "type" selects on Get section and Get marker is not documented.

## Miscellaneous
`layout-nodes/miscellaneous-node-category/`

- **Launch NDisplay** (`launch-n-display.md`): Launches NDisplay instance. In: Lifeline, String. Out: Lifeline.
- **Kill NDisplay** (`kill-n-display.md`): Kills NDisplay instance. In: Lifeline. Out: Lifeline.
- **Save project file** (`save-project.md`): Saves current solution to set directory. In: Lifeline, String. Out: Lifeline.
- **Open project file** (`open-project.md`): Opens project file. In: Lifeline, String. Out: Lifeline.
- **Run .bat file** (`run-bat-file.md`): Executes bat file. In: Lifeline, String. Out: Lifeline.
- **Set video output state** (`enable-or-disable-video-output.md`), Deprecated: Enables or disables video output. In: Lifeline, Boolean. Out: Lifeline. No replacement named (Set data has Video output State).
- **Get launch argument** (`get-launch-parameter.md`): Gets a launch argument by name. In: String. Out: String.
- **Get performance** (`get-performance.md`): Returns performance information. Out: Integer, Float.
- **Trigger volume** (`trigger-volume.md`): Trigger volume. In: Vec3 array, Viewport object. Out: Lifeline, Integer. kw: box sphere volume hit.

## Projection
`layout-nodes/projection-node-category/`

- **AutoBlend** (`autoblend.md`): Returns autoblend texture. Out: Texture.
- **Run autoblend** (`run-autoblend.md`): Triggers Autoblend's calculate. In: Lifeline, Boolean. Out: Lifeline.
- **Calibrate Iris camera** (`calibrate-iris-camera.md`): Computes world position based on inputs. In: Viewport object, Vec3 array, Vec2 array. Out: Lifeline. kw: 3dcal.
- **Run Iris calibration** (`run-iris-calibration.md`): Computes projector world position based on inputs. In: Viewport object, Lifeline. Out: Lifeline.
- **Send PJLink command** (`send-pj-link-command.md`): Sends PJLink command to projector. In: Lifeline, LA Object, Integer. Out: Lifeline. Unclear: the Integer to command mapping is not listed.
- **Projected points** (`projected-points.md`): Returns projected points texture. Out: Texture.

---

# Device nodes

`device-nodes.md` lists 3 categories: Content I/O, Data I/O, Trackers. Device node pages have a Description and sometimes Search keywords only. No pins, properties, ports, addresses or formats are listed for any device. Many layout nodes list a Device input.

## Content I/O (devices)
`device-nodes/content-io-node-category/`

### Video
`.../video-node-category/` (subfolders `ndi-`, `spout-`, `deltacast-`, `blackmagic-`, `directshow-capture-node-category/`)

- **NDI receiver** (`ndi-receiver-device.md`): Receives an NDI stream. kw: read.
- **NDI sender** (`ndi-sender-device.md`): Sends an NDI stream.
- **Spout receiver** (`spout-receiver-device.md`): Receives a Spout stream. kw: read.
- **Spout sender** (`spout-sender-device.md`): Sends a Spout stream. kw: send.
- **Deltacast receiver** (`deltacast-device.md`): Reads frame data from Deltacast capture card (page spells it "Delcast"). kw: read.
- **Deltacast sender** (`deltacast-sender-device.md`): Sends frame data to Deltacast capture card. kw: send.
- **Blackmagic receiver** (`blackmagic-device.md`): "Reads/sends data from/to Blackmagic capture card". kw: read. Unclear: titled receiver but described as read and send; there is no separate Blackmagic sender page.
- **DirectShow capture** (`ds-capture-device.md`): Captures device content using DirectShow. kw: read webcam.

### Audio
`.../audio-node-category/`

- **Audio output** (`audio-sender-device.md`): Audio output device.
- **Audio input** (`audio-receiver-device.md`): Audio input device. kw: read.

## Data I/O (devices)
`device-nodes/data-io-node-category/`

- **UDP sender** (`udp-node-category/udp-sender-device.md`): Sends data over the network using an UDP connection.
- **UDP receiver** (`udp-node-category/udp-receiver-device.md`): Receives data from the network using an UDP connection. kw: read.
- **TCP sender** (`tcp-node-category/tcp-sender-device.md`): Sends data over the network using a TCP connection.
- **TCP receiver** (`tcp-node-category/tcp-receiver-device.md`): Receives data from the network using a TCP connection. kw: read.
- **TUIO receiver** (`tuio-node-category/tuio-receiver-device.md`): Receives TUIO data from the network. kw: read.
- **OSC sender** (`osc-node-category/osc-sender-device.md`): Sends OSC data over the network.
- **OSC receiver** (`osc-node-category/osc-receiver-device.md`): Receives OSC data from the network. kw: read.
- **Texture share** (`unreal-engine-node-category/texture-share-receiver-device.md`): Reads Unreal Engine's shared texture. kw: unreal engine read receive.
- **UE data sender** (`unreal-engine-node-category/ue-data-sender-node.md`): Sends data to ue. kw: unreal engine.
- **UE data receiver** (`unreal-engine-node-category/ue-data-receiver-node.md`): Receives data from ue. kw: unreal engine read.
- **MIDI receiver** (`midi-node-category/midi-receiver-device.md`): Receives MIDI data. kw: read.
- **MIDI sender** (`midi-node-category/midi-sender-device.md`): Sends midi data. kw: send.
- **Iris camera** (`iris-camera-device.md`): Reads incoming camera stream.
- No DMX, Art-Net or sACN device node is listed in this section; DMX appears only as layout nodes (Get DMX, Set DMX, DMX by UV and the Art-Net / sACN in status and state nodes).

## Trackers (devices)
`device-nodes/trackers-node-category/` (one subfolder per vendor)

- **PSN receiver** (`psn-node-category/psn-receiver-device.md`): Receives PSN data from the network. kw: read.
- **PSN sender** (`psn-node-category/psn-sender-device.md`): Sends PSN data over the network.
- **MoSys receiver** (`mo-sys-node-category/mo-sys-receiver-device.md`): Receives MoSys data from the network. kw: read.
- **Stype receiver** (`stype-node-category/stype-receiver-device.md`): Receives Stype data from the network. kw: read.
- **FreeD receiver** (`freed-node-category/free-d-receiver-device.md`): Receives FreeD data from the network. kw: read.
- **OptiTrack data receiver** (`optitrack-node-category/opti-track-receiver-device.md`): Receives OptiTrack data from the network. kw: read.
- **OptiTrack camera receiver** (`optitrack-node-category/prime-camera-receiver-device.md`): Receives OptiTrack prime data from the device. kw: prime read slimx primex.
- **BlackTrax receiver** (`blacktrax-node-category/rt-tr-p-receiver-device.md`): Receives BlackTrax data from the network. kw: read RTTrP.
- **Ncam receiver** (`ncam-node-category/ncam-receiver-device.md`): Receives NCam data from the network. kw: read.
- **SPNet receiver** (`spnet-node-category/stage-precision-receiver-device.md`): Receives Stage Precision data from the network. kw: read.
- **Vive device** (`vive-node-category/vive-device.md`): Reads controllers location and orientation.
- **ZED receiver** (`zed-node-category/zed-receiver-device.md`): Receives ZED data from the device. kw: read.
- **RealSense receiver** (`realsense-node-category/real-sense-receiver-device.md`): Receives RealSense data from the device. kw: read.
- **OAK receiver** (`oak-node-category/oak-receiver-device.md`): Receives OAK data from the device. kw: read.
- **SICK Visionary camera receiver** (`sick-node-category/sick-visionary-receiver-device.md`): Receives SICK Visionary camera data from the device. kw: read.
- **Antilatency receiver** (`antilatency-node-category/antilatency-receiver-device.md`): Receives Antilatency data from the network. kw: read.

---

## Deprecated nodes (all in one place)

- Lifeline and actions: Set layer state, Get device status (use Get data), Get timeline state, Set timeline time (use Set data), Timeline time, Set timeline state, Timeline play (use Set timeline state).
- Texture processing: Texture warp & blend.
- Computer vision: Get LightTrack data.
- Logic: Larger or equal (use Larger), Smaller or equal (use Smaller).
- Content I/O: Set audio.
- Utilities: Float to vec2, Float to vec3, To resolution, Set object transform (use Set data), Get layer data (use Get data).
- Miscellaneous: Set video output state.

## For automation and pipelines

- This section is a catalogue, not a spec. It gives node titles, categories, pin types and search keywords. Pin names, properties, defaults, ranges, units, OSC addresses, ports and file formats are not here; take them from the other manual sections or from the node in LightAct itself.
- Two places hold nodes: Device nodes in the *Devices* window and Layout nodes in *Layer Layouts*, *Projector Layouts* and *Mapping Layouts*. Layout read and send nodes list a Device input (Send PSN is the exception).
- Lifeline pins carry the trigger flow (Sequence "splits lifeline impulse"). Trigger sources with no Lifeline input include the Read nodes and: Tick (every frame while the layer is active), On Begin, On End, Run every, Run on marker, Key up/down, On shutdown, On project loaded (Event pin), and the four LightNet events (LightSync session join / leave, backup to primary / secondary).
- General read and write of show state from a layout goes through **Get data** and **Set data**. Set data can write timeline Name, Duration, Fade in, Fade out, State, Time, master fade, volume and speed multiplier; section and layer fades, volumes and names; layer State, Start time and Duration; marker Name, Time, Action on playhead pass and Use as cue; video output Name, State and Fade; canvas Name and Resolution; viewport object Name, Position, Rotation, Size, Transform and Output opacity; 3D model mesh path; Asset Name; and "Send Dmx". Set timeline time and Set object transform are deprecated in favour of Set data; Get device status and Get layer data in favour of Get data.
- Timeline navigation without Set data: Go to marker, Go to section, Go to landmark; look-ups with Get marker and Get section (return an LA Object or null).
- External data in and out of a layout: Read / Send OSC (Integer, Float and String only), Read / Send UDP and TCP (String payloads), Read / Send UE data, Read MIDI, Read MIDI CC, Read MIDI Note, Send MTC, Read TUIO, Get / Set DMX, DMX by UV (CSV driven), Send PSN, Send PJLink command.
- Glue for pipelines: Read from file and Write to file (strings), JSON Pack and JSON Unpack, Split string, Substring, Convert, Get launch argument (read a launch argument by name), Run .bat file, Open project file, Save project file, Launch NDisplay, Kill NDisplay, Write to log, Print to console, Get performance.
- Content by reference: Asset by index, Device by index, Mapping by index and Viewport object by index return references from an Integer. Play Video, Play Notch block and Play TouchDesigner component take an Asset input, so an index is the documented way to choose content from data. Convert offers Asset -> String. No node here turns a String (file name or path) into an Asset.
- Content out: Render texture (to a Mapping) and Set texture (to a Viewport object, Mapping or Device; its search keywords are ndi, spout, deltacast). Set ndi stream takes a Device, a String and a Boolean.
- Computer vision nodes use the OpenCV type; Convert bridges Texture and OpenCV both ways. ZED, RealSense and OAK data arrives as OpenCV through Read ZED, Read RealSense and Read OAK.
- File names in the mirror do not match node titles, so search the digest by title, not by slug.
- Known page errors to keep in mind: Send UDP is described as sending TCP, On project loaded carries JSON Unpack's description, Subtract's description is a keyword list, Mapping by index outputs Canvas.
