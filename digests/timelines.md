# timelines

## What this section covers

How show sequencing is organised: Timeline Groups, Timelines, and the Sections, Layers and Markers inside them.
It defines the play states, the Timeline group Mode, the Cue List window and Global Cues, the difference between Project framerate and Application framerate, and how a Timeline chases external timecode (LTC, MTC, Art-Net).
Five pages.

## Overview
`docs/timelines/overview.md`

- Two windows: **Timelines** (control and monitor Play state of all Timelines and Timeline groups) and **Timeline Editor** (edit Sections, Layers and Markers of one Timeline).
- Hierarchy:
  - **Timeline Group** contains one or several Timelines.
  - **Timeline** contains layers, sections and markers. A Timeline can be in only one Timeline Group.
  - Sections, layers and markers belong to one Timeline.
- Every Timeline and every Timeline group has its own play controls:
  - **Play**: playhead keeps advancing, including across section borders.
  - **Play and pause**: playhead advances to the last frame of its section, then pauses (hold).
  - **Play and loop**: playhead advances to the last frame of its section, then jumps back to the first frame of that section.
  - **Pause**: playhead does not advance, but the active layers are still executing.
  - **Stop**: playhead does not advance. No layers are executing.
  - **Jump to previous** / **Jump to next**: jumps to the previous or next section, marker or layer.
- Timeline group **Mode** property:
  1. **Only one**: only one Timeline in the group can be in a Play state. When another Timeline switches to Play, all the others switch to Pause. Useful with Timeline cross-fades.
  2. **Multiple**: play states of the Timelines in the group are fully independent.
- **Speed multiplier**: introduced in LightAct 4.12. Affects the playback speed of the entire timeline.

## Sections & Markers
`docs/timelines/sections.md`

- **Section**: splits a timeline into separate parts. Very often used as Cues, triggered manually or by external signals such as DMX or OSC. Sections can also be synced to external timecode.
- **Marker**: marks a specific point in the timeline. Can trigger a specific Play state, or other actions such as Timeline jumps. Can also be used as a cue.

## Cue List
`docs/timelines/cue-list.md`

- Open with **Window > Cue List**. Lists all Cues in the entire project.
- Columns:
  - **Trigger**: icon matches the cue's **Play state change** property. Clicking it makes the Playhead jump to that Cue and execute the *On playhead pass* action.
  - **Position**: position in the Timeline, and position relative to the Playhead.
  - **Play state change**: whether the Timeline's play state changes when the cue is triggered.
- Sections and Markers only appear in the Cue list if their **Use as cue** checkbox is true.
- A Cue placed beyond the timeline duration shows its position in a yellow warning color. This can only happen when **Auto duration** is disabled in the Timeline's properties.
- **Global Cues**: actions not tied to a position on the Timeline (example: fade out when a performer leaves the stage).
  1. Add a global variable of type **Event**.
  2. In a Layer Layout, create a *Getter node* from the Event variable. It fires a lifeline output each time the Event is triggered. Program the action from there.
  3. Click the control icon on the Event variable so it shows as a *Global Cue* in the Cue List window.
- Clicking **Trigger** on a Global cue fires the Event wherever the Playhead is, but only if the Layer holding the logic is active at that moment.
- The **Set fade** layer template changes the fade of a video output, section or layer when its Event variable is triggered.

## Project framerate
`docs/timelines/project-framerate.md`

- All Timelines share one framerate, set in **Project settings > General**.
- Effects of Project framerate:
  - Timeline increments: at full zoom, each vertical line in the Timeline editor is one frame.
  - Playhead progression: the Playhead steps frame by frame (30 increments per second at 30).
  - Snapping: layers, markers and sections are created and moved on that frame grid.
- Set it to the content framerate "or multiple of 2". For 25 FPS content use 25 or 50.
- Changing Project framerate after programming does not move anything, but from then on snapping uses the new grid, so a moved layer may not be returnable to its exact original position.
- **Application framerate** is the rate LightAct is actually running at. It is set by the refresh rate of your displays, or by performance load if LightAct cannot keep up.
- **Force Project framerate**: with no outputs enabled, the UI is synced to the refresh rate of the UI display by default (60 Hz display gives 60). With Force Project framerate enabled and no outputs enabled, Application framerate always equals Project framerate.

## Syncing to a timecode
`docs/timelines/syncing-to-a-timecode.md`

- Three steps: receive external TC, sync the Timeline group to the incoming TC, sync a Timeline to its Timeline group.
- Receiving: LTC through Audio input nodes and MTC through MIDI Receiver nodes (both in the Devices window); Art-Net timecode through the DMX In window.
- Timeline group: pick the TC source in its **Source** dropdown. The Timelines window then shows incoming TC + *Timecode offset*.
- Timeline group **Engaged** means it locks to incoming TC when valid TC arrives. Statuses next to the Engaged/Disengaged button:
  1. **No TC source**: no Sync source selected in the group's Properties.
  2. **No TC**: a source is selected but it is not receiving TC.
  3. **Chasing TC**: the source is receiving valid TC.
- **Grace period** (Timeline group Properties): if TC stops, LightAct assumes for the set duration that TC will resume. Covers short unintended breaks.
- LTC only: bit-flip prevention. A sudden LTC jump caused by audio noise is ignored unless following LTC frames confirm it.
- Timeline, **Sync sections** part of its Properties:
  1. **Sync in all sections**
  2. **Sync in selected sections**
  3. **Sync in unselected sections**
  In each case a section chases TC only when the TC falls within it.
- Each synced section has a **Start TC** property: the TC at which it starts chasing.
  1. **Automatic**: Start TC equals the section's position in the timeline (section at 00:01:50:23 gets Start TC 00:01:50:23).
  2. **Custom**: you set the Start TC.
- An Automatic section placed after a Custom section gets its Start TC from the Custom section's Start TC plus the time difference between the two section starts.
- **Show start TC labels** checkbox displays the Start TC times.
- A selected section with Custom Start TC can be nudged one frame with **Ctrl & +** and **Ctrl & -**.
- To sync the Timeline, switch its sync mode to **Engaged**. Timeline statuses:
  1. **Group not chasing TC**: the parent Timeline group is not chasing, so the Timeline is not either.
  2. **Chasing TC**
  3. **Outside synced sections**: incoming TC is not inside any synced section.
  4. **Ignoring TC**: TC is inside a synced section, but a manual trigger (a play state button, a cue trigger "or something else") made the Timeline ignore it for now. If the incoming TC jumps and is still inside a synced section, the Timeline starts chasing again.

## For automation and pipelines

- Model for code: Timeline Group > Timeline > Sections, Layers, Markers. One framerate for the whole project.
- Timeline positions snap to the Project framerate grid. Generate times that land on whole frames of that framerate.
- Five play states exist in the UI (Play, Play and pause, Play and loop, Pause, Stop). Pause keeps active layers executing; Stop executes no layers.
- In a Timeline group with Mode **Only one**, putting one Timeline into Play pauses the others. Expect that side effect when driving transport from code.
- A Section or Marker is only a Cue if **Use as cue** is true. Cues can be fired by external signals; see the osc-and-midi digest for OSC addresses and the api digest for `section.trigger` and `timeline.gotoLandmark`.
- Global Cues are Event-type global variables with a Getter node in a Layer Layout. They only do anything while the Layer holding that logic is active.
- A manual or external trigger on a timecode-synced Timeline puts it into **Ignoring TC** until the incoming TC jumps. A script that fires cues on a TC-chasing Timeline will therefore break the chase.
- Timecode setup is per Timeline group (Source, Grace period, Engaged) and per Timeline (Sync sections, Start TC, Engaged). None of it is exposed in the documented API.
- **Speed multiplier** needs LightAct 4.12 or later.
