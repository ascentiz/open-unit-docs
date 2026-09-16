# 嵌入 YouTube 视频

本指南统一 Ascentiz 文档站第一阶段的 YouTube 视频嵌入方式。

## 何时使用视频

当运动、操作顺序或操作人员判断比静态截图更重要时，使用视频：

- 启动与结束流程
- 有人监督的运动或安全检查
- 线缆布置、夹具安装或机械对齐
- 故障复现与排查
- 涉及多个工具或屏幕的实验流程

不要只依赖视频。每页仍应以文字说明关键步骤，确保播放器被阻止或不可用时，流程仍能理解。

## 标准嵌入模式

为每个视频添加简短说明块，记录适用范围、版本及读者应关注的内容。

<div class="video-callout">
  <h2>启动检查演示</h2>
  <p>外部托管的教程或流程视频均可采用此模式。</p>
  <div class="video-callout__meta">
    <span>硬件 v1.2+</span>
    <span>固件 0.9.x</span>
    <span>Open Unit 0.14.x</span>
  </div>
  <div class="video-embed">
    <iframe
      src="https://www.youtube-nocookie.com/embed/VIDEO_ID"
      title="启动检查演示"
      loading="lazy"
      referrerpolicy="strict-origin-when-cross-origin"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen>
    </iframe>
  </div>
  <div class="video-transcript">
    <p><strong>检查重点：</strong>连接健康、无活动故障、遥测新鲜度及最终会话状态。</p>
    <p><strong>备用说明：</strong>如果视频不可用，请继续阅读下方文字步骤。</p>
  </div>
</div>

## 可复制的代码片段

以下 HTML 片段保留英文占位文本，便于直接复用原版模板；发布中文页面时，请翻译标题、版本标签及说明文字。

```html
<div class="video-callout">
  <h2>Video Title</h2>
  <p>One sentence describing the task shown in the video.</p>
  <div class="video-callout__meta">
    <span>Hardware vX.Y</span>
    <span>Firmware X.Y.Z</span>
    <span>Open Unit X.Y.Z</span>
  </div>
  <div class="video-embed">
    <iframe
      src="https://www.youtube-nocookie.com/embed/VIDEO_ID"
      title="Video Title"
      loading="lazy"
      referrerpolicy="strict-origin-when-cross-origin"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen>
    </iframe>
  </div>
  <div class="video-transcript">
    <p><strong>What to verify:</strong> key checks or outcomes.</p>
    <p><strong>Fallback:</strong> note the written section the reader should use if playback fails.</p>
  </div>
</div>
```

## 编写规则

1. 使用 `youtube-nocookie.com` 嵌入地址，而非默认 YouTube 域名。
2. 在视频下方保留文字步骤，不要只在视频中说明操作。
3. 在播放器附近注明适用的硬件、固件及软件版本。
4. 使用以任务为中心的标题，例如“启动检查演示”或“安全门控命令会话”。
5. 即使视频已有口头解释，也应在文字中说明安全边界与停止条件。
6. 如果页面后续需要非 YouTube 镜像以支持区域访问，请在嵌入视频下方添加备用托管地址的普通链接。

## 建议后续应用

- 为[启动检查流程](bring-up-workflow.md)添加正式启动视频
- 为[安全门控命令](safety-gated-commanding.md)添加命令会话录像
- 创建包含简短故障模式视频的故障排查页面
