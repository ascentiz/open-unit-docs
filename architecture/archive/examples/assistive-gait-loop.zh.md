# 步态辅助循环

本示例描述运行在 Open Unit 上的高层辅助应用的组织方式。

## 设计意图

Open Unit 可以承载相位估计、自适应参数选择或实验编排等逻辑，但不应负责最终的底层安全约束执行。

## 示例结构

```python
while app.running:
    state = telemetry.read_latest()
    phase = estimator.update(state)
    target = controller.compute(phase, state)

    if session.is_armed() and target.is_valid():
        control.send_assist_command(target)
```

## Open Unit 的职责

- 相位估计
- 实验逻辑
- 自适应策略更新
- 操作人员交互及实验测量工具

## Exoskeleton Unit 的职责

- 最终执行器约束执行
- 硬性限制
- 安全关断行为
- 看门狗触发的回退行为

## 本示例的意义

它展示平台架构的核心目标：开发者可以构建有实际价值的控制应用，同时保持实验逻辑与安全约束执行之间的分离。
