# Development Kit

The Open Unit development kit is the reference environment for building and validating software against the Ascentiz platform.

## Reference Assumptions

The current reference profile assumes:

- an Open Unit compute module in the Raspberry Pi CM5 class
- Linux-based user-space services for orchestration, diagnostics, and application logic
- a device-local interface to the Exoskeleton Unit for commands, state, and telemetry
- lab-friendly access for SSH, log capture, and service restarts

These assumptions may change as product hardware is finalized, but they are a reasonable baseline for early software development.

## Minimum Software Expectations

The Open Unit environment should provide:

- a process supervisor for core platform services
- a transport layer for control and telemetry exchange
- log access for device health and application diagnostics
- a reproducible way to deploy experimental applications

## Recommended Host Tools

For most teams, the following host-side tools are sufficient:

- Python 3.11+
- `ssh` and `rsync` or another deployment mechanism
- `git`
- a serial or network diagnostics workflow appropriate to your device setup

## Bring-Up Checklist

Use this checklist before running an application:

- device boots cleanly
- platform services are healthy
- Exoskeleton Unit is detected
- no active faults are present
- telemetry stream is readable
- session state reports unarmed by default

If any of these checks fail, do not continue to motion-related tests until the fault is understood.

