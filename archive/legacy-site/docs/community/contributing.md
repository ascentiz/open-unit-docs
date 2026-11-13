# Contributing

This project is intended to be easy to extend as the platform matures.

## Contribution Workflow

1. Open or review an issue describing the change.
2. Create a short-lived branch for the update.
3. Keep changes narrowly scoped and technically explicit.
4. Run a local documentation build before opening a pull request.
5. Request review from the relevant platform owner when the change touches architecture, safety, or API behavior.

## Documentation Standards

When contributing to the docs:

- prefer precise technical language over promotional language
- call out assumptions when interfaces are not finalized
- include units, states, and failure behavior where relevant
- keep examples small enough to review quickly

## Pull Request Checklist

Before submitting:

- pages build successfully with `mkdocs build --strict`
- navigation is updated if a new page is added
- links resolve correctly
- placeholder material is clearly labeled as such

## High-Sensitivity Changes

Changes affecting the following areas should receive extra review:

- safety behavior
- state machines
- control authority
- device limits
- research guidance that could influence study execution

