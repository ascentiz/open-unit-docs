# Platform Overview

This documentation covers the physical device, its hardware, and the developer-facing software toolkit.

| Component | Documentation scope |
| --- | --- |
| Exo Belt | Mechanical structure, assembly, and fit |
| B-core Pi 1 | Hardware architecture, power, connections, and board interfaces |
| BodyOS SDK | A Python SDK distributed as a `.whl` package |
| Exoskeleton Unit | Device-local actuation and final safety enforcement |

BodyOS is not a complete operating system. Installing its wheel installs a Python package, not a device image or firmware.

## Where to Go Next

- Prepare a [first run](setup-and-first-run.md).
- Read [SDK installation and configuration](../sdk/installation-and-configuration.md).
- Understand the [architecture and safety boundary](../sdk/architecture-and-safety-boundary.md).

!!! note "Early platform"
    The SDK package name, supported runtime, device compatibility, and final APIs must be documented from the actual release. Existing code examples remain conceptual until verified.
