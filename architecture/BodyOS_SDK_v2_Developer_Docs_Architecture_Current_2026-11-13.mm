<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <node ID="root" TEXT="BodyOS 开发者文档">
    <node ID="home" POSITION="right" TEXT="01 首页">
      <node ID="home-scope" TEXT="文档定位与范围"/>
      <node ID="home-entry" TEXT="机械、硬件、Installation、SDK 与示例入口"/>
      <node ID="home-order" TEXT="推荐阅读顺序与安全提示"/>
    </node>
    <node ID="product" POSITION="right" TEXT="02 产品与硬件">
      <node ID="overview" TEXT="02.1 系统组成与开发边界">
        <node ID="overview-belt" TEXT="Exo Belt：机械结构、装配与佩戴"/>
        <node ID="overview-core" TEXT="B-core Pi 1：用户计算与控制入口"/>
        <node ID="overview-sdk" TEXT="BodyOS SDK：数据与控制 API"/>
        <node ID="overview-unit" TEXT="Exoskeleton Unit：内部硬件与驱动封装"/>
        <node ID="overview-path" TEXT="B-core Pi 1 → SDK/API → Exoskeleton Unit"/>
      </node>
      <node ID="belt" TEXT="02.2 机械结构：Exo Belt">
        <node ID="belt-components" TEXT="机械组成与安装关系（待资料）"/>
        <node ID="belt-assembly" TEXT="装配、拆卸与检查（待资料）"/>
        <node ID="belt-wear" TEXT="佩戴、调节与适配（待资料）"/>
        <node ID="belt-safety" TEXT="载荷、活动范围与维护（待确认）"/>
      </node>
      <node ID="bcore" TEXT="02.3 硬件：B-core Pi 1">
        <node ID="bcore-role" TEXT="系统角色与开发工作流"/>
        <node ID="bcore-architecture" TEXT="硬件架构与外形安装（待资料）"/>
        <node ID="bcore-power" TEXT="供电、连接器与板卡接口（待资料）"/>
        <node ID="bcore-software" TEXT="软件环境与支持版本（待确认）"/>
      </node>
    </node>
    <node ID="installation" POSITION="left" TEXT="03 Installation">
      <node ID="installation-release" TEXT="SDK 版本、平台与架构"/>
      <node ID="installation-download" TEXT=".gz / .tar.gz 软件包下载"/>
      <node ID="installation-checksum" TEXT="文件大小与 SHA-256 校验"/>
      <node ID="installation-verify" TEXT="解压、安装与安装后验证"/>
      <node ID="installation-history" TEXT="GitHub Release 历史版本"/>
    </node>
    <node ID="sdk" POSITION="left" TEXT="04 BodyOS SDK">
      <node ID="manual" TEXT="04.1 SDK 开发者手册">
        <node ID="manual-architecture" TEXT="核心架构与特性"/>
        <node ID="manual-deploy" TEXT="部署与 C++/Python 快速接入"/>
        <node ID="manual-faq" TEXT="常见问题"/>
      </node>
      <node ID="api-reference" TEXT="04.2 API Reference">
        <node ID="cpp" TEXT="C++ API">
          <node ID="cpp-control" TEXT="控制、传感器与配置"/>
          <node ID="cpp-monitor" TEXT="BLE、报警、故障与录制"/>
        </node>
        <node ID="python" TEXT="Python API">
          <node ID="python-control" TEXT="控制、传感器与断线重连"/>
          <node ID="python-monitor" TEXT="配置、BLE、报警与录制"/>
          <node ID="python-whl" TEXT=".whl 分发信息待补充"/>
        </node>
      </node>
      <node ID="integration-libraries" TEXT="04.3 Integration Libraries（规划中）">
        <node ID="integration-sensors" TEXT="第三方传感器"/>
        <node ID="integration-devices" TEXT="外部设备"/>
        <node ID="integration-status" TEXT="正式交付后补充支持矩阵与 API"/>
      </node>
    </node>
    <node ID="examples" POSITION="left" TEXT="05 官方示例">
      <node ID="example-sensor" TEXT="sensor_read_record"/>
      <node ID="example-assist" TEXT="body_assist_control"/>
      <node ID="example-expert" TEXT="body_expert_control"/>
      <node ID="example-motor" TEXT="direct_motor_control"/>
    </node>
  </node>
</map>
