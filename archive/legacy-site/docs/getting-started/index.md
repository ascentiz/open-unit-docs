# Getting Started

Start here to understand Exo Belt, B-core Pi 1, and the BodyOS Python SDK, and prepare a first integration safely. BodyOS is distributed as a `.whl` package; it is not an operating system.

## Intended Workflow

Most teams will move through the platform in this order:

1. Bring up an Open Unit development kit.
2. Inspect system state and telemetry without commanding motion.
3. Establish a session with explicit safety state visibility.
4. Issue low-risk commands through a gated control workflow.
5. Move to closed-loop experiments only after validating hardware and software assumptions.

## Before You Begin

Have the following available:

- an Open Unit development target or evaluation kit
- a compatible Exoskeleton Unit running approved firmware
- network or wired debug access to the device
- a host workstation with a Python runtime compatible with the actual SDK wheel; supported versions are still to be confirmed
- an understanding of your lab or organization safety review process

## Documentation In This Section

- [Platform Overview](platform-overview.md) for product roles and capability boundaries
- [Setup and First Run](setup-and-first-run.md) for preparation and validation

The earlier [Development Kit](development-kit.md) and [First Session](first-session.md) pages remain as preliminary background. Their hardware assumptions and SDK calls are not release specifications.

## Early Platform Notes

At this stage, expect a mix of stable concepts and evolving interfaces:

- the architecture boundary is stable and central to the platform design
- exact transport choices, SDK packaging, and deployment tooling may change
- some examples in these docs are contract-focused placeholders rather than final release interfaces
