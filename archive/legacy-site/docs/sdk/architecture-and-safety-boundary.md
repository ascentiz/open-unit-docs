# Architecture and Safety Boundary

BodyOS is a developer-facing SDK. Installing or calling it does not replace the device-side safety controller or grant unrestricted actuator access.

## Responsibility boundary

- SDK: developer-facing connection, data access, and supported bounded command requests; exact modules await release documentation.
- Device-side control: retains final command acceptance and safety enforcement as described in the existing platform model.
- Application: must respect authorization, operating limits, telemetry freshness, and fault handling.

Do not treat SDK checks as a substitute for device-side safeguards. Document actual rejection behavior, timeout/disconnection behavior, and the approved stop procedure before publishing control examples.

Existing background: [Platform Boundary](../architecture/platform-boundary.md) and [Safety Model](../architecture/safety-model.md). These are conceptual references, not certification claims.
