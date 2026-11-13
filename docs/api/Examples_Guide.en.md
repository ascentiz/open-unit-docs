# Official Example Guide

[← Back to the BodyOS SDK Developer Guide](./README.md)

This guide explains the four official demos under `bin/` (C++) and `python/`, helping you quickly understand BodyOS SDK best practices and safety mechanisms.

> **📌 General notes**:
>
> - Compiled C++ examples are output to the `bin/` directory.
> - All Python examples depend on the `bodyos` package under `python/bodyos`. Run them from the `python` directory or add the package to `PYTHONPATH`.
> - Before running any control demo, such as assist or motor control, make sure the underlying physical hardware—including the CM5, CAN bus, and control board—is powered on and communicating normally.

---

## 1. `sensor_read_record` (Sensor Reading and Asynchronous Recording)

**Purpose**: Demonstrates how to request read-only `DATA_COLLECT` mode, retrieve sensor data at high frequency, and use a background thread to write compressed `.csv.gz` files. This example is suitable for data collection and offline algorithm analysis.

### Run

```bash
# C++ version
./bin/sensor_read_record -t 10 -i 100

# Python version
python3 sensor_read_record.py -t 10 -i 100
```

- `-t 10`: Exit automatically after 10 seconds.
- `-i 100`: Record at 100 ms intervals. Internally, `seq` is used to prevent the same frame from being written repeatedly.

### Core Logic and Safety Mechanisms

1. **Mode request**: The program first requests `DATA_COLLECT`. This is a **read-only mode** in which the lower layer forcibly rejects all motor-enable commands to keep the hardware safe.
2. **Data deduplication**: The main loop polls every 1 ms, but data is considered new only when `sensors.seq` changes. This prevents the 100 Hz hardware stream from being recorded more than once per frame.
3. **Asynchronous disk writes**: `client.record_sensors(sensors)` only places data into an in-memory queue and returns in microseconds. Disk I/O and Gzip compression run in a background thread, so the acquisition loop is never stalled.
4. **Graceful exit**: The Python version briefly calls `sleep(500ms)` during shutdown, giving the background Gzip thread time to complete the final `.csv` to `.csv.gz` conversion.

---

## 2. `body_assist_control` (BLE Assist-Mode Control)

**Purpose**: Controls the BLE controller's assist mode (EASE / ACC / TRAIN), movement scenario, and assist level. This is one of the most frequently used interaction features.

### Run

```bash
# C++ version: switch to EASE mode, scenario 2, assist level 50%
./bin/body_assist_control -m 0 -s 2 -l 50

# Python version
python3 body_assist_control.py -m 0 -s 2 -l 50
```

- `-m` (`mode`): `0` = EASE, `1` = ACC, `2` = TRAIN
- `-s` (`scene`): Scenario index; valid ranges depend on the selected mode. Use `-h` or `--help` for details.
- `-l` (`level`): Assist level from `0` to `100%`.
- `-p` (`pause`): `0` = run, `1` = pause.
- `-r` (`read`): Read the current status and exit without writing changes.

### Core Logic and Safety Mechanisms

1. **Control ownership**: After startup, the program checks `gait_mode`. If the value is not `0`, meaning the lower layer is not controlled by the compute unit, the program switches modes and **reads the value back for verification** before continuing.
2. **Incremental update**: The program uses `update_ble_assist`. The SDK first obtains the current heartbeat through the background stream as a baseline, then **overwrites only the supplied `-m/-s/-l` parameters**. Other parameters, such as automatic-recognition switches and other scenario fields, retain their original values and are not accidentally cleared.
3. **Parameter validation**: Before sending a command to the daemon, the SDK rejects an invalid scenario value, such as scenario 5 in TRAIN mode, or an assist level above 100%.

---

## 3. `body_expert_control` (Expert-Parameter Adjustment)

**Purpose**: Fine-tunes physical parameters in the assist algorithm, such as smoothness, base assistance, cadence, and response level. This example is intended for advanced debugging personnel.

### Run

```bash
# C++ version
./bin/body_expert_control --smooth 50 --base 10

# Python version
python3 body_expert_control.py --smooth 50 --base 10
```

- `-r` (`read`): Read and print the complete expert-parameter set from the cache.
- `--mode`, `--smooth`, `--base`, `--speed`, `--freq`, `--resp`, `--coeff`: Modify the corresponding physical parameters.

### Core Logic and Safety Mechanisms

1. **Silent synchronization**: Expert mode includes more than ten parameters across Easy and Acc groups. If a user supplies only `--smooth`, sending a new complete structure directly would clear all other fields. On the first call, the SDK's `update_ble_expert` silently executes `BLE_GET_EXPERT` to retrieve and cache the complete device parameter set. It then replaces only the supplied values and sends the merged structure once.
2. **Range checks**: Each parameter has its own permitted range—for example, coefficients use `-20` to `20`, while other parameters use `-200` to `200`. The SDK rejects out-of-range values before transmission.

---

## 4. `direct_motor_control` (Direct Low-Level Motor Control)

**Purpose**: Bypasses all gait algorithms and sends torque, velocity, or position commands directly to the four motor controllers. This example includes software- and hardware-level safety limits and is intended for motor testing or custom algorithm development.

### Run

```bash
# C++ version: torque mode, all four motors, 1.0 Nm output
./bin/direct_motor_control -m 0 -n 0x0F -v 1.0

# Python version
python3 direct_motor_control.py -m 0 -n 0x0F -v 1.0
```

- `-m`: `0` = torque, `1` = velocity, `2` = position.
- `-n`: Node mask; `15` or `0x0F` selects all four motors.
- `-v`: Target value.
- `-r`: Read the current control mode and exit without sending control commands.

### Core Logic and Safety Mechanisms

1. **Forced control takeover**: The program first requests `USER_CONTROL` mode, then calls `set_gait_mode(1)` to take control away from the lower-level algorithm. It continues only after **reading the setting back to verify** that control ownership is correct.
2. **Physical safety limits**: Before a value is passed to the SDK, the example enforces the safety ranges—torque ±2.0 Nm, velocity ±40 revolutions per second, and position ±32 revolutions—and reports the applied limit in the terminal.
3. **Non-blocking shutdown (critical)**:
    - **C++**: On exit, the example calls `send_raw` to transmit the stop command one-way. It does not wait for an ACK and therefore cannot block during shutdown.
    - **Python**: The control loop runs in a background thread. When the user presses `Ctrl+C`, the main thread sets `g_running` to `False`. In the `finally` block, it bypasses the regular wrapper, writes zero-velocity and disable commands directly to the socket with `wait_reply=False`, and applies a 0.2-second socket timeout. Even if the CAN bus is physically blocked, Python can disconnect and exit without hanging.
