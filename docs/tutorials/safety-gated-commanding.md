# Safety-Gated Commanding

This tutorial describes a minimal pattern for sending commands from an Open Unit application without blurring the safety boundary.

<div class="video-callout">
  <h2>Safety-Gated Command Session Video</h2>
  <p>Test embed using the current command session recording until a task-specific safety walkthrough is published.</p>
  <div class="video-callout__meta">
    <span>Hardware Tbd</span>
    <span>Firmware Tbd</span>
    <span>Open Unit Tbd</span>
  </div>
  <div class="video-embed">
    <iframe
      src="https://www.youtube-nocookie.com/embed/L-O7v6jCUVM"
      title="Safety-Gated Command Session"
      loading="lazy"
      referrerpolicy="strict-origin-when-cross-origin"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen>
    </iframe>
  </div>
  <div class="video-transcript">
    <p><strong>What to verify:</strong> explicit session opening, visible arm and disarm transitions, bounded command values, and a safe terminal state after the test.</p>
    <p><strong>Fallback:</strong> if the video is unavailable, treat the written checks and failure cases below as the source of truth.</p>
  </div>
</div>

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

## Stop Conditions

- disarm immediately if observed motion differs from the requested bounded command
- stop the test if telemetry stops updating during the command window
- end the session if any fault becomes active or the operating mode is ambiguous

## Why This Matters

The success condition is not just "the joint moved." The real success condition is that commanding happened through an explicit, observable, and revocable workflow.
