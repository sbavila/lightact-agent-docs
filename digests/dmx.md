# DMX digest

## What this section covers
LightAct sends and receives DMX over Art-Net and sACN. DMX In covers controlling layers, timelines, master properties and global variables from a lighting desk, including the Index manager that selects assets, mappings and devices by number. DMX Out covers nodes, fixtures built in the Fixture Editor, pixel mapping from content, the DMX by UV node driven by a CSV file, and Art-Net timecode in and out.

## DMX Overview
`docs/dmx/dmx-overview.md`
- Both Art-Net and sACN can be sent and received.
- Network settings: *Edit*, **Project Settings**, **DMX Tab**. Select a Network interface controller (NIC). Avoid 127.0.0.1 (localhost) in most cases.
- The DMX NIC cannot be changed while receiving DMX, sending DMX, or scanning Art-Net nodes.
- Art-Net transmission type: **Unicast (recommended)** or **Broadcast**.
- sACN transmission type: **Unicast**, **Multicast (recommended)** or **Broadcast**.
- Avoid Broadcast where possible, it can slow down the network.

## Receiving DMX
`docs/dmx/dmx-in.md`
- *DMX In* window: **Tools**, **DMX In** (in the *DMX* section). Receives DMX channel values and Art-Net timecode.
- The **Nodes** section lists 2 nodes: one Art-Net, one sACN. The *Configure* column sets the number of ports listened to and which port maps to which universe. Tick **Enabled** to start receiving.
- sACN and Art-Net can be received at the same time, as can multiple timecodes. Timecode is Art-Net only.
- A timecode offset can be applied to received Art-Net timecode. It affects all subsequent operations with that timecode.
- Controllable by DMX: all Layer variables, most Timeline properties (fades, volumes, Cue triggers, Engaged status), master fade and volume, Global variables.

## Index manager
`docs/dmx/dmx-in/index-manager.md`
- Lets DMX set *Layer variables* of type *Asset*, *Mapping* and *Device*. Organised into *collections* and *slots*.
- A variable of one of these 3 types works with Index manager when its DMX flag is true and it is set to 16bit. All stock layer templates are already set up this way.
- The variable listens on two channels (in the example, channels 16 and 17 for the *Video asset* variable of the *Video* layer). Both at 0 selects collection 0, slot 0.
- Unclear: the page does not say which of the two channels is the collection and which is the slot.
- **Autofill** (properties icon) analyses the names of objects (assets, mappings or devices) and asset collections. In the examples, the slot is the number at the start of the object name and the collection is the number at the start of the *Asset collection* name. Assets not in any Asset collection go to collection 0.
- Examples: *005_theSnacks.mp4* outside any Asset collection goes to collection 0, slot 5. *002_syncTest_opus_HAP.mov* inside Asset collection *001_intro* goes to collection 1, slot 2.
- Manual fill: drag an asset from the *Asset* window to a slot. Drag from a mapping (screens, canvases, throwers) to a slot. **Alt + drag** from a device node onto a slot.

## Controlling Timelines with DMX
`docs/dmx/dmx-in/controlling-timelines-with-dmx.md`
- Each timeline has DMX properties in the Properties window. Set Universe and starting Channel first. Easiest: drag from the channel (in DMX In) to the properties button of the Timeline.
- Each DMX controllable property takes one channel in the Timeline's footprint, set by the Channel offset column.
- Play state: one channel. Each play state has a range of values (Timeline state channel value ranges). Ranges must not overlap.
- Cues: every Cue (Section or Marker) has three Cue numbers, X, Y and Z. Each Timeline has 3 DMX channels for Cue triggering. A Cue fires when those 3 channel values match its CueX, CueY and CueZ.
- **Export GDTF** exports the Timeline's personality.
- Unclear: the actual channel offsets and play state value ranges are only shown in screenshots.

## Controlling Layers with DMX
`docs/dmx/dmx-in/adjust-layer-variables-with-dmx.md`
- Every layer has **Universe** and **Channel** properties in the **DMX** variable group. Default is -1, meaning not DMX controlled.
- Map a layer by dragging from a channel to the layer. This sets Universe and Channel.
- Hovering a channel shows which layer and variable is mapped to it.
- All Stock Layer templates have DMX footprints already set up.
- Per variable (right-click menu): **Include in DMX In** checkbox decides if it is in the footprint. Bit depth can be 8, 16, 24 or 32 bit.
- Mapping, Device and Asset variables are controlled through Index Manager.
- DMX flag: disable it to stop DMX setting that variable temporarily. It turns green while DMX is setting the variable.
- **Remap value** unchecked: the variable gets the raw DMX channel value. Checked: value is scaled between the variable's Min and Max. Example: Min 0, Max 1000, DMX 255 gives 1000, DMX 0 gives 0.
- Export a layer's personality: open the Layer's layout, **Export GDTF** or **Export PDF**.

## Master DMX Control
`docs/dmx/dmx-in/control-by-dmx.md`
- **Control by DMX** window (under *Tools*), must be enabled. Controls **Master control** (Master Fade, Master Volume), **Output fades** (fades of Virtual outputs) and **Global variables**.
- **Universe** property sets the universe used. In *Start channels*, the difference between two consecutive Start channels sets how many channels are reserved for each property.
- In *DMX In*, on the same Universe, the used channels show green. Hover for a tooltip naming the property.
- Global variables are set up for DMX the same way as Layer variables.

## Get DMX in Layer Layouts
`docs/dmx/dmx-in/get-dmx-in-layer-layouts.md`
- Needs DMX In enabled. The *Get Dmx* layer node reads a single channel value (example: value 40 from Channel 1, Universe 1).
- Multiple channels from one node: **Add channel** and **Remove channel** in *Node properties*.
- Unclear: the page calls the node both *Get Dmx* and *Get Data*.

## Sending DMX
`docs/dmx/dmx-out.md`
- *DMX Out* window: **Tools**, **DMX Out** (in the *DMX* section). Visualises and sends DMX, and scans for DMX nodes.
- Step 1, insert a node (an endpoint): **Add manual** and pick the protocol, or for Art-Net **Scan ArtNet nodes** (results listed after a 10-second timeout). In the *Configure* column set the number of ports and the universe per port.
- sACN forbids universe 0. sACN universes start from 1. Art-Net can use universe 0.
- Scanned Art-Net nodes report their port count and expected universes, so usually need no changes.
- A physical device with mixed protocols per port needs two separate nodes in DMX Out, one Art-Net and one sACN.
- Step 2, send data: the DMX section shows a grid of 512 channels per universe, all 0 by default. Change universe with the + and - icons of the Universe property. Up to 65,536 universes supported.
- Two ways to fill channels: a Fixture plus Output to DMX Fixture, or Set DMX in Layer Layouts.
- Tick **Send DMX** to transmit.
- **Send Art-Net Timecode** checkbox, then choose the Timeline in the dropdown. Timecode is output once **Play** is hit on that Timeline.

## Fixture Editor
`docs/dmx/dmx-out/fixture-editor.md`
- **Tools**, **Fixture Editor** (in the *DMX* section). Left side visualises, right side manages.
- Create: **Create new** under *fixtures*, give a valid name, **Create**. It then appears in the **Templates** dropdown.
- *General properties*: basic fixture information. *Pixel properties*: choose a *Pixel type* from presets or *Custom*. *Fixture properties*: pixel *Arrangement* of Grid, Circle or Custom.
- Custom Arrangement: double click the model or right click and Add pixel. Drag to move. Right click and Delete pixel.
- Pixel order must match the physical wiring. Right click, **Manual connect**, **Start**, then click each pixel in order. **Backspace** disconnects the last one.
- **Smart connect** (depends on Arrangement): Grid offers 4 patterns built from R (right), L (left), DL (down left) and DR (down right). Circle offers **Clockwise** or **Counterclockwise**.
- Always click **Save** when done, otherwise changes may be lost when the program closes.
- Unclear: Arrangement is listed under *Fixture properties* but later referred to as being under *Pixel properties*.

## DMX by UV
`docs/dmx/dmx-out/dmx-by-uv.md`
- The **DMX by UV** node maps pixels of an incoming texture to DMX addresses using a CSV file. Aimed at complex 3D DMX setups.
- CSV columns, with header: `x,y,universe,channel`. Example rows: `0,0,1,1` then `1,0,1,4` then `2,0,1,7`, so the channel steps by 3 per pixel in the example.
- Typical parts: a UV mapped 3D model (only needed for Viewport visualisation), content made to that UV map, and the CSV.
- Node inputs: **Input** (source texture for RGB values), **CSV path** (also via **Browse** in *Node properties*), **Delimiter**, **Channel offset** (offsets the channels in the CSV), **Adapt resolution** (if checked and the texture resolution differs from the CSV resolution, relative pixel coordinates are used).
- *Node properties*: **Pixel type** (preset or custom, sets how many consecutive channels one pixel uses) and **Method** (how the DMX value is calculated from the texture colours).
- Unclear: the Method options are not listed.

## Output to DMX Fixture
`docs/dmx/dmx-out/output-to-dmx-fixture.md`
- Add a fixture: drag the Fixture icon from the Toolbar to the Viewport floor and choose a Fixture model.
- **2D workflow**: map content from a canvas to the fixture in **Canvas Maps**, the same as any other Viewport object. No 3D positioning involved.
- **3D workflow**: the fixture sources content from a video screen, so their relative position matters. The page also says content can be mapped to fixtures with Throwers.
- Fixture Properties, **DMX Section**: **Pixel Straddle Universes** (whether one pixel may cross a universe boundary. If unchecked the pixel moves to the next Universe), **Start universe**, **Start channel**.
- After mapping, the DMX Data grid shows the values if *Send DMX* is enabled in *DMX Out*.

## Set DMX in Layer Layouts
`docs/dmx/dmx-out/set-dmx-in-layer-layouts.md`
- The **Set DMX** layer node sets a single channel (example: Channel 2, Universe 1, Value 220). It overwrites that channel and is sent with the rest of the DMX data.
- Multiple channels per node: **Add channel** and **Remove channel** in *Node properties*.
- A Stock Layer Template called Send DMX already does this.
- Unclear: the page calls the node both *Set DMX* and *Set Data*.

## For automation and pipelines
- DMX (Art-Net or sACN) is a full remote control surface: every Layer variable, Global variables, Timeline play state, fades, volumes and cues, Master Fade, Master Volume and Virtual output fades.
- Asset naming drives DMX selection. With Autofill, a leading number in the file name is the slot and a leading number in the Asset collection name is the collection (for example *005_theSnacks.mp4*, collection *001_intro*). Assets outside any collection land in collection 0. A content pipeline should name files and collections to this pattern.
- Index manager variables need the DMX flag on and 16bit, giving two channels: collection and slot.
- Cue triggering uses three channels matched against each Cue's X, Y and Z numbers.
- Layer **Universe** and **Channel** default to -1 (no DMX control).
- Remap value off means raw channel values reach the variable. On means scaling to the variable's Min and Max.
- Personalities can be exported as GDTF (layers and timelines) or PDF (layers) for a lighting desk.
- Sending: nothing leaves until **Send DMX** is ticked in DMX Out. sACN has no universe 0. Up to 65,536 universes. Art-Net scan takes 10 seconds.
- DMX by UV takes a plain CSV file (`x,y,universe,channel`, configurable delimiter) referenced by path on the node.
- Art-Net timecode can be received (with offset) and sent from a chosen Timeline. Timecode is not available over sACN.
- The DMX NIC cannot be changed while sending, receiving or scanning.
- The manual gives no exact channel offsets or play state value ranges in text, only in screenshots. The documented exports are **Export GDTF** and **Export PDF**.
