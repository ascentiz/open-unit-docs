# Read Exoskeleton Data

Read Ascentiz-H device status and sensor data through the B-core Pi 1 compute box. 

!!! warning "Startup can cause motion"
    Reading data does not request motion, but Ascentiz-H startup performs wear detection and can move its motors. Follow the approved wearing and startup procedure with a trained operator. This example does not include the exhibition document's unworn motor-restraint workaround. Do not bypass wear detection or device-side safeguards.

## Equipment and software

- One AZ compute box connected to an Ascentiz-H exoskeleton.
- One Windows laptop for network access and the monitoring application.
- Wireless access to the compute box, or the supplied HRS IX network cable for a wired connection.
- The SDK and demo already installed on the exhibition compute box.

The compute box connects to the Ascentiz-H USB Type-C port **without a lightning symbol**. 

The document identifies a green Ascentiz-H backpack indicator as successful wear detection. If detection fails, Ascentiz-H does not output data. Stop and consult the device operator rather than forcing a data connection.

## Connect the laptop to the compute box

| Connection | Compute box address | Laptop preparation |
| --- | --- | --- |
| Wireless | `10.42.0.1` | Join the compute box's CM5-prefixed Wi-Fi hotspot; use `dhcp_ip_set.bat` for the non-wired setup. |
| Wired | `192.168.10.1` | Connect RJ45 to the laptop and IX to the compute box; run `static_ip_set.bat`. |

The exhibition hotspot is named `CM5-0B2D`; the name can differ on another device. Obtain credentials from the device administrator. The batch files are supplied in the Windows desktop's `dist-exe` folder and are not included in this repository.

When changing connection methods, apply the matching batch file and update the destination address. The exhibition guide recommends wireless operation when stable; a cable limits the laptop's distance from the compute box. These addresses and scripts are exhibition-specific, not universal hardware defaults.

## Read data using the Python SDK

Run the SDK **on the Linux ARM64 compute box**, not in the Windows monitoring application. The documented release is:

- Wheel: `az_sdk-1.4.0-cp314-cp314-linux_aarch64.whl`.
- Import name: `az_sdk`.
- Directory: `/home/bodyos/cm5-az/spi_master/sdk`.
- Supplied example: `demo.py`.

The wheel filename targets CPython 3.14 and Linux AArch64. It does not establish compatibility with Windows, macOS, other CPU architectures, or other Python versions. The exhibition guide states that this SDK is already installed on the compute box.

### 1. Open an SSH session

For wireless access:

```bash
ssh bodyos@10.42.0.1
```

For wired access:

```bash
ssh bodyos@192.168.10.1
```

Use the credentials supplied by the administrator. Passwords are intentionally omitted from the public documentation.

### 2. Check the environment

In the compute box's terminal, use the Python environment where the exhibition SDK is installed:

```bash
cd /home/bodyos/cm5-az/spi_master/sdk
python3 --version
python3 -c "import az_sdk; print(az_sdk.__file__)"
```

Confirm that Python matches the wheel and that the package imports successfully. If it does not, check the intended environment before attempting to reinstall anything.

### 3. Run the supplied demo

Review the supplied `demo.py` and confirm that it matches this exhibition release and contains only the intended data-reading and local CSV-recording operations. Then run:

```bash
python3 demo.py
```

The exhibition guide lists the implemented operations in the demo: connection, status retrieval, sensor-data retrieval, sensor-data recording to CSV, and disconnection. “Writing sensor data” here means saving a local CSV file, **not writing commands to the sensors or actuators**.

The uploaded Word file does not contain the demo source, function signatures, parameters, returned fields, or CSV destination. Follow the actual demo for call order, output, and cleanup; this page does not invent an `az_sdk` API. Other planned interfaces are not claimed to work.

## View data using the Windows application

This is an alternative way to view data; the Word file does not specify whether it can run concurrently with the SDK demo.

1. Complete the network connection above.
2. Open the desktop `dist-exe` folder and launch `机械臂数据监控.exe`. This is the application's filename in the exhibition guide, even though this example reads Ascentiz-H data.
3. In the Microsoft Edge interface, open **连接配置** (Connection Configuration).
4. Select `10.42.0.1` for wireless or `192.168.10.1` for wired access and connect.
5. Return to **数据监控** (Data Monitoring) to view the data.

No server port, command-line options, or additional fields are specified in the Word file.

## Verify data and handle problems

A network connection alone does not prove that live device data is arriving. Check the returned status and that the data index continues to advance. Sensor values may remain steady while the device is stationary; a persistently unchanged index requires investigation.

- No data: check successful wear detection, the approved compute-box/Ascentiz-H connection, and the selected network address.
- Wrong address after switching networks: apply the appropriate laptop script and update the application's connection configuration.
- Import failure: check that execution is on the compute box in the SDK's Python environment.
- Values and index remain frozen: the exhibition guide identifies this as a possible compute-box/G4 communication failure. It states that manually restarting programs over SSH is not an effective remedy for that condition. Ask the device operator to follow the approved stop and power-cycle procedure.

The guide states that the device-communication program, TCP server, and cable-detection program start automatically. The first two are monitored and restart within three seconds after a crash; normally the operator does not launch them manually. Process recovery alone does not prove that device communication has recovered.

Use the demo's documented disconnection/cleanup path when finished. For unresolved problems, collect sanitized version information, timestamps, and errors using [Logs and Feedback](../troubleshooting/logs-and-feedback.md).

## Scope and remaining details

This page is adapted from the supplied exhibition operations guide; the physical equipment and wheel have not been tested here. The actual `demo.py` is needed to add a complete Python calling example, returned-field descriptions, CSV location, and exact cleanup behavior.

See [BodyOS SDK](../sdk/index.md) for SDK organization and [Architecture and Safety Boundary](../sdk/architecture-and-safety-boundary.md) for responsibilities.
