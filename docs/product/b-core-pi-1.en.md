# Hardware: B-core Pi 1

B-core Pi 1 is the developer-accessible computing and control entry point. Developers deploy applications on B-core Pi 1 and use BodyOS SDK/API to obtain data from the Exoskeleton Unit and send control requests.

!!! info "Current Status"
    This page is a hardware documentation framework. Board specifications, power parameters, connector definitions, pin assignments, operating-system versions, and environmental limits require confirmation from the hardware or development team.

## Role in the System

B-core Pi 1 sits between the developer application and the encapsulated Exoskeleton Unit:

```text
Developer application (B-core Pi 1)
        ↕
BodyOS SDK / Public API
        ↕
Exoskeleton Unit (encapsulated)
```

Developers do not directly access the internal drivers of the Exoskeleton Unit. All data reading and control operations must use the published BodyOS SDK/API.

## Development Workflow

1. Power B-core Pi 1 and connect it to the exoskeleton system according to confirmed instructions.
2. Prepare a supported software runtime on B-core Pi 1.
3. Install or deploy BodyOS SDK. The Python SDK will be distributed as a `.whl` file.
4. Run a data-reading or control application.
5. Use the SDK/API to receive data from the Exoskeleton Unit or send control requests within the safety constraints.

## Hardware Architecture

| Pending Item | Required Material | Current Status |
| --- | --- | --- |
| Compute core | Processor, memory, and storage specifications | Pending from the hardware team |
| System architecture diagram | Relationships among major components, buses, and interfaces | Pending |
| Supported environment | Operating system, architecture, and version requirements | Pending development-team confirmation |
| Form factor and mounting | Dimensions, weight, and mounting method | Pending confirmation |
| Environmental conditions | Operating temperature, storage temperature, and protection requirements | Pending confirmation |

## Power Supply

Do not infer wiring requirements or make connections until the following information is confirmed:

- Input voltage and permitted range
- Typical and peak power consumption
- Power connector model and polarity
- Power-on, power-off, and reset sequence
- Overcurrent, reverse-polarity, and abnormal power-loss protection

## Connections and Board Interfaces

The future interface section must include at least:

- External connection to the Exoskeleton Unit
- Mounting and cable relationship with Exo Belt
- Network, debugging, and storage interfaces
- User-accessible board interfaces and their intended uses
- Connector identifiers, orientations, pin assignments, and electrical limits
- Reserved interfaces or interfaces that users must not access

## Software Deployment Entry Points

Installation commands will be based on the software package delivered by the development team. For the current SDK architecture, APIs, and examples, see:

- [SDK Developer Guide](../api/README.md)
- [C++ API](../api/C++_API_Reference.md)
- [Python API](../api/Python_API_Reference.md)
- [Official Examples](../api/Examples_Guide.md)

## Safety and Encapsulation Boundaries

- Use only the power inputs, connectors, and board interfaces explicitly opened by the documentation.
- Do not use unpublished interfaces to bypass BodyOS SDK/API and control the Exoskeleton Unit.
- Do not perform custom wiring or powered debugging until power and pin definitions are confirmed.
- The internal hardware, drivers, and firmware of the Exoskeleton Unit are outside the B-core Pi 1 user-development scope.

## Related Pages

- [System Components and Development Boundaries](overview.md)
- [Mechanical Structure: Exo Belt](exo-belt.md)
