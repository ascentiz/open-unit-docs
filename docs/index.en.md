# BodyOS Developer Documentation

This site describes the components, developer access boundaries, and SDK interfaces of the BodyOS exoskeleton development system. The system consists of four parts: Exo Belt, B-core Pi 1, BodyOS SDK, and the encapsulated Exoskeleton Unit.

!!! warning "Safety Notice"
    Before running any control example, verify the device status, communication link, and emergency-stop measures. Only personnel familiar with the device may operate it under an approved procedure. `direct_motor_control` sends commands directly to the motors and must be used with particular caution.

## Documentation Map

### [System Components and Development Boundaries](product/overview.md)

Start with the relationships among the four system components and the mechanical, hardware, and software boundaries available to developers. The internal hardware and drivers of the Exoskeleton Unit are encapsulated. Developers use the BodyOS SDK/API on B-core Pi 1 to obtain data and send control requests.

### [Mechanical Structure: Exo Belt](product/exo-belt.md)

Review the documentation framework for the mechanical structure, assembly, and fitting of Exo Belt. Dimensions, materials, loads, and assembly procedures will be added after confirmation by the responsible teams.

### [Hardware: B-core Pi 1](product/b-core-pi-1.md)

Review the system role and development workflow of B-core Pi 1, together with the documentation framework for its hardware architecture, power supply, connections, and board interfaces.

### BodyOS SDK

- [SDK Developer Guide](api/README.md): Learn the `bodyos-daemon + dual client socket` architecture, core capabilities, deployment, quick integration, and troubleshooting guidance.
- **API Reference**
    - [C++ API](api/C++_API_Reference.md): Review the lifecycle, control, sensor, configuration, BLE, alarm, and recording interfaces of `BodyClient`.
    - [Python API](api/Python_API_Reference.md): Review the Python client's work modes, control, sensor, configuration, BLE, alarm, and recording interfaces.
- [Integration Libraries (Planned)](api/integration-libraries.md): Future libraries and adapters for integrating third-party sensors and external devices.

### [Official Examples](api/Examples_Guide.md)

Explore four official examples, each available in C++ and Python:

- `sensor_read_record`: sensor reading and asynchronous recording
- `body_assist_control`: BLE assist-mode control
- `body_expert_control`: expert parameter adjustment
- `direct_motor_control`: direct low-level motor control

## Recommended Reading Order

1. Read [System Components and Development Boundaries](product/overview.md) to understand the accessible scope.
2. Review the [Exo Belt](product/exo-belt.md) and [B-core Pi 1](product/b-core-pi-1.md) framework pages as needed.
3. Read the [SDK Developer Guide](api/README.md) to understand the runtime architecture and complete deployment.
4. Under **API Reference**, choose the [C++ API](api/C++_API_Reference.md) or [Python API](api/Python_API_Reference.md) for your project language.
5. When integrating third-party sensors or devices, check the delivery status under [Integration Libraries](api/integration-libraries.md).
6. Finish with the [Official Examples](api/Examples_Guide.md) to build your first working program.

## Current Documentation Scope

The formal technical content for BodyOS SDK is based on four Chinese Markdown documents supplied by the development team. The Exo Belt and B-core Pi 1 pages currently publish only the confirmed system positioning and documentation framework. Unknown mechanical parameters, hardware specifications, pin definitions, and connection methods are marked as pending confirmation and are not inferred from legacy materials.
