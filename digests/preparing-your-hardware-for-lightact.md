# Preparing your hardware for LightAct (digest)

## What this section covers
- Requirements and Windows prerequisites for running LightAct 4 on your own hardware.
- Windows, Nvidia and network sharing settings, including the shared LightNet projects folder.
- Tests for smooth running and for how many videos a server can play at once.
- A LightSync troubleshooting checklist and tested DisplayPort to HDMI adapters.

## Getting your hardware ready to run LightAct
`docs/preparing-your-hardware-for-lightact/getting-your-hardware-ready-to-run-lightact.md`
- Minimum: Windows 10 or later, discrete Nvidia graphics card, 8 GB RAM.
- Recommended: professional Quadro/RTX NVidia GPU, 64 GB RAM, fast NVMe media drives, fast CPU with a medium number of cores. No more detailed spec is offered.
- Prerequisites: CodeMeter User Runtime (a missing **WibuCM64.dll** error means it is absent). .NET Framework 3.5 and 4.8. .NET SDK 6.0 and 7.0 64bit. Visual C++ Redistributable 2010 and 2013 (64bit and 32bit), 2015-2019 32bit, 2015-2022 64bit.

## Setting up your computer
`docs/preparing-your-hardware-for-lightact/setting-up-your-computer.md`
- Windows: power plan **High performance**, **Ultimate performance** or the **LightAct** plan. Adjust for best performance. Game Mode On. Graphics settings: LightAct.exe set to High performance.
- Nvidia Manage 3D settings: CUDA - GPUs = Main GPU. OpenGL GDI compatibility = Prefer performance. OpenGL rendering GPU = Main GPU. Power management mode = Prefer maximum performance. Vertical sync = Use the 3D application setting.
- Nvidia Manage GPU Utilization: dedicate to graphics tasks (main GPU), disable ECC. Update drivers.
- Network sharing: turn on network discovery and file and printer sharing, turn off password protected sharing. NIC profile **Private**. Firewall: enable all "File and printer sharing" and "Network discovery" rules, inbound and outbound.
- Unclear: the manual's sharing step is garbled ("use 128…").
- For `Windows cannot access \Name; Error code: 0x80070035`, run as administrator:
  - `reg add HKLM\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters /f /v RequireSecuritySignature /t REG_DWORD /d 0`
  - `reg add HKLM\SOFTWARE\Policies\Microsoft\Windows\LanmanWorkstation /f /v AllowInsecureGuestAuth /t REG_DWORD /d 1`
  - `reg add HKLM\SOFTWARE\WOW6432Node\Policies\Microsoft\Windows\LanmanWorkstation /f /v AllowInsecureGuestAuth /t REG_DWORD /d 1`
- LightNet: create **LightNetProjects** on the D: (storage) drive, share with Everyone Read/Write, then set it in Edit > Preferences > Network > LightNet Projects folder path.

## Testing your computer
`docs/preparing-your-hardware-for-lightact/testing-your-computer.md`
- Throttling test: enable **Remote support mode** in Preferences (this unlocks **Vertical sync** in Project settings). Untick **Vertical sync** and **Force Project framerate**. Expect well over 1000 FPS and, more important, a steady figure. Dips every few seconds mean the GPU is being throttled.
- Smoothness test: re-enable both checkboxes. In **Output Maps** double-click a detected Physical output to make a virtual output of the same resolution. Enable a content override (**Strobe**, **Traveling gradient** or **Traveling lines**) and the output. Motion must be completely smooth.
- Multiple displays must be combined into a Mosaic to be completely smooth.

## Testing video playback
`docs/preparing-your-hardware-for-lightact/testing-video-playback.md`
- Uses the **Video Playback Template project**. Needs LightAct 4.11.0-89 or newer, Advanced Renamer, MediaInfo.
- Example rig: 4 x 4K outputs, 1 GUI plus 3 in Mosaic (11520x2160). 60Hz for 30/60 fps videos, 50Hz for 25/50 fps.
- Test videos: HAP with chunks = number of CPU cores, or NotchLC at Best quality. Constant bitrate. Copies named `VideoFileName_1`, `VideoFileName_2`, and so on, because each Play video node must play a unique file. LightAct can supply its reference test file.
- Close all other apps, including NVIDIA Control Panel. Keep only the Performance window (and Timeline editor) open. Main window fullscreen (F11).
- The **Loading thumbnails** layer waits, then the **Video layer** starts a new Play video node every 1 to 2 seconds. Both have a `Delay`. Marker 1 logs "Test started", Marker 2 logs "Test concluded". Output runs the **Traveling Lines** override.
- Assign each video variable of the Video layer to a different file, save, reopen the project.
- Result: the highest count with no continuous **Missed frames** in the Performance window (initial ones are fine) and smooth Traveling Lines.

## Troubleshooting LightSync
`docs/preparing-your-hardware-for-lightact/troubleshooting-lightsync.md`
- Symptoms: outputs out of sync, motion not smooth, large periodic graph spikes. One unstable server can upset the whole system.
- Simplify: one GUI display and one output display per server. Output display on Genlock or Framelock, GUI display not synced. Not needed if Primary has no output display. Same refresh rate everywhere, equal to project framerate. Dedicated switch with only LightAct machines.
- Close remote desktop tools (VNC Viewer, TeamViewer, AnyDesk), browsers, GPU monitoring tools, NVIDIA Control Panel. Apps that interact with desktop rendering can affect sync.
- Test: establish cluster, enable outputs in Output Maps with Content override **Strobe**, begin LightSync session. Then reconnect equipment step by step.
- Multiple outputs should be one NVIDIA Mosaic display.
- For support: a video of all outputs with the Output Maps **Render overlay** on (LightAct 4.16.0 or newer), a screenshot of NVIDIA Control Panel > View System Topology, and a Package for support.

## DisplayPort - HDMI converters
`docs/preparing-your-hardware-for-lightact/displayport-hdmi-converters.md`
- Direct DP to DP is recommended. Not all converters work. Tested: StarTech **DP2HDMI2** and **DP2HDMI4KS**.

## For automation and pipelines
- Encode targets: HAP with chunks equal to the playback machine's CPU core count, or NotchLC Best quality, constant bitrate.
- Match refresh to content: 60Hz for 30/60 fps, 50Hz for 25/50 fps. Project framerate should equal display refresh.
- Playback capacity is measured per server with the template project, not specified.
- LightNet uses a shared **LightNetProjects** folder on D: with Everyone Read/Write.
- The 0x80070035 fix sets `RequireSecuritySignature` to 0 and `AllowInsecureGuestAuth` to 1, which loosens file sharing security.
- Remote desktop tools, browsers and GPU monitors on a server can affect LightSync.
- **Vertical sync** is editable only while **Remote support mode** is on.
