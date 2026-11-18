# Real-time content playback (digest)

## What this section covers
- Playing Notch blocks and TouchDesigner .tox components in Layer Layouts, and integrating Unreal Engine (UE) running on the same machine.
- UE parts: LightAct UE plugin, Epic's Texture Share and nDisplay plugins, the UnrealLink window, three texture sharing workflows.
- Most UE pages carry a banner: the integration changed significantly for UE 5.3 and 5.4 and the doc is outdated. Treat UE steps as valid for 4.27 and 5.1.1 only.
- `docs/readme.md` was checked. It is a link index of manual sections and adds no facts.

## Overview
`docs/real-time-content-playback/notch.md`
- Unity has no native integration. Users run it on another machine, bring content in over NDI or live video input, and exchange data over UDP, OSC or TCP.

## Notch
`docs/real-time-content-playback/notch-1.md`
- Usual route is the Notch layer template. The node inside it is **Play Notch Block**. Its input pins are the template's exposed Layer variables (see `docs/layers-and-layouts/stock-layer-templates/content-layer-templates/notch-layer-template.md`).
- Node property **Unload on layer exit**: clears the block from VRAM on layer exit.
- Needs a valid Notch license: **Playback**, or **Builder** at limited resolution. PLE is untested. Users report watermarked playback if the block was also exported with PLE.
- Node Error with warning **Failed to load node contents** most likely means no suitable license.
- Needs a discrete GPU, preferably Nvidia. GPU matters most for performance. Multi-GPU: contact LightAct first.

## TouchDesigner
`docs/real-time-content-playback/touchdesigner.md`
- Copy .tox files into the **Assets/TouchDesigner** folder and they appear in LightAct. Play with the **Play TouchDesigner Component** node (asset dropdown).
- Loading takes a minute or two after selecting the asset. The node then rebuilds itself with new input and output pins.
- Needs TouchDesigner installed, with a Commercial license or above. Multi-GPU not supported.

## Unreal Engine
`docs/real-time-content-playback/unreal-engine-integration-overview.md`
- Both apps run on one machine. LightAct controls the pace of Unreal's render cycle and passes runtime data such as Timecode.
- Works with UE 4.27, or 5.1.1 and above. Not 5.0 or 5.1.0.
- Unclear: the same page says the doc is outdated for UE 5.3 and 5.4. No updated steps are given.

## Required Unreal Engine Plugins
`docs/real-time-content-playback/unreal-engine-integration-overview/required-unreal-engine-plugins.md`
- Required: the **LightAct** plugin (version must match the project's UE version), Epic's **Texture Share** and **nDisplay**. Creating the project from the nDisplay template enables the Epic ones.

## Installing LightAct Plugin
`docs/real-time-content-playback/unreal-engine-integration-overview/required-unreal-engine-plugins/installing-lightact-plugin.md`
- Engine install: copy the **LightAct** folder to `<UEEngineVersion>\Engine\Plugins`. Available, not auto-enabled, in all projects on that version.
- Project install: copy the **LightAct** folder into a **Plugins** folder in the project.
- Unclear: this page says to create Plugins "in the Content folder". The troubleshooting page only says "Plugins folder".
- Enable under Settings > Plugins > **Installed** > **Enabled**, then restart Unreal Editor.

## Setting up the Plugin
`docs/real-time-content-playback/unreal-engine-integration-overview/required-unreal-engine-plugins/setting-up-the-plugin.md`
- Three steps, detailed in the next three pages: LightAct Runtime actor, LightActTimeStep as Custom Time Step, LightActTimeCode as Timecode provider.

## LightAct Custom Time Step
`docs/real-time-content-playback/unreal-engine-integration-overview/required-unreal-engine-plugins/setting-up-the-plugin/lightact-custom-time-step.md`
- Lets LightAct drive Unreal's render cycle. The manual treats "Custom Timestep" and "Genlock" as the same thing.
- Create a Blueprint Class asset with parent **LightActTimeStep**. Select it in UE Project Settings > **Custom TimeStep** dropdown.
- Monitor: Window > Developer Tools > Genlock. Console: `stat fps`, `stat unit`.

## LightAct Runtime Actor
`docs/real-time-content-playback/unreal-engine-integration-overview/required-unreal-engine-plugins/setting-up-the-plugin/lightact-runtime-actor.md`
- Drag **LightAct Runtime** from Place Actors into the level. It passes performance and project data to LightAct by itself. No properties to set.

## LightAct Timecode
`docs/real-time-content-playback/unreal-engine-integration-overview/required-unreal-engine-plugins/setting-up-the-plugin/lightact-timecode.md`
- Create a Blueprint Class asset with parent **LightActTimeCode**. Select it in UE Project Settings > **Timecode Provider** dropdown.
- Monitor: Window > Developer Tools > Timecode Provider.

## UnrealLink
`docs/real-time-content-playback/unreal-engine-integration-overview/unreallink.md`
- **UnrealLink** is the LightAct window for the UE integration. Marked as under development.
- UE Editor path (**UE4Editor.exe** or **UE5Editor.exe**) is set in **Preferences > UE**. It decides which UE version launches .uproject assets.
- Sync: **Send timecode to UE**. **Genlock Unreal Engine** (off, every frame, every second, every third; usually Every frame). **Wait for UE texture** (sub-frame latency feature). If Unreal cannot keep up, lower LightAct's FPS in Project Settings.
- Unclear: the genlock control is also called the **Lock UE to** dropdown.
- Order: import Unreal asset, create .ndisplay file, generate launch command, launch nDisplay, optionally kill it.
- Unreal asset = .exe of a packaged game or a .uproject. Drag it into LightAct's window. Assets show as radio buttons in UnrealLink. Select one.
- The .ndisplay file needs at least one Thrower or Projector in the Viewport with its **nDisplay** checkbox on. Click **...** to pick or create the file, then **Generate config file**.
- **Generate command** fills the command textbox. Then **Launch nDisplay**.
- With Every frame, real-time UE stats appear a few seconds after launch. No stats means the LightAct plugin is not set up correctly.
- **Exec cmd line Args**: extra command line arguments (example `-trace` for UnrealInsights). **Custom ExecCmds**: extra console commands.
- **Show advanced settings**: **Render offscreen** (no Unreal windows), **Enable mGPU** (render nDisplay viewports on another GPU; needs an NVidia card with NVLink).
- **Kill nDisplay** stops the instance. Instances launched by LightAct also die when LightAct exits.

## Texture Sharing
`docs/real-time-content-playback/unreal-engine-integration-overview/texture-sharing.md`
- Three workflows: **Thrower2UCam** (most common), **Projector2UCam** (specific cases), **ViewportUCam** (the only one not launching nDisplay from LightAct).

## Thrower2UCam
`docs/real-time-content-playback/unreal-engine-integration-overview/texture-sharing/thrower2ucam.md`
- For cases where Unreal's camera is independent of the projectors: cyclo walls, flat or curved walls, domes. A LightAct 3D model gets its content from one thrower.
- Create an nDisplay viewport from the thrower in UnrealLink. In Devices create a **Texture Share** device node with the thrower's viewport handle (handles are offered as suggestions). Tick **Listen**.
- Route the texture to the thrower through **Render to Canvas**, or directly with **Set Texture**.

## Projector2UCam
`docs/real-time-content-playback/unreal-engine-integration-overview/texture-sharing/projector2ucam.md`
- For when each projector needs its own point of view (complex 3D objects). The object must also exist in Unreal with the content applied there.
- Calibrate projectors in LightAct, generate the .ndisplay from them (one Unreal viewport per projector), launch, read each with a **Texture Share** node, apply to LightAct Projectors in Layer Layouts.
- The LightAct 3D model is used only for calibration.
- Heavy: one Unreal render per projector. The Unreal scene must match reality: real objects only, matching level of detail, no view-dependent lighting, usually no particles.

## ViewportUCam
`docs/real-time-content-playback/unreal-engine-integration-overview/texture-sharing/viewportucam.md`
- Written for UE 4.27. For 5.1.1 or above, contact support.
- Texture Share plugin actors: **BP_TextureShare** and **BP_TextureShare_CustomData** (enable **Show Plugin Content** to see them). Put BP_TextureShare in the level. On Play it streams the viewport.
- Its **Share Name** variable is the handle. Type the same value as the viewport name in LightAct.
- Unclear: the page does not name the LightAct field. The troubleshooting page calls it **Viewport name** on the Texture Share node.

## Unreal Engine Integration Troubleshooting
`docs/real-time-content-playback/unreal-engine-integration-overview/unreal-engine-integration-troubleshooting.md`
- Wrong texture: Unreal cameras must match LightAct throwers or projectors. A **Player start** actor can move the whole nDisplay configuration.
- nDisplay fails to launch or crashes: remove all spaces from file paths (above all the .ndisplay path), check nDisplay plugin enabled, check UE and plugin versions, try Unreal's Switchboard.

## Texture Sharing Troubleshooting
`docs/real-time-content-playback/unreal-engine-integration-overview/unreal-engine-integration-troubleshooting/texture-sharing-troubleshooting.md`
- Written with UE 5.1.1 and LightAct 4.2.2. Most common fault: a space in the .ndisplay path.
- Unreal: new project from the **nDisplay template**, copy the plugin into Plugins, enable it.
- LightAct, in order: drag the .uproject into a blank project (shows in Assets). Set the UE version in Project Settings. Set UE editor paths in Preferences. Insert one Thrower with nDisplay ticked. In UnrealLink select the .uproject. Click **Generate config file** twice so the file is really written. Show advanced settings, untick **Render offscreen**, Generate command. Launch nDisplay.
- Expected: a 1920x1080 px window opens on the primary screen after a few seconds. If not, launch the project with the NDC_Basic configuration from Switchboard.
- Then: Devices, insert **Texture Share**, click **LAThrow_0** under Object suggestions to fill **Viewport name**, tick **Listen**.
- Support wants: .la project file, .ndisplay file, software versions, GPU and CPU details.

## For automation and pipelines
- No OSC, DMX, HTTP or script interface is documented here for Notch, TouchDesigner or UnrealLink. All steps are GUI.
- Ingest by file: .tox into **Assets/TouchDesigner**. .uproject or .exe by drag into the window.
- TouchDesigner node pins do not exist until the component finishes loading (a minute or two).
- Notch and TouchDesigner need their own licenses on the playback machine.
- No spaces in any Unreal related path.
- Texture Share handles are plain names: `LAThrow_0` for a thrower, or BP_TextureShare's **Share Name**.
- Extra Unreal launch arguments and console commands go in **Exec cmd line Args** and **Custom ExecCmds**.
- Multi-GPU: unsupported for TouchDesigner, ask first for Notch, NVLink plus **Enable mGPU** for Unreal.
