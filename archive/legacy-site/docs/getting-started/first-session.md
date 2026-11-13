# First Session

This walkthrough shows a minimal first interaction with an Open Unit target. The goal is to inspect state, confirm the platform boundary, and exercise a basic command path without assuming a finalized SDK.

## 1. Connect To The Device

```bash
ssh developer@open-unit.local
```

Verify that core services are healthy:

```bash
systemctl --type=service --state=running
```

## 2. Inspect Platform State

Before any control action, confirm that the device reports:

- a connected Exoskeleton Unit
- a known firmware version
- no active safety faults
- an explicit session state such as `idle` or `unarmed`

Example placeholder response:

```json
{
  "device_id": "ou-dev-001",
  "exo_link": "online",
  "session_state": "unarmed",
  "faults": [],
  "firmware": {
    "exoskeleton_unit": "0.4.2",
    "open_unit_platform": "0.3.0"
  }
}
```

## 3. Start A Read-Only Telemetry Session

Use a read-only telemetry path before any commanding workflow:

```python
from ascentiz.telemetry import TelemetryClient

client = TelemetryClient("open-unit.local")

for sample in client.stream(topic="joint_state", rate_hz=50):
    print(sample.timestamp, sample.knee.position_rad, sample.knee.torque_nm)
```

The details of the final package layout may change, but the pattern should remain the same: observe state first, command second.

## 4. Request A Gated Command Session

When the system is healthy, request a control session with explicit state transitions:

```python
from ascentiz.control import ControlClient

control = ControlClient("open-unit.local")

session = control.open_session(mode="developer")
session.arm()
session.set_joint_torque_limit("knee", 8.0)
session.disarm()
```

## 5. Validate Shutdown Behavior

At the end of the session:

- disarm command authority
- confirm the Exoskeleton Unit reports a safe idle state
- capture logs for later review if anything unexpected occurred

## What Matters In This Example

- the Open Unit does not directly replace the safety layer
- state inspection comes before command issuance
- command authority is explicit, bounded, and revocable

