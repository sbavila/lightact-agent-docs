# LightTrack digest

## What this section covers
LightTrack is LightAct's markerless people tracking, using ceiling mounted depth cameras (OAK or SICK Visionary-T Mini). It has a Simulation mode that needs no hardware and a live mode for real tracking. This section covers the viewport objects, the hardware and network setup for SICK cameras, and the tuning steps in LightAct.

## LightTrack
`docs/lighttrack/lighttrack.md`
- Markerless tracking with depth cameras installed on a ceiling. Works in dark or bright spaces, indoors and outdoors.
- Two tracking modes: **Simulation** and **LightTrack live**.
- **Simulation**: tracks *People* objects in the Viewport. No special hardware. Works with the free LightAct license. Steps: add a LightTrack sensor and a LightTrack system to the Viewport. In the *LightTrack system* properties under *Sources*, double click the sensors to add them. Move the *LightTrack sensor* above a *People* object. Click **Start** in the *LightTrack system* properties.
- **LightTrack live**: tracks physical people. Needs a paid LightAct license and hardware. Steps: add an OAK receiver node in the *Devices* window. Add a LightTrack sensor in the *Viewport* and choose the *OAK camera* as source. Add a LightTrack system and choose the *LightTrack sensor* as source. Click **Start** in the LightTrack system properties.
- Use the **Get LightTrack data** node in a Layer Layout to read the tracking data.
- **LightTrack system**: viewport object that aggregates data from sensors. Drag from the *Side bar* to the *Viewport*.
- **LightTrack sensor**: viewport object that reads data from a device such as an OAK camera. Place it to mimic the physical space. Properties include the source device and settings such as FOV.
- Unclear: the page spells the product LightTrack, Lightrack and LighTrack, and names the modes both "Simulation" / "Simulate" and "LightTrack live" / "LightTrack".

## SICK Camera Setup
`docs/lighttrack/lighttrack/sick-camera-setup.md`
- Hardware: SICK Visionary-T Mini camera, Visionary mounting kit (recommended), 24V DC power supply, power cable M12 8-pin A-coded (10 m recommended), Ethernet cable M12 8-pin X-coded to RJ45, 1 Gbit or faster switch, dedicated NIC (recommended).
- Set a static IP on the computer's network adapter. Sharing the network with internet traffic is supported but not recommended.
- Camera IPs: in **SICK AppManager**, click **Search**, select a camera, assign a static IP, repeat. Example: 10.10.10.10, 10.10.10.11, 10.10.10.12.
- Verify in LightAct: **Devices** window, add **SICK Visionary Camera Receiver**, select camera, click **Receive**, check the depth stream is visible.
- Mounting: same distance to the surface, perpendicular to the surface, same orientation, firm (no vibration), minimum 20% overlap between cameras, avoid reflective surfaces. Mount one by one and check coverage. Overlap is required for multi-camera tracking.
- Measure and write down: camera height from lens to floor, and horizontal distance between cameras. Both are needed for LightTrack setup.

## SICK LightTrack Setup
`docs/lighttrack/lighttrack/sick-lighttrack-setup.md`
- Receivers: in **Devices**, add one **SICK Visionary Camera Receiver** per camera, rename each, click **Receive**.
- Depth filtering, in **Device Settings**: reduce **Max depth** until the floor is completely black (value close to the measured height), then raise **Min depth** to fine-tune. Tracked objects should look as white as possible in the stream, unwanted objects as black as possible.
- Sensors: drag one **LightTrack Sensor** per camera into the viewport and rename. Position: Y = measured height, X = horizontal distance between cameras, Z = 0. First camera at X = 0.
- Unclear: the example gives Camera 2 and Camera 3 the same X ("measured distance").
- For each sensor: Properties, Source, select its SICK Visionary Camera Receiver. Set HFOV = 70° for all sensors.
- System: add a **LightTrack System**, add all sensors under **Sources**, under **Tracking** select **LightTrack**, click **Start**.
- Threshold: select the receiver node, hold CTRL, click the darkest area you want to track, use that value as Threshold.
- Blob tracking: under **Input**, adjust Min diameter, Max diameter and Min distance. Objects closer than the minimum distance are merged.
- Overlap alignment: place an object in the overlap area and adjust **Inward offset** until blobs from both cameras align.
- Unclear: the page does not say which object's properties hold **Input** and **Inward offset**.

## For automation and pipelines
- Tracking data reaches content only through the **Get LightTrack data** node in a Layer Layout. No network output or API for tracking data is described here.
- Simulation mode works on the free license with *People* objects, so tracking driven content can be developed and tested without cameras.
- Live mode needs a paid license. Tracking must be started with **Start** on the LightTrack system. No automatic start is documented.
- Supported inputs named in the manual: OAK camera (OAK receiver node) and SICK Visionary-T Mini (SICK Visionary Camera Receiver).
- SICK cameras need static IPs, ideally on a dedicated NIC with a 1 Gbit switch. HFOV is 70°.
- Sensor positions use measured real world values (Y is height), so the Viewport must match the physical space.
