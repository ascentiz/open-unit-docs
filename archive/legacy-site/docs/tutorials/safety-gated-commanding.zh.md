# 安全门控命令

本教程介绍 Open Unit 应用发送命令的最小模式，同时保持安全边界清晰。

<div class="video-callout">
  <h2>安全门控命令会话视频</h2>
  <p>在发布专门的安全操作演示之前，目前使用现有命令会话录像进行测试嵌入。</p>
  <div class="video-callout__meta">
    <span>硬件版本待定</span>
    <span>固件版本待定</span>
    <span>Open Unit 版本待定</span>
  </div>
  <div class="video-embed">
    <iframe
      src="https://www.youtube-nocookie.com/embed/L-O7v6jCUVM"
      title="安全门控命令会话"
      loading="lazy"
      referrerpolicy="strict-origin-when-cross-origin"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen>
    </iframe>
  </div>
  <div class="video-transcript">
    <p><strong>检查重点：</strong>明确开启会话、可见的使能与解除使能转换、有界的命令值，以及测试结束后的安全状态。</p>
    <p><strong>备用说明：</strong>如果视频不可用，请以下方文字检查项与失败情况作为操作依据。</p>
  </div>
</div>

## 目标

开启有明确边界的控制会话，发送简单命令，并验证系统返回安全状态。

## 前置条件

- 设备连接健康
- 不存在活动故障
- 遥测可用
- 操作人员已准备好在必要时中断测试

## 流程示例

```python
from ascentiz.control import ControlClient

control = ControlClient("open-unit.local")
session = control.open_session(mode="developer")

assert session.state == "unarmed"

session.arm()
session.command_joint_position("knee", position_rad=0.10, duration_ms=250)
session.disarm()
```

## 检查内容

在命令序列执行期间及结束后，确认：

- 会话状态变化已记录到日志
- 命令值保持在预期限制内
- 遥测能够确认实测行为
- 会话返回 `unarmed` 或 `idle`

## 预期失败情况

以下情况下，平台应可以拒绝或修改命令：

- 请求的运动与已配置限制冲突
- 设备处于错误的运行模式
- 会话心跳已过期
- 命令执行窗口内出现故障

## 停止条件

- 如果观察到的运动与请求的有界命令不一致，立即解除使能
- 如果命令执行窗口内遥测停止更新，停止测试
- 如果出现任何故障，或运行模式不明确，结束会话

## 为什么重要

成功标准不只是“关节动了”，而是命令通过明确、可观测且可撤销的流程执行。
