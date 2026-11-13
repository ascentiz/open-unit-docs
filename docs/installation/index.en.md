# Installation

This page is the download and release entry point for BodyOS SDK packages. Each official release will include a version number, supported platform, file size, SHA-256 checksum, and installation instructions.

!!! info "Current Status"
    No SDK archive has been published yet. The download entry will be enabled after the package version is confirmed and the file passes the required safety checks.

## SDK Downloads

| Version | Platform | Package | Size | SHA-256 |
| --- | --- | --- | --- | --- |
| Pending | To be confirmed | No download available | — | — |

## Verify the Download

Every official package will be published with a SHA-256 checksum. After downloading it, run the following command on macOS or Linux:

```bash
shasum -a 256 <downloaded-file>.gz
```

The result must exactly match the SHA-256 value published on this page. Do not extract or install a package if the values differ.

## Extract the Package

The command depends on the delivered file format:

=== "`.tar.gz` package"

    ```bash
    tar -xzf <package-name>.tar.gz
    ```

=== "Single `.gz` file"

    ```bash
    gzip -dk <file-name>.gz
    ```

If extraction produces a Python `.whl` file, install it with:

```bash
python3 -m pip install ./<package-name>.whl
```

!!! note "Installation Details Pending"
    The final file name, version, supported platforms, Python versions, dependencies, and installation command depend on the package delivered by the development team. Do not infer the actual package name from the examples on this page.

## Verify the Installation

When the first official package is released, this section will provide:

- A package-version command
- A `BodyClient` import check
- A connection check for `bodyos-daemon`
- A supported platform and Python version matrix
- Upgrade, downgrade, and uninstall procedures

## Continue Reading

- [Hardware: B-core Pi 1](../product/b-core-pi-1.md)
- [SDK Developer Guide](../api/README.md)
- [Python API](../api/Python_API_Reference.md)
- [Official Examples](../api/Examples_Guide.md)
