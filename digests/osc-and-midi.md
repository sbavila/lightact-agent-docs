# osc-and-midi

## What this section covers

How LightAct receives and sends OSC and MIDI. Each protocol needs a device node in the Devices window plus read or send nodes in a layout.
It also covers the two built-in control surfaces: the **OSC In** window (auto-generated OSC addresses for Layer variables) and the **Control by OSC** window (Master fade and volume, Timeline play states, Cue triggers), and the MIDI equivalents.
Five pages. Port numbers and defaults are not given anywhere in this section.

## Receiving OSC
`docs/osc-and-midi/receiving-osc.md`

- Devices window: insert an **OSC Receiver** node, set its *Stream* parameters, tick **Receive**.
- Layouts window: search **Read OSC** and pick the node for the data type you are receiving (integer, float, string and so on).
- Read OSC node inputs: **Device** (the OSC Receiver), **Address** (string, the OSC address), **Index**.
- **Index**: OSC allows several values on one address. Index selects which value in the array received in a bundle.
- Unclear: the *Stream* parameters (port, interface) are not listed in text.

## Controlling Layers with OSC
`docs/osc-and-midi/receiving-osc/oscin.md`

- Any variable that has a small **OSC** button can be controlled by OSC.
- In the **OSC In** window, click **Regenerate**: every Layer variable with its OSC flag set to True gets a unique OSC address.
- When a message with the right address arrives, the green circle lights up, the variable's OSC flag in Layer Properties turns green, and the variable's value is set.
- Unclear: the format of the generated addresses is not given in text, and the page does not say whether Regenerate changes addresses that already exist.

## Master control and Cue triggering with OSC
`docs/osc-and-midi/receiving-osc/master-control-and-cue-triggering-with-osc.md`

- All of this is in the **Control by OSC** window, which lists every controllable property with its OSC address.
- Master control: example address `/la/playctrl/master/fade`. LightAct reads the float argument and sets *Master fade*. Master volume is controlled the same way (its address is not written out in the text).
- A green *State* LED blinks when a message with the correct address arrives.
- Timeline control: each Timeline play state has its own address in the *Address* column. Addresses can be edited.
- LightAct expects every OSC message to include an argument.
- Cue triggering: the address must include the cue's numbers **CueX.CueY.CueZ**, which are a property of the cue. Example: `/la/playctrl/cue/83.69.67`.
- The incoming address must match the window exactly. In the page's screenshot example:
  - `/la/playctrl/cue/00.77.00` does not trigger it.
  - `/la/playctrl/cue/0.77.0` does.
- Default cue numbers (from the changelog, LA4-6636, not on this page): a new cue has CueXYZ `-1,-1,-1`, which OSC and DMX cannot trigger. `-1` switches an axis off and shortens the address: `5,-1,-1` is `/la/playctrl/cue/5`, `5,10,-1` is `/la/playctrl/cue/5.10`, `-1,-1,2` is `/la/playctrl/cue/2`. Source: `docs/release-changelogs/lightact-4.16/lightact-4.16.b1.md`.
- Unclear: the default Timeline play state addresses are only shown in a screenshot, not in text.
- Unclear: which device or port the Control by OSC window listens on is not stated.

## Sending OSC
`docs/osc-and-midi/sending-osc.md`

- Devices window: insert an **OSC Sender** node, set its *Stream* parameters, tick **Send**.
- Layouts window: search **Send OSC** and pick the node for the data type to send (integer, float, string and so on).
- Send OSC node inputs: **Device** (the OSC Sender) and **Address** (string).
- Bundle messages: several values to the same address using one OSC Sender device. Create several **Send OSC** nodes, chain them through their **Lifeline** input/output, and tick **Send as bundle**.
- The receiver reads individual values from the bundle with the **Index** input of a **Read OSC** node.

## MIDI
`docs/osc-and-midi/midi.md`

- Receiving, Devices window: insert a **MIDI receiver** node, select a *Stream* source, tick **Receive**.
- Incoming MIDI Timecode is shown at the bottom of the node's Data section.
- MTC must be in **MTC Short Message** format or LightAct cannot parse it.
- The MIDI Receiver node's properties include a **Timecode offset**, applied to everything that uses this timecode afterwards.
- Receiving, Layouts window: place a **Read MIDI** node and select the MIDI receiver device. Right-click an output pin and choose **Watch** to see values.
- Controlling Layers with MIDI: in the **MIDI In** window click **Regenerate**. Every layer variable with its MIDI flag enabled gets a unique MIDI Control and Value combination. When that MIDI message arrives, the variable is set.
- Sending, Devices window: place a **MIDI Sender** node, choose *Stream* parameters such as *Timecode rate* and Stream output, tick **Send**.
- Sending, Layouts window: place a **Send Mtc** node and select the MIDI sender device as its input.
- Unclear: the page says a variable gets a "MIDI Control and Value combination". It does not explain how a continuous value is set from that.
- Unclear: the only send node described is Send Mtc. Sending notes or control changes is not covered.

## For automation and pipelines

- Fixed OSC addresses given in the manual: `/la/playctrl/master/fade` and `/la/playctrl/cue/<CueX>.<CueY>.<CueZ>`. Everything else must be read from the **Control by OSC** and **OSC In** windows of the actual project.
- Always send an argument, even for a trigger. LightAct expects every OSC message to include one.
- Cue addresses are matched as exact strings. Do not zero-pad the numbers: `0.77.0`, never `00.77.00`.
- Only Sections and Markers with **Use as cue** enabled are Cues (timelines digest), and each Cue carries its own CueX, CueY, CueZ.
- Layer variables are opt-in for OSC: set the variable's OSC flag, then press **Regenerate** in **OSC In** to get its address. Record the generated addresses from the window; the format is not documented.
- To send several values at once, use a bundle on one address and read them by **Index**.
- Timeline control addresses are editable per project, so a tool should treat them as configuration, not constants.
- MIDI timecode into LightAct must be MTC Short Message format. Timecode offset is set on the MIDI Receiver node.
- In a LightNet cluster, OSC and MIDI device nodes have a manual **Run on** setting (lightnet digest), which decides which machine listens or sends.
- No ports, no default addresses for Timeline play states and no rate limits are documented here. For structured, two-way control with responses, the JSON-RPC API (api digest, LightAct 4.18+) is the documented alternative.
