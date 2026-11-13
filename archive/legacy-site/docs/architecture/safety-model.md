# Safety Model

The Open Unit platform is intended to support experimentation without weakening the safety posture of the underlying device.

## Safety Principles

1. The device starts from a non-commanding state.
2. Command authority must be explicitly requested and can be explicitly revoked.
3. Hard limits are enforced by the Exoskeleton Unit, not by application convention alone.
4. Fault handling is part of normal integration behavior, not an exceptional edge case.

## Session State Model

A minimal session lifecycle should look similar to the following:

| State | Meaning |
| --- | --- |
| `idle` | Device is available but no client session is active |
| `unarmed` | Client session exists but motion-producing commands are blocked |
| `armed` | Client may issue commands within approved bounds |
| `fault` | Device detected a condition requiring intervention or reset |
| `estop` | Immediate stop condition requiring explicit recovery workflow |

The exact names may evolve, but the state transitions should remain explicit.

## Expected Guardrails

The platform should provide:

- heartbeat or lease expiry for commanding sessions
- bounded mode switching
- operator-visible fault codes
- auditable logs for session open, arm, disarm, and fault events

## Developer Guidance

Applications running on the Open Unit should:

- treat `armed` as an acquired privilege, not a default
- verify state before every control sequence
- surface rejected commands in logs and operator interfaces
- fail closed when telemetry or session freshness becomes uncertain

## Out Of Scope For Open Unit Applications

The following should not be implemented as application-only safeguards:

- final joint limit enforcement
- over-current shutdown
- emergency stop handling
- timing-critical motor safety behaviors

Those controls belong on the Exoskeleton Unit side of the boundary.

