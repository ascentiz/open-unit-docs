# Architecture

The Ascentiz platform is built around a deliberate separation between two layers:

1. **Exoskeleton Unit**: the embedded real-time control and safety layer connected to the actuators and device sensors
2. **Open Unit**: the developer-facing compute layer where applications, research logic, data pipelines, and external integrations run

This is the most important concept in the platform.

## Why The Split Exists

Exoskeleton development often pulls two needs in opposite directions:

- device behavior must be predictable, bounded, and safe
- developer workflows need iteration speed, visibility, and room for experimentation

The Ascentiz architecture addresses this by keeping fast-changing application software separate from the lowest-level enforcement layer.

## Responsibilities By Layer

| Capability | Exoskeleton Unit | Open Unit |
| --- | --- | --- |
| Motor commutation and actuator control loops | Yes | No |
| Safety interlocks and device protection | Yes | No |
| Watchdogs and fault handling | Yes | Assists with reporting only |
| High-level assistance logic | No | Yes |
| Experiment software and custom algorithms | No | Yes |
| Telemetry logging and cloud integration | Limited | Yes |
| Third-party applications | No | Yes |

## Practical Consequences

- the Exoskeleton Unit remains authoritative for safe operating bounds
- the Open Unit can request behavior, but not redefine hard safety policy at runtime
- applications must handle degraded states and rejected commands as normal operating conditions

## Pages In This Section

- [Platform Boundary](platform-boundary.md) explains the control and data contract between the two layers
- [Safety Model](safety-model.md) documents how session state, faults, and command gating are expected to work

