# Release changelogs (LightAct 4.13 to 4.17)

## What this section covers

- Release notes for LightAct 4.13 through 4.17 (December 2025 to November 2026), one page per build: betas (B), release candidates (RC) and point releases.
- This digest is organised by version, newest first, then by feature area. Tickets keep their Jira number (LA4-xxxx) and a tag for the build where they appeared.
- Features and behaviour changes are kept. Plain bug fixes are listed only when they show how something works.
- Each build page lists only what changed since the previous build, so x.y.0 pages are short and the beta carries most of the content. The few tickets that repeat are named once per version.
- Ticket text is AI-rewritten from developer tickets. Some entries describe the request or the bug, not the delivered result. Those are marked "Unclear:".

## Changelogs before 4.13
`docs/release-changelogs/changelogs-before-4.13.md`

- Older changelogs live on LightAct Answerhub: https://answerhub.lightact.com/c/changelog/17. Nothing else on the page.

## How are Changelogs generated
`docs/release-changelogs/how-are-changelogs-generated.md`

- Generated semi-automatically from the LightAct 4 Jira project, grouped by Epic. Tickets outside any Epic are listed at the end (the build pages head that part "Other Upgrades").
- Ticket types: Features (completely new), Improvements (existing, improved), Fixes.
- Descriptions are developer text rewritten by AI; the page admits results are sometimes "less than ideal".
- Status: in a Beta some tickets may still be "Testing". Requesters: 3 letter acronyms of users who asked. None listed means LightAct designed it.
- Only tickets judged of interest to users are included.

---

## LightAct 4.17
`docs/release-changelogs/lightact-4.17.md` (index, links only)

Pages read:
- `docs/release-changelogs/lightact-4.17/lightact-4.17.0.md`: 18 November 2026, 1 Epic, 6 upgrades. Tag [0].
- `docs/release-changelogs/lightact-4.17/lightact-4.17.rc1.md`: 18 November 2026, 6 Epics, 31 upgrades. Tag [RC1].
- `docs/release-changelogs/lightact-4.17/lightact-4.17.b1.md`: 23 October 2026, 9 Epics, 67 upgrades. Tag [B1].
- No ticket repeats across the three pages; 4.17 is the sum of all three.

### Crossfade (sections only, now includes audio)
- LA4-7358 [B1]: layer crossfade controls removed. Crossfades are configured on sections.
- LA4-7357, LA4-6920 [B1]: two defaults. Project Settings holds the project-wide default crossfade and duration, used only for newly created timelines. Timeline Properties holds a timeline default, used only for newly created sections on that timeline. Neither changes existing timelines or sections.
- LA4-7386 [RC1]: duration is set directly in seconds; 0 disables the crossfade. "Hold opacity" option keeps the previous FadeHold behaviour.
- LA4-7387 [RC1]: FadeDip has a shallower dip.
- LA4-7361 [B1]: crossfade also applies to audio (embedded in video and standalone audio assets). Audio always uses a fixed FadeDip with a linear curve; FadeHold / Hold opacity does not affect it.

### Play modes and transport
- LA4-7450 [RC1]: "Pause" renamed "Hold" ("Play & Pause" is now "Play & Hold").
- LA4-7449 [RC1]: video mode "Freerun & Restart" renamed "Freerun on Hold". Video keeps playing when the playhead reaches the end of a section and holds; a manual pause stops it. Jumping into a layer follows the same timing as Normal playback. LA4-7465 confirms this for "Play to the end of section and hold".
- LA4-7499 [RC1]: switching to "Play to the end of section and LOOP" after holding at a section end loops that section instead of running into the next.
- LA4-7479 [0]: Fade In no longer triggers in Pause mode when "Apply fade to Pause" is unchecked.
- LA4-7254 [B1]: the one-second jump threshold applies only during playback. Paused or stopped, jump-back goes to the current section's start.
- LA4-6929 [B1]: a timeline group following another group that is synced to timecode now follows its own configured behaviour when that timecode is lost.
- LA4-7303 [B1]: layer "Preview Only" mode removed.

### Video buffering and performance
- LA4-7452 [RC1]: the Always Ready buffer had ignored its settings and used only Video Buffer Count. It now honours playhead position, Always Ready buffer % and Preload mode.
- LA4-7453 [RC1]: Missed Frames counter in the Performance window works (was always 0).
- LA4-7350 [B1]: Canvases with many Subareas render cheaper: 400 area renders can be handled as 20 Canvas renders. LA4-7349: less overhead with many timelines and layers, including stopped ones.
- LA4-6305 [B1]: opt-in NotchLC path (asynchronous PBO uploads, no CPU BGRA-to-RGBA conversion); also fixes HAPQ alpha. Test with six 4K NotchLC videos: CPU 85% to 35%.
- Unclear: LA4-6305 is "enabled with the preprocessor definition", unnamed. It reads like a build-time switch, not a user setting.

### Timeline editing
- LA4-7287 [B1]: layer grouping. A group is movable, has open, save, undo and delete actions, a fixed duration, and cannot be resized or cut. LA4-7526 [0]: new layers land above or below a group, not on its track.
- LA4-7258 [B1]: minimum layer duration is 1 frame.
- LA4-7284 [B1]: a new section created on an existing one extends through the available timeline space.
- LA4-7282 [B1]: Shift range selection for layers and sections (not tracks). Alt-click a section selects the layers above it.
- LA4-7283 [B1]: selecting a timeline element logs its time distance from the playhead.
- LA4-7288 [B1]: arrow keys scrub the selected timeline when the pointer is over the Timelines or Viewport window.
- LA4-6877, LA4-6882 [B1]: snapping includes layer fade start and end; "Snap to keyframes" snaps elements and playhead to visible keyframes.
- LA4-6640 [B1]: "Unmap from DMX" clears a timeline's DMX universe and channel.
- LA4-7278 [B1]: Get Usage window lists each timeline's layers and variables with a jump control.
- LA4-6168 [B1]: Curve Editor is an attached overlay above the Timeline Editor, shown when a curve-enabled variable is selected. LA4-5232, LA4-5227, LA4-6504: keyframe markers on layers; arrow keys move curve points; inserting time shifts keyframes right of the playhead.

### Layer Connections
- LA4-6879, LA4-7235 [B1]: create by Alt-dragging between layers, then pick compatible source and destination variables (any compatible non-default variable, not only textures).
- LA4-7331: connections can span timelines. LA4-7259: window groups them by source timeline. LA4-7236: delete a single incoming or outgoing connection from the layer's context menu. LA4-7273: searchable dropdowns.
- LA4-7272 [B1]: timeline lists in OSC In and MIDI In follow the order of the Timelines and Cue List windows.

### Variables and nodes
- LA4-7338 [B1]: copying a Getter/Setter node within a layout keeps it linked to the same variable. Copying between layouts creates a new local variable when allowed. Non-editable variables cannot be copied.
- LA4-6198, LA4-6598, LA4-6431, LA4-7324 [B1]: duplicate variables with settings; move several between groups; drag variable groups to global variables or reorder them.
- Unclear: LA4-7323 says dragging a variable group into a layout "can add Getter controls", that Setter controls were not created, and to "confirm the final behavior before publishing".
- LA4-7194 [B1]: node to convert a texture to monochrome. LA4-6914: Channel Mixer gets "Pre-multiply Alpha". LA4-7434: a bypassed Texture Mask passes the texture through.
- LA4-7016 [RC1]: UDP, TCP, OSC, TUIO and other Sender/Receiver nodes show connection details on the node; NDI nodes show the stream name.
- LA4-7015 [RC1]: UDP and TCP Sender nodes can send a test message: "Hello from LightAct!".
- LA4-3752 [B1]: Shared Memory Handle size and Name are editable (ticket "UE Data Handle Size"). LA4-7427 [RC1]: TouchDesigner features lose the Beta label.

### Show control, NDI
- LA4-6912 [RC1]: menu controls (ticket "Ctrl Mute Show Control") enable or disable OSC receivers, Art-Net and sACN inputs.
- LA4-6662 [RC1]: indicator under the Universe control shows whether that universe can be received via Art-Net or sACN, or whether DMX input is disabled or not configured for it.
- LA4-7221 [B1]: a DMX cue triggers when its enabled channels match; unused channels no longer block it.
- LA4-7522 [0]: Art-Net Timecode sending and chase resume after reopening a project.
- LA4-7503 [RC1]: NDI accepts interlaced and progressive inputs; NDI Sender nodes output audio. LA4-7364 [B1]: NDI SDK 6.3.2.

### LightNet, launch, logs
- LA4-7513 [RC1]: command-line arguments -backup and -editor set the LightNetRole at startup, alongside existing -secondary.
- LA4-7457 [RC1]: "Transfer project" in the LightNet Management window moves only the project. Assets move only via "Initiate transfer of all assets" and the "Initiate transfer" buttons. LA4-7459: an asset presence check runs after asset transfer.
- LA4-6405 [B1]: "Open LightNet Folder" opens the shared project folder in Windows Explorer.
- LA4-7344 [B1]: logs include computer name and, when available, IP address and user name; entries show frame rate and update time.

### Assets and transcoding
- LA4-7256 [RC1]: convert an asset to HAP and generate proxy files from the Assets window. Options: HAP chunk count, proxy resolution, overwrite existing.
- LA4-7309 [RC1]: transcode a whole Video collection at once. Runs in a separate process, so failures do not crash LightAct.
- LA4-7240 [B1]: drag an item or collection onto its parent collection to unlink it.

### Mapping, outputs, Viewport
- LA4-7398 [RC1]: "Show all" in CanvasMaps and OutputMaps unhides all objects, collections and canvases; "Return home" also in object views.
- LA4-7456 [RC1]: several Video Screens or sub-areas mapped to one Video Output all render (only the last did before).
- LA4-7296 [B1]: Video output info shows mapped position or NDI destination, plus resolution.
- LA4-7314 [RC1]: cursor hides when an output window is clicked. LA4-6654: the rear of a video screen is always solid black.
- LA4-7241 [B1]: copy and paste transform (position, rotation, scale) from an object's context menu. LA4-7163: Ctrl while rotating is five times finer than the Preferences step.
- LA4-7306, LA4-7433, LA4-7242 [B1]: Scale removed from Null objects (always 1), LightTrack sensors, Throwers and Iris objects.
- LA4-7044 [B1]: cylindrical video screens support Inside normals. LA4-7249: default LightTrack camera FOV is 70° x 60°.
- Shortcuts confirmed by fixes: Shift+F is Look at Target (LA4-7307); Ctrl+Shift+G in the Objects window puts the selection under one Null (LA4-7575).

---

## LightAct 4.16
`docs/release-changelogs/lightact-4.16.md` (index, links only)

Pages read:
- `docs/release-changelogs/lightact-4.16/lightact-4.16.4.md`: 16 September 2026, 1 upgrade. [4]
- `docs/release-changelogs/lightact-4.16/lightact-4.16.3.md`: 09 September 2026, 3 upgrades (fixes: NDI Receiver in a LightNet session, Assets window freeze, cluster output counts). [3]
- `docs/release-changelogs/lightact-4.16/lightact-4.16.2.md`: 09 September 2026, 1 upgrade. [2]
- `docs/release-changelogs/lightact-4.16/lightact-4.16.1.md`: 21 August 2026, 4 upgrades. [1]
- `docs/release-changelogs/lightact-4.16/lightact-4.16.0.md`: 10 August 2026, 1 upgrade. [0]
- `docs/release-changelogs/lightact-4.16/lightact-4.16.rc1.md`: "There were no new features introduced in this version."
- `docs/release-changelogs/lightact-4.16/lightact-4.16.b1.md`: 20 July 2026, 7 Epics, 51 upgrades. [B1]
- Carried over: LA4-7034 (right-click a locked layer, single option "Unlock") is in 4.16.B1 and was already in 4.15.2.

### Cues, OSC, DMX
- LA4-6636 [B1]: CueXYZ rules. Default -1,-1,-1 means the cue cannot be triggered via DMX or OSC; OSC requests with -1 are ignored; -1 disables matching on that axis. Examples as written:
  - 5,-1,-1: DMX needs X=5. OSC /la/playctrl/cue/5
  - 5,10,-1: DMX needs X=5 and Y=10. OSC /la/playctrl/cue/5.10
  - -1,-1,2: DMX needs Z=2. OSC /la/playctrl/cue/2
- LA4-6637 [B1]: Preferences "Use Markers as Cues", off by default. When on, new Markers get "Use as Cue" checked. Sections always default to "Use as Cue" on.
- LA4-6067 [B1]: Previous and Next buttons per timeline header in the CueList window.
- LA4-7229 [1]: previous-cue logic while playing: within n seconds after a cue, jump two cues back; otherwise jump to the nearest cue before the current time. (n is not stated here; 4.17 calls it the one-second jump threshold.)
- LA4-6457 [B1]: Master fade (top-right control) now affects DMX output on all universes.
- LA4-6443 [B1]: sACN transport dropdown removed; note reads "sACN uses Multicast mode only", hint "Target IP = 239.255.uniLOW.uniHIGH".
- Unclear: that byte order is quoted as written; check the sACN page before relying on it.

### Timecode and audio
- LA4-6923 [B1]: timecode shows exact framerate, not type names like Film. DMX In window Time column: [00:00:40:23] @ 24 FPS; Type column removed. Same in the Devices window for MIDI Receiver and Audio Input nodes.
- LA4-7065 [B1]: Timecode Monitor shows hours and minutes and applies offsets to all fields.
- LA4-6886 [B1]: Audio In device node gets a Volume control (clipped audio stopped LTC parsing). Order: "Parse LTC", "Min consecutive frames", "Timecode offset".
- LA4-5662 [B1]: ASIO drivers supported, only with the -asio launch argument. Status Testing.
- LA4-6456 [B1]: Audio In/Out node needs at least one device selected; otherwise logs "Cannot initialise device. Please select at least one source."

### Nodes
- LA4-7247 [1]: Trigger Volume. Inputs: Positions (vec3 array), Primitive (Box or Sphere). Outputs: On Inside (continuous while any point is inside), On Enter (once per new point), On Exit (once when the count decreases), Objects Inside (int). Respects the primitive's position, rotation, scale.
- LA4-6852 [B1]: Go to Section / Go to Marker: Timeline input removed (current timeline only); Mode (Integer) dropdown Next, Previous (no wraparound, ignore the selection), Selected. Go to Landmark: Integer dropdown Previous, Next.
- LA4-6851 [B1]: "Get marker". Inputs: Timeline, Marker (Previous or Next), Only Cues. Output: LAObject reference to the first marker before or after the playhead.
- LA4-6490 [B1]: "Get Data → Timeline Group" and "Set Data → Timeline Group (Property)": Engaged, Disengaged, grace period on/off.
- LA4-6510 [B1]: "Add Frame Delay" buffers frames to add latency. Keywords: latency, sync, frame delay.
- LA4-6847 [B1]: Play Audio node Play Mode dropdown replaces Solo run: Normal, Freerun (was Solo run on), Freerun & Restart. Timecode no longer used.
- Unclear: whether the Play Audio mode was also renamed Freerun on Hold in 4.17 is not stated.
- LA4-7159 [0]: Play Video "Loop nr" output hidden; existing projects compatible.
- LA4-6595 [B1]: copying a node layout to another layer auto-creates and links its Layer Variables. LA4-6593: right-click recreates a node from its template, restoring connections where possible.
- LA4-6256, LA4-7069 [B1]: Texture processing nodes (Softedge, Mask, Perspective Warp, Mesh Warp): Arrow 1 px, Shift+Arrow 10 px, Ctrl+Arrow next/previous point, Ctrl+Shift+Arrow 100 px.
- Unclear: LA4-6215 (Mesh Warp "Reset point", relative to neighbouring points) is worded as a request, status Done.

### Iris, 3DCal, projectors, 3D assets
- LA4-6931 [B1]: Iris 2.0, calibration rebuilt; can output a point cloud of the projection object to verify the 3D model. No detail given.
- LA4-7012 [B1]: 3DCal "Algorithm" dropdown: Linear Projection, Zhang Radial & Tangential, Iterative LM (+RANSAC). LA4-7078: "Render wireframe". LA4-7048: "Grab only visible points" skips occluded points.
- LA4-6515 [B1]: Projection Masks hide content behind the projector relative to its field of view. LA4-5243: projectors auto-aim at their projection object when moved.
- LA4-6821 [B1]: Props. FBX/OBJ files in the Assets/Props subfolder appear as a Props collection. Shaded by default, no textures, no FBO or resolution, cannot receive mapped content, absent from Maps windows; multi-part files are one object.
- LA4-6884 [B1]: an FBX with submodels imports as separate objects parented to a Null named after the asset, keeping relative offsets. LA4-4672: 3D Models default to Unshaded.

### LightNet and LightSync
- LA4-7073 [B1]: LightSync simplified, with diagnostic tools (no specifics). LA4-7124: Strobe content override shows frame numbers to compare outputs.
- LA4-7379 [4]: duplicated Canvas areas now get unique IDs. Before, duplicating a Canvas caused wrong subarea mapping and duplicate layer outputs on Secondary nodes. Status Code Review.

### Crossfade internals
- LA4-7228 [1], LA4-7318 [2]: a layer spanning both sections of a crossfade (Dip/Hold) is rendered to a texture on the source side and reused on the destination so the background stays continuous. LA4-6984 [B1]: crossfades work across different tracks.

### Project, assets, UI
- LA4-6505 [B1]: Viewport camera positions are saved in the project file, not user preferences.
- LA4-6682 [B1]: "Package for Support" dialog (Description of the issue, Expected behaviour, Observed behaviour) writes YYMMDD_HHMMSS_supportRequestSummary.txt in the log folder and builds "package for support.zip".
- LA4-6641 [B1]: Collection dropdown lists up to 255 collections (was 15), matching the Index Manager. LA4-6989: right-click "Remove" on a single missing asset or collection.
- LA4-6857 [B1]: Performance window "Project Stats": counts of timelines, layers, viewport objects, device nodes, outputs.
- LA4-6801 [B1]: Preferences → UI "reActor logo brightness" (Rental/Hardware or Server licenses); with LightNet on, the logo follows the Machine color.
- LA4-7009 [B1]: dragging a child object out of its parent unlinks it.

---

## LightAct 4.15
`docs/release-changelogs/lightact-4.15.md` (index, links only)

Pages read:
- `docs/release-changelogs/lightact-4.15/lightact-4.15.2.md`: 01 July 2026, 1 upgrade, LA4-7034 only (unlock locked layers). [2]
- `docs/release-changelogs/lightact-4.15/lightact-4.15.1.md`: 15 June 2026, 1 Epic, 12 upgrades. [1]
- `docs/release-changelogs/lightact-4.15/lightact-4.15.0.md`: 30 May 2026, 2 upgrades, both crash fixes (LA4-6957 changing a 3D model version, LA4-6953 deleting a Timeline Group used as Sync source). [0]
- `docs/release-changelogs/lightact-4.15/lightact-4.15.b1.md`: 12 May 2026, 7 Epics, 32 upgrades. [B1]
- No ticket repeats inside 4.15.

### LightNet: Editors, asset presence, Backup
- LA4-6451 [B1]: Editor has "Request Project Transfer" in its Primary machine section. Without the "Request project transfer" permission the Primary replies "You don't have permission to request project transfer." Otherwise it transfers the project to that Editor only.
- LA4-6843, LA4-6842 [B1]: Editors can request asset transfer (all, or asset by asset); per-Editor permissions in the Editor menu.
- LA4-6837 [B1]: Asset Presence split into "Local presence" (green OK or Missing) and "Cluster presence". Only the Primary monitors cluster presence: green, or red with the devices missing it. Elsewhere: "Only Primary monitors cluster presence of assets." / "Cluster presence: NA".
- LA4-6832 [B1]: "Check Asset presence" logs "Checking Asset presence across the cluster", then "All assets present where they should be." or "Assets missing (check Assets window)". Automatic checks log only errors and warnings.
- LA4-6833: roles shown as (P), (S), (B) in the Assets window. LA4-6436: Iris window only on the Primary ("Iris is available only on Primary machine.").
- LA4-6855, LA4-6448 [B1]: Automatic failover setup for Backup machines redesigned; roles shown in the Automatic Failover list. LA4-6829: LightNet port management improved (no specifics).

### Outputs
- LA4-6853 [B1]: "Latency" input on every Video output adds latency per output.
- LA4-6437 [B1]: 3D Models can be downsampled, like Video screens, Throwers and projectors.

### Video playback
- LA4-6891 [B1]: "Preload mode": "By time" (shows "Video preload time [s]") or "Next section" (preloads all videos in the upcoming section).
- LA4-6862 [B1]: "Always ready buffer" adds 0%, 5%, 10%. LA4-6892: buffers cleared more consistently when a video layer ends.
- LA4-6710, LA4-6875 [B1]: with Frameblending on, slow playback (for example 0.2x) blends adjacent frames; 29.97 fps files in 60 FPS projects improved.
- LA4-6432, LA4-6639 [B1]: Play Video node outputs "Buffer" and "Missed" integers. Performance window Video playback table adds Time (HH:MM:SS:FF plus frame number), Loop (counter) and Update (last update time).
- LA4-5611 [B1], LA4-6975 [1]: Play Video graphs: Frames (missing yellow, buffered green), Times (Decode, Decompress), Frame Blending, New frame time.
- LA4-6963 [1]: Play Video node can render a stats overlay onto outputs (enable in node properties). LA4-6991 [1]: fixes missed frames with 60fps files introduced in 4.15.0.

### Projects, timeline, nodes
- LA4-6795, LA4-6794, LA4-6793 [B1]: large projects open and add layers much faster; a status label shows project-open stages.
- LA4-6900 [B1]: Project settings "Default section crossfade time" beside "Default layer crossfade time", each with "Apply to all existing". (Layer crossfade is removed in 4.17.)
- LA4-6863 [B1]: Home moves the playhead to the first frame of the selected timeline. LA4-6740: "On no TC" dropdown sits under "Show TC labels" in Timeline Properties.
- LA4-6922 [B1]: nodes Set Timeline Master Fade, Set Timeline Volume, Set Timeline Speed Multiplier.
- LA4-6813 [B1]: "Get Section" returns a reference to the Current, Next or Previous Section. LA4-6848: Run on Marker takes an LA Object input.
- LA4-6909 [B1]: Set Data Canvas Resolution enforces a minimum of 1x1.
- LA4-6901 [B1]: "Reset default workspace" shows in the Workspaces menu when the active workspace is named Basic, Mapping or Playback.
- LA4-6970, LA4-6979 [1]: a copied video layer's Timeline label auto-renames when its Video variable changes; Notch template no longer duplicates Layer variables on asset change.

---

## LightAct 4.14
`docs/release-changelogs/lightact-4.14.md` (index, links only)

Pages read:
- `docs/release-changelogs/lightact-4.14/lightact-4.14.1.md`: 21 April 2026, 3 upgrades. [1]
- `docs/release-changelogs/lightact-4.14/lightact-4.14.0.md`: 21 April 2026, 1 Epic, 3 upgrades. [0]
- `docs/release-changelogs/lightact-4.14/lightact-4.14.rc2.md`: 27 March 2026, 2 upgrades. [RC2]
- `docs/release-changelogs/lightact-4.14/lightact-4.14.rc1.md`: 26 March 2026, 2 Epics, 8 upgrades, mostly mapping and workspace crash fixes. [RC1]
- `docs/release-changelogs/lightact-4.14/lightact-4.14.b1.md`: 13 March 2026, 6 Epics, 49 upgrades. [B1]
- Carried over: LA4-6865 (Crossfade Update) is in both RC2 and 4.14.0.

### Crossfade
- LA4-6556 [B1]: types unified across Timelines, Sections and Layers: None, FadeHold, FadeDip.
- LA4-6865 [RC2, 0]: Timeline no longer has crossfade properties; Section no longer has "Inherit". A jump inside a section does not trigger its crossfade; it runs only on entering the section, by jump or by playing in.
- LA4-6866 [RC2]: Crossfade dropdown works on multi-selected layers or sections. LA4-6904 [0]: sub-second section crossfades work (0.9 s failed before).

### CanvasMaps and OutputMaps
- LA4-5675 [B1]: CanvasMaps reworked: filter canvases and objects, organise by collections. LA4-6286: new "Canvases" window, like Objects but only Canvases.
- LA4-6645 [B1]: OutputMaps: the eye icon controls visibility in CanvasMaps, not Viewport. Eye and Solo on a collection cover its children. Default visible: Video Screens, Projectors, 3D Models; hidden: Throwers. Objects with no texture output (People, Iris Cams) are omitted or permanently hidden. Order follows the Objects window.
- LA4-6647 [B1]: drag the gray upward arrow of an Object (CanvasMaps) or Virtual Output (OutputMaps) onto a Canvas or Object to auto-create a subarea at that item's resolution.
- LA4-5772: "Duplicate multiple" makes an array of subareas. LA4-6660: right-click menu: Add to output/objects, Unmap from outputs/objects, Duplicate, Duplicate multiple, Delete. LA4-5776: unmap options reduced to "Unmap from objects" (CanvasMaps) and "Unmap from outputs" (OutputMaps).
- LA4-6605, LA4-6563, LA4-6562, LA4-6288 [B1]: lasso or Ctrl+click multi-select and group move; Shift on a corner pin scales proportionally; Ctrl disables snapping; subareas snap to canvas centre.
- LA4-6254 [B1]: arrow keys always move exactly 1 px regardless of zoom; holding moves 1 px, waits 1 second, then repeats.
- LA4-6704 [B1]: F in CanvasMaps, OutputMaps or Devices returns the view to its initial position.
- LA4-6643 [B1]: minimum padding lowered from 36 to 8. Unclear: the ticket does not name the padding control.
- LA4-6248 [B1]: Viewport drop dialogs for Video screens, Projectors, Throwers and 3D models ask for name, resolution and pixel pitch (which sets size).
- LA4-6807 [RC1]: subareas may have negative dimensions (for example -360x120 px); selection hit-testing fixed for them.

### Output freeze and saving
- LA4-6700, LA4-6503, LA4-6698 [B1]: freeze and unfreeze outputs from the CTRL Menu; "Freeze all/Unfreeze all" in OutputMaps above Fade up; OutputMaps warns when an output is frozen.
- LA4-5677 [B1]: Ctrl+S saves the project even with focus on an Output window.

### Workspaces and GUI
- LA4-4288 [B1]: Workspaces in the top menu. LA4-6835 [0]: default workspaces are Basic, Playback, Mapping (Basic.xml, Playback.xml, Mapping.xml); Performance workspace removed.
- LA4-6200 [B1]: "2-screen Workspace" makes F11 span two displays. LA4-6625: unfocused floating windows auto-collapse (disable in Preferences, UI tab). LA4-6657: Edit > Reset Windows.
- LA4-6791, LA4-6790 [RC1]: custom workspace order persists; Previous workspace (Ctrl+PgUp) wraps.
- LA4-6733 [B1]: a new enable/disable icon replaces the eye in Tracks and Layer connections; the eye now means visibility only.

### Search and ordering
- LA4-5749 [B1]: every dropdown has a search bar. LA4-6672: asset lists sort alphabetically like Windows Explorer, not by import order. LA4-6738: asset versions list newest first (v14, v13, v12, v4, v3, v1).
- LA4-6638 [B1]: Timeline properties "Elements" panel (below DMX) lists sections, markers, layers. Columns: Trigger, Time Point, Position, Type, Update. Active items green, others "Inactive". Enter jumps to the top result.
- LA4-6635 [B1]: Cue List search by name or CueXYZ ID (for example 77.65.82).
- LA4-6633, LA4-6631, LA4-5750, LA4-6634 [B1]: Ctrl+F focuses search in Objects/Viewport, Assets and Timeline Editor (Variables search if a layer is selected, else Elements).
- LA4-6646 [B1]: reorder objects in the Objects window by drag; collections stay on top.

### Timeline, devices, logs
- LA4-6576 [B1]: after dropping an asset on the Timeline the first option is preselected; Up/Down and Enter confirm. LA4-6555: holding an arrow key scrubs with acceleration.
- LA4-6721 [B1]: all Device nodes log "Enabling …" then success or failure, for example "Enabling NDI Sender 0…", "NDI Sender 0 enabled." (also NDI Receiver, Audio Input, Audio Output, DirectShow).
- LA4-6717 [B1]: an NDI Sender name already in use on the network (for example "LightActNDI0" from another instance) crashed on enable; fixed.
- LA4-6921 [1]: Play Video stopped purging frames every second when held at the end of a NotchLC layer (29.97 FPS NotchLC .mov in a 60 FPS project). Status Testing.

---

## LightAct 4.13
`docs/release-changelogs/lightact-4.13.md` (index, links only)

Pages read:
- `docs/release-changelogs/lightact-4.13/lightact-4.13.4.md`: 11 March 2026, 3 upgrades, embedded-audio fixes (stops after loops, pop at volume 0, garbling after jumps). [4]
- `docs/release-changelogs/lightact-4.13/lightact-4.13.3.md`: 08 March 2026, 3 upgrades, Play Video buffer fixes. [3]
- `docs/release-changelogs/lightact-4.13/lightact-4.13.2.md`: 08 March 2026, 3 upgrades. [2]
- `docs/release-changelogs/lightact-4.13/lightact-4.13.1.md`: 01 February 2026, 3 upgrades. [1]
- `docs/release-changelogs/lightact-4.13/lightact-4.13.0.md`: 12 January 2026, 10 upgrades. [0]
- `docs/release-changelogs/lightact-4.13/lightact-4.13-rc1.md`: 30 December 2025, 1 Epic, 16 upgrades. [RC1]
- `docs/release-changelogs/lightact-4.13/lightact-4.13.b2.md`: 15 December 2025, 4 Epics, 9 upgrades. [B2]
- `docs/release-changelogs/lightact-4.13/lightact-4.13.b1.md`: 15 December 2025, 10 Epics, 62 upgrades. [B1]
- Carried over: LA4-6137 (LightSync no longer drops machines from the session prematurely, status Testing) is in B1 and B2. LA4-6481 and LA4-6482 are the same node (6482 is the 4.12 backport).

### Project folder layout and logs
- LA4-6314 [RC1]: logs and videoimportsummary.json go in a Logs folder next to the .la file.
- LA4-6315 [RC1], LA4-6604 [0]: console.log in the Logs folder holds high-volume diagnostics, overwritten each session. It starts "###LightAct 4 Console File###", then "#Build:" and "#Current time:". LA4-6603 [0]: startup crash when console.log is not writable, fixed.
- LA4-6316 [RC1]: saves go to Projectfolder\Exports, not ProgramData\Lightact\Lightact4\saves. LA4-6317: EDID files go in the project folder (Testing). LA4-6435: BugSplat dumps go to crashDumps next to the .la file.
- LA4-6318 [RC1], LA4-6683 [2]: autosaves moved to an Autosaves folder in the project, then in 4.13.2 Autosave was removed entirely (options hidden in Preferences, no folder created).
- LA4-6623 [1]: -no_bugsplat (command line or options.ini) disables BugSplat or just its popup, depending on the SDK.
- LA4-6470 [RC1]: "Package for Support" reintroduced.
- LA4-6497 [RC1]: log timestamps are [YYYY-MM-DD HH:MM:SS.mmm], for example [2025-11-27 10:22:31.231].
- LA4-6495 [RC1]: every cue fired manually, via OSC or DMX is logged with cue name, timeline and source.
- LA4-6491, LA4-6492 [RC1]: logged: play state changes, end-of-section events with resulting pause or loop, playhead jumps, group sync and Engaged/Disengaged changes (DMX, OSC, manual), timecode state transitions (Chasing TC includes the current TC), "Layer X entered active/inactive state", "Section Y entered active/inactive state".
- LA4-6478 [RC1]: "Log every message" checkbox, default on, on all six TCP/UDP/OSC nodes. Example: "OSC Receiver 0" received message "oscMessage" from 192.168.0.15 on port 6345.
- LA4-6477 [RC1], LA4-6723 [3]: Play video node logs phases (Loading, Ready, Scrolling), "always ready" and "play" buffer start/filled, audio enable/disable, buffer flushes; rate limited.
- LA4-6494, LA4-6493 [RC1]: option to skip loading selected devices at launch; per-device load logs ("Loading Blackmagic… Blackmagic loaded").

### Timecode and sync
- LA4-6513 [RC1]: Timeline state "Engaged (Ignore TC)". While engaged and chasing, a manual trigger (pause, jump buttons, Cue List cues via UI, OSC or DMX) no longer disengages; the Timeline ignores TC, then resumes chasing when incoming timecode jumps, or stops and starts.
- LA4-6214 [B1]: sync option "Follow in all but these sections", inverse of "Follow in these sections only".
- LA4-6204 [B1]: Timeline properties: editable section names, Start TC, computed End TC (yellow when it overlaps another section's Start TC), warning on overlapping custom TC times.
- LA4-6172, LA4-6152 [B1]: Timecode Monitor always shows all TC sources with editable names and offsets; multiple incoming Art-Net TC sources supported.
- Unclear: LA4-6507 [B2] (30 fps MTC on a 60 fps timeline skips frames 30 to 59 in Timecode play mode) is a problem statement with status Code Review.

### Crossfade (first design, later replaced)
- LA4-6343, LA4-3781, LA4-6342 [B2]: Timeline "Cross-fade time [s]"; Section and Layer dropdowns Inherit or Fade. Crossfade time comes from the destination (section or layer) only, never combined. Superseded in 4.14 and 4.17.

### Timeline programming
- LA4-6308 [B1]: "Split at Playhead" splits a layer in two; offered only when the playhead is on the layer.
- LA4-6205 [B1]: locked tracks block creating, editing, pasting or dropping layers. LA4-6331: paste finds the next free unlocked track or creates tracks. LA4-5765: trash bin icon deletes any track.
- LA4-6161 [B1]: timeline playback speed multiplier, only when the timeline is not synchronised.
- LA4-6203 [B1]: Timelines window shows Timeline fade, master volume and render time.
- LA4-5768 [B1]: timeline drop menu: "Assign to all layers", "Assign to all layers on this track" (assets and mappings).
- LA4-6211 [B1]: click-jumps snap the playhead to section starts and ends, markers, layer boundaries, else the nearest vertical line. LA4-6069: select all layers left, right or both on a track.
- LA4-6206 [B1]: non-whole project frame rates (29.97, 59.94, 48 named) "temporarily removed" from Project Settings.
- Unclear: no changelog up to 4.17 says they were reinstated.
- LA4-6572 [0]: "Force project framerate" off by default; it is effectively ignored once any output is enabled.

### Assets and import
- LA4-5274 [B1]: proxy video files are found by filename suffix: _proxy2 or _prx2 for 2x lower resolution, _proxy4 or _prx4 for 4x, and so on. Primary and Editor machines can play them for Viewport previews.
- LA4-6132 [B1]: "Apply to Notch Blocks" under Preview downsampling renders Play Notch Block at reduced resolution, then upscales.
- LA4-5943, LA4-6089 [B1]: asset ingestion is three non-blocking phases: import, get data (optional), load & play. FileWatcher can be disabled so imports during shows are user controlled.
- LA4-5817 [B1]: an asset file without a version suffix appears in the Version dropdown as "No version".
- Unclear: LA4-6237 states the problem (missing asset on open set layers to None), status Done; the new behaviour is implied only. LA4-5652 (frame count in asset properties) is worded as an inquiry.
- LA4-6568, LA4-6526 [0]: image sequence FPS now changes playback speed; PNG, TIF, JPG stills keep accurate colour.
- LA4-6186 [B1]: non-Latin characters in project file names are not supported ("temporarily"); a warning is shown.

### LightNet and Backup
- LA4-6075 [B1]: drag a server into your cluster: a Primary becomes Secondary and joins; Backup or Editor just join.
- LA4-5187, LA4-6065, LA4-6064 [B1]: Selective Backup: a "Setup" button assigns Backup servers to servers; Automatic failover is optional, off by default, license dependent. Manual takeover: drag a Backup onto the server to replace (same cluster). The Backup mirrors output windows so the switch fits in a single frame.
- LA4-6187 [B1]: "End LightSync" button lets non-primary machines stop the Primary's LightSync session.
- LA4-5474, LA4-5476 [B1]: Performance window graphs all cluster machines; Preferences "Status message frequency" 100ms to 1s; the Primary's top-right indicator reflects the whole cluster.
- LA4-5994 [B1]: "Vertical Sync" dropdown: "VSync one output window" (default) or "VSync all output windows".
- LA4-5924 [B1]: the GUI auto-minimises when an output window is enabled on the GUI's display, or on any display of a secondary server.
- LA4-6073 [B1]: device node machine checkboxes can all be unchecked ("None" option).

### Mapping, DMX, AutoBlend
- LA4-6223 [B2]: Subarea coordinates are stored as integers, not floats (fixes 1px edge errors).
- LA4-5680 [B1]: Projectors removed from Mapping dropdowns; Canvas to Projector is legacy, behind the -legacy launch argument.
- LA4-6434 [B1]: DMX fixture "pixel straddling" (Fixture editor, Pixel properties, on by default) lets one pixel span a universe border. LA4-6309: max 1024 pixels per DMX fixture.
- LA4-6581 [0]: AutoBlend defaults: Angle Cutoff on at 45°, Linear mode on.

### Nodes and editing
- New [B1]: "Run on Shutdown" (LA4-5767), absolute value (LA4-5580), "Texture Vignette" (LA4-6171), JSON Parser and Packager (LA4-5706), Expression with dynamic float inputs (LA4-5634), "Set DMX Out State", a boolean toggling "Send DMX" in the DMX Out window (LA4-6481).
- LA4-6216: Render Texture has separate Scale X and Scale Y. LA4-5238: some Get data nodes output a "Content override" boolean. LA4-5795: Softedge "Draw handles" renamed "Render handles".
- Unclear: LA4-5802 offers project framerate "on the Application Tick node or a new Project framerate node" without saying which shipped.
- LA4-6070 [B1]: "Restore to default" for unconnected inputs in variable groups. LA4-6476 [B2]: watches on dropdown integers show "label [value]". LA4-6496 [B2]: "Undo Stack" viewer under Redo.
- LA4-6620 [1]: Deltacast interlaced input (FHD60i) fixed via Field Merging (VHD_CORE_SP_FIELD_MERGE = TRUE). LA4-5446 [B1]: option to hide all Viewport warnings.

---

## For automation and pipelines

- Launch arguments: -secondary, -backup, -editor (the last two from 4.17, set LightNetRole at startup); -asio (4.16); -no_bugsplat (4.13.1, also via options.ini); -legacy.
- OSC cue trigger (4.16): /la/playctrl/cue/X or /la/playctrl/cue/X.Y, matched against each cue's CueXYZ. A cue left at -1,-1,-1 cannot be fired by OSC or DMX, and OSC requests containing -1 are ignored.
- DMX cues need only their enabled channels to match (4.17). Master fade also dims DMX output (4.16). sACN is Multicast only. OSC, Art-Net and sACN inputs can be muted from the menu (4.17), so check that first when triggers go silent.
- Timecode: a manual, OSC or DMX trigger on a chasing timeline puts it in "Engaged (Ignore TC)" until incoming TC jumps or restarts (4.13). Non-whole project frame rates were removed in 4.13.
- Content naming: proxy suffixes _proxy2/_prx2, _proxy4/_prx4 (4.13). Unversioned files show as "No version"; versions list newest first; assets sort alphabetically (4.14). Props go in Assets/Props as FBX/OBJ (4.16). From 4.17 LightAct can make HAP and proxy files itself, per asset or per Video collection.
- Import is non-blocking and FileWatcher can be disabled for controlled imports (4.13).
- Next to the .la file since 4.13: Logs\ (logs, console.log, videoimportsummary.json), Exports\, crashDumps\, EDID files. Autosave is gone from 4.13.2; save explicitly.
- Logs work as an event feed: millisecond timestamps, cue triggers with source, layer and section active/inactive, timeline and TC state, every TCP/UDP/OSC message with IP and port ("Log every message", default on), device enable results. From 4.17 also computer name, IP, frame rate, update time.
- Control nodes: Get Section, Get marker, Go to Section/Marker (current timeline only), Run on Marker, Set Timeline Master Fade/Volume/Speed Multiplier, Timeline Group get/set, Set DMX Out State, Run on Shutdown, JSON Parser and Packager, Expression, Trigger Volume. Play Video outputs Buffer and Missed.
- LightNet: project transfer never moves assets (4.17). Only the Primary monitors Cluster presence and runs Iris. Editors need permission to request a project transfer.
- Crossfade changed in 4.13, 4.14 and 4.17. Current model: sections only, seconds (0 = off), "Hold opacity", audio included; defaults affect only new timelines and sections.
- 4.17 renames: Pause to Hold, Freerun & Restart to Freerun on Hold; layer Preview Only mode removed.
- Subarea coordinates are integer pixels (4.13) and can be negative in size (4.14). Duplicated Canvas areas only get unique IDs from 4.16.4.
- Not marked Done when published: LA4-5662 (ASIO), LA4-6317, LA4-6315, LA4-7379, LA4-7352, LA4-6921, LA4-6773, LA4-6507, LA4-6137. Verify on the target build.
