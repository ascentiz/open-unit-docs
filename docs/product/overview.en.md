# System Components and Development Boundaries

The BodyOS development system consists of four parts: Exo Belt, B-core Pi 1, BodyOS SDK, and the Exoskeleton Unit. Developers can access and use B-core Pi 1 and the public SDK/API. The internal hardware, device drivers, and execution logic of the Exoskeleton Unit remain encapsulated.

## Four System Components

| Component | Role | Current Documentation Scope |
| --- | --- | --- |
| Exo Belt | Exoskeleton belt and load-bearing mechanical structure | Mechanical structure, assembly, fitting, and load boundaries; detailed parameters are pending |
| B-core Pi 1 | Developer-accessible computing and control entry point | Hardware architecture, power supply, connections, and board interfaces; detailed parameters are pending |
| BodyOS SDK | Developer access layer | SDK architecture, C++/Python APIs, and official examples; the Python SDK will be distributed as a `.whl` package |
| Exoskeleton Unit | Encapsulated device execution unit | Internal hardware and device drivers are not exposed to users; the unit performs local device driving and enforces final safety constraints |

## Developer Access Path

```text
Developer application
    │
    │  Runs on B-core Pi 1
    ▼
BodyOS SDK / Public API
    │
    │  Read status and sensor data / Send control requests
    ▼
Exoskeleton Unit (encapsulated)
    │
    └── Internal hardware, device drivers, and final execution logic are not exposed
```

The standard development path is to deploy and run an application on B-core Pi 1, then call the public API through BodyOS SDK to obtain data from the Exoskeleton Unit or send control requests to it. Developers neither need nor have direct access to the internal drivers or hardware implementation of the Exoskeleton Unit.

## What Developers Can Do

- Install and run supported SDKs and applications on B-core Pi 1.
- Obtain status and sensor data provided by the Exoskeleton Unit through the public API.
- Send control requests within the constraints of the public API, safety modes, and supported parameter ranges.
- Build custom application logic using the C++ API, Python API, and official examples.

## Encapsulation Boundary

- The internal hardware architecture of the Exoskeleton Unit is not a user development interface.
- Device drivers, firmware implementation, and internal communication details of the Exoskeleton Unit are not exposed to users.
- Users must not bypass BodyOS SDK/API to control the encapsulated unit directly.
- Whether a control request is executed, and which final safety constraints apply during execution, are jointly governed by the encapsulated unit and the published software interfaces.

!!! note "Documentation Status"
    This page defines the product components and development boundaries. Mechanical dimensions, electrical specifications, interface definitions, and the support matrix will be added after confirmation by the development team. Unconfirmed information will not be published as a formal specification.

## Continue Reading

- [Mechanical Structure: Exo Belt](exo-belt.md)
- [Hardware: B-core Pi 1](b-core-pi-1.md)
- [SDK Developer Guide](../api/README.md)
