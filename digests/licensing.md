# Licensing (digest)

## What this section covers
- LightAct 4 is licensed through Wibu CodeMeter. Licenses live in a "container": a USB dongle or a software package locked to one machine.
- Adding, updating and transferring a license is a manual exchange of files by email with LightAct support.
- A license on the container must still be applied inside LightAct.

## Licensing Overview
`docs/licensing/licensing-overview.md`
- **CodeMeter Runtime** must be installed. A container can hold several licenses, including other vendors'.
- **CodeMeter Control Center** lists containers. **WebAdmin** shows the licenses on each.

## Adding or updating a License
`docs/licensing/adding-or-updating-a-license.md`
- Dongle serial number must start with at least 3-344. Older dongles cannot take a LightAct license.
- Create the request from the container the license should live on.
- Machine-locked: if no LightAct container exists, drag **LightAct.WibuCmLIF** (from LightAct-CodeMeterContainer.zip) into CodeMeter Control Center to get an empty one. Select it, **License Update**, "Create license request", **Commit**.
- USB dongle: select it, **License Update**, "Create license request", then **Extend existing license** or **Add license of a new vendor** with Firm code **6001083**, **Commit**.
- Commit saves a **.WibuCmRaC** file. Email it to support@lightact.com.
- LightAct returns a **.WibuCmRaU** file. Import it with **Import license update**. On **Error: Import Update failed. Error 0**, drag and drop the file into CodeMeter Control Center.
- Unclear: the manual spells the option "Create lisence request".

## Applying a License
`docs/licensing/applying-a-license.md`
- LightAct: Edit > Preferences > **Licenses** tab, click the license's **Apply** button. Hover **Features:** to see enabled features.
- Expired licenses show *'This license needs to be upgraded'*.

## Transferring a License
`docs/licensing/transferring-a-license.md`
- Order: send a request file from the source container. LightAct sends an update file that destroys the license. Send back the receipt file. Send a request file from the destination container. LightAct sends the update file that creates it.
- Manual process with a small fee.

## For automation and pipelines
- No online or scripted activation is described. Every change needs an email round trip with support, so allow lead time.
- File types: **.WibuCmRaC** (request), **.WibuCmRaU** (update), **.WibuCmLIF** (empty container).
- Firm code **6001083**.
- After importing, someone must click **Apply** in LightAct.
- Features are per license. Check **Features:** before relying on one.
