# video-playback

## What this section covers

How LightAct plays Video assets: the Play video node, the relationship between Content, Project and Application framerate, per-Timeline frame buffering settings, and proxy video files for LightNet.
It also gives measured maximum concurrent UHD streams for two LightAct servers (Double 2, reActor v3) and a troubleshooting guide for missed frames.
Seven pages.

## Playing video files
`docs/video-playback/playing-video-files.md`

- Video assets are normally played with the **Video** or **Multi-layer** stock layer templates. Both contain a **Play video** node, which does the actual playback. The node's inputs match the layer's exposed Layer variables.
- Three framerates: **Content framerate** (of the Video asset), **Project framerate**, **Application framerate**.
- Rules:
  - Application framerate should always be higher than or equal to Project framerate.
  - Project framerate should in most cases equal Content framerate, and never be lower.
  - If Application framerate drops below Content framerate, frames are missed.
- When a Play Video node is triggered, LightAct passes it the time of the frame it wants. That time comes from the playhead, which advances at the Project framerate.
- Examples:
  - Project 30, Content 30, Application steady 60: each frame is requested and shown twice.
  - Content 30, Project 60, Application 60: each frame is requested twice. With *Frameblending* enabled, you get 2 frames blended every second frame.

## Frame buffering
`docs/video-playback/frame-buffering.md`

- "Buffering" here means the same as caching.
- Settings are per Timeline, in the Timeline's properties under the **Video Playback** collapsible section:
  - **Video Buffer**: number of frames LightAct tries to keep in an internal buffer while playing a video asset.
  - **Video Preload Time**: seconds before the playhead reaches the start of a layer containing a Play Video node at which frames are loaded into the Video Buffer.
  - **Always Ready Buffer**: the share of the Video Buffer kept in memory at all times, so a playhead jump straight onto a video layer has frames ready.
- Worked example on the page: Video buffer 20 frames, Video preload time 5 seconds, Always ready buffer 50% = 10 frames. More than 5 seconds before the layer, the Play Video node holds 10 frames. At the 5 second mark it loads the full buffer.
- Unclear: the example says the full buffer is "19 in the case above" although Video buffer is set to 20.
- Tuning advice:
  - Playback performance problems: raise Video buffer to, say, 32 and Video preload time to, say, 20.
  - Highly interactive timelines with lots of jumping: raise Always ready buffer.
  - Watch the *Missed frame* indicator in the **Performance** window.
- **Performance** window has a **Video playback** collapsible section showing the status of every Play Video node in the project.
- Per-node graphs (double-click the video layer, select the Play video node):
  - **Missed frames**: whether a frame was missed in the last few seconds.
  - **Decode times**: time to decode the codec. Low for HAP and NotchLC, often higher for H.264 and other CPU codecs.
  - **Decompress times**: time to unpack the frame.
  - **Buffered frame**: buffer status. A slowly falling graph may mean disk read speed is too slow.
  - **Frame blending**: shows blending of frames when Frame blending is enabled.

## Proxy video files
`docs/video-playback/proxy-video-files.md`

- Purpose: in LightNet, Primary and Editor servers show all content in the Viewport without the cost of full-resolution playback.
- Naming: a Video asset with **`_proxyN`** or **`_prxN`** in its name is a proxy downscaled by a factor of N. The Play Video node upscales it by N before passing the frame on.
- Example: original `LightAct_showreel_published.mov`, with one proxy downscaled by 2 and one by 4.
- Proxy status is shown in the asset's Properties.
- A server that should play a proxy always picks the most downscaled one. With `_proxy2` and `_proxy4` both present, it plays `_proxy4`.
- Which server plays the original, a proxy or nothing is decided by the Run on logic (lightnet digest, Server workload distribution).
- Unclear: the page says the suffix is "in its name" but does not show the exact proxy filenames in text or say where the suffix must sit relative to a version suffix.
- Unclear: the page does not say whether LightAct can generate proxy files or whether they must be supplied.

## LightAct Hardware video playback performance
`docs/video-playback/video-playback-performance.md`

- Measurement method for the benchmark pages:
  - Servers in Base Configuration: a single GPU.
  - 4 x 4UHD displays. One shows the GUI; the other 3 are joined into a single 11,520 x 2,160 output with Nvidia Mosaic, and LightAct outputs to that.
  - Output refresh rate: 60 Hz for 30 and 60 fps playback, 50 Hz for 25 and 50 fps playback.
  - Nothing else running, Nvidia Control Panel closed, GUI full screen with only the Performance window open, thumbnails loaded first.
  - Every 1 or 2 seconds a new Play video node (all in one layer) starts a unique copy of the same file. The limit is where the Missed frames counters start to increase regularly.
- The Video playback section of the Performance window is stated as "available in 4.12".
- Unclear: the two result pages say the measurements were made on LightAct v4.10.1, which is earlier than the 4.12 feature the method says it used.

## Double 2
`docs/video-playback/video-playback-performance/double-2.md`

- Measured July 2025, LightAct v4.10.1. Media drives: 2 x SSD 2TB in RAID1. HAP files exported with an 8 chunk setting.

| Resolution | Codec and framerate | Data rate [MB/s] | Max # videos |
| --- | --- | --- | --- |
| UHD | NotchLC @ 60 FPS | 637 | 3 |
| UHD | NotchLC @ 30 FPS | 320 | 7 |
| UHD | HAP @ 60 FPS | 250 | 12 |
| UHD | HAP @ 30 FPS | 125 | 32 |

- No 25 or 50 FPS rows are given for this server. Results depend on several factors and may be lower or higher.

## reActor v3
`docs/video-playback/video-playback-performance/reactor-v3.md`

- Measured July 2025, LightAct v4.10.1. Media drives: 4 x SSD 2TB in RAID10. HAP files exported with a 28 chunk setting.

| Resolution | Codec and framerate | Data rate [MB/s] | Max # videos |
| --- | --- | --- | --- |
| UHD | NotchLC @ 60 FPS | 637 | 8 |
| UHD | NotchLC @ 50 FPS | 531 | 8 |
| UHD | NotchLC @ 30 FPS | 320 | 16 |
| UHD | NotchLC @ 25 FPS | 265 | 18 |
| UHD | HAP @ 60 FPS | 250 | 20 |
| UHD | HAP @ 50 FPS | 207 | 25 |
| UHD | HAP @ 30 FPS | 125 | 49 |
| UHD | HAP @ 25 FPS | 104 | 60 |

- Results depend on several factors and may be lower or higher.

## Video playback troubleshooting
`docs/video-playback/video-playback-troubleshooting.md`

- Start in the **Performance** window, **Video playback** section.
- **Missed frames** rising continuously: Play Video nodes cannot read, decode and render fast enough. Usual causes: insufficient disk read speed, or insufficient CPU speed.
- Missed frames not rising but output still stutters: the cause is something else.
- Disk read speed: most likely with large-file codecs (HAP, NotchLC, image sequences). If Decode times and Decompress times are low and frames are still missed, suspect the disk. The Performance window shows current **Disk read speed**.
- Background software that uses disk bandwidth (the page names Google Drive) should be disabled on the server.
- Decode speed: every codec uses some CPU, including HAP and NotchLC. H.264 needs far more. High Decode and Decompress times in the Play video node graphs point to the CPU.
- Framerate: if the video file's framerate is higher than the application's current framerate, frames are missed. The only fix is to raise the application framerate.
- Blinking or flickering on videos with an alpha channel: disable the **Frame blending** boolean. With it enabled, semi-transparent pixels may flicker.
- Unclear: one sentence reads "If disk read disk speed is low, yet you see Missed frames ... check the Decode and Decompress times". It appears to mean "if the disk is not the bottleneck", but the wording is ambiguous.

## For automation and pipelines

- Encode for the Project framerate. Content framerate should equal Project framerate; Project framerate must never be lower than Content framerate.
- Proxies are made by filename: add `_proxyN` or `_prxN` where N is the downscale factor (2, 4, ...). LightAct upscales by N on playback and always chooses the largest N available. For LightNet shows, plan for a proxy alongside each master (the manual does not say LightAct makes them).
- Capacity planning numbers (UHD, single GPU): Double 2 handles 12 HAP @ 60 or 32 HAP @ 30; reActor v3 handles 20 HAP @ 60, 25 HAP @ 50, 49 HAP @ 30 or 60 HAP @ 25. NotchLC is far heavier (3 to 8 streams @ 60).
- Data rates to budget disk throughput: UHD HAP is 104 to 250 MB/s per stream (25 to 60 FPS); UHD NotchLC is 265 to 637 MB/s per stream.
- HAP chunk setting used in the benchmarks: 8 on Double 2, 28 on reActor v3.
- Buffering is configured per Timeline (Video Buffer, Video Preload Time, Always Ready Buffer). Timelines that will be jumped around by external triggers need a larger Always Ready Buffer.
- Turn Frame blending off for any content with alpha.
- Keep sync clients such as Google Drive off playback servers. This matters if a content pipeline was planning to deliver files through a sync client.
- Health signals worth watching are Missed frames and Disk read speed in the Performance window. The API's `system.performance` (api digest) returns fps, frame time and RAM only, not missed frames.
