# Safety-Gated Commanding

This tutorial describes a minimal pattern for sending commands from an Open Unit application without blurring the safety boundary.

## Goal

Open a bounded control session, issue a simple command, and verify that the system returns to a safe state.

## Preconditions

- device link is healthy
- no active faults are present
- telemetry is available
- operator is prepared to interrupt the test if needed

## Example Flow

```python
from ascentiz.control import ControlClient

control = ControlClient("open-unit.local")
session = control.open_session(mode="developer")

assert session.state == "unarmed"

session.arm()
session.command_joint_position("knee", position_rad=0.10, duration_ms=250)
session.disarm()
```

## What To Check

During and after the command sequence, verify:

- session state changes are logged
- command values remain within expected limits
- telemetry confirms measured behavior
- the session returns to `unarmed` or `idle`

## Failure Cases To Expect

The platform should be allowed to reject or modify commands when:

- the requested motion conflicts with configured limits
- the device is in the wrong operating mode
- the session heartbeat is stale
- a fault becomes active during the command window

## Why This Matters

The success condition is not just "the joint moved." The real success condition is that commanding happened through an explicit, observable, and revocable workflow.

