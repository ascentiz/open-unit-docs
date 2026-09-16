# BodyOS 

**BodyOS** is a Python/C++ SDK for developers working with the Ascentiz exoskeleton platform. It is distributed as a `.whl` package, not as a complete operating system.

It is designed for teams that need a credible path from hardware integration to applied robotics research:

- embedded and controls engineers building device-side applications
- researchers validating sensing, intent estimation, and assistance strategies
- university labs running studies on gait, rehabilitation, and human-machine interaction
- ecosystem partners integrating perception, analytics, or fleet tooling

!!! note "Platform status"
    The current documentation reflects an early-stage developer platform. Interfaces, hardware details, and software contracts should be treated as evolving until versioned release commitments are published.

## Platform At A Glance

The Ascentiz platform is intentionally split into two layers:

| Layer | Responsibility | Change Rate |
| --- | --- | --- |
| Exoskeleton Unit | Real-time actuation, device protection, motor control, and hard safety enforcement | Controlled and conservative |
| Open Unit | Developer applications, higher-level control logic, data processing, experiment tooling, and external integrations | Faster iteration |

This separation lets developers build on the platform without bypassing the device-level safety layer.

## What You Can Expect In These Docs

- a clear boundary between hardware safety functions and application logic
- starter API structure for control, state, and telemetry interfaces
- integration workflows for bring-up, streaming telemetry, and safety-gated commanding
- collaboration guidance for research teams and external contributors

## Documentation Map

- [Getting Started](getting-started/index.md): platform overview, setup, and a first run.
- [Exo Belt Mechanical](mechanical/index.md): structure, assembly, and fit.
- [Hardware: B-core Pi 1](hardware/index.md): hardware architecture, power, connections, and interfaces.
- [BodyOS SDK](sdk/index.md): wheel installation, basic usage, and the architecture and safety boundary.
- [API](api/index.md): detailed interface contracts.
- [Examples](examples/index.md): reading AZ-H exoskeleton status and sensor data in the exhibition setup.
- [Integrations](integrations/index.md): external devices and tools, including a planned ROS 2 guide.
- [Troubleshooting](troubleshooting/index.md): common issues, logs, and feedback.

Hardware specifications, SDK compatibility, and integration support must be confirmed against released materials. Pages marked **To be completed** are authoring scaffolds, not validated procedures.

## Design Principles

1. Safety-critical behavior stays close to the actuator and does not depend on best-effort user code.
2. Developer workflows should be easy to test, inspect, and extend with standard robotics tools.
3. Research integrations should be practical to reproduce across labs and pilot deployments.
4. APIs should be explicit about state, permissions, and failure modes.

## Next Steps

If you are new to the platform, start with [Getting Started](getting-started/index.md). To understand the SDK's responsibilities, read [Architecture and Safety Boundary](sdk/architecture-and-safety-boundary.md).

## Additional Resources

Existing [tutorials](tutorials/index.md), [research collaboration guidance](research/index.md), and [contribution guidelines](community/contributing.md) remain available as supporting resources. They are no longer top-level navigation sections.
