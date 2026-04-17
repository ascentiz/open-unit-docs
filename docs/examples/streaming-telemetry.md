# Streaming Telemetry

This example shows a small Python application that subscribes to telemetry and prints structured samples for downstream processing.

## Use Case

Use this pattern when you need:

- a live debug view during device bring-up
- experiment logging into CSV, Parquet, or a database
- a simple bridge into visualization tools

## Example

```python
from ascentiz.telemetry import TelemetryClient

client = TelemetryClient("open-unit.local")

for sample in client.stream(topic="joint_state", rate_hz=50):
    knee = sample.payload["knee"]
    print(
        sample.timestamp,
        knee["position_rad"],
        knee["velocity_rad_s"],
        knee["torque_nm"],
    )
```

## Notes

- this example is read-only and should be safe for early integration work
- downstream logging should preserve timestamps and device identifiers
- the final implementation may support additional transports or schemas

