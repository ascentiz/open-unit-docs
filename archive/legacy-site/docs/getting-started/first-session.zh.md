# 首次会话

本教程展示与 Open Unit 设备进行最小化首次交互的流程。目标是检查状态、确认平台边界并验证基本命令路径，不假定 SDK 已经定型。

## 1. 连接设备

```bash
ssh developer@open-unit.local
```

确认核心服务运行正常：

```bash
systemctl --type=service --state=running
```

## 2. 检查平台状态

执行任何控制操作之前，请确认设备报告：

- Exoskeleton Unit 已连接
- 固件版本已知
- 不存在活动安全故障
- 会话状态明确，例如 `idle` 或 `unarmed`

占位响应示例：

```json
{
  "device_id": "ou-dev-001",
  "exo_link": "online",
  "session_state": "unarmed",
  "faults": [],
  "firmware": {
    "exoskeleton_unit": "0.4.2",
    "open_unit_platform": "0.3.0"
  }
}
```

## 3. 启动只读遥测会话

在任何命令流程之前，先使用只读遥测路径：

```python
from ascentiz.telemetry import TelemetryClient

client = TelemetryClient("open-unit.local")

for sample in client.stream(topic="joint_state", rate_hz=50):
    print(sample.timestamp, sample.knee.position_rad, sample.knee.torque_nm)
```

最终软件包结构可能变化，但使用模式应保持一致：先观察状态，再发送命令。

## 4. 请求受安全门控约束的命令会话

系统健康时，请求一个具有明确状态转换的控制会话：

```python
from ascentiz.control import ControlClient

control = ControlClient("open-unit.local")

session = control.open_session(mode="developer")
session.arm()
session.set_joint_torque_limit("knee", 8.0)
session.disarm()
```

## 5. 验证结束行为

会话结束时：

- 解除命令权限
- 确认 Exoskeleton Unit 报告安全的空闲状态
- 如发生异常，采集日志供后续检查

## 本示例的关键点

- Open Unit 不直接替代安全层
- 状态检查先于命令发送
- 命令权限必须明确、有界且可撤销
