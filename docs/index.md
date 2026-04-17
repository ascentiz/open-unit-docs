# Ascentiz Open Unit

**Ascentiz Open Unit** is the developer-facing compute and control layer for the Ascentiz modular exoskeleton platform.

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

- **Getting Started** explains the development kit mindset, prerequisites, and a first device session.
- **Architecture** describes how the Exoskeleton Unit and Open Unit interact and where authority is enforced.
- **API** outlines the current control and telemetry surface and how it is expected to evolve.
- **Tutorials** walks through end-to-end setup and safe command workflows.
- **Examples** shows realistic reference applications and integration patterns.
- **Research** documents how university labs can collaborate with Ascentiz.
- **Community** explains contribution, feedback, and support expectations.

## Design Principles

1. Safety-critical behavior stays close to the actuator and does not depend on best-effort user code.
2. Developer workflows should be easy to test, inspect, and extend with standard robotics tools.
3. Research integrations should be practical to reproduce across labs and pilot deployments.
4. APIs should be explicit about state, permissions, and failure modes.

## Next Steps

If you are new to the platform, start with [Getting Started](getting-started/index.md). If you need the system boundary first, go directly to [Architecture](architecture/index.md).

