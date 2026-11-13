# BodyOS 开发者文档（当前架构）

日期：2026-11-13
事实来源：用户确认的系统组成与开发边界，以及开发团队提供的四份中文 SDK Markdown 文档。

## 01 首页

- 文档定位与范围
- 系统组成与开发边界入口
- 机械、硬件、Installation、SDK 与示例入口
- 推荐阅读顺序与控制安全提示

## 02 产品与硬件

### 02.1 系统组成与开发边界

- Exo Belt：机械结构、装配与佩戴
- B-core Pi 1：用户可接触的计算与控制入口
- BodyOS SDK：数据与控制 API
- Exoskeleton Unit：内部硬件和驱动封装
- 用户路径：B-core Pi 1 → SDK/API → Exoskeleton Unit

### 02.2 机械结构：Exo Belt

- 机械组成与安装关系（待资料）
- 装配、拆卸与检查（待资料）
- 佩戴、调节与适配（待资料）
- 载荷、活动范围与维护（待确认）

### 02.3 硬件：B-core Pi 1

- 系统角色与开发工作流
- 硬件架构与外形安装（待资料）
- 供电、连接器与板卡接口（待资料）
- 软件环境与支持版本（待确认）
- 通过 SDK/API 读取和控制 Exoskeleton Unit

## 03 Installation

- SDK 版本、平台与架构
- `.gz` / `.tar.gz` 软件包下载
- 文件大小与 SHA-256 校验
- 解压、安装与安装后验证
- 通过 GitHub Release 管理历史版本

## 04 BodyOS SDK

### 04.1 SDK 开发者手册

- 核心架构与特性
- 守护进程部署
- C++ 与 Python 快速接入
- 常见问题

### 04.2 API Reference

#### C++ API

- 生命周期、系统与状态
- 驱动器控制、传感器与配置
- BLE、报警、故障与异步录制

#### Python API

- 生命周期、系统与工作模式
- 驱动器控制、传感器与断线重连
- 配置、BLE、报警与异步录制
- Python `.whl` 分发信息待交付后补充

### 04.3 Integration Libraries（规划中）

- 第三方传感器集成库
- 外部设备集成库
- 支持型号、安装、连接、API 与示例待正式交付后补充

## 05 官方示例

- `sensor_read_record`：传感器读取与异步录制
- `body_assist_control`：BLE 助力模式控制
- `body_expert_control`：专家参数调整
- `direct_motor_control`：底层电机直接控制

## 不进入当前网站

- Exoskeleton Unit 内部硬件、驱动、固件与内部通信实现
- 旧版 Mechanical、Hardware、Integrations、Research、Tutorials 页面
- 未经中文事实来源支持的技术扩写
- 由个人资料或旧版 Wiki 推断出的参数与兼容性说明
