<a href="https://remakelist.com/zh/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=intro-zh-CN"><img src="assets/brand-banner.svg" alt="RemakeList — software recreations and classic game ports" width="920"></a>

# Awesome RemakeList

整理软件重实现、游戏引擎和跨平台移植，也写清体验前需要准备什么。

[English](README.md) · **简体中文** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md)

[浏览 RemakeList](https://remakelist.com/zh/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=intro-zh-CN) · [推荐项目](https://github.com/CharlexH/awesome-remakelist/issues/new?template=project.yml)

[![Catalog checks](https://github.com/CharlexH/awesome-remakelist/actions/workflows/check.yml/badge.svg?branch=main)](https://github.com/CharlexH/awesome-remakelist/actions/workflows/check.yml) [![Website sync](https://github.com/CharlexH/awesome-remakelist/actions/workflows/sync.yml/badge.svg?branch=main)](https://github.com/CharlexH/awesome-remakelist/actions/workflows/sync.yml)

点击项目名可直达作者来源，展开条目可查看设备、游戏文件和构建要求。RemakeList 详情页还提供截图与安装说明。

## 从这里开始

| 项目 | 查看详情 | 开始方式 |
| --- | --- | --- |
| [Graphite](https://remakelist.com/zh/remakes/graphite/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=graphite-featured-zh-CN) | Adobe Illustrator | [浏览器体验](https://editor.graphite.art/) |
| [Webamp](https://remakelist.com/zh/remakes/webamp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=webamp-featured-zh-CN) | Winamp 2 | [浏览器体验](https://webamp.org/) |
| [OpenTTD](https://remakelist.com/zh/remakes/openttd/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openttd-featured-zh-CN) | Transport Tycoon Deluxe | [下载](https://www.openttd.org/) |
| [OpenRCT2](https://remakelist.com/zh/remakes/openrct2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openrct2-featured-zh-CN) | RollerCoaster Tycoon 2 | [下载程序并自备游戏文件](https://openrct2.io/download) |
| [D2R Mobile](https://remakelist.com/zh/remakes/d2r-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=d2r-mobile-featured-zh-CN) | Diablo II: Resurrected | [自行构建并自备游戏文件](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) |
| [nxnative](https://remakelist.com/zh/remakes/nxnative/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nxnative-featured-zh-CN) | Nintendo Switch 游戏 | [自行构建并自备游戏文件](https://github.com/seedds/nxnative#pack-an-ipa) |

## 浏览分类

- [设计与创作工具](#creative) · 13
- [日常工具与界面再现](#everyday) · 9
- [游戏引擎与重制](#classic_games) · 26
- [移植与兼容项目](#ports) · 42

<img src="assets/overview-zh-CN.svg" alt="目录" width="920">

<a id="creative"></a>

## 设计与创作工具

### [Compositor](https://github.com/robbietilton/Compositor)

面向 Apple silicon Mac 的图层合成与后期编辑器，围绕 Photoshop 式工作流设计。

原作或参考对象: **Adobe Photoshop** · 独立功能平替  
[下载](https://github.com/robbietilton/Compositor/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/compositor/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=compositor-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Apple silicon Mac · macOS 26+

**当前阶段:** 开发中 · 提供发行版

**需要准备什么:** 无需 Photoshop；需要 Apple silicon Mac 与 macOS 26+。从源码构建还需 Xcode 26+，编辑素材的权利由用户负责。

**现在能用什么:** 已有可下载发行版，要求 Apple silicon Mac 与 macOS 26+，目前仅支持英文。PSD/PSB 导入限 8-bit RGB，不支持 CMYK，部分矢量与竖排文本会栅格化。源码构建需 Xcode 26+。

**代码许可:** [MIT](https://github.com/robbietilton/Compositor/blob/main/LICENSE)  
**作者:** robbietilton  
[官方文档](https://github.com/robbietilton/Compositor/blob/main/README.md) · 资料核对日期: 2026-10-12

</details>

### [PhotoCraft](https://github.com/storytold/photocraft)

ArtCraft 团队用 Rust 再实现 Photoshop 式图像编辑工作流，当前处于 alpha。

原作或参考对象: **Adobe Photoshop** · 工作流重实现  
[下载](https://github.com/storytold/photocraft/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/photocraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=photocraft-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / FreeBSD / Web

**当前阶段:** Alpha · 工作流仍在完善

**需要准备什么:** 无需 Photoshop 安装文件；处理的图片和其他素材需有使用权。字体、图标等另有许可，ArtCraft 品牌标识不在代码许可中。

**现在能用什么:** 已有可下载的 alpha 发行版，无需安装 Photoshop。项目列出 Windows、macOS、Linux、FreeBSD 与 Web 支持；PSD 互操作、工具深度与插件兼容仍有缺口，暂不宜视为专业工作流的完整替代。

**代码许可:** [MIT OR Apache-2.0](https://github.com/storytold/photocraft/blob/main/LICENSE-MIT)  
**作者:** storytold  
[官方文档](https://github.com/storytold/photocraft/blob/main/README.md) · 资料核对日期: 2026-10-12

</details>

### [Graphite](https://github.com/GraphiteEditor/Graphite)

把矢量绘图、图层与节点连接起来的开源设计工具，在浏览器里尝试非破坏式创作。

原作或参考对象: **Adobe Illustrator** · 独立功能平替  
[浏览器体验](https://editor.graphite.art/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/graphite/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=graphite-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** 浏览器

**当前阶段:** Alpha · 可在线体验

**需要准备什么:** 无需 Illustrator 或原软件安装文件；使用自己的图片、字体等创作素材。

**现在能用什么:** 现在可直接打开浏览器编辑器体验矢量设计，无需安装 Illustrator。项目仍是 alpha；照片编辑、动态图形、出版和 VFX 等更广泛能力仍在发展，不宜据此替换整套 Adobe 工作流。

**代码许可:** [MIT OR Apache-2.0](https://graphite.art/license/)  
**作者:** Graphite community  
[官方文档](https://github.com/GraphiteEditor/Graphite/blob/master/README.md) · 资料核对日期: 2026-10-12

</details>

### [Friction](https://github.com/friction2d/friction)

面向二维动态图形的开源动画工具，支持矢量、栅格、时间线和表达式。

原作或参考对象: **Adobe After Effects** · 独立功能平替  
[下载](https://friction.graphics/#download) · [浏览 RemakeList](https://remakelist.com/zh/remakes/friction/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=friction-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 提供桌面下载 · 二维动效

**需要准备什么:** 无需安装 After Effects；使用自己的图片、字体、音视频等创作素材。

**现在能用什么:** 官网提供 Windows、Linux 和 macOS 下载。可以制作二维动画与动效；自定义 shader 效果仍在实验阶段，也不保证兼容 After Effects 的项目、插件或完整特效链。

**代码许可:** [GPL-3.0-only](https://github.com/friction2d/friction/blob/main/LICENSE.md)  
**作者:** Ole-André Rodlie &amp; contributors  
[官方文档](https://friction.graphics/) · 资料核对日期: 2026-10-12

</details>

### [OpenCut](https://github.com/OpenCut-app/OpenCut)

瞄准 CapCut 式视频剪辑的开源编辑器，官网目前提供 classic 早期 beta，下一版正在重写。

原作或参考对象: **CapCut / 剪映** · 独立功能平替  
[浏览器体验](https://opencut.app/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/opencut/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=opencut-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** 浏览器

**当前阶段:** 早期 Beta · 重写中

**需要准备什么:** 无需 CapCut 或剪映安装文件；导入自己有权使用的视频、图片和音频素材。

**现在能用什么:** 现在可以从官网进入 classic 早期 beta。它还在快速变化，classic 源码已归档，新版本正重写；适合尝鲜，不应默认能完整接替日常 CapCut 工作流。

**代码许可:** [MIT](https://github.com/OpenCut-app/OpenCut/blob/main/LICENSE)  
**作者:** OpenCut contributors  
[官方文档](https://github.com/OpenCut-app/OpenCut/blob/main/README.md) · 资料核对日期: 2026-10-12

</details>

### [Penpot](https://github.com/penpot/penpot)

开源协作设计与原型平台，可使用官方云端或自行部署。

原作或参考对象: **Figma** · 独立功能平替  
[注册体验或自托管](https://design.penpot.app) · [浏览 RemakeList](https://remakelist.com/zh/remakes/penpot/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=penpot-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Browser / self-hosted

**当前阶段:** 见官方说明

**需要准备什么:** 不需要 Figma 软件或素材；迁移自有设计需自行导出导入。

**现在能用什么:** 可注册使用官方云端，或自行部署。迁移已有设计需要导出与导入；云端服务方案需查看官方价格页。

**代码许可:** [MPL-2.0](https://github.com/penpot/penpot/blob/develop/LICENSE)  
**作者:** penpot  
[官方文档](https://penpot.app/penpot-vs-figma) · 资料核对日期: 2026-10-11

</details>

### [VectorCraft](https://github.com/storytold/vectorcraft)

ArtCraft 团队以 Rust 重建Adobe Illustrator式工作流：钢笔、路径布尔运算、外观效果与矢量插画。

原作或参考对象: **Adobe Illustrator** · 工作流重实现  
[下载](https://getartcraft.com/apps/vectorcraft) · [浏览 RemakeList](https://remakelist.com/zh/remakes/vectorcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vectorcraft-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Web

**当前阶段:** Alpha

**需要准备什么:** 无需原版商业软件。自备有使用权的文档和素材；附带字体、图片与品牌标识各有许可。

**现在能用什么:** Alpha：可尝试日常矢量绘图，但复杂文件互操作和效果深度仍需验证。提供桌面安装包，具体平台和文件兼容性以项目说明为准。

**代码许可:** [MIT OR Apache-2.0](https://github.com/storytold/vectorcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[官方文档](https://github.com/storytold/vectorcraft/blob/main/README.md) · 资料核对日期: 2026-10-12

</details>

### [FilmCraft](https://github.com/storytold/filmcraft)

ArtCraft 团队以 Rust 重建Adobe Premiere Pro式工作流：源监视器、节目监视器、多轨时间线与剪辑修整。

原作或参考对象: **Adobe Premiere Pro** · 工作流重实现  
[下载](https://getartcraft.com/apps/filmcraft) · [浏览 RemakeList](https://remakelist.com/zh/remakes/filmcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=filmcraft-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** Alpha

**需要准备什么:** 无需原版商业软件。自备有使用权的文档和素材；附带字体、图片与品牌标识各有许可。

**现在能用什么:** Alpha：已有剪辑和导出流程；大素材性能、效果渲染与专业项目兼容仍有缺口。提供桌面安装包，具体平台和文件兼容性以项目说明为准。

**代码许可:** [MIT OR Apache-2.0](https://github.com/storytold/filmcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[官方文档](https://github.com/storytold/filmcraft/blob/main/README.md) · 资料核对日期: 2026-10-12

</details>

### [LightCraft](https://github.com/storytold/lightcraft)

ArtCraft 团队以 Rust 重建Adobe Lightroom式工作流：照片图库管理、RAW 显影与非破坏性调色。

原作或参考对象: **Adobe Lightroom** · 工作流重实现  
[下载](https://getartcraft.com/apps/lightcraft) · [浏览 RemakeList](https://remakelist.com/zh/remakes/lightcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=lightcraft-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Web

**当前阶段:** Alpha

**需要准备什么:** 无需原版商业软件。自备有使用权的文档和素材；附带字体、图片与品牌标识各有许可。

**现在能用什么:** Alpha：可试 JPEG、DNG 及多种相机 RAW；相机色彩校准和部分压缩 RAW 支持不完整。提供桌面安装包，具体平台和文件兼容性以项目说明为准。

**代码许可:** [MIT OR Apache-2.0](https://github.com/storytold/lightcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[官方文档](https://github.com/storytold/lightcraft/blob/main/README.md) · 资料核对日期: 2026-10-12

</details>

### [EffectCraft](https://github.com/storytold/effectcraft)

ArtCraft 团队以 Rust 重建Adobe After Effects式工作流：图层合成、关键帧动画、动态图形与特效。

原作或参考对象: **Adobe After Effects** · 工作流重实现  
[下载](https://getartcraft.com/apps/effectcraft) · [浏览 RemakeList](https://remakelist.com/zh/remakes/effectcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=effectcraft-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Web

**当前阶段:** 早期开发

**需要准备什么:** 无需原版商业软件。自备有使用权的文档和素材；附带字体、图片与品牌标识各有许可。

**现在能用什么:** 早期开发：适合尝试动画与合成，尚不适合客户交付；不能打开 AEP/AEPX，也不能运行 After Effects 插件。提供桌面安装包，具体平台和文件兼容性以项目说明为准。

**代码许可:** [MIT OR Apache-2.0](https://github.com/storytold/effectcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[官方文档](https://github.com/storytold/effectcraft/blob/main/README.md) · 资料核对日期: 2026-10-12

</details>

### [DesignCraft](https://github.com/storytold/designcraft)

ArtCraft 团队以 Rust 重建Adobe InDesign式工作流：跨页排版、文本框串联、母版与出版文档。

原作或参考对象: **Adobe InDesign** · 工作流重实现  
[下载](https://getartcraft.com/apps/designcraft) · [浏览 RemakeList](https://remakelist.com/zh/remakes/designcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=designcraft-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Web

**当前阶段:** 开发中

**需要准备什么:** 无需原版商业软件。自备有使用权的文档和素材；附带字体、图片与品牌标识各有许可。

**现在能用什么:** 开发中：已有排版与导出版本；复杂出版文件、字体排版和印前工作流需逐项检查。提供桌面安装包，具体平台和文件兼容性以项目说明为准。

**代码许可:** [MIT OR Apache-2.0](https://github.com/storytold/designcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[官方文档](https://github.com/storytold/designcraft/blob/main/README.md) · 资料核对日期: 2026-10-12

</details>

### [SoundCraft](https://github.com/storytold/soundcraft)

ArtCraft 团队以 Rust 重建Avid Pro Tools式工作流：音轨录制、编辑窗口、混音台与 MIDI 编排。

原作或参考对象: **Avid Pro Tools** · 工作流重实现  
[下载](https://getartcraft.com/apps/soundcraft) · [浏览 RemakeList](https://remakelist.com/zh/remakes/soundcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=soundcraft-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Web

**当前阶段:** Pre-alpha

**需要准备什么:** 无需原版商业软件。自备有使用权的文档和素材；附带字体、图片与品牌标识各有许可。

**现在能用什么:** Pre-alpha：已有录制、编辑、混音和导出流程；音频设备与缓冲设置、MIDI 控制器录制和 AAF/OMF 交换尚缺。提供桌面安装包，具体平台和文件兼容性以项目说明为准。

**代码许可:** [MIT OR Apache-2.0](https://github.com/storytold/soundcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[官方文档](https://github.com/storytold/soundcraft/blob/main/README.md) · 资料核对日期: 2026-10-12

</details>

### [CADCraft](https://github.com/storytold/cadcraft)

ArtCraft 团队以 Rust 重建Autodesk AutoCAD式工作流：命令行绘图、对象捕捉、图层、尺寸标注与图纸布局。

原作或参考对象: **Autodesk AutoCAD** · 工作流重实现  
[下载](https://getartcraft.com/apps/cadcraft) · [浏览 RemakeList](https://remakelist.com/zh/remakes/cadcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cadcraft-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Web

**当前阶段:** 早期开发

**需要准备什么:** 无需原版商业软件。自备有使用权的文档和素材；附带字体、图片与品牌标识各有许可。

**现在能用什么:** 早期开发：可尝试二维图纸与 PDF 出图；不能视为 AutoCAD 全套三维、DWG 和行业插件工作流的替代。提供桌面安装包，具体平台和文件兼容性以项目说明为准。

**代码许可:** [MIT OR Apache-2.0](https://github.com/storytold/cadcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[官方文档](https://github.com/storytold/cadcraft/blob/main/README.md) · 资料核对日期: 2026-10-12

</details>


<a id="everyday"></a>

## 日常工具与界面再现

### [ONLYOFFICE Desktop Editors](https://github.com/ONLYOFFICE/DesktopEditors)

一套可离线使用的 Office 开源平替，把文档、表格、演示与 PDF 编辑放在同一个桌面应用里。

原作或参考对象: **Microsoft Office** · 独立功能平替  
[下载](https://www.onlyoffice.com/download-desktop) · [浏览 RemakeList](https://remakelist.com/zh/remakes/onlyoffice/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=onlyoffice-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 提供正式发行版

**需要准备什么:** 无需 Microsoft Office 或账号即可编辑本地文件；云端协作需要连接相应服务，部分服务收费。

**现在能用什么:** Windows、macOS、Linux 都有安装包，文档可保存在本机并离线编辑。个人日常办公可以直接下载使用；团队云端服务与企业版另有方案，复杂文档仍建议先检查排版。

**代码许可:** [AGPL-3.0](https://github.com/ONLYOFFICE/DesktopEditors/blob/master/LICENSE)  
**作者:** ONLYOFFICE  
[官方文档](https://github.com/ONLYOFFICE/DesktopEditors) · 资料核对日期: 2026-10-12

</details>

### [Grist](https://github.com/gristlabs/grist-core)

把电子表格与关系数据库放在一起，适合把 Excel 或 Airtable 里的业务表格做成可关联的数据工具。

原作或参考对象: **Microsoft Excel / Airtable** · 独立功能平替  
[下载](https://github.com/gristlabs/grist-desktop/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/grist/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=grist-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 提供正式发行版

**需要准备什么:** 桌面版可处理本地文件；自行托管需要服务器环境。官网云端方案需要账号，并有用量与功能边界。

**现在能用什么:** 可下载 Windows、macOS、Linux 桌面版编辑本地文件，也可以自行托管 Community 版。官网另有免费和付费云端方案，企业功能并不全部包含在开源核心里。

**代码许可:** [Apache-2.0](https://github.com/gristlabs/grist-core/blob/main/LICENSE.txt)  
**作者:** Grist Labs  
[官方文档](https://github.com/gristlabs/grist-core) · 资料核对日期: 2026-10-12

</details>

### [LibreOffice](https://github.com/LibreOffice/core)

一套完整的免费开源办公套件，用 Writer、Calc 和 Impress 承接文档、表格与演示工作。

原作或参考对象: **Microsoft Office** · 独立功能平替  
[下载](https://www.libreoffice.org/download/download-libreoffice/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/libreoffice/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=libreoffice-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 提供正式发行版

**需要准备什么:** 无需 Microsoft Office、订阅或账号；安装适合系统的桌面版本即可，本地文件需有使用权。

**现在能用什么:** Windows、macOS、Linux 都能下载使用。写文档、做表格与演示已有完整工具；如果工作依赖 VBA 宏、复杂 Office 模板或精确版式，迁移前应拿实际文件试一遍。

**代码许可:** [MPL-2.0 (primarily)](https://www.libreoffice.org/licenses/)  
**作者:** The Document Foundation  
[官方文档](https://www.libreoffice.org/) · 资料核对日期: 2026-10-12

</details>

### [Webamp](https://github.com/captbaritone/webamp)

把 Winamp 2 搬到浏览器，保留经典播放器界面和皮肤支持。

原作或参考对象: **Winamp 2** · 网页重实现  
[浏览器体验](https://webamp.org/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/webamp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=webamp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Browser

**当前阶段:** 见官方说明

**需要准备什么:** 不需要安装 Winamp；音频与第三方皮肤另受各自权利约束。

**现在能用什么:** 提供可直接打开的在线播放器。播放所需的音频可另行准备，无需原版程序。

**代码许可:** [MIT](https://github.com/captbaritone/webamp/blob/master/LICENSE.txt)  
**作者:** captbaritone  
[官方文档](https://github.com/captbaritone/webamp/blob/master/README.md) · 资料核对日期: 2026-10-11

</details>

### [WinXP in React](https://github.com/ShizukuIchi/winXP)

在浏览器里重现 Windows XP 桌面、开始菜单和经典小程序。

原作或参考对象: **Windows XP 桌面** · 界面再现  
[浏览器体验](https://winxp.vercel.app/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/winxp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=winxp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Browser

**当前阶段:** 见官方说明

**需要准备什么:** 无需 Windows XP 安装文件。

**现在能用什么:** 提供在线演示，无需 Windows XP 安装文件。体验范围是已重现的桌面与小程序，不能运行任意 XP 软件。

**代码许可:** [MIT (project code)](https://github.com/ShizukuIchi/winXP/blob/master/LICENSE)  
**作者:** ShizukuIchi  
[官方文档](https://github.com/ShizukuIchi/winXP/blob/master/README.md) · 资料核对日期: 2026-10-11

</details>

### [PdfCraft](https://github.com/storytold/pdfcraft)

ArtCraft 团队以 Rust 重建Adobe Acrobat式工作流：PDF 阅读、批注、页面整理、合并与拆分。

原作或参考对象: **Adobe Acrobat** · 工作流重实现  
[下载](https://getartcraft.com/apps/pdfcraft) · [浏览 RemakeList](https://remakelist.com/zh/remakes/pdfcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pdfcraft-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Web

**当前阶段:** 早期 Alpha

**需要准备什么:** 无需原版商业软件。自备有使用权的文档和素材；附带字体、图片与品牌标识各有许可。

**现在能用什么:** 早期 Alpha：已有阅读和页面管理流程；不要把它当作 Acrobat 全套编辑、签名和印前功能的完整替代。提供桌面安装包，具体平台和文件兼容性以项目说明为准。

**代码许可:** [MIT OR Apache-2.0](https://github.com/storytold/pdfcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[官方文档](https://github.com/storytold/pdfcraft/blob/main/README.md) · 资料核对日期: 2026-10-12

</details>

### [WordCraft](https://github.com/storytold/wordcraft)

ArtCraft 团队以 Rust 重建Microsoft Word式工作流：文字处理、样式、表格、修订与文档布局。

原作或参考对象: **Microsoft Word** · 工作流重实现  
[下载](https://getartcraft.com/apps/wordcraft) · [浏览 RemakeList](https://remakelist.com/zh/remakes/wordcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wordcraft-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Web

**当前阶段:** Alpha

**需要准备什么:** 无需原版商业软件。自备有使用权的文档和素材；附带字体、图片与品牌标识各有许可。

**现在能用什么:** Alpha：可尝试写作与 DOCX 文档；分页、图表与 SmartArt 往返保真、原生打印仍是完善重点。提供桌面安装包，具体平台和文件兼容性以项目说明为准。

**代码许可:** [MIT OR Apache-2.0](https://github.com/storytold/wordcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[官方文档](https://github.com/storytold/wordcraft/blob/main/README.md) · 资料核对日期: 2026-10-13

</details>

### [DeckCraft](https://github.com/storytold/deckcraft)

ArtCraft 团队以 Rust 重建Microsoft PowerPoint式工作流：幻灯片母版、主题、图形、动画与演示播放。

原作或参考对象: **Microsoft PowerPoint** · 工作流重实现  
[下载](https://getartcraft.com/apps/deckcraft) · [浏览 RemakeList](https://remakelist.com/zh/remakes/deckcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=deckcraft-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Web

**当前阶段:** Alpha

**需要准备什么:** 无需原版商业软件。自备有使用权的文档和素材；附带字体、图片与品牌标识各有许可。

**现在能用什么:** Alpha：可尝试制作和播放演示文稿；复杂 PPTX 文件和动画效果不应假定与 PowerPoint 完全一致。提供桌面安装包，具体平台和文件兼容性以项目说明为准。

**代码许可:** [MIT OR Apache-2.0](https://github.com/storytold/deckcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[官方文档](https://github.com/storytold/deckcraft/blob/main/README.md) · 资料核对日期: 2026-10-13

</details>

### [GridCraft](https://github.com/storytold/gridcraft)

ArtCraft 团队以 Rust 重建Microsoft Excel式工作流：工作表、公式、表格、图表与数据透视工作流。

原作或参考对象: **Microsoft Excel** · 工作流重实现  
[下载](https://getartcraft.com/apps/gridcraft) · [浏览 RemakeList](https://remakelist.com/zh/remakes/gridcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gridcraft-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Web

**当前阶段:** Alpha

**需要准备什么:** 无需原版商业软件。自备有使用权的文档和素材；附带字体、图片与品牌标识各有许可。

**现在能用什么:** Alpha：核心表格流程已可尝试；真实 XLSX 保真、大工作簿性能、图表深度与旧格式导入仍需改进。提供桌面安装包，具体平台和文件兼容性以项目说明为准。

**代码许可:** [MIT OR Apache-2.0](https://github.com/storytold/gridcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[官方文档](https://github.com/storytold/gridcraft/blob/main/README.md) · 资料核对日期: 2026-10-13

</details>


<a id="classic_games"></a>

## 游戏引擎与重制

### [Vanguard Engine](https://github.com/harshilmathur/openra2)

面向红警 2 数据的独立浏览器 RTS 引擎，当前聚焦苏军单人遭遇战开发切片。

原作或参考对象: **红色警戒 2 / 尤里的复仇数据** · 引擎重实现  
[从源码构建](https://github.com/harshilmathur/openra2/blob/master/README.md#quickstart) · [浏览 RemakeList](https://remakelist.com/zh/remakes/vanguard/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vanguard-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** 浏览器 · 本地开发服务器

**当前阶段:** 开发切片 · 无正式 release

**需要准备什么:** Classic 模式需合法拥有 RA2/YR 并提供原版文件；Original 模式使用仓库原创资源，不需原游戏。两种资源模式分开。需要 Node.js 20.19+ 和本地开发服务器。

**现在能用什么:** 目前是需本地运行的开发切片，无正式发行版；需要 Node.js 20.19+ 与本地开发服务器。Classic 模式需自备合法 RA2/YR 文件，Original 模式无需原游戏。盟军、联机与尤里玩法尚未完成，不能当作完整版红警 2。

**代码许可:** [GPL-3.0-or-later](https://github.com/harshilmathur/openra2/blob/master/LICENSE)  
**作者:** harshilmathur  
[官方文档](https://github.com/harshilmathur/openra2/blob/master/README.md) · 资料核对日期: 2026-10-12

</details>

### [OpenTTD](https://github.com/OpenTTD/OpenTTD)

重建运输大亨玩法，并扩展现代平台和多人游戏支持。

原作或参考对象: **Transport Tycoon Deluxe** · 游戏重实现  
[下载](https://www.openttd.org/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/openttd/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openttd-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 见官方说明

**需要准备什么:** 需要基础图形，可用免费的 OpenGFX2 或 OpenGFX；OpenSFX 音效与 OpenMSX 音乐可选。这条免费启动路径无需原版游戏文件。

**现在能用什么:** 可下载桌面发行版。先准备必需的免费 OpenGFX2 或 OpenGFX 图形；OpenSFX 音效与 OpenMSX 音乐可选。这条启动路径无需原版游戏文件。

**代码许可:** [GPL-2.0; third-party components have separate licenses](https://github.com/OpenTTD/OpenTTD/blob/master/COPYING.md)  
**作者:** OpenTTD  
[官方文档](https://github.com/OpenTTD/OpenTTD/blob/master/README.md) · 资料核对日期: 2026-10-11

</details>

### [OpenRCT2](https://github.com/OpenRCT2/OpenRCT2)

让过山车大亨 2 在现代平台继续运行，并加入合作联机等改进。

原作或参考对象: **RollerCoaster Tycoon 2** · 游戏重实现  
[下载程序并自备游戏文件](https://openrct2.io/download) · [浏览 RemakeList](https://remakelist.com/zh/remakes/openrct2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openrct2-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 见官方说明

**需要准备什么:** 必须自备 RCT2 原版数据文件；支持使用 RCT1 数据扩展场景。

**现在能用什么:** 可下载发行版，但必须自备 RCT2 原版数据文件；另有 RCT1 数据时，还可加入其场景。免费下载的是引擎，原版游戏素材需另外取得。

**代码许可:** [GPL-3.0-or-later](https://github.com/OpenRCT2/OpenRCT2/blob/develop/licence.txt)  
**作者:** OpenRCT2  
[官方文档](https://github.com/OpenRCT2/OpenRCT2/blob/develop/readme.md) · 资料核对日期: 2026-10-11

</details>

### [OpenMW](https://github.com/OpenMW/openmw)

用现代开源引擎运行晨风，改善兼容性与图形体验。

原作或参考对象: **The Elder Scrolls III: Morrowind** · 引擎重实现  
[下载程序并自备游戏文件](https://www.openmw.org) · [浏览 RemakeList](https://remakelist.com/zh/remakes/openmw/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openmw-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 见官方说明

**需要准备什么:** 玩晨风需要拥有原游戏并配置其数据文件。

**现在能用什么:** 可下载引擎，玩《晨风》需要合法拥有原游戏并配置其数据文件。部分原版模组不兼容，已有模组组合需先确认支持情况。

**代码许可:** [GPLv3; some fonts separately licensed](https://github.com/OpenMW/openmw/blob/master/LICENSE)  
**作者:** OpenMW  
[官方文档](https://github.com/OpenMW/openmw/blob/master/README.md) · 资料核对日期: 2026-10-11

</details>

### [OpenRA](https://github.com/OpenRA/OpenRA)

重建并现代化经典即时战略游戏，包含三套官方游戏模组。

原作或参考对象: **红色警戒 1 / Command &amp; Conquer / Dune 2000** · 玩法再创作  
[下载](https://www.openra.net/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/openra/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openra-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 见官方说明

**需要准备什么:** 仍使用原游戏素材；官方说明首次运行可自动取得所需素材，也可从原盘导入。

**现在能用什么:** 提供 Windows、macOS 和 Linux 下载。仍需要原游戏素材；官方说明首次运行可自动获取所需素材，也可以从原版光盘导入。

**代码许可:** [GPL-3.0-or-later (engine)](https://github.com/OpenRA/OpenRA/blob/bleed/COPYING)  
**作者:** OpenRA  
[官方文档](https://www.openra.net/about/) · 资料核对日期: 2026-10-11

</details>

### [fheroes2](https://github.com/ihhub/fheroes2)

重建英雄无敌 II 引擎，为桌面和 Android 提供改进的运行体验。

原作或参考对象: **Heroes of Might and Magic II（英雄无敌 II）** · 引擎重实现  
[下载程序并自备游戏文件](https://github.com/ihhub/fheroes2/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/fheroes2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fheroes2-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Android

**当前阶段:** 有发行版 · 原作或 demo 数据

**需要准备什么:** 需完整版原作或官方英文 demo 数据；INSTALL.md 说明随附脚本的 demo 获取路径。Demo 资源只有其授权的有限内容。

**现在能用什么:** 提供发行版，需自备完整版原作数据，或使用官方英文 demo 数据；安装文档提供 demo 获取方式。Demo 只有有限内容，完整游戏仍需合法拥有原版素材，各平台安装步骤也不同。

**代码许可:** [GPL-2.0-or-later](https://github.com/ihhub/fheroes2/blob/master/LICENSE)  
**作者:** ihhub  
[官方文档](https://github.com/ihhub/fheroes2/blob/master/README.md) · 资料核对日期: 2026-10-12

</details>

### [OpenXcom](https://github.com/OpenXcom/OpenXcom)

在现代桌面平台重现经典 X-COM 两部作品，并支持扩展模组。

原作或参考对象: **UFO: Enemy Unknown / Terror from the Deep** · 游戏重实现  
[下载程序并自备游戏文件](https://github.com/OpenXcom/OpenXcom/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/openxcom/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openxcom-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 桌面引擎 · 需原版数据

**需要准备什么:** 必须提供 UFO: Enemy Unknown 或 Terror from the Deep 的未修改原版数据；Windows 安装器可从已拥有的 Steam 游戏提取资源。

**现在能用什么:** 可下载桌面发行版，必须提供其中一部原作的未修改数据文件。Windows 安装器可从已拥有的 Steam 副本提取素材；额外模组可能有自己的素材要求。

**代码许可:** [GPL-3.0-or-later](https://github.com/OpenXcom/OpenXcom/blob/master/LICENSE.txt)  
**作者:** OpenXcom  
[官方文档](https://github.com/OpenXcom/OpenXcom/blob/master/README.md) · 资料核对日期: 2026-10-12

</details>

### [VCMI](https://github.com/vcmi/vcmi)

《英雄无敌 III》的开源引擎再实现，提供桌面与手机版本、模组支持和多人游戏。

原作或参考对象: **魔法门之英雄无敌 III** · 引擎重实现  
[下载程序并自备游戏文件](https://vcmi.eu/download/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/vcmi/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vcmi-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Android / iOS

**当前阶段:** 公开发行 · 需原版数据

**需要准备什么:** 完整游戏需自备已拥有的《英雄无敌 III》Complete 或 Shadow of Death 数据。启动器可导入 GOG 离线安装包或已有安装目录。仅有 HD Edition 不够；它只能作为可选扩展，仍需 Complete/SoD。官方模组目录另有内容受限的 demo 支持。

**现在能用什么:** 已公开发行 1.7.5，官方列有 Windows、macOS、Linux 与 Android 安装包；iOS 通过 TestFlight 或侧载安装。不保证完全兼容；本站未运行。

**代码许可:** [GPL-2.0-or-later code; VCMI-created assets CC-BY-SA 4.0; original game assets separate](https://github.com/vcmi/vcmi/blob/66fa496c6328a276c4eb14c0011b3a9d751dfac3/license.txt)  
**作者:** VCMI Team  
[官方文档](https://github.com/vcmi/vcmi/blob/66fa496c6328a276c4eb14c0011b3a9d751dfac3/docs/Readme.md) · 资料核对日期: 2026-10-18

</details>

### [Julius](https://github.com/bvschaik/julius)

忠于原版逻辑的《凯撒大帝 III》再实现，让这款城市建设游戏运行于现代桌面系统、安卓等平台。

原作或参考对象: **凯撒大帝 III** · 游戏重实现  
[下载程序并自备游戏文件](https://github.com/bvschaik/julius/releases/tag/v1.8.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/julius/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=julius-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows · Linux · macOS · Android · 网页（Emscripten）· PS Vita · Nintendo Switch

**当前阶段:** 已发行 · 需原版游戏数据

**需要准备什么:** 需自备光盘版、GOG 或 Steam 版《凯撒大帝 III》的完整安装数据，并更新至 1.0.1.0。Julius 读取该数据目录，并需要向其中写入存档的权限。代码许可不提供或授予原游戏素材的使用权。

**现在能用什么:** 1.8.0 版提供 Windows、Linux、macOS、安卓下载，以及 Vita、Switch 和 Emscripten 包。浏览器包仍需自行配置和提供游戏文件。本站未运行。

**代码许可:** [AGPL-3.0 · engine code; original Caesar III assets are separate](https://github.com/bvschaik/julius/blob/34d1ecd54befb845c0139b371fa8a0438210dac1/LICENSE.txt)  
**作者:** Bianca van Schaik and contributors  
[官方文档](https://github.com/bvschaik/julius/blob/34d1ecd54befb845c0139b371fa8a0438210dac1/README.md) · 资料核对日期: 2026-10-18

</details>

### [CorsixTH](https://github.com/CorsixTH/CorsixTH)

《主题医院》引擎再实现，支持现代桌面系统、高分辨率和自定义医院关卡。

原作或参考对象: **主题医院** · 游戏重实现  
[下载程序并自备游戏文件](https://github.com/CorsixTH/CorsixTH/releases/tag/v0.70.1) · [浏览 RemakeList](https://remakelist.com/zh/remakes/corsixth/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=corsixth-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows · macOS · Linux · BSD

**当前阶段:** 已发行 · 需原版或试玩数据

**需要准备什么:** 需自备合法持有的《主题医院》光盘或数字安装数据，首次启动时选择数据目录。官方试玩数据仅有一关，并缺少大部分管理界面。引擎许可不授予原版素材使用权。

**现在能用什么:** 0.70.1 提供 Windows、macOS 版本及 Linux AppImage、发行版软件包，也支持 BSD。Mac 发行版禁用 RtMidi 硬件 MIDI。本站未运行。

**代码许可:** [MIT · engine code; Theme Hospital assets are separate](https://github.com/CorsixTH/CorsixTH/blob/master/LICENSE.txt)  
**作者:** CorsixTH team and contributors  
[官方文档](https://github.com/CorsixTH/CorsixTH/blob/master/README.md) · 资料核对日期: 2026-10-19

</details>

### [Warzone 2100](https://github.com/Warzone2100/warzone2100)

1999 年 3D 即时战略游戏的社区延续版，提供完整战役、可定制单位和桌面联机。

原作或参考对象: **战地 2100（1999）** · 开源项目续作  
[下载](https://wz2100.net/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/warzone2100/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=warzone2100-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows · macOS · Linux · 网页

**当前阶段:** 已发行 · 桌面与浏览器版本

**需要准备什么:** 无需另外购买原游戏或提供光盘镜像。使用官方安装包；部分平台可能需另从官方补充下载战役视频。代码、游戏数据与各组件分别遵循其声明许可。

**现在能用什么:** 4.7.0 提供 Windows、macOS 和 Linux 下载，Mac 包支持 Intel 与 Apple silicon。官方浏览器版可玩战役和遭遇战，图形规格较低且无在线多人。本站未运行。

**代码许可:** [GPL-2.0-or-later and component licenses](https://github.com/Warzone2100/warzone2100/blob/master/COPYING)  
**作者:** Warzone 2100 Project  
[官方文档](https://github.com/Warzone2100/warzone2100/blob/master/README.md) · 资料核对日期: 2026-10-19

</details>

### [ScummVM](https://github.com/scummvm/scummvm)

通过重新实现的游戏引擎，让《猴岛》《神秘岛》《银翼杀手》等经典冒险游戏运行于现代设备。

原作或参考对象: **经典冒险游戏与角色扮演游戏** · 引擎重实现  
[下载程序并自备游戏文件](https://www.scummvm.org/downloads/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/scummvm/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=scummvm-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Android / iOS

**当前阶段:** 已发行 · 兼容性随游戏和平台变化

**需要准备什么:** ScummVM 本身不附带游戏。多数商业作品需自备受支持的游戏数据；官网 Freeware Games 页面另提供《钢铁天空之下》等免费完整版，与 Demos 页的有限试玩不同。先将游戏解压至独立文件夹，再在启动器中添加该文件夹；各游戏沿用自身的分发条款。

**现在能用什么:** 稳定版 2026.4.0 提供 Windows、macOS 与 Linux 下载。2026-10-19 核对时，官网下载页仍将 Android 和 iOS 包列为旧版本区的 2026.3.0。本站未运行游戏。

**代码许可:** [GPL-3.0-or-later engine code; individual game data retains its own terms](https://github.com/scummvm/scummvm/blob/7d2709da5136866589f7602f5f5a7b17de03420e/COPYING)  
**作者:** ScummVM Team  
[官方文档](https://github.com/scummvm/scummvm/blob/7d2709da5136866589f7602f5f5a7b17de03420e/README.md) · 资料核对日期: 2026-10-19

</details>

### [RigelEngine](https://github.com/lethal-guitar/RigelEngine)

《毁灭公爵 II》的原生引擎再实现，提供宽屏、更流畅的移动、快速存档和改进的手柄支持。

原作或参考对象: **毁灭公爵 II** · 引擎重实现  
[下载程序并自备游戏文件](https://github.com/lethal-guitar/RigelEngine/releases/tag/v0.9.1) · [浏览 RemakeList](https://remakelist.com/zh/remakes/rigelengine/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rigelengine-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 已发行 · 维护模式

**需要准备什么:** 需提供《毁灭公爵 II》安装数据中的 NUKEM2.CMP；完整四章需要注册版数据，shareware 仅含有限内容。NUKEM2.F1 至 NUKEM2.F5 是可选片头动画。首次启动时选择游戏数据目录。官方 README 链接试玩存档及完整游戏销售方，本站不提供原版数据。

**现在能用什么:** 官方 0.9.1 包包括 Windows x64 ZIP、macOS x64 DMG 与 Linux x64 DEB。发行说明另推荐第三方 Mac 通用构建供 Apple 芯片用户参考；README 明确标注网页版目前不可用。本站未运行。

**代码许可:** [GPL-2.0-or-later engine code; original Duke Nukem II data is separate](https://github.com/lethal-guitar/RigelEngine/blob/30afeff8f0b105eac77ee0a2fbd54b06e1a49b60/LICENSE.md)  
**作者:** Nikolai Wuttke and contributors  
[官方文档](https://github.com/lethal-guitar/RigelEngine/blob/30afeff8f0b105eac77ee0a2fbd54b06e1a49b60/README.md) · 资料核对日期: 2026-10-19

</details>

### [OpenLoco](https://github.com/OpenLoco/OpenLoco)

以 C++ 重新实现 Chris Sawyer’s Locomotion，让这款运输公司经营游戏运行于现代桌面系统。

原作或参考对象: **Chris Sawyer’s Locomotion** · 游戏重实现  
[下载程序并自备游戏文件](https://openloco.io/download/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/openloco/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openloco-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x86/x64 · Linux x64 · macOS Apple silicon

**当前阶段:** 已发行 · 需原版游戏数据

**需要准备什么:** 需自备合法持有的 Locomotion 数据，例如 Steam 或 GOG 安装文件。原版文件与应用分开放置。OpenGraphics 新增内容不取消官方原版数据要求；MIT 不涵盖商业游戏素材。

**现在能用什么:** v26.09 提供 Windows 32/64 位 ZIP、Linux x86-64 AppImage 和原生 macOS arm64 应用。Mac 下载需要 Apple silicon，尚未签名及公证。本站未运行这些版本。

**代码许可:** [MIT · engine code; original game assets are separate](https://github.com/OpenLoco/OpenLoco/blob/v26.09/LICENSE)  
**作者:** OpenLoco developers  
[官方文档](https://github.com/OpenLoco/OpenLoco/blob/v26.09/README.md) · 资料核对日期: 2026-10-19

</details>

### [The Force Engine](https://github.com/TheForceEngine/TheForceEngine)

用宽屏、现代鼠标操作和快速存档重玩《星球大战：黑暗力量》，并兼容原作社区模组。

原作或参考对象: **星球大战：黑暗力量** · 引擎重实现  
[下载程序并自备游戏文件](https://github.com/TheForceEngine/TheForceEngine/releases/tag/v1.22.420) · [浏览 RemakeList](https://remakelist.com/zh/remakes/the-force-engine/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=the-force-engine-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux · macOS 需构建

**当前阶段:** 已发行 · 支持 Dark Forces

**需要准备什么:** 自备购买的 Dark Forces 安装数据。引擎会尝试识别 Steam 与 GOG 安装；未识别时，在 Settings &gt; Game 选择游戏数据目录。引擎许可不包含商业游戏文件。

**现在能用什么:** 官方提供 1.22.420 Windows ZIP；当前 README 推荐 Linux 使用 Flathub，并提供 macOS 源码构建说明。未确认可直接安装的官方 Mac 包。

**代码许可:** [GPL-2.0 engine code; original Dark Forces assets are separate](https://github.com/TheForceEngine/TheForceEngine/blob/master/LICENSE)  
**作者:** Lucius and The Force Engine contributors  
[官方文档](https://github.com/TheForceEngine/TheForceEngine#readme) · 资料核对日期: 2026-10-19

</details>

### [OpenJazz](https://github.com/AlisterT/openjazz)

在现代桌面系统重玩初代《爵士兔》，使用自己的游戏文件或原厂 shareware 试玩数据。

原作或参考对象: **爵士兔** · 引擎重实现  
[下载程序并自备游戏文件](https://github.com/AlisterT/openjazz/releases/tag/20260301) · [浏览 RemakeList](https://remakelist.com/zh/remakes/openjazz/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openjazz-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 已发行 · 需原版或试玩数据

**需要准备什么:** 自备持有的初代 Jazz Jackrabbit 安装文件，或原厂 shareware 数据。完整游戏数据与免费引擎分开，试玩仅含有限章节。解压后的游戏文件需放在一起，再让 OpenJazz 读取所在目录。

**现在能用什么:** 20260301 发行提供 Windows x86-64 与 Linux x86-64 程序；Linux 包需要 glibc 2.35。Mac Source Ports 另行发行已签名的 Universal 2 Mac 应用，支持 Apple silicon 与 Intel。

**代码许可:** [GPL-2.0-or-later engine code; Jazz Jackrabbit data is separate](https://github.com/AlisterT/openjazz/blob/master/doc/licenses.txt)  
**作者:** AJ Thomson, Carsten Teibes and contributors  
[官方文档](https://github.com/AlisterT/openjazz#readme) · 资料核对日期: 2026-10-19

</details>

### [cnc-port](https://github.com/dk8827/cnc-port)

将《命令与征服：泰伯利亚的黎明》源码适配到现代Mac，并提供Android和iOS开发构建。游戏数据另行准备，移动端仍需区分构建成功与实机可玩。

原作或参考对象: **命令与征服：泰伯利亚的黎明** · 开源项目续作  
[自行构建并自备游戏文件](https://github.com/dk8827/cnc-port#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/cnc-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cnc-port-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** macOS · Android 调试版 · iOS 模拟器

**当前阶段:** 源码移植 · 移动端开发目标

**需要准备什么:** 需自行准备 C&amp;C Gold Windows 95 的 GDI 与 Nod 数据。作者链接历史免费发行版的社区镜像，仓库不附数据。代码许可不授予原游戏、画面或商业数据的使用权。

**现在能用什么:** 需要源码构建。作者已测试 Mac 菜单与战术游玩；另有 Android 调试 APK 和 iOS 模拟器构建说明。移动端构建或模拟器启动不等于广泛实机游玩验证。社区镜像不是 EA 托管的下载。

**代码许可:** [GPLv3 with additional EA terms. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/dk8827/cnc-port#license-and-notice)  
**作者:** dk8827  
[官方文档](https://github.com/dk8827/cnc-port#readme) · 资料核对日期: 2026-10-19

</details>

### [Generals Zero Hour for Mac, iPhone &amp; iPad](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad)

基于EA公开源码和GeneralsX，将《将军：绝命时刻》带到苹果芯片Mac、iPhone与iPad，加入即时战略触控操作。需要正版游戏文件、Mac上的构建与安装流程。

原作或参考对象: **命令与征服：将军——绝命时刻** · 开源项目续作  
[自行构建并自备游戏文件](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/generals-apple/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=generals-apple-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** 苹果芯片 Mac / iPhone / iPad

**当前阶段:** 可玩源码移植 · 需自行构建

**需要准备什么:** 需要自备零售版或 Steam 版 Zero Hour 文件、兼容的苹果芯片 Mac 与文档要求的构建工具。代码许可不授予原游戏、画面或商业数据的使用权。

**现在能用什么:** 按 Mac 源码构建指南操作；iPhone/iPad 还需要 Xcode 与苹果签名。作者报告已游玩战役和遭遇战。这是源码构建流程，并非 EA 官方移动版；游戏数据与签名是额外前提。

**代码许可:** [GPLv3 with upstream terms. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad#readme)  
**作者:** ammaarreshi  
[官方文档](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad#readme) · 资料核对日期: 2026-10-19

</details>

### [geow2](https://github.com/techknight/geow2)

使用自备 XBLA 游戏文件运行《几何战争：复古进化2》的桌面原生移植，作者记录了六种模式和本地多人支持。

原作或参考对象: **几何战争：复古进化 2** · 游戏重实现  
[下载程序并自备游戏文件](https://github.com/techknight/geow2/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/geow2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=geow2-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS 11+ / Linux x64

**当前阶段:** 已有发行包。

**需要准备什么:** 自备合法取得的文件：Xbox Live Arcade · 584108FF · v0x102 · FFmpeg。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Windows / macOS 11+ / Linux x64。已有发行包。 选择与系统匹配的官方发行包。

**代码许可:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/techknight/geow2/blob/main/LICENSE)  
**作者:** techknight  
[官方文档](https://github.com/techknight/geow2#readme) · 资料核对日期: 2026-10-19

</details>

### [NOVA Swift](https://github.com/SirStig/NovaSwift)

使用自备《逃逸速度：新星》数据的 Swift 引擎再实现，提供 Apple 平台应用和其他桌面平台的 beta。作者记录了原版行为核对，但项目仍有已知问题。

原作或参考对象: **逃逸速度：新星** · 引擎重实现  
[下载程序并自备游戏文件](https://sirstig.github.io/NovaSwift/download.html) · [浏览 RemakeList](https://remakelist.com/zh/remakes/nova-swift/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nova-swift-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** macOS / iOS / iPadOS / tvOS / Linux / Windows / Steam Deck

**当前阶段:** Beta；仍有错误和未完成的验证。

**需要准备什么:** 自备合法取得的文件：EV Nova · 原版游戏数据。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：macOS / iOS / iPadOS / tvOS / Linux / Windows / Steam Deck。Beta；仍有错误和未完成的验证。 选择与系统匹配的官方发行包。

**代码许可:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/SirStig/NovaSwift/blob/main/LICENSE)  
**作者:** SirStig  
[官方文档](https://github.com/SirStig/NovaSwift#readme) · 资料核对日期: 2026-10-19

</details>

### [PeonPad](https://github.com/chrissotraidis/peonpad)

把 Stratagus/Wargus 的《魔兽争霸2》工作流带到 iPad 的开发者预览，提供触控即时战略操作。需自行签名并复制从自有游戏提取的数据。

原作或参考对象: **魔兽争霸2：黑暗之潮** · 引擎重实现  
[下载程序并自备游戏文件](https://github.com/chrissotraidis/peonpad/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/peonpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=peonpad-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** iPadOS 16+

**当前阶段:** 开发者预览 · 未签名 IPA · 需自行签名

**需要准备什么:** 自备《魔兽争霸2》游戏文件，以及能运行 Wargus 提取工具的 Mac 或 PC，生成完整 data.Wargus 文件夹。安装已签名应用后再复制该目录。免费 IPA 不含游戏数据，也不授予暴雪内容的权利。

**现在能用什么:** 适用于 iPadOS 16+ 的开发者预览。GitHub 预发行提供不含《魔兽争霸2》数据的未签名 IPA，可自行签名安装，无需强制编译应用。在 Mac 或 PC 上用 Wargus 从自己的游戏提取数据，再把完整 data.Wargus 文件夹复制到「我的 iPad/PeonPad/data.Wargus」。目前没有应用内内容导入器、App Store 或 TestFlight 版本。

**代码许可:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/chrissotraidis/peonpad/blob/main/LICENSE)  
**作者:** chrissotraidis  
[官方文档](https://github.com/chrissotraidis/peonpad#readme) · 资料核对日期: 2026-10-19

</details>

### [Pocket Wormhole](https://github.com/adamkulik/pocket-wormhole)

基于 Project Wormhole 的 Android《FTL》引擎移植，直接读取自备 Steam/GOG 的 ftl.dat，并增加触控操作。部分界面和跨引擎存档转换仍有限制。

原作或参考对象: **FTL：超越光速** · 引擎重实现  
[下载程序并自备游戏文件](https://github.com/adamkulik/pocket-wormhole/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/pocket-wormhole/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pocket-wormhole-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Android 8+ · GLES 3.0

**当前阶段:** 可玩或实验性预览。

**需要准备什么:** 自备合法取得的文件：Steam / GOG · ftl.dat · ~280 MB。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Android 8+ · GLES 3.0。可玩或实验性预览。 跨引擎存档转换有限制，请先读指南。 选择与系统匹配的官方发行包。

**代码许可:** [GPL-2.0-or-later applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/adamkulik/pocket-wormhole/blob/main/LICENSE)  
**作者:** adamkulik  
[官方文档](https://github.com/adamkulik/pocket-wormhole#readme) · 资料核对日期: 2026-10-19

</details>

### [ra-port](https://github.com/dk8827/ra-port)

基于 EA 公开源码，将初代《红色警戒》带到 Mac、Linux 和手机的非官方移植。需要自行构建及原作数据，目前不支持联网对战。

原作或参考对象: **命令与征服：红色警戒** · 开源项目续作  
[自行构建并自备游戏文件](https://github.com/dk8827/ra-port#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/ra-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ra-port-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** macOS / Linux / Android / iOS / iPadOS

**当前阶段:** 需源码构建 · 自备原游戏

**需要准备什么:** 自备初代《红色警戒》盟军与苏军光盘数据；需源码构建，不含原作资源和成品安装程序。

**现在能用什么:** 开发版；Mac、Linux 可构建，Android／iOS 仅本地 debug；尚无联网对战。 本站未构建、安装或游玩。

**代码许可:** [GPL-3.0 with EA additional terms](https://github.com/dk8827/ra-port#readme)  
**作者:** dk8827  
[官方文档](https://github.com/dk8827/ra-port#readme) · 资料核对日期: 2026-10-19

</details>

### [Rugrats: Search for Reptar — Rust Port](https://github.com/toyz/rugrats)

用 Rust 重建 PS1《Rugrats: Search for Reptar》的原生电脑版本，读取你自己的游戏光盘。作者记录了完整关卡流程，当前安装需要源码构建。

原作或参考对象: **Rugrats：寻找 Reptar** · 游戏重实现  
[自行构建并自备游戏文件](https://github.com/toyz/rugrats#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/rugrats-rust-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rugrats-rust-port-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows

**当前阶段:** 需源码构建 · 自备原游戏

**需要准备什么:** 自备 PS1 美版 SLUS-00650 光盘，按作者文档本地提取并使用 Rust 构建；不需要 BIOS。

**现在能用什么:** 作者记录可从开头玩到结尾；当前需要源码构建，本站未运行。 本站未构建、安装或游玩。

**代码许可:** [MIT OR Apache-2.0 authored code; original game data excluded](https://github.com/toyz/rugrats#readme)  
**作者:** toyz  
[官方文档](https://github.com/toyz/rugrats#readme) · 资料核对日期: 2026-10-19

</details>

### [Rich4 Renew](https://github.com/iam567/rich4-renew-app)

面向电脑与手机的非官方《大富翁4》重制，加入高清重绘，保留地产、股票、卡片玩法，并提供派对联机。

原作或参考对象: **大富翁4** · 游戏重实现  
[下载](https://github.com/iam567/rich4-renew-app/releases/latest) · [浏览 RemakeList](https://remakelist.com/zh/remakes/rich4-renew/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rich4-renew-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Android / iOS

**当前阶段:** 公开发行 v0.6.6 · 安装与素材另有限制

**需要准备什么:** 源码运行需要作者另行提供的 rich4-assets.tar，包含原版相关素材、高清重绘、地图与音效。这些素材不适用 GPL，作者限定仅供私人使用。打包脚本会将素材装入应用，但本站未独立检查发行包内容；免费下载不代表可以自由再分发美术或原游戏素材。

**现在能用什么:** v0.6.6 提供 Windows ZIP、macOS DMG、Android APK 和未签名 iOS IPA；作者说明 Mac 支持 Intel 与 Apple Silicon。iOS 需自行签名，macOS 应用未经公证，Android APK 使用 debug 签名。未核到公开浏览器试玩；本站未安装或运行这些发行包。

**代码许可:** [GPL-3.0-or-later · code only](https://github.com/iam567/rich4-renew-app/blob/main/LICENSE)  
**作者:** iam567 (Liang)  
[官方文档](https://github.com/iam567/rich4-renew-app/blob/main/README.md) · 资料核对日期: 2026-10-20

</details>

### [Supermodel-VK](https://github.com/Igloo-Garage/Supermodel-VK)

面向世嘉 Model 3 街机游戏的 Supermodel 增强分支，加入 Vulkan 渲染、CRT 滤镜、宽屏和中英文设置界面。

原作或参考对象: **世嘉 Model 3 街机 / Supermodel** · emulator-enhancement-fork  
[下载程序并自备游戏文件](https://github.com/Igloo-Garage/Supermodel-VK/releases/latest) · [浏览 RemakeList](https://remakelist.com/zh/remakes/supermodel-vk/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=supermodel-vk-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 / Linux x86-64 / macOS 11+（Intel 与 Apple Silicon）

**当前阶段:** 公开构建 v0.9.0.3a-20261017 · v0.9.2 仅预览 · 需自备 ROM

**需要准备什么:** 不附游戏 ROM。需自行准备合法取得的世嘉 Model 3 ROM ZIP，并在启动器中选择所在目录。模拟器的 GPL 许可不涵盖游戏数据、美术或世嘉商标。Vulkan 需 1.3 驱动，或支持 dynamic rendering 与 synchronization2 的 1.2 驱动；另有 OpenGL 4.1 回退。

**现在能用什么:** v0.9.0.3a-20261017 已提供 Windows、Linux 和 macOS 通用二进制压缩包。README 展示的 v0.9.2 尚属下一版预览；封面来自该预览，不代表当前发行版已包含图中全部功能。作者对 Linux/macOS 的测试较少。macOS 未经公证，需以 ./supermodel 启动，MoltenVK 可能影响性能。本站未安装或运行模拟器。

**代码许可:** [GPL-3.0-or-later · emulator code](https://github.com/Igloo-Garage/Supermodel-VK/blob/master/Docs/LICENSE.txt)  
**作者:** Igloo-Garage · upstream: The Supermodel Team  
[官方文档](https://github.com/Igloo-Garage/Supermodel-VK/blob/master/README.md) · 资料核对日期: 2026-10-20

</details>


<a id="ports"></a>

## 移植与兼容项目

### [D2R Mobile](https://github.com/jhaizhou-ops/d2r-mobile)

想在 iPhone、iPad 或 Mac 玩 D2R Mobile？先看自备 Switch 游戏文件的要求、设备兼容性和安装顺序，再决定是否动手。

原作或参考对象: **Diablo II: Resurrected** · 平台兼容层  
[自行构建并自备游戏文件](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) · [浏览 RemakeList](https://remakelist.com/zh/remakes/d2r-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=d2r-mobile-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** iPhone / iPad / Mac · A14 / M1+

**当前阶段:** 需自行做包与自备 Switch 游戏文件

**需要准备什么:** 自己购买的 Switch 版《暗黑破坏神 II：狱火重生》本体和「术士君临」资料片，主机版本需为 1.0.34.0。工具和目录把它写作 3.3.94012。PC、PlayStation、Xbox 版文件不能替代。 从自己游戏准备出的两部分文件：程序（ExeFS）和画面、声音等资源（RomFS）。登录购买账号不等于已经有这些文件。RemakeList 不提供游戏文件、密钥或安装包。 合适的设备，以及一台处理文件的电脑。手机资源约 5.6 GB，旧设备另需约 1 GB 贴图包，还要留安装空间。免费 Apple ID 每 7 天需重新签名，不支持 iCloud 存档同步。

**现在能用什么:** 系统也要选对：iOS/iPadOS 26 及以上用标准版，18–25 用「老接口版」。Apple 芯片 Mac 的 macOS 26 及以上用标准版，15–25 用老接口版。达到 A14/M1 的芯片最低要求，不等于该型号已经实测通过。 按作者说明完成 Apple 签名；Mac/Xcode 是主路线。作者已验证 Windows 做包、再转到 Mac 签名后在手机游玩；Sideloadly/AltStore 自签以及 Linux 尚未验证。做出的包包含游戏衍生内容，仅供自己使用，不要分发。

**代码许可:** [MIT](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/LICENSE)  
**作者:** joe jiang (@happyjoejiang)  
[官方文档](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) · 资料核对日期: 2026-10-20

</details>

### [MW2 Recompiled](https://github.com/PaulCombal/mw2-recompiled)

将 Xbox 360 版 2009 年《现代战争 2》静态重编译为 Windows 与 Linux 原生程序。

原作或参考对象: **Modern Warfare 2 (2009)** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/PaulCombal/mw2-recompiled/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/mw2-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mw2-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux

**当前阶段:** 已发行 · 需原版素材

**需要准备什么:** 需自备正版 Xbox 360 光盘 ISO，美/欧版 1.0.557。启动器应用第 6 次标题更新；不包含原游戏代码或数据。

**现在能用什么:** 已发布 v0.4.1。需 64 位 Windows/Linux、Vulkan 1.2、8 GB 空间与手柄。Special Ops 未测试，不支持公开匹配；本站未运行。 仅与可信朋友联机：未改动的 2009 年网络代码存在已知安全漏洞。

**代码许可:** [GPL-3.0-only](https://github.com/PaulCombal/mw2-recompiled/blob/master/LICENSE)  
**作者:** PaulCombal  
[官方文档](https://github.com/PaulCombal/mw2-recompiled/blob/master/README.md) · 资料核对日期: 2026-10-14

</details>

### [Zelda 64: Recompiled](https://github.com/Zelda64Recomp/Zelda64Recomp)

将《梅祖拉的假面》静态重编译为原生桌面移植，加入现代控制与图形选项。

原作或参考对象: **Majora’s Mask** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/Zelda64Recomp/Zelda64Recomp/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/zelda64-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=zelda64-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux / macOS

**当前阶段:** 已发行 · 需原版素材

**需要准备什么:** 需自备北美 N64 版《梅祖拉的假面》ROM；仓库和发行包均不含游戏素材。

**现在能用什么:** 已提供 Windows、Linux、macOS 预编译 v1.2.2；需兼容图形 API。本站未运行。

**代码许可:** [GPL-3.0](https://github.com/Zelda64Recomp/Zelda64Recomp/blob/dev/COPYING)  
**作者:** Zelda64Recomp team  
[官方文档](https://github.com/Zelda64Recomp/Zelda64Recomp/blob/dev/README.md) · 资料核对日期: 2026-10-14

</details>

### [MacNativeGames · Tears of the Kingdom](https://github.com/ly05010419/MacNativeGames)

用自己的 Switch 游戏文件，在 Apple 芯片 Mac 上构建《王国之泪》Mac App 或 iPhone/iPad App。仍在实验阶段，需要本地构建，手机版还要签名。

原作或参考对象: **塞尔达传说 王国之泪** · 平台兼容层  
[自行构建并自备游戏文件](https://github.com/ly05010419/MacNativeGames#build-the-app) · [浏览 RemakeList](https://remakelist.com/zh/remakes/zelda-totk-mac-research/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=zelda-totk-mac-research-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Apple 芯片 Mac · macOS 26+；iPhone 14+ / iPad · iOS/iPadOS 26+

**当前阶段:** 实验阶段 · 本地构建与签名 · 无正式发行

**需要准备什么:** 自备自己主机导出的 Switch v1.0.0 本体（XCI/NSP）、密钥与系统文件。Mac 可另配 v1.1.2、v1.2.1 或 v1.4.3 累计更新（NSP/NSZ），iOS 只测过 v1.4.3。Mac 要 Apple 芯片、macOS 26+ 与 Metal 4，建议 16 GB 内存。本体 Mac 构建除游戏输入外约需 25 GB；无法用 APFS 克隆时还要约 17 GB，首次完整更新构建约需 40 GB。iOS 构建要完整 Xcode 26+、iOS/iPadOS 26+，手机最低为 iPhone 14；签名须保留提高内存上限的权限，全新本体构建预留 45 GB，加更新则 60 GB。生成的 App 包含原游戏内容，仅供自己使用。本站不提供游戏、密钥、固件、签名 App 或衍生着色器。

**现在能用什么:** 目前需要从源码构建，没有正式 Releases。作者报告在 M4 Mac 上测试，并在 iPhone 14 和 A16 iPad 上游玩 v1.4.3；本站没有实测。较早 Mac 缓存预热后约 90 帧的观察，不代表全流程、所有场景或稳定帧率。iPhone 14 内存占用接近 4 GB，在复杂区域出现过两次约玩 8 分钟后被 iOS 关闭。iOS 缺少着色器变体时可能不显示部分物体，Mac 新场景也可能编译卡顿。不支持联网和 amiibo。

**代码许可:** [Project code MIT · game rights and third-party licenses separate](https://github.com/ly05010419/MacNativeGames/blob/main/LICENSE)  
**作者:** Yong Li / liyong (@liyong2077)  
[官方文档](https://github.com/ly05010419/MacNativeGames/blob/b75be8cfa704df3701e86130c8ced268e79d6b11/README.md) · 资料核对日期: 2026-10-20

</details>

### [Dusklight](https://github.com/TwilitRealm/dusklight)

《黄昏公主》原生移植，提供更高分辨率、帧率选项和内置模组浏览器。

原作或参考对象: **塞尔达传说：黄昏公主** · 基于反编译的项目  
[下载程序并自备游戏文件](https://twilitrealm.dev/install/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/dusklight/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=dusklight-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux / macOS / iOS / Android

**当前阶段:** 已发行 · 需原版素材

**需要准备什么:** 需自行转储持有的 GameCube 或 Wii《黄昏公主》光盘，不支持韩版 Wii 光盘；项目不提供受版权保护的游戏素材。

**现在能用什么:** 已提供官方桌面和移动版构建；iOS 需侧载。建议使用 D3D12、Vulkan 1.1+ 或 Metal，旧图形后端的准确性与性能有限。本站未运行。

**代码许可:** [CC0-1.0 · project code; original game assets excluded](https://github.com/TwilitRealm/dusklight/blob/main/LICENSE.md)  
**作者:** Twilit Realm  
[官方文档](https://github.com/TwilitRealm/dusklight/blob/main/README.md) · 资料核对日期: 2026-10-18

</details>

### [Mega Man X4 Recompiled](https://github.com/mstan/MegaManX4Recomp)

《洛克人 X4》原生重编译，加入实验性 X 与 Zero 双人合作，支持本地及网络联机。

原作或参考对象: **洛克人 X4** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/mstan/MegaManX4Recomp/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/mega-man-x4-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mega-man-x4-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux

**当前阶段:** 合作模式 Alpha · 需原光盘

**需要准备什么:** 需自备美版 Mega Man X4（SLUS-00561）的 .cue 与 .bin 光盘镜像。内置 OpenBIOS，另行转储 BIOS 为可选；Capcom 游戏内容不在项目代码许可范围内。

**现在能用什么:** 已提供 Windows ZIP 与 Linux AppImage 公开测试版。合作模式仍为 Alpha，需 OpenGL，联机双方需同一版本；Linux 需 x86_64 与 glibc 2.38+。本站未运行。

**代码许可:** [MIT · original project code; dependencies retain their licenses](https://github.com/mstan/MegaManX4Recomp/blob/master/LICENSE)  
**作者:** Matthew Stanley  
[官方文档](https://github.com/mstan/MegaManX4Recomp/blob/master/README.md) · 资料核对日期: 2026-10-18

</details>

### [Galaxy Android](https://github.com/OpenPort-Labs/Galaxy-Android)

《超级马力欧银河》的早期安卓原生移植，加入触屏控制、手柄支持和超宽屏显示。

原作或参考对象: **超级马力欧银河** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/OpenPort-Labs/Galaxy-Android/blob/main/docs/INSTALLATION.md) · [浏览 RemakeList](https://remakelist.com/zh/remakes/galaxy-android/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=galaxy-android-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Android 11+ · ARM64

**当前阶段:** 早期发行 · 需原版素材

**需要准备什么:** 需自备合法转储的 Wii《超级马力欧银河》光盘镜像，由导入器提取本地文件。可选 Shield 来源素材属于另一套专有数据，本条目不提供。

**现在能用什么:** 已提供公开 APK；早期版本有图形、性能和崩溃反馈。封面来自贡献者的 v0.0.1 截图，并非本站测试画面。本站未运行。

**代码许可:** [GPL-3.0 · port code; original game assets excluded](https://github.com/OpenPort-Labs/Galaxy-Android/blob/main/LICENSE)  
**作者:** OpenPort Labs  
[官方文档](https://github.com/OpenPort-Labs/Galaxy-Android/blob/main/README.md) · 资料核对日期: 2026-10-18

</details>

### [Tekken 3 Recompiled](https://github.com/FishB0nes98/Tekken3Recompiled)

《铁拳 3》的 Windows 混合重编译预览版，提供宽屏、自定义服装和可选的风间准导入。

原作或参考对象: **铁拳 3** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/FishB0nes98/Tekken3Recompiled/releases/tag/v0.1.4) · [浏览 RemakeList](https://remakelist.com/zh/remakes/tekken-3-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=tekken-3-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64

**当前阶段:** 混合重编译预览 · 需自备光盘

**需要准备什么:** 需自备合法持有的美版《铁拳 3》SLUS-00402 CUE/BIN。可选的风间准还需自备非合并版 tektagt（World C1）及 tekken3（World E1）街机 ZIP；没有这些文件时可关闭 Include Jun Kazama。项目声明不附带零售游戏数据、索尼 BIOS 或已提取的角色素材，使用 OpenBIOS；代码许可不授予原游戏素材权利。

**现在能用什么:** 已发布 v0.1.4 Windows x64 简易安装预览版。首次安装需联网下载固定版本工具并在本地构建，至少需要 4 GB 工作空间。Linux 与 Steam Deck 未验证；本站未运行。

**源码可见；使用受许可限制:** [Source available under PolyForm Noncommercial 1.0.0; dependencies retain their licenses](https://github.com/FishB0nes98/Tekken3Recompiled/blob/main/LICENSE)  
**作者:** FishB0nes98  
[官方文档](https://github.com/FishB0nes98/Tekken3Recompiled/blob/main/README.md) · 资料核对日期: 2026-10-18

</details>

### [DevilutionX](https://github.com/diasurgical/DevilutionX)

让《暗黑破坏神》和《地狱火》在现代电脑与手机上运行，加入宽屏、手柄支持及可选的便利功能。

原作或参考对象: **暗黑破坏神 / 地狱火** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/diasurgical/DevilutionX/releases/tag/1.5.5) · [浏览 RemakeList](https://remakelist.com/zh/remakes/devilutionx/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=devilutionx-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Android / iOS

**当前阶段:** 已发行 · 完整游戏需自备数据

**需要准备什么:** 游玩完整《暗黑破坏神》需自备原版光盘或已购买安装中的 DIABDAT.MPQ；《地狱火》另需 hellfire.mpq、hfmonk.mpq、hfmusic.mpq 和 hfvoice.mpq。官方指南另提供 spawn.mpq 的有限试玩方式，并非完整游戏免费。中文、日文和韩文显示还需项目的 fonts.mpq。

**现在能用什么:** 官方 1.5.5 提供 Windows ZIP、macOS 通用 DMG、Linux 构建、安卓 APK 及 iOS IPA；iOS 需侧载。已核对发行文件清单和安装文档，本站未运行游戏。

**源码可见；使用受许可限制:** [Source available under Sustainable Use License 1.0; redistribution must be free of charge and non-commercial; original game assets excluded](https://github.com/diasurgical/DevilutionX/blob/0011dc9670c2093d5ab0084c1cdbeb086556563a/LICENSE.md)  
**作者:** diasurgical / DevilutionX contributors  
[官方文档](https://github.com/diasurgical/DevilutionX/blob/0011dc9670c2093d5ab0084c1cdbeb086556563a/README.md) · 资料核对日期: 2026-10-18

</details>

### [ACFA-Port](https://github.com/sulphurs16/acfa-port)

把自备的美版PS3《装甲核心：答案》文件在本机编译成Windows程序，加入鼠标、键位和显示设置。需要对应游戏文件与首次设置，不能直接下载游戏开玩。

原作或参考对象: **装甲核心：答案** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/sulphurs16/acfa-port/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/acfa-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=acfa-port-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64

**当前阶段:** 提供启动器 · 本机生成游戏程序

**需要准备什么:** 需要自备美版 PS3 BLUS30187 游戏文件、RPCS3 与索尼 PS3 4.93 系统软件；01.35 游戏更新为可选项。代码许可不授予原游戏、画面或商业数据的使用权。

**现在能用什么:** 下载作者启动器，选中自己的游戏文件，再由工具在本机生成游戏程序。启动器本身不是游戏，需要对应版本文件与首次设置。

**代码许可:** [MIT. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/SulphurS16/ACFA-Port/blob/main/LICENSE)  
**作者:** SulphurS16  
[官方文档](https://github.com/sulphurs16/acfa-port#readme) · 资料核对日期: 2026-10-19

</details>

### [AgePad](https://github.com/chrissotraidis/agepad)

把自己Steam里的Mac版《帝国时代2：决定版》带到iPad，加入触控和Apple Pencil操作。目前是限指定版本的开发预览，Steam兼容性与账号安全尚未确认。

原作或参考对象: **帝国时代2：决定版** · 平台兼容层  
[自行构建并自备游戏文件](https://github.com/chrissotraidis/agepad#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/agepad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=agepad-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** iPad · 内存 8 GB 以上

**当前阶段:** 开发预览 · 存在账号风险边界

**需要准备什么:** 需要持有 Steam Mac 版游戏、匹配的游戏与 Steam 版本、Mac、内存 8 GB 以上且可用空间 25 GB 的 iPad，以及侧载签名。代码许可不授予原游戏、画面或商业数据的使用权。

**现在能用什么:** 0.1.0 开发预览：在 Mac 上把作者的小型程序包与自己的匹配游戏及 Steam 文件组合，再签名安装。Steam 兼容性与账号安全未获确认；完整在线对局及作者 M2 iPad 以外设备尚未验证。

**代码许可:** [MIT (AgePad code). The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/agepad#credits-and-license)  
**作者:** chrissotraidis  
[官方文档](https://github.com/chrissotraidis/agepad#readme) · 资料核对日期: 2026-10-19

</details>

### [BearBirdPad](https://github.com/chrissotraidis/bearbirdpad)

基于BanjoRecomp的苹果移动端项目，提供触控、存档和本地ROM导入。需在Mac上自行构建，并准备美版1.0游戏ROM；作者已记录iPhone和iPad实机游玩。

原作或参考对象: **班卓熊大冒险** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/chrissotraidis/bearbirdpad#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/bearbirdpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=bearbirdpad-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** iPhone / iPad · iOS 16+

**当前阶段:** 开发预览 · 需自行构建

**需要准备什么:** 需要自备美版 NTSC-U 1.0 ROM、装有 Xcode 的苹果芯片 Mac 与苹果签名身份。代码许可不授予原游戏、画面或商业数据的使用权。

**现在能用什么:** 使用苹果芯片 Mac，通过 Xcode 或 PadMint 自行构建并签名。发行页提供构建配方，不提供 App。作者已在 iPhone 14 与 iPad Pro 测试；实体手柄与生命周期测试仍不完整。没有 App Store 或 TestFlight 入口。

**代码许可:** [GPL-3.0-or-later. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/bearbirdpad#legal-and-acknowledgements)  
**作者:** chrissotraidis  
[官方文档](https://github.com/chrissotraidis/bearbirdpad#readme) · 资料核对日期: 2026-10-19

</details>

### [Birdman64](https://github.com/noahvl/birdman64)

让自备美版《飞行俱乐部64》ROM在Windows或Linux原生运行，加入宽屏、手柄和可改键位。Android属于实验版本，iPhone版本需要自行构建。

原作或参考对象: **飞行俱乐部64** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/noahvl/birdman64/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/birdman64/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=birdman64-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux · Android 实验版 · iOS 自行构建

**当前阶段:** 桌面发行 · 移动端仍属实验

**需要准备什么:** 需要自备美版 Pilotwings 64 ROM，首次构建需要联网；工具不会下载 ROM。代码许可不授予原游戏、画面或商业数据的使用权。

**现在能用什么:** 桌面发行提供启动器与一次性本地设置。Android 为实验版，iPhone/iPad 需要自行构建。各移动平台的验证程度不同；不提供现成 iOS 下载包。

**代码许可:** [MIT (project code). The code license grants no rights to the original game, artwork or commercial data.](https://github.com/NoahVl/Birdman64#license)  
**作者:** NoahVl  
[官方文档](https://github.com/noahvl/birdman64#readme) · 资料核对日期: 2026-10-19

</details>

### [Chupathingy](https://github.com/ChupathingyCE/chupathingyce)

基于《光环》反编译成果的跨平台原生移植，整理联机大厅、服务器和控制体验。需要自己的Xbox版游戏地图，不能用PC地图代替核心资源。

原作或参考对象: **光环：战斗进化** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/ChupathingyCE/chupathingyce/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/chupathingy/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=chupathingy-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Android

**当前阶段:** 已有发行 · 需原 Xbox 数据

**需要准备什么:** 需要自备 Halo Combat Evolved Xbox 光盘镜像或地图；可选 PC 与 Custom Edition 地图使用独立目录。代码许可不授予原游戏、画面或商业数据的使用权。

**现在能用什么:** 作者提供 Windows、Mac、Linux 与 Android 发行版；首次设置需导入 Xbox 游戏地图。PC 地图不能代替核心 Xbox 地图。联机兼容取决于对方版本；Android 还受地图内存限制。

**代码许可:** [GPL-3.0-or-later from 0.8.0; earlier releases through 0.7.5d CC0. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/ChupathingyCE/chupathingyce#license)  
**作者:** Milenko (MrMilenko) and ChupathingyCE contributors; credits retain OpenCE and Halo decomp authors  
[官方文档](https://github.com/ChupathingyCE/chupathingyce#readme) · 资料核对日期: 2026-10-19

</details>

### [CTRPad](https://github.com/chrissotraidis/ctrpad)

基于CTR Native与CTR-ModSDK的苹果平台移植，为原版《古惑狼赛车》加入触控和本地光盘导入。需要Mac自行构建及对应美版PS1光盘镜像，并非Nitro-Fueled重制版。

原作或参考对象: **古惑狼赛车（1999）** · 基于反编译的项目  
[自行构建并自备游戏文件](https://github.com/chrissotraidis/ctrpad#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/ctrpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ctrpad-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** 苹果芯片 Mac / iPhone / iPad

**当前阶段:** 自行构建 · 已记录苹果设备游玩

**需要准备什么:** 需要自备兼容的北美 NTSC-U 单轨原始 MODE2/2352 BIN，以及苹果芯片 Mac 和文档要求的苹果构建、签名工具。代码许可不授予原游戏、画面或商业数据的使用权。

**现在能用什么:** 通过苹果芯片 Mac 上的 PadMint 自行构建。发行页提供配方，不提供可安装 App。作者已在 Mac、iPhone 14 与 iPad Pro 游玩；完整实体手柄矩阵仍未验证。没有 App Store 或 TestFlight 发行。

**代码许可:** [GPL-3.0. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/ctrpad#legal-and-acknowledgements)  
**作者:** chrissotraidis  
[官方文档](https://github.com/chrissotraidis/ctrpad#readme) · 资料核对日期: 2026-10-19

</details>

### [Def Jam: Fight for NY Recompiled](https://github.com/vyanhursky/defjamffny-recomp)

通过自备美版Xbox文件，在本机生成《Def Jam：纽约街头格斗》的Windows、Mac或Linux移植。作者提供对战实机画面，宽屏仍为测试功能，部分剧情路线已验证。

原作或参考对象: **Def Jam：纽约街头格斗** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/vyanhursky/defjamffny-recomp/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/defjam-ffny-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=defjam-ffny-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / 苹果芯片 macOS / Linux / Steam Deck

**当前阶段:** 可玩发行 · 宽屏仍为测试

**需要准备什么:** 需要自备兼容的美版初代 Xbox 光盘镜像或转储目录，PS2 与 GameCube 版本不能替代。代码许可不授予原游戏、画面或商业数据的使用权。

**现在能用什么:** 下载作者提供的 Windows、苹果芯片 Mac 或 Linux/Steam Deck 设置工具，选中自己的兼容转储文件。作者验证了对战与部分剧情路线；16:9 仍为测试功能，超宽屏为实验功能。不支持网络多人。

**代码许可:** [MIT project code; separate toolkit licenses. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/vyanhursky/defjamffny-recomp#credits-and-licensing)  
**作者:** vyanhursky  
[官方文档](https://github.com/vyanhursky/defjamffny-recomp#readme) · 资料核对日期: 2026-10-19

</details>

### [DOAXVB Native PC Port](https://github.com/norain211/doaxvb-re)

把自备美版Xbox《死或生：沙滩排球》文件转换为现代电脑上的原生程序，支持设置与本地存档。作者已记录长时间游玩，但仍列有泳池切换与画面问题。

原作或参考对象: **死或生：沙滩排球** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/norain211/doaxvb-re/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/doaxvb-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=doaxvb-native-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 可玩测试版 · 存在画面问题

**需要准备什么:** 需要自备兼容的美版 Xbox 光盘镜像或转储文件；生成的游戏内容留在自己的电脑。代码许可不授予原游戏、画面或商业数据的使用权。

**现在能用什么:** 按作者桌面设置与发行说明，使用自己的兼容美版游戏文件。作者记录了长时间游玩，仍列有泳池与渲染问题。假期结尾延续从修改过的第14天存档验证，并非全新完整流程。

**代码许可:** [GPL-3.0-or-later. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/norain211/doaxvb-re#license)  
**作者:** NoRain211  
[官方文档](https://github.com/norain211/doaxvb-re#readme) · 资料核对日期: 2026-10-19

</details>

### [Forza Horizon 1: ReImagined](https://github.com/Dyotson/ForzaHorizon1-ReImagined)

将自己的 Xbox 360《极限竞速：地平线》带到 Linux 的原生移植，附带社区在线服务与高帧率选项。Windows 路线仍待真机验证。

原作或参考对象: **极限竞速：地平线** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/dyotson/forzahorizon1-reimagined/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/forza-horizon-reimagined/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=forza-horizon-reimagined-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Linux x64 / Windows 10–11 x64

**当前阶段:** 可玩或实验性预览。

**需要准备什么:** 自备合法取得的文件：Xbox 360 · 4D5309C9 · Disc 1 / Games on Demand。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Linux x64 / Windows 10–11 x64。可玩或实验性预览。 作者报告 Linux 游玩；Windows 原生游玩尚未验证。 选择与系统匹配的官方发行包。

**代码许可:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/Dyotson/ForzaHorizon1-ReImagined/blob/main/LICENSE)  
**作者:** Dyotson  
[官方文档](https://github.com/Dyotson/ForzaHorizon1-ReImagined#readme) · 资料核对日期: 2026-10-19

</details>

### [Gears of War 2 PC Port](https://github.com/santiquiroz/gears-of-war-2-pc-port)

把自备的 Xbox 360《战争机器2》文件用于原生 PC 移植，提供高分辨率与合作模式实验。当前只验证了部分关卡，Android 仍有温升降速。

原作或参考对象: **战争机器 2** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/santiquiroz/gears-of-war-2-pc-port/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/gears-of-war-2-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gears-of-war-2-native-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10–11 x64 / Android 10+ ARM64

**当前阶段:** 可玩或实验性预览。

**需要准备什么:** 自备合法取得的文件：Xbox 360 · 4D53082D · default.xex + GearGame。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Windows 10–11 x64 / Android 10+ ARM64。可玩或实验性预览。 尚未验证完整游戏流程。 Android 仍为实验性支持。 选择与系统匹配的官方发行包。

**代码许可:** [BSD-3-Clause applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/santiquiroz/gears-of-war-2-pc-port/blob/master/LICENSE)  
**作者:** santiquiroz  
[官方文档](https://github.com/santiquiroz/gears-of-war-2-pc-port#readme) · 资料核对日期: 2026-10-19

</details>

### [GoldenEye 007 PC Port](https://github.com/jkdansereau/goldeneye-pc-port)

从自备 N64 ROM 读取素材的《黄金眼007》PC 移植，支持宽屏、鼠标和分屏。当前为 0.5.0 预正式版本。

原作或参考对象: **黄金眼 007** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/jkdansereau/goldeneye-pc-port/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/goldeneye-007-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=goldeneye-007-pc-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux / Steam Deck

**当前阶段:** 可玩或实验性预览。

**需要准备什么:** 自备合法取得的文件：Nintendo 64 · GoldenEye 007 ROM · USA。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Windows / Linux / Steam Deck。可玩或实验性预览。 PAL 和日版 ROM 支持尚未完成。 选择与系统匹配的官方发行包。

**代码许可:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/jkdansereau/goldeneye-pc-port/blob/main/LICENSE)  
**作者:** jkdansereau  
[官方文档](https://github.com/jkdansereau/goldeneye-pc-port#readme) · 资料核对日期: 2026-10-19

</details>

### [Gravity Rush 2 Native Port](https://github.com/HayatoG/gr2_pc)

面向自备 PS4 游戏文件的《重力异想世界2》PC 移植，作者在 Linux 上展示了原生运行画面。存档、开放世界和其他平台仍在验证。

原作或参考对象: **重力异想世界 2** · 平台兼容层  
[下载程序并自备游戏文件](https://github.com/hayatog/gr2_pc/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/gravity-rush-2-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gravity-rush-2-native-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Linux · Vulkan

**当前阶段:** 可玩或实验性预览。

**需要准备什么:** 自备合法取得的文件：PS4 · CUSA03694 · 01.11 · libSceNgs2.sprx。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Linux · Vulkan。可玩或实验性预览。 作者报告 Linux 游玩；Windows 原生游玩尚未验证。 存档与开放世界覆盖仍在测试。 选择与系统匹配的官方发行包。

**代码许可:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/HayatoG/gr2_pc/blob/main/port/LICENSE)  
**作者:** HayatoG  
[官方文档](https://github.com/HayatoG/gr2_pc#readme) · 资料核对日期: 2026-10-19

</details>

### [inFAMOUS Second Son Native Port](https://github.com/HayatoG/iss_pc)

使用自备 PS4 文件运行《声名狼藉：次子》的早期 PC 移植。作者展示了 Linux 上的前期章节，仍有帧率波动和画面问题。

原作或参考对象: **声名狼藉：次子** · 平台兼容层  
[下载程序并自备游戏文件](https://github.com/hayatog/iss_pc/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/infamous-second-son-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=infamous-second-son-native-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Linux · Vulkan

**当前阶段:** 可玩或实验性预览。

**需要准备什么:** 自备合法取得的文件：PS4 · CUSA00223 · 1.00 + 1.07。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Linux · Vulkan。可玩或实验性预览。 仍有帧率与画面问题。 选择与系统匹配的官方发行包。

**代码许可:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/HayatoG/iss_pc/blob/main/port/LICENSE)  
**作者:** HayatoG  
[官方文档](https://github.com/HayatoG/iss_pc#readme) · 资料核对日期: 2026-10-19

</details>

### [LAS Recomp](https://github.com/peiikai/LASRecomp)

把自备 Switch《织梦岛》1.0.0 文件在本机转换为桌面原生程序，支持宽屏和随机化选项。当前为 beta，随机化与图形仍有限制。

原作或参考对象: **塞尔达传说：织梦岛** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/peiikai/lasrecomp/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/las-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=las-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64 / macOS Apple silicon / Linux x64

**当前阶段:** Beta；仍有错误和未完成的验证。

**需要准备什么:** 自备合法取得的文件：Nintendo Switch · v1.0.0 · exefs + romfs。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Windows x64 / macOS Apple silicon / Linux x64。Beta；仍有错误和未完成的验证。 Linux ARM64 构建尚未在实机验证。 选择与系统匹配的官方发行包。

**代码许可:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/peiikai/LASRecomp/blob/main/LICENSE)  
**作者:** peiikai  
[官方文档](https://github.com/peiikai/LASRecomp#readme) · 资料核对日期: 2026-10-19

</details>

### [Lets Go Recomp](https://github.com/raulzrrs/letsgo-recomp)

使用自备《宝可梦 Let’s Go》文件的 Windows 原生移植，作者主要验证了伊布 1.0.0 的前期探索、捕捉和战斗。完整流程尚未通关验证。

原作或参考对象: **宝可梦 Let's Go！皮卡丘／Let's Go！伊布** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/raulzrrs/letsgo-recomp/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/lets-go-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=lets-go-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10–11 x64 · Vulkan 1.3 · AVX2

**当前阶段:** 可玩或实验性预览。

**需要准备什么:** 自备合法取得的文件：Nintendo Switch · exefs + romfs · Eevee 1.0.0。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Windows 10–11 x64 · Vulkan 1.3 · AVX2。可玩或实验性预览。 尚未验证完整游戏流程。 主要测试伊布 1.0.0；皮卡丘及更新版本的证据范围较小。 选择与系统匹配的官方发行包。

**代码许可:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/raulzrrs/letsgo-recomp/blob/main/LICENSE)  
**作者:** raulzrrs  
[官方文档](https://github.com/raulzrrs/letsgo-recomp#readme) · 资料核对日期: 2026-10-19

</details>

### [Muscle March Recomp](https://github.com/tmcleroy/muscle-march-recomp)

将自备 WiiWare《肌肉进行曲》带到电脑和 Android，提供摇杆、触控与键鼠操作。当前为 beta，设备和控制器测试范围仍有限。

原作或参考对象: **肌肉进行曲** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/tmcleroy/muscle-march-recomp/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/muscle-march-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=muscle-march-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10–11 / macOS 13+ Apple silicon / Linux / Android 8+ ARM64

**当前阶段:** Beta；仍有错误和未完成的验证。

**需要准备什么:** 自备合法取得的文件：WiiWare · USA WAD + 自有 Wii 通用密钥。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Windows 10–11 / macOS 13+ Apple silicon / Linux / Android 8+ ARM64。Beta；仍有错误和未完成的验证。 公开性能记录来自有限设备。 作者说明发行包含转换后的游戏代码，虽不含游戏数据文件，也不是纯空壳。 选择与系统匹配的官方发行包。

**代码许可:** [GPL-3.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/tmcleroy/muscle-march-recomp/blob/main/LICENSE)  
**作者:** tmcleroy  
[官方文档](https://github.com/tmcleroy/muscle-march-recomp#readme) · 资料核对日期: 2026-10-19

</details>

### [NSMB Wii Multiplayer Recompilation](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation)

使用自备美版 Wii 游戏文件的《新超级马力欧兄弟 Wii》原生移植，提供 Android 触控与跨手机、电脑的局域网联机。

原作或参考对象: **新超级马力欧兄弟 Wii** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/nsmb-wii-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nsmb-wii-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Android 11+ ARM64 / Windows 10–11 x64

**当前阶段:** 可玩或实验性预览。

**需要准备什么:** 自备合法取得的文件：Wii · USA SMNE01 · 修订版 1。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Android 11+ ARM64 / Windows 10–11 x64。可玩或实验性预览。 作者说明发行包含转换后的游戏代码，虽不含游戏数据文件，也不是纯空壳。 选择与系统匹配的官方发行包。

**代码许可:** [GPL-3.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation/blob/main/LICENSE)  
**作者:** WitherBlitz  
[官方文档](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation#readme) · 资料核对日期: 2026-10-19

</details>

### [OpenSA2](https://github.com/kittycache9/OpenSA2)

基于自备 2012 PC 版文件的《索尼克大冒险2》原生移植实验，已有 Windows、Linux 和 Android 早期构建。关卡覆盖仍不完整。

原作或参考对象: **索尼克大冒险 2** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/kittycache9/OpenSA2/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/opensa2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=opensa2-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux / Android

**当前阶段:** 可玩或实验性预览。

**需要准备什么:** 自备合法取得的文件：PC · Sonic Adventure 2 (2012) · 程序与素材。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Windows / Linux / Android。可玩或实验性预览。 尚未验证完整游戏流程。 选择与系统匹配的官方发行包。 官方发行包包含重新编译的游戏逻辑与移植运行环境；仍需通过安装器提供自己持有且受支持的 2012 PC 版程序和素材，不能把这些发行包称为纯空壳。

**代码许可:** [GPL-3.0-only applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/kittycache9/OpenSA2/blob/main/LICENSE)  
**作者:** kittycache9  
[官方文档](https://github.com/kittycache9/OpenSA2#readme) · 资料核对日期: 2026-10-19

</details>

### [Ottsel](https://github.com/chrissotraidis/ottsel)

基于 OpenGOAL 的《杰克与达斯特》Apple 平台移植，需要自备指定 PS2 光盘并在 Mac 上构建。当前为开发者预览，已展示 iPad 运行，尚未真机验证 iPhone。

原作或参考对象: **杰克与达斯特：先祖遗产** · 基于反编译的项目  
[自行构建并自备游戏文件](https://github.com/chrissotraidis/ottsel#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/ottsel/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ottsel-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** iPadOS 18.5+ / macOS Apple silicon

**当前阶段:** 开发者预览；需自行构建或签名。

**需要准备什么:** 自备合法取得的文件：PS2 · USA SCUS-97124 · Black Label。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：iPadOS 18.5+ / macOS Apple silicon。开发者预览；需自行构建或签名。 已有 iPad 和 Mac 运行记录，尚未实机验证 iPhone。 按官方说明在本机构建。

**代码许可:** [ISC applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/chrissotraidis/ottsel/blob/main/LICENSE)  
**作者:** chrissotraidis  
[官方文档](https://github.com/chrissotraidis/ottsel#readme) · 资料核对日期: 2026-10-19

</details>

### [Phantom Hourglass Recomp](https://github.com/dguillot-gh/phantom-hourglass-recomp)

从自备 DS 卡带文件构建的《梦幻沙漏》Windows 与 Android 移植，结合原生编译的主程序和 melonDS 硬件核心，提供多屏布局与触控选项。

原作或参考对象: **塞尔达传说：梦幻沙漏** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/dguillot-gh/phantom-hourglass-recomp#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/phantom-hourglass-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=phantom-hourglass-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Android

**当前阶段:** 可玩或实验性预览。

**需要准备什么:** 自备合法取得的文件：Nintendo DS · USA · ROM SHA-1: 4c8f52dd719918bbcd46e73a8bae8628139c1b85 / 7e0d26d143992f1eee182b24f1abb9e7f038eacf。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Windows / Android。可玩或实验性预览。 生成的应用和游戏衍生构建仅供个人使用，请勿分发。 按官方说明在本机构建。

**代码许可:** [GPL-3.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/dguillot-gh/phantom-hourglass-recomp/blob/main/LICENSE)  
**作者:** dguillot-gh  
[官方文档](https://github.com/dguillot-gh/phantom-hourglass-recomp#readme) · 资料核对日期: 2026-10-19

</details>

### [Pinyon Shift](https://github.com/arcanite24/pinyon-shift)

从自备 Xbox 360《极限竞速：地平线》构建的原生移植预览，提供桌面与 Steam Deck 路线、图像设置和可选更新包支持。Android 仍处 alpha。

原作或参考对象: **极限竞速：地平线** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/arcanite24/pinyon-shift#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/pinyon-shift/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pinyon-shift-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux / macOS Apple silicon / Android

**当前阶段:** 可玩或实验性预览。

**需要准备什么:** 自备合法取得的文件：Xbox 360 · Forza Horizon 光盘 · 可选自有 TU4/DLC。项目可免费获取，原版游戏另计；本站不提供游戏文件、密钥或可直接玩的安装包。

**现在能用什么:** 官方路线：Windows / Linux / macOS Apple silicon / Android。可玩或实验性预览。 Android 仍为实验性支持。 按官方说明在本机构建。

**代码许可:** [BSD-3-Clause applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/arcanite24/pinyon-shift/blob/main/LICENSE)  
**作者:** arcanite24  
[官方文档](https://github.com/arcanite24/pinyon-shift#readme) · 资料核对日期: 2026-10-19

</details>

### [Road Trip Recomp](https://github.com/silentsudin/RoadTripAdventure-recomp)

在电脑和 Android 上重玩《Road Trip／Choro Q HG2》，支持宽屏、存档状态和双屏地图。首次启动需选择自己的美版光盘镜像，由程序在本机完成准备。

原作或参考对象: **街头飙车王 HG2** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/silentsudin/RoadTripAdventure-recomp/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/road-trip-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=road-trip-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Android

**当前阶段:** 预览版本 · 自备原游戏

**需要准备什么:** 自备美版 SLUS-20398 光盘镜像；首次启动在本机准备游戏。Mac 还需 Apple Command Line Tools。

**现在能用什么:** 作者提供桌面和 Android 包，记录冒险与快速比赛可运行；需按设备核对要求。 本站未构建、安装或游玩。

**代码许可:** [GPL-3.0; third-party notices separate](https://github.com/silentsudin/RoadTripAdventure-recomp#readme)  
**作者:** silentsudin  
[官方文档](https://github.com/silentsudin/RoadTripAdventure-recomp#readme) · 资料核对日期: 2026-10-19

</details>

### [Silent Hill — Native PC Port](https://github.com/SlickAmogus/silent-hill-decomp)

基于 PS1《寂静岭》的反编译成果制作原生移植，提供宽屏、现代操作和可选画面增强。需自备光盘数据；Windows 为主线，其他平台仍有实验限制。

原作或参考对象: **寂静岭** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/SlickAmogus/silent-hill-decomp/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/silent-hill-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=silent-hill-native-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows

**当前阶段:** 预览版本 · 自备原游戏

**需要准备什么:** 自备 PS1《寂静岭》光盘镜像；GPL 只覆盖移植层，不授予 Konami 游戏和反编译代码权利。

**现在能用什么:** Windows 为主线；Linux／Mac 尚不稳定，移动端早期，本站未验证。 本站未构建、安装或游玩。

**代码许可:** [GPL-3.0 for port layer only; decompilation and Konami material not relicensed](https://github.com/SlickAmogus/silent-hill-decomp#readme)  
**作者:** Chris Hardin / KushAstronaut / SlickAmogus  
[官方文档](https://github.com/SlickAmogus/silent-hill-decomp#readme) · 资料核对日期: 2026-10-19

</details>

### [SpeedBreaker](https://github.com/speedbreakerproject/speedbreaker)

让 Xbox 360 版《极品飞车：最高通缉》在现代设备上原生运行，并提供宽屏与显示设置。需要自己的 Xbox 360 光盘镜像，iPhone／iPad 路线仍属实验。

原作或参考对象: **极品飞车：最高通缉** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/speedbreakerproject/speedbreaker/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/speedbreaker/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=speedbreaker-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Linux / macOS / iOS / iPadOS

**当前阶段:** 预览版本 · 自备原游戏

**需要准备什么:** 自备 Xbox 360 版《极品飞车：最高通缉》的光盘镜像，在设备上校验导入；PC 版不能直接替代。

**现在能用什么:** 桌面发行与实验性 iOS 路线；需逐个核对目标设备及发行要求。 本站未构建、安装或游玩。

**代码许可:** [GPL-3.0-or-later authored code; original game content excluded](https://github.com/speedbreakerproject/speedbreaker#readme)  
**作者:** project(u) / SpeedBreakerProject  
[官方文档](https://github.com/speedbreakerproject/speedbreaker#readme) · 资料核对日期: 2026-10-19

</details>

### [Renegade Squadron — PC](https://github.com/gtteancum/starwars-renegadesquadron-pc)

把 PSP《星球大战：前线之精英部队》移植到 Windows，支持双摇杆与更高显示分辨率。需要自己的美版游戏文件，当前仍有帧时间不均等已知问题。

原作或参考对象: **星球大战：前线之精英部队** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/gtteancum/starwars-renegadesquadron-pc/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/renegade-squadron-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=renegade-squadron-pc-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows

**当前阶段:** 预览版本 · 自备原游戏

**需要准备什么:** 自备 PSP 美版 ULUS10292 游戏，将提取的 PSP_GAME 放入 data；程序不含游戏数据。

**现在能用什么:** 作者记录地面和太空战斗；帧时间仍有不均，本站未游玩。 本站未构建、安装或游玩。

**代码许可:** [MIT for framework/port, third-party notices separate](https://github.com/gtteancum/starwars-renegadesquadron-pc#readme)  
**作者:** gtteancum  
[官方文档](https://github.com/gtteancum/starwars-renegadesquadron-pc#readme) · 资料核对日期: 2026-10-19

</details>

### [Super Mario Bros. Wonder Recomp](https://github.com/BelmanteGu/SuperMarioWonderRecomp)

将 Switch《超级马力欧兄弟 惊奇》静态重编译到桌面和 Android，提供原生 Vulkan 画面。当前需要源码构建及自备游戏、密钥和固件，兼容性仍在完善。

原作或参考对象: **超级马力欧兄弟 惊奇** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/BelmanteGu/SuperMarioWonderRecomp#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/super-mario-wonder-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=super-mario-wonder-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Android

**当前阶段:** 需源码构建 · 自备原游戏

**需要准备什么:** 自备 Switch 版 1.0.0 游戏、自己的密钥和固件，按平台源码构建；衍生 APK 和数据不可分享。

**现在能用什么:** 开发版；已记录多平台运行，存在 GPU／Windows 角色选择等问题，不保证完整流程。 本站未构建、安装或游玩。

**代码许可:** [MIT authored code; Nintendo game and derivatives excluded](https://github.com/BelmanteGu/SuperMarioWonderRecomp#readme)  
**作者:** Projeto Belmante / BelmanteGu  
[官方文档](https://github.com/BelmanteGu/SuperMarioWonderRecomp#readme) · 资料核对日期: 2026-10-19

</details>

### [Super Street Fighter II Turbo HD Remix — PC Port](https://github.com/saulob/ssf2t-hd-remix-recompiled)

让 Xbox Live Arcade 版《超级街霸 II Turbo HD Remix》在 Windows 原生运行，带有启动器和本地存档。需要指定版本的自有游戏包；不支持在线对战，Linux 路线尚未实机验证。

原作或参考对象: **超级街霸 II Turbo HD Remix** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/saulob/ssf2t-hd-remix-recompiled/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/ssf2t-hd-remix-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ssf2t-hd-remix-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows

**当前阶段:** 预览版本 · 自备原游戏

**需要准备什么:** 自备指定 Xbox Live Arcade 版本 0.0.1.3 的 STFS LIVE 包；其他版本会被拒绝。

**现在能用什么:** Windows 主线；不支持在线对战；Linux／Steam Deck 尚未实机验证。启动器许可存在未明边界。 本站未构建、安装或游玩。

**代码许可:** [GPL-2.0-only authored code; TRG launcher explicit license absent at pinned revision](https://github.com/saulob/ssf2t-hd-remix-recompiled#readme)  
**作者:** saulob  
[官方文档](https://github.com/saulob/ssf2t-hd-remix-recompiled#readme) · 资料核对日期: 2026-10-19

</details>

### [The Last Guardian — PC](https://github.com/hayatog/tlg_pc)

在 PC 上直接运行自有 PS4《最后的守护者》的非官方兼容移植，提供手柄和鼠标键盘操作。Linux 有作者运行记录，Windows 包尚未完成游戏内验证；需自备游戏及相关系统文件。

原作或参考对象: **最后的守护者** · 平台兼容层  
[下载程序并自备游戏文件](https://github.com/hayatog/tlg_pc/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/last-guardian-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=last-guardian-pc-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Linux / Windows

**当前阶段:** 预览版本 · 自备原游戏

**需要准备什么:** 自备 PS4 美版 CUSA03627 或欧版 CUSA03745 与 01.03 更新，及自己主机的音频系统文件。

**现在能用什么:** Linux 有作者实测；Windows 仅自动构建，游戏内未测；Mac 尚在计划中。 本站未构建、安装或游玩。

**代码许可:** [GPL-2.0 per port/LICENSE and README; game/firmware excluded](https://github.com/hayatog/tlg_pc#readme)  
**作者:** HayatoG  
[官方文档](https://github.com/hayatog/tlg_pc#readme) · 资料核对日期: 2026-10-19

</details>

### [Tiberian Sun Recomp](https://github.com/sp00nznet/tiberiansun-recomp)

从自有《泰伯利亚之日／火线风暴》安装生成原生程序，加入宽屏和显示设置。当前为早期可运行版本，作者检查了遭遇战及战役首关，完整流程尚未确证。

原作或参考对象: **泰伯利亚之日/火线风暴** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/sp00nznet/tiberiansun-recomp#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/tiberian-sun-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=tiberian-sun-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux

**当前阶段:** 需源码构建 · 自备原游戏

**需要准备什么:** 自备 Steam《泰伯利亚之日／火线风暴》安装；工具从本地数据生成并构建，不提供游戏文件。

**现在能用什么:** 早期可运行；作者检查遭遇战及四条战役首关，完整通关待验证；Mac 需 Wine。 本站未构建、安装或游玩。

**代码许可:** [MIT authored tooling; EA game and generated C excluded](https://github.com/sp00nznet/tiberiansun-recomp#readme)  
**作者:** sp00nznet  
[官方文档](https://github.com/sp00nznet/tiberiansun-recomp#readme) · 资料核对日期: 2026-10-19

</details>

### [Wind Waker HD Android — Plus](https://github.com/Nycolazs/WindWakerHD-Android-Plus)

在 Android 上运行自有 Wii U《风之律动 HD》的移植分支，增加葡萄牙语、触控布局和设备修复。需要自己的游戏镜像；它基于现有 Android／Enhanced 项目。

原作或参考对象: **塞尔达传说：风之律动 HD** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/Nycolazs/WindWakerHD-Android-Plus/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/wind-waker-hd-android-plus/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wind-waker-hd-android-plus-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Android

**当前阶段:** 预览版本 · 自备原游戏

**需要准备什么:** 自备 Wii U《风之律动 HD》光盘镜像和自己的密钥，或自有 WUA；生成内容留在本机。

**现在能用什么:** 提供 Android APK；基于 Android／Enhanced 分支，加入葡萄牙语、触控布局和设备修复。 本站未构建、安装或游玩。

**代码许可:** [MPL-2.0 code; translation/third-party notices separate](https://github.com/Nycolazs/WindWakerHD-Android-Plus#readme)  
**作者:** Nycolazs  
[官方文档](https://github.com/Nycolazs/WindWakerHD-Android-Plus#readme) · 资料核对日期: 2026-10-19

</details>

### [Wind Waker HD — Mods Fork](https://github.com/asadsi/wwhd-recomp-mods)

为《风之律动 HD》原生移植加入可选海上事件、可驾驶海盗船等内容的非官方分支。需自备 Wii U 游戏，联机合作仍属实验，Android 需要自行构建。

原作或参考对象: **塞尔达传说：风之律动 HD** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/asadsi/wwhd-recomp-mods/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/wind-waker-hd-mods/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wind-waker-hd-mods-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux

**当前阶段:** 预览版本 · 自备原游戏

**需要准备什么:** 自备美欧版 Wii U 游戏与所需自己的密钥，或自有 WUA；存档状态和生成代码不要分发。

**现在能用什么:** 非官方模组分支；桌面包已列出，合作联机实验性；Android 需自行构建。 本站未构建、安装或游玩。

**代码许可:** [MPL-2.0 code; Nintendo assets excluded](https://github.com/asadsi/wwhd-recomp-mods#readme)  
**作者:** AsadSi / asadsi  
[官方文档](https://github.com/asadsi/wwhd-recomp-mods#readme) · 资料核对日期: 2026-10-19

</details>

### [nxnative](https://github.com/seedds/nxnative)

在 Mac 上用自备、受支持的 Switch 游戏文件，构建 iPhone、iPad 或 Apple 芯片 Mac App。兼容性取决于游戏配置与构建版本。

原作或参考对象: **Nintendo Switch 游戏** · 平台兼容层  
[自行构建并自备游戏文件](https://github.com/seedds/nxnative#pack-an-ipa) · [浏览 RemakeList](https://remakelist.com/zh/remakes/nxnative/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nxnative-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** iPhone / iPad · iOS / iPadOS 26+；Apple 芯片 Mac · 本地构建

**当前阶段:** 需本地构建 · 兼容性为作者报告

**需要准备什么:** 自备自己持有游戏的 NSP、所需更新或 DLC，以及自己的 prod.keys，在装有 Xcode 和 Homebrew 的 Mac 上本地构建。iPhone/iPad 路线生成未签名 IPA，需另行签名和侧载；Apple 芯片 Mac 使用 Mac App 路线。生成的包包含游戏衍生代码与资源，仅供个人使用，不可再分发。本站不提供商业游戏、密钥或可直接安装的游戏包；请自行核实自备文件的使用权。

**现在能用什么:** 构建前查看作者当前游戏状态表和各游戏配置。《王国之泪》现已报告可在 iPhone 游玩；60 fps 选项要求 1.4.3 更新，不代表所有设备都能达到该帧率。Mac App 路线使用 --platform mac-app，在 Apple 芯片 Mac 上从 Finder 打开。iPhone 的运行报告不代表 Mac 兼容性已验证。

**代码许可:** [MIT project code · game rights and third-party licenses separate](https://github.com/seedds/nxnative/blob/main/LICENSE)  
**作者:** seedds and contributors  
[官方文档](https://github.com/seedds/nxnative/blob/main/README.md) · 资料核对日期: 2026-10-25

</details>

### [Zelda-Mobile · Tears of the Kingdom](https://github.com/OJZen/totk-mobile)

《王国之泪》v1.4.3 的 Apple 芯片原生移植实验。需要自备游戏并从源码构建，iPhone 上的实际游玩尚未验证。

原作或参考对象: **塞尔达传说：王国之泪** · 平台兼容层  
[自行构建并自备游戏文件](https://github.com/OJZen/totk-mobile/blob/main/docs/getting-started.md) · [浏览 RemakeList](https://remakelist.com/zh/remakes/totk-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=totk-mobile-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Apple 芯片 Mac；M1+ iPad；iPhone 15 Pro · 实验阶段

**当前阶段:** 实验阶段 · 需源码构建 · 无正式发行

**需要准备什么:** 需要从自己主机导出的 Switch 游戏本体、v1.4.3 更新包（.nsz）和匹配的 prod.keys，目前只支持这一版本。在 Apple 芯片 Mac 上准备完整 Xcode、命令行工具、Homebrew 和约 60 GB 可用空间。iPhone/iPad 另需 iOS/iPadOS 26+、开发签名、开发者模式、USB 连接和设备约 25 GB 可用空间。仓库与本站均不提供游戏文件、密钥、已签名 App 或衍生着色器包。代码许可不包含任天堂游戏内容的使用权。

**现在能用什么:** 目前是实验性源码构建，没有正式 Releases。作者报告 Apple 芯片 Mac 可以读档、运行场景，但尚未验证完整通关。M1 及以上 iPad 在原版分辨率下明显低于 60 帧，实体手柄也未完整验证。iPhone 15 Pro 仅验证开发签名安装、资源传输和缓存热启动进入标题画面；实际游玩、帧率、内存及发热都还没测。其他 iPhone（包括 iPhone 13 Pro）未经测试。首次进入新场景可能因着色器编译卡顿。

**代码许可:** [Original code: Apache-2.0 · reused components retain their own licenses](https://github.com/OJZen/totk-mobile/blob/main/LICENSE)  
**作者:** JZen (@JZennm)  
[官方文档](https://github.com/OJZen/totk-mobile/blob/510d95b8da159c0a7da467ad51b10a5a7c7ac133/README.md) · 资料核对日期: 2026-10-20

</details>

## 关于这份清单

清单由 RemakeList 已上线的资料生成。新增、修改和移除项目，都先在网站审核，再自动同步到 GitHub。项目介绍只维护一份。 [数据与同步说明](docs/data.md)

功能平替、重实现和移植是不同的项目关系。代码许可不等于原作素材许可。兼容性和性能说明来自所引资料，不表示 RemakeList 已经安装或实测。本仓库不提供游戏文件、密钥或安装包。部分项目的源码虽可见，许可仍有限制，不能据此称为开源。

可以通过 Issue 推荐项目或纠错，提交前请查看贡献说明中的来源要求。自动生成的项目数据与 README 条目统一从 RemakeList 更新。 [推荐项目](CONTRIBUTING.md)

清单原创文字采用 CC BY 4.0，生成脚本采用 MIT。各项目和第三方内容保留各自的许可，详见 LICENSE 与 NOTICE.md。

[CC BY 4.0](LICENSE) · [MIT](scripts/LICENSE) · [NOTICE](NOTICE.md)
