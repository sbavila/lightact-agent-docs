# lightnet

## What this section covers

LightNet is LightAct's multi-server system: machine roles (Primary, Secondary, Editor, Backup), the three communication channels (LightNet, LightSync, Asset transfer), and licensing rules for clusters.
It covers the Windows share that every non-Primary machine needs (the LightNetProjects folder), multicast and NIC settings, the steps to scan, invite and establish a cluster, frame sync, asset distribution, and how LightAct decides which server runs which object ("Run on").
Eight pages.

## LightNet overview
`docs/lightnet/lightnet-overview.md`

- LightNet lets you: detect other LightAct machines, give each a role, set up multiple clusters, set up frame syncing, transfer project files inside a cluster, and edit in real time across the cluster.
- "Machine" and "server" mean the same thing.
- Roles:
  - **Primary**: the controlling server. Only one per cluster. (Elsewhere called Director, Host, Master.)
  - **Secondary**: servers outputting content. Many allowed. (Actors, Clients, Playout machines.)
  - **Editor**: outputs nothing. Usually an operator's laptop.
  - **Backup**: on stand-by, ready to replace a failed server. (Understudy.)
- "Non-Primary machines" means Secondary, Editor and Backup.
- Small projects often use one Primary that outputs content plus one Backup. Any number of Editors.
- If the Primary outputs content alongside Secondaries, the outputs of Primary and Secondaries "might not be in sync".
- All servers that output content need their outputs genlocked.
- Roles that output (or must be able to): Primary with outputs, Secondaries, Backups. Roles that do not: Primary without outputs (usually a Unit v or Double v) and Editors (a laptop is enough).
- Licences: all machines in a cluster need the same licence tier, with two exceptions:
  1. **Live** and **Ultimate** can be combined in one cluster.
  2. **Editor** machines can use the **Creator** licence.
- Only the **Ultimate** tier enables the Secondary role.
- Mixed cluster: Ultimate machines as Secondaries and Backups, a Live machine as the Primary.
- A Live machine can be a Backup, but then it can only replace a Primary.
- A **No Outputs Ultimate license** exists for Primary servers with no outputs.

## LightNet basics
`docs/lightnet/lightnet-basics.md`

- Three communication channels:
  - **LightNet**: cluster and role management, real-time edits.
  - **LightSync**: frame-locking between machines.
  - **Asset transfer**: copies assets. Uses Robocopy.
- File management is the Primary's job:
  1. The Project folder is set up on the Primary.
  2. The Primary transfers the entire Project folder into the **LightNetProjects** folder of every machine in the cluster, where it is opened.
  3. Real-time edits flow as long as the LightNet connection is active.
  4. Asset ingestion and distribution across the cluster are managed from the Primary.

## Network setup
`docs/lightnet/network-setup.md`

- All machines must be on the same network, with IPs and subnet masks that let them reach each other.
- Create a folder named exactly **LightNetProjects** on every machine in the cluster. On non-Primary machines it receives all project files and assets, so it needs enough space and a fast enough drive.
- The Primary does not strictly need one (nothing copies to the Primary; it always copies from its own Project folder), but creating it there too is recommended.
- Share the folder with Windows sharing so it sits directly at the root of the machine's network path. The Primary must be able to open and write to it on every non-Primary machine.
- It must be reachable both ways:
  - by computer shared name (the manual's example reads `LA5\\LightNetProjects\`),
  - and, more importantly, by IP address, for example `\\192.168.0.160\LightNetProjects\`.
- It must be shared directly. A path such as `\\192.168.0.160\anotherFolder\LightNetProjects\` does not work; LightAct cannot transfer files to it.
- If Windows asks for a username and password, tick **Save my credentials**. Do this for both access types (name and IP).
- Set the folder in **Edit > Preferences > LightNet**, under *LightNet project path*.
- Also in **Preferences > LightNet**:
  - **Multicast address and port**: must be identical on every machine in the same cluster.
  - **Assigning NICs**: LightNet and LightSync channels can each use a different NIC.
- Several clusters on one network: give each cluster its own Multicast address and port.
- Unclear: the page spells the folder both "LightNetProjects" and "LightNetProject". The create and share steps use LightNetProjects.
- Unclear: the default multicast address and port are not given.

## Finding LightAct Machines
`docs/lightnet/lightnet-clusters.md`

- Order: enable LightNet on all machines, scan on Primary, assign roles, establish cluster, then asset transfer (a separate step, repeated many times in a session).
- Enable: tick the **Enabled** checkbox in the **LightNet Management** window (Window top menu).
- **Preferences > LightNet > Enable on new project**: LightNet is already enabled every time LightAct starts.
- A launch argument also enables LightNet (see the miscellaneous digest: `-lightnet`).
- **Scan network** button: lists every machine that has LightNet enabled and uses the same Multicast address and port.

## Establish LightNet Cluster
`docs/lightnet/establish-lightnet-cluster.md`

- A successfully established cluster means all 3 channels (LightNet, LightSync, Asset transfer) work and all servers have the same project file open.
- Steps: invite machines into the Primary's cluster, assign roles, establish.
- Invite: drag a machine into the Primary's cluster. It is automatically given the Secondary role.
- Role: set with the role dropdown. Assigning Primary to a machine in your cluster removes it from your cluster, since a cluster has only one Primary.
- **Establish Cluster** button does, in order:
  1. Save the project file on the Primary.
  2. Establish a LightNet connection with all machines in the cluster.
  3. Check all machines have the same version of LightAct.
  4. Check the Primary has access to the LightNetProjects folders on all machines.
  5. Transfer the project file to all machines.
  6. Open the project file on all machines.
  7. Establish LightSync.
  8. Check that project files match on all machines.
- If any step fails, the cluster will not work as intended. The most common failure is step 4 (access to LightNetProjects folders).
- Green circular lights blink on each LightNet message (real-time updates). Dragging an object makes them blink much faster.
- Message frequency is also set by the **Real-time edit updates** and **Heartbeat frequency** dropdowns in **Project settings > LightNet**.
- Manual controls per machine: **Access check** (does the Primary have write access to that machine's LightNetProjects folder) and **Connect/Disconnect**.
- Multi-user: projects can be modified on the Primary, all Secondaries and all Editors. Changes go to the Primary first, then to the whole cluster in real time.
- Editing on Secondaries is not blocked, but only editing on Primary and Editor machines is recommended and officially supported.

## LightSync connection
`docs/lightnet/lightsync-connection.md`

- Two sync layers are needed:
  - **Hardware sync**: Quadro Sync card. Syncs the render cycles of all GPUs in the cluster. Frame-locking and genlock to an external source are both supported.
  - **LightSync**: software level. Makes the whole cluster output the same timeline frame.
- The only way to keep the cluster in sync when a server fails and a Backup takes over is to sync the entire cluster to an external genlock generator (House Sync). With frame-locking, where one machine is the timing master, Hardware sync cannot be guaranteed if that machine fails.
- Approved LightSync topologies:
  1. 1 Primary with outputs + 1 Backup with outputs.
  2. 1 Primary without outputs + Secondaries with outputs + Backups with outputs.
- The number of Editors is not limited by the software.
- In **LightNet Management**, the LightSync lights are lit all the time because LightSync messages are sent every frame.
- Manual controls: **Invite in/Kick out** (add or remove a machine from the Sync session) and **Framelock** checkbox (whether the Primary waits for this machine to finish its frame). Enable Framelock only on genlocked machines. If Framelock keeps disabling itself, that machine is not in Hardware sync.

## Asset management in LightNet
`docs/lightnet/asset-management-in-lightnet.md`

- Asset distribution is managed from the **Assets** window on the Primary. The Assets window and each Asset's Properties show where the Asset is assigned.
- **Check Asset presence**: checks whether all Assets are distributed across the cluster. Usually automatic; the button forces a re-check.
- If a server that should hold an asset is missing it, the icon turns red and the asset's properties name the server.
- Transfer: **Initiate transfer across cluster** (everything not yet transferred) or **Initiate transfer** on an individual asset.
- Only assets not already present on the target are copied. LightAct does not overwrite existing assets.
- **Always transfer all the assets** checkbox: sends every asset to every machine. Required if the asset a layer plays will be changed during the show, because LightAct cannot know in advance which server will need it. Example: swapping assets with incoming DMX and **Index Manager**.

## Server workload distribution
`docs/lightnet/server-workload-distribution.md`

- Most objects and assets have a **Run on** property: the server(s) that object runs on. Applies to Viewport objects, Layers, Devices and Assets.
- Automatic assignment starts in **Output Maps**:
  1. A Virtual output is assigned to a Physical output of a server. Viewport objects (Video screen and so on) mapped to that Virtual output are assigned to that server.
  2. Layers rendering to those Viewport objects are assigned to the same servers.
  3. Assets used in those layers are assigned to those servers too.
- Devices are the exception: Run on for a Device is set manually in the Properties of the Device node.
- Run on is usually **Automatic**. It can be switched to **Manual**.
- An object not running on the machine you are looking at shows a downscaled texture and a WiFi icon. Downscale amount: **Preview downsampling** in **Project settings > General**.
- Every layer runs on every server. Run on changes how video files and Notch blocks play:
  - **Primary and Editor**: original video files and full-resolution Notch blocks if the layer is assigned to them; otherwise the lowest (most downscaled) proxy video file and a downscaled Notch block.
  - **Secondary**: original files if the layer is assigned to it; nothing at all if not.
- Notch downscaling also follows *Preview downsampling*, but only if **Apply to Notch blocks** is checked.
- Run on for Assets is visible in the Assets window and in Properties.
- **LightNet Workload** window shows the Run on setting for all objects.
- Unclear: the page says to open a Viewport object's "Preferences" to find the Run on section; elsewhere object settings are called Properties.

## For automation and pipelines

- The Primary is the single point of control: project file, asset ingestion and asset distribution all start there. Feed content to the Primary's project folder, not to Secondaries.
- Asset transfer is a separate, manual step (Initiate transfer) using Robocopy, and the manual says LightAct "doesn't overwrite existing assets" on the target. Do not count on a changed file with an unchanged name being re-sent; use versioned filenames (see the assets digest).
- If code or external control will swap which asset a layer plays at show time, **Always transfer all the assets** must be ticked, otherwise the needed file may not be on the server that outputs it.
- Each non-Primary machine needs a share named exactly `LightNetProjects` at the share root, writable from the Primary by both computer name and IP, with saved credentials. This is the most common reason Establish Cluster fails.
- All machines must run the same LightAct version and share the same Multicast address and port. Use a different address and port per cluster.
- On Primary and Editor machines, layers not assigned to them play the most downscaled proxy file. Supplying proxy files (`_proxyN` / `_prxN`) is what keeps the Primary responsive. Secondaries play nothing for layers not assigned to them.
- Device nodes (OSC, MIDI and so on) do not follow Output Maps. Their Run on must be set by hand, which decides which machine actually receives or sends the control data.
- LightNet can be enabled at launch with the `-lightnet` argument and a machine can be given the Secondary role with `-secondary` (miscellaneous digest).
- The API page documents no LightNet methods.
