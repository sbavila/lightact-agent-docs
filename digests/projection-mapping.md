# Projection Mapping digest

## What this section covers
Planning and aligning projectors in LightAct. Projection Study for planning projector count, position and brightness. The 2D workflow (warp and blend in Output Maps) and the 3D workflow (digital twin model, 3DCal calibration, AutoBlend). Iris, LightAct's camera based computer vision system for automatic projector calibration, including IrisVirtual for planning camera placement. Nearly everything here is a manual, on-site process.

## Projection Mapping
`docs/projection-mapping/projection-mapping.md`
- Steps: Projection study (usually before projectors are connected), then Projection mapping.
- *2D projection Mapping*: flat or curved surfaces such as screens and walls.
- *3D Projection Mapping*: complex 3D objects. Needs an accurate 3D model of the projection object. Content is usually rendered onto that 3D model. May use Iris.

## Projection Study
`docs/projection-mapping/projection-study.md`
- In a multi-server setup, *Projection Study* runs only on the *Primary* machine.
- Set the Render mode of the projection object to *Unshaded* for best results.
- Setup: place objects in the *Viewport*, add projectors and set their **Properties**, map the objects to the projectors.
- Open with **Tools**, **Projection Study**. Select projectors and objects to analyse, choose a mode in the *Setup* section, click **Enable**.
- Four modes: **Projected content** (how the projection will look), **Shadow analysis** (areas getting no light), **Illuminance** (adjustable lux scale, for projector count and lumen output), **Pixel size** (pixel grid on objects, shows pixel stretching).
- When enabled, a tag appears at the upper left of the *Viewport* and only the chosen objects and projectors are shown.
- Blending (AutoBlend) results can be viewed in *Projected content* and *Illuminance* modes.

## 2D Projection Mapping Workflow
`docs/projection-mapping/2d-projection-mapping-workflow.md`
- In 2D projection mapping you usually do not use Projector viewport objects at all. All warping and blending is done in the Output Maps window.
- Initial calculations: from object size, required brightness and viewing distance, determine projector count, resolution, lens properties and overlap (in pixels or percent). Then calculate the overall content resolution.
- Project setup (one option): create a Video screen with the correct physical size and resolution and render test content to it. In **Output Maps** create one *Virtual output* per projector. **Create subareas** in the *Video screen* matching projector resolution and snap them to the screen edges. **Map the subareas** to the Virtual outputs. Right click the destination subarea and select **Create layout**.
- Mapping layout node chain: **Perspective warp** first (align corners), **Mesh warp** (fine tune), **Softedge** (blend projectors).
- Warp one projector first, then the next relative to it. Blending is usually last.
- For blending, switch to White Content override. Some users prefer red.
- For colour mismatch between projectors use colour correction nodes in the Layout, for example *Texture Modify* or *Channel Multiply*.

## 3D Projection Mapping Workflow
`docs/projection-mapping/3d-projection-mapping-workflow.md`
- The 3D model in the viewport must be a precise digital twin of the physical object. It needs proper UV mapping and correct normals to take a texture.
- Steps: 1. Import and place precise 3D models (relative positions between objects must be accurate) and set them as the ***Sources*** of the projectors. 2. Calibrate projectors: with *Iris*, calibrate cameras first then all projectors automatically. Without Iris, use *3DCal* manually. 3. Blend with *AutoBlend*. 4. Fine-tune with warp, blend and colour correction nodes.
- Two ways to set a projector's sources: the *Content section* in the projector's properties (double click a source or use the <> buttons), or drag from the objects to the projector. Mapped objects appear in the projector's thumbnail.
- The object's render mode should be **Unshaded** for projection mapping.

## 3DCal
`docs/projection-mapping/3d-projection-mapping-workflow/3dcal.md`
- 3DCal matches a virtual projector's location, rotation and lens properties to the physical one, using at least 6 pairs of matching points on the virtual and physical object.
- Point rules: not all on the same plane, non symmetrical, spread across the whole projected part of the object. Breaking the first two can look fine but place the projector wrongly.
- *Reprojection* error should be kept below 1px.
- First place the virtual projector roughly where the physical one is. Double click the projector, or right click and **Setup**, then the **3DCal** tab. Left preview is the view from the virtual projector, right preview is what the projector outputs.
- Settings: **Output** (toggle whether points are sent to the output, disable after point selection to judge precision). **Viewport** (Render mode of the projected object). **Calibrate on change** (recalibrate on every new or moved point, otherwise only on the **Calibrate** button). **Snap to vertex** (clicks snap to the closest model vertex). **Adjust projection points** (moves projected points within the max delta range to lower reprojection error). **Preferences** (cursor colour, background colour, thickness). **Viewport** (toggle 3D helper spheres in the main Viewport, **Draw helper spheres**). **Fallbacks** (save, restore and compare calibration solutions).
- Click **Store current orientation** first so you can revert if calibration moves the projector far away.
- Virtual and physical points can be picked in any order. Virtual points are clicked on the left side.
- Projected points are selected on the right side. The projector must already be mapped to an enabled physical output.
- After the 6th pair the projector is calibrated and moved. Success means reprojection error below or close to 1.
- Right click a point to delete it. Points can be moved with the mouse or arrow keys. Arrow keys move the cursor by 1px.
- Unclear: the control buttons on the right of the 3DCal tab are only shown in a screenshot. "Viewport" appears twice in the settings list with different meanings.

## AutoBlend
`docs/projection-mapping/3d-projection-mapping-workflow/autoblend.md`
- Automatically calculates blend masks for projectors or throwers.
- Open with **F8** or **Tools**, **AutoBlend**. Select the projection objects and click **Blend**. Blend masks appear on the right.
- All projected objects should have render mode *Unshaded*, otherwise blending might not be perfect.
- Settings: **Blend on open** (recalculate when the project file opens). **Blend every frame** (recalculate every frame, only for moving projectors or objects). **Mute all AutoBlend nodes** (disables AutoBlend on the outputs).
- **Run Autoblend** node triggers AutoBlend automatically.
- **Blend with distance**: for projectors at different distances from the object. When enabled, distance is fully taken into account in the mask. Recommended practice is identical projectors at similar distances.
- **Angle cutoff**: reduces pixel stretching on complex 3D objects. Applies the least blending to the projector hitting a face most perpendicularly and the most blending to the one with the sharpest angle. Gives fewer sharp edges between masks. It does not remove sharp mask edges caused by projector shadows.
- Where masks are applied: double click a projector to open its Layout. The **AutoBlend** node outputs the blend mask into a **Texture Blend** node, which blends it with the content (the **Input** node). Masks can be adjusted further with nodes.

## Iris
`docs/projection-mapping/iris.md`
- Iris is one or several *Power over Ethernet* machine vision cameras pre-calibrated by LightAct, used to calibrate projectors faster and more accurately.
- Workflow: optional IrisVirtual, Setting up Iris Device Node, Adjusting Focus, Adding and Calibrating Iris Camera in Viewport, Calibrate Projectors.
- Unclear: the page numbers the steps 1, 3, 4, 5. There is no step 2.

## Adjusting Focus
`docs/projection-mapping/iris/adjusting-focus.md`
- Adjust the focus ring on the camera while clicking **Refresh the texture**. The **Circles and lines** override helps. Tighten the screw afterwards.

## IrisVirtual
`docs/projection-mapping/iris/irisvirtual.md`
- Estimates the number of Iris cameras needed, with location, orientation and lens type, before buying. Under development, features will likely change.
- Process: add Iris cameras to the viewport and choose lenses, map the projection objects to them, open the **Iris** window, select the **Iris camera(s)** and all projectors, tick **IrisVirtual**, click **Calibrate**.
- Projection objects must be properly UV mapped. Projection object resolution must be high enough: one pixel of the object should be the same size or smaller than a projected pixel.
- Negative results: reprojection error above 1 px, or *"Insufficient number of points"*. Causes: camera does not see the entire projected area, or the area from one projector is too small in the camera view.
- A positive result (below 1 px for all projectors) can still fail in reality. LightAct asks you to send the project file for review before deciding.
- Unclear: one sentence says a successful result has reprojection errors "below 0". Elsewhere the page says below 1 px.

## Setting up Iris Device Node
`docs/projection-mapping/iris/setting-up-iris-device-node.md`
- Create an *Iris device node* in the **Devices** window and select the physical camera from the dropdown. The camera must be powered and on the network to be listed.
- **Mode** dropdown: *3DCal* or *Projector calibration*. Each mode stores its own *Exposure time*, *Gain* and *Gamma*. Changing a value saves it into the current mode.
- **Exposure time [ms]**: higher is brighter. **Gain**: brightens bright areas more than dark ones, useful for *Projector calibration*. **Gamma**: lower is brighter, minimum 0.25, post process so click **Refresh texture** to see it. **Undistort**: keep checked at all times.
- **Setup** button opens the *Iris* Setup window for masking. **Add polygon**, drag the handle to move, double click a line to add a point, right click a point to remove. Masked area shows red and is ignored for calibration. **Inverse mask** inverts it.
- Settings for 3DCal (mode set to **3DCal**): object neither under nor over exposed. Recommended **Exposure** around 30000, **Gain** around 1, **Gamma** around 1. With no ambient light, set projectors to Edit color override for lighting.
- Settings for Projector calibration (mode set to **Projector Calibration**): lit areas as white as possible, unlit as dark as possible. Tune with **Black and white override** enabled on a projector in the camera's view.
- With a LightNet setup, when calibrating a projector connected to a Secondary machine, select the right Machine in the projector's Properties.
- Unclear: the property is labelled Exposure time [ms] but the recommended value is around 30000.

## Iris Troubleshooting
`docs/projection-mapping/iris/iris-troubleshooting.md`
- Black lines in incoming images (seen in the Iris folder in LightAct's Program Data folder during projector calibration): change network adapter settings. Network settings, Ethernet, Change adapter options, the adapter on the camera network, **Properties**, **Configure**, **Advanced** tab.
- Unclear: the required adapter settings are only shown in a screenshot.
- Vimba Viewer (part of the Allied Vision Vimba SDK) lists Iris cameras as Mako G-507B. Open a camera, click Freerun, All tab, Stream, Statistics. The marked fields should all be zero (which fields is only shown in a screenshot).

## Calibrating projectors using Iris
`docs/projection-mapping/iris/calibrating-projectors-using-iris.md`
- Open **Tools**, **Iris**. Select the cameras and projectors on the right.
- **IrisVirtual**: uncheck for real projectors.
- **Include Iris camera points**: includes points picked in the camera's 3DCal window. Leave checked in 99% of cases.
- **Show advanced**: extra settings, rarely needed.
- **Export calibration images**: saves every camera image from the calibration to *ProgramData\Lightact\Lightact4\iris*. Leave checked, support asks for these first.
- **Adjust projection points**: adjusts projected points within *fix delta [px]* to lower reprojection error.
- **Show in Explorer** opens that directory. **Calibrate** starts the process.
- Afterwards all selected projectors are calibrated and their 3DCal windows hold a larger number of calibration points.

## Calibrating OptiTrack cameras with active or passive markers
`docs/projection-mapping/iris/calibrating-optitrack-cameras-with-active-or-passive-markers.md`
- Cameras: OptiTrack Primex13 or Slimx13. Slimx13 works with Active markers only. Passive markers need Primex13.
- A separate OptiTrack license is needed per camera.
- Active Tags need an OptiTrack Active BaseStation. Also needs a PoE switch. Contact LightAct before buying.
- Firmware may need updating and Active Tags re-programming. Antivirus may interfere with Motive's communication with the markers.
- Unclear: the calibration process is "Coming soon".

## Adding and manually calibrating Iris camera
`docs/projection-mapping/iris/adding-and-calibrating-iris-camera.md`
- Insert an Iris camera in the Viewport roughly where the physical one is. Match its frustum to the physical FOV, easiest with the **Lens override** dropdown.
- Map camera to device: select the Iris camera, in its **Device** section select the **Iris device node**.
- Map projection objects to the camera by dragging from the object to the camera, or with the camera's **Sources** properties.
- Calibrate: double click the camera or right click and **Setup**. The Iris 3DCal window works like the projector one, with these differences: you select **Physical points** by clicking on the camera image, there is a *Stream* section for device node settings, and there is *Overlay opacity* (shortcut **O**).
- Calibrates after 6 or more points. Good calibration: reprojection error below 1px, yellow calibration lines all parallel, and little visible shift when changing *Overlay opacity*.

## For automation and pipelines
- The only node based hook in this section is the **Run Autoblend** node, which triggers AutoBlend from a layout. AutoBlend also has **Blend on open** and **Blend every frame**.
- Calibration (3DCal, Iris) is interactive. No API or file format for calibration data is described. Fallbacks store alternative calibrations inside the project.
- Iris calibration images are written to *ProgramData\Lightact\Lightact4\iris* when **Export calibration images** is checked. LightAct support asks for these first.
- Content pipeline requirements for 3D mapping: models must be accurate digital twins with correct UVs and normals, object render mode **Unshaded**, and (for IrisVirtual) object texture resolution at least as fine as the projected pixel.
- For 2D mapping, content resolution comes from projector count, resolution and overlap. Warp and blend live in Output Maps Mapping layouts (Perspective warp, Mesh warp, Softedge), not on Projector objects.
- Projection Study runs only on the Primary machine. When calibrating with Iris across LightNet, the projector's Machine property must point to the right Secondary.
- Quality thresholds to check against: reprojection error below 1px, minimum 6 non-coplanar, non symmetrical point pairs.
- Shortcuts: F8 opens AutoBlend, O changes Overlay opacity in the Iris 3DCal window, arrow keys nudge the 3DCal cursor by 1px.
