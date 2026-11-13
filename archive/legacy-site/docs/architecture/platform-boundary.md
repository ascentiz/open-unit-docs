# Platform Boundary

The boundary between the Exoskeleton Unit and Open Unit is a control contract, not just a wiring diagram.

## Exoskeleton Unit

The Exoskeleton Unit is responsible for the behaviors that must remain deterministic and device-local:

- actuator drive and timing-critical control loops
- device state transitions required for safe operation
- enforcement of joint, current, torque, temperature, and communication limits
- watchdog behavior when upstream software stalls or disconnects

In short, the Exoskeleton Unit is where the system protects the user and the hardware.

## Open Unit

The Open Unit is responsible for the behaviors that benefit from a more flexible compute environment:

- higher-level control strategies
- intent estimation and sensor fusion
- experiment protocols and application logic
- telemetry aggregation, storage, and forwarding
- developer tools, remote operations, and integration services

This makes the Open Unit the right place for researchers and partners to build, while keeping safety-critical enforcement out of best-effort user-space code.

## Command Flow

A typical command path looks like this:

1. An application on the Open Unit computes a requested action.
2. The request is packaged with session and mode context.
3. The Exoskeleton Unit validates the request against current state and configured limits.
4. The Exoskeleton Unit accepts, modifies, or rejects the request.
5. Telemetry and status feedback return to the Open Unit for logging and adaptation.

## Design Rules

The architecture should preserve these rules over time:

- no application should depend on bypassing the Exoskeleton Unit safety layer
- loss of Open Unit connectivity should degrade to a safe Exoskeleton Unit behavior
- command acceptance should always be state-aware
- fault reporting should be machine-readable and operator-visible

## Integration Implication For Developers

When writing software for Open Unit, assume you are building against an authoritative lower layer. Your code should be prepared for:

- rejected commands
- command clamping
- stale or paused sessions
- temporary sensor unavailability
- explicit disarm or emergency stop transitions

