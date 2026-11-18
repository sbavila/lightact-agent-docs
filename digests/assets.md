# assets

## What this section covers

Which file types LightAct can ingest as Assets (3D models, video, images, image sequences, audio, Notch blocks, TouchDesigner components) and the rules they must follow.
It also covers the two ingestion controls in the Assets window (FileWatcher, Get data) and the filename rule that turns files into versions of the same Asset.
Seven short pages. Most of the value for a pipeline is in the file naming rules.

## 3D models
`docs/assets/3d-model.md`

- Supported 3D formats: **.fbx** and **.obj**, and "to an extent" .dae.
- FBX is the preferred format and has the best support.
- To apply content to a 3D model it must be properly UV mapped and its normals must face the correct way.
- Render mode: default is **Shaded** (best for general visualisation in the Viewport).
- If the 3D model is a Source for a projector, always use **Unshaded** render mode, otherwise the content will not look as intended.

## UV Mapping of 3D Models
`docs/assets/3d-model/uv-mapping-of-3d-models.md`

- Use as much of the UV map as possible. Wasted UV space costs VRAM.
- In most cases the UV map should have no overlapping areas. In Blender, **Smart UV Project** usually achieves this.
- Exception: surfaces that always show the same content (example given: wheels of a car) may overlap.
- Check the UV map in Blender by applying a grid texture to the model.
- A grid image can be exported from LightAct with a **Color Grid** node: right-click its output pin.

## Asset ingestion management
`docs/assets/asset-ingestion-management.md`

- Options live in the properties menu of the **Assets** window.
- **FileWatcher**: monitors the asset repository. If enabled, a file copied into the repository is ingested the moment it lands.
- Disable FileWatcher if you want manual control over when assets are ingested.
- **Get data**: reads the Asset and makes it ready to play. LightAct must Get the Data of an Asset before it can play it.
- Unclear: the page does not say where the asset repository folder is, or whether Get data runs automatically after FileWatcher ingestion.

## Asset versioning
`docs/assets/asset-versioning.md`

- Versioning works for all asset types.
- To enable it, add `_versionName` to the end of the Asset's filename.
- Examples given: `_v1`, `_v2`, `_v3`; `_YYMMDD` (or any 6 numbers); `_YYMMDDa`, `_YYMMDDb`, `_YYMMDDc`.
- Pick one naming method and stick to it. Then, when a new version of an Asset is imported, LightAct automatically uses it.
- Unclear: the page does not say how LightAct decides which version is newest, what happens if naming methods are mixed, or how to pin an older version.

## Audio files
`docs/assets/audio-files.md`

- Supported audio: **.mp3** and **.wav**.
- Stereo only "at the moment".

## Notch and TouchDesigner
`docs/assets/playing-notch-blocks.md`

- Notch blocks: **.dfxdll** file extension. Both Notch 0.9xxx and 1.0 and above are supported.
- TouchDesigner components: **.tox** files.
- Details are in the real-time content playback section (Notch page and TouchDesigner page), not here.

## Video, images and image sequences
`docs/assets/video-formats-and-codecs.md`

- Video files, single images and image sequences are all treated as a **Video asset** and used in more or less the same way.
- Containers: **.mp4** and **.mov**. The container does not determine the codec (a .mov can hold H.264, NotchLC or HAP).
- LightAct only decodes. It cannot encode.
- Codecs decoded on the CPU: **H.264**.
- Codecs decoded on the GPU: **NotchLC**, **HAP**, **HAPa**, **HAPQ**. Much better performance (maximum resolution at a given framerate), much larger files.
- For the highest number of concurrent videos, HAP is usually recommended.
- Codecs not in the table may play if they are in a supported container, but they are not fully supported and performance may be limited.
- Performance benchmarks exist only for HAP and NotchLC. LightAct does not optimise for or benchmark ProRes, H.264 or other codecs.
- Images: **.png**, **.jpg**, **.tga**, **.tiff**. For best performance .png or .tiff is recommended.
- A single image file is treated as a video file with one frame.
- Image sequence rules:
  - All frames must have the same file extension. No mixing png and jpg.
  - Filenames (without extension) must be identical apart from an incrementing number at the end.
  - Example: `Frames0000.tif`, `Frames0001.tif`, `Frames0002.tif`, `Frames0003.tif`, `Frames0004.tif`.
  - Numbering must start at 0, not at, for example, 10000.
  - With versioning, the pattern is `000_Counter000_v1.tif`, `000_Counter001_v1.tif`, and so on: the frame number comes before the version suffix.
- A detected image sequence gets an image sequence icon, and its properties let you choose the playback framerate.
- Unclear: the page's own versioned sequence example jumps from `Counter001` to `Counter003`, which looks like a typo. Whether gaps are tolerated is not stated.
- Unclear: the image list says ".tiff" while the sequence examples use ".tif".

## For automation and pipelines

- Deliverable formats to target: video as .mov or .mp4 with HAP (most concurrent streams) or NotchLC; stills as .png or .tiff; audio as stereo .mp3 or .wav; 3D as .fbx.
- Version by filename suffix: `<name>_v2.mov`, or `<name>_251118.mov`. Keep one scheme for the whole project so new versions are picked up automatically.
- Image sequences: same extension, same base name, counter at the end starting from 0. If versioned, put the version after the counter (`Name000_v1.tif`).
- With FileWatcher enabled, copying a file into the asset repository is enough to ingest it. Turn FileWatcher off if a pipeline needs to drop files in without LightAct reacting mid-show.
- An Asset is not playable until **Get data** has run on it.
- Proxy files use a second filename convention (`_proxyN` / `_prxN`), covered in the video-playback digest. Unclear: the manual does not say how a proxy suffix and a version suffix combine in one filename.
- The API page documents no asset methods, so ingestion is driven by the file system, not by JSON-RPC.
