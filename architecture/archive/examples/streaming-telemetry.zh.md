# 遥测数据流

本示例展示一个订阅遥测并打印结构化样本的小型 Python 应用，便于后续处理。

## 使用场景

以下需求可采用此模式：

- 设备启动检查期间的实时调试视图
- 将实验日志记录到 CSV、Parquet 或数据库
- 简单地桥接到可视化工具

## 示例

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

## 注意事项

- 本示例为只读模式，适合早期集成工作
- 下游日志应保留时间戳及设备标识符
- 最终实现可能支持更多传输方式或结构定义
