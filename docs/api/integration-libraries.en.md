# Integration Libraries (Planned)

BodyOS will provide integration libraries to help developers connect third-party sensors and external devices to B-core Pi 1. This page records the planned scope, delivery status, and future documentation entry points.

!!! info "Current Status"
    Integration Libraries are still in the planning stage. Only libraries, devices, and interfaces that have been delivered and explicitly included in the support list are formally supported. The categories on this page do not indicate that the corresponding capabilities are currently available.

## Planned Scope

### Third-Party Sensors

This section may later document:

- Adapter libraries for IMUs, force sensors, pressure sensors, and other devices
- Device discovery, initialization, and connection methods
- Data structures, units, timestamps, and sampling rates
- Data synchronization, caching, and abnormal-state handling
- How to combine external sensor data with BodyOS data streams

### External Devices

This section may later document:

- Adapter libraries for external controllers, acquisition equipment, and interaction devices
- Communication methods, connection procedures, and permission requirements
- Command, status, and event interfaces
- Device disconnection, reconnection, and error handling
- Verified device models and software versions

## Documentation Requirements for Each Integration Library

Every formally delivered integration library must document at least:

1. Supported devices, models, and versions.
2. Runtime environment, dependencies, and installation method.
3. B-core Pi 1 connection and configuration requirements.
4. Initialization, reading, control, and shutdown workflows.
5. APIs, data structures, units, and error behavior.
6. Runnable examples and safety precautions.
7. Known limitations and compatibility scope.

## Delivery Status

| Category | Library or Device | Status | Documentation |
| --- | --- | --- | --- |
| Third-party sensors | Pending development-team confirmation | Planned | To be added |
| External devices | Pending development-team confirmation | Planned | To be added |

## Development Boundary

- Integration libraries run in the user development environment on B-core Pi 1.
- Integration libraries extend third-party sensors or external devices; they do not expose the internal hardware or device drivers of the Exoskeleton Unit.
- Exoskeleton data reading and control continue to use the public BodyOS SDK/API.
- Devices not included in the formal support list must not be described as compatible or ready for direct use.

## Related Pages

- [System Components and Development Boundaries](../product/overview.md)
- [Hardware: B-core Pi 1](../product/b-core-pi-1.md)
- [SDK Developer Guide](README.md)
- [C++ API](C++_API_Reference.md)
- [Python API](Python_API_Reference.md)
