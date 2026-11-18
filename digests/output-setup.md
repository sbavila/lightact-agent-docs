# Output Setup digest

## What this section covers
How content from Viewport objects (Video screens, Projectors) leaves the server. Two steps: Output Maps (Viewport objects to Virtual outputs to Physical outputs) and Output management (framerate, vertical sync, fixed EDIDs, Nvidia Mosaic). Most of the output management work happens in NVIDIA Control Panel, not in LightAct. Also covers LightAct servers (reActor) with multiple GPUs and GPU troubleshooting.

## Output Setup Overview
`docs/output-setup/output-setup-overview.md`
- Two steps: **Output Maps** (map Viewport object content onto Physical outputs), then **Output management** (correct framerates, sync, EDIDs).

## Output Maps
`docs/output-setup/output-maps.md`
- *Output Maps* window has 3 areas: **Viewport objects** (those selected in Properties on the right), **Virtual outputs** (mapped or not yet mapped), **Physical outputs** (all detected outputs, on all machines in a multi-machine setup).
- Order: 1. Create Virtual outputs. 2. Map objects to Virtual outputs, then Virtual outputs to Physical outputs. 3. Enable the Virtual outputs.
- Create a Virtual output: right click a Physical output and pick **Create matching output** (same resolution) or **Create and map matching output** (same resolution, also mapped). Double click a Physical output also creates a matching Virtual output. Right click in the *Outputs* area to create one at other resolutions.
- Mapping Viewport objects to Virtual outputs works the same as in Canvas Maps. A Mapping layout can also be created in Output Maps.
- Map Virtual to Physical: drag from the Virtual output's Properties icon to a Physical output. **Shift + drag** maps and enables. Or left click the Properties icon (top right of each Virtual output) and use its Mapping section.
- Enable: Properties icon, then Enable. Enabling creates a new full screen window that covers that output entirely.
- Shortcut: dragging creates a Virtual output with the same resolution as the Source area and maps it to that Physical output. Shift-dragging also enables it.
- Unclear: the drag start point for that shortcut is only shown in a screenshot ("as shown above").

## Output management
`docs/output-setup/output-management.md`
- Recommendations: understand vsync handling, use fixed EDIDs wherever possible, use Mosaic wherever possible.
- Vsync rules: with no outputs enabled, LightAct is vertically synced to its UI display. As soon as one output is enabled, it releases vsync from the UI display and enables vsync to the output display. Automatic.
- Manual vsync: enable **Remote support** in the *General* tab of *Preferences*, then set the **Vertical sync** dropdown in the *General* tab of *Project settings*.
- Fixed EDID means loading the EDID from a file, so the OS always assumes the display is attached. Protects against hot plug events and EDID loss through switchers and extenders. Two ways: in LightAct, or in NVIDIA Control Panel.
- Multiple outputs on one machine: strongly recommended to combine them into an Nvidia Mosaic (presented to the OS as a single logical GPU). Keep the UI display separate and put all output displays in the Mosaic.
- Mosaic can currently only be enabled from NVIDIA Control Panel.
- Without Mosaic: all outputs need the same refresh rate, and should be synced with a Quadro Sync card (Sync Expansion Module).
- Unclear: the page ends with a broken link for "how to set up a Mosaic".

## Set up Mosaic
`docs/output-setup/output-management/set-up-mosaic.md`
- Before starting: remove the Windows user password or set automatic login, so the machine can be entered after a crash or bluescreen during setup.
- Only displays with the same resolution and framerate can be combined.
- NVIDIA Control Panel, *Workstation*, **Set up Mosaic**, **Create new configuration**.
- If GPUs are not sync-capable (see *Sync capability* icon), enable V-Sync: *3D Settings*, **Manage 3D Settings**, **Global Settings** tab, *Global presets* set to **Base profile**, *Vertical sync* **On**, **Apply**.
- Multi-projector or stereoscopic 3D installations must use Mosaic with sync-capable GPUs.
- *Select topology*: **Number of displays**, **Topology**, **Orientation of displays**, **Configuration name**.
- Limits (NVIDIA): all displays need at least one display timing in common. Each display must be greater than 800x600. Total Mosaic resolution must not exceed 16,384 pixels horizontally or vertically.
- *Select displays*: choose displays, **Refresh rate**, **Resolution per display**. *Arrange displays*: set order (note it down for mapping in LightAct), then **Apply**.
- Applications using the NVIDIA driver may need to be closed (click **Continue**). Displays may flash. Applying can take more than 30 seconds.
- *Apply Changes* pop up gives about 20 seconds to click **Yes**. If missed, NVIDIA Control Panel may misbehave: close it, reopen, restart the process.
- Optional last step: *Adjust overlap and bezel correction*. Edge overlap needs sync-capable GPUs.

## Modify or Disable Mosaic
`docs/output-setup/output-management/modify-or-disable-mosaic.md`
- NVIDIA Control Panel, *Workstation*, **Set Up Mosaic**. **Modify** reopens the setup window. **Disable**, then **Disable** again in the pop up.

## GPU Troubleshooting
`docs/output-setup/output-management/gpu-management-troubleshooting.md`
- Mosaic driver issues: remove NVIDIA drivers, shut down, check all monitor cables, boot, reinstall drivers.
- BSOD or freeze during Mosaic: caused by changing the setup while in Mosaic mode (adding or removing monitors), total resolution above 16,384 pixels in either direction, or exceeding PCIe bus data limits.
- BSOD while Mosaic was Primary Display: usually leaves Windows login unreachable if the password was not removed. Boot from the Windows Recovery USB dongle shipped with the reActor server, **Troubleshoot**, **Advanced options**, **Startup Settings**, **Restart**, press **4** or **F4** for Safe Mode, uninstall all NVIDIA drivers, remove password or set autologin, reboot, reinstall drivers.
- Only some Mosaic displays show content: check Vertical Sync is On in NVIDIA Control Panel, all monitors connected and active, disable and re-create the Mosaic, then treat as a driver issue.
- Flickering black bars on outputs: Nvidia driver bug, not tearing. Mitigate by enabling triple buffering in NVidia settings.
- Nvidia-smi.exe error: likely a GPU driver issue. No known workaround other than reinstalling all graphics drivers.
- Unclear: the page does not give the text of the Nvidia-smi.exe error.

## Multiple GPUs
`docs/output-setup/output-management/multiple-gpus.md`
- Applies only to LightAct servers, not multi-GPU systems in general.
- LightAct has no native "select GPU" feature.
- Typical reActor multi-GPU configuration: 1 GPU for GUI output, 2 GPUs for Video Outputs. By default this does not make full use of the output GPUs. Extra steps are needed (Mosaic, Primary Display, Workflow).
- First **Export** and **Load EDIDs** for all connected displays.

## EDID Management with Nvidia Control Panel
`docs/output-setup/output-management/edid-management-with-nvidia-control-panel.md`
- Three steps: export EDID to a file, load EDID from the file, unload at the end.
- Export: NVIDIA Control Panel, *Workstation*, **View system topology**, click the **EDID** link beside a Display Connector. *Manage EDID* window, **Export** tab, select display, **Export EDID**.
- Load: **Load** tab, **Browse** to the file, select the *Display Connector* and *Video Signal* (in the example *DisplayPort(Digital)*), **Load EDID**.
- Loading the wrong EDID file can cause the display or GPU to malfunction. Incompatibility warnings appear in the Comments section.
- Unload: **Unload** tab, choose the *Display Connector*, **Unload EDID**. Do this when done with a display. With a fixed EDID loaded, connecting a display that cannot read the signal may lock you out of the computer.
- Displays may flash during load and unload.

## EDID Management in LightAct
`docs/output-setup/output-management/edid-management-in-lightact.md`
- Ultimate license only.
- In the Output Maps window, right click a detected Physical display: **Export EDID** (type a descriptive name), **Load EDID** (choose from available EDID files for that Physical output), **Unload**, **Unload all** (all connected displays).

## Workflow
`docs/output-setup/output-management/multiple-gpus/workflow.md`
- With Mosaic as Primary display, every program opens stretched across the Mosaic. Select it on the taskbar and press **Windows key + Shift + Left arrow** or **Right arrow** to move it to the Monitoring Display.
- *LightAct 4* and *LightAct 4 Manager* window location and size can be set in the **Registry Editor** using the format *posX,posY;resX,resY*. Both remember location and size on close and reopen there if the monitor configuration is unchanged.
- Unclear: the registry key path and value name are not given.
- To reboot with this configuration, remove the Windows login password or turn on automatic login.
- Finishing up, in this order: 1. Make the Monitoring Display the Primary Display. 2. Disable Mosaic. 3. Unload EDID.

## Primary Display
`docs/output-setup/output-management/multiple-gpus/primary-display.md`
- Set all displays to 100% scale. Turn off Night Light, it affects the content on the outputs.
- NVIDIA Control Panel, *Workstation*, **Manage GPU Utilization** shows two containers: the monitoring GPU, and the two output GPUs as a single logical GPU.
- The GPU connected to the primary display is the primary GPU. All others act as slaves. By default the primary display is the Monitoring display, so the monitoring GPU is primary.
- To use the output GPUs: *Display*, **Set up multiple displays**, right click the Mosaic display, **Make primary**, **Apply**, **Yes** in *Apply Changes*. A star icon on the Mosaic display confirms it.

## For automation and pipelines
- No scripting or API hooks are described in this section. Output mapping, enabling, Mosaic and EDID are all done by hand in the Output Maps window and NVIDIA Control Panel.
- Enabling a Virtual output creates a full screen window on that output and moves LightAct's vsync from the UI display to the output display.
- Content resolution planning: a Mosaic cannot exceed 16,384 pixels in either direction, all its displays must share resolution and framerate, and each must be greater than 800x600.
- Without Mosaic, all outputs need the same refresh rate.
- LightAct has no GPU selection. On multi-GPU reActor servers the output GPUs only do the rendering if the Mosaic is the Windows primary display.
- LightAct 4 and LightAct 4 Manager window placement is stored in the Windows registry as *posX,posY;resX,resY* and can be edited there. The key path is not documented.
- Machines running Mosaic should have no Windows password or should autologin, otherwise a crash can lock you out.
- EDID management inside LightAct needs the Ultimate license. Fixed EDIDs should be unloaded before changing displays.
- Manual Vertical sync control is hidden until **Remote support** is enabled in Preferences.
