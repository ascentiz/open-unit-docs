# Telemetry API

Telemetry is the primary interface for understanding device state, validating experiments, and debugging integrations.

## Telemetry Categories

The Open Unit should expose machine-readable telemetry for at least:

- joint state
- actuator status
- inertial and auxiliary sensing
- safety and fault state
- session and command metadata
- platform health and resource usage

## Example Stream

```json
{
  "timestamp": "2026-04-17T09:20:31.240Z",
  "topic": "joint_state",
  "sequence": 10428,
  "payload": {
    "knee": {
      "position_rad": 0.18,
      "velocity_rad_s": -0.04,
      "torque_nm": 5.7,
      "temperature_c": 42.3
    }
  }
}
```

## Design Expectations

Telemetry interfaces should be:

- timestamped at the source when possible
- explicit about units and coordinate frames
- robust to dropped samples
- easy to consume from Python and other common robotics tooling

## Suggested Topics

| Topic | Purpose |
| --- | --- |
| `joint_state` | Position, velocity, torque, and thermal state |
| `imu` | Body or segment motion data |
| `session_state` | Current command authority and lease status |
| `fault_state` | Active faults and recovery status |
| `system_health` | CPU, memory, storage, transport, and process health |

## Planned Expansion

Later revisions can add:

- retention and replay guidance
- schema definitions
- topic-level quality-of-service recommendations
- example collectors for cloud or lab data pipelines

