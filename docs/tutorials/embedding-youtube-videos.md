# Embedding YouTube Videos

This guide standardizes how Ascentiz documentation pages should embed YouTube videos during phase one of the wiki rollout.

## When To Use A Video

Use a video when motion, sequencing, or operator judgment matters more than a static screenshot:

- bring-up and shutdown sequences
- supervised motion or safety checks
- cable routing, fixture setup, or mechanical alignment
- failure reproduction and troubleshooting
- experiment workflows with multiple tools or screens

Do not rely on video alone. Every page should still explain the critical steps in text so the workflow remains understandable even when the player is blocked or unavailable.

## Standard Embed Pattern

Wrap each video in a short callout that captures scope, versions, and what the reader should watch for.

<div class="video-callout">
  <h2>Bring-Up Walkthrough</h2>
  <p>Use this pattern for any externally hosted tutorial or workflow video.</p>
  <div class="video-callout__meta">
    <span>Hardware v1.2+</span>
    <span>Firmware 0.9.x</span>
    <span>Open Unit 0.14.x</span>
  </div>
  <div class="video-embed">
    <iframe
      src="https://www.youtube-nocookie.com/embed/VIDEO_ID"
      title="Bring-Up Walkthrough"
      loading="lazy"
      referrerpolicy="strict-origin-when-cross-origin"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen>
    </iframe>
  </div>
  <div class="video-transcript">
    <p><strong>What to verify:</strong> link health, no active faults, telemetry freshness, and final session state.</p>
    <p><strong>Fallback:</strong> if the video is unavailable, continue with the written procedure below.</p>
  </div>
</div>

## Copy-Paste Snippet

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

## Authoring Rules

1. Use `youtube-nocookie.com` embeds instead of the default YouTube domain.
2. Keep the written procedure below the video, not inside the video only.
3. Add applicable hardware, firmware, and software versions near the player.
4. Keep titles task-oriented, such as `Bring-Up Walkthrough` or `Safety-Gated Command Session`.
5. Mention the safety boundary and stop conditions in text, even if the video explains them verbally.
6. If a page may later require a non-YouTube mirror for regional access, add a plain link to the alternate host below the embed.

## Recommended Next Uses

- Add a real bring-up video to [Bring-Up Workflow](bring-up-workflow.md)
- Add a command session recording to [Safety-Gated Commanding](safety-gated-commanding.md)
- Create a troubleshooting page with short failure-mode clips
