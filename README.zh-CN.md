# Awesome RemakeList

软件重实现、经典游戏引擎、跨平台移植，以及明确标注的功能平替。由 [RemakeList](https://remakelist.com/zh/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=intro-zh) 整理。

[English](README.md) · **简体中文** · [完整目录](https://remakelist.com/zh/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=directory-zh) · [推荐项目](https://github.com/CharlexH/awesome-remakelist/issues/new?template=project.yml)

每条都写明对应的原作、目前的阶段和开始前要准备的东西。先看清要求，再决定要不要动手。

- 想直接体验：先看每条的「开始方式」。浏览器演示、下载和自行构建是不同路线。
- 想玩老游戏：先看「需要什么」。免费引擎可能仍需自备特定版本的原版文件；演示数据通常只有部分内容。
- 想继续了解：项目名直达官方来源，「要求与截图」进入 RemakeList。所有兼容性和功能说明均基于所引资料，不代表本站已经安装或试玩。

## 目录

- [设计与创作工具](#creative)
- [办公工具与界面再现](#everyday)
- [经典游戏引擎与重制](#classic_games)
- [移植与兼容项目](#ports)

<a id="creative"></a>

## 设计与创作工具

- **[Compositor](https://github.com/robbietilton/Compositor)** — Adobe Photoshop · 独立功能平替。面向 Apple silicon Mac 的图层合成与照片编辑器，采用 Photoshop 式工作流。
  <br>平台: Apple silicon Mac · macOS 26+ · 开始方式: [下载](https://github.com/robbietilton/Compositor/releases) · 现状: 开发中 · 提供发行版
  <br>需要什么: 需要 Apple silicon Mac 和 macOS 26+；源码构建需 Xcode 26+，PSD/PSB 导入仅支持 8-bit RGB。 · [代码许可: MIT](https://github.com/robbietilton/Compositor/blob/main/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/compositor/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=compositor-zh)

- **[PhotoCraft](https://github.com/storytold/photocraft)** — Adobe Photoshop · 工作流重实现。用 Rust 重新实现 Photoshop 式工作流的图像编辑器，目前处于 alpha 阶段。
  <br>平台: Windows / macOS / Linux / FreeBSD / Web · 开始方式: [下载](https://github.com/storytold/photocraft/releases) · 现状: Alpha · 工作流仍在完善
  <br>需要什么: 已有 alpha 下载版；PSD 互操作和插件支持尚不完整，使用前先检查自己的文件和工作流。 · [代码许可: MIT OR Apache-2.0](https://github.com/storytold/photocraft/blob/main/LICENSE-MIT) · [要求与截图](https://remakelist.com/zh/remakes/photocraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=photocraft-zh)

- **[Graphite](https://github.com/GraphiteEditor/Graphite)** — Adobe Illustrator · 独立功能平替。在浏览器中结合图层和节点图进行矢量设计。
  <br>平台: 浏览器 · 开始方式: [浏览器体验](https://editor.graphite.art/) · 现状: Alpha · 可在线体验
  <br>需要什么: 可直接打开浏览器编辑器；目前仍是 alpha，更多创作工作流还在开发中。 · [代码许可: MIT OR Apache-2.0](https://graphite.art/license/) · [要求与截图](https://remakelist.com/zh/remakes/graphite/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=graphite-zh)

- **[Friction](https://github.com/friction2d/friction)** — Adobe After Effects · 独立功能平替。提供矢量工具、时间线和表达式的二维动画与动态图形编辑器。
  <br>平台: Windows / macOS / Linux · 开始方式: [下载](https://friction.graphics/#download) · 现状: 提供桌面下载 · 二维动效
  <br>需要什么: 可下载桌面版；不保证兼容 After Effects 项目和插件，自定义 shader 仍属实验功能。 · [代码许可: GPL-3.0-only](https://github.com/friction2d/friction/blob/main/LICENSE.md) · [要求与截图](https://remakelist.com/zh/remakes/friction/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=friction-zh)

- **[OpenCut](https://github.com/OpenCut-app/OpenCut)** — CapCut / 剪映 · 独立功能平替。采用 CapCut 式剪辑工作流的浏览器视频编辑器，下一版正在重写。
  <br>平台: 浏览器 · 开始方式: [浏览器体验](https://opencut.app/) · 现状: 早期 Beta · 重写中
  <br>需要什么: 官网当前运行的是 classic 早期 beta；桌面端、移动端和自动化等规划尚不能当作稳定功能。 · [代码许可: MIT](https://github.com/OpenCut-app/OpenCut/blob/main/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/opencut/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=opencut-zh)

- **[Penpot](https://github.com/penpot/penpot)** — Figma · 独立功能平替。提供托管和自托管两种方式的协作界面设计与原型工具。
  <br>平台: Browser / self-hosted · 开始方式: [注册体验／自托管](https://design.penpot.app) · 现状: 见官方说明
  <br>需要什么: 注册托管服务账号或自行部署服务器；迁移已有设计需要导出和导入。 · [代码许可: MPL-2.0](https://github.com/penpot/penpot/blob/develop/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/penpot/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=penpot-zh)

- **[VectorCraft](https://github.com/storytold/vectorcraft)** — Adobe Illustrator · 工作流重实现。重新实现 Illustrator 式钢笔、路径和外观工作流的矢量编辑器，目前处于 alpha 阶段。
  <br>平台: Windows / macOS / Linux / Web · 开始方式: [下载](https://getartcraft.com/apps/vectorcraft) · 现状: Alpha
  <br>需要什么: 已有桌面安装包；迁移项目前请先检查复杂文件的导入导出和外观效果。 · [代码许可: MIT OR Apache-2.0](https://github.com/storytold/vectorcraft/blob/main/LICENSE-MIT) · [要求与截图](https://remakelist.com/zh/remakes/vectorcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vectorcraft-zh)

- **[LightCraft](https://github.com/storytold/lightcraft)** — Adobe Lightroom · 工作流重实现。提供照片管理、RAW 显影和非破坏式调色的工具，目前处于 alpha 阶段。
  <br>平台: Windows / macOS / Linux / Web · 开始方式: [下载](https://getartcraft.com/apps/lightcraft) · 现状: Alpha
  <br>需要什么: 已有桌面安装包；相机色彩校准和部分压缩 RAW 格式仍有缺口。 · [代码许可: MIT OR Apache-2.0](https://github.com/storytold/lightcraft/blob/main/LICENSE-MIT) · [要求与截图](https://remakelist.com/zh/remakes/lightcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=lightcraft-zh)

- **[CADCraft](https://github.com/storytold/cadcraft)** — Autodesk AutoCAD · 工作流重实现。提供命令行、对象捕捉、图层和尺寸标注的二维制图工具，仍在早期开发中。
  <br>平台: Windows / macOS / Linux / Web · 开始方式: [下载](https://getartcraft.com/apps/cadcraft) · 现状: 早期开发
  <br>需要什么: 已有桌面安装包；请检查 DWG 兼容性，不能据此假定支持 AutoCAD 的三维功能和行业插件。 · [代码许可: MIT OR Apache-2.0](https://github.com/storytold/cadcraft/blob/main/LICENSE-MIT) · [要求与截图](https://remakelist.com/zh/remakes/cadcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cadcraft-zh)

- **[SoundCraft](https://github.com/storytold/soundcraft)** — Avid Pro Tools · 工作流重实现。提供录音、音轨编辑、混音和 MIDI 编排的音频工作站，目前处于 pre-alpha 阶段。
  <br>平台: Windows / macOS / Linux / Web · 开始方式: [下载](https://getartcraft.com/apps/soundcraft) · 现状: Pre-alpha
  <br>需要什么: 已有桌面安装包；音频设备与缓冲区选择、MIDI 控制器录制及 AAF/OMF 互操作尚未完成。 · [代码许可: MIT OR Apache-2.0](https://github.com/storytold/soundcraft/blob/main/LICENSE-MIT) · [要求与截图](https://remakelist.com/zh/remakes/soundcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=soundcraft-zh)

- **[FilmCraft](https://github.com/storytold/filmcraft)** — Adobe Premiere Pro · 工作流重实现。提供源素材与节目监视器、多轨时间线和修剪功能的视频编辑器，目前处于 alpha 阶段。
  <br>平台: Windows / macOS / Linux · 开始方式: [下载](https://getartcraft.com/apps/filmcraft) · 现状: Alpha
  <br>需要什么: 已有桌面安装包；大型素材处理、效果渲染和专业项目互操作仍有缺口。 · [代码许可: MIT OR Apache-2.0](https://github.com/storytold/filmcraft/blob/main/LICENSE-MIT) · [要求与截图](https://remakelist.com/zh/remakes/filmcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=filmcraft-zh)


<a id="everyday"></a>

## 办公工具与界面再现

- **[ONLYOFFICE Desktop Editors](https://github.com/ONLYOFFICE/DesktopEditors)** — Microsoft Office · 独立功能平替。将离线文档、电子表格、演示文稿和 PDF 编辑整合在一起的桌面办公套件。
  <br>平台: Windows / macOS / Linux · 开始方式: [下载](https://www.onlyoffice.com/download-desktop) · 现状: 提供正式发行版
  <br>需要什么: 本地编辑无需 Microsoft Office 账号；请先检查复杂排版和宏，云协作需另接兼容服务。 · [代码许可: AGPL-3.0](https://github.com/ONLYOFFICE/DesktopEditors/blob/master/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/onlyoffice/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=onlyoffice-zh)

- **[LibreOffice](https://github.com/LibreOffice/core)** — Microsoft Office · 独立功能平替。包含 Writer、Calc 和 Impress 的桌面办公套件，可处理日常文档、表格和演示文稿。
  <br>平台: Windows / macOS / Linux · 开始方式: [下载](https://www.libreoffice.org/download/download-libreoffice/) · 现状: 提供正式发行版
  <br>需要什么: 安装桌面版即可使用，无需 Office 订阅；迁移前请测试 VBA 宏和复杂 Office 模板。 · [代码许可: MPL-2.0 (primarily)](https://www.libreoffice.org/licenses/) · [要求与截图](https://remakelist.com/zh/remakes/libreoffice/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=libreoffice-zh)

- **[Grist](https://github.com/gristlabs/grist-core)** — Microsoft Excel / Airtable · 独立功能平替。将电子表格式编辑与关系数据结合，用于整理表格和关联记录。
  <br>平台: Windows / macOS / Linux · 开始方式: [下载](https://github.com/gristlabs/grist-desktop/releases) · 现状: 提供正式发行版
  <br>需要什么: 可使用本地桌面版、自托管 Community 版，或选择有套餐限制的托管服务。 · [代码许可: Apache-2.0](https://github.com/gristlabs/grist-core/blob/main/LICENSE.txt) · [要求与截图](https://remakelist.com/zh/remakes/grist/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=grist-zh)

- **[Webamp](https://github.com/captbaritone/webamp)** — Winamp 2 · 网页重实现。在浏览器中重现 Winamp 2 的播放器界面和换肤体验。
  <br>平台: Browser · 开始方式: [浏览器体验](https://webamp.org/) · 现状: 见官方说明
  <br>需要什么: 打开浏览器播放器并导入自己的音频即可，无需安装 Winamp。 · [代码许可: MIT](https://github.com/captbaritone/webamp/blob/master/LICENSE.txt) · [要求与截图](https://remakelist.com/zh/remakes/webamp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=webamp-zh)

- **[WinXP in React](https://github.com/ShizukuIchi/winXP)** — Windows XP 桌面 · 界面再现。在浏览器中重现 Windows XP 桌面、开始菜单和部分小应用。
  <br>平台: Browser · 开始方式: [浏览器体验](https://winxp.vercel.app/) · 现状: 见官方说明
  <br>需要什么: 无需 XP 安装文件；这个演示不能运行任意 Windows 软件。 · [代码许可: MIT (project code)](https://github.com/ShizukuIchi/winXP/blob/master/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/winxp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=winxp-zh)

- **[PdfCraft](https://github.com/storytold/pdfcraft)** — Adobe Acrobat · 工作流重实现。提供阅读、批注、页面整理、合并和拆分的 PDF 工具，目前处于早期 alpha 阶段。
  <br>平台: Windows / macOS / Linux / Web · 开始方式: [下载](https://getartcraft.com/apps/pdfcraft) · 现状: 早期 Alpha
  <br>需要什么: 已有桌面安装包；尚未覆盖 Acrobat 的完整编辑、签名和印前工作流。 · [代码许可: MIT OR Apache-2.0](https://github.com/storytold/pdfcraft/blob/main/LICENSE-MIT) · [要求与截图](https://remakelist.com/zh/remakes/pdfcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pdfcraft-zh)


<a id="classic_games"></a>

## 经典游戏引擎与重制

- **[OpenTTD](https://github.com/OpenTTD/OpenTTD)** — Transport Tycoon Deluxe · 游戏重实现。延续 Transport Tycoon 玩法的运输公司经营游戏，并扩展了多人功能。
  <br>平台: Windows / macOS / Linux · 开始方式: [下载](https://www.openttd.org/) · 现状: 见官方说明
  <br>需要什么: 使用免费的 OpenGFX2 或 OpenGFX 基础画面即可，无需原版文件；OpenSFX 音效和 OpenMSX 音乐可选。 · [代码许可: GPL-2.0](https://github.com/OpenTTD/OpenTTD/blob/master/COPYING.md) · [要求与截图](https://remakelist.com/zh/remakes/openttd/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openttd-zh)

- **[OpenRCT2](https://github.com/OpenRCT2/OpenRCT2)** — RollerCoaster Tycoon 2 · 游戏重实现。重新实现 RollerCoaster Tycoon 2，并加入合作多人等改进。
  <br>平台: Windows / macOS / Linux · 开始方式: [下载程序＋自备文件](https://openrct2.io/download) · 现状: 见官方说明
  <br>需要什么: 需要自备 RCT2 数据文件；另有 RCT1 数据时可添加其场景。 · [代码许可: GPL-3.0-or-later](https://github.com/OpenRCT2/OpenRCT2/blob/develop/licence.txt) · [要求与截图](https://remakelist.com/zh/remakes/openrct2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openrct2-zh)

- **[OpenMW](https://github.com/OpenMW/openmw)** — The Elder Scrolls III: Morrowind · 引擎重实现。为 Morrowind 提供现代系统兼容性和图形选项的替代引擎。
  <br>平台: Windows / macOS / Linux · 开始方式: [下载程序＋自备文件](https://www.openmw.org) · 现状: 见官方说明
  <br>需要什么: 需要持有 Morrowind 并配置其数据文件；已有模组需单独检查兼容性。 · [代码许可: GPLv3](https://github.com/OpenMW/openmw/blob/master/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/openmw/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openmw-zh)

- **[OpenRA](https://github.com/OpenRA/OpenRA)** — 红色警戒 1 / Command & Conquer / Dune 2000 · 玩法再创作。以现代操作方式重新演绎经典即时战略游戏，包含初代 Red Alert，而非 Red Alert 2。
  <br>平台: Windows / macOS / Linux · 开始方式: [下载](https://www.openra.net/) · 现状: 见官方说明
  <br>需要什么: 首次启动可按引导获取所需原版素材，或从原版光盘导入；规则和平衡性与原作存在差异。 · [代码许可: GPL-3.0-or-later (engine)](https://github.com/OpenRA/OpenRA/blob/bleed/COPYING) · [要求与截图](https://remakelist.com/zh/remakes/openra/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openra-zh)

- **[fheroes2](https://github.com/ihhub/fheroes2)** — Heroes of Might and Magic II（英雄无敌 II） · 引擎重实现。重新实现 Heroes of Might and Magic II 引擎，并改进现代设备上的操作界面。
  <br>平台: Windows / macOS / Linux / Android · 开始方式: [下载程序＋自备文件](https://github.com/ihhub/fheroes2/releases) · 现状: 有发行版 · 原作或 demo 数据
  <br>需要什么: 自备完整原版数据，或按文档使用官方英文试玩版体验有限内容。 · [代码许可: GPL-2.0-or-later](https://github.com/ihhub/fheroes2/blob/master/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/fheroes2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fheroes2-zh)

- **[OpenXcom](https://github.com/OpenXcom/OpenXcom)** — UFO: Enemy Unknown / Terror from the Deep · 游戏重实现。重新实现两款经典 X-COM 游戏，并支持扩展模组。
  <br>平台: Windows / macOS / Linux · 开始方式: [下载程序＋自备文件](https://github.com/OpenXcom/OpenXcom/releases) · 现状: 桌面引擎 · 需原版数据
  <br>需要什么: 需要未经修改的 UFO: Enemy Unknown 或 Terror from the Deep 数据；Windows 安装器可导入自有 Steam 版本。 · [代码许可: GPL-3.0-or-later](https://github.com/OpenXcom/OpenXcom/blob/master/LICENSE.txt) · [要求与截图](https://remakelist.com/zh/remakes/openxcom/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openxcom-zh)

- **[VCMI](https://github.com/vcmi/vcmi)** — 魔法门之英雄无敌 III · 引擎重实现。支持模组、多人及桌面与移动设备的 Heroes III 替代引擎。
  <br>平台: Windows / macOS / Linux / Android / iOS · 开始方式: [下载程序＋自备文件](https://vcmi.eu/download/) · 现状: 公开发行 · 需原版数据
  <br>需要什么: 完整游戏需要 Heroes III Complete 或 Shadow of Death 数据，仅有 HD Edition 不够；iOS 需通过 TestFlight 或侧载安装。 · [代码许可: GPL-2.0-or-later code](https://github.com/vcmi/vcmi/blob/66fa496c6328a276c4eb14c0011b3a9d751dfac3/license.txt) · [要求与截图](https://remakelist.com/zh/remakes/vcmi/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vcmi-zh)

- **[Julius](https://github.com/bvschaik/julius)** — 凯撒大帝 III · 游戏重实现。忠实延续 Caesar III 的引擎重实现，适用于现代电脑及其他平台。
  <br>平台: Windows · Linux · macOS · Android · 网页（Emscripten）· PS Vita · Nintendo Switch · 开始方式: [下载程序＋自备文件](https://github.com/bvschaik/julius/releases/tag/v1.8.0) · 现状: 已发行 · 需原版游戏数据
  <br>需要什么: 需要完整的 Caesar III 安装文件并更新至 1.0.1.0，同时允许向数据目录写入存档。 · [代码许可: AGPL-3.0](https://github.com/bvschaik/julius/blob/34d1ecd54befb845c0139b371fa8a0438210dac1/LICENSE.txt) · [要求与截图](https://remakelist.com/zh/remakes/julius/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=julius-zh)

- **[CorsixTH](https://github.com/CorsixTH/CorsixTH)** — 主题医院 · 游戏重实现。为 Theme Hospital 带来现代分辨率和桌面系统支持的引擎重实现。
  <br>平台: Windows · macOS · Linux · BSD · 开始方式: [下载程序＋自备文件](https://github.com/CorsixTH/CorsixTH/releases/tag/v0.70.1) · 现状: 已发行 · 需原版或试玩数据
  <br>需要什么: 选择自有 Theme Hospital 数据目录；官方试玩版只有一个关卡，且缺少大部分管理界面。 · [代码许可: MIT](https://github.com/CorsixTH/CorsixTH/blob/master/LICENSE.txt) · [要求与截图](https://remakelist.com/zh/remakes/corsixth/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=corsixth-zh)

- **[Warzone 2100](https://github.com/Warzone2100/warzone2100)** — 战地 2100（1999） · 开放源码续作。由社区持续维护的三维战略游戏，包含战役、自定义单位和桌面多人玩法。
  <br>平台: Windows · macOS · Linux · 网页 · 开始方式: [下载](https://wz2100.net/) · 现状: 已发行 · 桌面与浏览器版本
  <br>需要什么: 官方安装包无需另购原版游戏；浏览器版画面有所精简，不支持在线多人。 · [代码许可: GPL-2.0-or-later and component licenses](https://github.com/Warzone2100/warzone2100/blob/master/COPYING) · [要求与截图](https://remakelist.com/zh/remakes/warzone2100/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=warzone2100-zh)

- **[ScummVM](https://github.com/scummvm/scummvm)** — 经典冒险游戏与角色扮演游戏 · 引擎重实现。通过替代引擎，在现代设备上运行受支持的经典冒险游戏。
  <br>平台: Windows / macOS / Linux / Android / iOS · 开始方式: [下载程序＋自备文件](https://www.scummvm.org/downloads/) · 现状: 已发行 · 兼容性随游戏和平台变化
  <br>需要什么: 自备受支持的游戏数据，或从官方 Freeware Games 页面选择完整免费游戏；兼容性需对应设备上的 ScummVM 版本检查。 · [代码许可: GPL-3.0-or-later engine code](https://github.com/scummvm/scummvm/blob/7d2709da5136866589f7602f5f5a7b17de03420e/COPYING) · [要求与截图](https://remakelist.com/zh/remakes/scummvm/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=scummvm-zh)

- **[RigelEngine](https://github.com/lethal-guitar/RigelEngine)** — 毁灭公爵 II · 引擎重实现。为 Duke Nukem II 提供宽屏、更平滑的移动、快速存档和手柄支持的引擎。
  <br>平台: Windows / macOS / Linux · 开始方式: [下载程序＋自备文件](https://github.com/lethal-guitar/RigelEngine/releases/tag/v0.9.1) · 现状: 已发行 · 维护模式
  <br>需要什么: 需要完整版或有限共享版中的 NUKEM2.CMP；官方 Mac DMG 为 x64，Apple silicon 构建另有链接。 · [代码许可: GPL-2.0-or-later engine code](https://github.com/lethal-guitar/RigelEngine/blob/30afeff8f0b105eac77ee0a2fbd54b06e1a49b60/LICENSE.md) · [要求与截图](https://remakelist.com/zh/remakes/rigelengine/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rigelengine-zh)

- **[OpenLoco](https://github.com/OpenLoco/OpenLoco)** — Chris Sawyer’s Locomotion · 游戏重实现。重新实现 Chris Sawyer’s Locomotion 运输经营游戏，使其适应现代电脑。
  <br>平台: Windows x86/x64 · Linux x64 · macOS Apple silicon · 开始方式: [下载程序＋自备文件](https://openloco.io/download/) · 现状: 已发行 · 需原版游戏数据
  <br>需要什么: 需要自备 Locomotion 原版数据；v26.09 的 Mac 版要求 Apple silicon，尚未签名和公证。 · [代码许可: MIT](https://github.com/OpenLoco/OpenLoco/blob/v26.09/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/openloco/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openloco-zh)

- **[The Force Engine](https://github.com/TheForceEngine/TheForceEngine)** — 星球大战：黑暗力量 · 引擎重实现。为 Dark Forces 加入宽屏、现代鼠标操作和快速存档，并支持原版社区模组。
  <br>平台: Windows / Linux · macOS 需构建 · 开始方式: [下载程序＋自备文件](https://github.com/TheForceEngine/TheForceEngine/releases/tag/v1.22.420) · 现状: 已发行 · 支持 Dark Forces
  <br>需要什么: 需要已购 Dark Forces 的数据及 OpenGL 3.3；Windows 有官方 ZIP，Linux 可用 Flathub，macOS 需源码构建。 · [代码许可: GPL-2.0 engine code](https://github.com/TheForceEngine/TheForceEngine/blob/master/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/the-force-engine/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=the-force-engine-zh)

- **[OpenJazz](https://github.com/AlisterT/openjazz)** — 爵士兔 · 引擎重实现。让初代 Jazz Jackrabbit 在现代桌面系统上运行的替代引擎。
  <br>平台: Windows / macOS / Linux · 开始方式: [下载程序＋自备文件](https://github.com/AlisterT/openjazz/releases/tag/20260301) · 现状: 已发行 · 需原版或试玩数据
  <br>需要什么: 需要完整版或有限共享版数据；Linux x64 发行版要求 glibc 2.35，Mac Source Ports 另提供已签名的 Universal 2 Mac 应用。 · [代码许可: GPL-2.0-or-later engine code](https://github.com/AlisterT/openjazz/blob/master/doc/licenses.txt) · [要求与截图](https://remakelist.com/zh/remakes/openjazz/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openjazz-zh)

- **[DevilutionX](https://github.com/diasurgical/DevilutionX)** — 暗黑破坏神 / 地狱火 · 基于反编译的移植。让 Diablo 和 Hellfire 在现代设备上运行，并提供宽屏、手柄和可选的便利性改进。
  <br>平台: Windows / macOS / Linux / Android / iOS · 开始方式: [下载程序＋自备文件](https://github.com/diasurgical/DevilutionX/releases/tag/1.5.5) · 现状: 已发行 · 完整游戏需自备数据
  <br>需要什么: 完整 Diablo 需要自有 DIABDAT.MPQ，Hellfire 还需额外 MPQ 文件；可使用有限共享版，iOS 需要侧载。 · [源码可见；有限制许可: Sustainable Use License 1.0](https://github.com/diasurgical/DevilutionX/blob/0011dc9670c2093d5ab0084c1cdbeb086556563a/LICENSE.md) · [要求与截图](https://remakelist.com/zh/remakes/devilutionx/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=devilutionx-zh)


<a id="ports"></a>

## 移植与兼容项目

- **[Zelda 64: Recompiled](https://github.com/Zelda64Recomp/Zelda64Recomp)** — Majora’s Mask · 静态重编译。将 Majora’s Mask 重编译为原生桌面版本，并提供现代操作与图形选项。
  <br>平台: Windows / Linux / macOS · 开始方式: [下载程序＋自备文件](https://github.com/Zelda64Recomp/Zelda64Recomp/releases) · 现状: 已发行 · 需原版素材
  <br>需要什么: 需要自有的北美 Nintendo 64 版 Majora’s Mask ROM 和兼容的图形 API；已有 Windows、Linux 和 macOS 安装包。 · [代码许可: GPL-3.0](https://github.com/Zelda64Recomp/Zelda64Recomp/blob/dev/COPYING) · [要求与截图](https://remakelist.com/zh/remakes/zelda64-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=zelda64-recompiled-zh)

- **[D2R Mobile](https://github.com/jhaizhou-ops/d2r-mobile)** — Diablo II: Resurrected · 平台兼容层。让 Switch 版 Diablo II: Resurrected 在兼容 Apple 设备上运行的社区项目。
  <br>平台: iPhone / iPad / Mac · A14 / M1+ · 开始方式: [自行构建＋自备文件](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) · 现状: 需自行做包与自备 Switch 游戏文件
  <br>需要什么: 需要自有 Switch 本体及 Reign of the Warlock 扩展，版本为 1.0.34.0（工具中为 3.3.94012），并备好导出的 ExeFS/RomFS、A14/M1 及以上设备，完成本地构建与签名。旧设备需转换贴图，构建版本须对应系统，包含游戏衍生内容的包不能再分发。 · [代码许可: MIT](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/d2r-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=d2r-mobile-zh)

- **[nxnative](https://github.com/seedds/nxnative)** — Nintendo Switch 游戏 · 平台兼容层。通过本地构建，将受支持的 Switch 游戏制作成 iPhone 和 iPad App 的兼容项目。
  <br>平台: iPhone / iPad · iOS / iPadOS 26+；Mac · 开发构建 · 开始方式: [自行构建＋自备文件](https://github.com/seedds/nxnative#pack-an-ipa) · 现状: 需自行构建 · iPhone 测试为作者报告
  <br>需要什么: 需要 iOS/iPadOS 26+、A17 Pro 及以后 iPhone 或 M1 及以后 iPad、自有游戏 NSP／更新／DLC 和 prod.keys，并在装有 Xcode、Homebrew 的 Mac 上构建后签名侧载。生成的游戏包不能再分发，兼容性须逐个游戏和构建版本确认。 · [代码许可: MIT project code](https://github.com/seedds/nxnative/blob/main/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/nxnative/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nxnative-zh)

- **[MW2 Recompiled](https://github.com/PaulCombal/mw2-recompiled)** — Modern Warfare 2 (2009) · 静态重编译。将 Xbox 360 版 Modern Warfare 2（2009）重编译为 Windows 和 Linux 版本。
  <br>平台: Windows / Linux · 开始方式: [下载程序＋自备文件](https://github.com/PaulCombal/mw2-recompiled/releases) · 现状: 已发行 · 需原版素材
  <br>需要什么: 需要美版或欧版 Xbox 360 光盘 ISO（1.0.557）、64 位 Windows／Linux、Vulkan 1.2、8 GB 空间和手柄。不支持公共匹配；原版网络代码存在已知安全漏洞，联机仅限可信好友。 · [代码许可: GPL-3.0-only](https://github.com/PaulCombal/mw2-recompiled/blob/master/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/mw2-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mw2-recompiled-zh)

- **[Mega Man X4 Recompiled](https://github.com/mstan/MegaManX4Recomp)** — 洛克人 X4 · 静态重编译。将 Mega Man X4 重编译为原生版本，并尝试加入 X／Zero 本地及在线合作。
  <br>平台: Windows / Linux · 开始方式: [下载程序＋自备文件](https://github.com/mstan/MegaManX4Recomp/releases) · 现状: 合作模式 Alpha · 需原光盘
  <br>需要什么: 需要美版 SLUS-00561 的 .cue／.bin 光盘文件；合作玩法为 alpha，需 OpenGL 及相同发行版，Linux x86_64 还需 glibc 2.38+。 · [代码许可: MIT](https://github.com/mstan/MegaManX4Recomp/blob/master/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/mega-man-x4-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mega-man-x4-recompiled-zh)

- **[Birdman64](https://github.com/noahvl/birdman64)** — 飞行俱乐部64 · 基于反编译的移植。为 Pilotwings 64 加入宽屏、手柄和可配置操作的移植项目。
  <br>平台: Windows / Linux · Android 实验版 · iOS 自行构建 · 开始方式: [下载程序＋自备文件](https://github.com/noahvl/birdman64/releases) · 现状: 桌面发行 · 移动端仍属实验
  <br>需要什么: 需要自有美版 ROM，并在首次准备时联网；桌面版提供启动器，Android 属实验支持，iPhone／iPad 需自行构建。 · [代码许可: MIT (project code). The code license grants no rights to the original game, artwork or commercial data.](https://github.com/NoahVl/Birdman64#license) · [要求与截图](https://remakelist.com/zh/remakes/birdman64/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=birdman64-zh)

- **[PeonPad](https://github.com/chrissotraidis/peonpad)** — 魔兽争霸2：黑暗之潮 · 引擎重实现。将 Stratagus／Wargus 的 Warcraft II 引擎带到 iPad 并加入触控操作，目前为开发预览。
  <br>平台: iPadOS 16+ · 开始方式: [下载程序＋自备文件](https://github.com/chrissotraidis/peonpad/releases) · 现状: 开发者预览 · 未签名 IPA · 需自行签名
  <br>需要什么: 需要 iPadOS 16+，自行签名未签名 IPA，并在 Mac／PC 上用 Wargus 将自有 Warcraft II 数据提取为完整的 data.Wargus 文件夹。之后手动复制到应用中，目前没有 App Store 或 TestFlight 版本。 · [代码许可: GPL-2.0 applies to the project’s original code only](https://github.com/chrissotraidis/peonpad/blob/main/LICENSE) · [要求与截图](https://remakelist.com/zh/remakes/peonpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=peonpad-zh)

## 收录与纠错

可以通过 Issue 推荐项目或修正资料，也可以提交 PR 改进清单。[贡献说明](CONTRIBUTING.md)列出了需要提供的来源。首批条目来自已发布的 RemakeList 目录；资料核对日期和官方文档保存在[结构化数据](data/projects.json)中。[数据说明](docs/data.md)

这里同时收录功能平替、界面再现和游戏相关项目，不把它们都叫作「复刻」或「开源」。代码许可不等于原作素材许可；本仓库只提供清单，不提供游戏文件、密钥或安装包。

原创清单文字采用 [CC BY 4.0](LICENSE)，生成脚本采用 [MIT](scripts/LICENSE)。各项目及第三方内容保留自己的许可，见[说明](NOTICE.md)。
