# Control API

The control surface should make command authority visible and bounded.

## Core Concepts

### Session

A client establishes a session before sending commands:

```json
{
  "session_id": "sess_8fd2",
  "mode": "developer",
  "state": "unarmed",
  "lease_ms": 500
}
```

### Arm And Disarm

Applications should not assume that opening a session grants immediate command authority.

Example placeholder flow:

```python
session = control.open_session(mode="developer")
session.arm()
session.command_joint_position("knee", position_rad=0.15)
session.disarm()
```

### Rejected Commands

A rejected command is a normal part of the contract. Common reasons include:

- session not armed
- heartbeat expired
- actuator limit conflict
- active fault or emergency stop
- invalid mode for requested action

## Contract Guidelines

The final control API should:

- require explicit units in every command structure
- separate target requests from measured state
- return reasoned rejection codes, not just generic errors
- support simulation and hardware-in-the-loop workflows

## Placeholder Namespaces

Until the implementation is fixed, use these conceptual namespaces:

- `session.*`
- `control.*`
- `limits.*`
- `faults.*`

## Planned Expansion

This page is ready to absorb:

- generated reference docs
- state transition diagrams
- mode tables
- per-joint capability matrices

