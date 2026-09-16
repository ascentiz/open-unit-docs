# Setup and First Run

!!! warning "To be completed"
    The actual SDK wheel and validated connection instructions have not been supplied. This page defines the onboarding sequence, not a ready-to-run hardware procedure.

## Preparation

1. Confirm the device revision and applicable [assembly and fit](../mechanical/assembly-and-fit.md) instructions.
2. Follow the approved [power and connection](../hardware/power-and-connection.md) procedure.
3. Obtain the release wheel and check its Python and platform compatibility in [SDK installation](../sdk/installation-and-configuration.md).
4. Follow [basic usage](../sdk/basic-usage.md) to import the actual package, connect, and inspect device state.
5. Read telemetry before attempting a bounded command. Never bypass the [safety boundary](../sdk/architecture-and-safety-boundary.md).

## First-Run Acceptance

- Record the hardware, firmware, SDK, and Python versions.
- Verify the package imports and the intended device is identified.
- Verify state and fresh telemetry are readable without requesting motion.
- Close the connection and confirm a safe terminal state.

Add the verified commands, expected output, and failure handling here once a release is available. The older [First Session](first-session.md) is a conceptual reference, not a validated SDK test.
