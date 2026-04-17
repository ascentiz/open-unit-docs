# Bring-Up Workflow

This tutorial walks through a sensible first-day bring-up sequence for an Open Unit target connected to an Exoskeleton Unit.

## Goal

Confirm that the platform is healthy enough for non-risky developer work before running any application logic that could request actuation.

## Prerequisites

- physical access to the hardware or a supervised lab setup
- SSH or serial access to the Open Unit
- a known-good power and communication path to the Exoskeleton Unit

## Procedure

### 1. Boot And Inspect

Confirm the Open Unit boots and core services start successfully:

```bash
journalctl -u ascentiz-platform --since "10 minutes ago"
```

### 2. Verify Device Link

Check that the Exoskeleton Unit link is present and not degraded:

```bash
ascentiz-cli device status
```

Expected high-level outcome:

- device link online
- no active safety faults
- session state unarmed

### 3. Read Telemetry

Subscribe to a known telemetry topic and verify sample freshness:

```bash
ascentiz-cli telemetry stream joint_state --rate 20
```

### 4. Record Baseline Metadata

Capture the following before any control tests:

- Open Unit software version
- Exoskeleton Unit firmware version
- device identifier
- timestamp and operator

### 5. Stop If Anything Looks Ambiguous

If state is unclear, fault reporting is missing, or telemetry does not match expectations, pause and resolve the platform issue before moving on.

## Success Criteria

You should now have enough confidence to begin low-risk application testing or move to the [Safety-Gated Commanding](safety-gated-commanding.md) tutorial.

