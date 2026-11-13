# 启动检查流程

本教程介绍 Open Unit 连接 Exoskeleton Unit 后，首日启动检查的建议顺序。

<div class="video-callout">
  <h2>启动检查演示视频</h2>
  <p>正式教程视频仍在准备中，目前使用有人监督的启动检查录像进行测试嵌入。</p>
  <div class="video-callout__meta">
    <span>硬件版本待定</span>
    <span>固件版本待定</span>
    <span>Open Unit 版本待定</span>
  </div>
  <div class="video-embed">
    <iframe
      src="https://www.youtube-nocookie.com/embed/L-O7v6jCUVM"
      title="启动检查演示"
      loading="lazy"
      referrerpolicy="strict-origin-when-cross-origin"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen>
    </iframe>
  </div>
  <div class="video-transcript">
    <p><strong>检查重点：</strong>在任何控制测试之前，确认启动健康状态、设备连接就绪、遥测新鲜度，以及明确的未使能会话状态。</p>
    <p><strong>备用说明：</strong>如果视频尚不可用，请以下方文字步骤作为操作依据。</p>
  </div>
</div>

## 目标

在运行可能请求驱动动作的应用逻辑之前，确认平台状态足以支持低风险开发工作。

## 前置条件

- 可实际接触硬件，或处于有人监督的实验室环境
- 可通过 SSH 或串口访问 Open Unit
- Exoskeleton Unit 的供电与通信路径已确认正常

## 操作步骤

### 1. 启动并检查

确认 Open Unit 正常启动，核心服务成功运行：

```bash
journalctl -u ascentiz-platform --since "10 minutes ago"
```

### 2. 验证设备连接

检查 Exoskeleton Unit 连接存在且未降级：

```bash
ascentiz-cli device status
```

预期结果：

- 设备连接在线
- 不存在活动安全故障
- 会话处于未使能状态

### 3. 读取遥测

订阅已知遥测主题并验证样本新鲜度：

```bash
ascentiz-cli telemetry stream joint_state --rate 20
```

### 4. 记录基线元数据

任何控制测试之前，记录：

- Open Unit 软件版本
- Exoskeleton Unit 固件版本
- 设备标识符
- 时间戳及操作人员

### 5. 出现不明确情况时停止

如果状态不清楚、故障报告缺失或遥测不符合预期，请暂停并解决平台问题后再继续。

## 操作人员注意事项

- 在现场监督下执行流程
- 进入命令测试前，记录软件、固件及硬件版本
- 如任何状态转换不明确，或遥测疑似过期，立即停止

## 成功标准

完成以上检查后，应具备开始低风险应用测试，或进入[安全门控命令](safety-gated-commanding.md)教程所需的基础条件。
