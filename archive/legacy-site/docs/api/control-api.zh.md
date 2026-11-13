# 控制 API

控制接口应使命令权限可见且有明确边界。

## 核心概念

### 会话

客户端在发送命令之前建立会话：

```json
{
  "session_id": "sess_8fd2",
  "mode": "developer",
  "state": "unarmed",
  "lease_ms": 500
}
```

### 使能与解除使能

应用不应假定开启会话就立即获得命令权限。

占位流程示例：

```python
session = control.open_session(mode="developer")
session.arm()
session.command_joint_position("knee", position_rad=0.15)
session.disarm()
```

### 被拒绝的命令

命令拒绝是契约中的正常情况。常见原因包括：

- 会话未使能
- 心跳已过期
- 与执行器限制冲突
- 存在活动故障或急停
- 当前模式不允许请求的动作

## 契约指南

最终控制 API 应：

- 要求每个命令结构使用明确单位
- 将目标请求与测量状态分离
- 返回包含拒绝原因的代码，而不只是通用错误
- 支持仿真及硬件在环流程

## 占位命名空间

在实现确定之前，使用以下概念性命名空间：

- `session.*`
- `control.*`
- `limits.*`
- `faults.*`

## 计划扩展

本页后续可以补充：

- 自动生成的接口参考
- 状态转换图
- 模式表
- 各关节能力矩阵
