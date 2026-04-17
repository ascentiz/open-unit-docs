# Getting Started

This section helps new developers understand what the Open Unit is, what is expected from a development environment, and how to approach a first integration safely.

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
- a host workstation with Python 3.11+ or another supported runtime
- an understanding of your lab or organization safety review process

## Documentation In This Section

- [Development Kit](development-kit.md) for hardware and software prerequisites
- [First Session](first-session.md) for a minimal inspection and command workflow

## Early Platform Notes

At this stage, expect a mix of stable concepts and evolving interfaces:

- the architecture boundary is stable and central to the platform design
- exact transport choices, SDK packaging, and deployment tooling may change
- some examples in these docs are contract-focused placeholders rather than final release interfaces

