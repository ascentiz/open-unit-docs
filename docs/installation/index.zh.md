# Installation

本页用于发布和下载 BodyOS SDK 软件包。每个正式版本将提供版本号、适用平台、文件大小、SHA-256 校验值和安装说明。

!!! info "当前状态"
    SDK 压缩包尚未发布。文件经过版本确认和安全检查后，下载入口将在本页启用。

## SDK 下载

| 版本 | 适用平台 | 软件包 | 大小 | SHA-256 |
| --- | --- | --- | --- | --- |
| 待发布 | 待确认 | 暂无下载 | — | — |

## 下载后校验

正式软件包发布时，本页会同时给出 SHA-256。下载后可在 macOS 或 Linux 中执行：

```bash
shasum -a 256 <下载的文件名>.gz
```

命令输出必须与本页公布的 SHA-256 完全一致。若不一致，请勿解压或安装。

## 解压方式

具体命令取决于交付文件的实际格式：

=== "`.tar.gz` 软件包"

    ```bash
    tar -xzf <软件包名称>.tar.gz
    ```

=== "单文件 `.gz`"

    ```bash
    gzip -dk <文件名称>.gz
    ```

如果解压后得到 Python `.whl` 文件，可通过以下方式安装：

```bash
python3 -m pip install ./<软件包名称>.whl
```

!!! note "安装参数待确认"
    正式文件名、版本、支持的平台、Python 版本、依赖和最终安装命令以开发团队交付的软件包为准。不要根据本页示例猜测实际包名。

## 安装后验证

正式版本发布时，本节将提供：

- 包版本查询命令
- `BodyClient` 导入检查
- 与 `bodyos-daemon` 的连接检查
- 支持的平台与 Python 版本矩阵
- 升级、降级和卸载方法

## 继续阅读

- [硬件：B-core Pi 1](../product/b-core-pi-1.md)
- [SDK 开发者手册](../api/README.md)
- [Python API](../api/Python_API_Reference.md)
- [官方示例](../api/Examples_Guide.md)
