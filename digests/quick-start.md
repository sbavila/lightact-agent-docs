# Quick Start (digest)

What this section covers:
- The content pipeline in one page: Assets and Device nodes feed Layers, Layers render to mappings or Device nodes.
- Core terminology: Timeline, Timeline group, Track, Section, Layer, Marker, Canvas, Thrower, Video output and the DMX terms.
- The user interface: dockable windows, Workspaces, Top Bar (Lock UI), Viewport navigation, drag and drop.
- The full keyboard and mouse shortcut list.
- General troubleshooting (launch crashes, cloud-sync folders) and how to file a support request (Package for Support).

## Content flow
`docs/quick-start/overview-of-content-pipeline.md`
- Content comes in two ways: through the Assets repository (assets are then played back in Layers), or through Device nodes such as NDI, Spout or Unreal Texture Share. Device content also goes through the layer system.
- Layers live in Timelines. All content to play and all data to process passes through the layer system at some point.
- Layers render to 3 types of mappings:
  - Direct mappings: the layer renders straight onto a viewport object (for example a video screen).
  - Canvases: a texture container that lets you map the texture, or parts of it, onto viewport objects.
  - Throwers: a virtual viewport object that "projects" content onto viewport objects.
- Layers can also render to Device nodes. This is the usual way to send content out through NDI or video IO cards (Deltacast, Blackmagic).
- All of the above destinations can also receive content through Set Texture nodes.

## Terminology
`docs/quick-start/terminology.md`
- Timeline: where content (layers), events and actions are sequenced and composited. A project can have several independent timelines. A timeline holds Tracks, Sections, Layers and Markers.
- Timeline group: one or more Timelines. Used to control syncing to external timecode sources and to control play states of the Timelines in it.
- Track: a lane in a Timeline that holds one or more layers.
- Layer: exists in a Timeline, has a beginning and an end (set by the Duration parameter). Does content playback and processing (video, image, image sequence, Notch block) or just logic. "Layers in LightAct are called Layer Templates."
- Layouts: the node-based system. Found in Layers, in Mappings (Canvas Maps and Output Maps windows) and in Projectors.
- Variable: a container for information (integer, float, color, texture and more). Layer variables exist within one layer. Global variables are accessible anywhere.
- Section: part of a timeline. Often used as a cue.
- Marker: a position on a Timeline.
- Viewport: the visual preview of the real-world setup.
- Video screen: virtual stand-in for a physical video screen.
- Thrower: helper virtual object that maps content onto viewport objects using their position in the 3D scene.
- 3D model: usually imported as `.fbx` or `.obj` assets.
- Primitive: a cube, plane, sphere or cone.
- Null object: an empty object used as a container to group and move other objects.
- Marker in Viewport: a 3D position in the Viewport window (separate from a Timeline marker).
- Canvas: holds one texture of arbitrary resolution. Usually filled by Layers, then sent to viewport objects through the Canvas maps window.
- Assets: external resources used by a project. Images, image sequences, video files, Notch blocks, TouchDesigner components, audio files, 3D models, Unreal Engine projects.
- Video output: virtual stand-in for a physical output on the system's GPU.
- DMX is DMX512. Art-Net and sACN are UDP-based protocols carrying DMX over Ethernet. Fixture means a DMX light fixture.
- Unclear: this page says a layer's length is set by a "Duration" parameter. The Layers page lists "End (HMSF)" as the layer property.

## User Interface
`docs/quick-start/user-interface.md`
- Windows are dockable. Drag them and drop on docking handles.
- A Workspace is a saved window arrangement. Three predefined: Basic, Playback, Programming. Custom workspaces can be created.
- A workspace is saved whenever the program closes or you switch to another workspace.

## Top Bar
`docs/quick-start/user-interface/top-bar.md`
- The Top Bar shows machine and project state. The page has headings for Master Fade and Master Volume but no text under them.
- CTRL (Master Control) button:
  - Lock UI: locks all program functions until the password is entered. Click CTRL, choose Lock UI. The popup is prefilled with the default lock password from the Preferences Window, General tab. Click Lock.
  - Unlock by typing the password, or by pressing LeftCtrl + LeftShift + L.
  - Default password: `LightAct`.
  - Lock cursor to app: keeps the cursor inside LightAct's GUI.
- Unclear: Master Fade and Master Volume are not described. The sentence describing CTRL is cut off.

## Drag & drop
`docs/quick-start/user-interface/drag-and-drop.md`
- Most actions are drag and drop. Dragging the video screen icon from the Viewport toolbar creates a video screen where you drop it, with a popup to choose the resolution.
- Hold a number key while dropping to skip the popup and pick the option with that sequential number.

## Quick Tips
`docs/quick-start/user-interface/quick-tips.md`
- (i) icons open the Quick Tips window with help resources and shortcuts for the place where you clicked.

## Viewport Navigation
`docs/quick-start/user-interface/viewport-navigation.md`
- Right mouse button rotates the camera, middle mouse button pans, left mouse button selects. Hold right mouse button and use WASD to fly.
- Camera modes: Orbit (rotates around the selected object, or around a point in front of the camera if nothing is selected) and Pilot (rotates around itself, best with WASD).
- Predefined camera positions: Top, Front, Side. Right-click in the Viewport to create a custom camera position, then recall it from the Viewport properties menu.
- Most Viewport settings are in the Properties menu of the Viewport.

## Shortcuts
`docs/quick-start/shortcuts.md`

General
- Ctrl + N new file. Ctrl + O open. Ctrl + S save. Ctrl + Shift + S save as. Ctrl + I import asset. Ctrl + Q quit.
- Ctrl + C copy. Ctrl + V paste. Ctrl + Z undo. Ctrl + Y redo. Ctrl + A select all.
- Ctrl + F4 closes the undocked hovered window or popup.

Viewport
- Hold 1 to 4 while dragging a viewport object with a texture (for example a video screen) onto the viewport: picks the matching resolution automatically.
- NumPad 0 resets the camera. F focuses on the selected object. Del deletes the selected object.
- T translate gizmo. R rotate gizmo. E scale gizmo. L shows object labels. W toggles World/Local coordinate space.
- Shift + drag duplicates an object. Shift + L locks or unlocks an object. Shift + F looks at the source object of a projector.

Timelines (the window listing timelines)
- Shift + click Play: plays the current Timeline and stops all others.
- Shift + click Pause: pauses the current Timeline and stops all others.
- Shift + click Stop: stops all Timelines.
- Double click on timeline: creates a sequence.
- Shift + mousewheel: scrolls the Sequences section horizontally.

Timeline (the editor)
- Double click on a sequence: creates a blank layer. L + left click: creates a blank layer.
- M + left click: creates a marker.
- Ctrl + . jumps to next marker. Ctrl + , jumps to previous marker.
- Shift + mousewheel scrolls horizontally. Ctrl + mousewheel moves the playhead 1 frame. Ctrl + Shift + mousewheel moves the playhead 1 second.
- Ctrl & + increases the selected section's Start TC time by one frame. Ctrl & - decreases it by one frame.

Layers
- Del deletes the selected layer.
- Shift + Del deletes it and shifts track content to fill the gap.
- Shift + Ctrl + Del deletes it and shifts timeline content to fill the gap.

Inserting layer templates
- Every layer template editable in the Template Editor window can have a shortcut key. Defaults (users may have changed them): V video layer, I image layer, N Notch layer, D NDI or Spout layer, C color grid layer, S solid color layer. The page gives each as "key + right click".

Creating variables in Layouts
- Hold a key while clicking the plus icon of a variable group to create that type directly: F float, I integer, B boolean, S string, c color, t texture, 2 vec2, 3 vec3, r resolution, 1 canvas, o object, d device. (Case is as printed in the manual.)

Nodes
- Ctrl + X cuts a node. Q straightens connections between selected nodes.
- Arrow keys move the selected node 1 step, or the selected point 1 step in the Setup Window of a node such as Texture Mask.
- Ctrl + arrows: selected point moves 10 steps. Ctrl + Shift + arrows: 100 steps. Shift + arrows: selects the neighbouring point.

Curve Editor
- Double click adds a point. Del removes the selected point.

Fixture editor (Custom mode, where Fixture pixels can be selected or deselected)
- Double click adds a pixel. Up/down arrows move the pixel 1 unit. Ctrl + up/down 10 units. Shift + up/down 100 units. Del deletes the pixel. ESC stops the connecting process.

Video Output (the Output window must have focus)
- Ctrl + T toggles the "Always on top" flag of an Output window.
- Alt + Ctrl + Shift + Q closes the Output window.

Dragging onto tracks (untitled table at the end of the page)
- Drag to empty space on a track: creates a layer on the track.
- Shift + drag to empty space: creates the layer and shifts all affected layers on the track to the right.
- Ctrl + Shift + drag to empty space: creates the layer and shifts all affected layers on the sequence to the right.
- Drag onto an existing layer: finds all variables of the same type and sets them to the dragged object or asset.
- Shift + drag onto an existing layer: replaces that layer with a new one, adjusts its duration and shifts layers to its right on the track.
- Ctrl + Shift + drag onto an existing layer: replaces that layer and adjusts the position of all layers to its right on the sequence.

Unclear items on this page:
- Unclear: "sequence" is used here ("Double click on timeline creates a sequence") but the Terminology page has no Sequence. It appears to mean Section.
- Unclear: template insert is "key + right click" here, but the Fast layer workflows page says key + left mouse button, or Alt + key.
- Unclear: Curve Editor double click adds a point here. The Curve Editor page says double-clicking a point deletes it.
- Unclear: the step sizes differ between node Setup windows (Ctrl 10, Ctrl + Shift 100) and the Fixture editor (Ctrl 10, Shift 100).
- Unclear: templates are edited in a "Template Editor window" here. The User Layer Templates page puts template management in Preferences, Files tab.
- Unclear: the "Assets" heading on this page is empty.

## General troubleshooting
`docs/quick-start/general-troubleshooting.md`
- Do not save project files in Google Drive, Dropbox or similar synced folders. These services interfere with file access and can make LightAct crash or act oddly.
- GUI black on launch: most likely an unsuitable GPU. Use a discrete Nvidia GPU.
- Closes on launch (cache): delete certain files and folders in `C:\ProgramData\LightAct\LightAct4`. If that fails, uninstall completely including the Preferences, then reinstall. Contact support@lightact.com either way.
- Unclear: which files and folders to delete is shown only in a screenshot, not in the text.
- Closes on launch on version 4.12 or 4.13 (DirectShow): launch with the `-omit "14"` argument, which stops the DirectShow module loading:
  `"C:\Program Files\LightAct\LightAct4\LightAct4.exe" -omit "14"`
  Adjust the path if installed elsewhere. The DirectShow Receiver node in the Devices window will then be unavailable.

## Asking for support
`docs/quick-start/asking-for-support.md`
- Contact: support@lightact.com or Discord. First check you are on the latest version and that the docs do not cover the issue.
- Always include: a Package for Support, a Bug Report, and the problem Assets if possible.
- Package for Support (introduced in LightAct 4.13): zips the entire project folder except the Assets. Contains the project file, all log files, BugSplat crash dumps (if any) and other diagnostic information. Send any problem asset separately.
- Bug report contents: Reproduction steps (short, clear), The result, Expected result, plus screenshots, screen recordings, and photos or videos of the outputs.

## For automation and pipelines
- Pipeline model: Assets or Device nodes (NDI, Spout, Unreal Texture Share) feed Layers. Layers render to Direct mappings, Canvases, Throwers, or back out to Device nodes (NDI, Deltacast, Blackmagic). Set Texture nodes can also feed those destinations.
- Objects a control tool will reference: Timeline, Timeline group, Track, Section, Layer, Marker, Canvas, Video output, Global variable. Sections often act as cues. Timeline groups govern timecode sync and play states for their Timelines.
- A project is a folder. Assets sit inside it and are the only part left out of Package for Support. Logs and BugSplat crash dumps are in the project folder too.
- Keep project folders out of Google Drive, Dropbox and similar sync services. Plan asset delivery so files land in a plain local folder.
- Asset kinds LightAct accepts: images, image sequences, video files, Notch blocks, TouchDesigner components, audio files, 3D models (`.fbx`, `.obj`), Unreal Engine projects.
- Install paths: program in `C:\Program Files\LightAct\LightAct4\LightAct4.exe` by default, cache and settings in `C:\ProgramData\LightAct\LightAct4`. Launch argument `-omit "14"` skips the DirectShow module (relevant to 4.12 and 4.13).
- Lock UI default password is `LightAct`, and LeftCtrl + LeftShift + L unlocks without a password. Lock UI is an operator guard, not security.
- Dropping an asset or object onto an existing layer sets every variable of the matching type at once. The same drop with Shift or Ctrl + Shift replaces the layer and ripples the track or the whole sequence.
- Delete has ripple variants too: Shift + Del ripples the track, Shift + Ctrl + Del ripples the whole timeline.
