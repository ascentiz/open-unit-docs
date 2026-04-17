# Assistive Gait Loop

This example describes the shape of a higher-level assistance application running on the Open Unit.

## Intent

The Open Unit can host logic such as phase estimation, adaptive parameter selection, or experiment orchestration. It should not own final low-level safety enforcement.

## Example Structure

```python
while app.running:
    state = telemetry.read_latest()
    phase = estimator.update(state)
    target = controller.compute(phase, state)

    if session.is_armed() and target.is_valid():
        control.send_assist_command(target)
```

## What Stays On Open Unit

- phase estimation
- experiment logic
- adaptive policy updates
- operator UX and study instrumentation

## What Stays On Exoskeleton Unit

- final actuator enforcement
- hard limits
- safety shutdown behavior
- watchdog-triggered fallback behavior

## Why This Example Matters

It illustrates the core architectural promise of the platform: developers can build meaningful control applications without collapsing the separation between experimentation and safety enforcement.

