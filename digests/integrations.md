# Integrations (digest)

## What this section covers
- 10-bit displays, audio in and out (including LTC), camera and object tracking, content inputs and outputs (Deltacast, RealSense and others), and network messaging (TCP, UDP, TUIO).
- One pattern throughout: create a device node in the **Devices** window, enable it with a checkbox, then use a matching node in a Layer Layout that points at the device.
- The pages name nodes and checkboxes but give almost no ports, addresses, defaults or full pin lists.

## 10-Bit Displays
`docs/integrations/10-bit-displays.md`
- Nvidia Control Panel > Display > Change Resolution > **Use Nvidia color settings** > **Output color depth** 10-bit, Apply. Shown only when a 10-bit display is detected.
- LightAct: Edit > Preferences > **General** tab > **10-bit** in the dropdown. Restart LightAct.

## Audio
`docs/integrations/audio.md`
- Input: Devices > **Audio Input**. Under *Stream* choose the input, tick **Receive**.
- LTC: same device, then tick **Parse LTC**. If not detected, raise the LTC source volume. A timecode offset can be set and affects all later use of that timecode.
- Output: Devices > **Audio Output**. Under *Stream* choose the output, tick **Play**.
- Layers: use the Audio layer template, or a **Blank layer** with the node **Play Audio (from Asset)**.

## Camera and object tracking
`docs/integrations/camera-and-object-tracking.md`
- Current list of supported trackers: Devices right-click menu, **Trackers** category.
- "Camera tracking" = protocol carries lens data (FOV, lens distortion). "Object tracking" = position and rotation only.
- Create the Receiver device first, then use CalTrack, node-based workflows or Tracking Visualizer.

## CalTrack
`docs/integrations/camera-and-object-tracking/caltrack.md`
- Only for primitive objects, video screens and imported 3D objects. Moves the Viewport object to follow physical trackers.
- In the object's *CalTrack* section: pick the receiver in **Tracker device**. Click **Add point** and click on the object, for at least three different points matching the physical tracker positions. Type each tracker's name in the *Tracker* column. Tick **Apply transformation override**.
- **Pick a point** mode isolates the object. **Render spheres** shows a sphere under the cursor. Exit with ESC or a left-click elsewhere.
- If no suitable transformation is found (for example wrong point pairing), the object does not move.

## Node-based Tracking Workflows
`docs/integrations/camera-and-object-tracking/node-based-tracking-workflows.md`
- **Read Tracker** works with every tracking technology. All give at least Position and Orientation. Most also have their own Read node (below).

## Antilatency
`docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/antilatency.md`
- Device **Antilatency receiver**: paste a custom **Environment link** under *Device options*, click **Parse**, tick **Receive**.
- Node **Read Antilatency**: **Device** dropdown plus **Tag** name. Outputs Tag Position, Orientation, Velocity, Angular Velocity.

## BlackTrax
`docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/blacktrax.md`
- Device **BlackTrax Receiver**: set *Stream*, tick **Listen**. Coordinate system under *Data*: **Stage** or **Screen**.
- In CAST's **Tracking Adapter** app, disable **Acceleration and Velocity** filtering or beacon positions are not detected.
- Node **Read BlackTrax**: **Device** dropdown or a **Device reference** node. Outputs Vec3s Position, Orientation, Acceleration, Velocity, and Vec3 vectors LED Position, LED Acceleration, LED Velocity (printed "LEC Velocity").

## FreeD
`docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/freed.md`
- Device **FreeD Receiver** (set *Stream*, tick **Listen**). Node **Read FreeD**. Outputs not listed.

## Mo-Sys
`docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/mo-sys.md`
- Device **MoSys Receiver** (set *Stream*, tick **Listen**). Node **Read MoSys**. Outputs not listed.
- Mo-Sys does not allow 127.0.0.1 (localhost).

## Ncam
`docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/ncam.md`
- **TCP** and **UDP** versions supported. Needs **Server address** (IP of the Ncam server).
- Device **Ncam Receiver** (tick **Listen**). Node **Read Ncam**. Outputs not listed.

## OptiTrack (NatNet)
`docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/optitrack.md`
- Uses OptiTrack's NatNet SDK. Device **OptiTrack Receiver**: **Auto-detect** on gives a **Discovered servers** dropdown, off means manual server parameters. Tick **Listen**.
- Node **Read OptiTrack**: Rigid body position, Rigid body orientation, Marker position.

## PSN
`docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/psn.md`
- Send and receive. Both devices need a **Multicast address**.
- Send: device **PSN Sender** (tick **Send**), node **Send PSN** with **Name** and vec3s Position, Orientation, Speed, Acceleration, Target position.
- Receive: device **PSN Receiver** (tick **Listen**), node **Read PSN**. Outputs not listed.

## SPNet
`docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/spnet.md`
- Device **SPNet Receiver** with **Multicast address** (tick **Listen**). Node **Read SPNet**. Also offers object tracking. Outputs not listed.

## Stype
`docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/stype.md`
- Device **Stype Receiver** (set *Stream*, tick **Listen**). Node **Read Stype**. Outputs not listed.

## Vive
`docs/integrations/camera-and-object-tracking/node-based-tracking-workflows/vive.md`
- Device **Vive Controller**: set **Latency**, tick **Listen**. Node **Read Vive**: Position, Orientation, and **Pressed** boolean (beacon button).

## Tracking Visualizer
`docs/integrations/camera-and-object-tracking/tracking-visualizer.md`
- A Viewport object dragged from the toolbar. *Content*: **Tracker device** dropdown. *Source*: **Add tracker**, then type unique tracker names. *Rendering*: **Show trackers**, and for BlackTrax **Show LEDs** and **Show LED connections**.
- Trackers turn red when the device is not enabled or not receiving.
- LightAct says "trackers" for BlackTrax Beacons and Antilatency Tags or Markers.

## Content IO
`docs/integrations/content-io.md`
- Texture devices: Video in/out (**Deltacast**, **BlackMagic**, **DirectShow** compatible sources), **NDI**, **Spout**, **Unreal Texture Share**.
- Receive: Receiver device, then node **Get Texture (from Device)** (or the Content Input layer template).
- Send: Sender device, then node **Set Texture (to Device)** (or the **Send texture** stock layer template).
- Interlaced video is not supported, in or out.
- Unclear: the page promises detail pages for each type, but only Deltacast and RealSense have one in this section.

## Deltacast Setup
`docs/integrations/content-io/deltacast-setup.md`
- With power off, fit the card (PCIe) and connect FLEX modules to the Gateway card. Install **Deltacast VideoMaster.exe** and **dCARE**. Check firmware in dCARE, update with VideoMaster.
- Ask support@lightact.com which VideoMaster version matches your LightAct version.
- LightAct: add a Deltacast Receiver or Sender node, select the Deltacast Board and I/O port, click **Receive**.

## Deltacast FAQ and Troubleshooting
`docs/integrations/content-io/deltacast-setup/deltacast-faq-and-troubleshooting.md`
- LightAct 4.11.4: VideoMaster SDK 6.20. LightAct 4.12.2: 6.31 (driver bug). LightAct 4.12.3 and later: 6.30.
- Unclear: 4.12.3 is said to have "reverted to" 6.30, though the earlier listed version is 6.20.
- Never hot-plug FLEX modules. BSOD during Install.bat: mixed VideoMaster versions, loose modules or hot-plugging. Do a clean install.

## Deltacast FLEX Management
`docs/integrations/content-io/deltacast-setup/flex-management.md`
- reActor servers use a PCI Express gateway card (**DELTA-gwy** in Device Manager) with FLEX modules, one per gateway port. Modules exist for DisplayPort, HDMI and SDI, input and output.
- LightAct calls a module a **Deltacast board**. It is detected once one module is connected. Servers must be off when modules are changed.

## RealSense
`docs/integrations/content-io/realsense.md`
- Devices > Content I/O > RealSense > **RealSense Receiver**. Pick the camera under *Stream*. Set resolution and frame rate under *Camera settings*. Tick **Receive**.
- "Colonizer" section properties can be changed while receiving. Unclear: "Colonizer" may be a typo.
- Node **Read RealSense**: pick the device on its *Input* pin.
- Unclear: Content IO says textures always arrive through Get Texture (from Device), but this page uses Read RealSense.

## Network
`docs/integrations/network.md`
- Protocols: OSC, TCP, UDP, TUIO. Device nodes and layout nodes are both under a *Network* category in their right-click menus.

## TCP & UDP
`docs/integrations/network/tcp-and-udp.md`
- Receive: device **UDP Receiver** or **TCP Receiver**, set *Stream*, tick **Receive**. Node **Read UDP** or **Read TCP** with **Device** input.
- Send: device **UDP Sender** or **TCP Sender**, set *Stream*, tick **Send**. Node **Send UDP** or **Send TCP** with **Device** and **Message** inputs.
- Unclear: *Stream* parameters, ports, message encoding and framing are not described.

## TUIO
`docs/integrations/network/tuio.md`
- OSC-based touch protocol, receive only. Device **TUIO Receiver** (set *Stream*, tick **Listen**). Node **Read TUIO** with **Device** and **Message index** (which of several received messages to read).

## For automation and pipelines
- Layout nodes pick their device through a **Device** dropdown or a connected **Device reference** node.
- The enable checkbox differs per device: **Receive**, **Listen**, **Send** or **Play**. Nothing flows until it is ticked.
- Custom data in: **UDP Receiver** + **Read UDP**, or **TCP Receiver** + **Read TCP**. Data out: **Send UDP** or **Send TCP** with **Message**. Ports and payload format are not documented here. OSC has its own manual section.
- Textures in via **Get Texture (from Device)**, out via **Set Texture (to Device)**. No interlaced video.
- LTC comes from an **Audio Input** device with **Parse LTC**. Low level stops detection.
- LightAct can send tracking data as PSN.
- Tracker names are free text typed by the user and must match what the tracking system sends.
- Deltacast driver version is tied to LightAct version.
- 10-bit needs the Nvidia setting, the LightAct Preferences setting and a restart.
