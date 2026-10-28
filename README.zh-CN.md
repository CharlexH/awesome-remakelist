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
- [游戏引擎与重制](#classic_games) · 30
- [移植与兼容项目](#ports) · 90

<img src="assets/overview-zh-CN.svg" alt="目录" width="920">

<a id="creative"></a>

## 设计与创作工具

### [Compositor](https://github.com/robbietilton/Compositor)

面向 Apple silicon Mac 的图层合成与后期编辑器，围绕 Photoshop 式工作流设计。

原作或参考对象: **Adobe Photoshop** · 独立功能平替  
[下载](https://github.com/robbietilton/Compositor/releases/tag/v1.5.12) · [浏览 RemakeList](https://remakelist.com/zh/remakes/compositor/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=compositor-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Apple silicon Mac · macOS 26+

**当前阶段:** v1.5.12 · Apple silicon · macOS 26+

**需要准备什么:** 无需 Photoshop；需要 Apple silicon Mac 与 macOS 26+。从源码构建还需 Xcode 26+，编辑素材的权利由用户负责。

**现在能用什么:** v1.5.12 提供 DMG，要求 Apple silicon Mac 和 macOS 26+；源码构建需 Xcode 26+。 界面仅英文。PSD/PSB 仅支持 8 位 RGB，不支持 CMYK，部分矢量和竖排文字会栅格化。本站未安装或实测。

**代码许可:** [MIT](https://github.com/robbietilton/Compositor/blob/main/LICENSE)  
**作者:** robbietilton  
[官方文档](https://github.com/robbietilton/Compositor/blob/main/README.md) · 资料核对日期: 2026-10-28

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
[下载](https://github.com/iam567/rich4-renew-app/blob/main/README.md) · [浏览 RemakeList](https://remakelist.com/zh/remakes/rich4-renew/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rich4-renew-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Android / iOS

**当前阶段:** v0.8.0 · 折叠屏适配 · 素材限制仍适用

**需要准备什么:** 源码运行需要作者另行提供的 rich4-assets.tar，包含原版相关素材、高清重绘、地图与音效。这些素材不适用 GPL，作者限定仅供私人使用。打包脚本会将素材装入应用，但本站未独立检查发行包内容；免费下载不代表可以自由再分发美术或原游戏素材。

**现在能用什么:** v0.8.0 提供 Windows ZIP、Intel／Apple silicon Mac DMG、Android APK 和未签名 iOS IPA。更新适配展开后近方形的屏幕布局，折叠时重排，并修复部分宽屏资料栏被挤出；适配检查来自作者报告。 iOS 需个人签名；桌面文档说明 Windows 未签名、Mac 未公证。本站未独立检查包内容与签名。原游戏素材及重绘不在 GPL 范围内，作者的私人使用声明不等于原权利人授权；本站未安装或试玩。

**代码许可:** [GPL-3.0-or-later · code only](https://github.com/iam567/rich4-renew-app/blob/main/LICENSE)  
**作者:** iam567 (Liang)  
[官方文档](https://github.com/iam567/rich4-renew-app/blob/main/README.md) · 资料核对日期: 2026-10-28

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

### [pokerecomp](https://github.com/Decryptu/pokerecomp)

用 Godot 重写前两代《宝可梦》，提供现代显示与操作选项；从自有且受支持的 GB／GBC ROM 读取游戏内容。

原作或参考对象: **《宝可梦》红／蓝／黄、金／银／水晶** · 游戏重实现  
[下载程序并自备游戏文件](https://github.com/Decryptu/pokerecomp/releases/tag/v0.1.86) · [浏览 RemakeList](https://remakelist.com/zh/remakes/pokerecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pokerecomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64／ARM64；Linux x64／ARM64；macOS；Android；iOS；Switch 自制软件环境

**当前阶段:** v0.1.86 · 支持第一、二代 · 需自有 ROM

**需要准备什么:** 需自备受支持且哈希匹配的红、蓝、黄、金、银或水晶 ROM 版本；引擎包不包含原版游戏。

**现在能用什么:** v0.1.86 提供桌面版本、Android APK、未签名 iOS IPA 与 Switch 自制软件包；iOS 需自行签名／侧载，Switch 需已有自制软件环境。 第三代仍为实验且不可玩，不支持的 ROM 版本会被拒绝。Apple 包不是普通 App Store 发行；macOS 为临时签名，免费 Apple 账户的 iOS 签名通常需要续签。

**代码许可:** [The rewritten engine code is MIT. Original Pokémon code, ROM content, artwork and music remain outside that license.](https://github.com/Decryptu/pokerecomp/blob/main/LICENSE)  
**作者:** Decryptu  
[官方文档](https://github.com/Decryptu/pokerecomp/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Streetball Revival](https://github.com/luckvj/streetball-revival)

用 Rust 重写《NBA 街头篮球 2》，提供桌面操作与实验性联网；从自有受支持的美版 PS2 光盘读取内容。

原作或参考对象: **《NBA 街头篮球 2》PS2 版** · 游戏重实现  
[下载程序并自备游戏文件](https://github.com/luckvj/streetball-revival/releases/tag/v0.1.4-beta) · [浏览 RemakeList](https://remakelist.com/zh/remakes/streetball-revival/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=streetball-revival-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows；Linux

**当前阶段:** v0.1.4-beta · Windows／Linux · 联网为实验功能

**需要准备什么:** 需自备美版 PS2《NBA Street Vol. 2》ISO，编号 SLUS-20651，且符合项目指定哈希；引擎下载不包含原作数据。

**现在能用什么:** v0.1.4-beta 提供 Windows 安装器／压缩包与 Linux 压缩包；联网仍在开发，需要更多玩家验证。 玩法还原尚不完整，电脑队伍行为、渲染和 Gamebreaker 镜头细节可能不同；作者对照表只衡量选定行为，不是完整游戏还原百分比。

**代码许可:** [The rewritten engine is MIT. The license does not include EA’s original game data, artwork or music.](https://github.com/luckvj/streetball-revival/blob/main/LICENSE)  
**作者:** luckvj  
[官方文档](https://github.com/luckvj/streetball-revival/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Torchlight Rekindled](https://github.com/GreenSwampDweller/torchlight-rekindled)

面向掌机和电脑的《火炬之光》引擎，沿用 Xbox 360 版偏重手柄的游戏逻辑，读取自有 PC 或 Xbox 360 游戏数据。

原作或参考对象: **火炬之光** · 引擎重实现  
[下载程序并自备游戏文件](https://github.com/GreenSwampDweller/torchlight-rekindled/releases/tag/1.0.2) · [浏览 RemakeList](https://remakelist.com/zh/remakes/torchlight-rekindled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=torchlight-rekindled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Switch homebrew / Android 12+ arm64 / iOS / Windows / Linux

**当前阶段:** 已有下载 · 自备原游戏

**需要准备什么:** 自备购买的完整 PC 或 Xbox 360 游戏中的 pak.zip／Pak.zip 和 music 目录；PC 数据使用项目提供的备用主机式界面。项目声明不分发游戏数据。

**现在能用什么:** 1.0.2 提供 Switch NRO、Android APK、Windows／Linux x64 压缩包和未签名 iOS IPA。Switch 需要 homebrew；Android 要求 arm64、Android 12+，并申请所选游戏目录的文件访问权限。iOS 包未签名，需要自行签名。桌面测试限作者连接手柄的笔记本，未核实 Steam Deck。1.0.2 发行页同时列有旧 1.0.1 IPA，应选择明确标注 1.0.2 的文件。本站未安装或试玩。

**代码许可:** [GPL-3.0 for the engine; game data and third-party components retain separate rights](https://github.com/GreenSwampDweller/torchlight-rekindled/blob/main/LICENSE)  
**作者:** GreenSwampDweller  
[官方文档](https://github.com/GreenSwampDweller/torchlight-rekindled/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [ZQuest Classic](https://github.com/ZQuestClassic/ZQuestClassic)

用于初代 NES《塞尔达传说》风格冒险的免费引擎、任务播放器与编辑器，可以游玩社区任务或制作自己的作品。

原作或参考对象: **塞尔达传说／塞尔达风格冒险** · 引擎重实现  
[下载](https://zquestclassic.com/releases/) · [浏览 RemakeList](https://remakelist.com/zh/remakes/zquest-classic/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=zquest-classic-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / macOS / Linux / Web (experimental)

**当前阶段:** 稳定桌面发行 · 实验性网页播放器

**需要准备什么:** 引擎与播放器使用任务文件，可从作者处取得或自行制作。引擎 GPL 许可不授予任天堂名称、图像或第三方任务素材的权利；各任务条款需分别遵守。

**现在能用什么:** 稳定版 2.55.17 提供 Windows x64／x86、macOS 与 Linux 下载，官网另有实验性网页播放器。本条选择稳定版 2.55.17，3.0 预发行是另一条版本线。网页版本及其移动端体验仍属实验性。任务兼容性和素材条款依作者与引擎版本而异。本站只核验文档与发行信息，未安装或试玩任务。

**代码许可:** [GPL-3.0 for the engine; individual quests and their media have separate rights](https://github.com/ZQuestClassic/ZQuestClassic/blob/main/LICENSE)  
**作者:** ZQuestClassic  
[官方文档](https://github.com/ZQuestClassic/ZQuestClassic/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>


<a id="ports"></a>

## 移植与兼容项目

### [D2R Mobile](https://github.com/jhaizhou-ops/d2r-mobile)

将自备 Switch 版《暗黑破坏神 II：狱火重生》与「术士君临」资料片带到 Apple 设备、Android 和 HarmonyOS 的兼容层；需按平台准备自己的游戏文件。

原作或参考对象: **Diablo II: Resurrected** · 平台兼容层  
[自行构建并自备游戏文件](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) · [浏览 RemakeList](https://remakelist.com/zh/remakes/d2r-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=d2r-mobile-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** iPhone / iPad / Apple silicon Mac / Android ARM64 / HarmonyOS NEXT

**当前阶段:** v2.1.0 · 自备 Switch 文件 · 可选实验镜头

**需要准备什么:** 需自备合法购买的 Switch 本体与「术士君临」资料片，更新至主机版本 1.0.34.0（工具标作 3.3.94012）的 ExeFS、RomFS。其他主机或 PC 文件不能替代；资源约 5.6 GB，旧 Apple 芯片另需从自己的文件生成约 1 GB 贴图包。Apple 最低 A14/M1；iOS 26+ 与 18–25、macOS 26+ 与 15–25 分别选标准／老接口路线。Android 需 ARM64、Android 12+、Vulkan 1.1；HarmonyOS NEXT 需开发者账号、签名工具与自制运行包。

**现在能用什么:** v2.1.0 更新 Android APK 与两份 iOS 构建输入 ZIP。Android 沿用既有导入包和存档；iOS 需用新输入与 v2.1.0 源码重新做包、签名。未签名 HarmonyOS HAP 仍是 v2.0.0 文件，需个人开发者签名和运行包；Mac 仍需源码构建。 仅离线。Android 仍有未完成的触控细节和特定设备图形问题。4 GB Apple 设备内存紧张；侧载工具签名与 Linux 做包仍未验证。免费 Apple ID 每 7 天需重签且无 iCloud 同步。Apple TV 仅到选角色预览；含游戏内容的自制包不可分发。本站未构建、安装或试玩。

**代码许可:** [MIT covers project code; original game files and third-party components retain separate rights and licenses.](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/LICENSE)  
**作者:** joe jiang (@happyjoejiang)  
[官方文档](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [MW2 Recompiled](https://github.com/PaulCombal/mw2-recompiled)

将 Xbox 360 版 2009 年《现代战争 2》静态重编译为 Windows 与 Linux 原生程序。

原作或参考对象: **Modern Warfare 2 (2009)** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/PaulCombal/mw2-recompiled/releases/tag/v0.8.1) · [浏览 RemakeList](https://remakelist.com/zh/remakes/mw2-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mw2-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux x64 · SSE4.2 · Vulkan 1.2

**当前阶段:** 稳定版 v0.8.1 · 另有 v0.8.2 预发布

**需要准备什么:** 需自备合法取得的 Xbox 360 美／欧版 1.0.557 光盘 ISO；启动器校验并下载应用 Title Update 6。需 x64 SSE4.2 处理器、Vulkan 1.2、约 8 GB 空间和手柄，键盘仅覆盖菜单。PC 自定义地图的实验导入另需自己的 PC 游戏素材。

**现在能用什么:** 主入口保留 Windows／Linux 稳定版 v0.8.1，v0.8.2 另列为预发布。通过 mw2-launcher 导入自备的指定 ISO，选普通平台包；同版 -steam／-lan 附件只是兼容旧启动器的重复包。 不支持公开匹配或排名玩法，自定义地图仍为 Beta。其他 Steam 用户可发现 SYSTEM LINK，同中继或 LAN 用户也可能接触游戏；仅与可信朋友使用同一版本。作者报告网络漏洞修复，本站未独立安全审计、安装或试玩。

**代码许可:** [GPL-3.0-only](https://github.com/PaulCombal/mw2-recompiled/blob/master/LICENSE)  
**作者:** PaulCombal  
[官方文档](https://github.com/PaulCombal/mw2-recompiled/blob/master/README.md) · 资料核对日期: 2026-10-28

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

《洛克人 X4》原生重编译，加入 X 与 Zero 双人合作，支持本地和网络联机；当前为公开 Beta。

原作或参考对象: **洛克人 X4** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/mstan/MegaManX4Recomp/releases/tag/v1.0.14) · [浏览 RemakeList](https://remakelist.com/zh/remakes/mega-man-x4-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mega-man-x4-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64 / Linux x86-64 (glibc 2.38+)

**当前阶段:** 公开 Beta · 双人合作 · 需原光盘

**需要准备什么:** 需自备原始、未修改的美版 Mega Man X4（SLUS-00561）.cue 与 .bin 光盘镜像，即使关闭全部 mod 也须使用该版本。修改盘、undub 与重新翻译盘不受支持；内置 OpenBIOS，另行转储 BIOS 为可选。原作内容不在 MIT 许可范围内。

**现在能用什么:** v1.0.14 提供 Windows x64 ZIP 与 Linux x86-64 AppImage，优化合作模式渲染；作者公布的提速来自特定 Boss 场景，不代表全游戏表现。合作模式需 OpenGL，联机各方须更新至同版；原有原生记忆卡存档可沿用。 仍为公开 Beta：独立镜头可能减速，在线登录与启动问题仍在调查。Linux 需 glibc 2.38+；四人合作实验为独立版本。本站未安装或试玩。

**代码许可:** [MIT · original project code; dependencies retain their licenses](https://github.com/mstan/MegaManX4Recomp/blob/master/LICENSE)  
**作者:** Matthew Stanley  
[官方文档](https://github.com/mstan/MegaManX4Recomp/blob/master/README.md) · 资料核对日期: 2026-10-28

</details>

### [Galaxy Android](https://github.com/OpenPort-Labs/Galaxy-Android)

《超级马力欧银河》的早期安卓原生移植，加入触屏控制、手柄支持和超宽屏显示。

原作或参考对象: **超级马力欧银河** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/OpenPort-Labs/Galaxy-Android/releases/tag/v0.0.4b) · [浏览 RemakeList](https://remakelist.com/zh/remakes/galaxy-android/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=galaxy-android-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Android 11+ · ARM64 · Vulkan 1.0

**当前阶段:** v0.0.4b · 测试侧载包 · 升级前备份存档

**需要准备什么:** 自备合法转储的 Wii《超级马力欧银河》光盘镜像（.rvz、.wbfs、.iso 或 .wia），由导入器在本地提取和转换；预留约 2.5 GB（不含影片）或 5 GB（含影片）存储。可选 Shield 来源素材另属专有数据，本条目不提供。

**现在能用什么:** v0.0.4b 提供 GalaxyAndroid.apk，要求 Android 11+ ARM64、Vulkan 1.0 和至少 3 GB 内存，无 OpenGL 回退。 这是可调试的测试侧载包，不是商店包。签名证书已更换，GitHub v0.0.4／4a 不能覆盖升级；卸载会删除应用私有数据，需先备份存档，共享 GalaxyData 目录另计。作者此次没有连接手机／头显验证，联机认证及正式签名密钥轮换仍待处理。本站未安装或实测。

**代码许可:** [GPL-3.0 · port code; original game assets excluded](https://github.com/OpenPort-Labs/Galaxy-Android/blob/main/LICENSE)  
**作者:** OpenPort Labs  
[官方文档](https://github.com/OpenPort-Labs/Galaxy-Android/blob/main/README.md) · 资料核对日期: 2026-10-28

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

基于 CTR Native 与 CTR-ModSDK 的苹果平台移植，为原版《古惑狼赛车》加入触控和本地光盘导入。通过 Mac 上的 PadMint 构建个人 App，iPhone／iPad 也可使用其 GitHub Cloud Build。

原作或参考对象: **古惑狼赛车（1999）** · 基于反编译的项目  
[自行构建并自备游戏文件](https://github.com/chrissotraidis/ctrpad#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/ctrpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ctrpad-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Apple Silicon Mac（macOS 11+）／iPhone／iPad（iOS／iPadOS 15+）

**当前阶段:** v0.2.4 · 个人构建 · 仅发行配方

**需要准备什么:** 导入自备的兼容 NTSC-U SCUS944.26 单轨原始 MODE2／2352 BIN，内容需从第 0 字节开始。选择 BIN 而非 CUE；不支持 cooked ISO、CHD 或压缩包。本地 Apple 构建需文档指定的构建／签名工具，iPhone／iPad 云构建需按其签名流程操作。代码许可不覆盖原作数据或美术。

**现在能用什么:** v0.2.4 修复 iPad 横屏启动与触控布局。发行页只有 PadMint 配方和校验和，没有 App。可用 Apple Silicon Mac 构建，iPhone／iPad 也可经 PadMint 的 GitHub Cloud Build 在没有 Mac 时构建；安装后本地导入自备的指定 BIN。 个人构建须保持私有，没有 App Store／TestFlight 发行。作者记录了 Mac／iPhone／iPad 游玩和 iPad 真机修复检查，更广泛游玩、手柄与本地多人覆盖仍不完整；本站未安装或试玩。

**代码许可:** [GPL-3.0. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/ctrpad/blob/main/LICENSE)  
**作者:** chrissotraidis  
[官方文档](https://github.com/chrissotraidis/ctrpad#readme) · 资料核对日期: 2026-10-28

</details>

### [Def Jam: Fight for NY Recompiled](https://github.com/vyanhursky/DefJamFFNY-recomp)

通过自备美版初代 Xbox 转储，在本机生成《Def Jam：纽约街头格斗》的 Windows、Mac 或 Linux 原生移植，加入高分辨率与最多四人本地对战；宽屏仍为测试功能。

原作或参考对象: **Def Jam：纽约街头格斗** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/vyanhursky/DefJamFFNY-recomp/releases/tag/v0.12.2) · [浏览 RemakeList](https://remakelist.com/zh/remakes/defjam-ffny-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=defjam-ffny-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64（Direct3D 11）/ Apple 芯片 macOS / Linux x86-64 / Steam Deck

**当前阶段:** 公开发行 v0.12.2 · 本机构建 · 宽屏 Beta

**需要准备什么:** 需要自备与作者清单匹配的美版初代 Xbox 光盘镜像或转储目录，PS2 与 GameCube 版本不能替代。设置工具在本机核验、重编译和构建，生成高清贴图另需时间与磁盘空间；代码许可不授予原游戏或画面的权利。

**现在能用什么:** v0.12.2 提供 Windows x64、Apple silicon macOS 与 Linux x86-64 设置工具，改善故事模式 Power Plant 场景的帧节奏，并修复标题菜单画面问题。设置程序校验自备转储并在本机构建；已有安装需 Clean Update 后重新构建，保留存档、设置、mod 与材质。 16:9／16:10 宽屏仍为 Beta，更宽比例属实验功能，多人仅限本地。商店停顿、部分帧节奏和宽屏问题，以及 Steam Deck 音频与教学关性能仍待解决。macOS 未签名，Proton 未测试；本站未安装或试玩。

**代码许可:** [MIT project code; separate toolkit licenses. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/vyanhursky/DefJamFFNY-recomp#credits-and-licensing)  
**作者:** vyanhursky  
[官方文档](https://github.com/vyanhursky/DefJamFFNY-recomp#readme) · 资料核对日期: 2026-10-28

</details>

### [DOAXVB Native PC Port](https://github.com/norain211/doaxvb-re)

从自备美版 Xbox 光盘在本机构建的《死或生：沙滩排球》非官方原生移植。推荐版 v0.6.0 beta 提供新启动器与桌面包，仍有渲染问题。

原作或参考对象: **死或生：沙滩排球** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/NoRain211/doaxvb-re/releases/tag/v0.6.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/doaxvb-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=doaxvb-native-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 / macOS Apple silicon·Intel / Linux x86-64·Steam Deck

**当前阶段:** 推荐 v0.6.0 beta · 本机编译 · 测试未完整

**需要准备什么:** 自备受支持美版 Xbox 光盘映像，安装流程在本机校验并生成游戏代码。Mac／Linux 还需文档规定的构建工具；Steam Deck 通过含编译器的容器构建。生成的游戏内容与原版美术不在项目 GPL-3.0-or-later 授权范围内。

**现在能用什么:** v0.6.0 已替代 v0.5.3 成为作者推荐的 beta，提供 Windows、Mac、Linux ZIP。均需从自备光盘构建；配方已变，需解压到新目录重新构建，再复制旧 private 存档。Windows 现在下载 llvm-mingw，不再要求 Visual Studio。 作者尚未完整试玩 v0.6.0。记录了 Windows／Linux ZIP 构建检查，但未在 Mac 上构建 Mac ZIP；启动器手柄仅用虚拟手柄检查。岸边闪烁和泳池切换问题仍存；Mac／Linux 缺少部分雾效、光照和阴影，发行版的光追 GI 开关无效果。本站未构建或试玩。

**代码许可:** [GPL-3.0-or-later. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/norain211/doaxvb-re#license)  
**作者:** NoRain211  
[官方文档](https://github.com/norain211/doaxvb-re#readme) · 资料核对日期: 2026-10-28

</details>

### [Forza Horizon 1: ReImagined](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined)

将自备 Xbox 360《极限竞速：地平线》文件在本机构建为 Windows 与 Linux 原生移植，加入社区在线服务、车辆调校和显示选项。

原作或参考对象: **极限竞速：地平线** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined/releases/tag/v0.2.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/forza-horizon-reimagined/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=forza-horizon-reimagined-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 / Linux x86-64；macOS 仅源码实验

**当前阶段:** v0.2.0 已发行 · 本机构建 · VR 实验性

**需要准备什么:** 需自备合法取得的 Xbox 360《极限竞速：地平线》光盘映像、Games on Demand 包或已提取目录。Title Update 4 与 DLC 另行自备；Horizon Rally 和 1000 Club 需要 TU4。运行约需 4 GB 可用内存和 15 GB 磁盘，Vulkan 路线需 Vulkan 1.3；Windows 另有 Direct3D 12。首次构建需下载或安装编译工具。

**现在能用什么:** v0.2.0 提供 Windows 安装器、Linux x86-64 归档和 Flatpak。启动器从自备游戏文件在本机生成、编译游戏；更新后需重新构建一次。macOS 仅有源码实验路线，没有 Mac 发行包。 Steam Deck 与低端设备仍有明显性能限制，部分 GPU 有画面或崩溃问题。VR 仅有作者的 Quest 3 + Linux WiVRn 测试，Windows VR 未测；macOS 的完整比赛、存档重载和实体手柄仍待验证。TU4 与基础版不共用联机房间，TU4 存档不能直接回退基础版。本站未构建或试玩。

**代码许可:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined/blob/main/LICENSE)  
**作者:** Dyotson  
[官方文档](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined#readme) · 资料核对日期: 2026-10-27

</details>

### [Gears of War 2 PC Port](https://github.com/santiquiroz/gears-of-war-2-pc-port)

使用自备 Xbox 360《战争机器 2》文件的非官方原生移植，提供高分辨率、分屏和 System Link 合作玩法；Android 仍为实验性支持，完整战役尚未验完。

原作或参考对象: **战争机器 2** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/santiquiroz/gears-of-war-2-pc-port/releases/tag/v0.3.7) · [浏览 RemakeList](https://remakelist.com/zh/remakes/gears-of-war-2-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gears-of-war-2-native-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64（DirectX 12）/ Android 10+ ARM64（Vulkan，实验性）

**当前阶段:** 公开发行 · 战役验证未完 · Android 实验性

**需要准备什么:** 自备合法取得的零售版 Xbox 360《战争机器 2》（Title ID 4D53082D）ISO，或含 default.xex 与 GearGame 的完整目录。Windows 首次提取 ISO 约需 8 GB 空间；Android 导入会复制到应用存储，需额外容纳一份完整游戏。本站不提供原游戏数据。

**现在能用什么:** v0.3.7 提供 Windows 10/11 x64 ZIP 和实验性 Android 10+ ARM64 APK。Windows 需要 DirectX 12 显卡，Android 需要 Vulkan；更新包括独立语音与字幕语言选择。 作者只完整游玩过第一幕，短时间章节扫描不等于第二至五幕通关验证。Android 持续性能受温升影响；三至四人合作和互联网联机仍有未测场景，同场玩家须用同版。Windows 文件未签名，可能被系统阻止；作者扫描声明不是本站安全认证。本站未构建、安装或运行。

**代码许可:** [BSD-3-Clause applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/santiquiroz/gears-of-war-2-pc-port/blob/master/LICENSE)  
**作者:** santiquiroz  
[官方文档](https://github.com/santiquiroz/gears-of-war-2-pc-port#readme) · 资料核对日期: 2026-10-27

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

使用自备 PS4 文件的《声名狼藉：次子》非官方 PC 兼容移植，提供 Linux 与 Windows 包。作者记录了早期章节游玩，性能和画面问题仍存。

原作或参考对象: **声名狼藉：次子** · 平台兼容层  
[下载程序并自备游戏文件](https://github.com/HayatoG/iss_pc/releases/tag/v1.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/infamous-second-son-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=infamous-second-son-native-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Linux x86-64 / Windows 10（1903+）–11 x64 · Vulkan 1.3

**当前阶段:** 稳定版 v1.0 · 可选 beta-rc1 · 自备 PS4 文件

**需要准备什么:** 需自备 PS4 美版 CUSA00223 的解密基础版 1.00 与 1.07 更新，合并后约 33 GB。需 AVX、Vulkan 1.3，建议 6 GB 显存；音频不再需要主机固件文件，发行包不含游戏文件。

**现在能用什么:** 推荐稳定下载仍为 v1.0，提供 Linux x86-64（glibc 2.39+）和 Windows 10/11 x64 包；beta-rc1 是同平台的独立预发布，不替代稳定版。 帧率和画面仍不稳定，Windows RX 580／Polaris 兼容路线属实验。beta-rc1 列出超分时地面可能发黑、3 倍 FSR 偏糊及 Linux 超分未经测试；启动器不会把 beta 当普通更新推送。本站未安装或试玩任一构建。

**代码许可:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/HayatoG/iss_pc/blob/main/port/LICENSE)  
**作者:** HayatoG  
[官方文档](https://github.com/HayatoG/iss_pc#readme) · 资料核对日期: 2026-10-28

</details>

### [LAS Recomp](https://github.com/peiikai/LASRecomp)

把自备 Switch《织梦岛》1.0.0、1.0.1 或 1.1.0 文件在本机转换为桌面原生程序，加入宽屏与随机化选项；仍为 beta。

原作或参考对象: **塞尔达传说：织梦岛** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/peiikai/LASRecomp/releases/tag/beta_5.3) · [浏览 RemakeList](https://remakelist.com/zh/remakes/las-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=las-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64 / macOS Apple silicon / Linux x64；Linux ARM64 实验性

**当前阶段:** beta_5.3 · 仍有错误与未完成验证

**需要准备什么:** 需自备合法取得的 Switch《织梦岛》1.0.0、1.0.1 或 1.1.0 的 exefs、romfs 文件，选择其所在目录进行本地构建。Mac 需 Apple silicon、macOS 15+；Windows 10/11 与 Linux x64 需 AVX2、FMA、Vulkan 1.3，至少 8 GB RAM 和约 12 GB 设置空间。项目不提供游戏文件或密钥。

**现在能用什么:** 常规下载仍是 beta_5.3，提供 Windows、Apple silicon Mac 和 Linux 包。较新的 test-413-deck、test-452-owl、test-356-haze-2 预发布用于特定问题反馈，并非新的通用版本。test-413-deck 针对 Steam Deck 阴影条纹／闪烁，沿用常规数据目录；参与该测试时再选。 仍可能崩溃、生成无法通关的种子或出现宽屏画面问题，地牢房间打乱尤属实验功能。Linux ARM64 未在真机测试，不支持 Intel Mac 和较旧 Intel 核显；Beta 5 之前的种子编号会生成不同结果。本站未构建或试玩。

**代码许可:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/peiikai/LASRecomp/blob/main/LICENSE)  
**作者:** peiikai  
[官方文档](https://github.com/peiikai/LASRecomp#readme) · 资料核对日期: 2026-10-28

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
[自行构建并自备游戏文件](https://github.com/arcanite24/pinyon-shift/releases/tag/v0.7.1) · [浏览 RemakeList](https://remakelist.com/zh/remakes/pinyon-shift/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pinyon-shift-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64 / Linux x86-64·SteamOS / macOS 13+ Apple silicon / Android 13+ 测试版

**当前阶段:** v0.7.1 · 本机编译 · Android alpha

**需要准备什么:** 需自备美版零售 Xbox 360《极限竞速：地平线》光盘（MS-2505，标题 ID 4D5309C9）或受支持的未修改提取目录，TU4／DLC 另行自备。作者估计首次编译需 20–60 分钟和约 30 GB 空间。桌面图形需 Vulkan 1.3；Android alpha 需 Android 13+、Vulkan 1.3，主要面向骁龙 8 Gen 2 及以上、8 GB 内存设备。

**现在能用什么:** v0.7.1 提供 Windows、Linux x86-64 与 Apple silicon Mac 启动器，均从自备文件在本机编译；更新会重建游戏并保留存档、设置及 DLC。Android 没有可直接下载的发行 APK，需在电脑启动器中生成后传到设备。 仍有画面问题和降速。AMD／Intel PC GPU 尚未完成适配验证，Linux／Mac 的 v4 仅测了脚本路线。Android 为 alpha，非高通 GPU 需主动开启实验路线。DLSS 仅 Windows；蓝牙或非 Windows 的 DualSense 未测。社区 UDLC 仅验证少量车辆，内容权利另计。本站未构建或试玩。

**代码许可:** [BSD-3-Clause applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/arcanite24/pinyon-shift/blob/main/LICENSE)  
**作者:** arcanite24  
[官方文档](https://github.com/arcanite24/pinyon-shift#readme) · 资料核对日期: 2026-10-28

</details>

### [Red Alert 2 Recomp](https://github.com/sp00nznet/redalert2-recomp)

通过安装器在本机从自备《红色警戒 2／尤里的复仇》文件生成原生版本，加入宽屏和现代显示选项。它与 OpenRA、RA2WEB、Vanguard 是不同项目。

原作或参考对象: **红色警戒 2/尤里复仇** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/sp00nznet/redalert2-recomp/releases/tag/v0.1.3) · [浏览 RemakeList](https://remakelist.com/zh/remakes/redalert2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=redalert2-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64 / Linux x64 / macOS ARM64

**当前阶段:** 提供安装器 · 本机构建 · 自备原游戏

**需要准备什么:** 自备 Steam／EA App（Origin）的《红色警戒 2／尤里的复仇》安装目录，包含 game.exe 1.006 与 gamemd.exe 1.001。安装器识别文件后在本机生成与构建，可能需要安装构建工具；生成的原作代码和数据保留在本地。

**现在能用什么:** v0.1.3 提供 Windows x64、Linux x64 与 macOS ARM64 安装器，使用自备原版文件在本机生成与构建。此版修复部分 Windows 启动失败，以及 Linux/macOS 退出后进程残留；作者估计首次构建需 30–60 分钟和约 6 GB 空间。 安装器尚未签名，系统可能阻止启动；它需要本机构建，不含原版游戏文件。作者脚本检查覆盖菜单、遭遇战和战役入口，不代表本站验证完整通关。MIT 仅覆盖项目自身代码，EA 原游戏代码与素材权利另计。本站未构建、安装或运行。

**代码许可:** [MIT for project-authored tooling only; EA game code and assets retain separate rights.](https://github.com/sp00nznet/redalert2-recomp/blob/main/LICENSE)  
**作者:** sp00nznet  
[官方文档](https://github.com/sp00nznet/redalert2-recomp#readme) · 资料核对日期: 2026-10-27

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

### [Rogue Squadron 64 Recomp](https://github.com/MikeSemicolonD/RogueSquadron64Recomp)

将 N64《星球大战：侠盗中队》静态重编译到现代设备，加入宽屏与鼠标、手柄和飞行摇杆支持。需要自备指定美版 ROM；Mac 目前只有编译记录。

原作或参考对象: **星球大战：侠盗中队** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/MikeSemicolonD/RogueSquadron64Recomp#readme) · [浏览 RemakeList](https://remakelist.com/zh/remakes/rogue-squadron64-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rogue-squadron64-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux / Android

**当前阶段:** 需源码构建 · 自备原游戏

**需要准备什么:** 自备 N64 美版 1.0 的 16 MB ROM；Mac 只有编译记录，尚无运行验证。

**现在能用什么:** 有 Windows、Linux 与 Android 源码构建文档，作者报告可完整游玩。未列出发行附件，需按文档从源码构建并自备美版 1.0 ROM。作者称可从头玩到结尾，但实验性光追、插值与多人仍有限制。macOS 只有编译记录，未在 Mac 运行；Linux x86 仅在 64 位电脑的软件 Vulkan 上测试。GPL-3.0 覆盖项目自有宿主／模组／工具代码，不覆盖原游戏权利。本站未构建或试玩。

**代码许可:** [GPL-3.0 for host runtime, patches, hooks, mods, tools and docs; ROM-derived code and game assets are separate](https://github.com/MikeSemicolonD/RogueSquadron64Recomp/blob/main/LICENSE)  
**作者:** MikeSemicolonD  
[官方文档](https://github.com/MikeSemicolonD/RogueSquadron64Recomp#readme) · 资料核对日期: 2026-10-28

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

让自备 Xbox 360 版《极品飞车：最高通缉》在现代设备上运行，提供宽屏、分屏和显示设置；iPhone／iPad 侧载与 Windows 分别保留实验性和 beta 标记。

原作或参考对象: **极品飞车：最高通缉** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/speedbreakerproject/speedbreaker/releases) · [浏览 RemakeList](https://remakelist.com/zh/remakes/speedbreaker/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=speedbreaker-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Linux / SteamOS / macOS Apple silicon / iOS·iPadOS 实验性 / Windows beta

**当前阶段:** v0.2.0 已发行 · Windows beta · iOS 侧载实验性

**需要准备什么:** 自备 Xbox 360 美版 NTSC-U 或欧洲 PAL 西语版《最高通缉》的合法 ISO、XISO 或提取目录；无需 Title Update，其他地区、Games on Demand 与 PC 版不能替代。约需 7.2 GB 空间。Windows/Linux x64 需 AVX2 与 Vulkan 1.2；Mac 需 Apple silicon、macOS 15+；iOS/iPadOS 需 17+、A15 级以上及手柄或键盘，并自行签名侧载。

**现在能用什么:** 正式 v0.2.0 提供 SteamOS/Linux x86-64、Steam Frame ARM64、Apple silicon Mac 与实验性 iOS IPA。Windows 使用独立预发布 v0.2.0-windows-beta.2；Android 尚无发行包。两种 SteamOS 架构不可互换。 Windows beta 只在有限 Intel 核显配置上由作者测试。iOS IPA 附件本身尚未在真机安装，作者测试的是 Xcode 签名构建；侧载权限与内存限制可能阻止运行。Mac 未公证，macOS 15 仅虚拟机测试。Steam Frame 为平面屏幕模式，非 VR；ARM64 包未验证其他 Linux 设备。Steam Deck OLED 应设为 60 Hz，LCD 型号未测；不保证普遍帧率。本站未运行。

**代码许可:** [Project-authored code is GPL-3.0-or-later; bundled libraries retain their own licenses, and original game content is excluded.](https://github.com/speedbreakerproject/speedbreaker#readme)  
**作者:** project(u) / SpeedBreakerProject  
[官方文档](https://github.com/speedbreakerproject/speedbreaker#readme) · 资料核对日期: 2026-10-27

</details>

### [Renegade Squadron — PC](https://github.com/gtteancum/starwars-renegadesquadron-pc)

把 PSP《星球大战：前线之精英部队》移植到 Windows，支持双摇杆与更高显示分辨率。需要自己的美版游戏文件，当前仍有帧时间不均等已知问题。

原作或参考对象: **星球大战：前线之精英部队** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/GTTeancum/StarWars-RenegadeSquadron-PC/releases/tag/v0.9b) · [浏览 RemakeList](https://remakelist.com/zh/remakes/renegade-squadron-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=renegade-squadron-pc-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · DirectX 12

**当前阶段:** 预览版 v0.9b · Windows 下载

**需要准备什么:** 自备 PSP 美版 ULUS10292 游戏，将提取的 PSP_GAME 放入 data；程序不含游戏数据。

**现在能用什么:** v0.9b 提供 Windows x64 的 RenegadeSquadronPC-0.9b.zip，使用 DirectX 12，支持键鼠和 Xbox 手柄。自备美版 ULUS10292 的 PSP_GAME 目录。仍有帧时间不均和近似实现的 PC 菜单叠层。可选高清纹理包单独提供，放大模型声明含 CC BY 与非商业 CC BY-NC-SA 条款，不授予原游戏图像权利；基础移植无需该包。本站未安装或试玩。

**代码许可:** [MIT for framework/port, third-party notices separate](https://github.com/GTTeancum/StarWars-RenegadeSquadron-PC/blob/main/work/project/source/LICENSE)  
**作者:** gtteancum  
[官方文档](https://github.com/gtteancum/starwars-renegadesquadron-pc#readme) · 资料核对日期: 2026-10-28

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
[下载程序并自备游戏文件](https://github.com/HayatoG/tlg_pc/releases/tag/v2026.10.27-4825a99) · [浏览 RemakeList](https://remakelist.com/zh/remakes/last-guardian-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=last-guardian-pc-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Linux x86-64（glibc 2.39+）/ Windows 10–11 x64（游玩未验证）

**当前阶段:** v2026.10.27-4825a99 · 预览 · 自备 PS4 文件

**需要准备什么:** 自备 PS4 美版 CUSA03627 或欧版 CUSA03745 与 01.03 更新，及自己主机的音频系统文件。

**现在能用什么:** v2026.10.27-4825a99 提供不含游戏文件的 Linux／Windows 归档。Linux 游玩来自作者报告；默认 30 FPS，可选实验性 60 FPS／解锁帧率。 Windows 有自动构建包，但作者尚未验证游玩；高帧率模式仍为实验，未建立完整通关覆盖。macOS 尚在计划中，无发行包。本站未构建、安装或试玩。

**代码许可:** [GPL-2.0 per port/LICENSE and README; game/firmware excluded](https://github.com/HayatoG/tlg_pc/blob/main/port/LICENSE)  
**作者:** HayatoG  
[官方文档](https://github.com/hayatog/tlg_pc#readme) · 资料核对日期: 2026-10-28

</details>

### [Tiberian Sun Recomp](https://github.com/sp00nznet/tiberiansun-recomp)

从自有《泰伯利亚之日／火线风暴》安装生成原生程序，加入宽屏和显示设置。当前为早期可运行版本，作者检查了遭遇战及战役首关，完整流程尚未确证。

原作或参考对象: **泰伯利亚之日/火线风暴** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/sp00nznet/tiberiansun-recomp/releases/tag/v0.1.0-alpha.2) · [浏览 RemakeList](https://remakelist.com/zh/remakes/tiberian-sun-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=tiberian-sun-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux；macOS 经 CrossOver（未验证）

**当前阶段:** Alpha 安装器 · 从自有游戏构建

**需要准备什么:** 自备 Steam《泰伯利亚之日／火线风暴》安装；工具从本地数据生成并构建，不提供游戏文件。

**现在能用什么:** v0.1.0-alpha.2 提供获取工具并在本地构建的平台安装器；Linux 新增 F10 设置及更多分辨率。安装器从自有 Steam《泰伯利亚之日＋火线风暴》文件构建，并非捆绑游戏。首次约需 30–60 分钟及 6 GB，可能经许可安装构建工具；安装器未签名。Windows／Linux 有作者测试记录，macOS 经 CrossOver 且作者尚未测试；完整通关仍待验证。本站未构建、安装或试玩。

**代码许可:** [MIT authored tooling; EA game and generated C excluded](https://github.com/sp00nznet/tiberiansun-recomp/blob/main/LICENSE)  
**作者:** sp00nznet  
[官方文档](https://github.com/sp00nznet/tiberiansun-recomp#readme) · 资料核对日期: 2026-10-28

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

### [Melee Unlocked](https://github.com/Hero88go/melee-unlocked)

Super Smash Bros. Melee 的原生 PC 移植，支持 Slippi 联机和高刷新率画面；需自备 NTSC 1.02 ISO。

原作或参考对象: **Super Smash Bros. Melee（NTSC 1.02）** · 平台兼容层  
[下载程序并自备游戏文件](https://github.com/Hero88go/melee-unlocked/releases/tag/v0.9.63) · [浏览 RemakeList](https://remakelist.com/zh/remakes/melee-unlocked/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=melee-unlocked-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 / Linux x86-64（AVX2、OpenGL 4.5）

**当前阶段:** Beta v0.9.63 · Linux 实验支持 · 需自备 ISO

**需要准备什么:** 需自备合法取得、干净且未压缩的 Super Smash Bros. Melee NTSC 1.02 ISO。项目不附原版游戏数据；代码许可不涵盖游戏素材。

**现在能用什么:** v0.9.63 提供 Windows x64 与 Linux x86-64 包，修复联机帧率下降、舞台皮肤、音乐延迟及低内存崩溃。 仍为 Beta。Linux 属实验支持，需 AVX2 与 OpenGL 4.5；Static Recomp 仅限 Windows，mod 兼容性因引擎而异。需自备 NTSC 1.02 ISO；本站未安装或试玩。

**代码许可:** [GPL-3.0-or-later · port code; third-party components keep their own terms.](https://github.com/Hero88go/melee-unlocked/blob/main/LICENSE)  
**作者:** Hero88go / Melee Unlocked contributors  
[官方文档](https://github.com/Hero88go/melee-unlocked#readme) · 资料核对日期: 2026-10-28

</details>

### [Brawl Recompiled](https://github.com/josiahg2502-glitch/BrawlRecompiled)

通过静态重编译实现的 Super Smash Bros. Brawl 原生 PC 移植，提供 Windows 和 Linux 版本；需自备美版 USA RSBE01 revision 1 光盘镜像。

原作或参考对象: **Super Smash Bros. Brawl（Wii，美版 USA RSBE01 revision 1）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/josiahg2502-glitch/BrawlRecompiled/releases/tag/v0.4.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/brawl-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=brawl-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux 64 位（glibc 2.35+、Vulkan）

**当前阶段:** 开发中 · v0.4.0 · 需自备原版光盘镜像

**需要准备什么:** 需自备合法取得的 Brawl 光盘镜像：美版 USA、RSBE01、revision 1，格式为 ISO、CISO 或 WBFS。解包约需 7 GB 空间；RVZ、WIA、GCZ 或 NKit 镜像需先转换为普通 ISO。RemakeList 不提供光盘镜像。

**现在能用什么:** v0.4.0 提供 Windows 和 Linux 下载包。Linux 要求 64 位系统、glibc 2.35 或更新版本及 Vulkan 驱动。作者报告 VS 对战可运行，Classic 与 Subspace 仅测试到开头；本站未安装或试玩这些构建。

**代码许可:** [GPLv3 · project code only; original game artwork and third-party components have separate rights and terms.](https://github.com/josiahg2502-glitch/BrawlRecompiled/blob/v0.4.0/wiicompiled/LICENSE)  
**作者:** JosiahG  
[官方文档](https://github.com/josiahg2502-glitch/BrawlRecompiled/blob/v0.4.0/README.md) · 资料核对日期: 2026-10-25

</details>

### [Splinter Cell: Double Agent — Xbox Recomp](https://github.com/TGP482/SCDA-XBERecomp)

将原版 Xbox《细胞分裂：双重间谍》带到 Windows 的原生移植，加入键鼠操作、分辨率与帧率调整及合作模式；需自备 Xbox 游戏文件。

原作或参考对象: **细胞分裂：双重间谍（2006 原版 Xbox）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/TGP482/SCDA-XBERecomp/releases/tag/V2) · [浏览 RemakeList](https://remakelist.com/zh/remakes/scda-xbe-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=scda-xbe-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10+ x64 · Direct3D 12

**当前阶段:** V2 正式版 · 需原版 Xbox 文件

**需要准备什么:** 需自备合法取得的原版 Xbox《双重间谍》。发行包可读取 ISO 或提取后的文件；default.xbe、sc4_adv.xbe 需与 Default、Media、adv 文件夹放在一起。源码构建仅接受提取后的文件。PC 和 Xbox 360 版文件不能替代，下载内容不含游戏素材。

**现在能用什么:** 下载 V2 并解压 SCDA-XBERecomp.zip，将自备 ISO 或提取后的游戏文件放入 assets，再运行 SCDA.exe；首次启动会在本机编译游戏代码。需 Windows 10+ x64、Direct3D 12 显卡、支持 SSE4.2 与 POPCNT 的双核处理器、4 GB 内存及约 6 GB 空间。

**代码许可:** [MIT for the project code; original game content and third-party components retain their own rights.](https://github.com/TGP482/SCDA-XBERecomp/blob/main/LICENSE)  
**作者:** TGP482  
[官方文档](https://github.com/TGP482/SCDA-XBERecomp#readme) · 资料核对日期: 2026-10-25

</details>

### [P.T. for PC](https://github.com/LoreanXavier/pt-pc)

将 PS4《P.T.》试玩版带到桌面的移植，加入键鼠、手柄和拍照模式；需自备 PS4 游戏数据。

原作或参考对象: **P.T.（2014 PS4 试玩版）** · 平台兼容层  
[下载程序并自备游戏文件](https://github.com/LoreanXavier/pt-pc/releases/tag/v1.0.8) · [浏览 RemakeList](https://remakelist.com/zh/remakes/pt-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pt-pc-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 / Linux x86-64 / macOS 14+

**当前阶段:** v1.0.8 · 早期移植 · 需原版文件

**需要准备什么:** 需自备合法取得的 PS4 P.T. 数据，作者测试的是美版 CUSA01127。加密商店 PKG 不能使用；移植和安装器不附原版游戏文件。

**现在能用什么:** v1.0.8 提供 Windows、Linux 安装器及便携包，以及 Apple silicon 和 Intel Mac 构建。Linux 需 glibc 2.38+；图形需 Vulkan 1.3，macOS 通过随附 MoltenVK 运行。本站未运行这些构建。 Intel Mac 构建尚未在 Intel Mac 真机测试；VR 仅用模拟运行时检查。macOS 不支持部分效果和超分功能，硬件支持范围不同。

**代码许可:** [MIT for project code; original game content and third-party components retain their own rights and terms.](https://github.com/LoreanXavier/pt-pc/blob/main/LICENSE)  
**作者:** LoreanXavier  
[官方文档](https://github.com/LoreanXavier/pt-pc/blob/main/README.md) · 资料核对日期: 2026-10-26

</details>

### [GT4Recomp](https://github.com/moesuito/gt4-staticrecomp)

将《Gran Turismo 4》带到 Windows，提供分辨率、手柄和材质包设置；需自备受支持的 PS2 光盘镜像。

原作或参考对象: **Gran Turismo 4（PS2）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/moesuito/gt4-staticrecomp/releases/tag/v1.3.0-rc6) · [浏览 RemakeList](https://remakelist.com/zh/remakes/gt4-staticrecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gt4-staticrecomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · Vulkan / Direct3D 12 / Direct3D 11

**当前阶段:** v1.3.0-rc6 · 预发布 · 需原版文件

**需要准备什么:** 需自备合法取得的 Gran Turismo 4 美版 v2.00（SCUS-97328）普通 ISO；Spec II 需另备 Spec II 1.10 镜像。项目不提供游戏或模组文件。

**现在能用什么:** v1.3.0-rc6 是公开测试版，提供 Windows 安装器和便携 ZIP，并非正式 1.3.0。Vulkan 是已测试的默认渲染方式，Direct3D 12 与 11 是较新的备选；Linux 和 Android 仍在计划中。 候选测试版：部分驾照演示和菜单背景不播放，尚不支持赛车方向盘，长时间游玩未完成验证。性能模式会移除灯光光晕和太阳眩光；Spec II 超宽屏 HUD 仍有问题，表现取决于硬件。

**代码许可:** [MIT for original project code; the separate PCSX2 GS process is GPL-3.0-or-later. Original game and mod content have separate rights.](https://github.com/moesuito/gt4-staticrecomp/blob/main/LICENSE)  
**作者:** moesuito  
[官方文档](https://github.com/moesuito/gt4-staticrecomp/blob/main/README.md) · 资料核对日期: 2026-10-26

</details>

### [God of War PSP Recomp](https://github.com/DrummingBird1/gow-psp-recomp)

使用自备美版光盘镜像，在 Windows 本地重编译两部 PSP《战神》的启动器，提供现代显示与输入设置。

原作或参考对象: **战神：奥林匹斯之链／斯巴达之魂（PSP）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/DrummingBird1/gow-psp-recomp/releases/tag/v1.3.1) · [浏览 RemakeList](https://remakelist.com/zh/remakes/gow-psp-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gow-psp-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows · Linux / Steam Deck 在计划中

**当前阶段:** v1.3.1 · 早期移植 · 需原版文件

**需要准备什么:** 需自备合法取得的美版 PSP CHD 或 ISO：奥林匹斯之链 UCUS98653，或斯巴达之魂 UCUS98737。项目不提供原版游戏数据。

**现在能用什么:** v1.3.1 提供 Windows 启动器 ZIP。首次 Build 会先询问并下载便携构建工具，再在本机编译选中的游戏。目前发行平台为 Windows，两部游戏均未完成完整通关验证。 预览软件，后期关卡、Boss 与结局可能仍有问题。Linux 和 Steam Deck 尚在计划中；启动器未签名，构建工具需首次下载。自动关卡巡检不等于完整通关。

**代码许可:** [GPL-3.0-or-later for project code; original game content and third-party components retain their own rights and terms.](https://github.com/DrummingBird1/gow-psp-recomp/blob/main/LICENSE)  
**作者:** DrummingBird1  
[官方文档](https://github.com/DrummingBird1/gow-psp-recomp/blob/main/README.md) · 资料核对日期: 2026-10-26

</details>

### [PrimeRecomp](https://github.com/gminustwo/primerecomp)

《银河战士 Prime 复刻版》的早期桌面移植，加入鼠标操作；安装需自备已提取的 Switch v1.0.0 文件。

原作或参考对象: **银河战士 Prime 复刻版（Switch）** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/gminustwo/primerecomp/releases/tag/v0.0.3) · [浏览 RemakeList](https://remakelist.com/zh/remakes/primerecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=primerecomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64／Linux x86-64／macOS 15+ Apple Silicon

**当前阶段:** v0.0.3 · 早期 Beta · 需原版文件

**需要准备什么:** 需自备合法取得的 Switch《银河战士 Prime 复刻版》v1.0.0 文件，不含更新，并提取为 exefs 与 romfs 文件夹。项目不含原版游戏数据。

**现在能用什么:** v0.0.3 已发布 Windows ZIP、Linux AppImage，并新增 Apple Silicon macOS DMG。Windows／Linux 需 AVX2 与 Vulkan 1.3，Linux 另需 glibc 2.35+；Mac 需 M1+ 和 macOS 15+。设置时从自备的 Switch v1.0.0 提取文件在本机重编译。本次改善 Steam Deck 性能并提供 30／60 fps 预设。 早期 Beta：过门可能明显减速，仍有画面问题，Magmoor Caverns 之后尚未测试，可能崩溃或卡住。Deck 性能记录只覆盖特定区域；macOS 未公证，首次编译着色器可能短暂卡顿。本站未试玩。

**代码许可:** [MIT for project code; original game content and third-party components retain their own rights and terms.](https://github.com/gminustwo/primerecomp/blob/main/LICENSE)  
**作者:** gminustwo  
[官方文档](https://github.com/gminustwo/primerecomp/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Wario Land: Shake It! Native PC](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC)

将 Wii《瓦力欧大陆：摇摆》带到 Windows，提供键盘／手柄和图形设置；需自备受支持的美版游戏镜像。

原作或参考对象: **瓦力欧大陆：摇摆（Wii）** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC/releases/tag/v0.2.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/wario-land-shake-it-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wario-land-shake-it-pc-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · Direct3D 12 / Vulkan

**当前阶段:** v0.2.0 · 测试版 · 需本地编译

**需要准备什么:** 需自备合法取得、未修改的 Wii 美版 Wario Land: Shake It!（RWLE01）镜像，或提取后的 sys／files 文件夹；启动器校验原始 main.dol。构建约需 3 GB，提取镜像另需约 4.4 GB。项目不提供原版数据、游戏可执行文件或已翻译的游戏代码。

**现在能用什么:** v0.2.0 提供 Windows 启动器及含构建工具的 ZIP，并非预编译好的游戏。导入自备的指定美版 Wii 镜像后，在本机构建约需 15–45 分钟，建议 16 GB 内存。需 Windows 10／11 x64 和 D3D12 或 Vulkan。 GitHub 虽未标记预发布，作者仍称测试版。全流程、Boss、影片及 DualSense 体感覆盖不完整，可能有渲染问题或崩溃；宽屏与插帧属实验功能。本站未安装或试玩。

**代码许可:** [GPL-3.0 for project code; original game content and third-party components retain their own rights and terms.](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC/blob/main/LICENSE)  
**作者:** santiagovalencia109  
[官方文档](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [PGR4 Native](https://github.com/shaunsingh/pgr4-native)

为《世界街头赛车 4》重编译版本提供原生 Direct3D 12 渲染器；在 Windows 或 Proton 下运行，需自备游戏与 Title Update #2。

原作或参考对象: **世界街头赛车 4（Xbox 360）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/shaunsingh/pgr4-native/releases/tag/v0.2.1) · [浏览 RemakeList](https://remakelist.com/zh/remakes/pgr4-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pgr4-native-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64 / Linux、Steam Deck 通过 Proton

**当前阶段:** v0.2.1 · 早期移植 · 需原版文件

**需要准备什么:** 需自备合法取得并提取后的 PGR4 光盘，以及 Title Update #2 包或文件。作者称 PAL 与 NTSC 光盘内容一致；项目不含原版游戏数据。

**现在能用什么:** v0.2.1 提供 Windows x64 ZIP；Linux 与 Steam Deck 使用 Proton，这个发行包并非原生 Linux 程序。本站未验证游玩或性能。 需使用受支持的游戏／更新组合和图形配置；兼容性及帧率取决于硬件，并在适用时取决于 Proton，不保证 Steam Deck 的普遍帧率。

**代码许可:** [MIT for project code; original game content and third-party components retain their own rights and terms.](https://github.com/shaunsingh/pgr4-native/blob/main/LICENSE)  
**作者:** shaunsingh  
[官方文档](https://github.com/shaunsingh/pgr4-native/blob/main/README.md) · 资料核对日期: 2026-10-27

</details>

### [Sky Recomp](https://github.com/Apolinario-coder/SkyRecomp)

《御天之剑 HD》的实验性桌面移植，提供键鼠操作和图形设置；需自备 Switch v1.0.0 游戏文件。

原作或参考对象: **塞尔达传说：御天之剑 HD（Switch）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/Apolinario-coder/SkyRecomp/releases/tag/v2.0.2) · [浏览 RemakeList](https://remakelist.com/zh/remakes/skyrecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=skyrecomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows / Linux / macOS

**当前阶段:** v2.0.2 · 早期移植 · 需原版文件

**需要准备什么:** 需自备合法取得的 Switch《御天之剑 HD》v1.0.0 文件，不含更新。项目不提供原版游戏文件；可选视觉包遵循各作者独立条款。

**现在能用什么:** v2.0.2 提供 Windows、Linux 与 macOS 包。Windows／Linux 需要兼容 Vulkan 1.3 的硬件，x86 构建需 AVX2；macOS 使用项目的 Metal 后端。全程稳定性尚未建立。 实验阶段：崩溃、菜单卡死与渲染差异仍在排查。高帧率模式属于实验功能，表现取决于硬件；本站未安装或试玩这些包。

**代码许可:** [MIT for original code; LAS Recomp and third-party components retain their notices. Texture packs and presets have separate authors and terms.](https://github.com/Apolinario-coder/SkyRecomp/blob/main/LICENSE)  
**作者:** Apolinario-coder  
[官方文档](https://github.com/Apolinario-coder/SkyRecomp/blob/main/README.md) · 资料核对日期: 2026-10-26

</details>

### [Madden NFL 08 Recompiled](https://github.com/anishchandra24/MaddenNFL08-Recompiled)

Xbox 360《Madden NFL 08》的早期 Windows 移植；安装程序下载工具链，并从自备提取后的游戏文件在本机构建。

原作或参考对象: **Madden NFL 08（Xbox 360）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/anishchandra24/MaddenNFL08-Recompiled/releases/tag/v0.1.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/madden-nfl08-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=madden-nfl08-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · Direct3D 12，需 ROV

**当前阶段:** v0.1.0 · 预发布 · 需原版文件

**需要准备什么:** 需自备合法取得的 Xbox 360 Madden NFL 08（Title ID 4541081D），提取后将 default.xex 与其他游戏文件放在一起。仅支持 README 指定的主程序版本。

**现在能用什么:** v0.1.0 是预发布安装程序，不是解压即玩的游戏程序。安装需受支持的游戏文件、网络、Git、带 C++ 工具的 Visual Studio 2022 Community，以及约 10 GB 构建空间。 需较快处理器及支持 Direct3D 12 光栅化顺序视图（ROV）的显卡。作者低配置电脑无法流畅比赛，测试仅覆盖两台电脑；仍有着色器卡顿、部分视听问题，在线服务不支持。

**代码许可:** [GPL-3.0 for project code; original game content and third-party components retain their own rights and terms.](https://github.com/anishchandra24/MaddenNFL08-Recompiled/blob/main/LICENSE)  
**作者:** anishchandra24  
[官方文档](https://github.com/anishchandra24/MaddenNFL08-Recompiled/blob/main/README.md) · 资料核对日期: 2026-10-26

</details>

### [CPS-2 Recomp](https://github.com/tmcleroy/cps2recomp)

将多款 CPS-2、CPS-1 街机游戏移植到桌面，提供统一启动器、格斗训练工具和三人清版动作玩法；需自备街机基板对应的指定 ROM 版本。

原作或参考对象: **Capcom CPS-2／CPS-1 街机游戏** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/tmcleroy/cps2recomp/releases/tag/v0.4.0-beta.7) · [浏览 RemakeList](https://remakelist.com/zh/remakes/cps2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cps2-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10／11 x64 · macOS 13+（Apple Silicon／Intel）· Linux x86_64／ARM64／SteamOS

**当前阶段:** v0.4.0-beta.7 · Beta · 需指定原版 ROM

**需要准备什么:** 需自备所持街机基板对应的指定 ROM 版本，CPS-2 游戏还需对应密钥文件。启动器校验文件，不接受其他区域或修订版；部分集合还需父集合。项目不提供游戏文件或密钥。

**现在能用什么:** v0.4.0-beta.7 提供 Windows x64、macOS、Linux x86_64 压缩包，并新增 Linux ARM64 包。macOS 支持 Apple Silicon 与 Intel；Linux x86_64 包也用于 SteamOS／Steam Deck。GitHub 虽未标记预发布，项目仍为 Beta。 机器及手柄覆盖有限。作者称格斗游戏已检查至结局，新清版动作游戏仅覆盖前期脚本操作。macOS 未公证，Windows 未签名；需指定原版 ROM，本站未安装或试玩。

**代码许可:** [Project code is GPL-3.0-only; third-party components retain their own notices. This license does not grant rights to Capcom or other rights holders’ game code, ROMs, keys, music or artwork.](https://github.com/tmcleroy/cps2recomp/blob/main/LICENSE)  
**作者:** tmcleroy  
[官方文档](https://github.com/tmcleroy/cps2recomp/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Free Riders Recompiled](https://github.com/YuutaTsubasa/Free-Riders-Recompiled)

Xbox 360《Sonic Free Riders》的非官方移植，无需 Kinect 也能使用手柄或键盘游玩；从自备美版／欧版光盘镜像导入数据，仍在开发中。

原作或参考对象: **Sonic Free Riders（Xbox 360）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/YuutaTsubasa/Free-Riders-Recompiled/releases/tag/v0.10.36) · [浏览 RemakeList](https://remakelist.com/zh/remakes/free-riders-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=free-riders-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows／Linux x64 · Android arm64 · 实验性 macOS Apple Silicon／iOS

**当前阶段:** v0.10.36 · 开发中 · 需原版光盘

**需要准备什么:** 需自备合法取得的美版／欧版 Xbox 360《Sonic Free Riders》光盘镜像（.iso），由启动器导入模型、材质、音频和影片。作者说明发行包包含重编译程序，不包含这些原版游戏数据；项目的 GPL 许可不覆盖 SEGA 内容。

**现在能用什么:** v0.10.36 提供 Windows／Linux x64、Android arm64、macOS arm64 与 iOS 包；此次优化 Android 比赛性能，其他平台代码未变。Windows／Linux 需 AVX 及对应的 D3D12 或 Vulkan 1.2；Android 需 9+／Vulkan 1.1，另有 10+ APK。Apple 构建需 macOS 13.3+ 或侧载的 iOS 16.3+。 许多模式仍未测试。作者记录了 Windows、M1 Mac 的一场 Dolphin Resort 完整比赛及 AYN Thor 测试，不覆盖其他手机或 iOS。Apple 支持仍为实验，macOS 未公证，Kinect v2 和在线联机仍待更广泛验证；本站未安装或试玩。

**代码许可:** [Project code is GPL-3.0-or-later. The original game’s code and data remain SEGA’s and are outside that grant; third-party components and models retain their separate licenses.](https://github.com/YuutaTsubasa/Free-Riders-Recompiled/blob/main/COPYING)  
**作者:** YuutaTsubasa  
[官方文档](https://github.com/YuutaTsubasa/Free-Riders-Recompiled/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [James Pond 2 Recompiled](https://github.com/griches/JamesPond2RobocodRecomp)

Amiga《James Pond 2》的社区移植，加入宽屏、存档槽与更平滑的画面运动；需自备受支持的 Kixx 版磁盘镜像或 WHDLoad 安装文件。

原作或参考对象: **James Pond 2: Codename RoboCod（Amiga）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/griches/JamesPond2RobocodRecomp/releases/tag/v1.0.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/james-pond-2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=james-pond-2-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · macOS 13+（Apple Silicon／Intel）· Linux x86_64／Steam Deck · PS5 自制软件环境

**当前阶段:** 桌面 v1.0.0 · PS5 v1.0.2 · 需原版磁盘

**需要准备什么:** 需自备合法取得的 Amiga Kixx 再版标准 .adf 镜像，可使用 gzip 压缩的 .adz 或 .zip 包装，或受支持的 WHDLoad 安装文件。原始 Millennium 加密发行版、扩展 ADF、.dms 与 .ipf 不受支持；本站不提供原盘下载。

**现在能用什么:** 桌面下载为 v1.0.0，提供 Windows、macOS 与 Linux 包，Steam Deck 使用 Linux 包。PS5 单独更新至 v1.0.2，需要已经能够运行自制软件的主机。v1.0.2 发行说明明确其他平台仍为 v1.0.0，并非桌面更新。 属于早期公开版本，持有其他发行版不代表其磁盘格式可用。PS5 是独立的自制软件目标，不是普通主机商店版本。本站未安装、试玩或独立验证全流程兼容性。

**代码许可:** [The project’s own code is GPL-3.0. SDL3, Musashi, fonts and other dependencies retain their separate licenses; the original game’s code, artwork and music are not granted under the project license.](https://github.com/griches/JamesPond2RobocodRecomp/blob/main/LICENSE)  
**作者:** griches  
[官方文档](https://github.com/griches/JamesPond2RobocodRecomp/blob/main/README.md) · 资料核对日期: 2026-10-27

</details>

### [recvx-enhanced-port](https://github.com/aikatore/recvx-enhanced-port)

《维罗妮卡 X》增强移植，加入双人合作、可选第三人称瞄准与宽屏，直接读取自备 PS2 光盘镜像。

原作或参考对象: **生化危机：维罗妮卡 X（PS2）** · 社区移植  
[下载程序并自备游戏文件](https://github.com/aikatore/recvx-enhanced-port/releases/tag/v0.6.10) · [浏览 RemakeList](https://remakelist.com/zh/remakes/recvx-enhanced-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=recvx-enhanced-port-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10+ x86 · Linux i686 · OpenGL 3.3

**当前阶段:** v0.6.10 · 预发布 · 双人合作

**需要准备什么:** 需自备合法取得的 PS2 美版 NTSC-U《维罗妮卡 X》ISO，序列号 SLUS-20184；游戏数据和可选高清材质包均不包含。

**现在能用什么:** v0.6.10 为预发布，包含 Windows x86、Linux i686 游戏包及独立的 Linux x86_64 合作服务器。Linux 需 glibc 2.34+ 和 32 位图形／音频库，两种客户端均需 OpenGL 3.3。过场角色替换仍是早期实现，合作与模组组合可能存在问题。

**代码许可:** [MIT for the port and credited decompilation code; third-party components and Capcom game content have separate terms.](https://github.com/aikatore/recvx-enhanced-port/blob/main/LICENSE)  
**作者:** aikatore  
[官方文档](https://github.com/aikatore/recvx-enhanced-port/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Code Veronica PS3 HD Recomp](https://github.com/kastieloficial/RE-Code-Veronica-PS3-HD-Recomp-PC)

PS3《维罗妮卡 X HD》移植，加入补帧、速通练习工具与现代战斗 HUD；需自备受支持的 PSN 版本。

原作或参考对象: **生化危机：维罗妮卡 X HD（PS3）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/kastieloficial/RE-Code-Veronica-PS3-HD-Recomp-PC/releases/tag/v1.1.9) · [浏览 RemakeList](https://remakelist.com/zh/remakes/code-veronica-ps3-hd-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=code-veronica-ps3-hd-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · Direct3D 12

**当前阶段:** v1.1.9 · Windows 移植 · 需指定 PSN 文件

**需要准备什么:** 需自备 PS3 PSN 本体 01.00：欧版 NPEB00553、美版 NPUB30467 或日版 NPJB00135，目录包含 PARAM.SFO 与 USRDIR／EBOOT.BIN。欧美版还需购买账号自己的 .rap 授权文件；更新版和光盘版不支持，启动器不能直接打开 PKG。

**现在能用什么:** v1.1.9 包含 Windows 移植与独立可选 PKG 提取工具，需 Windows 10／11、Direct3D 12 和 x64 Visual C++ 运行库。60 fps 插值模式下逻辑仍为 30 Hz，电脑无法维持 60 fps 时可能拖慢游戏；GPU 插值和材质模组仍属实验性，着色器编译可能卡顿。

**代码许可:** [MIT for port/ps3recomp code; third-party terms and Capcom’s original game rights are separate.](https://github.com/kastieloficial/RE-Code-Veronica-PS3-HD-Recomp-PC/blob/code-veronica/LICENSE)  
**作者:** kastieloficial  
[官方文档](https://github.com/kastieloficial/RE-Code-Veronica-PS3-HD-Recomp-PC/blob/code-veronica/README.md) · 资料核对日期: 2026-10-28

</details>

### [OpenRAC](https://github.com/OpenRAC/OpenRAC)

《瑞奇与叮当》原生移植，提供统一启动器、图形增强和模组工具；初代可玩，后续作品仍在开发。

原作或参考对象: **瑞奇与叮当（PS2）** · 社区移植  
[下载程序并自备游戏文件](https://github.com/OpenRAC/OpenRAC/releases/tag/launcher-v0.9.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/openrac/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openrac-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64 · Linux x64／ARM64 · macOS 通用版 · Android ARM64

**当前阶段:** launcher-v0.9.0 · 初代可玩 · 续作开发中

**需要准备什么:** 需自备初代 PS2 光盘 ISO 或 CHD：PAL SCES_509.16 光盘 v2.00，或 NTSC-U SCUS_971.99 光盘 v1.00。启动器核验光盘，其他地区／发行版可能不匹配；不下载游戏数据。

**现在能用什么:** launcher-v0.9.0 提供 Windows 安装器、Linux 包、通用 Mac DMG 和 Android ARM64 debug APK。当前仅初代 PAL／NTSC 列为可玩，《Going Commando》可进入主菜单，其他续作仍在进行中。增强图形属于实验功能，可能需要逐关烘焙光照。

**代码许可:** [Top-level launcher/tools use GPL-3.0-or-later; game modules and the MIT SDK/editor retain their own notices. None of these licenses grant original game-content rights.](https://github.com/OpenRAC/OpenRAC/blob/master/LICENSE.md)  
**作者:** OpenRAC  
[官方文档](https://github.com/OpenRAC/OpenRAC/blob/master/README.md) · 资料核对日期: 2026-10-28

</details>

### [The Umbrella Chronicles Recompiled](https://github.com/solleo95/reuc-recomp)

《保护伞编年史》Windows 移植，提供鼠标瞄准、现代渲染选项及早期双人在线合作。

原作或参考对象: **生化危机：保护伞编年史（Wii）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/solleo95/reuc-recomp/releases/tag/0.0.6) · [浏览 RemakeList](https://remakelist.com/zh/remakes/reuc-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=reuc-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · AVX2 · Vulkan 1.3

**当前阶段:** 0.0.6 · 早期版本 · 合作模式实验性

**需要准备什么:** 需自备 Wii 美版 NTSC-U 光盘镜像，游戏 ID RBUE08；可用启动器内置 Wit 提取，或提供已提取的 DATA 目录。PAL RBUP08 与日版 RBUJ08 不支持；可选专有运行库及材质包另有条款。

**现在能用什么:** 0.0.6 提供 Windows ZIP，需要 AVX2 与 Vulkan 1.3。属于早期版本，主要在作者的 RTX 4080／Windows 11 电脑上测试，最低性能配置尚未确定。在线合作可能连接失败、不同步或短暂卡住，光追目前只覆盖阴影；本版复杂场景最多可能增加约 1 GiB 内存占用。

**代码许可:** [GPL-3.0 for project code; vendor DLSS/FidelityFX runtimes and other dependencies keep their own licenses. Capcom game code and assets are excluded.](https://github.com/solleo95/reuc-recomp/blob/main/LICENSE)  
**作者:** solleo95  
[官方文档](https://github.com/solleo95/reuc-recomp/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [G-Diffuser 3DS](https://github.com/cruxxxxxx/gdx-3ds)

面向 3DS 系列的原生《F-Zero X》移植，提供裸眼 3D、下屏仪表与 2–4 人比赛；需自备受支持的卡带转储和可运行自制软件的主机。

原作或参考对象: **《F-Zero X》（Nintendo 64）** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/cruxxxxxx/gdx-3ds/releases/tag/v1.1.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/g-diffuser-3ds/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=g-diffuser-3ds-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Old／New Nintendo 3DS 与 2DS 系列 · 自制软件环境

**当前阶段:** v1.1.0 · 自制软件主机 · 自备原版卡带

**需要准备什么:** 需自备 F-Zero X 美版 revision 0 卡带转储，在电脑转换为两个 .o2r 包；声音另需本机 DSP 固件转储。EK 需受支持的日版零售 64DD 磁盘转储，不支持民间汉化／翻译盘。项目不提供 ROM、磁盘或预转换游戏资产。

**现在能用什么:** v1.1.0 提供独立的 Old／New 3DS ZIP、.3dsx 和 .cia，以及可选 EK 构建与桌面资产提取器。先在电脑处理资产；提取脚本需要带 decomp 子模块的 git 检出。v1.0.0 下载已撤下。须按主机型号选择包。宽屏与新赛道缓冲仅做过模拟器测试，多人尚未覆盖所有机型配对；Old 3DS 的 3D 多人上限为 30 fps，EK 构建存在卡顿、音乐断续和编辑器迟缓。内存与音频问题仍在，不保证 60 fps。托管联机服务器为临时服务；

**代码许可:** [MIT covers original G-Diffuser and 3DS-port additions, unless a file says otherwise. Dependencies, decompiled Nintendo/N64 SDK code and game content have separate rights; the MIT license does not grant rights to those materials.](https://github.com/cruxxxxxx/gdx-3ds/blob/main/LICENSE)  
**作者:** cruxxxxxx  
[官方文档](https://github.com/cruxxxxxx/gdx-3ds/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Metroid Dread Recomp — Linux fork](https://github.com/DaniSald/Metroid-Dread-Recomp)

Metroid Dread Recomp 的 Linux 增强分支，从自备 Switch 2.1.0 文件构建原生 PC 版本，提供 Linux AppImage 与 Windows 包。

原作或参考对象: **《银河战士 生存恐惧》（Nintendo Switch）** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/DaniSald/Metroid-Dread-Recomp/releases/tag/v0.4.0-linux.2) · [浏览 RemakeList](https://remakelist.com/zh/remakes/metroid-dread-recomp-linux/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=metroid-dread-recomp-linux-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64／Linux x86-64（glibc 2.38+、OpenGL 4.3）／Steam Deck

**当前阶段:** v0.4.0-linux.2 · 早期预览 · 本地编译

**需要准备什么:** 需自备合法取得的 Metroid Dread 2.1.0 ExeFS 与 RomFS，更新可合并或单独指定；仅有 RomFS 不够。项目不分发游戏代码、数据或密钥。

**现在能用什么:** v0.4.0-linux.2 提供 Linux x86-64 AppImage 与 Windows ZIP；首次运行核对文件并本地编译。Linux 需约 7 GB 空间、glibc 2.38+、OpenGL 4.3、SDL2 及目录选择工具；Windows EXE 须与 recompiler 文件夹放在一起。虽未勾选 GitHub 预发布标记，作者仍将全部 0.x 称为早期预览，可能崩溃或安装失败。Linux 尚无原生 Vulkan、内置发行更新、鼠标自由瞄准与 F7 录像。Steam Deck OLED 的报告仅为九分钟测试，不代表通关或普遍 60 fps 保证；

**代码许可:** [SwitchRecomp code is Apache-2.0; the README identifies the combined Windows executable with the ScarletNX renderer as GPL-3.0. Linux and bundled toolchain/libraries have their own notices. Nintendo game files and keys are excluded.](https://github.com/DaniSald/Metroid-Dread-Recomp/blob/main/README.md#licences)  
**作者:** DaniSald  
[官方文档](https://github.com/DaniSald/Metroid-Dread-Recomp/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Odin Sphere Leifthrasir PC](https://github.com/saulob/odin-sphere-leifthrasir-pc)

在 Windows 运行自备且受支持的 PS4《奥丁领域 里普特拉西尔》包，提供启动器、渲染选项与本地奖杯；Linux 和 Steam Deck 下载为实验性。

原作或参考对象: **《奥丁领域 里普特拉西尔》（PlayStation 4）** · 平台兼容层  
[下载程序并自备游戏文件](https://github.com/saulob/odin-sphere-leifthrasir-pc/releases/tag/v0.1.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/odin-sphere-leifthrasir-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=odin-sphere-leifthrasir-pc-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10 1903+／11 x64／实验性 Linux x86-64 与 Steam Deck

**当前阶段:** v0.1.0 · Windows 公开版 · 实验性 Linux

**需要准备什么:** 需自备合法取得且已解密的 PS4 包：美版 CUSA05083 基础版 1.00；日版 CUSA01290 基础版 1.00 或 1.02 更新；欧版 CUSA05262 基础版 1.00 或 1.01 更新。更新须搭配同区基础版；主机加密包或其他版本会被拒绝，不提供游戏文件或密钥。

**现在能用什么:** v0.1.0 是首个公开版本，提供 Windows x64 ZIP 与实验性 Linux x86-64 AppImage；在启动器 Play 页面导入自备、已解密且受支持的 PS4 .pkg。两条路线都需 Vulkan 1.3 及指定扩展、约 4 GB 磁盘；Linux 另需 glibc 2.31+ 与 X11／Wayland。只有 16:9 Original 保持原画面比例：超宽比例拉伸游戏，并非显示更多场景，其他比例会压缩；HUD、菜单与视频未适配。Linux／Steam Deck 仅通过脚本检查，尚未在真实硬件测试。下载未签名；奖杯仅本地，无 PSN 或联机。

**代码许可:** [GPL-2.0-or-later covers original project code. The shadPS4-derived renderer and other third-party components retain their notices; the original game and its assets are excluded.](https://github.com/saulob/odin-sphere-leifthrasir-pc/blob/main/LICENSE)  
**作者:** saulob  
[官方文档](https://github.com/saulob/odin-sphere-leifthrasir-pc/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Rogue Galaxy Recompiled](https://github.com/victor-takai/rogue-galaxy-recomp)

从自备美版 PS2《银河游侠》光盘在本机构建 Windows 原生版本，提供宽屏、分辨率缩放与玩法选项。

原作或参考对象: **《Rogue Galaxy／银河游侠》（PlayStation 2）** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/victor-takai/rogue-galaxy-recomp/releases/tag/v0.1.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/rogue-galaxy-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rogue-galaxy-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64

**当前阶段:** v0.1.0 预发布 · Windows 本地构建 · 仅美版原盘

**需要准备什么:** 需自备合法取得的美版 PS2 Rogue Galaxy 光盘镜像 SCUS-97490，不支持其他地区版本。不分发游戏数据、BIOS 或光盘衍生文件，本机生成的游戏应保留在本地。

**现在能用什么:** v0.1.0 为 Windows 安装工具 ZIP 预发布；运行 Install.bat 并选择自备美版光盘，将下载约 300 MB 构建工具并在本地编译。需约 16 GB 空间，按电脑性能约 20–60 分钟；下载包不是已构建完整游戏。作者报告标题／开场、Salgin 场景与战斗，并非完整通关。Story 加载后仍可能偶发卡死，重场景可能降至约 50 fps，宽屏会拉伸菜单与文字。杀毒软件可能阻止本地编译器，不构成安全保证；

**代码许可:** [GPL-3.0 covers the project, matching the linked PS2Recomp framework. Dependencies retain their own notices; original game data, BIOS and disc-derived files are not included or relicensed.](https://github.com/victor-takai/rogue-galaxy-recomp/blob/main/LICENSE)  
**作者:** victor-takai  
[官方文档](https://github.com/victor-takai/rogue-galaxy-recomp/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [PaxDino](https://github.com/wootbeer/PaxDino)

《恐龙猎人：狂暴之战》的 PC 移植，增加鼠标瞄准、宽屏和最多四人本地游玩。

原作或参考对象: **恐龙猎人：狂暴之战（Nintendo 64）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/wootbeer/PaxDino/releases/tag/v0.1.6) · [浏览 RemakeList](https://remakelist.com/zh/remakes/paxdino/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=paxdino-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64／实验性 Linux x86_64 与 Steam Deck

**当前阶段:** v0.1.6 · Beta · 需原版 ROM

**需要准备什么:** 需自备受支持的美版《Turok: Rage Wars》ROM；README 提供 .n64、.z64 校验值，也接受 .v64。合作试炼修复使用美版 1.0；项目不提供游戏数据。

**现在能用什么:** v0.1.6 提供 Windows 与 Linux 压缩包，项目仍为 Beta，Linux 和 Steam Deck 属实验支持。启动器导入自备 ROM；本站未安装或试玩。

**代码许可:** [GPL-3.0 applies to project code; original game content and third-party components retain separate rights and terms.](https://github.com/wootbeer/PaxDino/blob/main/COPYING)  
**作者:** wootbeer  
[官方文档](https://github.com/wootbeer/PaxDino/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [KirbyRecomp](https://github.com/xtamqispeak/KirbyRecomp)

从自备 Switch 文件在本机构建的《超级卡比猎人队》实验性移植。

原作或参考对象: **超级卡比猎人队（Switch）** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/xtamqispeak/KirbyRecomp/releases/tag/v0.2.0-alpha) · [浏览 RemakeList](https://remakelist.com/zh/remakes/kirby-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=kirby-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · AVX2/FMA · Vulkan 1.3

**当前阶段:** v0.2.0-alpha · 本机构建 · 战斗未验证

**需要准备什么:** 需自备标题 ID 01003FB00C5A8000 对应且匹配的 ExeFS／RomFS。已测试 main 构建 ID 以 c9649e053bd7be2751ef0b00e7c03f5d59695b94 开头，其他版本未验证；不提供 NSP／XCI 导入或解密。

**现在能用什么:** v0.2.0-alpha 提供未签名安装 EXE 与源码包，并非现成游戏程序。首次安装需下载构建工具并留出数 GB 空间。作者仅测试 RTX 4070 SUPER，报告标题、村庄、菜单与存档可用，完整战斗和后期关卡未验证。在线服务、购买、多人及下载内容不可用；本站未构建或试玩。

**代码许可:** [MIT applies to project code; original game content and third-party components retain separate rights and terms.](https://github.com/xtamqispeak/KirbyRecomp/blob/main/LICENSE)  
**作者:** xtamqispeak  
[官方文档](https://github.com/xtamqispeak/KirbyRecomp/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [1080° Snowboarding: Recompiled](https://github.com/thebradshaw/1080-Snowboarding-decomp)

《1080° 雪上飞》的 PC 移植，增加宽屏、可选高帧率与更远视距。

原作或参考对象: **1080° 雪上飞（Nintendo 64）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/thebradshaw/1080-Snowboarding-decomp/releases/tag/1.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/1080-snowboarding-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=1080-snowboarding-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64／实验性 Linux x64

**当前阶段:** 1.0 · Windows 发行 · Linux 实验性

**需要准备什么:** 需自备未修改的美版 .z64 ROM，MD5 为 fa27089c425dbab99f19245c5c997613；项目不提供 ROM。滑雪板高清材质和启动器美术源自原作，不在代码许可授权范围内。

**现在能用什么:** 1.0 提供 Windows x64 与实验性 Linux x64 包。Windows 需 Vulkan 或 Direct3D 12；Linux 未经真机测试，需要接近 Ubuntu 24.04 的系统、Vulkan、SDL2 和 GTK 3。帧率选项不代表性能保证；本站未安装或试玩。 RetroAchievements 批准前，成就解锁仅保存本地。

**代码许可:** [GPL-3.0 applies to project code; original game content and third-party components retain separate rights and terms.](https://github.com/thebradshaw/1080-Snowboarding-decomp/blob/main/LICENSE)  
**作者:** thebradshaw  
[官方文档](https://github.com/thebradshaw/1080-Snowboarding-decomp/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Mission: Impossible — PC Recomp](https://github.com/nickallevato/mi_n64_exe)

N64《碟中谍》的 Linux 移植，增加鼠标瞄准、宽屏与现代摇杆视角。

原作或参考对象: **碟中谍（Nintendo 64）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/nickallevato/mi_n64_exe/releases/tag/v0.1.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/mi-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mi-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Linux x86_64 · glibc 2.35+ · Vulkan

**当前阶段:** v0.1.0 · Linux 发行 · 全流程未验证

**需要准备什么:** 需自备美版 .z64 ROM，SHA-1 为 7546d5df1fc93fed8205a066f1333fd7dd50c1e1；不提供 ROM 或原作素材。

**现在能用什么:** v0.1.0 提供基于 Ubuntu 22.04 的 Linux x64 AppImage 与 tar.gz，需 Vulkan、glibc 2.35+。作者报告 20 关均可加载游玩，但未验证完整通关；无 Windows 或 macOS 包。本站未安装或试玩。 60 FPS 选项不保证所有设备均达到该帧率。

**代码许可:** [GPL-3.0 applies to project code; original game content and third-party components retain separate rights and terms.](https://github.com/nickallevato/mi_n64_exe/blob/main/COPYING)  
**作者:** nickallevato  
[官方文档](https://github.com/nickallevato/mi_n64_exe/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Ascension](https://github.com/arnaldolima1/gow-ascension-pc)

从自备欧版 PS3《战神：升天》光盘构建的实验性 Windows 移植；作者报告已到首关及首个首领，尚不能完整通关。

原作或参考对象: **战神：升天（PS3）** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/arnaldolima1/gow-ascension-pc/blob/main/docs/README.en.md#building) · [浏览 RemakeList](https://remakelist.com/zh/remakes/god-of-war-ascension-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=god-of-war-ascension-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · 手动源码构建

**当前阶段:** 源码构建 · 前期玩法实验

**需要准备什么:** 需自备合法取得的欧版 BCES-01741 1.00 光盘数据、本地准备的 EBOOT.ELF 及所需自有密钥。可选巴西葡语内容从自备美版光盘生成；项目不提供游戏文件或密钥。

**现在能用什么:** 尚无发行包。需手动配置 Visual Studio 2022、CMake、Ninja、Vulkan SDK、带补丁的 ps3recomp 与本地 .env；作者估计首次构建需 20–40 分钟及 16 GB 内存。Windows 是已记录测试的路线，macOS 已暂停。仍有性能不足、画面重复和 SPU 作业卡住，后续关卡未确立可玩；本站未构建或试玩。

**代码许可:** [MIT covers this repository’s code. The author states that builds using RPCS3’s RSX renderer are GPL-2.0; original game code and assets retain their owners’ rights.](https://github.com/arnaldolima1/gow-ascension-pc/blob/main/LICENSE)  
**作者:** arnaldolima1  
[官方文档](https://github.com/arnaldolima1/gow-ascension-pc/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [LostWorldNative](https://github.com/snicolast/LostWorldNative)

1997 年街机光枪游戏的 Windows 源码构建移植，加入宽屏、现代渲染及鼠标／手柄瞄准；需指定日版 ROM 集合。

原作或参考对象: **失落的世界：侏罗纪公园（街机）** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/snicolast/LostWorldNative/blob/master/README.md#install) · [浏览 RemakeList](https://remakelist.com/zh/remakes/lost-world-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=lost-world-native-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · Vulkan 1.3 · 本机构建

**当前阶段:** 源码构建 · 需原版街机 ROM

**需要准备什么:** 需自备合法取得的 lostwsga.zip，即 Sega Model 3 Step 1.5 的日版 Rev. A 集合及指定 ROM 文件；不支持其他修订版，不提供原作数据。

**现在能用什么:** 尚无已发布二进制。文档提供 Windows 路线：准备 ROM、Python 3 与 Visual Studio 2022 C++ 构建工具后运行 build.bat，首次构建会下载依赖。作者截图展示了移植，但全流程／设备覆盖与高刷新表现未获独立验证；可选画面功能取决于显卡。本站未构建或试玩。

**代码许可:** [MIT covers the repository’s authored code. Third-party libraries and fonts retain their own licenses; the original arcade game’s ROM, code and data retain their owners’ rights.](https://github.com/snicolast/LostWorldNative/blob/master/LICENSE)  
**作者:** snicolast  
[官方文档](https://github.com/snicolast/LostWorldNative/blob/master/README.md) · 资料核对日期: 2026-10-28

</details>

### [HarmonyRecomp](https://github.com/Wrexxial/HarmonyRecomp)

从自备 XBLA《绝望和声》包构建的 Windows 移植，提供画面设置与最多六人的局域网／虚拟局域网合作。

原作或参考对象: **恶魔城：绝望和声（Xbox 360）** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/Wrexxial/HarmonyRecomp/blob/main/README.md#building) · [浏览 RemakeList](https://remakelist.com/zh/remakes/harmony-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=harmony-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · 本机构建

**当前阶段:** 源码构建 · 局域网合作 · 需原版 XBLA 包

**需要准备什么:** 需自备合法取得的 Xbox 360 XBLA 58410A7A 游戏包，来自自有主机或购买内容；可选 DLC 包也须自备。不要再分发提取素材或生成的原作代码。

**现在能用什么:** 尚无发行二进制。Python build.py 会提取自备包、取得固定版本 SDK，并使用 Clang 20+、CMake、Ninja 在本地构建。作者报告支持全部关卡与六名基础角色；DLC 安装未用真实 DLC 包测试，关闭时可能出现堆损坏崩溃报告。合作需相同源码版本及局域网／虚拟局域网，并非 Xbox Live。本站未构建或试玩。

**代码许可:** [The project code is BSD-3-Clause; the extractor includes MIT-licensed NocturneRecomp code. Runtime dependencies retain their terms, and original game code/data are outside these grants.](https://github.com/Wrexxial/HarmonyRecomp/blob/main/LICENSE)  
**作者:** Wrexxial  
[官方文档](https://github.com/Wrexxial/HarmonyRecomp/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Underground 2 Android Evolved](https://github.com/codepdbh/nfsu2-recompiled)

将 PC 版《地下狂飙 2》带到 Android，提供触屏操作和图形设置；需自备受支持的 PC 原版文件。

原作或参考对象: **《极品飞车：地下狂飙 2》PC 版** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/codepdbh/nfsu2-recompiled/releases/tag/v0.14.11) · [浏览 RemakeList](https://remakelist.com/zh/remakes/nfsu2-android-evolved/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nfsu2-android-evolved-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Android 10+（ARM64／ARMv7），Vulkan 1.1+；Windows x86 需源码构建

**当前阶段:** v0.14.11 Android APK · Windows 源码构建

**需要准备什么:** 需自备受支持的 PC 安装数据及指定 SPEED2.EXE（4,800,512 字节），再导入游戏文件；其他程序版本或发行版未必兼容。

**现在能用什么:** v0.14.11 提供 ARM64 与 ARMv7 APK 及校验值；发行说明仅称细节修复，明确没有性能或玩法变化。Windows 有源码构建说明，本次发行没有 Windows 成品包。 设备与驱动兼容性存在差异；Windows 需本地编译工具链。README 下载段仍写 v0.14.9，此处以已核对的 v0.14.11 发行页为准。

**源码可见；使用受许可限制:** [The README declares MIT for the author’s original tooling. No standalone project license was verified. This statement does not license the original executable, game code or assets.](https://github.com/codepdbh/nfsu2-recompiled/blob/main/README.md)  
**作者:** codepdbh  
[官方文档](https://github.com/codepdbh/nfsu2-recompiled/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [LASRecomp Android](https://github.com/mamcjr/LASRecompAndroid)

LASRecomp 的 Android 分支，提供移动操作与设备端编译；需自备受支持的 Switch《织梦岛》文件。

原作或参考对象: **《塞尔达传说：织梦岛》Switch 版** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/mamcjr/LASRecompAndroid/releases/tag/v0.5.7) · [浏览 RemakeList](https://remakelist.com/zh/remakes/las-recomp-android/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=las-recomp-android-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Android 11+ ARM64；兼容 Vulkan GPU／驱动

**当前阶段:** v0.5.7 预发布 · Android · 设备端构建

**需要准备什么:** 需自备 Switch《织梦岛》1.0.0、1.0.1 或 1.1.0 的 ExeFS 与 RomFS，并保持可执行程序与数据版本匹配。

**现在能用什么:** v0.5.7 为 ARM64 Android 11+ 预发布 APK；设置约需 12 GB 可用空间并在手机上编译。存在 Vulkan 1.1／1.2 回退路径，效果取决于设备。 验证主要使用骁龙 8 Elite／Adreno 830 的 POCO F7 Ultra；Adreno 较好表现可能依赖 Turnip。强制回退路径测试不能证明真实 Mali 支持，v0.5.7 未在真实 Mali 设备测试。

**代码许可:** [The Android port and upstream project code have scoped MIT notices. Third-party components retain their licenses; original Nintendo data and generated game code are outside that grant.](https://github.com/mamcjr/LASRecompAndroid/blob/main/LICENSE)  
**作者:** mamcjr  
[官方文档](https://github.com/mamcjr/LASRecompAndroid/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Project Stonehenge](https://github.com/Onaga00/ProjectStonehenge)

《皇牌空战 04》的 Windows 原生重建，提供现代显示设置；需自备美版 PS2 游戏镜像。

原作或参考对象: **《皇牌空战 04》PS2 版** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/Onaga00/ProjectStonehenge/releases/tag/Beta) · [浏览 RemakeList](https://remakelist.com/zh/remakes/project-stonehenge/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=project-stonehenge-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64；Vulkan 1.2

**当前阶段:** 0.9.6 下载包 · Beta 发行标签 · Windows

**需要准备什么:** 需自备美版 PS2 光盘 SLUS-20152，使用每扇区 2048 字节的标准 ISO9660 镜像；不支持原始 BIN／CUE。

**现在能用什么:** 发行标签为 Beta，所附 Windows 包版本是 0.9.6；作者报告完整战役可玩，但仍属于 Beta。 Beta 兼容性与高帧率表现来自作者声明，不能保证所有机器；GitHub 未勾选预发布不代表已完成正式版。

**代码许可:** [Project code is GPL-3.0. The license does not cover original game assets, trademarks or disc data; dependencies retain their own terms.](https://github.com/Onaga00/ProjectStonehenge/blob/main/LICENSE)  
**作者:** Onaga00  
[官方文档](https://github.com/Onaga00/ProjectStonehenge/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Project 8 Plus](https://github.com/MaxLeiter/project-8-plus)

《托尼霍克 Project 8》的桌面原生移植，提供现代图形与模组工具；需自备受支持的 PS3 游戏及更新文件。

原作或参考对象: **《托尼霍克 Project 8》PS3 版** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/MaxLeiter/project-8-plus/releases/tag/v0.9.2) · [浏览 RemakeList](https://remakelist.com/zh/remakes/project-8-plus/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=project-8-plus-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64、Direct3D 12；实验性 Linux x86_64

**当前阶段:** v0.9.2 · Windows · Linux 实验支持

**需要准备什么:** 需自备美版 PS3 BLUS30011 游戏文件夹及 01.02 更新，并完成文档要求的 RPCS3 准备；可选高清包不提供原版游戏纹理。

**现在能用什么:** v0.9.2 提供 Windows 设置包、实验性 Linux 压缩包与可选高清模型／工具包；Windows 设置需联网及约 4 GB 空间，作者估计需 20–25 分钟。 Linux 仍为实验支持；已有安装需重新构建才能应用 v0.9.2 共享存档变更。可选升频需要本地处理，不代表普遍提升画质或性能已经验证。

**代码许可:** [Project code is MIT; the optional upscaling model is CC-BY-4.0 and dependencies have their own notices. Original game content is excluded.](https://github.com/MaxLeiter/project-8-plus/blob/master/LICENSE)  
**作者:** MaxLeiter  
[官方文档](https://github.com/MaxLeiter/project-8-plus/blob/master/README.md) · 资料核对日期: 2026-10-28

</details>

### [2014 FIFA World Cup Brazil: Recompiled](https://github.com/HossEz/fifa-world-cup-2014-recompiled)

将 Xbox 360 版世界杯足球游戏移植到 Windows，通过启动器导入自备光盘镜像或已提取的游戏文件夹。

原作或参考对象: **2014 FIFA 世界杯巴西** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/HossEz/fifa-world-cup-2014-recompiled/releases/tag/v0.1.10) · [浏览 RemakeList](https://remakelist.com/zh/remakes/fifa-world-cup-2014-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fifa-world-cup-2014-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · Direct3D 12 · SSE4.2

**当前阶段:** v0.1.10 - 预览版 - 需原版素材

**需要准备什么:** 自备 Xbox 360 原版 ISO，或含 default.xex 的文件夹；项目不提供游戏数据。

**现在能用什么:** v0.1.10 提供 Windows 安装器与便携 ZIP，启动器检查导入游戏；仍需满足处理器与显卡要求。Intel UHD 与 Iris Xe 使用较慢的渲染路径，高分辨率过场、回放和庆祝仍可能低于 60 帧。以上来自作者说明，并非本站全流程实测。

**代码许可:** [BSD-3-Clause covers the author's launcher, fixes, SDK patches and tools. It excludes the original game and recompiled game code; dependencies retain their own licenses.](https://github.com/HossEz/fifa-world-cup-2014-recompiled/blob/main/LICENSE)  
**作者:** HossEz  
[官方文档](https://github.com/HossEz/fifa-world-cup-2014-recompiled/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Smash 4 PC](https://github.com/josiahg2502-glitch/Smash4PC)

将 Wii U 版《任天堂明星大乱斗》移植到 Windows，通过启动器选择自备游戏、更新和可选 DLC 文件。

原作或参考对象: **任天堂明星大乱斗 Wii U** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/josiahg2502-glitch/Smash4PC/releases/tag/v0.1.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/smash4pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=smash4pc-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · Vulkan 1.3

**当前阶段:** v0.1.0 - 预览版 - 需原版素材

**需要准备什么:** 自备美版 Wii U 游戏导出数据，建议使用 v304；DLC 另需自备。Pretendo 还需要本人 Wii U 主机文件及账号。

**现在能用什么:** v0.1.0 提供 Windows ZIP。README 说明支持原始 v1.0 或 v304 更新；着色器在首次使用时编译。高于 60 帧的画面采用插帧，游戏模拟仍为 60 帧。README 提醒生成程序含游戏代码，不应上传；发行包如何处理该代码尚未经本站审计。联网与各模式功能未由本站实测。

**代码许可:** [Project-authored code is MIT; Cemu-derived network code is MPL-2.0 and other components retain their notices. None of these licenses grants rights to Nintendo game code or assets.](https://github.com/josiahg2502-glitch/Smash4PC/blob/main/LICENSE)  
**作者:** josiahg2502-glitch  
[官方文档](https://github.com/josiahg2502-glitch/Smash4PC/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Glassline](https://github.com/MoonCellar-Team/Glassline)

将 iPad 版《镜之边缘》带到桌面、Android 与浏览器，加入现代操作方式及可选的一对一联网玩法。

原作或参考对象: **镜之边缘 iPad 版** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/MoonCellar-Team/Glassline/releases/tag/v1.3.1) · [浏览 RemakeList](https://remakelist.com/zh/remakes/glassline/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=glassline-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64 · Linux x64／Steam Deck · Android 9+ · 浏览器

**当前阶段:** v1.3.1 - 需设置 - 需原版素材

**需要准备什么:** 自备 iPad 版《镜之边缘》1.1.48 或更新版本 IPA；不支持 iPhone 版，项目不提供原作数据。

**现在能用什么:** v1.3.1 提供 Windows、Linux、Android 与 Web 包，作者也托管浏览器版本。没有原生 macOS 发行包，macOS 使用浏览器路线。源码可见，但不是开源。联网仅限一对一，并依赖 MoonCellar 服务；账号功能遵循该服务条款。浏览器须具备指定 WebAssembly、存储与图形能力，清理站点数据会删除本地游戏文件和存档；增强特效需 OpenGL ES 3.0。

**源码可见；使用受许可限制:** [The custom license permits specified personal noncommercial use of the author's work. Redistribution, modified builds and commercial use need separate permission. EA's original code and assets are excluded; dependencies retain their licenses.](https://github.com/MoonCellar-Team/Glassline/blob/main/LICENSE)  
**作者:** MoonCellar-Team  
[官方文档](https://github.com/MoonCellar-Team/Glassline/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [RE: Outbreak](https://github.com/Ninjacornix/reo)

为《生化危机：爆发》File #1 提供 Windows 移植，通过引导在本机编译游戏，支持操作设置与可选 openSNAP 合作模式。

原作或参考对象: **生化危机：爆发 File #1** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/Ninjacornix/reo/releases/tag/v1.0.19) · [浏览 RemakeList](https://remakelist.com/zh/remakes/reo-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=reo-native-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64 · .NET 8 Desktop Runtime · Vulkan

**当前阶段:** v1.0.19 - 需设置 - 需本机构建与原版素材

**需要准备什么:** 仅支持原版 NTSC-U v2.00 File #1 ISO，编号 SLUS-20765。本机编译后仍须保留 ISO；不支持 PAL、日版、修改版本和 File #2。

**现在能用什么:** v1.0.19 提供 Windows 启动器和依赖源码归档。首次设置需下载工具并在本机编译，约需 10 GB 可用空间，可能超过一小时。File #2 与可玩 Linux 包尚未提供。全流程可玩是作者声明；互联网主机需可达网络或 VPN，参与者可见主机 IP，CPU 负载较高的房间可能变慢。

**代码许可:** [This fork's original contributions use GPL-3.0-only. Upstream and third-party code retains its own notices. Original game content and generated game code are not licensed by this grant.](https://github.com/Ninjacornix/reo/blob/main/LICENSE)  
**作者:** Ninjacornix  
[官方文档](https://github.com/Ninjacornix/reo/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [SegaSonic Native Port](https://github.com/cheviman/segasonic-port)

世嘉三人街机游戏的原生移植，提供桌面与掌机路线，需自备精确匹配的街机 ROM 集合。

原作或参考对象: **SegaSonic 刺猬索尼克（街机）** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/cheviman/segasonic-port/releases/tag/v1.2.2) · [浏览 RemakeList](https://remakelist.com/zh/remakes/segasonic-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=segasonic-port-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64 · Linux x64 · macOS 11+ · Anbernic H700 · Android／Switch 包本机生成

**当前阶段:** v1.2.2 - 需设置 - 需原版素材

**需要准备什么:** 自备 SegaSonic The Hedgehog 日版 rev. C 的 sonic.zip，包含要求的 18 个文件。导入生成 segasonic.assets；生成的移动或主机包含自备素材，不应分享。

**现在能用什么:** v1.2.2 提供 Windows、Linux、通用 macOS 和 Anbernic H700 包。Android 7+ APK 与 Switch 包需用附带工具在自己的电脑生成，并非独立现成下载。作者报告与 MAME 对照并在部分系统游玩，本站未复测。三人支持指本地游玩，不代表互联网联机；macOS 应用未签名。

**代码许可:** [Project code uses BSD-3-Clause; MAME/ymfm-derived components, SDL and Kenney assets have their own BSD, zlib or CC0 terms. Original Sega ROMs and assets are not licensed by the project.](https://github.com/cheviman/segasonic-port/blob/main/LICENSE)  
**作者:** cheviman  
[官方文档](https://github.com/cheviman/segasonic-port/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [Stunt Race FX DECOMP](https://github.com/Mabec-games/Stunt-Race-FX-DECOMP)

SNES Super FX 赛车游戏的实验性 Linux 移植，保留原版游戏逻辑，同时绘制更流畅、更高分辨率的画面。

原作或参考对象: **特技赛车 FX** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/Mabec-games/Stunt-Race-FX-DECOMP/releases/tag/beta-0.1) · [浏览 RemakeList](https://remakelist.com/zh/remakes/stunt-race-fx-decomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=stunt-race-fx-decomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Linux x86-64

**当前阶段:** beta-0.1 - 预览版 - 需原版素材

**需要准备什么:** 自备 Stunt Race FX 美版 rev. 1 ROM，SHA-1 为 781e376ff453a83c7bcf72339abe6b842efd9c86；移植不含游戏数据。

**现在能用什么:** beta-0.1 已提供 Linux x86-64 AppImage。README 所说稍后发布 AppImage 已落后于实际附件；另有源码构建说明。早期 Beta，以 Speed Trax 尤其初级赛道的验证较多；其他赛道与模式仍不完整。菜单、选车和双人对战保留原分辨率、不插帧；60 帧画面不改变原版模拟速度。

**代码许可:** [The upstream decompilation and this fork are offered under CC0-1.0. Nintendo/Argonaut's original game and ROM contents remain separately protected and are not supplied.](https://github.com/Mabec-games/Stunt-Race-FX-DECOMP/blob/main/LICENSE)  
**作者:** Mabec-games  
[官方文档](https://github.com/Mabec-games/Stunt-Race-FX-DECOMP/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [God of War: Ascension PC](https://github.com/otavix010/gow-ascension-pc)

PS3《战神：升天》的实验性 Windows 移植，通过作者的 Otavix 启动器或构建脚本，从自备受支持光盘在本机生成。

原作或参考对象: **战神：升天** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/otavix010/otavix-launcher/releases/tag/v1.0.50) · [浏览 RemakeList](https://remakelist.com/zh/remakes/gow-ascension-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gow-ascension-pc-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows x64 · Direct3D 12 · 本机编译

**当前阶段:** 早期 - 需本机构建与原版素材

**需要准备什么:** 自备美版 PS3 光盘 BCUS98232、精确 1.04 更新和 PS3 固件。作者列出索尼官方依赖来源；不支持 1.05 及之后更新。

**现在能用什么:** 作者入口指向 Otavix Launcher v1.0.50，用于下载移植支持文件并在本机构建游戏。移植仓库最新 shaders 标签是着色器包，不是游戏发行版本。作者仅报告检查了开场关卡和第 16 章，未验证全流程。CPU 能力明显影响性能，高于 60 帧可能加速游戏逻辑。启动器的可选社区着色器共享在接受后才上传着色器，需单独查看该设置。

**代码许可:** [MIT covers the author's code and tools; scripts/gpl contains GPL-2.0 helpers and dependencies retain their terms. The license excludes the original game, firmware and generated game output.](https://github.com/otavix010/gow-ascension-pc/blob/main/LICENSE)  
**作者:** otavix010  
[官方文档](https://github.com/otavix010/gow-ascension-pc/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [2010 FIFA World Cup South Africa: Recompiled](https://github.com/CalinGraphics/fifa-world-cup-2010-recompiled)

Xbox 360 世界杯足球游戏的 Windows 移植，目前可按文档从源码构建，需自备受支持光盘。

原作或参考对象: **2010 FIFA 世界杯南非** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/CalinGraphics/fifa-world-cup-2010-recompiled/blob/main/README.md) · [浏览 RemakeList](https://remakelist.com/zh/remakes/fifa-world-cup-2010-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fifa-world-cup-2010-recompiled-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · Direct3D 12 · SSE4.2

**当前阶段:** 早期 - 需本机构建与原版素材

**需要准备什么:** 自备带英语、西班牙语、荷兰语的精确欧洲 Xbox 360 版本，default.xex 与 fifadllzf.xex 哈希均须匹配；不支持 PS3 或其他区域。

**现在能用什么:** 2026 年 10 月 28 日 GitHub 没有发行记录，虽然 README 存在下载按钮。应使用 BUILDING.md 与 build.ps1；作者称首次 SDK 和游戏构建可能约需一小时。不支持联网／Xbox Live。菜单与过场仍为 30 帧，作者尚未完成所有模式全流程测试。已定位图片是作者的启动器截图，不作为实机玩法证明。

**代码许可:** [BSD-3-Clause covers the author's launcher, app, hooks, SDK patches and tools. Original and recompiled game code are excluded, and third-party components keep their licenses.](https://github.com/CalinGraphics/fifa-world-cup-2010-recompiled/blob/main/LICENSE)  
**作者:** CalinGraphics  
[官方文档](https://github.com/CalinGraphics/fifa-world-cup-2010-recompiled/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [BotW Recompiled for Windows](https://github.com/ryderclanky/BotW-Native)

Wii U《旷野之息》的早期 Windows 移植，在本机转换游戏代码并通过 Vulkan 后端绘制。

原作或参考对象: **塞尔达传说：旷野之息（Wii U）** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/ryderclanky/BotW-Native/releases/tag/v0.1.1) · [浏览 RemakeList](https://remakelist.com/zh/remakes/botw-native-windows/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=botw-native-windows-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · Vulkan 1.1 · 本机编译

**当前阶段:** v0.1.1 - 早期 - 需本机构建与原版素材

**需要准备什么:** 自备已提取的 Wii U 美版游戏，应用 v208（1.5.0）更新，包含 code、content、meta 目录且 U-King.rpx 哈希匹配；项目不提供密钥或游戏文件。

**现在能用什么:** v0.1.1 提供含启动器与源码的 Windows ZIP，启动器从自备游戏在本机构建；源码路线使用 MSYS2 UCRT64。此版本并非完整游戏发行。作者仅在近期 NVIDIA 笔记本上检查了列明的开场、战斗、地图、传送与哈特诺场景；手柄映射、特效、过场文字、DLC 和长时间游玩仍不完整或未核实。README 对声音是否可用存在矛盾，因此不确认声音功能。此分支的 Linux 与 Apple 可玩性尚未建立。

**代码许可:** [Project-authored code is MIT; Cemu-derived components stay MPL-2.0, with other dependencies under their own licenses. Nintendo's original game, assets and extracted files are excluded.](https://github.com/ryderclanky/BotW-Native/blob/main/LICENSE)  
**作者:** ryderclanky  
[官方文档](https://github.com/ryderclanky/BotW-Native/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [358/2 Days for Android](https://github.com/sonofskywalker3/khdays-358-android)

Yokimitsuro 原生《王国之心 358/2 天》移植的 Android 分支，在 AYN Thor 上提供双屏布局，手机上则共享单屏。

原作或参考对象: **王国之心 358/2 天** · 基于反编译的项目  
[下载程序并自备游戏文件](https://github.com/sonofskywalker3/khdays-358-android/releases/tag/android-0.1.4-beta6) · [浏览 RemakeList](https://remakelist.com/zh/remakes/khdays-358-android/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=khdays-358-android-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Android 10+ · ARM64 · Vulkan · AYN Thor 双屏支持

**当前阶段:** android-0.1.4-beta6 - 预览版 - 需原版素材

**需要准备什么:** 自备欧版或北美版 DS 卡带 ROM。可选 HD 视频与菜单需自有 HD 1.5+2.5 ReMIX，菜单另需 HD 2.8；项目不提供这些素材。

**现在能用什么:** android-0.1.4-beta6 提供 ARM64 APK，以及用于可选 HD 素材的独立 Windows 辅助程序。作者在 AYN Thor 上测试；手机在同一显示屏呈现两块 DS 画面。Beta 阶段，设备验证以 AYN Thor 为主。自定义外部模组／HD 文件夹会申请 Android 所有文件访问权限。卸载会删除应用本地游戏数据和存档，需先备份；全游戏支持来自作者声明，并非本站试玩。

**代码许可:** [Project code uses MIT with upstream and third-party notices retained. This does not grant rights to Square Enix/Disney game files or optional HD collection assets.](https://github.com/sonofskywalker3/khdays-358-android/blob/master/LICENSE)  
**作者:** sonofskywalker3  
[官方文档](https://github.com/sonofskywalker3/khdays-358-android/blob/master/.github/README.md) · 资料核对日期: 2026-10-28

</details>

### [F.E.A.R. 360 Recompiled](https://github.com/Juansolo457/fear360-recomp)

需从源码构建的 Windows 移植，将 Xbox 360 版 F.E.A.R. 与 F.E.A.R. Files 整合为便于手柄操作的合集。

原作或参考对象: **F.E.A.R.／F.E.A.R. Files（Xbox 360）** · 静态重编译  
[自行构建并自备游戏文件](https://github.com/Juansolo457/fear360-recomp/releases/tag/v0.1.5) · [浏览 RemakeList](https://remakelist.com/zh/remakes/fear360-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fear360-recomp-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · AVX2／FMA · Direct3D 12 · 实验性 Proton／Steam Deck

**当前阶段:** v0.1.5 - 早期 - 需本机构建与原版素材

**需要准备什么:** 自备受支持 Xbox 360 光盘：F.E.A.R. Title ID 565507D9，F.E.A.R. Files 为 565507E8，并匹配设置指南中的程序哈希。

**现在能用什么:** v0.1.5 仅提供源码，没有可执行发行附件。需在 Windows 使用文档指定工具链构建；Steam Deck／Linux 走实验性 Proton 路线，并非原生 Linux 发行。两部战役均未获本站全流程验证。当前绘制为 1280×720，不支持 PC 纹理包；复杂特效、高帧率物理和部分渲染仍有问题，Steam Deck 手柄可能在剧情自动保存时短暂断连。Android 与 Windows ARM64 属于未来工作。

**代码许可:** [Own tools and glue are MIT, fear-nx-derived runtime parts are GPL-3.0-or-later, and renderer/SDK components have MIT/BSD terms. Linked builds include GPL obligations. Original game code, assets and generated private builds must not be redistributed as project downloads.](https://github.com/Juansolo457/fear360-recomp/blob/master/LICENSE)  
**作者:** Juansolo457  
[官方文档](https://github.com/Juansolo457/fear360-recomp/blob/master/README.md) · 资料核对日期: 2026-10-28

</details>

### [ReStreet](https://github.com/samuelit0davila/fifa-street-pc-port)

《FIFA 街头足球》（2012）的 Windows 重编译移植，提供启动器、本地生涯和可选社区服务器联网玩法，需自备 Xbox 360 游戏。

原作或参考对象: **FIFA 街头足球（2012）** · 静态重编译  
[下载程序并自备游戏文件](https://github.com/samuelit0davila/fifa-street-pc-port/releases/tag/v2.1.3-online-beta) · [浏览 RemakeList](https://remakelist.com/zh/remakes/restreet-fifa-street/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=restreet-fifa-street-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** Windows 10/11 x64 · Linux 启动器搭配 Proton（Beta）

**当前阶段:** v2.1.3-online-beta - 预览版 - 需原版素材

**需要准备什么:** 自备《FIFA 街头足球》（2012）Xbox 360 ISO。项目不单独提供原作数据下载；作者明确说明安装器含生成的游戏二进制。

**现在能用什么:** v2.1.3-online-beta 提供 Windows 安装器与原生 Linux 启动器，Linux 游戏本体通过 Proton 运行。README 的 2.0.8 已过时；Windows 增加 World Tour 存档恢复，Linux 启动器尚无此功能。联网 Beta：Linux 房间与邀请仍在测试，作者尚未测试 Steam Deck。Vulkan 可能卡顿或在 AMD 上崩溃，当前内部分辨率为 1280×720；社区服务器另有服务条件。World Tour 生涯丢失时应先停止游玩再恢复旧档，因为只保留最近十份存档。作者未声称生成游戏二进制的分发权已获许可。

**代码许可:** [MIT covers the author's installer, launcher and scripts only; dependencies keep their licenses. The installer contains generated game binaries, and the author explicitly says MIT does not establish redistribution rights or legal clearance for them.](https://github.com/samuelit0davila/fifa-street-pc-port/blob/main/LICENSE)  
**作者:** samuelit0davila  
[官方文档](https://github.com/samuelit0davila/fifa-street-pc-port/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

### [NX2Apple](https://github.com/LNPANDY/NX2Apple)

为 nxnative 增加 Mac 游戏库与图形化构建流程，用自备、受支持的 Switch 文件生成个人 Mac 或 iPhone／iPad App。它是独立的社区分支，不是捆绑游戏合集。

原作或参考对象: **Nintendo Switch 游戏的 Apple 平台构建与管理** · 平台兼容层  
[自行构建并自备游戏文件](https://github.com/LNPANDY/NX2Apple/releases/tag/v0.5.0) · [浏览 RemakeList](https://remakelist.com/zh/remakes/nx2apple/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nx2apple-zh-CN)

<details>
<summary>要求与截图</summary>

**平台:** 构建工具：Apple 芯片 Mac、macOS 13+ · 输出目标：Mac／iPhone／iPad

**当前阶段:** v0.5.0 · 图形化构建工具 · 兼容性按游戏区分

**需要准备什么:** 需自备自己持有的 Switch 卡带或购买内容转储、各游戏配置指定的更新／DLC 和自己的 prod.keys。构建器文档要求 Apple 芯片 Mac、macOS 13+、Xcode／iOS SDK、Python 3.9+ 与 .NET SDK 10；README 的移动端目标为 iOS／iPadOS 26+，实际运行要求因游戏与设备而异。项目不提供游戏文件或密钥；生成的游戏代码和资源包仅供个人设备使用，不可再分发。

**现在能用什么:** v0.5.0 提供 Mac ARM64 启动器，选择 NX2Apple-macOS-arm64.zip；它获取构建工具并在本地生成游戏，不提供即装即玩的游戏 App。该分支报告了《王国之泪》《Hades II》《集合啦！动物森友会》的 iPhone 构建、安装与游玩检查。游戏配置及上游运行报告不等于所有游戏兼容或完整通关。Windows 仅有 Actions 前端，没有本次发行包或完整构建流水线验证。Mods 尚未用真实模组测试；大型游戏受设备内存及签名所保留的内存权限影响，免费 Apple ID 的开发签名七天到期。本站未构建、安装或试玩。

**代码许可:** [MIT covers project code, with upstream attribution and separate third-party notices. It grants no rights to Nintendo game code, assets, keys or the game-derived packages you build.](https://github.com/LNPANDY/NX2Apple/blob/main/LICENSE)  
**作者:** LNPANDY and contributors  
[官方文档](https://github.com/LNPANDY/NX2Apple/blob/main/README.md) · 资料核对日期: 2026-10-28

</details>

## 关于这份清单

清单由 RemakeList 已上线的资料生成。新增、修改和移除项目，都先在网站审核，再自动同步到 GitHub。项目介绍只维护一份。 [数据与同步说明](docs/data.md)

功能平替、重实现和移植是不同的项目关系。代码许可不等于原作素材许可。兼容性和性能说明来自所引资料，不表示 RemakeList 已经安装或实测。本仓库不提供游戏文件、密钥或安装包。部分项目的源码虽可见，许可仍有限制，不能据此称为开源。

可以通过 Issue 推荐项目或纠错，提交前请查看贡献说明中的来源要求。自动生成的项目数据与 README 条目统一从 RemakeList 更新。 [推荐项目](CONTRIBUTING.md)

清单原创文字采用 CC BY 4.0，生成脚本采用 MIT。各项目和第三方内容保留各自的许可，详见 LICENSE 与 NOTICE.md。

[CC BY 4.0](LICENSE) · [MIT](scripts/LICENSE) · [NOTICE](NOTICE.md)
