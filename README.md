<a href="https://remakelist.com/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=intro-en"><img src="assets/brand-banner.svg" alt="RemakeList — software recreations and classic game ports" width="920"></a>

# Awesome RemakeList

Software recreations, game engines and native ports, with the requirements you need before trying them.

**English** · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md)

[Browse RemakeList](https://remakelist.com/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=intro-en) · [Suggest a project](https://github.com/CharlexH/awesome-remakelist/issues/new?template=project.yml)

[![Catalog checks](https://github.com/CharlexH/awesome-remakelist/actions/workflows/check.yml/badge.svg?branch=main)](https://github.com/CharlexH/awesome-remakelist/actions/workflows/check.yml) [![Website sync](https://github.com/CharlexH/awesome-remakelist/actions/workflows/sync.yml/badge.svg?branch=main)](https://github.com/CharlexH/awesome-remakelist/actions/workflows/sync.yml)

Project names link to their authors’ sources. Expand an entry for device, game-file and build requirements; RemakeList adds screenshots and setup context.

## Start here

| Project | Explore | Start |
| --- | --- | --- |
| [Graphite](https://remakelist.com/remakes/graphite/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=graphite-featured-en) | Adobe Illustrator | [Try in a browser](https://editor.graphite.art/) |
| [Webamp](https://remakelist.com/remakes/webamp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=webamp-featured-en) | Winamp 2 | [Try in a browser](https://webamp.org/) |
| [OpenTTD](https://remakelist.com/remakes/openttd/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openttd-featured-en) | Transport Tycoon Deluxe | [Download](https://www.openttd.org/) |
| [OpenRCT2](https://remakelist.com/remakes/openrct2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openrct2-featured-en) | RollerCoaster Tycoon 2 | [Download and supply your own game files](https://openrct2.io/download) |
| [D2R Mobile](https://remakelist.com/remakes/d2r-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=d2r-mobile-featured-en) | Diablo II: Resurrected | [Build and supply your own game files](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) |
| [nxnative](https://remakelist.com/remakes/nxnative/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nxnative-featured-en) | Nintendo Switch games | [Build and supply your own game files](https://github.com/seedds/nxnative#pack-an-ipa) |

## Browse category

- [Creative tools](#creative) · 13
- [Everyday tools and interface recreations](#everyday) · 9
- [Game engines and recreations](#classic_games) · 30
- [Ports and compatibility projects](#ports) · 91

<img src="assets/overview-en.svg" alt="Overview" width="920">

<a id="creative"></a>

## Creative tools

### [Compositor](https://github.com/robbietilton/Compositor)

A layer compositing and post-processing editor for Apple silicon Macs, designed around Photoshop-style workflows.

Original or reference: **Adobe Photoshop** · Functional alternative  
[Download](https://github.com/robbietilton/Compositor/releases/tag/v1.5.12) · [Browse RemakeList](https://remakelist.com/remakes/compositor/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=compositor-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Apple silicon Mac · macOS 26+

**Status:** v1.5.12 · Apple silicon · macOS 26+

**What you need:** No Photoshop installation is needed. Requires an Apple silicon Mac and macOS 26+; source builds need Xcode 26+. You are responsible for rights to the edited media.

**What is available:** v1.5.12 provides a DMG for Apple silicon Macs running macOS 26+. Source builds require Xcode 26+. The interface is English-only. PSD/PSB import is limited to 8-bit RGB, not CMYK; some vectors and vertical text are rasterized. RemakeList has not installed or tested it.

**Code license:** [MIT](https://github.com/robbietilton/Compositor/blob/main/LICENSE)  
**Author:** robbietilton  
[Official documentation](https://github.com/robbietilton/Compositor/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [PhotoCraft](https://github.com/storytold/photocraft)

A Rust reimplementation of Photoshop-style image editing workflows by the ArtCraft team, currently in alpha.

Original or reference: **Adobe Photoshop** · Workflow reimplementation  
[Download](https://github.com/storytold/photocraft/releases/tag/v0.17.0) · [Browse RemakeList](https://remakelist.com/remakes/photocraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=photocraft-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux / FreeBSD / Web

**Status:** v0.17.0 · early alpha

**What you need:** No Photoshop installation is required. Images you edit need appropriate rights; bundled fonts/icons have separate licenses. ArtCraft marks are excluded from the code license.

**What is available:** v0.17.0 provides Windows, macOS, Linux, FreeBSD and web packages. This remains an early alpha; the release updates document/artboard handling and rendering, while Photoshop compatibility and professional workflows remain incomplete.

**Code license:** [MIT OR Apache-2.0](https://github.com/storytold/photocraft/blob/main/LICENSE-MIT)  
**Author:** storytold  
[Official documentation](https://github.com/storytold/photocraft/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [Graphite](https://github.com/GraphiteEditor/Graphite)

An open-source vector design tool combining layers and nodes for nondestructive creation in the browser.

Original or reference: **Adobe Illustrator** · Functional alternative  
[Try in a browser](https://editor.graphite.art/) · [Browse RemakeList](https://remakelist.com/remakes/graphite/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=graphite-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Web

**Status:** Alpha · browser editor available

**What you need:** No Illustrator installation or original program files are needed. Bring your own images, fonts and creative assets.

**What is available:** The browser editor is available now for trying vector design without Illustrator. It remains alpha; broader photo-editing, motion, publishing and VFX capabilities are still evolving, so it should not be treated as a replacement for an entire Adobe workflow.

**Code license:** [MIT OR Apache-2.0](https://graphite.art/license/)  
**Author:** Graphite community  
[Official documentation](https://github.com/GraphiteEditor/Graphite/blob/master/README.md) · Sources reviewed: 2026-10-12

</details>

### [Friction](https://github.com/friction2d/friction)

An open-source 2D motion graphics tool with vector and raster animation, timelines and expressions.

Original or reference: **Adobe After Effects** · Functional alternative  
[Download](https://friction.graphics/#download) · [Browse RemakeList](https://remakelist.com/remakes/friction/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=friction-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux

**Status:** Desktop downloads · 2D motion graphics

**What you need:** No After Effects installation is required. Bring your own images, fonts, audio and video assets.

**What is available:** Downloads are listed for Windows, Linux and macOS. It can create 2D animation and motion graphics; custom shader effects remain experimental, and After Effects projects, plugins or complete effects chains are not promised to be compatible.

**Code license:** [GPL-3.0-only](https://github.com/friction2d/friction/blob/main/LICENSE.md)  
**Author:** Ole-André Rodlie &amp; contributors  
[Official documentation](https://friction.graphics/) · Sources reviewed: 2026-10-12

</details>

### [OpenCut](https://github.com/OpenCut-app/OpenCut)

An open-source video editor targeting CapCut-style editing, with a classic early beta online while the next version is rewritten.

Original or reference: **CapCut** · Functional alternative  
[Try in a browser](https://opencut.app/) · [Browse RemakeList](https://remakelist.com/remakes/opencut/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=opencut-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Web

**Status:** Early beta · rewrite in progress

**What you need:** No CapCut installation is required. Import video, images and audio you have rights to use.

**What is available:** The official site currently offers the classic early beta. The classic source is archived and the new version is being rewritten; it is a candidate to explore, without assuming it can fully take over a daily CapCut workflow.

**Code license:** [MIT](https://github.com/OpenCut-app/OpenCut/blob/main/LICENSE)  
**Author:** OpenCut contributors  
[Official documentation](https://github.com/OpenCut-app/OpenCut/blob/main/README.md) · Sources reviewed: 2026-10-12

</details>

### [Penpot](https://github.com/penpot/penpot)

An open-source collaborative design and prototyping platform, hosted or self-hosted.

Original or reference: **Figma** · Functional alternative  
[Sign up or self-host](https://design.penpot.app) · [Browse RemakeList](https://remakelist.com/remakes/penpot/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=penpot-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Browser / self-hosted

**Status:** See official documentation

**What you need:** No Figma software or assets are needed. You must export and import your own designs to migrate them.

**What is available:** Sign up for the hosted service or run your own installation. Moving existing designs requires export and import; check the pricing page for hosted service plans.

**Code license:** [MPL-2.0](https://github.com/penpot/penpot/blob/develop/LICENSE)  
**Author:** penpot  
[Official documentation](https://penpot.app/penpot-vs-figma) · Sources reviewed: 2026-10-11

</details>

### [VectorCraft](https://github.com/storytold/vectorcraft)

An ArtCraft Rust reimplementation of Adobe Illustrator-style workflows: pen drawing, path booleans, appearance effects and vector illustration.

Original or reference: **Adobe Illustrator** · Workflow reimplementation  
[Download](https://github.com/storytold/vectorcraft/releases/tag/v0.18.0) · [Browse RemakeList](https://remakelist.com/remakes/vectorcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vectorcraft-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Status:** v0.18.0 · Alpha

**What you need:** No original commercial application is required. Supply documents and media you have rights to use; bundled fonts, images and brand marks have separate licenses.

**What is available:** v0.18.0 provides desktop installers/archives and a web build. Fixes duplicate threaded text, recovered text flow, compound-path transforms and RGB working-profile changes. Alpha: useful for trying everyday vector drawing; complex file interchange and effect fidelity still need checking. Not installed or fully tested here.

**Code license:** [MIT OR Apache-2.0](https://github.com/storytold/vectorcraft/blob/main/LICENSE-MIT)  
**Author:** ArtCraft  
[Official documentation](https://github.com/storytold/vectorcraft/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [FilmCraft](https://github.com/storytold/filmcraft)

An ArtCraft Rust reimplementation of Adobe Premiere Pro-style workflows: source and program monitors, multitrack timelines and trim editing.

Original or reference: **Adobe Premiere Pro** · Workflow reimplementation  
[Download](https://github.com/storytold/filmcraft/releases/tag/v0.14.0) · [Browse RemakeList](https://remakelist.com/remakes/filmcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=filmcraft-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Status:** v0.14.0 · Alpha

**What you need:** No original commercial application is required. Supply documents and media you have rights to use; bundled fonts, images and brand marks have separate licenses.

**What is available:** v0.14.0 provides desktop installers/archives and a web build. Improves linked audio/video trimming, mask-point selection and Lift/Extract clipboard behavior. Alpha: editing and export workflows exist; large-media performance, effect rendering and professional project interchange remain incomplete. Not installed or fully tested here.

**Code license:** [MIT OR Apache-2.0](https://github.com/storytold/filmcraft/blob/main/LICENSE-MIT)  
**Author:** ArtCraft  
[Official documentation](https://github.com/storytold/filmcraft/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [LightCraft](https://github.com/storytold/lightcraft)

An ArtCraft Rust reimplementation of Adobe Lightroom-style workflows: photo-library management, RAW development and nondestructive color adjustment.

Original or reference: **Adobe Lightroom** · Workflow reimplementation  
[Download](https://github.com/storytold/lightcraft/releases/tag/v0.15.0) · [Browse RemakeList](https://remakelist.com/remakes/lightcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=lightcraft-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Status:** v0.15.0 · Alpha

**What you need:** No original commercial application is required. Supply documents and media you have rights to use; bundled fonts, images and brand marks have separate licenses.

**What is available:** v0.15.0 provides desktop installers/archives and a web build. Adds a Sony α7R V camera profile and improves full-size export and RAW/HEIF decoder resource handling. Alpha: supports trying JPEG, DNG and many camera RAW formats; camera color calibration and some compressed RAW variants remain incomplete. Not installed or fully tested here.

**Code license:** [MIT OR Apache-2.0](https://github.com/storytold/lightcraft/blob/main/LICENSE-MIT)  
**Author:** ArtCraft  
[Official documentation](https://github.com/storytold/lightcraft/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [EffectCraft](https://github.com/storytold/effectcraft)

An ArtCraft Rust reimplementation of Adobe After Effects-style workflows: layer compositing, keyframe animation, motion graphics and effects.

Original or reference: **Adobe After Effects** · Workflow reimplementation  
[Download](https://github.com/storytold/effectcraft/releases/tag/v0.18.0) · [Browse RemakeList](https://remakelist.com/remakes/effectcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=effectcraft-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Status:** v0.18.0 · Alpha

**What you need:** No original commercial application is required. Supply documents and media you have rights to use; bundled fonts, images and brand marks have separate licenses.

**What is available:** v0.18.0 provides desktop installers/archives and a web build. Updates docked panels and composition tabs and fixes focused-text editing and menu behavior. Alpha: suitable for experimenting with animation and compositing, not client delivery. Proprietary project formats and After Effects SDK plug-ins are unsupported. Rendering checks focus on small compositions; macOS is the most-tested platform. RemakeList has not installed or fully tested it.

**Code license:** [MIT OR Apache-2.0](https://github.com/storytold/effectcraft/blob/main/LICENSE-MIT)  
**Author:** ArtCraft  
[Official documentation](https://github.com/storytold/effectcraft/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [DesignCraft](https://github.com/storytold/designcraft)

An ArtCraft Rust reimplementation of Adobe InDesign-style workflows: spread layout, threaded text frames, parent pages and publishing documents.

Original or reference: **Adobe InDesign** · Workflow reimplementation  
[Download](https://github.com/storytold/designcraft/releases/tag/v0.14.0) · [Browse RemakeList](https://remakelist.com/remakes/designcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=designcraft-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Status:** v0.14.0 · Pre-alpha

**What you need:** No original commercial application is required. Supply documents and media you have rights to use; bundled fonts, images and brand marks have separate licenses.

**What is available:** v0.14.0 provides desktop installers/archives and a web build. Improves DOCX table import, footnote editing, PDF document metadata and gradient table-cell output. Pre-alpha: layout and export builds are available; complex publishing files, typography and prepress workflows need individual checks. RemakeList has not installed or fully tested it.

**Code license:** [MIT OR Apache-2.0](https://github.com/storytold/designcraft/blob/main/LICENSE-MIT)  
**Author:** ArtCraft  
[Official documentation](https://github.com/storytold/designcraft/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [SoundCraft](https://github.com/storytold/soundcraft)

An ArtCraft Rust reimplementation of Avid Pro Tools-style workflows: track recording, an edit window, a mixer and MIDI arrangement.

Original or reference: **Avid Pro Tools** · Workflow reimplementation  
[Download](https://github.com/storytold/soundcraft/releases/tag/v0.14.0) · [Browse RemakeList](https://remakelist.com/remakes/soundcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=soundcraft-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Status:** v0.14.0 · Pre-alpha

**What you need:** No original commercial application is required. Supply documents and media you have rights to use; bundled fonts, images and brand marks have separate licenses.

**What is available:** v0.14.0 provides desktop installers/archives and a web build. Fixes Auto Pan stereo handling, paste and Strip Silence behavior, and improves mix-bounce processing. Pre-alpha: recording, editing, mixing and bounce workflows exist; audio-device/buffer selection, MIDI-controller recording and AAF/OMF interchange are still missing. Not installed or fully tested here.

**Code license:** [MIT OR Apache-2.0](https://github.com/storytold/soundcraft/blob/main/LICENSE-MIT)  
**Author:** ArtCraft  
[Official documentation](https://github.com/storytold/soundcraft/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [CADCraft](https://github.com/storytold/cadcraft)

An ArtCraft Rust reimplementation of Autodesk AutoCAD-style workflows: command-line drafting, object snaps, layers, dimensions and drawing layouts.

Original or reference: **Autodesk AutoCAD** · Workflow reimplementation  
[Download](https://github.com/storytold/cadcraft/releases/tag/v0.14.0) · [Browse RemakeList](https://remakelist.com/remakes/cadcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cadcraft-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Status:** v0.14.0 · Early development

**What you need:** No original commercial application is required. Supply documents and media you have rights to use; bundled fonts, images and brand marks have separate licenses.

**What is available:** v0.14.0 provides desktop installers/archives and a web build. Improves drawing recovery and save prompts, DXF text escaping and geometry/constraint handling. Early development: suitable for trying 2D drawings and PDF plotting; it is not a replacement for every AutoCAD 3D, DWG and industry plug-in workflow. Not installed or fully tested here.

**Code license:** [MIT OR Apache-2.0](https://github.com/storytold/cadcraft/blob/main/LICENSE-MIT)  
**Author:** ArtCraft  
[Official documentation](https://github.com/storytold/cadcraft/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>


<a id="everyday"></a>

## Everyday tools and interface recreations

### [ONLYOFFICE Desktop Editors](https://github.com/ONLYOFFICE/DesktopEditors)

An open-source Microsoft Office alternative combining offline document, spreadsheet, presentation and PDF editing in one desktop app.

Original or reference: **Microsoft Office** · Functional alternative  
[Download](https://www.onlyoffice.com/download-desktop) · [Browse RemakeList](https://remakelist.com/remakes/onlyoffice/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=onlyoffice-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux

**Status:** Stable releases available

**What you need:** No Microsoft Office installation or account is needed for local editing. Cloud collaboration requires a compatible service, which may charge.

**What is available:** Installers are available for Windows, macOS and Linux, with local storage and offline editing. Desktop use is free; cloud services and enterprise editions have separate plans. Check complex document layouts before switching.

**Code license:** [AGPL-3.0](https://github.com/ONLYOFFICE/DesktopEditors/blob/master/LICENSE)  
**Author:** ONLYOFFICE  
[Official documentation](https://github.com/ONLYOFFICE/DesktopEditors) · Sources reviewed: 2026-10-12

</details>

### [Grist](https://github.com/gristlabs/grist-core)

An open-source alternative for Excel and Airtable workflows, combining relational data with spreadsheet-style editing.

Original or reference: **Microsoft Excel / Airtable** · Functional alternative  
[Download](https://github.com/gristlabs/grist-desktop/releases) · [Browse RemakeList](https://remakelist.com/remakes/grist/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=grist-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux

**Status:** Community core v1.7.22 · desktop released separately

**What you need:** The desktop app edits local files. Self-hosting requires a server environment; hosted plans require an account and have usage and feature limits.

**What is available:** Community core v1.7.22 adds an in-document Widget Creator, more sorting controls and clearer import/access-rule messages. It has no GitHub release attachments; the README provides Docker and source-run instructions. Desktop packages are released separately, and hosted free/paid plans and enterprise features remain separate choices. Self-hosting needs a server; hosted plans require an account and have usage limits. Its data model differs from Excel.

**Code license:** [Apache-2.0](https://github.com/gristlabs/grist-core/blob/main/LICENSE.txt)  
**Author:** Grist Labs  
[Official documentation](https://github.com/gristlabs/grist-core) · Sources reviewed: 2026-10-30

</details>

### [LibreOffice](https://github.com/LibreOffice/core)

A free, open-source Microsoft Office alternative with Writer, Calc and Impress for documents, spreadsheets and presentations.

Original or reference: **Microsoft Office** · Functional alternative  
[Download](https://www.libreoffice.org/download/download-libreoffice/) · [Browse RemakeList](https://remakelist.com/remakes/libreoffice/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=libreoffice-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux

**Status:** Stable releases available

**What you need:** No Microsoft Office installation, subscription or account is needed. Install the desktop release for your system and use files you have permission to edit.

**What is available:** Downloads are available for Windows, macOS and Linux, with a complete set of everyday office tools. Try your own files first if you rely on VBA macros, complex Office templates or exact layout matching.

**Code license:** [MPL-2.0 (primarily)](https://www.libreoffice.org/licenses/)  
**Author:** The Document Foundation  
[Official documentation](https://www.libreoffice.org/) · Sources reviewed: 2026-10-12

</details>

### [Webamp](https://github.com/captbaritone/webamp)

A browser reimplementation of Winamp 2, with the classic player interface and skin support.

Original or reference: **Winamp 2** · Web reimplementation  
[Try in a browser](https://webamp.org/) · [Browse RemakeList](https://remakelist.com/remakes/webamp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=webamp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Browser

**Status:** See official documentation

**What you need:** No Winamp installation is needed. Audio and third-party skins retain their own rights.

**What is available:** An online player is available to open directly in your browser. No original program is required; bring the audio you want to play.

**Code license:** [MIT](https://github.com/captbaritone/webamp/blob/master/LICENSE.txt)  
**Author:** captbaritone  
[Official documentation](https://github.com/captbaritone/webamp/blob/master/README.md) · Sources reviewed: 2026-10-11

</details>

### [WinXP in React](https://github.com/ShizukuIchi/winXP)

A browser recreation of the Windows XP desktop, Start menu and classic small applications.

Original or reference: **Windows XP desktop** · Interface recreation  
[Try in a browser](https://winxp.vercel.app/) · [Browse RemakeList](https://remakelist.com/remakes/winxp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=winxp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Browser

**Status:** See official documentation

**What you need:** No Windows XP installation files are required.

**What is available:** An online demo is available without Windows XP installation files. It covers the recreated desktop and applications; it cannot run arbitrary XP software.

**Code license:** [MIT (project code)](https://github.com/ShizukuIchi/winXP/blob/master/LICENSE)  
**Author:** ShizukuIchi  
[Official documentation](https://github.com/ShizukuIchi/winXP/blob/master/README.md) · Sources reviewed: 2026-10-11

</details>

### [PdfCraft](https://github.com/storytold/pdfcraft)

An ArtCraft Rust reimplementation of Adobe Acrobat-style workflows: PDF reading, annotations, page organization, merging and splitting.

Original or reference: **Adobe Acrobat** · Workflow reimplementation  
[Download](https://github.com/storytold/pdfcraft/releases/tag/v0.15.0) · [Browse RemakeList](https://remakelist.com/remakes/pdfcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pdfcraft-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Status:** v0.15.0 · Early alpha

**What you need:** No original commercial application is required. Supply documents and media you have rights to use; bundled fonts, images and brand marks have separate licenses.

**What is available:** v0.15.0 provides desktop installers/archives and a web build. Improves XFA forms, imported comments, image clipping and document-opening destinations. Early alpha: reading and page-management workflows are available; it is not a complete substitute for Acrobat editing, signature and prepress workflows. Not installed or fully tested here.

**Code license:** [MIT OR Apache-2.0](https://github.com/storytold/pdfcraft/blob/main/LICENSE-MIT)  
**Author:** ArtCraft  
[Official documentation](https://github.com/storytold/pdfcraft/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [WordCraft](https://github.com/storytold/wordcraft)

An ArtCraft Rust reimplementation of Microsoft Word-style workflows: word processing, styles, tables, tracked changes and document layout.

Original or reference: **Microsoft Word** · Workflow reimplementation  
[Download](https://github.com/storytold/wordcraft/releases/tag/v0.12.0) · [Browse RemakeList](https://remakelist.com/remakes/wordcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wordcraft-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Status:** v0.12.0 · Alpha

**What you need:** No original commercial application is required. Supply documents and media you have rights to use; bundled fonts, images and brand marks have separate licenses.

**What is available:** v0.12.0 provides desktop installers/archives and a web build. Improves DOCX/RTF import details, Arabic list numbering, paragraph layout and LaTeX binomial import. Alpha: writing and DOCX workflows are available to try; pagination, chart/SmartArt round-trip fidelity and native printing still need work. Not installed or fully tested here.

**Code license:** [MIT OR Apache-2.0](https://github.com/storytold/wordcraft/blob/main/LICENSE-MIT)  
**Author:** ArtCraft  
[Official documentation](https://github.com/storytold/wordcraft/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [DeckCraft](https://github.com/storytold/deckcraft)

An ArtCraft Rust reimplementation of Microsoft PowerPoint-style workflows: slide masters, themes, shapes, animation and slide-show playback.

Original or reference: **Microsoft PowerPoint** · Workflow reimplementation  
[Download](https://github.com/storytold/deckcraft/releases/tag/v0.12.0) · [Browse RemakeList](https://remakelist.com/remakes/deckcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=deckcraft-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Status:** v0.12.0 · Alpha

**What you need:** No original commercial application is required. Supply documents and media you have rights to use; bundled fonts, images and brand marks have separate licenses.

**What is available:** v0.12.0 provides desktop installers/archives and a web build. Adds slide-range selection and selective slide reuse, and improves outline import and presentation controls. Alpha: decks can be created and presented; complex PPTX files and animation behavior should not be assumed identical to PowerPoint. Not installed or fully tested here.

**Code license:** [MIT OR Apache-2.0](https://github.com/storytold/deckcraft/blob/main/LICENSE-MIT)  
**Author:** ArtCraft  
[Official documentation](https://github.com/storytold/deckcraft/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [GridCraft](https://github.com/storytold/gridcraft)

An ArtCraft Rust reimplementation of Microsoft Excel-style workflows: worksheets, formulas, tables, charts and pivot-table workflows.

Original or reference: **Microsoft Excel** · Workflow reimplementation  
[Download](https://github.com/storytold/gridcraft/releases/tag/v0.13.0) · [Browse RemakeList](https://remakelist.com/remakes/gridcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gridcraft-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / ARM64 / x86 · macOS universal · Linux x86_64 / ARM64 / RISC-V64 · FreeBSD x86_64 · Web

**Status:** v0.13.0 · Alpha

**What you need:** No original commercial application is required. Supply documents and media you have rights to use; bundled fonts, images and brand marks have separate licenses.

**What is available:** v0.13.0 provides desktop installers/archives and a web build. Improves formula edge cases, preserves worksheet identifiers on XLSX rewrites and can open saved workbooks without recalculating. Alpha: core spreadsheet workflows can be tried; real-world XLSX fidelity, large-workbook performance, chart depth and legacy-format import still need work. Not installed or fully tested here.

**Code license:** [MIT OR Apache-2.0](https://github.com/storytold/gridcraft/blob/main/LICENSE-MIT)  
**Author:** ArtCraft  
[Official documentation](https://github.com/storytold/gridcraft/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>


<a id="classic_games"></a>

## Game engines and recreations

### [Vanguard Engine](https://github.com/harshilmathur/openra2)

An independent browser RTS engine for Red Alert 2 data, currently focused on a Soviet single-player skirmish development slice.

Original or reference: **Red Alert 2 / Yuri’s Revenge data** · Engine reimplementation  
[Build from source](https://github.com/harshilmathur/openra2/blob/master/README.md#quickstart) · [Browse RemakeList](https://remakelist.com/remakes/vanguard/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vanguard-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Browser · local development server

**Status:** Development slice · no formal release

**What you need:** Classic mode needs legally owned RA2/YR files. Original mode uses repository-authored assets and needs no original game; the modes remain separate. Requires Node.js 20.19+ and a local development server.

**What is available:** This is a development slice with no formal release, requiring Node.js 20.19+ and a local development server. Classic mode needs lawfully obtained RA2/YR files; Original mode needs no original game. Allied forces, netplay and Yuri gameplay are not complete, so this is not a full Red Alert 2 recreation.

**Code license:** [GPL-3.0-or-later](https://github.com/harshilmathur/openra2/blob/master/LICENSE)  
**Author:** harshilmathur  
[Official documentation](https://github.com/harshilmathur/openra2/blob/master/README.md) · Sources reviewed: 2026-10-12

</details>

### [OpenTTD](https://github.com/OpenTTD/OpenTTD)

Transport Tycoon gameplay rebuilt for modern platforms, with expanded multiplayer support.

Original or reference: **Transport Tycoon Deluxe** · Game reimplementation  
[Download](https://www.openttd.org/) · [Browse RemakeList](https://remakelist.com/remakes/openttd/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openttd-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux

**Status:** See official documentation

**What you need:** Base graphics are required; use free OpenGFX2 or OpenGFX. OpenSFX sound and OpenMSX music are optional. This free route does not need original game files.

**What is available:** Desktop releases are available. Start with the required free OpenGFX2 or OpenGFX graphics; OpenSFX sound and OpenMSX music are optional. No original game files are needed for this route.

**Code license:** [GPL-2.0; third-party components have separate licenses](https://github.com/OpenTTD/OpenTTD/blob/master/COPYING.md)  
**Author:** OpenTTD  
[Official documentation](https://github.com/OpenTTD/OpenTTD/blob/master/README.md) · Sources reviewed: 2026-10-11

</details>

### [OpenRCT2](https://github.com/OpenRCT2/OpenRCT2)

RollerCoaster Tycoon 2 on modern platforms, with improvements including cooperative multiplayer.

Original or reference: **RollerCoaster Tycoon 2** · Game reimplementation  
[Download and supply your own game files](https://openrct2.io/download) · [Browse RemakeList](https://remakelist.com/remakes/openrct2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openrct2-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux

**Status:** See official documentation

**What you need:** You must supply original RCT2 data files. RCT1 data can add scenarios.

**What is available:** Releases are available, but you must supply original RCT2 data files. RCT1 data can add its scenarios; the free engine does not include the original commercial assets.

**Code license:** [GPL-3.0-or-later](https://github.com/OpenRCT2/OpenRCT2/blob/develop/licence.txt)  
**Author:** OpenRCT2  
[Official documentation](https://github.com/OpenRCT2/OpenRCT2/blob/develop/readme.md) · Sources reviewed: 2026-10-11

</details>

### [OpenMW](https://github.com/OpenMW/openmw)

A modern open-source engine for Morrowind, improving compatibility and graphics options.

Original or reference: **The Elder Scrolls III: Morrowind** · Engine reimplementation  
[Download and supply your own game files](https://www.openmw.org) · [Browse RemakeList](https://remakelist.com/remakes/openmw/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openmw-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux

**Status:** See official documentation

**What you need:** Playing Morrowind requires owning the original game and configuring its data files.

**What is available:** The engine is available to download, but playing Morrowind requires owning the original game and configuring its data files. Some original mods are incompatible, so check support for your existing mod setup.

**Code license:** [GPLv3; some fonts separately licensed](https://github.com/OpenMW/openmw/blob/master/LICENSE)  
**Author:** OpenMW  
[Official documentation](https://github.com/OpenMW/openmw/blob/master/README.md) · Sources reviewed: 2026-10-11

</details>

### [OpenRA](https://github.com/OpenRA/OpenRA)

Classic real-time strategy games reimagined with modern controls and three official game mods.

Original or reference: **Red Alert 1 / Command &amp; Conquer / Dune 2000** · Game reimagining  
[Download](https://www.openra.net/) · [Browse RemakeList](https://remakelist.com/remakes/openra/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openra-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux

**Status:** See official documentation

**What you need:** Original game assets are still used. The official installer can fetch required assets on first run or import them from original discs.

**What is available:** Downloads are available for Windows, macOS and Linux. Original game assets are required; the project says first-run setup can fetch the required assets or import them from original discs.

**Code license:** [GPL-3.0-or-later (engine)](https://github.com/OpenRA/OpenRA/blob/bleed/COPYING)  
**Author:** OpenRA  
[Official documentation](https://www.openra.net/about/) · Sources reviewed: 2026-10-11

</details>

### [fheroes2](https://github.com/ihhub/fheroes2)

A recreation of the Heroes of Might and Magic II engine for desktop and Android, with modern improvements.

Original or reference: **Heroes of Might and Magic II** · Engine reimplementation  
[Download and supply your own game files](https://github.com/ihhub/fheroes2/releases) · [Browse RemakeList](https://remakelist.com/remakes/fheroes2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fheroes2-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux / Android

**Status:** Releases available · original/demo data

**What you need:** Requires full original-game data or official English demo data; INSTALL.md documents the bundled demo-download path. Demo assets provide only their licensed limited content.

**What is available:** Releases require full original-game data or official English demo data; installation guidance explains how to obtain the demo. The demo contains limited content, full play still requires legally owned original assets, and setup differs by platform.

**Code license:** [GPL-2.0-or-later](https://github.com/ihhub/fheroes2/blob/master/LICENSE)  
**Author:** ihhub  
[Official documentation](https://github.com/ihhub/fheroes2/blob/master/README.md) · Sources reviewed: 2026-10-12

</details>

### [OpenXcom](https://github.com/OpenXcom/OpenXcom)

A desktop reimplementation of the two classic X-COM games, with support for additional mods.

Original or reference: **UFO: Enemy Unknown / Terror from the Deep** · Game reimplementation  
[Download and supply your own game files](https://github.com/OpenXcom/OpenXcom/releases) · [Browse RemakeList](https://remakelist.com/remakes/openxcom/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openxcom-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux

**Status:** Desktop engine · original data required

**What you need:** Requires unmodified original data from UFO: Enemy Unknown or Terror from the Deep. The Windows installer can extract resources from your owned Steam copy.

**What is available:** Desktop releases require unmodified original data from either game. The Windows installer can extract assets from your owned Steam copy; additional mods may have their own asset requirements.

**Code license:** [GPL-3.0-or-later](https://github.com/OpenXcom/OpenXcom/blob/master/LICENSE.txt)  
**Author:** OpenXcom  
[Official documentation](https://github.com/OpenXcom/OpenXcom/blob/master/README.md) · Sources reviewed: 2026-10-12

</details>

### [VCMI](https://github.com/vcmi/vcmi)

An open-source Heroes III engine with desktop and mobile builds, mod support and multiplayer.

Original or reference: **Heroes of Might and Magic III** · Engine reimplementation  
[Download and supply your own game files](https://vcmi.eu/download/) · [Browse RemakeList](https://remakelist.com/remakes/vcmi/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vcmi-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux / Android / iOS

**Status:** Public release · original data required

**What you need:** For the full game, provide owned Heroes III Complete or Shadow of Death data. The launcher can import a GOG offline installer or an existing installation. HD Edition alone is insufficient; it is an optional extension with Complete/SoD still required. The official mod directory separately documents limited demo support.

**What is available:** Release 1.7.5 is public. Windows, macOS, Linux and Android packages are listed; iOS uses TestFlight or sideloading. Full compatibility is not guaranteed. Not run by RemakeList.

**Code license:** [GPL-2.0-or-later code; VCMI-created assets CC-BY-SA 4.0; original game assets separate](https://github.com/vcmi/vcmi/blob/66fa496c6328a276c4eb14c0011b3a9d751dfac3/license.txt)  
**Author:** VCMI Team  
[Official documentation](https://github.com/vcmi/vcmi/blob/66fa496c6328a276c4eb14c0011b3a9d751dfac3/docs/Readme.md) · Sources reviewed: 2026-10-18

</details>

### [Julius](https://github.com/bvschaik/julius)

A faithful Caesar III reimplementation that brings the original city builder to modern desktops, Android and other platforms.

Original or reference: **Caesar III** · Game reimplementation  
[Download and supply your own game files](https://github.com/bvschaik/julius/releases/tag/v1.8.0) · [Browse RemakeList](https://remakelist.com/remakes/julius/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=julius-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows · Linux · macOS · Android · Web (Emscripten) · PS Vita · Nintendo Switch

**Status:** Released · original game data required

**What you need:** Provide a full Caesar III installation from your own CD-ROM, GOG or Steam copy, patched to 1.0.1.0. Julius uses that data directory and needs permission to write saves there. Its code license does not supply or license the original game assets.

**What is available:** Version 1.8.0 provides Windows, Linux, macOS and Android downloads, plus Vita, Switch and Emscripten packages. The browser package still needs setup and your game files. Not run by RemakeList.

**Code license:** [AGPL-3.0 · engine code; original Caesar III assets are separate](https://github.com/bvschaik/julius/blob/34d1ecd54befb845c0139b371fa8a0438210dac1/LICENSE.txt)  
**Author:** Bianca van Schaik and contributors  
[Official documentation](https://github.com/bvschaik/julius/blob/34d1ecd54befb845c0139b371fa8a0438210dac1/README.md) · Sources reviewed: 2026-10-18

</details>

### [CorsixTH](https://github.com/CorsixTH/CorsixTH)

A Theme Hospital engine recreation with modern desktop support, high resolutions and an editable hospital-building campaign.

Original or reference: **Theme Hospital** · Game reimplementation  
[Download and supply your own game files](https://github.com/CorsixTH/CorsixTH/releases/tag/v0.70.1) · [Browse RemakeList](https://remakelist.com/remakes/corsixth/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=corsixth-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows · macOS · Linux · BSD

**Status:** Released · original or demo data required

**What you need:** Provide legally owned Theme Hospital data from a CD or digital installation and select its data directory on first launch. The official demo is an alternative with one level and most management screens absent. The engine license does not license the original assets.

**What is available:** Version 0.70.1 is available for Windows and macOS, with Linux AppImage and distribution packages. BSD is also supported. The Mac release disables RtMidi hardware MIDI. Not run by RemakeList.

**Code license:** [MIT · engine code; Theme Hospital assets are separate](https://github.com/CorsixTH/CorsixTH/blob/master/LICENSE.txt)  
**Author:** CorsixTH team and contributors  
[Official documentation](https://github.com/CorsixTH/CorsixTH/blob/master/README.md) · Sources reviewed: 2026-10-19

</details>

### [Warzone 2100](https://github.com/Warzone2100/warzone2100)

The community-maintained continuation of the 1999 3D strategy game, with a full campaign, customizable units and desktop multiplayer.

Original or reference: **Warzone 2100 (1999)** · Open-source continuation  
[Download](https://wz2100.net/) · [Browse RemakeList](https://remakelist.com/remakes/warzone2100/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=warzone2100-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows · macOS · Linux · Web

**Status:** Released · desktop and browser editions

**What you need:** No separately purchased original game or disc image is required. Use the official packages; campaign video files may need a separate official download on some platforms. Code, game data and individual components retain their stated licenses.

**What is available:** Version 4.7.0 offers Windows, macOS and Linux downloads; the Mac bundle supports Intel and Apple silicon. An official browser edition offers campaign and skirmish, with reduced graphics and no online multiplayer. Not run by RemakeList.

**Code license:** [GPL-2.0-or-later and component licenses](https://github.com/Warzone2100/warzone2100/blob/master/COPYING)  
**Author:** Warzone 2100 Project  
[Official documentation](https://github.com/Warzone2100/warzone2100/blob/master/README.md) · Sources reviewed: 2026-10-19

</details>

### [ScummVM](https://github.com/scummvm/scummvm)

Run classic adventures such as Monkey Island, Myst and Blade Runner on modern devices using replacement game engines.

Original or reference: **Classic adventure games and RPGs** · Engine reimplementation  
[Download and supply your own game files](https://www.scummvm.org/downloads/) · [Browse RemakeList](https://remakelist.com/remakes/scummvm/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=scummvm-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux / Android / iOS

**Status:** Released · compatibility varies by game and port

**What you need:** ScummVM itself includes no games. Most commercial titles require your own supported game data. The official Freeware Games page separately offers complete free releases, including Beneath a Steel Sky; these are different from the limited demos on the Demos page. Extract the selected game into a folder and add that folder in the launcher. Each game keeps its own distribution terms.

**What is available:** Stable 2026.4.0 has Windows, macOS and Linux downloads. On 19 October 2026, the official page still lists Android and iOS builds as 2026.3.0 under older versions. No game was run by RemakeList.

**Code license:** [GPL-3.0-or-later engine code; individual game data retains its own terms](https://github.com/scummvm/scummvm/blob/7d2709da5136866589f7602f5f5a7b17de03420e/COPYING)  
**Author:** ScummVM Team  
[Official documentation](https://github.com/scummvm/scummvm/blob/7d2709da5136866589f7602f5f5a7b17de03420e/README.md) · Sources reviewed: 2026-10-19

</details>

### [RigelEngine](https://github.com/lethal-guitar/RigelEngine)

A native Duke Nukem II engine with widescreen, smoother movement, quick saves and improved controller support.

Original or reference: **Duke Nukem II** · Engine reimplementation  
[Download and supply your own game files](https://github.com/lethal-guitar/RigelEngine/releases/tag/v0.9.1) · [Browse RemakeList](https://remakelist.com/remakes/rigelengine/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rigelengine-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux

**Status:** Released · maintenance mode

**What you need:** Provide NUKEM2.CMP from a Duke Nukem II installation. Registered data is needed for the full four-episode game; shareware covers limited content. NUKEM2.F1 through NUKEM2.F5 add optional intro movies. On first launch, select the game-data folder. The official README links a shareware archive and a licensed full-game seller; no original data is included by RemakeList.

**What is available:** Official 0.9.1 packages include Windows x64 ZIP, macOS x64 DMG and Linux x64 DEBs. The release points Apple silicon users to a separate third-party universal Mac build. The README marks its web build as currently unavailable. Not run by RemakeList.

**Code license:** [GPL-2.0-or-later engine code; original Duke Nukem II data is separate](https://github.com/lethal-guitar/RigelEngine/blob/30afeff8f0b105eac77ee0a2fbd54b06e1a49b60/LICENSE.md)  
**Author:** Nikolai Wuttke and contributors  
[Official documentation](https://github.com/lethal-guitar/RigelEngine/blob/30afeff8f0b105eac77ee0a2fbd54b06e1a49b60/README.md) · Sources reviewed: 2026-10-19

</details>

### [OpenLoco](https://github.com/OpenLoco/OpenLoco)

A modern C++ reimplementation of Chris Sawyer’s Locomotion, bringing its transport-company simulation to current desktops.

Original or reference: **Chris Sawyer’s Locomotion** · Game reimplementation  
[Download and supply your own game files](https://openloco.io/download/) · [Browse RemakeList](https://remakelist.com/remakes/openloco/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openloco-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x86/x64 · Linux x64 · macOS Apple silicon

**Status:** Released · original game data required

**What you need:** Provide data from your legally owned Locomotion copy, such as a Steam or GOG installation. Keep original files separate from the application. OpenGraphics additions do not remove the documented original-data requirement; MIT does not license the commercial game assets.

**What is available:** v26.09 offers Windows 32/64-bit ZIPs, a Linux x86-64 AppImage and a native macOS arm64 app. The Mac download requires Apple silicon and is unsigned and unnotarized. RemakeList has not run these builds.

**Code license:** [MIT · engine code; original game assets are separate](https://github.com/OpenLoco/OpenLoco/blob/v26.09/LICENSE)  
**Author:** OpenLoco developers  
[Official documentation](https://github.com/OpenLoco/OpenLoco/blob/v26.09/README.md) · Sources reviewed: 2026-10-19

</details>

### [The Force Engine](https://github.com/TheForceEngine/TheForceEngine)

Play Dark Forces with widescreen, modern mouse controls, quick saves and support for its original community mods.

Original or reference: **Star Wars: Dark Forces** · Engine reimplementation  
[Download and supply your own game files](https://github.com/TheForceEngine/TheForceEngine/releases/tag/v1.22.420) · [Browse RemakeList](https://remakelist.com/remakes/the-force-engine/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=the-force-engine-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Linux · macOS source build

**Status:** Released · Dark Forces supported

**What you need:** Provide your purchased Dark Forces installation. The engine attempts to detect Steam and GOG installations; otherwise select the game-data directory in Settings &gt; Game. The engine license does not include the commercial game files.

**What is available:** Official 1.22.420 Windows ZIP is available. The current README recommends Flathub for Linux and documents source builds for macOS. A ready-to-install official Mac package was not established.

**Code license:** [GPL-2.0 engine code; original Dark Forces assets are separate](https://github.com/TheForceEngine/TheForceEngine/blob/master/LICENSE)  
**Author:** Lucius and The Force Engine contributors  
[Official documentation](https://github.com/TheForceEngine/TheForceEngine#readme) · Sources reviewed: 2026-10-19

</details>

### [OpenJazz](https://github.com/AlisterT/openjazz)

Revisit the original Jazz Jackrabbit platformer on modern desktops, using your own game files or original shareware data.

Original or reference: **Jazz Jackrabbit** · Engine reimplementation  
[Download and supply your own game files](https://github.com/AlisterT/openjazz/releases/tag/20260301) · [Browse RemakeList](https://remakelist.com/remakes/openjazz/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openjazz-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux

**Status:** Released · original game or shareware data required

**What you need:** Supply files from an owned first-generation Jazz Jackrabbit installation or original shareware release. Complete-game data is separate from the free engine; shareware provides limited episodes. Keep the extracted game files together and point OpenJazz at their directory.

**What is available:** Release 20260301 provides Windows x86-64 and Linux x86-64 binaries; the Linux build requires glibc 2.35. Mac Source Ports separately distributes a signed Universal 2 Mac app for Apple silicon and Intel.

**Code license:** [GPL-2.0-or-later engine code; Jazz Jackrabbit data is separate](https://github.com/AlisterT/openjazz/blob/master/doc/licenses.txt)  
**Author:** AJ Thomson, Carsten Teibes and contributors  
[Official documentation](https://github.com/AlisterT/openjazz#readme) · Sources reviewed: 2026-10-19

</details>

### [cnc-port](https://github.com/dk8827/cnc-port)

A source port of Command &amp; Conquer: Tiberian Dawn for modern Macs, with Android and iOS development targets. Game data is separate, and mobile build evidence should not be read as broad device compatibility.

Original or reference: **Command &amp; Conquer: Tiberian Dawn** · Open-source continuation  
[Build and supply your own game files](https://github.com/dk8827/cnc-port#readme) · [Browse RemakeList](https://remakelist.com/remakes/cnc-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cnc-port-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** macOS · Android debug · iOS Simulator

**Status:** Source port · mobile development targets

**What you need:** Prepare C&amp;C Gold Windows 95 GDI and Nod data yourself. The author links community mirrors of the historical freeware release; no data is bundled. The code license grants no rights to the original game, artwork or commercial data.

**What is available:** Source build required. The author exercised Mac menus and tactical gameplay; Android debug APK and iOS Simulator build paths are documented. Mobile build or Simulator launch is not broad physical-device gameplay validation. Community mirrors are not EA-hosted downloads.

**Code license:** [GPLv3 with additional EA terms. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/dk8827/cnc-port#license-and-notice)  
**Author:** dk8827  
[Official documentation](https://github.com/dk8827/cnc-port#readme) · Sources reviewed: 2026-10-19

</details>

### [Generals Zero Hour for Mac, iPhone &amp; iPad](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad)

An Apple Silicon Mac, iPhone and iPad port of Generals: Zero Hour built on EA’s source release and GeneralsX, with RTS touch controls. Bring your own game files and follow the Mac build and signing workflow.

Original or reference: **Command &amp; Conquer: Generals — Zero Hour** · Open-source continuation  
[Build and supply your own game files](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad#readme) · [Browse RemakeList](https://remakelist.com/remakes/generals-apple/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=generals-apple-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Apple Silicon Mac / iPhone / iPad

**Status:** Playable source port · self-build

**What you need:** Own retail or Steam Generals Zero Hour files, a compatible Apple Silicon Mac and the documented build tools are required. The code license grants no rights to the original game, artwork or commercial data.

**What is available:** Follow the Mac source-build guide; iPhone/iPad additionally require Xcode and Apple signing. The author reports campaign and skirmish play. This is a source-build workflow, not an official EA mobile release. Game data and signing are separate prerequisites.

**Code license:** [GPLv3 with upstream terms. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad#readme)  
**Author:** ammaarreshi  
[Official documentation](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad#readme) · Sources reviewed: 2026-10-19

</details>

### [geow2](https://github.com/techknight/geow2)

A desktop native port of Geometry Wars: Retro Evolved 2 using your own XBLA game data, with six documented modes and local multiplayer.

Original or reference: **Geometry Wars: Retro Evolved 2** · Game reimplementation  
[Download and supply your own game files](https://github.com/techknight/geow2/releases/tag/v1.2.6) · [Browse RemakeList](https://remakelist.com/remakes/geow2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=geow2-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS 11+ / Linux x64

**Status:** v1.2.6 · desktop and Flatpak

**What you need:** Bring your own lawfully obtained Xbox Live Arcade · 584108FF · v0x102 · FFmpeg. The project is free to access; the original game is separate. No game files, keys or ready-to-play packages are supplied here.

**What is available:** v1.2.6 supplies Windows, macOS and Linux archives plus a Linux/Steam Deck Flatpak, fixing held Escape/Enter behavior. Provide your own XBLA title 584108FF version 0x102. Initial audio extraction needs FFmpeg; Flatpak bundles it, and an already prepared data folder does not need it. Windows/Linux require Vulkan; macOS 11+ supports Apple Silicon and Intel. Multiplayer is local for up to four players; optional online score sync uses a separate friends’ server. RemakeList has not installed or played it.

**Code license:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/techknight/geow2/blob/main/LICENSE)  
**Author:** techknight  
[Official documentation](https://github.com/techknight/geow2#readme) · Sources reviewed: 2026-10-30

</details>

### [NOVA Swift](https://github.com/SirStig/NovaSwift)

A Swift engine reimplementation for your own Escape Velocity Nova data, with Apple apps and a beta for other desktop platforms. The author documents fidelity checks, while bugs remain.

Original or reference: **Escape Velocity Nova** · Engine reimplementation  
[Download and supply your own game files](https://sirstig.github.io/NovaSwift/download.html) · [Browse RemakeList](https://remakelist.com/remakes/nova-swift/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nova-swift-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** macOS / iOS / iPadOS / tvOS / Linux / Windows / Steam Deck

**Status:** Beta; bugs and incomplete testing remain.

**What you need:** Bring your own lawfully obtained EV Nova · original game data. The project is free to access; the original game is separate. No game files, keys or ready-to-play packages are supplied here.

**What is available:** Official route: macOS / iOS / iPadOS / tvOS / Linux / Windows / Steam Deck. Beta; bugs and incomplete testing remain. Choose the official package matching your system.

**Code license:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/SirStig/NovaSwift/blob/main/LICENSE)  
**Author:** SirStig  
[Official documentation](https://github.com/SirStig/NovaSwift#readme) · Sources reviewed: 2026-10-19

</details>

### [PeonPad](https://github.com/chrissotraidis/peonpad)

A developer-preview iPad port of the Stratagus/Wargus Warcraft II engine with touch RTS controls. Sign the app yourself and copy data extracted from your own game.

Original or reference: **Warcraft II** · Engine reimplementation  
[Download and supply your own game files](https://github.com/chrissotraidis/peonpad/releases) · [Browse RemakeList](https://remakelist.com/remakes/peonpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=peonpad-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** iPadOS 16+

**Status:** Developer preview · unsigned IPA · user signing required

**What you need:** Your own Warcraft II game files, plus a Mac or PC with Wargus tooling to produce the complete data.Wargus folder. Copy that folder after installing the signed app. The free IPA contains no game data and does not grant rights to Blizzard content.

**What is available:** Developer preview for iPadOS 16+. The GitHub prerelease provides an unsigned IPA with no Warcraft II data. Sign and install it yourself; compiling the app is optional. On a Mac or PC, use Wargus to extract your own game data, then copy the complete data.Wargus folder to On My iPad/PeonPad/data.Wargus. There is no in-app content importer, App Store release or TestFlight.

**Code license:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/chrissotraidis/peonpad/blob/main/LICENSE)  
**Author:** chrissotraidis  
[Official documentation](https://github.com/chrissotraidis/peonpad#readme) · Sources reviewed: 2026-10-19

</details>

### [Pocket Wormhole](https://github.com/adamkulik/pocket-wormhole)

An Android port of the Project Wormhole FTL engine that reads your own Steam/GOG ftl.dat and adds touch controls. Some UI and cross-engine save transfers have limits.

Original or reference: **FTL: Faster Than Light** · Engine reimplementation  
[Download and supply your own game files](https://github.com/adamkulik/pocket-wormhole/releases) · [Browse RemakeList](https://remakelist.com/remakes/pocket-wormhole/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pocket-wormhole-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Android 8+ · GLES 3.0

**Status:** Playable or experimental preview.

**What you need:** Bring your own lawfully obtained Steam / GOG · ftl.dat · ~280 MB. The project is free to access; the original game is separate. No game files, keys or ready-to-play packages are supplied here.

**What is available:** Official route: Android 8+ · GLES 3.0. Playable or experimental preview. Cross-engine save transfer has specific limits; read the guide. Choose the official package matching your system.

**Code license:** [GPL-2.0-or-later applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/adamkulik/pocket-wormhole/blob/main/LICENSE)  
**Author:** adamkulik  
[Official documentation](https://github.com/adamkulik/pocket-wormhole#readme) · Sources reviewed: 2026-10-19

</details>

### [ra-port](https://github.com/dk8827/ra-port)

An unofficial source port of the first Red Alert for Mac, Linux and mobile targets, built from EA-released code. Bring your game data and build it yourself; network multiplayer is not connected.

Original or reference: **Command &amp; Conquer: Red Alert** · Open-source continuation  
[Build and supply your own game files](https://github.com/dk8827/ra-port#readme) · [Browse RemakeList](https://remakelist.com/remakes/ra-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ra-port-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** macOS / Linux / Android / iOS / iPadOS

**Status:** Source build · original game required

**What you need:** Legally obtained Red Alert 1 Allied and Soviet disc assets. No game data or packaged executables in source repository.

**What is available:** Source builds. Author reports campaigns and skirmish work; no online multiplayer, expansions not focus, no packaged .app or mobile release. Not built, installed or played by RemakeList.

**Code license:** [GPL-3.0 with EA additional terms](https://github.com/dk8827/ra-port#readme)  
**Author:** dk8827  
[Official documentation](https://github.com/dk8827/ra-port#readme) · Sources reviewed: 2026-10-19

</details>

### [Rugrats: Search for Reptar — Rust Port](https://github.com/toyz/rugrats)

A Rust reconstruction of the PS1 Rugrats: Search for Reptar for desktop play using your own disc. The author documents every level; installation currently follows a source-build route.

Original or reference: **Rugrats: Search for Reptar** · Game reimplementation  
[Build and supply your own game files](https://github.com/toyz/rugrats#readme) · [Browse RemakeList](https://remakelist.com/remakes/rugrats-rust-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rugrats-rust-port-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows

**Status:** Source build · original game required

**What you need:** Owned PlayStation USA SLUS-00650 disc; no emulator BIOS required; extract locally per README.

**What is available:** Author reports start-to-finish playable and publishes port screenshots. Source build with Rust; do not claim one-click installer. Not built, installed or played by RemakeList.

**Code license:** [MIT OR Apache-2.0 authored code; original game data excluded](https://github.com/toyz/rugrats#readme)  
**Author:** toyz  
[Official documentation](https://github.com/toyz/rugrats#readme) · Sources reviewed: 2026-10-19

</details>

### [Rich4 Renew](https://github.com/iam567/rich4-renew-app)

An unofficial Richman 4 recreation for computers and phones, with high-resolution redraws, property trading, stocks, cards and online party play.

Original or reference: **Richman 4** · Game reimplementation  
[Download](https://github.com/iam567/rich4-renew-app/releases/tag/v0.8.1) · [Browse RemakeList](https://remakelist.com/remakes/rich4-renew/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rich4-renew-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Android / iOS

**Status:** v0.8.1 · party-rule controls · asset restrictions apply

**What you need:** Running from source requires the author's separately supplied rich4-assets.tar. It contains material derived from the original game, high-resolution redraws, maps and sounds. These assets are excluded from GPL and restricted by the author to private use. Packaging scripts bundle assets into the apps, but release package contents were not independently inspected. Do not treat a free download as permission to redistribute the artwork or original game material.

**What is available:** v0.8.1 supplies Windows ZIP, universal Mac DMG, Android APK and unsigned iOS IPA downloads. Party hosts can set shared starting funds, movement, land permissions, time limits and victory rules; the mobile landscape lobby can scroll so its start button stays reachable. iOS needs self-signing; Windows is unsigned and Mac unnotarized. Original-derived assets and redraws are outside GPL, and the author’s private-use statement does not establish the rights holder’s authorization. Release contents and signatures were not independently inspected. RemakeList has not built, installed or played this release.

**Code license:** [GPL-3.0-or-later · code only](https://github.com/iam567/rich4-renew-app/blob/main/LICENSE)  
**Author:** iam567 (Liang)  
[Official documentation](https://github.com/iam567/rich4-renew-app/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

### [Model 3-Vulkan](https://github.com/Igloo-Garage/Model-3-Vulkan)

A modernized Supermodel fork for Sega Model 3 arcade games, adding Vulkan rendering, CRT filters, widescreen and a Chinese/English settings interface.

Original or reference: **Sega Model 3 arcade / Supermodel** · emulator-enhancement-fork  
[Download and supply your own game files](https://github.com/Igloo-Garage/Model-3-Vulkan/releases/tag/v0.9.8.3b) · [Browse RemakeList](https://remakelist.com/remakes/supermodel-vk/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=supermodel-vk-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 / Linux x86-64 / macOS 11+ (Intel &amp; Apple Silicon)

**Status:** v0.9.8.3b · Model 3-Vulkan · own ROMs

**What you need:** No game ROMs are supplied. Prepare legally obtained Sega Model 3 ROM sets as ZIP files and point the launcher to their folder. The emulator's GPL license does not license game data, artwork or Sega trademarks. Vulkan needs a 1.3 driver, or 1.2 with dynamic rendering and synchronization2; OpenGL 4.1 is the fallback.

**What is available:** Model 3-Vulkan is the renamed Supermodel-VK project. v0.9.8.3b provides Windows, Linux and macOS archives, restores sound effects lost in v0.9.8.3a and adds native DDS texture-pack support. It remains an emulator requiring your own ROM sets. Game compatibility and performance vary. The existing cover is a historical preview frame, not a newly verified screenshot of v0.9.8.3b. RemakeList has not installed or run this release. The macOS package is not notarized and may be blocked by Gatekeeper; follow the author’s installation instructions.

**Code license:** [GPL-3.0-or-later · emulator code](https://github.com/Igloo-Garage/Model-3-Vulkan/blob/master/Docs/LICENSE.txt)  
**Author:** Igloo-Garage · upstream: The Supermodel Team  
[Official documentation](https://github.com/Igloo-Garage/Model-3-Vulkan/blob/master/README.md) · Sources reviewed: 2026-10-29

</details>

### [pokerecomp](https://github.com/Decryptu/pokerecomp)

A Godot reimplementation of the first two Pokémon generations with modern display and control options. Reads game content from your own supported GB/GBC ROMs.

Original or reference: **Pokémon Red/Blue/Yellow and Gold/Silver/Crystal** · Game reimplementation  
[Download and supply your own game files](https://github.com/Decryptu/pokerecomp/releases/tag/v0.1.86) · [Browse RemakeList](https://remakelist.com/remakes/pokerecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pokerecomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64/ARM64; Linux x64/ARM64; macOS; Android; iOS; Switch homebrew

**Status:** v0.1.86 · generations 1–2 · own ROM required

**What you need:** Use your own supported, hash-matching Red, Blue, Yellow, Gold, Silver or Crystal ROM revision. The engine package does not include the original games.

**What is available:** v0.1.86 publishes desktop builds, Android APK, unsigned iOS IPA and Switch homebrew package. iOS requires personal signing/sideloading; Switch requires an existing homebrew environment. Generation 3 is experimental and not playable. Unsupported ROM revisions are rejected. Apple packages are not a normal App Store release; macOS builds are ad-hoc signed, and free Apple-account iOS signing commonly needs renewal.

**Code license:** [The rewritten engine code is MIT. Original Pokémon code, ROM content, artwork and music remain outside that license.](https://github.com/Decryptu/pokerecomp/blob/main/LICENSE)  
**Author:** Decryptu  
[Official documentation](https://github.com/Decryptu/pokerecomp/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [Streetball Revival](https://github.com/luckvj/streetball-revival)

A Rust recreation of NBA Street Vol. 2 with desktop controls and experimental online play. Loads content from your own supported USA PS2 disc.

Original or reference: **NBA Street Vol. 2 (PS2)** · Game reimplementation  
[Download and supply your own game files](https://github.com/luckvj/streetball-revival/releases/tag/v0.1.4-beta) · [Browse RemakeList](https://remakelist.com/remakes/streetball-revival/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=streetball-revival-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows; Linux

**Status:** v0.1.4-beta · Windows/Linux · online play experimental

**What you need:** Supply your own USA PS2 NBA Street Vol. 2 ISO, SLUS-20651, matching the project’s required hash. The engine download contains no original game data.

**What is available:** v0.1.4-beta offers Windows installer/archive and a Linux archive. Online play remains a work in progress needing further player testing. Gameplay parity remains incomplete: computer-team behavior, rendering and Gamebreaker camera details can differ. The author’s parity table measures selected behaviors, not a complete-game fidelity percentage.

**Code license:** [The rewritten engine is MIT. The license does not include EA’s original game data, artwork or music.](https://github.com/luckvj/streetball-revival/blob/main/LICENSE)  
**Author:** luckvj  
[Official documentation](https://github.com/luckvj/streetball-revival/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [Torchlight Rekindled](https://github.com/GreenSwampDweller/torchlight-rekindled)

A Torchlight engine for handhelds and desktops, following the Xbox 360 version’s controller-oriented game logic. Uses data from your own PC or Xbox 360 copy.

Original or reference: **Torchlight** · Engine reimplementation  
[Download and supply your own game files](https://github.com/GreenSwampDweller/torchlight-rekindled/releases/tag/1.1.0) · [Browse RemakeList](https://remakelist.com/remakes/torchlight-rekindled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=torchlight-rekindled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Switch homebrew / Android 12+ arm64 / iOS / Windows / Linux

**Status:** 1.1.0 · mod support; no new IPA attached

**What you need:** Supply pak.zip/Pak.zip and the music folder from your own purchased full PC or Xbox 360 release. PC data uses the project’s fallback console interface. No game data is distributed by the project.

**What is available:** 1.1.0 provides Switch NRO, Android APK and Windows/Linux archives, adding PC-mod folder support and gameplay fixes. This release has no IPA attachment; iOS builds still need personal signing. Supply your own full PC/Xbox 360 pak.zip and music; PC data uses the console-UI fallback. Android requires version 12+, ARM64 and All files access to the chosen game folder. Desktop testing is limited to the author’s laptop with a gamepad; Steam Deck is unverified.

**Code license:** [GPL-3.0 for the engine; game data and third-party components retain separate rights](https://github.com/GreenSwampDweller/torchlight-rekindled/blob/main/LICENSE)  
**Author:** GreenSwampDweller  
[Official documentation](https://github.com/GreenSwampDweller/torchlight-rekindled/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

### [ZQuest Classic](https://github.com/ZQuestClassic/ZQuestClassic)

A free engine, quest player and editor for adventures in the style of the original NES Zelda. Play community quests or build your own.

Original or reference: **The Legend of Zelda / Zelda-style adventures** · Engine reimplementation  
[Download](https://zquestclassic.com/releases/) · [Browse RemakeList](https://remakelist.com/remakes/zquest-classic/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=zquest-classic-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux / Web (experimental)

**Status:** Stable desktop release · experimental web player

**What you need:** The engine/player uses quest files; choose quests from their authors or create your own. The engine’s GPL license does not grant rights to Nintendo names, artwork or third-party quest assets; verify each quest’s separate terms.

**What is available:** Stable 2.55.17 provides Windows x64/x86, macOS and Linux downloads; the official site also offers an experimental web player. 2.55.17 is the selected stable release; 3.0 prereleases are a separate track. The web version is experimental, including on mobile. Quest compatibility and asset terms vary by author and engine version. RemakeList verified documentation and release metadata only, without installing or playing a quest.

**Code license:** [GPL-3.0 for the engine; individual quests and their media have separate rights](https://github.com/ZQuestClassic/ZQuestClassic/blob/main/LICENSE)  
**Author:** ZQuestClassic  
[Official documentation](https://github.com/ZQuestClassic/ZQuestClassic/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>


<a id="ports"></a>

## Ports and compatibility projects

### [D2R Mobile](https://github.com/jhaizhou-ops/d2r-mobile)

A compatibility layer for your own Switch Diablo II: Resurrected and Reign of the Warlock files on Apple devices, Android and HarmonyOS, with platform-specific preparation.

Original or reference: **Diablo II: Resurrected** · Platform compatibility layer  
[Build and supply your own game files](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) · [Browse RemakeList](https://remakelist.com/remakes/d2r-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=d2r-mobile-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** iPhone / iPad / Apple silicon Mac / Android ARM64 / HarmonyOS NEXT

**Status:** v2.1.0 · owned Switch files · experimental camera option

**What you need:** Supply lawfully purchased Switch base-game and Reign of the Warlock ExeFS/RomFS files updated to console version 1.0.34.0, called 3.3.94012 by the tools. PC and other console files are not substitutes. Resources take about 5.6 GB; older Apple chips need an additional roughly 1 GB texture pack generated from your files. Apple requires at least A14/M1; choose standard or older-API builds for iOS 26+ versus 18–25 and macOS 26+ versus 15–25. Android needs ARM64, Android 12+ and Vulkan 1.1. HarmonyOS NEXT needs a developer account, signing tools and a self-prepared runtime pack.

**What is available:** v2.1.0 updates the Android APK and both iOS build-input ZIPs. Android keeps the existing import pack and saves; iOS needs a new app built with the new inputs and v2.1.0 source, then signed. The unsigned HarmonyOS HAP remains the v2.0.0 file and needs your developer signature and runtime pack. Mac is source-build only. Offline only. Android retains unfinished touch details and device-specific graphics faults. Apple devices with 4 GB RAM are memory-constrained; sideload-tool signing and Linux packaging remain unverified. A free Apple ID needs re-signing every 7 days and has no iCloud sync. Apple TV is only a character-selection preview. Do not redistribute packages containing game content. RemakeList has not built, installed or played it.

**Code license:** [MIT covers project code; original game files and third-party components retain separate rights and licenses.](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/LICENSE)  
**Author:** joe jiang (@happyjoejiang)  
[Official documentation](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [MW2 Recompiled](https://github.com/PaulCombal/mw2-recompiled)

A native Windows and Linux recompilation of the Xbox 360 version of Modern Warfare 2 (2009).

Original or reference: **Modern Warfare 2 (2009)** · Static recompilation  
[Download and supply your own game files](https://github.com/PaulCombal/mw2-recompiled/releases/tag/v0.8.1) · [Browse RemakeList](https://remakelist.com/remakes/mw2-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mw2-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Linux x64 · SSE4.2 · Vulkan 1.2

**Status:** Stable v0.8.1 · v0.8.2 prerelease available

**What you need:** Supply your own lawfully obtained Xbox 360 USA/Europe version 1.0.557 disc ISO; the launcher checks it, then downloads and applies Title Update 6. Requires an x64 SSE4.2 processor, Vulkan 1.2, about 8 GB disk space and a controller; keyboard controls cover menus only. Experimental PC custom-map imports also need assets from your own PC copy.

**What is available:** The main download remains stable v0.8.1 for Windows and Linux. v0.8.2 is a separate prerelease. Launch mw2-launcher with your own supported ISO; use the regular platform package, as same-version -steam/-lan files are duplicate compatibility downloads. Public matchmaking/ranked play are unsupported; custom maps remain beta. Steam SYSTEM LINK is discoverable by other Steam users, and shared relay/LAN users can also reach games. Use the same version and trusted friends. The author reports network fixes; RemakeList has neither audited security nor installed or played it.

**Code license:** [GPL-3.0-only](https://github.com/PaulCombal/mw2-recompiled/blob/master/LICENSE)  
**Author:** PaulCombal  
[Official documentation](https://github.com/PaulCombal/mw2-recompiled/blob/master/README.md) · Sources reviewed: 2026-10-28

</details>

### [Zelda 64: Recompiled](https://github.com/Zelda64Recomp/Zelda64Recomp)

A static recompilation of Majora’s Mask into a native desktop port with modern controls and graphics options.

Original or reference: **Majora’s Mask** · Static recompilation  
[Download and supply your own game files](https://github.com/Zelda64Recomp/Zelda64Recomp/releases) · [Browse RemakeList](https://remakelist.com/remakes/zelda64-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=zelda64-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Linux / macOS

**Status:** Release · original assets required

**What you need:** Provide your own North American Nintendo 64 Majora’s Mask ROM. Neither repository nor releases include game assets.

**What is available:** Prebuilt v1.2.2 releases are available for Windows, Linux and macOS. A compatible graphics API is required. Not run here.

**Code license:** [GPL-3.0](https://github.com/Zelda64Recomp/Zelda64Recomp/blob/dev/COPYING)  
**Author:** Zelda64Recomp team  
[Official documentation](https://github.com/Zelda64Recomp/Zelda64Recomp/blob/dev/README.md) · Sources reviewed: 2026-10-14

</details>

### [MacNativeGames · Tears of the Kingdom](https://github.com/ly05010419/MacNativeGames)

Build a native Tears of the Kingdom app for Apple silicon Mac or iPhone/iPad from your own Switch files. Experimental; local builds and signing are required.

Original or reference: **The Legend of Zelda: Tears of the Kingdom** · Platform compatibility layer  
[Build and supply your own game files](https://github.com/ly05010419/MacNativeGames#build-the-app) · [Browse RemakeList](https://remakelist.com/remakes/zelda-totk-mac-research/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=zelda-totk-mac-research-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Apple silicon Mac · macOS 26+; iPhone 14+ / iPad · iOS/iPadOS 26+

**Status:** Experimental · local build and signing · no formal release

**What you need:** Requires your own Switch base game v1.0.0 as XCI/NSP and your own keys/system files from your console. Mac can also use separate cumulative updates v1.1.2, v1.2.1 or v1.4.3 as NSP/NSZ; only v1.4.3 has been tested on iOS. Apple silicon Mac needs macOS 26+ with Metal 4; 16 GB RAM is recommended. A base Mac build needs about 25 GB beyond the input game, plus roughly 17 GB if APFS cloning cannot be used. A fresh updated Mac build needs about 40 GB. iOS builds need full Xcode 26+, iOS/iPadOS 26+, an iPhone 14 or newer for phones, and signing that retains the increased-memory entitlement; allow 45 GB for a fresh base build or 60 GB with an update. The generated app contains original game content: keep it for your own use. This listing supplies no games, keys, firmware, signed apps or derived shaders.

**What is available:** Experimental source build with no formal Releases. The author reports Mac tests on M4 hardware and v1.4.3 gameplay on iPhone 14 and an A16 iPad; these are not RemakeList tests. Earlier Mac observations of roughly 90 FPS after warm-up are not a stable-performance or full-playthrough guarantee. iPhone 14 uses close to 4 GB and was closed by iOS twice at about eight minutes in busy areas. Missing iOS shader variants can leave objects invisible; new Mac scenes can stutter. Online features and amiibo are unsupported.

**Code license:** [Project code MIT · game rights and third-party licenses separate](https://github.com/ly05010419/MacNativeGames/blob/main/LICENSE)  
**Author:** Yong Li / liyong (@liyong2077)  
[Official documentation](https://github.com/ly05010419/MacNativeGames/blob/b75be8cfa704df3701e86130c8ced268e79d6b11/README.md) · Sources reviewed: 2026-10-20

</details>

### [Dusklight](https://github.com/TwilitRealm/dusklight)

A native Twilight Princess port with higher resolutions, frame-rate options and a built-in mod browser.

Original or reference: **The Legend of Zelda: Twilight Princess** · Decompilation-based project  
[Download and supply your own game files](https://twilitrealm.dev/install/) · [Browse RemakeList](https://remakelist.com/remakes/dusklight/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=dusklight-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Linux / macOS / iOS / Android

**Status:** Release · original assets required

**What you need:** Dump your own retail GameCube or Wii copy of Twilight Princess. The Korean Wii release is unsupported. The project does not provide copyrighted game assets.

**What is available:** Official desktop and mobile builds are available; iOS requires sideloading. D3D12, Vulkan 1.1+ or Metal is recommended. Older graphics backends offer limited accuracy and performance. Not run by RemakeList.

**Code license:** [CC0-1.0 · project code; original game assets excluded](https://github.com/TwilitRealm/dusklight/blob/main/LICENSE.md)  
**Author:** Twilit Realm  
[Official documentation](https://github.com/TwilitRealm/dusklight/blob/main/README.md) · Sources reviewed: 2026-10-18

</details>

### [Mega Man X4 Recompiled](https://github.com/mstan/MegaManX4Recomp)

A native Mega Man X4 recompilation with two-player X and Zero co-op, locally or over netplay. The current release is a public beta.

Original or reference: **Mega Man X4** · Static recompilation  
[Download and supply your own game files](https://github.com/mstan/MegaManX4Recomp/releases/tag/v1.0.17) · [Browse RemakeList](https://remakelist.com/remakes/mega-man-x4-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mega-man-x4-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / Linux x86-64 (glibc 2.38+)

**Status:** v1.0.17 · public beta

**What you need:** Supply your own original, unmodified Mega Man X4 USA (SLUS-00561) .cue and .bin disc image, even with all mods disabled. Patched discs, undubs and retranslated images are unsupported. OpenBIOS is included; a separate BIOS dump is optional. Original game content is outside the MIT license.

**What is available:** v1.0.17 is a public beta with Windows x64 and Linux x64 packages. It fixes paired pause menus and several two-player camera/scenery cases. Native memory-card saves carry forward and all netplay players must update; diagnostic recording remains optional and off by default. Independent cameras can still slow down, and online sign-in/startup reports remain under investigation. Linux needs glibc 2.38+. Four-player experiments are separate; no complete campaign, credits sequence or LAN playthrough is established. Supply the unchanged supported US disc. RemakeList has not built, installed or played it.

**Code license:** [MIT · original project code; dependencies retain their licenses](https://github.com/mstan/MegaManX4Recomp/blob/master/LICENSE)  
**Author:** Matthew Stanley  
[Official documentation](https://github.com/mstan/MegaManX4Recomp/blob/master/README.md) · Sources reviewed: 2026-10-30

</details>

### [Tekken 3 Recompiled](https://github.com/FishB0nes98/Tekken3Recompiled)

A Windows hybrid recompilation preview of Tekken 3 with widescreen, custom outfits and an optional Jun Kazama import.

Original or reference: **Tekken 3** · Static recompilation  
[Download and supply your own game files](https://github.com/FishB0nes98/Tekken3Recompiled/releases/tag/v0.1.4) · [Browse RemakeList](https://remakelist.com/remakes/tekken-3-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=tekken-3-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64

**Status:** Hybrid recompilation preview · own disc required

**What you need:** Provide your own legally owned Tekken 3 USA SLUS-00402 CUE/BIN. Optional Jun additionally requires non-merged tektagt (World C1) and tekken3 (World E1) arcade ZIPs; disable Include Jun Kazama if unavailable. The project says retail game data, Sony BIOS and extracted donor assets are excluded; OpenBIOS is used. Original game rights are not granted by its code license.

**What is available:** Public v0.1.4 Windows x64 Easy Setup preview. Initial setup downloads pinned tools and builds locally, requiring internet and at least 4 GB working space. Linux and Steam Deck are unverified. Not run by RemakeList.

**Source available; license restrictions apply:** [Source available under PolyForm Noncommercial 1.0.0; dependencies retain their licenses](https://github.com/FishB0nes98/Tekken3Recompiled/blob/main/LICENSE)  
**Author:** FishB0nes98  
[Official documentation](https://github.com/FishB0nes98/Tekken3Recompiled/blob/main/README.md) · Sources reviewed: 2026-10-18

</details>

### [DevilutionX](https://github.com/diasurgical/DevilutionX)

Diablo and Hellfire on modern computers and phones, with widescreen, controller support and optional quality-of-life improvements.

Original or reference: **Diablo / Hellfire** · Decompilation-based project  
[Download and supply your own game files](https://github.com/diasurgical/DevilutionX/releases/tag/1.5.5) · [Browse RemakeList](https://remakelist.com/remakes/devilutionx/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=devilutionx-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux / Android / iOS

**Status:** Released · own data required for the full game

**What you need:** Full Diablo requires DIABDAT.MPQ from your own original CD or purchased installation. Hellfire also requires hellfire.mpq, hfmonk.mpq, hfmusic.mpq and hfvoice.mpq. The official guide offers spawn.mpq for the limited shareware portion; it does not unlock the full game. Chinese, Japanese and Korean text additionally needs the project’s fonts.mpq.

**What is available:** Official 1.5.5 downloads include Windows ZIPs, a universal macOS DMG, Linux builds, an Android APK and an iOS IPA. iOS requires sideloading. Release packages and installation documentation were checked; RemakeList has not run the game.

**Source available; license restrictions apply:** [Source available under Sustainable Use License 1.0; redistribution must be free of charge and non-commercial; original game assets excluded](https://github.com/diasurgical/DevilutionX/blob/0011dc9670c2093d5ab0084c1cdbeb086556563a/LICENSE.md)  
**Author:** diasurgical / DevilutionX contributors  
[Official documentation](https://github.com/diasurgical/DevilutionX/blob/0011dc9670c2093d5ab0084c1cdbeb086556563a/README.md) · Sources reviewed: 2026-10-18

</details>

### [ACFA-Port](https://github.com/sulphurs16/acfa-port)

Build your own US PS3 Armored Core for Answer files into a Windows game with modern input and display controls. Requires matching game files and a one-time local setup.

Original or reference: **ARMORED CORE for Answer** · Static recompilation  
[Build and supply your own game files](https://github.com/SulphurS16/ACFA-Port/releases/tag/v0.7.4) · [Browse RemakeList](https://remakelist.com/remakes/acfa-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=acfa-port-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64

**Status:** v0.7.4 · Windows local build

**What you need:** Own US PS3 BLUS30187 game files, RPCS3 and Sony PS3 system software 4.93 are required; update 01.35 is optional. The code license grants no rights to the original game, artwork or commercial data.

**What is available:** v0.7.4 supplies a Windows launcher ZIP that compiles the game locally, with VOB mouse-control and menu-input fixes. It requires your own US PS3 BLUS30187 disc files, RPCS3 and Sony firmware 4.93; update 01.35 is optional. Windows 10 1903+/11 x64, AVX2 and Direct3D 11 are required. The project supplies no original game or firmware; RemakeList has not built or played it.

**Code license:** [MIT. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/SulphurS16/ACFA-Port/blob/main/LICENSE)  
**Author:** SulphurS16  
[Official documentation](https://github.com/sulphurs16/acfa-port#readme) · Sources reviewed: 2026-10-30

</details>

### [AgePad](https://github.com/chrissotraidis/agepad)

An iPad developer preview for your own Steam Mac copy of Age of Empires II: Definitive Edition, with touch and Pencil controls. Matching versions are required; Steam compatibility and account safety remain unconfirmed.

Original or reference: **Age of Empires II: Definitive Edition** · Platform compatibility layer  
[Build and supply your own game files](https://github.com/chrissotraidis/agepad#readme) · [Browse RemakeList](https://remakelist.com/remakes/agepad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=agepad-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** iPad · 8 GB+ RAM

**Status:** Developer preview · account-risk boundary

**What you need:** Owned Steam Mac game, matching game/Steam versions, a Mac, an iPad with 8 GB+ RAM and 25 GB free, and sideload signing are required. The code license grants no rights to the original game, artwork or commercial data.

**What is available:** 0.1.0 developer preview: use a Mac to combine the author’s small release app with your own matching game and Steam files, then sign and install it. Steam compatibility and account safety are unconfirmed. Full online matches and devices beyond the author’s M2 iPad are unverified.

**Code license:** [MIT (AgePad code). The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/agepad#credits-and-license)  
**Author:** chrissotraidis  
[Official documentation](https://github.com/chrissotraidis/agepad#readme) · Sources reviewed: 2026-10-19

</details>

### [BearBirdPad](https://github.com/chrissotraidis/bearbirdpad)

An Apple mobile integration of BanjoRecomp with touch controls, saves and local ROM import. Build it on a Mac using your own US 1.0 ROM; the author documents iPhone and iPad playtesting.

Original or reference: **Banjo-Kazooie** · Static recompilation  
[Build and supply your own game files](https://github.com/chrissotraidis/bearbirdpad#readme) · [Browse RemakeList](https://remakelist.com/remakes/bearbirdpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=bearbirdpad-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** iPhone / iPad · iOS 16+

**Status:** Self-build developer preview

**What you need:** Own Banjo-Kazooie NTSC-U 1.0 ROM, an Apple Silicon Mac with Xcode and an Apple signing identity are required. The code license grants no rights to the original game, artwork or commercial data.

**What is available:** Build and sign your own app on an Apple Silicon Mac with Xcode or PadMint. Releases publish recipes, not apps. Author-tested on iPhone 14 and iPad Pro; physical-controller and lifecycle coverage remain incomplete. No App Store or TestFlight listing.

**Code license:** [GPL-3.0-or-later. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/bearbirdpad#legal-and-acknowledgements)  
**Author:** chrissotraidis  
[Official documentation](https://github.com/chrissotraidis/bearbirdpad#readme) · Sources reviewed: 2026-10-19

</details>

### [Birdman64](https://github.com/noahvl/birdman64)

Run your own US Pilotwings 64 ROM natively on Windows or Linux with widescreen, gamepads and configurable controls. Android is experimental; iPhone builds require a separate self-build workflow.

Original or reference: **Pilotwings 64** · Decompilation-based project  
[Download and supply your own game files](https://github.com/noahvl/birdman64/releases) · [Browse RemakeList](https://remakelist.com/remakes/birdman64/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=birdman64-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Linux · Android experimental · iOS self-build

**Status:** Desktop releases · mobile experimental

**What you need:** Own USA Pilotwings 64 ROM and internet access for the initial build are required; no ROM is downloaded. The code license grants no rights to the original game, artwork or commercial data.

**What is available:** Desktop releases provide a launcher with one-time local setup. Android is experimental; iPhone/iPad require self-building. Mobile routes have different verification levels; an iOS ready-made download is not provided.

**Code license:** [MIT (project code). The code license grants no rights to the original game, artwork or commercial data.](https://github.com/NoahVl/Birdman64#license)  
**Author:** NoahVl  
[Official documentation](https://github.com/noahvl/birdman64#readme) · Sources reviewed: 2026-10-19

</details>

### [Chupathingy](https://github.com/ChupathingyCE/chupathingyce)

A native cross-platform Halo CE port built on the decompilation community’s work, with multiplayer lobbies and dedicated-server support. Requires your own Xbox game maps; optional PC maps use separate folders.

Original or reference: **Halo: Combat Evolved** · Decompilation-based project  
[Download and supply your own game files](https://github.com/ChupathingyCE/chupathingyce/releases/tag/v0.8.1d) · [Browse RemakeList](https://remakelist.com/remakes/chupathingy/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=chupathingy-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux / Android

**Status:** v0.8.1d · Released · original Xbox data required

**What you need:** Own Halo Combat Evolved Xbox disc image/maps are required. Optional Halo PC or Custom Edition maps use separate folders. The code license grants no rights to the original game, artwork or commercial data.

**What is available:** v0.8.1d provides Windows, macOS, Linux and Android packages and joins OpenCE’s newest network version 41. A Linux x64 AppImage is now an actual release attachment; 32-bit and Android ARM64 packages are separate selections. Original Xbox maps are still required for the core game. The Android ARM64 build is a separate experimental option; existing map-memory and network-compatibility limits still apply. RemakeList has not built, installed or played this release.

**Code license:** [GPL-3.0-or-later from 0.8.0; earlier releases through 0.7.5d CC0. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/ChupathingyCE/chupathingyce#license)  
**Author:** Milenko (MrMilenko) and ChupathingyCE contributors; credits retain OpenCE and Halo decomp authors  
[Official documentation](https://github.com/ChupathingyCE/chupathingyce#readme) · Sources reviewed: 2026-10-30

</details>

### [CTRPad](https://github.com/chrissotraidis/ctrpad)

An Apple-platform integration of CTR Native and CTR-ModSDK for the original Crash Team Racing, with touch controls and local disc import. Build a personal app through PadMint on Mac, or use its GitHub Cloud Build for iPhone/iPad.

Original or reference: **Crash Team Racing (1999)** · Decompilation-based project  
[Build and supply your own game files](https://github.com/chrissotraidis/ctrpad#readme) · [Browse RemakeList](https://remakelist.com/remakes/ctrpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ctrpad-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Apple Silicon Mac (macOS 11+) / iPhone / iPad (iOS/iPadOS 15+)

**Status:** v0.2.4 · Personal build · recipe-only release

**What you need:** Import your own compatible NTSC-U SCUS944.26 single-track raw MODE2/2352 BIN, starting at byte zero. Select the BIN, not the CUE; cooked ISO, CHD and archives are unsupported. Local Apple builds need the documented build/signing tools; iPhone/iPad cloud builds use the documented signing route. The code license does not cover original game data or artwork.

**What is available:** v0.2.4 fixes iPad landscape startup and touch-control layout. Releases contain only a PadMint recipe and checksum, not an app. Build on an Apple Silicon Mac, or use PadMint’s GitHub Cloud Build for iPhone/iPad without a Mac; import your own supported BIN after installation. Keep personal builds private; there is no App Store/TestFlight release. The author reports Mac/iPhone/iPad gameplay and a physical iPad fix check, while broader gameplay, controller and local-multiplayer coverage remain incomplete. RemakeList has not installed or played it.

**Code license:** [GPL-3.0. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/ctrpad/blob/main/LICENSE)  
**Author:** chrissotraidis  
[Official documentation](https://github.com/chrissotraidis/ctrpad#readme) · Sources reviewed: 2026-10-28

</details>

### [Def Jam: Fight for NY Recompiled](https://github.com/vyanhursky/DefJamFFNY-recomp)

Build a native Windows, Mac or Linux version of Def Jam: Fight for NY from your own supported USA original-Xbox dump, with higher resolution and up to four local players. Widescreen remains beta.

Original or reference: **Def Jam: Fight for NY** · Static recompilation  
[Build and supply your own game files](https://github.com/vyanhursky/DefJamFFNY-recomp/releases/tag/v0.12.3) · [Browse RemakeList](https://remakelist.com/remakes/defjam-ffny-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=defjam-ffny-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 (Direct3D 11) / Apple silicon macOS / Linux x86-64 / Steam Deck

**Status:** v0.12.3 · local compilation

**What you need:** Supply your own USA original-Xbox disc image or extracted dump matching the author’s supported manifest. PS2 and GameCube versions cannot substitute. Setup verifies, recompiles and builds locally; HD texture generation adds time and disk-space requirements. The code license grants no rights to the original game or artwork.

**What is available:** v0.12.3 supplies Windows setup, an Apple silicon Mac DMG and a Linux x64 archive. It evens out simulation frame pacing and fixes newer GCC/CachyOS builds. The setup analyzes and compiles your own game disc locally; its update workflow preserves saves and mods. Widescreen and mod compatibility remain limited; the release fixes frame pacing but does not establish every scene or configuration. Multiplayer is local. macOS is unsigned; RemakeList has not installed or played it.

**Code license:** [MIT project code; separate toolkit licenses. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/vyanhursky/DefJamFFNY-recomp#credits-and-licensing)  
**Author:** vyanhursky  
[Official documentation](https://github.com/vyanhursky/DefJamFFNY-recomp#readme) · Sources reviewed: 2026-10-29

</details>

### [DOAXVB Native PC Port](https://github.com/norain211/doaxvb-re)

An unofficial native port of Dead or Alive Xtreme Beach Volleyball built locally from your own USA Xbox disc. The recommended v0.6.0 beta has a new launcher, desktop packages and remaining rendering faults.

Original or reference: **Dead or Alive Xtreme Beach Volleyball** · Static recompilation  
[Build and supply your own game files](https://github.com/NoRain211/doaxvb-re/releases/tag/v0.6.0) · [Browse RemakeList](https://remakelist.com/remakes/doaxvb-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=doaxvb-native-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 / macOS Apple silicon·Intel / Linux x86-64·Steam Deck

**Status:** Recommended v0.6.0 beta · local build · incomplete testing

**What you need:** Provide your own supported USA Xbox disc image; setup validates and generates game code locally. Mac/Linux also require the documented build tools; Steam Deck builds use a container with a compiler. Generated game content and original artwork remain outside the project’s GPL-3.0-or-later grant.

**What is available:** v0.6.0 replaces v0.5.3 as the author’s recommended beta and offers Windows, Mac and Linux ZIPs. Each builds from your own disc; extract into a new folder and rebuild because the recipe changed, then copy your previous private saves. Windows setup now downloads llvm-mingw instead of requiring Visual Studio. v0.6.0 itself has not had a full author play session. Windows and Linux ZIP build checks are documented, but the Mac ZIP was not built on a Mac; launcher controller checks used a virtual gamepad. Shore flicker and pool-transition faults remain. Mac/Linux lack some fog, lights and shadows; the ray-traced GI option has no effect in release builds. RemakeList has not built or played it.

**Code license:** [GPL-3.0-or-later. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/norain211/doaxvb-re#license)  
**Author:** NoRain211  
[Official documentation](https://github.com/norain211/doaxvb-re#readme) · Sources reviewed: 2026-10-28

</details>

### [Forza Horizon 1: ReImagined](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined)

Builds a native Windows and Linux port locally from your own Xbox 360 Forza Horizon files, with community online services, car tuning and display options.

Original or reference: **Forza Horizon** · Static recompilation  
[Download and supply your own game files](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined/releases/tag/v0.2.0) · [Browse RemakeList](https://remakelist.com/remakes/forza-horizon-reimagined/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=forza-horizon-reimagined-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 / Linux x86-64; macOS source-build experiment only

**Status:** v0.2.0 released · local build · experimental VR

**What you need:** Supply your own lawfully obtained Xbox 360 Forza Horizon disc image, Games on Demand package or extracted folder. Supply Title Update 4 and DLC separately; Horizon Rally and the 1000 Club need TU4. Allow about 4 GB free RAM and 15 GB disk space. The Vulkan path needs Vulkan 1.3; Windows also offers Direct3D 12. Initial setup needs compiler tools to be downloaded or installed.

**What is available:** v0.2.0 provides a Windows installer, Linux x86-64 archive and Flatpak. The launcher generates and compiles the game locally from your own files; rebuild once after updating. macOS remains a source-build experiment with no Mac download. Steam Deck and low-end performance remains limited, with graphics or crash issues on some GPUs. The author tested VR on Quest 3 with Linux WiVRn; Windows VR is untested. Full races, save reloads and physical controllers still need validation on macOS. TU4 and base-game players use separate online rooms, and TU4 saves cannot simply return to the base game. RemakeList has not built or played it.

**Code license:** [The current project code uses GPL-3.0-or-later, with an additional permission described in NOTICE.md for graphics, VR and platform components. Earlier releases and commits published under MIT remain available under MIT. Original game content and third-party components retain separate rights; the linked Forza Live server and website have their own AGPL-3.0-or-later terms.](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined/blob/main/LICENSE)  
**Author:** Dyotson  
[Official documentation](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined#readme) · Sources reviewed: 2026-10-30

</details>

### [Gears of War 2 PC Port](https://github.com/santiquiroz/gears-of-war-2-pc-port)

An unofficial native port using your own Xbox 360 Gears of War 2 files, with high-resolution rendering, split-screen and System Link co-op. Android remains experimental and full-campaign coverage is unverified.

Original or reference: **Gears of War 2** · Static recompilation  
[Download and supply your own game files](https://github.com/santiquiroz/gears-of-war-2-pc-port/releases/tag/v0.3.11) · [Browse RemakeList](https://remakelist.com/remakes/gears-of-war-2-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gears-of-war-2-native-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 (DirectX 12) / Android 10+ ARM64 (Vulkan, experimental)

**Status:** v0.3.11 · Public release · campaign coverage incomplete · experimental Android

**What you need:** Supply your own lawfully obtained retail Xbox 360 Gears of War 2 (title ID 4D53082D) ISO, or a complete folder with default.xex and GearGame. Initial ISO extraction on Windows needs about 8 GB. Android import copies the data into app storage and needs room for another complete copy. RemakeList supplies no game data.

**What is available:** v0.3.11 supplies Windows x64 and experimental Android ARM64 packages. The PC update checker retains its state and skipped-version choice; Android changes only the package version. Earlier 0.3.10 Android changes and the frame counter remain untested on phones. Only Act 1 has an author-reported full playthrough; chapter sweeps do not verify Acts 2–5. Heat affects Android performance. Three/four-player co-op and internet play retain untested scenarios and require matching releases. AMD smearing has an Emulated EDRAM fallback; Vega menu-text and Proton D3D12 faults remain. Windows files are unsigned; author scan claims are not a security certification. RemakeList has not built, installed or played it.

**Code license:** [BSD-3-Clause applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/santiquiroz/gears-of-war-2-pc-port/blob/master/LICENSE)  
**Author:** santiquiroz  
[Official documentation](https://github.com/santiquiroz/gears-of-war-2-pc-port#readme) · Sources reviewed: 2026-10-30

</details>

### [GoldenEye 007 PC Port](https://github.com/jkdansereau/goldeneye-pc-port)

A GoldenEye 007 PC port that reads assets from your own N64 ROM, with widescreen, mouse controls and split-screen. Version 0.5.0 remains pre-1.0.

Original or reference: **GoldenEye 007** · Decompilation-based project  
[Download and supply your own game files](https://github.com/jkdansereau/goldeneye-pc-port/releases) · [Browse RemakeList](https://remakelist.com/remakes/goldeneye-007-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=goldeneye-007-pc-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Linux / Steam Deck

**Status:** Playable or experimental preview.

**What you need:** Bring your own lawfully obtained Nintendo 64 · GoldenEye 007 ROM · USA. The project is free to access; the original game is separate. No game files, keys or ready-to-play packages are supplied here.

**What is available:** Official route: Windows / Linux / Steam Deck. Playable or experimental preview. PAL and Japanese ROM support remain incomplete. Choose the official package matching your system.

**Code license:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/jkdansereau/goldeneye-pc-port/blob/main/LICENSE)  
**Author:** jkdansereau  
[Official documentation](https://github.com/jkdansereau/goldeneye-pc-port#readme) · Sources reviewed: 2026-10-19

</details>

### [Gravity Rush 2 Native Port](https://github.com/HayatoG/gr2_pc)

A Gravity Rush 2 PC port for user-supplied PS4 game files, demonstrated running on Linux. Saves, open-world coverage and other platforms still need verification.

Original or reference: **Gravity Rush 2** · Platform compatibility layer  
[Download and supply your own game files](https://github.com/HayatoG/gr2_pc/releases/tag/v2026.10.24-a2e69a1) · [Browse RemakeList](https://remakelist.com/remakes/gravity-rush-2-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gravity-rush-2-native-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Linux x86-64 (glibc 2.39+) · Windows 10/11 x64 (gameplay unverified) · Vulkan

**Status:** v2026.10.24-a2e69a1 · experimental; Windows unvalidated

**What you need:** Supply your own PS4 Gravity Rush 2 US CUSA03694 base files merged with exact update 01.11, including that update’s eboot.bin (about 28 GB in total). Audio additionally needs libSceNgs2.sprx from your own PS4 firmware, placed in system_lib/. No game or firmware files are included.

**What is available:** v2026.10.24-a2e69a1 provides Linux x86-64 (glibc 2.39+) and Windows 10/11 x64 archives. It addresses cutscene shader/GPU deadlocks and DLC-loader imports. Linux gameplay is reported; the Windows package is explicitly not yet tested in game. Windows gameplay, saves and open-world coverage remain under validation. The author’s reported Linux performance is not a guarantee for every machine. RemakeList has not built, installed or played this release. Original files / setup: Supply your own PS4 Gravity Rush 2 US CUSA03694 base files merged with exact update 01.11, including that update’s eboot.bin (about 28 GB in total). Audio additionally needs libSceNgs2.sprx from your own PS4 firmware, placed in system_lib/. No game or firmware files are included.

**Code license:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/HayatoG/gr2_pc/blob/main/port/LICENSE)  
**Author:** HayatoG  
[Official documentation](https://github.com/HayatoG/gr2_pc#readme) · Sources reviewed: 2026-10-29

</details>

### [inFAMOUS Second Son Native Port](https://github.com/HayatoG/iss_pc)

An unofficial PC compatibility port of inFAMOUS Second Son using your own PS4 files, with Linux and Windows packages. Early chapters are documented; performance and graphics issues remain.

Original or reference: **inFAMOUS Second Son** · Platform compatibility layer  
[Download and supply your own game files](https://github.com/HayatoG/iss_pc/releases/tag/v1.0) · [Browse RemakeList](https://remakelist.com/remakes/infamous-second-son-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=infamous-second-son-native-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Linux x86-64 / Windows 10 (1903+)–11 x64 · Vulkan 1.3

**Status:** Stable v1.0 · optional beta-rc1 · original PS4 files

**What you need:** Supply your own decrypted PS4 CUSA00223 USA base game 1.00 merged with update 1.07, about 33 GB. Requires AVX, Vulkan 1.3 and preferably 6 GB VRAM. No console firmware file is required for audio; game files are not included.

**What is available:** v1.0 remains the recommended stable download for Linux x86-64 (glibc 2.39+) and Windows 10/11 x64. beta-rc1 is a separately downloadable prerelease on the same platforms, not the stable replacement. Frame rate and graphics remain uneven. Windows RX 580/Polaris compatibility is experimental. beta-rc1 lists black ground textures with upscaling, soft FSR at 3x and untested Linux upscaling; the launcher does not offer betas as normal updates. RemakeList has not installed or played either build.

**Code license:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/HayatoG/iss_pc/blob/main/port/LICENSE)  
**Author:** HayatoG  
[Official documentation](https://github.com/HayatoG/iss_pc#readme) · Sources reviewed: 2026-10-28

</details>

### [LAS Recomp](https://github.com/peiikai/LASRecomp)

Builds a native desktop port locally from your own Switch Link’s Awakening 1.0.0, 1.0.1 or 1.1.0 files, with widescreen and randomizer options. It remains in beta.

Original or reference: **The Legend of Zelda: Link’s Awakening** · Static recompilation  
[Build and supply your own game files](https://github.com/peiikai/LASRecomp/releases/tag/beta_5.4) · [Browse RemakeList](https://remakelist.com/remakes/las-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=las-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / Apple silicon macOS / Linux x64; experimental Linux ARM64

**Status:** beta_5.4 · Beta · original files required

**What you need:** Supply your own lawfully obtained exefs and romfs files from Switch Link’s Awakening 1.0.0, 1.0.1 or 1.1.0 and choose their folder for local compilation. Mac needs Apple silicon and macOS 15+. Windows 10/11 and Linux x64 need AVX2, FMA, Vulkan 1.3, at least 8 GB RAM and about 12 GB setup space. No game files or keys are provided.

**What is available:** beta_5.4 is the general Windows, Apple silicon Mac and Linux download, fixing BowWow rendering, grass lines, controller selection and several randomizer faults. The later test-462-arc-2 build is only for Intel Arc issue testing; its fix is not part of beta_5.4. Crashes, unsolvable seeds and widescreen faults remain possible, especially with room shuffling. Linux ARM64 lacks hardware tests; Intel Macs and older Intel integrated GPUs are unsupported. Pre-Beta-5 seed IDs change results. RemakeList has not built, installed or played this release.

**Code license:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/peiikai/LASRecomp/blob/main/LICENSE)  
**Author:** peiikai  
[Official documentation](https://github.com/peiikai/LASRecomp#readme) · Sources reviewed: 2026-10-30

</details>

### [Lets Go Recomp](https://github.com/raulzrrs/letsgo-recomp)

A Windows native port for your own Pokémon: Let’s Go files, primarily tested with Eevee 1.0.0 in early exploration, capture and battles. Full-game completion is unverified.

Original or reference: **Pokémon: Let’s Go, Eevee! / Pikachu!** · Static recompilation  
[Download and supply your own game files](https://github.com/raulzrrs/letsgo-recomp/releases) · [Browse RemakeList](https://remakelist.com/remakes/lets-go-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=lets-go-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10–11 x64 · Vulkan 1.3 · AVX2

**Status:** Playable or experimental preview.

**What you need:** Bring your own lawfully obtained Nintendo Switch · exefs + romfs · Eevee 1.0.0. The project is free to access; the original game is separate. No game files, keys or ready-to-play packages are supplied here.

**What is available:** Official route: Windows 10–11 x64 · Vulkan 1.3 · AVX2. Playable or experimental preview. Full-game coverage has not been verified. Eevee 1.0.0 is the main tested version; Pikachu and updates have narrower evidence. Choose the official package matching your system.

**Code license:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/raulzrrs/letsgo-recomp/blob/main/LICENSE)  
**Author:** raulzrrs  
[Official documentation](https://github.com/raulzrrs/letsgo-recomp#readme) · Sources reviewed: 2026-10-19

</details>

### [Muscle March Recomp](https://github.com/tmcleroy/muscle-march-recomp)

A beta native Muscle March port for desktop and Android using your own WiiWare copy and Wii key, with stick, touch and keyboard controls. Hardware coverage remains limited.

Original or reference: **Muscle March** · Static recompilation  
[Download and supply your own game files](https://github.com/tmcleroy/muscle-march-recomp/releases) · [Browse RemakeList](https://remakelist.com/remakes/muscle-march-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=muscle-march-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10–11 / macOS 13+ Apple silicon / Linux / Android 8+ ARM64

**Status:** Beta; bugs and incomplete testing remain.

**What you need:** Bring your own lawfully obtained WiiWare · USA WAD + Wii common key. The project is free to access; the original game is separate. No game files, keys or ready-to-play packages are supplied here.

**What is available:** Official route: Windows 10–11 / macOS 13+ Apple silicon / Linux / Android 8+ ARM64. Beta; bugs and incomplete testing remain. Published performance comes from limited devices. The author says releases include translated game code, despite excluding game-data files. Choose the official package matching your system.

**Code license:** [GPL-3.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/tmcleroy/muscle-march-recomp/blob/main/LICENSE)  
**Author:** tmcleroy  
[Official documentation](https://github.com/tmcleroy/muscle-march-recomp#readme) · Sources reviewed: 2026-10-19

</details>

### [NSMB Wii Multiplayer Recompilation](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation)

A native New Super Mario Bros. Wii port using your own supported USA disc files, with Android touch controls and LAN play across phones and Windows PCs.

Original or reference: **New Super Mario Bros. Wii** · Static recompilation  
[Download and supply your own game files](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation/releases/tag/v0.3.1) · [Browse RemakeList](https://remakelist.com/remakes/nsmb-wii-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nsmb-wii-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Android 9+ ARM64 · Windows 10/11 x64 · Linux x86-64 (hardware validation limited)

**Status:** v0.3.1 · Playable or experimental preview.

**What you need:** Bring your own lawfully obtained Wii · USA SMNE01 · revision 1. The project is free to access; the original game is separate. No game files, keys or ready-to-play packages are supplied here.

**What is available:** v0.3.1 provides Windows x64, Linux x64 and Android ARM64 packages and fixes wrong course tiles introduced in 0.3.0. The underlying update moves graphics work onto a second CPU core on eligible devices; gains are device-dependent. Saves, settings and imported game data carry over. This remains a preview. Linux has only WSL software-rendering tests; physical Linux/Steam Deck GPUs and Mali phones lack validation. Releases include translated game code, although game-data files are excluded. RemakeList has not built, installed or played it.

**Code license:** [GPL-3.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation/blob/main/LICENSE)  
**Author:** WitherBlitz  
[Official documentation](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation#readme) · Sources reviewed: 2026-10-30

</details>

### [OpenSA2](https://github.com/kittycache9/OpenSA2)

An experimental native Sonic Adventure 2 port for your own 2012 PC files, with early Windows, Linux and Android builds. Stage coverage remains incomplete.

Original or reference: **Sonic Adventure 2** · Static recompilation  
[Download and supply your own game files](https://github.com/kittycache9/OpenSA2/releases) · [Browse RemakeList](https://remakelist.com/remakes/opensa2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=opensa2-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Linux / Android

**Status:** Playable or experimental preview.

**What you need:** Bring your own lawfully obtained PC · Sonic Adventure 2 (2012) · executable + assets. The project is free to access; the original game is separate. No game files, keys or ready-to-play packages are supplied here.

**What is available:** Official route: Windows / Linux / Android. Playable or experimental preview. Full-game coverage has not been verified. Choose the official package matching your system. Official packages contain recompiled game logic and the port runtime. You must still supply your own supported 2012 PC executable and assets through the installer; these packages are not blank shells.

**Code license:** [GPL-3.0-only applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/kittycache9/OpenSA2/blob/main/LICENSE)  
**Author:** kittycache9  
[Official documentation](https://github.com/kittycache9/OpenSA2#readme) · Sources reviewed: 2026-10-19

</details>

### [Ottsel](https://github.com/chrissotraidis/ottsel)

An OpenGOAL-based Jak and Daxter Apple-platform port built on your Mac from a supported PS2 disc. This developer preview runs on iPad; physical iPhone play is not yet tested.

Original or reference: **Jak and Daxter: The Precursor Legacy** · Decompilation-based project  
[Build and supply your own game files](https://github.com/chrissotraidis/ottsel#readme) · [Browse RemakeList](https://remakelist.com/remakes/ottsel/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ottsel-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** iPadOS 18.5+ / macOS Apple silicon

**Status:** Developer preview; build/signing work is required.

**What you need:** Bring your own lawfully obtained PS2 · USA SCUS-97124 · Black Label. The project is free to access; the original game is separate. No game files, keys or ready-to-play packages are supplied here.

**What is available:** Official route: iPadOS 18.5+ / macOS Apple silicon. Developer preview; build/signing work is required. Physical iPad and Mac runs are documented; physical iPhone gameplay is unverified. Build locally using the official instructions.

**Code license:** [ISC applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/chrissotraidis/ottsel/blob/main/LICENSE)  
**Author:** chrissotraidis  
[Official documentation](https://github.com/chrissotraidis/ottsel#readme) · Sources reviewed: 2026-10-19

</details>

### [Phantom Hourglass Recomp](https://github.com/dguillot-gh/phantom-hourglass-recomp)

A Windows and Android Phantom Hourglass port built from your own DS cartridge dump, combining recompiled ARM9 code with melonDS hardware emulation and flexible screen layouts.

Original or reference: **The Legend of Zelda: Phantom Hourglass** · Static recompilation  
[Build and supply your own game files](https://github.com/dguillot-gh/phantom-hourglass-recomp#readme) · [Browse RemakeList](https://remakelist.com/remakes/phantom-hourglass-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=phantom-hourglass-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Android

**Status:** Playable or experimental preview.

**What you need:** Bring your own lawfully obtained Nintendo DS · USA · ROM SHA-1: 4c8f52dd719918bbcd46e73a8bae8628139c1b85 / 7e0d26d143992f1eee182b24f1abb9e7f038eacf. The project is free to access; the original game is separate. No game files, keys or ready-to-play packages are supplied here.

**What is available:** Official route: Windows / Android. Playable or experimental preview. Generated app and game-derived build files are for private use; do not redistribute them. Build locally using the official instructions.

**Code license:** [GPL-3.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/dguillot-gh/phantom-hourglass-recomp/blob/main/LICENSE)  
**Author:** dguillot-gh  
[Official documentation](https://github.com/dguillot-gh/phantom-hourglass-recomp#readme) · Sources reviewed: 2026-10-19

</details>

### [Pinyon Shift](https://github.com/arcanite24/pinyon-shift)

A playable native Forza Horizon preview built locally from your Xbox 360 disc, with desktop and Steam Deck routes, graphics options and owned-update support. Android remains alpha.

Original or reference: **Forza Horizon** · Static recompilation  
[Build and supply your own game files](https://github.com/arcanite24/pinyon-shift/releases/tag/v0.7.1) · [Browse RemakeList](https://remakelist.com/remakes/pinyon-shift/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pinyon-shift-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / Linux x86-64·SteamOS / macOS 13+ Apple silicon / Android 13+ alpha

**Status:** v0.7.1 · local build · Android alpha

**What you need:** Supply your own USA retail Xbox 360 Forza Horizon disc (MS-2505, title ID 4D5309C9) or supported unmodified extracted folder, with owned TU4/DLC separately. First build takes an author-estimated 20–60 minutes and about 30 GB free space. Desktop graphics require Vulkan 1.3. Android alpha needs Android 13+, Vulkan 1.3 and is tuned for Snapdragon 8 Gen 2+ with 8 GB RAM.

**What is available:** v0.7.1 provides Windows, Linux x86-64 and Apple silicon Mac launchers. Each compiles the game from your own files; updating rebuilds it while retaining saves/settings/DLC. Android has no ready-made release APK: build it on your PC through the launcher, then transfer it to your device. Rendering faults and slowdowns remain. AMD/Intel PC GPUs are not yet qualified; v4 on Linux/Mac has scripted-route testing only. Android is alpha, with non-Qualcomm GPUs opt-in. DLSS is Windows-only; DualSense over Bluetooth or off Windows is untested. Community UDLC has limited car coverage and separate content rights. RemakeList has not built or played it.

**Code license:** [BSD-3-Clause applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/arcanite24/pinyon-shift/blob/main/LICENSE)  
**Author:** arcanite24  
[Official documentation](https://github.com/arcanite24/pinyon-shift#readme) · Sources reviewed: 2026-10-28

</details>

### [Red Alert 2 Recomp](https://github.com/sp00nznet/redalert2-recomp)

Uses an installer to build a native version locally from your own Red Alert 2 / Yuri’s Revenge files, adding widescreen and modern presentation options. It is separate from OpenRA, RA2WEB and Vanguard.

Original or reference: **Red Alert 2 / Yuri’s Revenge** · Static recompilation  
[Build and supply your own game files](https://github.com/sp00nznet/redalert2-recomp/releases/tag/v0.1.3) · [Browse RemakeList](https://remakelist.com/remakes/redalert2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=redalert2-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / Linux x64 / macOS ARM64

**Status:** Installer available · local build · original game required

**What you need:** Supply your own Steam/EA App (Origin) installation containing game.exe 1.006 and gamemd.exe 1.001. The installer detects the files and generates and builds locally, installing build tools when needed. Generated original-game code and data stay local.

**What is available:** v0.1.3 offers Windows x64, Linux x64 and macOS ARM64 installers that generate and build locally from your own original files. It fixes some Windows launch failures and lingering processes after quit on Linux/macOS. The author estimates 30–60 minutes and about 6 GB for the first build. The installers are unsigned and may be blocked by the operating system. They require local building and include no original game files. Author scripted checks cover menus, skirmishes and campaign entry, not a RemakeList full-playthrough verification. MIT covers the project’s own code; EA game code and assets have separate rights. RemakeList has not built, installed or run it.

**Code license:** [MIT for project-authored tooling only; EA game code and assets retain separate rights.](https://github.com/sp00nznet/redalert2-recomp/blob/main/LICENSE)  
**Author:** sp00nznet  
[Official documentation](https://github.com/sp00nznet/redalert2-recomp#readme) · Sources reviewed: 2026-10-27

</details>

### [Road Trip Recomp](https://github.com/silentsudin/RoadTripAdventure-recomp)

Revisits Road Trip / Choro Q HG2 on desktops and Android, with widescreen, save states and a second-screen map. The first launch prepares the game locally from your own US disc image.

Original or reference: **Road Trip / Choro Q HG2** · Static recompilation  
[Download and supply your own game files](https://github.com/silentsudin/RoadTripAdventure-recomp/releases) · [Browse RemakeList](https://remakelist.com/remakes/road-trip-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=road-trip-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Android

**Status:** Preview · original game required

**What you need:** Owned Road Trip USA SLUS-20398 disc image .cue/.bin/.iso/.chd; app builds title locally on first launch.

**What is available:** Author reports Adventure and Quick Race playable; official ZIP/DMG/APK linked. Mac needs Apple Command Line Tools. Not built, installed or played by RemakeList.

**Code license:** [GPL-3.0; third-party notices separate](https://github.com/silentsudin/RoadTripAdventure-recomp#readme)  
**Author:** silentsudin  
[Official documentation](https://github.com/silentsudin/RoadTripAdventure-recomp#readme) · Sources reviewed: 2026-10-19

</details>

### [Rogue Squadron 64 Recomp](https://github.com/MikeSemicolonD/RogueSquadron64Recomp)

A static recompilation of N64 Star Wars: Rogue Squadron with widescreen and modern mouse, controller and flight-stick input. Bring the specified US ROM; Mac support is compile-only.

Original or reference: **Star Wars: Rogue Squadron** · Static recompilation  
[Build and supply your own game files](https://github.com/MikeSemicolonD/RogueSquadron64Recomp#readme) · [Browse RemakeList](https://remakelist.com/remakes/rogue-squadron64-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rogue-squadron64-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Linux / Android

**Status:** Source build · original game required

**What you need:** Owned Star Wars Rogue Squadron N64 USA v1.0 16 MB ROM. No ROM data distributed.

**What is available:** Documented source build for Windows, Linux and Android; the author reports complete playthrough capability. No release assets were listed: use the documented source build with your own USA v1.0 ROM. The author calls the game playable end to end, but experimental ray tracing, interpolation and multiplayer still have limitations. macOS is compile-only and has not been run on a Mac; Linux x86 was tested only on a 64-bit PC with software Vulkan. GPL-3.0 covers the project’s own host/mod/tool code, not original game rights. RemakeList has not built or played it.

**Code license:** [GPL-3.0 for host runtime, patches, hooks, mods, tools and docs; ROM-derived code and game assets are separate](https://github.com/MikeSemicolonD/RogueSquadron64Recomp/blob/main/LICENSE)  
**Author:** MikeSemicolonD  
[Official documentation](https://github.com/MikeSemicolonD/RogueSquadron64Recomp#readme) · Sources reviewed: 2026-10-28

</details>

### [Silent Hill — Native PC Port](https://github.com/SlickAmogus/silent-hill-decomp)

A native Silent Hill port built on the PS1 decompilation, with widescreen, modern controls and optional visual enhancements. Your disc data is required; Windows is the main target and other platforms remain experimental.

Original or reference: **Silent Hill** · Decompilation-based project  
[Download and supply your own game files](https://github.com/SlickAmogus/silent-hill-decomp/releases) · [Browse RemakeList](https://remakelist.com/remakes/silent-hill-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=silent-hill-native-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows

**Status:** Preview · original game required

**What you need:** Owned original Silent Hill PlayStation disc image, preferably USA SLUS-00707. Game data excluded.

**What is available:** The PC route remains separate from xbox360-alpha-1, a new Xbox 360/homebrew test package with an original-Xbox build alongside it. That alpha reports only opening scenes, basic interactions and some save loading; it does not establish a complete Xbox playthrough. Realtime PC/mobile builds are a separate, untested update channel. Windows remains the main PC route; Linux/Mac are unstable work in progress and mobile support is early. Supply your own original PS1 Silent Hill disc image; the port-layer GPL does not cover Konami data or decompiled game code. RemakeList has not built, installed or played this release.

**Code license:** [GPL-3.0 for port layer only; decompilation and Konami material not relicensed](https://github.com/SlickAmogus/silent-hill-decomp#readme)  
**Author:** Chris Hardin / KushAstronaut / SlickAmogus  
[Official documentation](https://github.com/SlickAmogus/silent-hill-decomp#readme) · Sources reviewed: 2026-10-30

</details>

### [SpeedBreaker](https://github.com/speedbreakerproject/speedbreaker)

Runs your own Xbox 360 Need for Speed: Most Wanted on modern devices with widescreen, split screen and display options. iPhone/iPad sideloading remains experimental, and Windows is in beta.

Original or reference: **Need for Speed: Most Wanted (2005)** · Static recompilation  
[Download and supply your own game files](https://github.com/speedbreakerproject/speedbreaker/releases) · [Browse RemakeList](https://remakelist.com/remakes/speedbreaker/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=speedbreaker-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Linux / SteamOS / Apple silicon macOS / experimental iOS·iPadOS / Windows beta

**Status:** v0.2.0 released · Windows beta · experimental iOS sideloading

**What you need:** Supply your own lawful USA NTSC-U or European PAL Spanish Xbox 360 Most Wanted ISO, XISO or extracted folder. No Title Update is used; other regions, Games on Demand and the PC edition are unsupported. Allow about 7.2 GB. Windows/Linux x64 need AVX2 and Vulkan 1.2; Mac needs Apple silicon and macOS 15+; iOS/iPadOS need 17+, an A15-class chip or newer, a controller or keyboard, and your own sideload signing.

**What is available:** The main v0.2.0 release provides SteamOS/Linux x86-64, Steam Frame ARM64, Apple silicon Mac and an experimental iOS IPA. Windows uses the separate v0.2.0-windows-beta.2 prerelease; no Android build is available. The two SteamOS architectures are not interchangeable. The author tested the Windows beta on limited Intel integrated-graphics hardware. The iOS IPA attachment itself has not been installed on a device; author testing used Xcode-signed builds, and sideload entitlements or memory limits can prevent running. The Mac app is not notarized; macOS 15 was tested only in a VM. Steam Frame presents a flat screen, not VR; the ARM64 package is untested on other Linux devices. Set Steam Deck OLED to 60 Hz; the LCD model is untested. No universal frame rate is promised. RemakeList has not run it.

**Code license:** [Project-authored code is GPL-3.0-or-later; bundled libraries retain their own licenses, and original game content is excluded.](https://github.com/speedbreakerproject/speedbreaker#readme)  
**Author:** project(u) / SpeedBreakerProject  
[Official documentation](https://github.com/speedbreakerproject/speedbreaker#readme) · Sources reviewed: 2026-10-27

</details>

### [Renegade Squadron — PC](https://github.com/gtteancum/starwars-renegadesquadron-pc)

A native port of PSP Star Wars Battlefront: Renegade Squadron with modern twin-stick controls and higher-resolution rendering. Windows has a Vulkan route; the Linux package has strict library requirements and limited hardware validation.

Original or reference: **Star Wars Battlefront: Renegade Squadron** · Static recompilation  
[Download and supply your own game files](https://github.com/GTTeancum/StarWars-RenegadeSquadron-PC/releases/tag/v0.9.1) · [Browse RemakeList](https://remakelist.com/remakes/renegade-squadron-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=renegade-squadron-pc-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · Vulkan 1.1 / DirectX 12; Linux x64 (Ubuntu 26.04-era, glibc 2.43+)

**Status:** v0.9.1 · Windows / restricted Linux build

**What you need:** Own PSP Star Wars Battlefront Renegade Squadron USA ULUS10292; extracted PSP_GAME directory in data/.

**What is available:** v0.9.1 makes native Vulkan the Windows default, retains optional DirectX 12, fixes model textures and automatically extracts your US ULUS10292 ISO. An additional Linux x64 archive targets Ubuntu 26.04-era systems only, with glibc 2.43+, FFmpeg 8 and Vulkan 1.1. Windows Hoth smoke tests and Linux WSL2 software-Vulkan smoke tests are reported; Linux hardware-GPU performance, physical controls and full-game coverage remain unverified. Enhanced lighting, shadows and bloom remain DirectX 12-only. The optional old HD pack has not been revalidated with Vulkan. Back up custom settings and preserve saves when updating.

**Code license:** [MIT for framework/port, third-party notices separate](https://github.com/GTTeancum/StarWars-RenegadeSquadron-PC/blob/main/work/project/source/LICENSE)  
**Author:** gtteancum  
[Official documentation](https://github.com/gtteancum/starwars-renegadesquadron-pc#readme) · Sources reviewed: 2026-10-29

</details>

### [Super Mario Bros. Wonder Recomp](https://github.com/BelmanteGu/SuperMarioWonderRecomp)

Statically recompiles Switch Super Mario Bros. Wonder for desktops and Android with native Vulkan rendering. It requires a source build and your own game, keys and firmware; compatibility is still evolving.

Original or reference: **Super Mario Bros. Wonder** · Static recompilation  
[Build and supply your own game files](https://github.com/BelmanteGu/SuperMarioWonderRecomp#readme) · [Browse RemakeList](https://remakelist.com/remakes/super-mario-wonder-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=super-mario-wonder-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux / Android

**Status:** Source build · original game required

**What you need:** Own Switch Wonder 1.0.0 title 010015100B514000 dump plus own keys and firmware; personal APK/data must not be shared.

**What is available:** Source build; author reports Mac reference platform, Android Galaxy S23, NVIDIA/Intel Windows and Linux. Known GPU and Windows character-select issues; full playthrough not established. Not built, installed or played by RemakeList.

**Code license:** [MIT authored code; Nintendo game and derivatives excluded](https://github.com/BelmanteGu/SuperMarioWonderRecomp#readme)  
**Author:** Projeto Belmante / BelmanteGu  
[Official documentation](https://github.com/BelmanteGu/SuperMarioWonderRecomp#readme) · Sources reviewed: 2026-10-19

</details>

### [Super Street Fighter II Turbo HD Remix — PC Port](https://github.com/saulob/ssf2t-hd-remix-recompiled)

Runs the Xbox Live Arcade Super Street Fighter II Turbo HD Remix natively on Windows with a launcher and local saves. The exact owned game package is required; online play is unavailable and Linux is not hardware verified.

Original or reference: **Super Street Fighter II Turbo HD Remix** · Static recompilation  
[Download and supply your own game files](https://github.com/saulob/ssf2t-hd-remix-recompiled/releases/tag/v0.2.2) · [Browse RemakeList](https://remakelist.com/remakes/ssf2t-hd-remix-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ssf2t-hd-remix-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows

**Status:** v0.2.2 · Windows / experimental Linux

**What you need:** Supply your own XBLA game package and Title Update #1 for Title ID 584108A4, Media ID 37B7D7D3. The launcher requires default.xex 0.0.1.3 plus default.xexp to obtain game version 0.0.2.3. Neither package is included; removing the update makes this version unplayable.

**What is available:** v0.2.2 provides Windows x64 and experimental Linux AppImage downloads. It now requires the original XBLA game plus Title Update #1, with separate installers and version validation. The update changes the required executable from 0.0.1.3 to 0.0.2.3. Offline only; Linux/Steam Deck packages have scripted checks but no real-hardware test. The game remains 60 updates per second. Only game 0.0.1.3 plus Title Update #1 (resulting 0.0.2.3) is supported. Windows is unsigned. Original files / setup: Supply your own XBLA game package and Title Update #1 for Title ID 584108A4, Media ID 37B7D7D3. The launcher requires default.xex 0.0.1.3 plus default.xexp to obtain game version 0.0.2.3. Neither package is included; removing the update makes this version unplayable.

**Code license:** [Project code is GPL-2.0-only; v0.2.2 now includes the TRG Launcher MIT notice in THIRD-PARTY-LICENSES.txt. Dependencies keep their own terms. None of these grants cover the original game or title-update content.](https://github.com/saulob/ssf2t-hd-remix-recompiled#readme)  
**Author:** saulob  
[Official documentation](https://github.com/saulob/ssf2t-hd-remix-recompiled#readme) · Sources reviewed: 2026-10-29

</details>

### [The Last Guardian — PC](https://github.com/hayatog/tlg_pc)

An unofficial PC compatibility port for your PS4 copy of The Last Guardian, with controller and keyboard/mouse input. The author tested Linux; Windows packages lack gameplay verification and your game and required system files are needed.

Original or reference: **The Last Guardian** · Platform compatibility layer  
[Download and supply your own game files](https://github.com/HayatoG/tlg_pc/releases/tag/v2026.10.27-4825a99) · [Browse RemakeList](https://remakelist.com/remakes/last-guardian-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=last-guardian-pc-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Linux x86-64 (glibc 2.39+) / Windows 10–11 x64 (gameplay unverified)

**Status:** v2026.10.27-4825a99 · preview · original PS4 files

**What you need:** Own PS4 CUSA03627 USA / CUSA03745 EU with update 01.03 merged (~25 GB), own console firmware libSceNgs2.sprx for audio.

**What is available:** v2026.10.27-4825a99 provides Linux and Windows archives without game files. Linux gameplay is author-reported; 30 FPS is the default, with optional experimental 60 FPS/unlocked settings. Windows has an automatic build but no author gameplay verification. Higher frame-rate modes remain experimental; full-game coverage is not established. macOS is planned, not downloadable. RemakeList has not built, installed or played it.

**Code license:** [GPL-2.0 per port/LICENSE and README; game/firmware excluded](https://github.com/HayatoG/tlg_pc/blob/main/port/LICENSE)  
**Author:** HayatoG  
[Official documentation](https://github.com/hayatog/tlg_pc#readme) · Sources reviewed: 2026-10-28

</details>

### [Tiberian Sun Recomp](https://github.com/sp00nznet/tiberiansun-recomp)

Builds a native version of your Tiberian Sun and Firestorm installation with widescreen and display settings. An early playable bring-up with skirmish and opening campaign checks; a full playthrough is unverified.

Original or reference: **Tiberian Sun / Firestorm** · Static recompilation  
[Build and supply your own game files](https://github.com/sp00nznet/tiberiansun-recomp/releases/tag/v0.1.0-alpha.2) · [Browse RemakeList](https://remakelist.com/remakes/tiberian-sun-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=tiberian-sun-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Linux; macOS via CrossOver (untested)

**Status:** Alpha installer · builds from your game

**What you need:** Own Steam Tiberian Sun + Firestorm installation with Game.exe, Language.dll and MIX files.

**What is available:** v0.1.0-alpha.2 offers platform installers that fetch the toolkit and build locally; Linux gets the F10 settings menu and expanded resolution choices. Installers build from your own Steam Tiberian Sun + Firestorm files; they are not bundled copies of the game. First setup takes roughly 30–60 minutes and 6 GB and may install build tools with permission. Installers are unsigned. Windows and Linux have documented testing; macOS uses CrossOver and has not been tested by the author. Full campaign completion remains unverified. RemakeList has not built, installed or played it.

**Code license:** [MIT authored tooling; EA game and generated C excluded](https://github.com/sp00nznet/tiberiansun-recomp/blob/main/LICENSE)  
**Author:** sp00nznet  
[Official documentation](https://github.com/sp00nznet/tiberiansun-recomp#readme) · Sources reviewed: 2026-10-28

</details>

### [Wind Waker HD Android — Plus](https://github.com/Nycolazs/WindWakerHD-Android-Plus)

An Android fork for your Wii U Wind Waker HD, adding Portuguese localization, touch layout tools and device fixes. Your disc image is required; this builds on the Android and Enhanced ports.

Original or reference: **The Legend of Zelda: The Wind Waker HD** · Static recompilation  
[Download and supply your own game files](https://github.com/Nycolazs/WindWakerHD-Android-Plus/releases) · [Browse RemakeList](https://remakelist.com/remakes/wind-waker-hd-android-plus/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wind-waker-hd-android-plus-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Android

**Status:** Preview · original game required

**What you need:** Own Wii U Wind Waker HD disc dump WUD/WUX + own keys, or own Cemu WUA archive. Local generated content must not be shared.

**What is available:** Official APK releases; Galaxy S20 FE 5G Snapdragon865 screenshots. Fork of Enhanced/Android port adding Portuguese translation, HUD editor and fixes; not separate original recreation. Not built, installed or played by RemakeList.

**Code license:** [MPL-2.0 code; translation/third-party notices separate](https://github.com/Nycolazs/WindWakerHD-Android-Plus#readme)  
**Author:** Nycolazs  
[Official documentation](https://github.com/Nycolazs/WindWakerHD-Android-Plus#readme) · Sources reviewed: 2026-10-19

</details>

### [Wind Waker HD — Mods Fork](https://github.com/asadsi/wwhd-recomp-mods)

An unofficial fork adding optional sea events, a sailable pirate ship and other mods to the native Wind Waker HD port. Bring your Wii U game; co-op is experimental and Android requires a self-build.

Original or reference: **The Legend of Zelda: The Wind Waker HD** · Static recompilation  
[Download and supply your own game files](https://github.com/asadsi/wwhd-recomp-mods/releases) · [Browse RemakeList](https://remakelist.com/remakes/wind-waker-hd-mods/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wind-waker-hd-mods-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / macOS / Linux

**Status:** Preview · original game required

**What you need:** Own supported USA/EUR Wii U game dump and required own keys, or own WUA per instructions. Local states/generated code not redistributable.

**What is available:** Unofficial mods branch, not base project author. v0.2.11 documented; desktop packages, optional mods and experimental online co-op. Android build yourself. Not built, installed or played by RemakeList.

**Code license:** [MPL-2.0 code; Nintendo assets excluded](https://github.com/asadsi/wwhd-recomp-mods#readme)  
**Author:** AsadSi / asadsi  
[Official documentation](https://github.com/asadsi/wwhd-recomp-mods#readme) · Sources reviewed: 2026-10-19

</details>

### [nxnative](https://github.com/seedds/nxnative)

Build apps from your own supported Switch game files on a Mac, for iPhone, iPad or Apple silicon Mac. Compatibility depends on the game profile and build.

Original or reference: **Nintendo Switch games** · Platform compatibility layer  
[Build and supply your own game files](https://github.com/seedds/nxnative#pack-an-ipa) · [Browse RemakeList](https://remakelist.com/remakes/nxnative/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nxnative-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** iPhone / iPad · iOS / iPadOS 26+; Apple silicon Mac · local build

**Status:** Local build required · author-reported compatibility

**What you need:** Supply NSP files from your own game, required updates/DLC and your own prod.keys. Build locally on a Mac with Xcode and Homebrew. The iPhone/iPad route produces an unsigned IPA for separate signing and sideloading; Apple silicon Mac uses the Mac app route. Generated packages contain game-derived code and resources for personal use, not redistribution. No commercial games, keys or ready-to-install game packages are supplied here; check your rights to your files.

**What is available:** Check the author’s current game-status table and each game profile before building. Tears of the Kingdom is now reported playable on iPhone; its 60 fps option requires update 1.4.3 and does not guarantee that rate on every device. The Mac app route uses --platform mac-app and opens from Finder on Apple silicon. An iPhone report does not establish Mac compatibility.

**Code license:** [MIT project code · game rights and third-party licenses separate](https://github.com/seedds/nxnative/blob/main/LICENSE)  
**Author:** seedds and contributors  
[Official documentation](https://github.com/seedds/nxnative/blob/main/README.md) · Sources reviewed: 2026-10-25

</details>

### [Zelda-Mobile · Tears of the Kingdom](https://github.com/OJZen/totk-mobile)

An experimental native Apple silicon port of Tears of the Kingdom v1.4.3. Build from source with your own game; iPhone gameplay is not verified.

Original or reference: **The Legend of Zelda: Tears of the Kingdom** · Platform compatibility layer  
[Build and supply your own game files](https://github.com/OJZen/totk-mobile/blob/main/docs/getting-started.md) · [Browse RemakeList](https://remakelist.com/remakes/totk-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=totk-mobile-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Apple silicon Mac; M1+ iPad; iPhone 15 Pro · experimental

**Status:** Experimental · source build · no formal release

**What you need:** Requires your own Switch base game, v1.4.3 update in .nsz format and matching prod.keys, dumped from your own console. Only v1.4.3 is supported. Prepare an Apple silicon Mac with full Xcode, command line tools, Homebrew and about 60 GB free. iPhone/iPad installation also needs iOS/iPadOS 26+, developer signing, Developer Mode, USB and about 25 GB free on the device. The repository and this listing provide no game files, keys, signed apps or derived shader packages. Code licensing does not grant rights to Nintendo game content.

**What is available:** Experimental source build; no formal Releases. The author reports loading saves and playing scenes on Apple silicon Mac, but has not validated a full playthrough. M1-or-newer iPads run well below 60 FPS at original resolution; controller support is not fully verified. iPhone 15 Pro is verified only through installation, resource transfer and a warm launch to the title screen: gameplay, frame rate, memory and thermals are unmeasured. Other iPhones, including iPhone 13 Pro, are untested. New scenes may stutter while shaders compile.

**Code license:** [Original code: Apache-2.0 · reused components retain their own licenses](https://github.com/OJZen/totk-mobile/blob/main/LICENSE)  
**Author:** JZen (@JZennm)  
[Official documentation](https://github.com/OJZen/totk-mobile/blob/510d95b8da159c0a7da467ad51b10a5a7c7ac133/README.md) · Sources reviewed: 2026-10-20

</details>

### [Melee Unlocked](https://github.com/Hero88go/melee-unlocked)

A native PC port of Super Smash Bros. Melee with Slippi online play and high-refresh presentation. Requires your own NTSC 1.02 ISO.

Original or reference: **Super Smash Bros. Melee (NTSC 1.02)** · Platform compatibility layer  
[Download and supply your own game files](https://github.com/Hero88go/melee-unlocked/releases/tag/v0.9.72) · [Browse RemakeList](https://remakelist.com/remakes/melee-unlocked/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=melee-unlocked-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 / Linux x86-64 (AVX2, OpenGL 4.5)

**Status:** Beta v0.9.72 · Linux experimental · own ISO required

**What you need:** Supply a lawfully obtained, clean, uncompressed Super Smash Bros. Melee NTSC 1.02 ISO. No original game data is included; the code license does not cover the game's assets.

**What is available:** v0.9.72 supplies Windows x64 and Linux x64 packages. It fixes Fountain of Dreams reflections in true widescreen and prevents unsupported camera projections in mod discs from terminating the game. Use your own NTSC 1.02 ISO; close the game and launcher before updating. This remains beta software. Linux is experimental and requires AVX2/OpenGL 4.5; Static Recomp is Windows-only, and mod compatibility depends on the engine. RemakeList has not built, installed or played this release.

**Code license:** [GPL-3.0-or-later · port code; third-party components keep their own terms.](https://github.com/Hero88go/melee-unlocked/blob/main/LICENSE)  
**Author:** Hero88go / Melee Unlocked contributors  
[Official documentation](https://github.com/Hero88go/melee-unlocked#readme) · Sources reviewed: 2026-10-30

</details>

### [Brawl Recompiled](https://github.com/josiahg2502-glitch/BrawlRecompiled)

A native PC port of Super Smash Bros. Brawl for Windows and Linux, built through static recompilation. Requires your own USA RSBE01 revision 1 disc image.

Original or reference: **Super Smash Bros. Brawl (Wii, USA RSBE01 revision 1)** · Static recompilation  
[Download and supply your own game files](https://github.com/josiahg2502-glitch/BrawlRecompiled/releases/tag/v0.5.0) · [Browse RemakeList](https://remakelist.com/remakes/brawl-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=brawl-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Linux 64-bit (glibc 2.35+, Vulkan)

**Status:** v0.5.0 · early build

**What you need:** Requires your own lawfully obtained Brawl disc image: USA, RSBE01, revision 1 (ISO, CISO or WBFS). Extraction needs about 7 GB. Convert RVZ, WIA, GCZ or NKit images to plain ISO first. RemakeList does not provide disc images.

**What is available:** v0.5.0 supplies Windows and Linux packages. It adds optional 240 fps visual interpolation, with lower adaptive rates, and transfers the complete save for online play to fix a bug that could overwrite the host save. The higher display rate is interpolation, not 240 updates per second in the game logic. Work in progress: Classic and Subspace are reported tested only at their start. 120/180/240 fps interpolation remains experimental. Some networks block direct connections; vanilla online play is the tested path, and modded participants need matching SD content. Interpreted menu mods can run below 60 fps.

**Code license:** [GPLv3 · project code only; original game artwork and third-party components have separate rights and terms.](https://github.com/josiahg2502-glitch/BrawlRecompiled/blob/v0.4.0/wiicompiled/LICENSE)  
**Author:** JosiahG  
[Official documentation](https://github.com/josiahg2502-glitch/BrawlRecompiled/blob/master/README.md) · Sources reviewed: 2026-10-29

</details>

### [Splinter Cell: Double Agent — Xbox Recomp](https://github.com/TGP482/SCDA-XBERecomp)

A native Windows port of the original Xbox version of Splinter Cell: Double Agent. Adds mouse and keyboard controls, adjustable resolution and frame rate, plus co-op; requires your own Xbox game files.

Original or reference: **Splinter Cell: Double Agent (original Xbox, 2006)** · Static recompilation  
[Download and supply your own game files](https://github.com/TGP482/SCDA-XBERecomp/releases/tag/V3) · [Browse RemakeList](https://remakelist.com/remakes/scda-xbe-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=scda-xbe-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10+ x64 · Direct3D 12

**Status:** V3 release · original Xbox files required

**What you need:** Your own lawfully obtained original Xbox copy of Double Agent. The release accepts an ISO or extracted files; keep default.xbe, sc4_adv.xbe and the Default, Media and adv folders together. Source builds require extracted files. PC and Xbox 360 game files are not substitutes. No game assets are included.

**What is available:** V3 provides a Windows package that compiles your original-Xbox Double Agent files on first launch. It adds texture dumping/replacement, separate aiming sensitivities, gyro aiming and color-blind modes, and fixes high-frame-rate water and ragdoll behavior. RemakeList has not built, installed or played this release.

**Code license:** [MIT for the project code; original game content and third-party components retain their own rights.](https://github.com/TGP482/SCDA-XBERecomp/blob/main/LICENSE)  
**Author:** TGP482  
[Official documentation](https://github.com/TGP482/SCDA-XBERecomp#readme) · Sources reviewed: 2026-10-30

</details>

### [P.T. for PC](https://github.com/LoreanXavier/pt-pc)

A desktop port of the PS4 P.T. teaser, with keyboard, controller and photo-mode controls. Requires your own PS4 game data.

Original or reference: **P.T. (PS4, 2014)** · Platform compatibility layer  
[Download and supply your own game files](https://github.com/LoreanXavier/pt-pc/releases/tag/v1.0.8) · [Browse RemakeList](https://remakelist.com/remakes/pt-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pt-pc-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 / Linux x86-64 / macOS 14+

**Status:** v1.0.8 · Early port · original files required

**What you need:** Supply lawfully obtained PS4 P.T. data. The author tests the US CUSA01127 edition; encrypted store PKGs cannot be used. The port and installer do not include the original game files.

**What is available:** v1.0.8 has Windows and Linux installers and portable packages, plus Apple silicon and Intel Mac builds. Linux requires glibc 2.38+; graphics require Vulkan 1.3, with bundled MoltenVK on macOS. RemakeList has not run the builds. Intel Mac builds have not been tested on a physical Intel Mac. VR has only been checked against a simulated runtime. Some effects and upscalers are unavailable on macOS; hardware support varies.

**Code license:** [MIT for project code; original game content and third-party components retain their own rights and terms.](https://github.com/LoreanXavier/pt-pc/blob/main/LICENSE)  
**Author:** LoreanXavier  
[Official documentation](https://github.com/LoreanXavier/pt-pc/blob/main/README.md) · Sources reviewed: 2026-10-26

</details>

### [GT4Recomp](https://github.com/moesuito/gt4-staticrecomp)

A Windows port of Gran Turismo 4 with configurable resolution, controllers and texture packs. Requires your own supported PS2 disc image.

Original or reference: **Gran Turismo 4 (PS2)** · Static recompilation  
[Download and supply your own game files](https://github.com/moesuito/gt4-staticrecomp/releases/tag/v1.3.0-rc6) · [Browse RemakeList](https://remakelist.com/remakes/gt4-staticrecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gt4-staticrecomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · Vulkan / Direct3D 12 / Direct3D 11

**Status:** v1.3.0-rc6 · Pre-release · original files required

**What you need:** Requires a lawfully obtained plain ISO of Gran Turismo 4 USA v2.00 (SCUS-97328). Spec II needs your own Spec II 1.10 image separately. The project supplies no game or mod files.

**What is available:** v1.3.0-rc6 is a public test build with Windows installer and portable ZIP, not the final 1.3.0 release. Vulkan is the tested default; Direct3D 12 and 11 are newer alternatives. Linux and Android remain planned. Release candidate: some license demos and menu backgrounds do not play; racing wheels are unsupported and long sessions are not fully tested. Performance Mode removes light flares and sun glare. Spec II ultrawide HUD issues remain; performance is hardware-dependent.

**Code license:** [MIT for original project code; the separate PCSX2 GS process is GPL-3.0-or-later. Original game and mod content have separate rights.](https://github.com/moesuito/gt4-staticrecomp/blob/main/LICENSE)  
**Author:** moesuito  
[Official documentation](https://github.com/moesuito/gt4-staticrecomp/blob/main/README.md) · Sources reviewed: 2026-10-26

</details>

### [God of War PSP Recomp](https://github.com/DrummingBird1/gow-psp-recomp)

A Windows launcher that rebuilds the two PSP God of War games from your own US disc images, with modern display and input settings.

Original or reference: **God of War: Chains of Olympus / Ghost of Sparta (PSP)** · Static recompilation  
[Download and supply your own game files](https://github.com/DrummingBird1/gow-psp-recomp/releases/tag/v1.3.1) · [Browse RemakeList](https://remakelist.com/remakes/gow-psp-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gow-psp-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows · Linux / Steam Deck planned

**Status:** v1.3.1 · Early port · original files required

**What you need:** Supply lawfully obtained US PSP disc images in CHD or ISO: Chains of Olympus UCUS98653 and/or Ghost of Sparta UCUS98737. No original game data is supplied by the project.

**What is available:** v1.3.1 provides a Windows launcher ZIP. First Build downloads portable tools after asking, then compiles the selected game locally. Windows is the current release platform; neither game has a verified full playthrough. Preview software; late levels, bosses and endings may have bugs. Linux and Steam Deck are planned. Unsigned launcher; build tools need an initial download. Automated level tours do not establish full-game completion.

**Code license:** [GPL-3.0-or-later for project code; original game content and third-party components retain their own rights and terms.](https://github.com/DrummingBird1/gow-psp-recomp/blob/main/LICENSE)  
**Author:** DrummingBird1  
[Official documentation](https://github.com/DrummingBird1/gow-psp-recomp/blob/main/README.md) · Sources reviewed: 2026-10-26

</details>

### [PrimeRecomp](https://github.com/gminustwo/primerecomp)

An early desktop port of Metroid Prime Remastered with mouse controls. Setup requires your own extracted Switch v1.0.0 files.

Original or reference: **Metroid Prime Remastered (Switch)** · Static recompilation  
[Build and supply your own game files](https://github.com/gminustwo/primerecomp/releases/tag/v0.0.4) · [Browse RemakeList](https://remakelist.com/remakes/primerecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=primerecomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / Linux x86-64 / macOS 15+ Apple Silicon

**Status:** v0.0.4 · Early beta · original files required

**What you need:** Supply lawfully obtained Metroid Prime Remastered v1.0.0 Switch files without updates, extracted into exefs and romfs folders. No original game data is included.

**What is available:** v0.0.4 supplies Windows ZIP, Linux AppImage and Apple silicon Mac DMG downloads. GPU ASTC decoding and fewer lighting uploads reduce door-transition stalls in the author’s measured scene. Setup compiles locally from your own extracted Metroid Prime Remastered 1.0.0 files. Windows/Linux require AVX2 and Vulkan 1.3; Linux needs glibc 2.35+. Visual faults remain, and areas beyond Magmoor Caverns are untested and may crash or freeze. Steam Deck measurements cover specific scenes, not the full game. Mac is unnotarized and initial shader stutters remain. RemakeList has not built, installed or played it.

**Code license:** [MIT for project code; original game content and third-party components retain their own rights and terms.](https://github.com/gminustwo/primerecomp/blob/main/LICENSE)  
**Author:** gminustwo  
[Official documentation](https://github.com/gminustwo/primerecomp/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

### [Wario Land: Shake It! Native PC](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC)

A Windows port of the Wii Wario Land game, with keyboard/controller input and configurable graphics. Requires your own supported US game image.

Original or reference: **Wario Land: Shake It! (Wii)** · Static recompilation  
[Build and supply your own game files](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC/releases/tag/v0.2.0) · [Browse RemakeList](https://remakelist.com/remakes/wario-land-shake-it-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wario-land-shake-it-pc-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · Direct3D 12 / Vulkan

**Status:** v0.2.0 · Testing build · local compilation required

**What you need:** Supply a lawfully obtained, unmodified US Wii Wario Land: Shake It! (RWLE01) image or extracted sys/files folders. The launcher validates the original main.dol. Allow about 3 GB for the build and another 4.4 GB for image extraction. No original game data, executable or translated game code is supplied.

**What is available:** v0.2.0 supplies a Windows launcher and ZIP with build tools, not a ready-compiled game. After importing your own supported US Wii image, it builds locally in an estimated 15–45 minutes; 16 GB RAM is recommended. Windows 10/11 x64 and D3D12 or Vulkan are required. Still a testing build despite GitHub’s prerelease flag being off. Full-game, boss, movie and DualSense motion coverage is incomplete; rendering issues and crashes remain possible. Widescreen and interpolation are experimental. RemakeList has not installed or played it.

**Code license:** [GPL-3.0 for project code; original game content and third-party components retain their own rights and terms.](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC/blob/main/LICENSE)  
**Author:** santiagovalencia109  
[Official documentation](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [PGR4 Native](https://github.com/shaunsingh/pgr4-native)

A Project Gotham Racing 4 recompilation with a native Direct3D 12 renderer. Runs on Windows or through Proton with your own game and Title Update #2.

Original or reference: **Project Gotham Racing 4 (Xbox 360)** · Static recompilation  
[Download and supply your own game files](https://github.com/shaunsingh/pgr4-native/releases/tag/v0.3.0) · [Browse RemakeList](https://remakelist.com/remakes/pgr4-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pgr4-native-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / Linux and Steam Deck via Proton

**Status:** v0.3.0 · Windows; Proton on Linux

**What you need:** Supply your own lawfully obtained extracted PGR4 disc and Title Update #2 package or files. The author reports PAL and NTSC disc contents match. No original game data is included.

**What is available:** v0.3.0 supplies a Windows x64 ZIP with 16:10 rendering, in-game settings, dynamic resolution and optional FidelityFX frame generation. Linux and SteamOS use Proton. Provide your own extracted PGR4 disc and Title Update 2, plus your own optional DLC. Frame generation can present 90 frames from 45 rendered frames; author performance measurements are not a guarantee for every Steam Deck or GPU. RemakeList has not played it.

**Code license:** [MIT for project code; original game content and third-party components retain their own rights and terms.](https://github.com/shaunsingh/pgr4-native/blob/main/LICENSE)  
**Author:** shaunsingh  
[Official documentation](https://github.com/shaunsingh/pgr4-native/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

### [Sky Recomp](https://github.com/Apolinario-coder/SkyRecomp)

An experimental desktop port of Skyward Sword HD, with keyboard/mouse controls and graphics settings. Requires your own Switch v1.0.0 game files.

Original or reference: **The Legend of Zelda: Skyward Sword HD (Switch)** · Static recompilation  
[Download and supply your own game files](https://github.com/Apolinario-coder/SkyRecomp/releases/tag/v2.0.2) · [Browse RemakeList](https://remakelist.com/remakes/skyrecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=skyrecomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Linux / macOS

**Status:** v2.0.2 · Early port · original files required

**What you need:** Supply your own lawfully obtained Skyward Sword HD Switch v1.0.0 files without updates. Original game files are not supplied. Optional visual packs retain their authors’ separate terms.

**What is available:** v2.0.2 provides Windows, Linux and macOS packages. Windows/Linux require supported Vulkan 1.3 hardware; x86 builds require AVX2. macOS uses the project’s Metal backend. Full-game stability is not established. Experimental: crashes, menu freezes and rendering differences remain under investigation. High-frame-rate modes are experimental and hardware-dependent. RemakeList has not installed or played these packages.

**Code license:** [MIT for original code; LAS Recomp and third-party components retain their notices. Texture packs and presets have separate authors and terms.](https://github.com/Apolinario-coder/SkyRecomp/blob/main/LICENSE)  
**Author:** Apolinario-coder  
[Official documentation](https://github.com/Apolinario-coder/SkyRecomp/blob/main/README.md) · Sources reviewed: 2026-10-26

</details>

### [Madden NFL 08 Recompiled](https://github.com/anishchandra24/MaddenNFL08-Recompiled)

An early Windows port of the Xbox 360 Madden NFL 08. Its setup downloads the toolchain and builds locally from your own extracted game files.

Original or reference: **Madden NFL 08 (Xbox 360)** · Static recompilation  
[Download and supply your own game files](https://github.com/anishchandra24/MaddenNFL08-Recompiled/releases/tag/v0.1.0) · [Browse RemakeList](https://remakelist.com/remakes/madden-nfl08-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=madden-nfl08-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · Direct3D 12 with ROV

**Status:** v0.1.0 · Pre-release · original files required

**What you need:** Supply your own legally obtained Xbox 360 Madden NFL 08 (Title ID 4541081D), extracted with default.xex and other game files together. Only the executable revision specified in the README is supported.

**What is available:** v0.1.0 is a prerelease setup executable, not a ready-to-play game binary. Setup needs the supported game files, internet access, Git and Visual Studio 2022 Community with C++ tools, and about 10 GB build space. Requires a fast CPU and Direct3D 12 rasterizer-ordered views (ROV). The author’s low-end PC could not run matches playably; only two PCs were tested. Shader stutter, some visual/audio issues and unsupported online services remain.

**Code license:** [GPL-3.0 for project code; original game content and third-party components retain their own rights and terms.](https://github.com/anishchandra24/MaddenNFL08-Recompiled/blob/main/LICENSE)  
**Author:** anishchandra24  
[Official documentation](https://github.com/anishchandra24/MaddenNFL08-Recompiled/blob/main/README.md) · Sources reviewed: 2026-10-26

</details>

### [CPS-2 Recomp](https://github.com/tmcleroy/cps2recomp)

A collection of unofficial CPS-2 and CPS-1 arcade ports with one launcher, fighting-game training tools and three-player beat-’em-ups. Requires the exact supported ROM sets from your own arcade boards.

Original or reference: **Capcom CPS-2 / CPS-1 arcade games** · Static recompilation  
[Download and supply your own game files](https://github.com/tmcleroy/cps2recomp/releases/tag/v1.0.0) · [Browse RemakeList](https://remakelist.com/remakes/cps2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cps2-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · macOS 13+ (Apple Silicon / Intel) · Linux x86_64 / ARM64 / SteamOS

**Status:** v1.0.0 · full release · 17 games

**What you need:** Supply the exact supported arcade ROM revision from a board you own, with its key file for CPS-2 games. The launcher verifies checksums and rejects other regions or revisions; some sets also need their parent set. No game files or keys are supplied.

**What is available:** v1.0.0 is the author’s first full non-beta release, with Windows x64, universal macOS and Linux x64/ARM64 packages. It adds rollback online play and three games, bringing the supported lineup to 17. Every player still supplies the exact supported ROM sets and keys; no games are included. The author’s release status does not establish complete testing on every machine or game. Windows is unsigned and macOS is not notarized. Exact ROM revisions are required; RemakeList has not installed or played it.

**Code license:** [Project code is GPL-3.0-only; third-party components retain their own notices. This license does not grant rights to Capcom or other rights holders’ game code, ROMs, keys, music or artwork.](https://github.com/tmcleroy/cps2recomp/blob/main/LICENSE)  
**Author:** tmcleroy  
[Official documentation](https://github.com/tmcleroy/cps2recomp/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [Free Riders Recompiled](https://github.com/YuutaTsubasa/Free-Riders-Recompiled)

An unofficial port of the Xbox 360 Sonic Free Riders with controller and keyboard play without Kinect. It imports game data from your own USA/Europe disc image and remains a work in progress.

Original or reference: **Sonic Free Riders (Xbox 360)** · Static recompilation  
[Download and supply your own game files](https://github.com/YuutaTsubasa/Free-Riders-Recompiled/releases/tag/v0.10.38) · [Browse RemakeList](https://remakelist.com/remakes/free-riders-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=free-riders-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows / Linux x64 · Android arm64 · experimental macOS Apple Silicon / iOS

**Status:** v0.10.38 · Work in progress · original disc required

**What you need:** Supply your own lawfully acquired USA/Europe Xbox 360 Sonic Free Riders disc image (.iso). The launcher imports the models, textures, audio and movies from it. The author says releases include the recompiled program, not the original game-data files; the project’s GPL license does not license SEGA’s content.

**What is available:** v0.10.38 adds optional camera-based body tracking to Android and Linux; Android asks for camera permission only when that feature opens a camera. Windows, Linux, Apple silicon Mac, Android and iOS packages are available. Actual camera gameplay on Android/Linux remains untested; validation used stored pictures, and the tested Thor has no camera. Many modes and online/Kinect v2 support still need validation. Apple support is experimental, Mac unnotarized and iOS requires sideloading. RemakeList has not built, installed or played this release.

**Code license:** [Project code is GPL-3.0-or-later. The original game’s code and data remain SEGA’s and are outside that grant; third-party components and models retain their separate licenses.](https://github.com/YuutaTsubasa/Free-Riders-Recompiled/blob/main/COPYING)  
**Author:** YuutaTsubasa  
[Official documentation](https://github.com/YuutaTsubasa/Free-Riders-Recompiled/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

### [James Pond 2 Recompiled](https://github.com/griches/JamesPond2RobocodRecomp)

A community port of the Amiga James Pond 2 with widescreen, save slots and smoother display motion. Requires your own supported Kixx disk image or WHDLoad installation.

Original or reference: **James Pond 2: Codename RoboCod (Amiga)** · Static recompilation  
[Download and supply your own game files](https://github.com/griches/JamesPond2RobocodRecomp/releases/tag/v1.0.4) · [Browse RemakeList](https://remakelist.com/remakes/james-pond-2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=james-pond-2-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · macOS 13+ (Apple Silicon / Intel) · Linux x86_64 / Steam Deck · Android 7+ ARM64 (untested) · PS5 homebrew

**Status:** Windows v1.0.4 · other platforms separate

**What you need:** Supply your own lawfully obtained Kixx Amiga re-release as a standard .adf disk image, optionally gzip-compressed as .adz or in a .zip, or a supported WHDLoad installation. The original Millennium copy-protected release, extended ADF, .dms and .ipf images are not supported. No original disk download is provided here.

**What is available:** v1.0.4 is a Windows-only fix for repeated saves and settings failing after the first save, including non-English user-folder paths. Other platforms retain their own versions: macOS/Linux 1.0.0, PS5 1.0.2 and Android 1.0.3. Supply a supported lawfully obtained Amiga copy; no game data is included. Android 1.0.3 is a first test release that the author has not played on an Android device; it requires Android 7+ ARM64 and built-in or external physical controls. PS5 requires an existing homebrew environment. RemakeList has not installed, played or independently verified full-game compatibility.

**Code license:** [The project’s own code is GPL-3.0. SDL3, Musashi, fonts and other dependencies retain their separate licenses; the original game’s code, artwork and music are not granted under the project license.](https://github.com/griches/JamesPond2RobocodRecomp/blob/main/LICENSE)  
**Author:** griches  
[Official documentation](https://github.com/griches/JamesPond2RobocodRecomp/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [recvx-enhanced-port](https://github.com/aikatore/recvx-enhanced-port)

An enhanced Code: Veronica X port with two-player co-op, optional third-person aiming and widescreen. It reads your own PS2 disc image.

Original or reference: **Resident Evil Code: Veronica X (PS2)** · Community port  
[Download and supply your own game files](https://github.com/aikatore/recvx-enhanced-port/releases/tag/v0.6.10) · [Browse RemakeList](https://remakelist.com/remakes/recvx-enhanced-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=recvx-enhanced-port-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10+ x86 · Linux i686 · OpenGL 3.3

**Status:** v0.6.10 · prerelease · two-player co-op

**What you need:** Your own legally obtained PS2 NTSC-U Code: Veronica X ISO, serial SLUS-20184. Game data and optional HD texture packs are not included.

**What is available:** v0.6.10 is a prerelease with Windows x86 and Linux i686 game packages plus a separate Linux x86_64 co-op server. Linux requires glibc 2.34+ and 32-bit graphics/audio libraries; both clients need OpenGL 3.3. Cutscene model swapping remains an early implementation, and co-op/mod combinations may have bugs.

**Code license:** [MIT for the port and credited decompilation code; third-party components and Capcom game content have separate terms.](https://github.com/aikatore/recvx-enhanced-port/blob/main/LICENSE)  
**Author:** aikatore  
[Official documentation](https://github.com/aikatore/recvx-enhanced-port/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [Code Veronica PS3 HD Recomp](https://github.com/kastieloficial/RE-Code-Veronica-PS3-HD-Recomp-PC)

A PS3 Code: Veronica X HD port with interpolation, speedrun tools and a modern combat HUD. Requires your own supported PSN release.

Original or reference: **Resident Evil Code: Veronica X HD (PS3)** · Static recompilation  
[Download and supply your own game files](https://github.com/kastieloficial/RE-Code-Veronica-PS3-HD-Recomp-PC/releases/tag/v1.1.11) · [Browse RemakeList](https://remakelist.com/remakes/code-veronica-ps3-hd-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=code-veronica-ps3-hd-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · Direct3D 12

**Status:** v1.1.11 · Windows · own PS3 files

**What you need:** Your own PS3 PSN base release 01.00: NPEB00553 (EU), NPUB30467 (US) or NPJB00135 (Japan), with PARAM.SFO and USRDIR/EBOOT.BIN. EU/US also require the purchasing account’s .rap license. Updates and disc editions are unsupported; the launcher does not open PKGs directly.

**What is available:** v1.1.11 provides the Windows PC archive and a PKG extraction tool, improves launcher startup and texture switching, and keeps optional texture downloads separate. The US game was used for the build; European/Japanese identities were checked by filenames, not play-tested. Supply your own PS3 PSN game files and required licenses. Optional third-party/AI-upscaled texture packs have separate rights and are not covered automatically by the port code’s MIT license. RemakeList has not built or played it.

**Code license:** [MIT for port/ps3recomp code; third-party terms and Capcom’s original game rights are separate.](https://github.com/kastieloficial/RE-Code-Veronica-PS3-HD-Recomp-PC/blob/code-veronica/LICENSE)  
**Author:** kastieloficial  
[Official documentation](https://github.com/kastieloficial/RE-Code-Veronica-PS3-HD-Recomp-PC/blob/code-veronica/README.md) · Sources reviewed: 2026-10-29

</details>

### [OpenRAC](https://github.com/OpenRAC/OpenRAC)

A native Ratchet &amp; Clank port with a shared launcher, graphical enhancements and mod tools. The first game is playable; later games remain in progress.

Original or reference: **Ratchet &amp; Clank (PS2)** · Community port  
[Download and supply your own game files](https://github.com/OpenRAC/OpenRAC/releases/tag/launcher-v0.9.0) · [Browse RemakeList](https://remakelist.com/remakes/openrac/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openrac-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 · Linux x64 / ARM64 · macOS universal · Android ARM64

**Status:** launcher-v0.9.0 · first game playable · sequels in progress

**What you need:** Your own first-game PS2 disc as ISO or CHD: PAL SCES_509.16 disc v2.00, or NTSC-U SCUS_971.99 disc v1.00. The launcher checks the disc; other regions/editions may not match. No game data is downloaded.

**What is available:** launcher-v0.9.0 remains the general launcher release. sdk-v1.10.0 updates the mod-development SDK, not the playable game version. launcher-dev-master contains a separate 0.9.1 development build and should not be presented as the stable launcher. Only the first Ratchet &amp; Clank is listed as playable. Later games are incomplete; Android is packaged as a debug APK and enhanced graphics are experimental.

**Code license:** [Top-level launcher/tools use GPL-3.0-or-later; game modules and the MIT SDK/editor retain their own notices. None of these licenses grant original game-content rights.](https://github.com/OpenRAC/OpenRAC/blob/master/LICENSE.md)  
**Author:** OpenRAC  
[Official documentation](https://github.com/OpenRAC/OpenRAC/blob/master/README.md) · Sources reviewed: 2026-10-29

</details>

### [The Umbrella Chronicles Recompiled](https://github.com/solleo95/reuc-recomp)

A Windows port of The Umbrella Chronicles with mouse aiming, modern rendering options and early two-player online co-op.

Original or reference: **Resident Evil: The Umbrella Chronicles (Wii)** · Static recompilation  
[Download and supply your own game files](https://github.com/solleo95/reuc-recomp/releases/tag/0.0.12) · [Browse RemakeList](https://remakelist.com/remakes/reuc-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=reuc-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · AVX2 · Vulkan 1.3

**Status:** 0.0.12 · early build · co-op experimental

**What you need:** Your own Wii NTSC-U disc image, game ID RBUE08. Extract it through the launcher’s bundled Wit or supply the extracted DATA folder. PAL RBUP08 and Japanese RBUJ08 are unsupported. Optional proprietary runtimes and texture packs retain separate terms.

**What is available:** 0.0.12 provides a Windows package with better aim boundaries and reload zones, a configurable speed-up key and fewer false co-op desync stops. Light-gun/Wii Remote aiming has only simulated-input tests. The underlying transient co-op divergence is unresolved; this update tolerates a single occurrence. It remains an early build tested mainly on one RTX 4080/Windows 11 PC; minimum performance is not established. Online co-op may fail to connect, desync or freeze; ray tracing covers shadows only. RemakeList has not built, installed or played this release.

**Code license:** [GPL-3.0 for project code; vendor DLSS/FidelityFX runtimes and other dependencies keep their own licenses. Capcom game code and assets are excluded.](https://github.com/solleo95/reuc-recomp/blob/main/LICENSE)  
**Author:** solleo95  
[Official documentation](https://github.com/solleo95/reuc-recomp/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

### [G-Diffuser 3DS](https://github.com/cruxxxxxx/gdx-3ds)

A native F-Zero X port for the 3DS family, with stereoscopic 3D, a bottom-screen dashboard and two-to-four-player races. Requires your own supported cartridge dump and a homebrew-capable console.

Original or reference: **F-Zero X (Nintendo 64)** · Decompilation-based project  
[Download and supply your own game files](https://github.com/cruxxxxxx/gdx-3ds/releases/tag/v1.1.0) · [Browse RemakeList](https://remakelist.com/remakes/g-diffuser-3ds/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=g-diffuser-3ds-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Old/New Nintendo 3DS and 2DS family · homebrew

**Status:** v1.1.0 · homebrew console · original cartridge required

**What you need:** Supply your own F-Zero X USA revision 0 cartridge dump, convert it on a computer to the two .o2r archives, and use your own console DSP firmware dump for audio. EK needs the supported retail Japanese 64DD dump; fan-translated disks are unsupported. No ROM, disk or pre-converted game assets are supplied.

**What is available:** v1.1.0 provides separate Old/New 3DS ZIPs, .3dsx and .cia files, plus optional EK builds and desktop asset extractors. Prepare the assets on a computer first; the extractor script requires a local source copy with the decomp submodule. v1.0.0 downloads were withdrawn. Use the build matching the console. Widescreen and the new track buffer were tested only in an emulator; multiplayer has not been tested on every console pairing. Old 3DS 3D multiplayer is capped at 30 fps, and its EK build has stutter, broken-up music and slow editors. Memory and audio issues remain; 60 fps is not guaranteed. The hosted online server is temporary.

**Code license:** [MIT covers original G-Diffuser and 3DS-port additions, unless a file says otherwise. Dependencies, decompiled Nintendo/N64 SDK code and game content have separate rights; the MIT license does not grant rights to those materials.](https://github.com/cruxxxxxx/gdx-3ds/blob/main/LICENSE)  
**Author:** cruxxxxxx  
[Official documentation](https://github.com/cruxxxxxx/gdx-3ds/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [Metroid Dread Recomp — Linux fork](https://github.com/DaniSald/Metroid-Dread-Recomp)

A Linux-focused fork of Metroid Dread Recomp that builds a native PC version from your own Switch 2.1.0 files. It offers a Linux AppImage alongside a Windows package.

Original or reference: **Metroid Dread (Nintendo Switch)** · Static recompilation  
[Build and supply your own game files](https://github.com/DaniSald/Metroid-Dread-Recomp/releases/tag/v0.4.0-linux.2) · [Browse RemakeList](https://remakelist.com/remakes/metroid-dread-recomp-linux/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=metroid-dread-recomp-linux-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / Linux x86-64 (glibc 2.38+, OpenGL 4.3) / Steam Deck

**Status:** v0.4.0-linux.2 · early preview · local compilation

**What you need:** Provide both ExeFS and RomFS from your own lawfully obtained Metroid Dread 2.1.0, with the update merged or supplied separately. RomFS alone is insufficient. No game code, data or keys are distributed.

**What is available:** v0.4.0-linux.2 provides a Linux x86-64 AppImage and Windows ZIP. The first launch checks your files and compiles locally; Linux needs about 7 GB free, glibc 2.38+, OpenGL 4.3, SDL2 and a folder-picker utility. Keep the Windows EXE beside its recompiler folder. Despite the release's non-prerelease flag, the author calls all 0.x builds early previews and warns of crashes and setup problems. Linux lacks native Vulkan, built-in release updates, mouse free aim and F7 recording. The reported Steam Deck OLED result was a nine-minute session, not a full-game or universal 60 fps guarantee.

**Code license:** [SwitchRecomp code is Apache-2.0; the README identifies the combined Windows executable with the ScarletNX renderer as GPL-3.0. Linux and bundled toolchain/libraries have their own notices. Nintendo game files and keys are excluded.](https://github.com/DaniSald/Metroid-Dread-Recomp/blob/main/README.md#licences)  
**Author:** DaniSald  
[Official documentation](https://github.com/DaniSald/Metroid-Dread-Recomp/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [Odin Sphere Leifthrasir PC](https://github.com/saulob/odin-sphere-leifthrasir-pc)

Runs your own supported PS4 Odin Sphere Leifthrasir package on Windows, with a launcher, rendering options and local trophies. Linux and Steam Deck downloads are experimental.

Original or reference: **Odin Sphere Leifthrasir (PlayStation 4)** · Platform compatibility layer  
[Download and supply your own game files](https://github.com/saulob/odin-sphere-leifthrasir-pc/releases/tag/v0.1.0) · [Browse RemakeList](https://remakelist.com/remakes/odin-sphere-leifthrasir-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=odin-sphere-leifthrasir-pc-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10 1903+/11 x64 / experimental Linux x86-64 and Steam Deck

**Status:** v0.1.0 · Windows release · experimental Linux

**What you need:** Supply a lawfully obtained decrypted PS4 package: USA CUSA05083 base 1.00, Japan CUSA01290 base 1.00 or its 1.02 update, or Europe CUSA05262 base 1.00 or its 1.01 update. Updates require their matching regional base. Console-encrypted or other builds are refused; no game files or keys are supplied.

**What is available:** v0.1.0 is the first public release, with a Windows x64 ZIP and experimental Linux x86-64 AppImage. Import your own decrypted supported PS4 .pkg in the launcher's Play page. Both routes need Vulkan 1.3 and the specified extensions, with about 4 GB disk space; Linux needs glibc 2.31+ and X11/Wayland. Only 16:9 Original preserves the intended shape: ultrawide ratios stretch gameplay rather than reveal more of the world, and other ratios squeeze it; HUD, menus and videos are not adjusted. Linux/Steam Deck builds passed scripted checks but have not been tested on real hardware. Downloads are unsigned; trophies are local, with no PSN or online play.

**Code license:** [GPL-2.0-or-later covers original project code. The shadPS4-derived renderer and other third-party components retain their notices; the original game and its assets are excluded.](https://github.com/saulob/odin-sphere-leifthrasir-pc/blob/main/LICENSE)  
**Author:** saulob  
[Official documentation](https://github.com/saulob/odin-sphere-leifthrasir-pc/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [Rogue Galaxy Recompiled](https://github.com/victor-takai/rogue-galaxy-recomp)

Builds a native Windows version of the USA PS2 Rogue Galaxy from your own disc, with widescreen, resolution scaling and gameplay options.

Original or reference: **Rogue Galaxy (PlayStation 2)** · Static recompilation  
[Build and supply your own game files](https://github.com/victor-takai/rogue-galaxy-recomp/releases/tag/v0.1.0) · [Browse RemakeList](https://remakelist.com/remakes/rogue-galaxy-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rogue-galaxy-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64

**Status:** v0.1.0 prerelease · Windows local build · USA disc only

**What you need:** Provide your own lawfully obtained Rogue Galaxy USA PS2 disc image, SCUS-97490. Other regional versions are unsupported. No game data, BIOS or disc-derived files are distributed; keep your generated game local.

**What is available:** v0.1.0 is a prerelease Windows installer ZIP. Run Install.bat with your own USA disc; it downloads about 300 MB of build tools and compiles locally. Allow around 16 GB disk and roughly 20–60 minutes depending on the computer. The download is not a ready-built complete game. The author reports title/opening, Salgin scenes and battles, not a complete playthrough. A rare hang after the Story loading screen remains, heavy scenes may fall to around 50 fps, and widescreen stretches menus and text. Antivirus may block the local compiler; no security guarantee is implied.

**Code license:** [GPL-3.0 covers the project, matching the linked PS2Recomp framework. Dependencies retain their own notices; original game data, BIOS and disc-derived files are not included or relicensed.](https://github.com/victor-takai/rogue-galaxy-recomp/blob/main/LICENSE)  
**Author:** victor-takai  
[Official documentation](https://github.com/victor-takai/rogue-galaxy-recomp/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [PaxDino](https://github.com/wootbeer/PaxDino)

A Turok: Rage Wars PC port with mouse aim, widescreen and up to four local players.

Original or reference: **Turok: Rage Wars (Nintendo 64)** · Static recompilation  
[Download and supply your own game files](https://github.com/wootbeer/PaxDino/releases/tag/v0.1.6) · [Browse RemakeList](https://remakelist.com/remakes/paxdino/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=paxdino-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 / experimental Linux x86_64 and Steam Deck

**Status:** v0.1.6 · Beta · original ROM required

**What you need:** Supply your own supported Turok: Rage Wars USA ROM; the README lists hashes for .n64 and .z64 and also accepts .v64. The co-op trial fix uses USA 1.0. Game data is not supplied.

**What is available:** v0.1.6 offers Windows and Linux archives. The project remains beta; Linux and Steam Deck are experimental. The launcher imports your own ROM. RemakeList has not installed or played it.

**Code license:** [GPL-3.0 applies to project code; original game content and third-party components retain separate rights and terms.](https://github.com/wootbeer/PaxDino/blob/main/COPYING)  
**Author:** wootbeer  
[Official documentation](https://github.com/wootbeer/PaxDino/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [KirbyRecomp](https://github.com/xtamqispeak/KirbyRecomp)

An experimental Super Kirby Clash port that builds locally from your own Switch files.

Original or reference: **Super Kirby Clash (Switch)** · Static recompilation  
[Build and supply your own game files](https://github.com/xtamqispeak/KirbyRecomp/releases/tag/v0.3.0-alpha) · [Browse RemakeList](https://remakelist.com/remakes/kirby-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=kirby-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · AVX2/FMA · Vulkan 1.3

**Status:** v0.3.0-alpha · local build

**What you need:** Supply matching Super Kirby Clash ExeFS/RomFS for title 01003FB00C5A8000. The tested main build ID starts c9649e053bd7be2751ef0b00e7c03f5d59695b94; other revisions are unverified. NSP/XCI import and decryption are not provided.

**What is available:** v0.3.0-alpha supplies a Windows setup EXE and source kit. It fixes shop/profile rendering and adds custom resolution and a 120 fps option. Setup translates and compiles your own matching ExeFS/RomFS locally; it does not include a precompiled game. Full battles and later stages remain unvalidated. Missing services or unsupported instructions can stop the runtime; no complete-game or online-purchase claim is established. Requires Windows x64, AVX2/FMA and the documented Vulkan-capable hardware.

**Code license:** [MIT applies to project code; original game content and third-party components retain separate rights and terms.](https://github.com/xtamqispeak/KirbyRecomp/blob/main/LICENSE)  
**Author:** xtamqispeak  
[Official documentation](https://github.com/xtamqispeak/KirbyRecomp/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [1080° Snowboarding: Recompiled](https://github.com/thebradshaw/1080-Snowboarding-decomp)

A PC port of 1080° Snowboarding with widescreen, optional higher frame rates and longer draw distance.

Original or reference: **1080° Snowboarding (Nintendo 64)** · Static recompilation  
[Download and supply your own game files](https://github.com/thebradshaw/1080-Snowboarding-decomp/releases/tag/1.01) · [Browse RemakeList](https://remakelist.com/remakes/1080-snowboarding-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=1080-snowboarding-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 / experimental Linux x64

**Status:** 1.01 · Windows / experimental Linux

**What you need:** Supply an unmodified USA .z64 ROM with MD5 fa27089c425dbab99f19245c5c997613. No ROM is supplied. Optional board redraws and launcher artwork derive from the original game and are outside the code license.

**What is available:** 1.01 provides Windows x64 and experimental Linux x64 packages. It fixes the flickering dark bar in the Mountain Village cave and adds VSync control. Existing 1.0 saves and settings carry over; your supported US .z64 ROM is still required. Linux is experimental and not hardware-tested. RetroAchievements submission is awaiting approval; unlocks remain local.

**Code license:** [GPL-3.0 applies to project code; original game content and third-party components retain separate rights and terms.](https://github.com/thebradshaw/1080-Snowboarding-decomp/blob/main/LICENSE)  
**Author:** thebradshaw  
[Official documentation](https://github.com/thebradshaw/1080-Snowboarding-decomp/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [Mission: Impossible — PC Recomp](https://github.com/nickallevato/mi_n64_exe)

A Linux port of the N64 Mission: Impossible with mouse aim, widescreen and a modern analog camera.

Original or reference: **Mission: Impossible (Nintendo 64)** · Static recompilation  
[Download and supply your own game files](https://github.com/nickallevato/mi_n64_exe/releases/tag/v0.1.0) · [Browse RemakeList](https://remakelist.com/remakes/mi-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mi-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Linux x86_64 · glibc 2.35+ · Vulkan

**Status:** v0.1.0 · Linux release · full playthrough unverified

**What you need:** Supply your own USA .z64 ROM with SHA-1 7546d5df1fc93fed8205a066f1333fd7dd50c1e1. No ROM or original assets are supplied.

**What is available:** v0.1.0 offers Linux x64 AppImage and tar.gz builds based on Ubuntu 22.04; Vulkan and glibc 2.35+ are required. The author reports all 20 levels load and play but has not verified full playthroughs. There is no Windows or macOS package. RemakeList has not installed or played it. The 60 FPS option is not a performance guarantee for every device.

**Code license:** [GPL-3.0 applies to project code; original game content and third-party components retain separate rights and terms.](https://github.com/nickallevato/mi_n64_exe/blob/main/COPYING)  
**Author:** nickallevato  
[Official documentation](https://github.com/nickallevato/mi_n64_exe/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [Ascension](https://github.com/arnaldolima1/gow-ascension-pc)

An experimental Windows port built from your own European PS3 God of War: Ascension disc. The author reports reaching the first level and first boss, not a complete playthrough.

Original or reference: **God of War: Ascension (PS3)** · Static recompilation  
[Build and supply your own game files](https://github.com/arnaldolima1/gow-ascension-pc/blob/main/docs/README.en.md#building) · [Browse RemakeList](https://remakelist.com/remakes/god-of-war-ascension-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=god-of-war-ascension-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · manual source build

**Status:** Source build · early gameplay experiment

**What you need:** Supply your own lawfully obtained European BCES-01741 version 1.00 disc data, including a locally prepared EBOOT.ELF and any required personal keys. Optional Brazilian Portuguese content is built from your own US disc. No game files or keys are supplied.

**What is available:** No release package is published. Build manually with Visual Studio 2022, CMake, Ninja, Vulkan SDK, patched ps3recomp and a local .env; the author estimates 20–40 minutes and 16 GB RAM. Windows is the documented tested route; macOS is paused. Low performance, rendering duplication and SPU-job stalls remain, and later levels are not established as playable. RemakeList has not built or played it.

**Code license:** [MIT covers this repository’s code. The author states that builds using RPCS3’s RSX renderer are GPL-2.0; original game code and assets retain their owners’ rights.](https://github.com/arnaldolima1/gow-ascension-pc/blob/main/LICENSE)  
**Author:** arnaldolima1  
[Official documentation](https://github.com/arnaldolima1/gow-ascension-pc/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [LostWorldNative](https://github.com/snicolast/LostWorldNative)

A Windows source-built port of the 1997 arcade light-gun game, with widescreen, modern rendering and mouse or controller aiming. Requires the exact supported Japanese ROM set.

Original or reference: **The Lost World: Jurassic Park (arcade)** · Static recompilation  
[Build and supply your own game files](https://github.com/snicolast/LostWorldNative/blob/master/README.md#install) · [Browse RemakeList](https://remakelist.com/remakes/lost-world-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=lost-world-native-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · Vulkan 1.3 · local build

**Status:** Source build · original arcade ROM required

**What you need:** Supply your own lawfully obtained lostwsga.zip, the Japan Rev. A set for Sega Model 3 Step 1.5, including the specified ROM files. Other revisions are unsupported; the original game data is not supplied.

**What is available:** No release binary is published. The documented Windows route runs build.bat with your ROM, Python 3 and Visual Studio 2022 C++ build tools; the first build downloads dependencies. Author screenshots show the port, but full-game/device coverage and high-refresh performance are not independently verified. Optional graphics features depend on the GPU. RemakeList has not built or played it.

**Code license:** [MIT covers the repository’s authored code. Third-party libraries and fonts retain their own licenses; the original arcade game’s ROM, code and data retain their owners’ rights.](https://github.com/snicolast/LostWorldNative/blob/master/LICENSE)  
**Author:** snicolast  
[Official documentation](https://github.com/snicolast/LostWorldNative/blob/master/README.md) · Sources reviewed: 2026-10-28

</details>

### [HarmonyRecomp](https://github.com/Wrexxial/HarmonyRecomp)

A Windows port built from your own XBLA Harmony of Despair package, with graphics settings and up to six-player co-op over LAN or virtual LAN.

Original or reference: **Castlevania: Harmony of Despair (Xbox 360)** · Static recompilation  
[Build and supply your own game files](https://github.com/Wrexxial/HarmonyRecomp/releases/tag/v0.3.5) · [Browse RemakeList](https://remakelist.com/remakes/harmony-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=harmony-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · local build

**Status:** v0.3.5 · Windows local build

**What you need:** Supply your own Xbox 360 XBLA 58410A7A package. Optional DLC requires your own content packages and Title Update 2 (game 2.04); the current setup skips DLC without the update. Generated game code and extracted assets must not be redistributed.

**What is available:** v0.3.5 provides a Windows setup EXE and supporting toolchain archives for local compilation from your own XBLA package (about 10–30 minutes and 10 GB temporary space). It fixes the online-results crash; leaderboards remain empty because no server exists. The exit crash was fixed in v0.3.3. Optional DLC requires your own packages and Title Update 2; the current setup skips DLC without that update. Not every DLC stage has been played. Co-op needs matching releases/game versions over LAN or virtual LAN, not Xbox Live. RemakeList has not built or played it.

**Code license:** [The project code is BSD-3-Clause; the extractor includes MIT-licensed NocturneRecomp code. Runtime dependencies retain their terms, and original game code/data are outside these grants.](https://github.com/Wrexxial/HarmonyRecomp/blob/main/LICENSE)  
**Author:** Wrexxial  
[Official documentation](https://github.com/Wrexxial/HarmonyRecomp/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

### [Underground 2 Android Evolved](https://github.com/codepdbh/nfsu2-recompiled)

A native Android adaptation of the PC Underground 2, with touch controls and configurable graphics. Requires files from your own supported PC copy.

Original or reference: **Need for Speed: Underground 2 (PC)** · Static recompilation  
[Download and supply your own game files](https://github.com/codepdbh/nfsu2-recompiled/releases/tag/v0.14.11) · [Browse RemakeList](https://remakelist.com/remakes/nfsu2-android-evolved/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nfsu2-android-evolved-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Android 10+ (ARM64 / ARMv7), Vulkan 1.1+; Windows x86 source build

**Status:** v0.14.11 Android APKs · Windows source build

**What you need:** Use your own supported PC installation and the exact supported SPEED2.EXE (4,800,512 bytes), then import its game data. Other executables or editions may not match the recompiler.

**What is available:** v0.14.11 provides ARM64 and ARMv7 APKs with published checksums. Its notes describe minor fixes and explicitly no performance or gameplay change. Windows is a documented source-build target, not a Windows binary in this release. Device and driver compatibility varies. Windows requires a local compiler/toolchain build. The README download section still names v0.14.9; the checked release is v0.14.11.

**Source available; license restrictions apply:** [The README declares MIT for the author’s original tooling. No standalone project license was verified. This statement does not license the original executable, game code or assets.](https://github.com/codepdbh/nfsu2-recompiled/blob/main/README.md)  
**Author:** codepdbh  
[Official documentation](https://github.com/codepdbh/nfsu2-recompiled/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [LASRecomp Android](https://github.com/mamcjr/LASRecompAndroid)

An Android fork of LASRecomp with mobile controls and on-device compilation. Requires files from your own supported Switch Link’s Awakening copy.

Original or reference: **The Legend of Zelda: Link’s Awakening (Switch)** · Static recompilation  
[Build and supply your own game files](https://github.com/mamcjr/LASRecompAndroid/releases/tag/v0.5.7) · [Browse RemakeList](https://remakelist.com/remakes/las-recomp-android/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=las-recomp-android-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Android 11+ ARM64; compatible Vulkan GPU/driver

**Status:** v0.5.7 prerelease · Android · on-device build

**What you need:** Supply your own Switch Link’s Awakening 1.0.0, 1.0.1 or 1.1.0 ExeFS and RomFS. Keep the game executable and data versions compatible.

**What is available:** v0.5.7 is a prerelease APK for ARM64 Android 11+. Setup needs roughly 12 GB free and compiles on the phone. Vulkan 1.1/1.2 fallback paths exist, with device-dependent results. Validation is mainly on a POCO F7 Ultra with Snapdragon 8 Elite/Adreno 830. Good Adreno results can require Turnip; forced fallback tests do not establish real Mali support. v0.5.7 was not tested on a real Mali device.

**Code license:** [The Android port and upstream project code have scoped MIT notices. Third-party components retain their licenses; original Nintendo data and generated game code are outside that grant.](https://github.com/mamcjr/LASRecompAndroid/blob/main/LICENSE)  
**Author:** mamcjr  
[Official documentation](https://github.com/mamcjr/LASRecompAndroid/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [Project Stonehenge](https://github.com/Onaga00/ProjectStonehenge)

A native Windows reconstruction of Ace Combat 04 with modern display settings. Requires your own USA PS2 game disc image.

Original or reference: **Ace Combat 04: Shattered Skies (PS2)** · Decompilation-based project  
[Download and supply your own game files](https://github.com/Onaga00/ProjectStonehenge/releases/tag/Beta) · [Browse RemakeList](https://remakelist.com/remakes/project-stonehenge/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=project-stonehenge-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64; Vulkan 1.2

**Status:** 0.9.6 package · Beta release tag · Windows

**What you need:** Provide your own USA PS2 disc SLUS-20152 as a standard ISO9660 image with 2048-byte sectors. Raw BIN/CUE images are unsupported.

**What is available:** The release tag is Beta and its attached Windows package is version 0.9.6. The author reports a playable full campaign; this remains a beta release. Beta compatibility and high-frame-rate results are author claims, not a guarantee for every system. A GitHub non-prerelease flag does not make this a final release.

**Code license:** [Project code is GPL-3.0. The license does not cover original game assets, trademarks or disc data; dependencies retain their own terms.](https://github.com/Onaga00/ProjectStonehenge/blob/main/LICENSE)  
**Author:** Onaga00  
[Official documentation](https://github.com/Onaga00/ProjectStonehenge/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [Project 8 Plus](https://github.com/MaxLeiter/project-8-plus)

A native desktop adaptation of Tony Hawk’s Project 8 with modern graphics and mod tools. Requires your own supported PS3 game and update files.

Original or reference: **Tony Hawk’s Project 8 (PS3)** · Static recompilation  
[Build and supply your own game files](https://github.com/MaxLeiter/project-8-plus/releases/tag/v0.9.2) · [Browse RemakeList](https://remakelist.com/remakes/project-8-plus/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=project-8-plus-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64, Direct3D 12; experimental Linux x86_64

**Status:** v0.9.2 · Windows · Linux experimental

**What you need:** Provide your own USA PS3 BLUS30011 game folder with update 01.02 and the documented RPCS3 preparation. The optional HD package does not supply original game textures.

**What is available:** v0.9.2 offers a Windows setup package, experimental Linux archive and optional HD-model/tool package. Windows setup needs internet and roughly 4 GB, with an author estimate of 20–25 minutes. Linux remains experimental. Existing installs must rebuild to adopt v0.9.2’s shared-save change. Optional upscaling needs local processing and does not imply a verified universal visual/performance improvement.

**Code license:** [Project code is MIT; the optional upscaling model is CC-BY-4.0 and dependencies have their own notices. Original game content is excluded.](https://github.com/MaxLeiter/project-8-plus/blob/master/LICENSE)  
**Author:** MaxLeiter  
[Official documentation](https://github.com/MaxLeiter/project-8-plus/blob/master/README.md) · Sources reviewed: 2026-10-28

</details>

### [2014 FIFA World Cup Brazil: Recompiled](https://github.com/HossEz/fifa-world-cup-2014-recompiled)

An unofficial Windows port of the Xbox 360 football game, with a launcher that imports your own disc image or extracted game folder.

Original or reference: **2014 FIFA World Cup Brazil** · Static recompilation  
[Download and supply your own game files](https://github.com/HossEz/fifa-world-cup-2014-recompiled/releases/tag/v0.1.10) · [Browse RemakeList](https://remakelist.com/remakes/fifa-world-cup-2014-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fifa-world-cup-2014-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · Direct3D 12 · SSE4.2

**Status:** v0.1.10 - Preview - original assets required

**What you need:** Provide your own Xbox 360 copy as an ISO or a folder containing default.xex. No game data is provided by the project.

**What is available:** v0.1.10 has a Windows installer and portable ZIP; the launcher verifies the supplied game. CPU and GPU requirements still apply. Intel UHD and Iris Xe use a slower renderer, and high-resolution cutscenes, replays and celebrations can fall below 60 fps. These are author reports, not independent full-game testing.

**Code license:** [BSD-3-Clause covers the author's launcher, fixes, SDK patches and tools. It excludes the original game and recompiled game code; dependencies retain their own licenses.](https://github.com/HossEz/fifa-world-cup-2014-recompiled/blob/main/LICENSE)  
**Author:** HossEz  
[Official documentation](https://github.com/HossEz/fifa-world-cup-2014-recompiled/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [Smash 4 PC](https://github.com/josiahg2502-glitch/Smash4PC)

A native Windows port of Super Smash Bros. for Wii U, with a launcher for your own game, update and optional DLC files.

Original or reference: **Super Smash Bros. for Wii U** · Static recompilation  
[Download and supply your own game files](https://github.com/josiahg2502-glitch/Smash4PC/releases/tag/v0.1.1) · [Browse RemakeList](https://remakelist.com/remakes/smash4pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=smash4pc-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · Vulkan 1.3

**Status:** v0.1.1 · early port · streaming netplay beta

**What you need:** Supply your own USA Wii U game dump; v304 is recommended, and DLC must come from your own dump. Pretendo additionally requires your own Wii U console files and account.

**What is available:** v0.1.1 supplies a Windows ZIP with older-CPU support and input/stutter fixes. Its new beta netplay rooms stream one host’s game to up to seven guests at 1080p/60, with guest input returned to the host. This is remote-play streaming, not eight synchronized native game instances. The new streaming path was tested on one PC, not between separate homes; restrictive networks may prevent direct connections. Original US Wii U game files are required by the host. High display rates use interpolation; repository-generated game code has separate rights. RemakeList has not tested it.

**Code license:** [Project-authored code is MIT; Cemu-derived network code is MPL-2.0 and other components retain their notices. None of these licenses grants rights to Nintendo game code or assets.](https://github.com/josiahg2502-glitch/Smash4PC/blob/main/LICENSE)  
**Author:** josiahg2502-glitch  
[Official documentation](https://github.com/josiahg2502-glitch/Smash4PC/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [Glassline](https://github.com/MoonCellar-Team/Glassline)

Brings the iPad version of Mirror's Edge to desktop, Android and browsers, with modern controls and optional one-on-one network play.

Original or reference: **Mirror's Edge for iPad** · Decompilation-based project  
[Download and supply your own game files](https://github.com/MoonCellar-Team/Glassline/releases/tag/v1.4.1) · [Browse RemakeList](https://remakelist.com/remakes/glassline/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=glassline-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 · Linux x64 / Steam Deck · Android 9+ · Web

**Status:** v1.4.1 · desktop, Android and browser

**What you need:** Provide your own Mirror's Edge iPad IPA, version 1.1.48 or newer; the iPhone version is unsupported. The project does not supply original game data.

**What is available:** v1.4.1 supplies Windows, Linux, Android and web packages, fixing touch/balance controls and a browser-launch crash. Requires your own Mirror’s Edge iPad IPA 1.1.48+; the iPhone game is unsupported. Online one-on-one and accounts use MoonCellar services, not EA; the friends-only leaderboard remains empty. No native macOS package exists. Browser storage clearing deletes local game files/saves, and enhanced effects require OpenGL ES 3.0. Source-available terms restrict redistribution and commercial use.

**Source available; license restrictions apply:** [The custom license permits specified personal noncommercial use of the author's work. Redistribution, modified builds and commercial use need separate permission. EA's original code and assets are excluded; dependencies retain their licenses.](https://github.com/MoonCellar-Team/Glassline/blob/main/LICENSE)  
**Author:** MoonCellar-Team  
[Official documentation](https://github.com/MoonCellar-Team/Glassline/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

### [RE: Outbreak](https://github.com/Ninjacornix/reo)

A Windows port of Resident Evil Outbreak with guided local compilation, configurable controls and optional openSNAP co-op. File #1 has a stable release; File #2 is an experimental release-candidate route.

Original or reference: **Resident Evil Outbreak File #1** · Static recompilation  
[Build and supply your own game files](https://github.com/Ninjacornix/reo/releases/tag/v1.0.20-rc0) · [Browse RemakeList](https://remakelist.com/remakes/reo-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=reo-native-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 · .NET 8 Desktop Runtime · Vulkan

**Status:** v1.0.20-rc0 · release candidate · experimental File #2

**What you need:** v1.0.20-rc0 accepts your own File #1 NTSC-U v2.00 ISO (SLUS-20765) or experimental File #2 NTSC-U v1.05 (SLUS-20984). The stable v1.0.19 supports File #1 only. Keep the ISO and the release’s build-inputs ZIPs for local compilation. PAL, Japanese, modified or other revisions are unsupported; no game data or PS2 BIOS is supplied.

**What is available:** v1.0.20-rc0 is a release candidate with a portable Windows launcher, bundled .NET runtime and automatic compiler setup. It builds locally from your File #1 NTSC-U v2.00 or experimental File #2 NTSC-U v1.05 disc. v1.0.19 remains the stable File #1 release. RC0 automatically copies prior launcher data, caches, settings and saves when using a new data folder. Back up saves and follow the release’s clean-install guidance before opening a fresh extract. File #2 is experimental; RC support is not a stable-version claim.

**Code license:** [This fork's original contributions use GPL-3.0-only. Upstream and third-party code retains its own notices. Original game content and generated game code are not licensed by this grant.](https://github.com/Ninjacornix/reo/blob/main/LICENSE)  
**Author:** Ninjacornix  
[Official documentation](https://github.com/Ninjacornix/reo/blob/main/README.md) · Sources reviewed: 2026-10-29

</details>

### [SegaSonic Native Port](https://github.com/cheviman/segasonic-port)

A native port of Sega's three-player arcade game with desktop and handheld routes, using your own exact arcade ROM set.

Original or reference: **SegaSonic The Hedgehog (arcade)** · Decompilation-based project  
[Download and supply your own game files](https://github.com/cheviman/segasonic-port/releases/tag/v1.3.0) · [Browse RemakeList](https://remakelist.com/remakes/segasonic-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=segasonic-port-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows x64 · Linux x64 · macOS 11+ · Anbernic H700 · Android/Switch generated locally

**Status:** v1.3.0 · local asset import

**What you need:** Provide sonic.zip for SegaSonic The Hedgehog, Japan revision C, with all 18 expected files. Import creates segasonic.assets; generated mobile or console packages include your extracted assets and must not be shared.

**What is available:** v1.3.0 supplies Windows, Linux, macOS and Anbernic packages with new trackball settings and controller mapping. Provide your own sonic.zip (Japan rev. C, 18 files), or import your extracted segasonic.assets. Android 7+ APK and Switch NSP are generated locally; Switch generation also needs your own keys. These personal packages contain original assets and must not be shared. Multiplayer is local for up to three players. macOS builds are unsigned; author comparisons with MAME are not RemakeList gameplay tests.

**Code license:** [Project code uses BSD-3-Clause; MAME/ymfm-derived components, SDL and Kenney assets have their own BSD, zlib or CC0 terms. Original Sega ROMs and assets are not licensed by the project.](https://github.com/cheviman/segasonic-port/blob/main/LICENSE)  
**Author:** cheviman  
[Official documentation](https://github.com/cheviman/segasonic-port/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

### [Stunt Race FX DECOMP](https://github.com/Mabec-games/Stunt-Race-FX-DECOMP)

An experimental Linux port of the SNES Super FX racer, preserving the original game logic while drawing smoother, higher-resolution frames.

Original or reference: **Stunt Race FX** · Decompilation-based project  
[Download and supply your own game files](https://github.com/Mabec-games/Stunt-Race-FX-DECOMP/releases/tag/beta-0.1) · [Browse RemakeList](https://remakelist.com/remakes/stunt-race-fx-decomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=stunt-race-fx-decomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Linux x86-64

**Status:** beta-0.1 - Preview - original assets required

**What you need:** Supply your own Stunt Race FX USA revision 1 ROM matching SHA-1 781e376ff453a83c7bcf72339abe6b842efd9c86. The port does not include game data.

**What is available:** beta-0.1 provides a Linux x86-64 AppImage. The README's statement that an AppImage will be published later is stale; the release attachment is present. Source building is also documented. Early beta: Speed Trax, especially novice courses, has the most coverage. Other courses and modes remain incomplete; menus, car selection and two-player battle retain original resolution without interpolation. A smooth 60-fps picture does not change the original simulation rate.

**Code license:** [The upstream decompilation and this fork are offered under CC0-1.0. Nintendo/Argonaut's original game and ROM contents remain separately protected and are not supplied.](https://github.com/Mabec-games/Stunt-Race-FX-DECOMP/blob/main/LICENSE)  
**Author:** Mabec-games  
[Official documentation](https://github.com/Mabec-games/Stunt-Race-FX-DECOMP/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [2010 FIFA World Cup South Africa: Recompiled](https://github.com/CalinGraphics/fifa-world-cup-2010-recompiled)

A Windows port of the Xbox 360 World Cup football game, currently available through a documented local source-build route using your own supported disc.

Original or reference: **2010 FIFA World Cup South Africa** · Static recompilation  
[Build and supply your own game files](https://github.com/CalinGraphics/fifa-world-cup-2010-recompiled/blob/main/README.md) · [Browse RemakeList](https://remakelist.com/remakes/fifa-world-cup-2010-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fifa-world-cup-2010-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · Direct3D 12 · SSE4.2

**Status:** Early - local build and original assets required

**What you need:** Supply the exact Europe Xbox 360 edition with English, Spanish and Dutch, matching both default.xex and fifadllzf.xex hashes. PS3 and other regions are unsupported.

**What is available:** No GitHub releases were present on 28 October 2026 despite the README's download button. Use BUILDING.md and build.ps1; the initial SDK and game build can take about an hour according to the author. Online/Xbox Live does not work. Menus and cutscenes stay at 30 fps, and not every mode has been tested end to end by the author. The located image is the author's launcher screenshot, not gameplay proof.

**Code license:** [BSD-3-Clause covers the author's launcher, app, hooks, SDK patches and tools. Original and recompiled game code are excluded, and third-party components keep their licenses.](https://github.com/CalinGraphics/fifa-world-cup-2010-recompiled/blob/main/LICENSE)  
**Author:** CalinGraphics  
[Official documentation](https://github.com/CalinGraphics/fifa-world-cup-2010-recompiled/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [BotW Recompiled for Windows](https://github.com/ryderclanky/BotW-Native)

An early Windows port of Wii U Breath of the Wild, translating the game locally and rendering through a Vulkan backend.

Original or reference: **The Legend of Zelda: Breath of the Wild (Wii U)** · Static recompilation  
[Build and supply your own game files](https://github.com/ryderclanky/BotW-Native/releases/tag/v0.1.1) · [Browse RemakeList](https://remakelist.com/remakes/botw-native-windows/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=botw-native-windows-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · Vulkan 1.1 · local compilation

**Status:** v0.1.1 - Early - local build and original assets required

**What you need:** Provide your own already-extracted Wii U USA game with update v208 (1.5.0), including code, content and meta directories and the supported U-King.rpx hash. No keys or game files are supplied.

**What is available:** v0.1.1 provides a Windows ZIP with launcher and source. The launcher builds locally from your supplied game; source builds use MSYS2 UCRT64. This is not a full-game release. The author checked only listed opening, combat, map, travel and Hateno scenes on a recent NVIDIA laptop. Controller mapping, effects, cutscene text, DLC and long sessions remain incomplete or unverified. The README contradicts itself on audio, so working sound is not confirmed. This fork's Linux and Apple playability is not established.

**Code license:** [Project-authored code is MIT; Cemu-derived components stay MPL-2.0, with other dependencies under their own licenses. Nintendo's original game, assets and extracted files are excluded.](https://github.com/ryderclanky/BotW-Native/blob/main/LICENSE)  
**Author:** ryderclanky  
[Official documentation](https://github.com/ryderclanky/BotW-Native/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [358/2 Days for Android](https://github.com/sonofskywalker3/khdays-358-android)

An Android fork of Yokimitsuro's native Kingdom Hearts 358/2 Days port, with a two-screen layout for AYN Thor and a shared display on phones.

Original or reference: **Kingdom Hearts 358/2 Days** · Decompilation-based project  
[Download and supply your own game files](https://github.com/sonofskywalker3/khdays-358-android/releases/tag/android-0.1.4-beta8) · [Browse RemakeList](https://remakelist.com/remakes/khdays-358-android/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=khdays-358-android-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Android 10+ · ARM64 · Vulkan · AYN Thor dual-screen support

**Status:** android-0.1.4-beta8 · Mali experimental

**What you need:** Supply your own European or North American DS cartridge ROM. Optional HD videos and menus require your own HD 1.5+2.5 ReMIX and, for menus, HD 2.8 copies; these are not supplied.

**What is available:** android-0.1.4-beta8 provides an Android APK, fixing Mission Mode panel crashes and lower-screen layouts. Mali GPU support is experimental and untested on Mali hardware; busy 3D scenes remain slow on the older AYN Odin. Requires Android 10+, ARM64/Vulkan and your own European or North American DS ROM. The accompanying Windows EXE prepares optional HD content from your own HD collections; it is not an Android build. Custom HD/mod folders need All files access. Export saves before uninstalling, which deletes local app data. Full-game claims are the author’s, not RemakeList tests.

**Code license:** [Project code uses MIT with upstream and third-party notices retained. This does not grant rights to Square Enix/Disney game files or optional HD collection assets.](https://github.com/sonofskywalker3/khdays-358-android/blob/master/LICENSE)  
**Author:** sonofskywalker3  
[Official documentation](https://github.com/sonofskywalker3/khdays-358-android/blob/master/.github/README.md) · Sources reviewed: 2026-10-30

</details>

### [F.E.A.R. 360 Recompiled](https://github.com/Juansolo457/fear360-recomp)

A source-build native port of the Xbox 360 F.E.A.R. and F.E.A.R. Files for Linux and Steam Deck, with a collection menu and display-paced frame-rate controls.

Original or reference: **F.E.A.R. / F.E.A.R. Files (Xbox 360)** · Static recompilation  
[Build and supply your own game files](https://github.com/Juansolo457/fear360-recomp/blob/master/docs/SETUP.md) · [Browse RemakeList](https://remakelist.com/remakes/fear360-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fear360-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Current source: native Linux x86-64 / Steam Deck · AVX2/FMA · Vulkan 1.3; stable v0.1.5: Windows Direct3D 12 / Proton

**Status:** Source build · stable v0.1.5 / native Linux development line 0.9

**What you need:** Provide your own supported Xbox 360 discs: F.E.A.R. Title ID 565507D9 and F.E.A.R. Files 565507E8, matching the executable SHA-256 values in SETUP.md. Generated executables and the local Steam Deck package include disc-derived code/data; keep them private. No original assets or ready-made game package is supplied.

**What is available:** GitHub’s latest stable release endpoint still returns v0.1.5, a Windows source release with a Proton route for Steam Deck and no executable assets. Separately, the current default-branch documentation calls its development line 0.9 and provides native Linux/Steam Deck Vulkan builds without Proton, with author gameplay and performance test reports. We verified the build instructions, not a v0.9.0 release tag. Current-source Windows builds are untested. Full campaign playthroughs remain a v1.0 testing goal; RemakeList has not built or played either route. Rendering is currently 1280×720 and the PC texture pack is unsupported. Slow-motion firefights can miss 120 fps; Steam Deck blood marks are missing and story autosaves can briefly disconnect the controller. Docked 120 Hz, the Holiday bonus mission and complete campaigns still need validation. Windows builds from the documented 0.9 development line are untested; Android and Windows ARM64 remain future work. Original files / setup: Provide your own supported Xbox 360 discs: F.E.A.R. Title ID 565507D9 and F.E.A.R. Files 565507E8, matching the executable SHA-256 values in SETUP.md. Generated executables and the local Steam Deck package include disc-derived code/data; keep them private. No original assets or ready-made game package is supplied.

**Code license:** [Own tools and glue are MIT, fear-nx-derived runtime parts are GPL-3.0-or-later, and renderer/SDK components have MIT/BSD terms. Linked builds include GPL obligations. Original game code, assets and generated private builds must not be redistributed as project downloads.](https://github.com/Juansolo457/fear360-recomp/blob/master/LICENSE)  
**Author:** Juansolo457  
[Official documentation](https://github.com/Juansolo457/fear360-recomp/blob/master/README.md) · Sources reviewed: 2026-10-30

</details>

### [ReStreet](https://github.com/samuelit0davila/fifa-street-pc-port)

A Windows recompilation of FIFA Street (2012), with a launcher, local career play and optional community-server online play using your own Xbox 360 game.

Original or reference: **FIFA Street (2012)** · Static recompilation  
[Download and supply your own game files](https://github.com/samuelit0davila/fifa-street-pc-port/releases/tag/v2.1.3-online-beta) · [Browse RemakeList](https://remakelist.com/remakes/restreet-fifa-street/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=restreet-fifa-street-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · Linux launcher with Proton (beta)

**Status:** v2.1.3-online-beta - Preview - original assets required

**What you need:** Provide your own FIFA Street (2012) Xbox 360 ISO. Original game files are not supplied as a separate data download; the author states the installer includes generated game binaries.

**What is available:** v2.1.3-online-beta provides a Windows installer and native Linux launcher; the Linux game runs through Proton. The README's 2.0.8 version is stale. Windows adds World Tour save restoration; that feature is not yet in the Linux launcher. Online beta: rooms and invites on Linux remain under test, and Steam Deck has not been tested by the author. Vulkan may stutter or crash on AMD; internal rendering is currently 1280×720. Community servers have separate service conditions. If a World Tour career disappears, stop playing before restoring an older save because only the last ten saves are kept. Distribution rights for generated game binaries are not claimed.

**Code license:** [MIT covers the author's installer, launcher and scripts only; dependencies keep their licenses. The installer contains generated game binaries, and the author explicitly says MIT does not establish redistribution rights or legal clearance for them.](https://github.com/samuelit0davila/fifa-street-pc-port/blob/main/LICENSE)  
**Author:** samuelit0davila  
[Official documentation](https://github.com/samuelit0davila/fifa-street-pc-port/blob/main/README.md) · Sources reviewed: 2026-10-28

</details>

### [NX2Apple](https://github.com/LNPANDY/NX2Apple)

A Mac game-library launcher and graphical build tool for nxnative, preparing personal Mac or iPhone/iPad apps from your own supported Switch files. This is a separate community fork, not a bundled game collection.

Original or reference: **Nintendo Switch game builds and library management on Apple devices** · Platform compatibility layer  
[Build and supply your own game files](https://github.com/LNPANDY/NX2Apple/releases/tag/v0.7.1) · [Browse RemakeList](https://remakelist.com/remakes/nx2apple/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nx2apple-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Build tool: Apple silicon Mac, macOS 13+ · targets: Mac / iPhone / iPad

**Status:** v0.7.1 · guided local build tool

**What you need:** Supply your own Switch game dumps, required updates/DLC and prod.keys. The launcher opens on Apple silicon macOS 13+; NVN game builds need Xcode 27.1 on macOS 26.6+ unless using the documented alternate-Metal override. The app bundles Python/build tools and installs .NET SDK 10. iPhone builds target iOS 26+; older devices are untested. Game-derived code and assets must not be redistributed.

**What is available:** v0.7.1 supplies the Apple silicon Mac builder. Console mode now starts games fullscreen on the launcher’s display, build failures offer recovery actions and selected DLC is carried into slim iOS builds. v0.7.0 also adds Mac/iPhone save syncing through an iCloud Drive folder. Game changes require rebuilding from your own dumps. It supplies a builder, not ready-to-play game apps. Profiles do not establish complete compatibility; real mods remain untested. Windows has no verified release pipeline. Large games depend on device memory and signing entitlements; free Apple-ID signing expires after seven days. RemakeList has not built, installed or played this release.

**Code license:** [MIT covers project code, with upstream attribution and separate third-party notices. It grants no rights to Nintendo game code, assets, keys or the game-derived packages you build.](https://github.com/LNPANDY/NX2Apple/blob/main/LICENSE)  
**Author:** LNPANDY and contributors  
[Official documentation](https://github.com/LNPANDY/NX2Apple/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

### [NHL 2K8 Recompiled](https://github.com/anishchandra24/NHL2K8-Recompiled)

An unofficial Windows port of the Xbox 360 hockey game, rebuilt locally from your own NHL 2K8 files, with local multiplayer and custom soundtracks.

Original or reference: **NHL 2K8** · Static recompilation  
[Build and supply your own game files](https://github.com/anishchandra24/NHL2K8-Recompiled/releases/tag/v1.1.0) · [Browse RemakeList](https://remakelist.com/remakes/nhl2k8-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nhl2k8-recompiled-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 · Direct3D 12 · local build; Windows 11 untested

**Status:** v1.1.0 · local build · local multiplayer · online unavailable

**What you need:** Supply your own legally obtained Xbox 360 NHL 2K8, title ID 54540809, version 0.0.0.3, extracted with default.xex and all other files together. The README specifies the supported executable hash; other releases are unsupported. Keep additional space for these extracted files. No game data is supplied by RemakeList.

**What is available:** v1.1.0 offers a setup program that downloads tools and builds locally, plus a manual source-build route. Requires Windows 10/11 x64, Direct3D 12, Visual Studio 2022 C++ with Clang/CMake, Git, internet for setup and about 10 GB for the build, in addition to your own supported game files. Only Windows 10 has been tested by the author. Online features do not work; busy crowds and first shader encounters can stutter. The F4 settings screen’s Save to config button writes an unreadable configuration. RemakeList has not installed or played it; the author’s antivirus false-positive claim is not an independent security verification.

**Code license:** [GPL-3.0 covers the project-owned files only. ReXGlue/Xenia patches retain their BSD licenses. Original game files, generated game code, artwork and screenshots are excluded.](https://github.com/anishchandra24/NHL2K8-Recompiled/blob/main/LICENSE)  
**Author:** anishchandra24  
[Official documentation](https://github.com/anishchandra24/NHL2K8-Recompiled/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

### [Virtua Fighter 2 Recomp](https://github.com/mr-finster/vf2-recomp)

An unofficial desktop adaptation of Virtua Fighter 2, with higher-resolution rendering, widescreen support and experimental rollback online play using your own arcade ROM.

Original or reference: **Virtua Fighter 2** · Community port  
[Download and supply your own game files](https://github.com/mr-finster/vf2-recomp/releases/tag/v0.1.16) · [Browse RemakeList](https://remakelist.com/remakes/virtua-fighter-2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=virtua-fighter-2-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10/11 x64 / macOS 11+ Intel and Apple silicon / Linux x64 and ARM64 / Steam Deck

**Status:** v0.1.16 · desktop downloads · experimental rollback online play

**What you need:** Your own legally obtained MAME vf2 Version 2.1 ROM set, vf2.zip, is required. The project ships no ROMs or material generated from them. Online peers must use the same ROM set. Linux ARM64 instructions target Raspberry Pi 5 and Ubuntu 22.04, Debian 12 or Raspberry Pi OS Bookworm and later.

**What is available:** v0.1.16 provides Windows 10/11 x64, macOS 11+ Universal, Linux x64/Steam Deck and Linux ARM64 archives. Supply your own MAME vf2 Version 2.1 ROM set, vf2.zip. Mac and Windows builds are unsigned. Online play remains experimental and both players need matching ROMs and compatible releases; direct matches expose your IP to the opponent, while Hide my IP address uses a relay. Native Steam Deck setup must follow the Linux guide. RemakeList has not installed or played it.

**Code license:** [MIT for the project’s own code; MAME components retain BSD-3-Clause and other dependencies retain their terms. The author’s app icon and painted selection-screen sides use CC BY 4.0. SEGA game code and assets are not granted by these licenses.](https://github.com/mr-finster/vf2-recomp/blob/main/LICENSE)  
**Author:** mr-finster  
[Official documentation](https://github.com/mr-finster/vf2-recomp/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

### [FM4 Static Recomp](https://github.com/i2kiselev/fm4-static-recomp)

An unofficial Forza Motorsport 4 Windows port built locally from your own Xbox 360 disc, with Vulkan rendering, modern graphics controls and DLSS/FSR upscaling.

Original or reference: **Forza Motorsport 4** · Static recompilation  
[Build and supply your own game files](https://github.com/i2kiselev/fm4-static-recomp/releases/tag/v0.3.0) · [Browse RemakeList](https://remakelist.com/remakes/fm4-static-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fm4-static-recomp-en)

<details>
<summary>Requirements and screenshots</summary>

**Platforms:** Windows 10 version 2004+ x64 · Vulkan · local build

**Status:** v0.3.0 · experimental Windows local build · own Disc 1 required

**What you need:** Supply your own legally obtained Xbox 360 Forza Motorsport 4 Disc 1 version 1.0: PAL media ID 61D62D9F or USA 26FF1101, title ID 4D530910. Disc 1 Rev 1/1.1 is unsupported. Your own Disc 2 and DLC are optional and need around 5 GB extra space. The launcher builds the game locally; RemakeList supplies no game data.

**What is available:** Experimental v0.3.0 provides a free Windows launcher that builds the game from your own supported Disc 1 ISO or GOD data. Requires Windows 10 version 2004+ x64, a current Vulkan driver, initial internet access and roughly 10 GB of space. Setup downloads Microsoft build components after you accept their licenses; no prebuilt game is supplied. Only PAL/USA retail Disc 1 version 1.0 is supported; Rev 1/1.1 is not. Linux and racing-wheel support are planned, while Xbox LIVE and Kinect are unsupported. Upscaler shimmer remains a known issue. RemakeList has not installed or played it.

**Code license:** [BSD-3-Clause for this project’s source. Pinyon Shift-derived code retains its notices and dependencies keep their terms. The original game, assets, generated translation and resulting game executable are excluded and must not be redistributed.](https://github.com/i2kiselev/fm4-static-recomp/blob/main/LICENSE)  
**Author:** i2kiselev  
[Official documentation](https://github.com/i2kiselev/fm4-static-recomp/blob/main/README.md) · Sources reviewed: 2026-10-30

</details>

## About this list

This list is generated from published RemakeList records. Additions, changes and removals are reviewed on the website first, then synchronized to GitHub automatically. Project descriptions are maintained in one place. [Data and synchronization notes](docs/data.md)

Functional alternatives, recreations and ports describe different relationships. A code license does not license the original game's assets. Compatibility and performance statements come from the cited sources and do not imply testing by RemakeList. This repository provides no game files, keys or install packages. Some projects publish their source under restricted terms and are not open source.

Suggest a project or report a correction through an Issue. See the contribution guide for the sources to include; generated project records and README entries are updated through RemakeList. [Suggest a project](CONTRIBUTING.md)

Original list text is licensed under CC BY 4.0; generator scripts use MIT. Listed projects and third-party material retain their own licenses. See LICENSE and NOTICE.md.

[CC BY 4.0](LICENSE) · [MIT](scripts/LICENSE) · [NOTICE](NOTICE.md)
