# content-mapping

## What this section covers

Content mapping is the path a texture takes from a layer in a timeline to a Viewport object. Getting from a Viewport object to a physical display is a separate topic (Output Maps).
There are three ways: Direct mapping, Canvas mapping (the Canvas Maps window) and Throwers (3D-aware virtual projectors of content).
Three pages.

## Content mapping overview
`docs/content-mapping/content-mapping-overview.md`

- Three mapping methods:
  1. **Direct mapping**: content is rendered directly to a Viewport object.
  2. **Canvas mapping**: a 2D workflow. Content is rendered to the 2D texture of a Canvas, then from there to Viewport objects in various configurations. Canvas maps let you splice, cut and modify the canvas texture before it reaches the Viewport object.
  3. **Throwers**: mapping that takes the 3D position of Viewport objects into account.
- Direct mapping: select the Viewport object in the layer's **Mapping** variable, or drag from the Viewport object to the layer.
- Limit: with Direct mapping a layer can be mapped onto only one object at a time.
- To map one layer to 2 objects use:
  - **Canvas Maps**: the most common and recommended approach.
  - **Texture to mapping** layer template: requires knowledge of layer connections.

## Canvas Maps
`docs/content-mapping/canvas-mapping.md`

- **Canvas Maps** is the name of the window where canvas mappings are created.
- Create a canvas in the **Canvas Maps** window or the **Thumbnails** window.
- Render a layer to a Canvas: select the canvas in the layer's **Mapping** dropdown, or drag from the canvas onto the layer.
- Map a whole canvas onto a Viewport object: drag from the canvas's arrow onto the Viewport object.
- Subareas:
  - Create with **Shift+drag** on a canvas, or right-click and choose **Create a subarea**.
  - Right-click an existing subarea to edit it.
  - Map it by dragging from its arrow onto the destination Viewport object.
- A "Mapping" in Canvas Maps means the connection between a source (sub)area and the destination subareas.
- Right-click the destination subarea to edit the mapping. One option is **Create layout**.
- **Create layout** makes a node Layout dedicated to that one mapping. By default it contains a single **Mesh Warp** node. Any other nodes can be added.

## Throwers
`docs/content-mapping/throwers.md`

- A **Thrower** is a helper virtual object that maps content onto Viewport objects according to their position in the Viewport's 3D scene.
- Create one from the Viewport's right-click menu or by dragging from the Viewport toolbar. Hover the small arrow next to the Thrower icon in the Toolbar to change which type the toolbar places.
- Use one: select a Viewport object, open its **Content** collapsible, and in the **Sources** section pick the Thrower. Or drag from the Thrower onto the Viewport object.
- The page says there are 5 types: **Perspective**, **Orthogonal**, **Spherical**, **Cubic**, **Cylindrical**.
  - **Perspective**: throws content as a projector would. Its Properties have a **Frustum** collapsible that adjusts the projection.
  - **Orthogonal**: throws content in parallel. Changing its size changes the projection.
  - **Spherical**: throws content in all directions. Works best with **equirectangular content**. Use the **Horizontal flip** checkbox if content appears mirrored.
  - **Cubic**: throws content in all directions. Needs a cubemap: one texture with 6 rectangles, one per cube face, in a set pattern. The cubemap resolution must equal the Thrower's resolution. **Horizontal flip** checkbox available. If the content is 6 separate square textures, combine them with the **To Cube Map** node.
- Unclear: Cylindrical is named as a type but has no description on the page.
- Unclear: the cubemap face layout is shown only in an image, not described in text.

## For automation and pipelines

- Decide the mapping method before specifying content, because it changes what the deliverable looks like:
  - Direct mapping: one layer feeds one Viewport object.
  - Canvas mapping: one layer feeds a Canvas, which is sliced to Viewport objects by subareas.
  - Spherical thrower: equirectangular content.
  - Cubic thrower: a cubemap whose resolution matches the Thrower's resolution, or 6 square face textures joined with **To Cube Map**.
- Unclear: this section gives no resolution rules for Direct or Canvas mapping content.
- A layer's target is set in its **Mapping** variable (a Viewport object or a canvas).
- One layer to several screens needs Canvas Maps (recommended) or the **Texture to mapping** layer template. Direct mapping cannot do it.
- Per-mapping correction (warp and anything else) lives in the layout made by **Create layout** on a destination subarea, which starts with a **Mesh Warp** node.
- 3D models used as a Source for a projector should be in Unshaded render mode (assets digest).
- The API page documents no methods for canvases, Canvas Maps or throwers.
