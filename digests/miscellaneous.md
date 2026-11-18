# miscellaneous

## What this section covers

Two pages. The first lists the command line arguments LightAct can be launched with, including custom key/value arguments readable from inside a project.
The second explains how to turn on WebUI, a browser control page served from the LightAct server that exposes selected Global variables.

## Launching LightAct with Arguments
`docs/miscellaneous/launching-lightact-with-arguments.md`

- Executable path used in every example: `"C:\Program Files\Lightact\Lightact4\Lightact4.exe"`.
- Three kinds of argument: standalone, advanced, custom.
- Standalone arguments, format `Lightact4.exe -argument`:

| Command | Effect |
| --- | --- |
| `-log` | Extensive logging. The Log Window shows extended messages for Iris cameras, down-sampling, up-sampling and so on. |
| `-developer` | Shows developer information such as object IDs, down-sampled resolutions and more. |
| `-most_recent` | Opens your most recent project. |
| `-clear` | Clears the cache folder. |
| `-secondary` | Gives the machine a Secondary role in LightNet. |
| `-lightnet` | Sets the LightNet checkbox to ON. |

- Advanced arguments, format `Lightact4.exe -argument "<advanced_arguments>"`:

| Command | Effect |
| --- | --- |
| `-project "<filepath>"` | Opens the given project on launch. |
| `-window "<poz.x> <poz.y>"` | Sets the position of the program window on launch. |
| `-window "<poz.x> <poz.y> <size.x> <size.y>"` | Sets the position and size of the program window on launch. |
| `-nic "<ip> <port>"` | Sets the default NIC and data port for the application. If the NIC is not valid, a default NIC is set. |

- Example: `"C:\Program Files\Lightact\Lightact4\Lightact4.exe" -nic "192.169.0.101 12345"`.
- Custom launch arguments: any `-key "value"` pair. The string after the dash is the key, the string in quotation marks is the value. Read it in a layout with the **Get Launch Argument** node.
- Example: `-pizza "cheese"` gives key `-pizza`, value `cheese`.
- Unclear: the page does not say whether several arguments can be combined in one launch, though nothing says they cannot.
- Unclear: for custom arguments the page calls the key "-pizza" with the dash. Whether the Get Launch Argument node expects the dash is not stated.
- Unclear: what "data port" means for `-nic` is not explained.

## WebUI Setup
`docs/miscellaneous/webui-setup.md`

- WebUI is available for LightAct **server license** only.
- It gives a custom user interface to control LightAct from the browser of any device on the same network.
- Setup:
  1. Find the server's IPv4 address (`ipconfig` in Command Prompt run as administrator).
  2. Open **http-server.exe** and read its port number. Location: `C:\WebUI 4\dist\http-server.exe`. If the file is missing, contact support@lightact.com.
  3. In LightAct: **Project Settings > General**, enable **Enable REST & WebUI**.
  4. In a browser open `<IP>:<Port>/index.html`, for example `192.168.0.111:8000/index.html`.
- If WebUI receives no data: untick **Enable REST & WebUI** and tick it again, and confirm the browsing device is on the same network.
- Exposing a variable: drag a **Local variable** into a **Global variable** group, or add a **Global variable** directly. Widen the right side of the window until the **WebUI icon** is visible, and click it to enable the variable in WebUI.
- **Default value** and **Min and max** can be set for the variable.
- Every Global variable with the WebUI button enabled is visible in WebUI.
- Unclear: the setting is named "Enable REST & WebUI" but no REST endpoints are documented on this page, and the page does not say how this relates to the JSON-RPC API on port 9899 (api digest).
- Unclear: the port (8000 in the example) is read from http-server.exe; the page does not say whether it is fixed or configurable.

## For automation and pipelines

- A server can be booted straight into a show from a script or a Windows startup task: `Lightact4.exe -project "<filepath>"`, or `-most_recent`.
- `-lightnet` and `-secondary` let a playout machine come up already in LightNet with the Secondary role, with no one at the keyboard.
- Custom `-key "value"` arguments plus the **Get Launch Argument** node are a way to pass per-machine or per-venue configuration into project logic at launch.
- `-developer` shows object IDs in the UI. The API identifies everything by integer ID, so this may help when building against it. Unclear: the manual does not confirm these are the same IDs.
- `-log` gives extended Log Window output for diagnosing down-sampling, up-sampling and Iris camera issues.
- WebUI needs a server license and the **Enable REST & WebUI** project setting. Only Global variables with the WebUI button enabled show up, each with Default, Min and max.
- Global variables are also what the API exposes as Container ID `0` in `variable.list`, so a Global variable is the common hand-off point for external control.
