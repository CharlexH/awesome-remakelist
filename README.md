# Awesome Remakes

Software recreations, classic game engines, native ports, and clearly labeled functional alternatives. Curated by [RemakeList](https://remakelist.com/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=intro-en).

**English** · [简体中文](README.zh-CN.md) · [Browse the directory](https://remakelist.com/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=directory-en) · [Suggest a project](https://github.com/CharlexH/awesome-remakes/issues/new?template=project.yml)

Find what a project recreates or replaces, where it runs, and what you need before getting started.

- **Want to try something?** Check the starting route: a browser demo, a download and a personal build are different commitments.
- **Looking for an old game?** Read the file requirement first. A free engine may need a specific original edition; demo data usually covers limited content.
- **Need more detail?** Project names link directly to official sources. The accompanying RemakeList pages add screenshots and setup context. Compatibility and feature statements come from the cited sources, not a claim that we installed or played every project.

## Contents

- [Creative tools](#creative)
- [Everyday tools and interface recreations](#everyday)
- [Classic game engines and recreations](#classic_games)
- [Ports and compatibility projects](#ports)

<a id="creative"></a>

## Creative tools

- **[Compositor](https://github.com/robbietilton/Compositor)** — Adobe Photoshop · Functional alternative. Layer compositing and photo editing for Apple silicon Macs, with Photoshop-style workflows.
  <br>Platforms: Apple silicon Mac · macOS 26+ · Start: [Download](https://github.com/robbietilton/Compositor/releases) · Status: In development · releases available
  <br>Needs: Apple silicon Mac with macOS 26+; source builds need Xcode 26+, and PSD/PSB import is limited to 8-bit RGB. · [code: MIT](https://github.com/robbietilton/Compositor/blob/main/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/compositor/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=compositor-en)

- **[PhotoCraft](https://github.com/storytold/photocraft)** — Adobe Photoshop · Workflow reimplementation. An alpha image editor reimplementing Photoshop-style workflows in Rust.
  <br>Platforms: Windows / macOS / Linux / FreeBSD / Web · Start: [Download](https://github.com/storytold/photocraft/releases) · Status: Alpha · workflows in progress
  <br>Needs: Alpha downloads are available; check your PSD files and workflow because format interchange and plug-in support remain incomplete. · [code: MIT OR Apache-2.0](https://github.com/storytold/photocraft/blob/main/LICENSE-MIT) · [Requirements & screenshots](https://remakelist.com/remakes/photocraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=photocraft-en)

- **[Graphite](https://github.com/GraphiteEditor/Graphite)** — Adobe Illustrator · Functional alternative. Browser-based vector design with layers and editable node graphs.
  <br>Platforms: Web · Start: [Browser](https://editor.graphite.art/) · Status: Alpha · browser editor available
  <br>Needs: Open the browser editor; it is still alpha, with broader creative workflows under development. · [code: MIT OR Apache-2.0](https://graphite.art/license/) · [Requirements & screenshots](https://remakelist.com/remakes/graphite/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=graphite-en)

- **[Friction](https://github.com/friction2d/friction)** — Adobe After Effects · Functional alternative. A 2D animation and motion-graphics editor with vector tools, timelines and expressions.
  <br>Platforms: Windows / macOS / Linux · Start: [Download](https://friction.graphics/#download) · Status: Desktop downloads · 2D motion graphics
  <br>Needs: Desktop downloads are available; After Effects project and plug-in compatibility is not promised, and custom shaders are experimental. · [code: GPL-3.0-only](https://github.com/friction2d/friction/blob/main/LICENSE.md) · [Requirements & screenshots](https://remakelist.com/remakes/friction/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=friction-en)

- **[OpenCut](https://github.com/OpenCut-app/OpenCut)** — CapCut · Functional alternative. A CapCut-style browser video editor whose next version is being rewritten.
  <br>Platforms: Web · Start: [Browser](https://opencut.app/) · Status: Early beta · rewrite in progress
  <br>Needs: The live site runs the classic early beta; desktop, mobile and automation plans are not established stable features. · [code: MIT](https://github.com/OpenCut-app/OpenCut/blob/main/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/opencut/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=opencut-en)

- **[Penpot](https://github.com/penpot/penpot)** — Figma · Functional alternative. A collaborative interface-design and prototyping tool with hosted and self-hosted options.
  <br>Platforms: Browser / self-hosted · Start: [Sign up / self-host](https://design.penpot.app) · Status: See official documentation
  <br>Needs: Use a hosted account or set up your own server; migrating designs requires export and import. · [code: MPL-2.0](https://github.com/penpot/penpot/blob/develop/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/penpot/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=penpot-en)

- **[VectorCraft](https://github.com/storytold/vectorcraft)** — Adobe Illustrator · Workflow reimplementation. An alpha vector editor reworking Illustrator-style pen, path and appearance workflows.
  <br>Platforms: Windows / macOS / Linux / Web · Start: [Download](https://getartcraft.com/apps/vectorcraft) · Status: Alpha
  <br>Needs: Desktop installers are available; test complex file interchange and appearance effects before moving a project. · [code: MIT OR Apache-2.0](https://github.com/storytold/vectorcraft/blob/main/LICENSE-MIT) · [Requirements & screenshots](https://remakelist.com/remakes/vectorcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=vectorcraft-en)

- **[LightCraft](https://github.com/storytold/lightcraft)** — Adobe Lightroom · Workflow reimplementation. An alpha photo-library and RAW-development tool with nondestructive color adjustment.
  <br>Platforms: Windows / macOS / Linux / Web · Start: [Download](https://getartcraft.com/apps/lightcraft) · Status: Alpha
  <br>Needs: Desktop installers are available; camera calibration and some compressed RAW formats remain incomplete. · [code: MIT OR Apache-2.0](https://github.com/storytold/lightcraft/blob/main/LICENSE-MIT) · [Requirements & screenshots](https://remakelist.com/remakes/lightcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=lightcraft-en)

- **[CADCraft](https://github.com/storytold/cadcraft)** — Autodesk AutoCAD · Workflow reimplementation. An early 2D drafting tool with commands, object snaps, layers and dimensions.
  <br>Platforms: Windows / macOS / Linux / Web · Start: [Download](https://getartcraft.com/apps/cadcraft) · Status: Early development
  <br>Needs: Desktop installers are available; check DWG compatibility and do not assume AutoCAD 3D or industry plug-in support. · [code: MIT OR Apache-2.0](https://github.com/storytold/cadcraft/blob/main/LICENSE-MIT) · [Requirements & screenshots](https://remakelist.com/remakes/cadcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=cadcraft-en)

- **[SoundCraft](https://github.com/storytold/soundcraft)** — Avid Pro Tools · Workflow reimplementation. A pre-alpha audio workstation with recording, track editing, mixing and MIDI arrangement.
  <br>Platforms: Windows / macOS / Linux / Web · Start: [Download](https://getartcraft.com/apps/soundcraft) · Status: Pre-alpha
  <br>Needs: Desktop installers are available; audio-device/buffer selection, MIDI-controller recording and AAF/OMF interchange are still missing. · [code: MIT OR Apache-2.0](https://github.com/storytold/soundcraft/blob/main/LICENSE-MIT) · [Requirements & screenshots](https://remakelist.com/remakes/soundcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=soundcraft-en)

- **[FilmCraft](https://github.com/storytold/filmcraft)** — Adobe Premiere Pro · Workflow reimplementation. An alpha video editor with source/program monitors, multitrack timelines and trim editing.
  <br>Platforms: Windows / macOS / Linux · Start: [Download](https://getartcraft.com/apps/filmcraft) · Status: Alpha
  <br>Needs: Desktop installers are available; large-media handling, effect rendering and professional project interchange remain incomplete. · [code: MIT OR Apache-2.0](https://github.com/storytold/filmcraft/blob/main/LICENSE-MIT) · [Requirements & screenshots](https://remakelist.com/remakes/filmcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=filmcraft-en)


<a id="everyday"></a>

## Everyday tools and interface recreations

- **[ONLYOFFICE Desktop Editors](https://github.com/ONLYOFFICE/DesktopEditors)** — Microsoft Office · Functional alternative. A desktop suite for offline documents, spreadsheets, presentations and PDF editing.
  <br>Platforms: Windows / macOS / Linux · Start: [Download](https://www.onlyoffice.com/download-desktop) · Status: Stable releases available
  <br>Needs: Local editing needs no Microsoft Office account; check complex layouts and macros, and use a compatible service for cloud collaboration. · [code: AGPL-3.0](https://github.com/ONLYOFFICE/DesktopEditors/blob/master/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/onlyoffice/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=onlyoffice-en)

- **[LibreOffice](https://github.com/LibreOffice/core)** — Microsoft Office · Functional alternative. A desktop office suite with Writer, Calc and Impress for everyday documents.
  <br>Platforms: Windows / macOS / Linux · Start: [Download](https://www.libreoffice.org/download/download-libreoffice/) · Status: Stable releases available
  <br>Needs: Install the desktop version without an Office subscription; test VBA macros and complex Office templates before switching. · [code: MPL-2.0 (primarily)](https://www.libreoffice.org/licenses/) · [Requirements & screenshots](https://remakelist.com/remakes/libreoffice/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=libreoffice-en)

- **[Grist](https://github.com/gristlabs/grist-core)** — Microsoft Excel / Airtable · Functional alternative. Spreadsheet-style editing backed by relational data, for structured tables and linked records.
  <br>Platforms: Windows / macOS / Linux · Start: [Download](https://github.com/gristlabs/grist-desktop/releases) · Status: Stable releases available
  <br>Needs: Use the local desktop app, self-host the Community edition or choose a hosted account with plan limits. · [code: Apache-2.0](https://github.com/gristlabs/grist-core/blob/main/LICENSE.txt) · [Requirements & screenshots](https://remakelist.com/remakes/grist/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=grist-en)

- **[Webamp](https://github.com/captbaritone/webamp)** — Winamp 2 · Web reimplementation. Winamp 2-style audio playback and skins recreated in a browser.
  <br>Platforms: Browser · Start: [Browser](https://webamp.org/) · Status: See official documentation
  <br>Needs: Open the browser player and bring your own audio; no Winamp installation is needed. · [code: MIT](https://github.com/captbaritone/webamp/blob/master/LICENSE.txt) · [Requirements & screenshots](https://remakelist.com/remakes/webamp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=webamp-en)

- **[WinXP in React](https://github.com/ShizukuIchi/winXP)** — Windows XP desktop · Interface recreation. A browser recreation of the Windows XP desktop, Start menu and small built-in apps.
  <br>Platforms: Browser · Start: [Browser](https://winxp.vercel.app/) · Status: See official documentation
  <br>Needs: No XP installation files are needed; the demo cannot run arbitrary Windows software. · [code: MIT (project code)](https://github.com/ShizukuIchi/winXP/blob/master/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/winxp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=winxp-en)

- **[PdfCraft](https://github.com/storytold/pdfcraft)** — Adobe Acrobat · Workflow reimplementation. An early-alpha PDF tool for reading, annotations, page organization, merging and splitting.
  <br>Platforms: Windows / macOS / Linux / Web · Start: [Download](https://getartcraft.com/apps/pdfcraft) · Status: Early alpha
  <br>Needs: Desktop installers are available; full Acrobat editing, signature and prepress workflows are not covered. · [code: MIT OR Apache-2.0](https://github.com/storytold/pdfcraft/blob/main/LICENSE-MIT) · [Requirements & screenshots](https://remakelist.com/remakes/pdfcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=pdfcraft-en)


<a id="classic_games"></a>

## Classic game engines and recreations

- **[OpenTTD](https://github.com/OpenTTD/OpenTTD)** — Transport Tycoon Deluxe · Game reimplementation. Transport Tycoon-style transport-company simulation with expanded multiplayer.
  <br>Platforms: Windows / macOS / Linux · Start: [Download](https://www.openttd.org/) · Status: See official documentation
  <br>Needs: Use the required free OpenGFX2 or OpenGFX graphics; OpenSFX sound and OpenMSX music are optional, with no original game files needed for this route. · [code: GPL-2.0](https://github.com/OpenTTD/OpenTTD/blob/master/COPYING.md) · [Requirements & screenshots](https://remakelist.com/remakes/openttd/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=openttd-en)

- **[OpenRCT2](https://github.com/OpenRCT2/OpenRCT2)** — RollerCoaster Tycoon 2 · Game reimplementation. A RollerCoaster Tycoon 2 reimplementation with improvements such as cooperative multiplayer.
  <br>Platforms: Windows / macOS / Linux · Start: [Download + own files](https://openrct2.io/download) · Status: See official documentation
  <br>Needs: Supply your own RCT2 data files; RCT1 data can add its scenarios. · [code: GPL-3.0-or-later](https://github.com/OpenRCT2/OpenRCT2/blob/develop/licence.txt) · [Requirements & screenshots](https://remakelist.com/remakes/openrct2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=openrct2-en)

- **[OpenMW](https://github.com/OpenMW/openmw)** — The Elder Scrolls III: Morrowind · Engine reimplementation. A Morrowind engine replacement with modern compatibility and graphics options.
  <br>Platforms: Windows / macOS / Linux · Start: [Download + own files](https://www.openmw.org) · Status: See official documentation
  <br>Needs: Own Morrowind and configure its data files; check support for your existing mods. · [code: GPLv3](https://github.com/OpenMW/openmw/blob/master/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/openmw/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=openmw-en)

- **[OpenRA](https://github.com/OpenRA/OpenRA)** — Red Alert 1 / Command & Conquer / Dune 2000 · Reimagining. A modernized take on classic RTS games, including the original Red Alert rather than Red Alert 2.
  <br>Platforms: Windows / macOS / Linux · Start: [Download](https://www.openra.net/) · Status: See official documentation
  <br>Needs: First-run setup can fetch required original assets or import them from original discs; rules and balance differ from the originals. · [code: GPL-3.0-or-later (engine)](https://github.com/OpenRA/OpenRA/blob/bleed/COPYING) · [Requirements & screenshots](https://remakelist.com/remakes/openra/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=openra-en)

- **[fheroes2](https://github.com/ihhub/fheroes2)** — Heroes of Might and Magic II · Engine reimplementation. A Heroes of Might and Magic II engine recreation with modern interface improvements.
  <br>Platforms: Windows / macOS / Linux / Android · Start: [Download + own files](https://github.com/ihhub/fheroes2/releases) · Status: Releases available · original/demo data
  <br>Needs: Supply full original-game data or use the documented official English demo route for limited content. · [code: GPL-2.0-or-later](https://github.com/ihhub/fheroes2/blob/master/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/fheroes2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=fheroes2-en)

- **[OpenXcom](https://github.com/OpenXcom/OpenXcom)** — UFO: Enemy Unknown / Terror from the Deep · Game reimplementation. A reimplementation of the two classic X-COM games with mod support.
  <br>Platforms: Windows / macOS / Linux · Start: [Download + own files](https://github.com/OpenXcom/OpenXcom/releases) · Status: Desktop engine · original data required
  <br>Needs: Provide unmodified UFO: Enemy Unknown or Terror from the Deep data; the Windows installer can import an owned Steam copy. · [code: GPL-3.0-or-later](https://github.com/OpenXcom/OpenXcom/blob/master/LICENSE.txt) · [Requirements & screenshots](https://remakelist.com/remakes/openxcom/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=openxcom-en)

- **[VCMI](https://github.com/vcmi/vcmi)** — Heroes of Might and Magic III · Engine reimplementation. A Heroes III engine replacement with mods, multiplayer and desktop/mobile versions.
  <br>Platforms: Windows / macOS / Linux / Android / iOS · Start: [Download + own files](https://vcmi.eu/download/) · Status: Public release · original data required
  <br>Needs: Full play needs Heroes III Complete or Shadow of Death data; HD Edition alone is insufficient, and iOS requires TestFlight or sideloading. · [code: GPL-2.0-or-later code](https://github.com/vcmi/vcmi/blob/66fa496c6328a276c4eb14c0011b3a9d751dfac3/license.txt) · [Requirements & screenshots](https://remakelist.com/remakes/vcmi/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=vcmi-en)

- **[Julius](https://github.com/bvschaik/julius)** — Caesar III · Game reimplementation. A faithful Caesar III engine reimplementation for modern computers and other platforms.
  <br>Platforms: Windows · Linux · macOS · Android · Web (Emscripten) · PS Vita · Nintendo Switch · Start: [Download + own files](https://github.com/bvschaik/julius/releases/tag/v1.8.0) · Status: Released · original game data required
  <br>Needs: Supply a full Caesar III installation patched to 1.0.1.0 and allow saves to be written to its data folder. · [code: AGPL-3.0](https://github.com/bvschaik/julius/blob/34d1ecd54befb845c0139b371fa8a0438210dac1/LICENSE.txt) · [Requirements & screenshots](https://remakelist.com/remakes/julius/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=julius-en)

- **[CorsixTH](https://github.com/CorsixTH/CorsixTH)** — Theme Hospital · Game reimplementation. A Theme Hospital engine recreation with modern resolutions and desktop support.
  <br>Platforms: Windows · macOS · Linux · BSD · Start: [Download + own files](https://github.com/CorsixTH/CorsixTH/releases/tag/v0.70.1) · Status: Released · original or demo data required
  <br>Needs: Select your own Theme Hospital data folder; the official demo offers only one level and omits most management screens. · [code: MIT](https://github.com/CorsixTH/CorsixTH/blob/master/LICENSE.txt) · [Requirements & screenshots](https://remakelist.com/remakes/corsixth/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=corsixth-en)

- **[Warzone 2100](https://github.com/Warzone2100/warzone2100)** — Warzone 2100 (1999) · Open-source continuation. The community-maintained 3D strategy game with a campaign, customizable units and desktop multiplayer.
  <br>Platforms: Windows · macOS · Linux · Web · Start: [Download](https://wz2100.net/) · Status: Released · desktop and browser editions
  <br>Needs: Official packages need no purchased original game; the browser edition has reduced graphics and no online multiplayer. · [code: GPL-2.0-or-later and component licenses](https://github.com/Warzone2100/warzone2100/blob/master/COPYING) · [Requirements & screenshots](https://remakelist.com/remakes/warzone2100/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=warzone2100-en)

- **[ScummVM](https://github.com/scummvm/scummvm)** — Classic adventure games and RPGs · Engine reimplementation. Replacement engines that run supported classic adventures on modern devices.
  <br>Platforms: Windows / macOS / Linux / Android / iOS · Start: [Download + own files](https://www.scummvm.org/downloads/) · Status: Released · compatibility varies by game and port
  <br>Needs: Provide supported game data or choose a complete title from the official Freeware Games page; check compatibility for your device’s ScummVM version. · [code: GPL-3.0-or-later engine code](https://github.com/scummvm/scummvm/blob/7d2709da5136866589f7602f5f5a7b17de03420e/COPYING) · [Requirements & screenshots](https://remakelist.com/remakes/scummvm/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=scummvm-en)

- **[RigelEngine](https://github.com/lethal-guitar/RigelEngine)** — Duke Nukem II · Engine reimplementation. A Duke Nukem II engine with widescreen, smoother movement, quick saves and controller support.
  <br>Platforms: Windows / macOS / Linux · Start: [Download + own files](https://github.com/lethal-guitar/RigelEngine/releases/tag/v0.9.1) · Status: Released · maintenance mode
  <br>Needs: Supply NUKEM2.CMP from the full game or limited shareware; the official Mac DMG is x64, with Apple silicon builds linked separately. · [code: GPL-2.0-or-later engine code](https://github.com/lethal-guitar/RigelEngine/blob/30afeff8f0b105eac77ee0a2fbd54b06e1a49b60/LICENSE.md) · [Requirements & screenshots](https://remakelist.com/remakes/rigelengine/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=rigelengine-en)

- **[OpenLoco](https://github.com/OpenLoco/OpenLoco)** — Chris Sawyer’s Locomotion · Game reimplementation. A modern reimplementation of Chris Sawyer’s Locomotion transport simulation.
  <br>Platforms: Windows x86/x64 · Linux x64 · macOS Apple silicon · Start: [Download + own files](https://openloco.io/download/) · Status: Released · original game data required
  <br>Needs: Supply original Locomotion data; the v26.09 Mac app requires Apple silicon and is unsigned and unnotarized. · [code: MIT](https://github.com/OpenLoco/OpenLoco/blob/v26.09/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/openloco/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=openloco-en)

- **[The Force Engine](https://github.com/TheForceEngine/TheForceEngine)** — Star Wars: Dark Forces · Engine reimplementation. Dark Forces with widescreen, modern mouse controls, quick saves and original community mods.
  <br>Platforms: Windows / Linux · macOS source build · Start: [Download + own files](https://github.com/TheForceEngine/TheForceEngine/releases/tag/v1.22.420) · Status: Released · Dark Forces supported
  <br>Needs: Supply purchased Dark Forces data and OpenGL 3.3; Windows has an official ZIP, Linux uses Flathub, and macOS requires a source build. · [code: GPL-2.0 engine code](https://github.com/TheForceEngine/TheForceEngine/blob/master/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/the-force-engine/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=the-force-engine-en)

- **[OpenJazz](https://github.com/AlisterT/openjazz)** — Jazz Jackrabbit · Engine reimplementation. An engine replacement for the original Jazz Jackrabbit on modern desktops.
  <br>Platforms: Windows / macOS / Linux · Start: [Download + own files](https://github.com/AlisterT/openjazz/releases/tag/20260301) · Status: Released · original game or shareware data required
  <br>Needs: Supply full-game or limited shareware data; the Linux x64 release needs glibc 2.35, while Mac Source Ports provides a signed Universal 2 Mac app. · [code: GPL-2.0-or-later engine code](https://github.com/AlisterT/openjazz/blob/master/doc/licenses.txt) · [Requirements & screenshots](https://remakelist.com/remakes/openjazz/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=openjazz-en)

- **[DevilutionX](https://github.com/diasurgical/DevilutionX)** — Diablo / Hellfire · Decompilation-based port. Diablo and Hellfire on modern devices with widescreen, controllers and optional quality-of-life changes.
  <br>Platforms: Windows / macOS / Linux / Android / iOS · Start: [Download + own files](https://github.com/diasurgical/DevilutionX/releases/tag/1.5.5) · Status: Released · own data required for the full game
  <br>Needs: Full Diablo needs your DIABDAT.MPQ, with additional MPQs for Hellfire; limited shareware is available, and iOS requires sideloading. · [source available; restricted license: Sustainable Use License 1.0](https://github.com/diasurgical/DevilutionX/blob/0011dc9670c2093d5ab0084c1cdbeb086556563a/LICENSE.md) · [Requirements & screenshots](https://remakelist.com/remakes/devilutionx/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=devilutionx-en)


<a id="ports"></a>

## Ports and compatibility projects

- **[Zelda 64: Recompiled](https://github.com/Zelda64Recomp/Zelda64Recomp)** — Majora’s Mask · Static recompilation. A native desktop recompilation of Majora’s Mask with modern controls and graphics options.
  <br>Platforms: Windows / Linux / macOS · Start: [Download + own files](https://github.com/Zelda64Recomp/Zelda64Recomp/releases) · Status: Release · original assets required
  <br>Needs: Provide your own North American Nintendo 64 Majora’s Mask ROM and a compatible graphics API; Windows, Linux and macOS packages are available. · [code: GPL-3.0](https://github.com/Zelda64Recomp/Zelda64Recomp/blob/dev/COPYING) · [Requirements & screenshots](https://remakelist.com/remakes/zelda64-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=zelda64-recompiled-en)

- **[D2R Mobile](https://github.com/jhaizhou-ops/d2r-mobile)** — Diablo II: Resurrected · Platform compatibility. A community project running the Switch version of Diablo II: Resurrected on compatible Apple devices.
  <br>Platforms: iPhone / iPad / Mac · A14 / M1+ · Start: [Build + own files](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) · Status: Personal build and owned Switch game files required
  <br>Needs: Requires your own Switch base game plus Reign of the Warlock at 1.0.34.0 (tool version 3.3.94012), extracted ExeFS/RomFS, an A14/M1+ device, local building and signing. Older devices need converted textures; select the build for your OS and keep game-derived packages private. · [code: MIT](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/d2r-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=d2r-mobile-en)

- **[nxnative](https://github.com/seedds/nxnative)** — Nintendo Switch games · Platform compatibility. A local-build compatibility project for turning supported Switch games into iPhone and iPad apps.
  <br>Platforms: iPhone / iPad · iOS / iPadOS 26+; Mac · development builds · Start: [Build + own files](https://github.com/seedds/nxnative#pack-an-ipa) · Status: Source build required · author-reported iPhone tests
  <br>Needs: Requires iOS/iPadOS 26+, an A17 Pro+ iPhone or M1+ iPad, your own game NSP/updates/DLC and prod.keys, plus a Mac with Xcode and Homebrew for building, signing and sideloading. Generated game packages are not for redistribution; compatibility is specific to each game and build. · [code: MIT project code](https://github.com/seedds/nxnative/blob/main/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/nxnative/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=nxnative-en)

- **[MW2 Recompiled](https://github.com/PaulCombal/mw2-recompiled)** — Modern Warfare 2 (2009) · Static recompilation. A Windows and Linux recompilation of the Xbox 360 version of Modern Warfare 2 (2009).
  <br>Platforms: Windows / Linux · Start: [Download + own files](https://github.com/PaulCombal/mw2-recompiled/releases) · Status: Release · original assets required
  <br>Needs: Provide a USA/Europe Xbox 360 disc ISO, version 1.0.557, plus 64-bit Windows/Linux, Vulkan 1.2, 8 GB space and a controller. Public matchmaking is unsupported; the original network code has known security bugs, so online play is limited to trusted friends. · [code: GPL-3.0-only](https://github.com/PaulCombal/mw2-recompiled/blob/master/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/mw2-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=mw2-recompiled-en)

- **[Mega Man X4 Recompiled](https://github.com/mstan/MegaManX4Recomp)** — Mega Man X4 · Static recompilation. A native Mega Man X4 recompilation with experimental local and online X/Zero co-op.
  <br>Platforms: Windows / Linux · Start: [Download + own files](https://github.com/mstan/MegaManX4Recomp/releases) · Status: Co-op alpha · original disc required
  <br>Needs: Supply USA SLUS-00561 .cue/.bin disc files; co-op is alpha, needs OpenGL and matching releases, and Linux x86_64 needs glibc 2.38+. · [code: MIT](https://github.com/mstan/MegaManX4Recomp/blob/master/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/mega-man-x4-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=mega-man-x4-recompiled-en)

- **[Birdman64](https://github.com/noahvl/birdman64)** — Pilotwings 64 · Decompilation-based port. A Pilotwings 64 port with widescreen, gamepads and configurable controls.
  <br>Platforms: Windows / Linux · Android experimental · iOS self-build · Start: [Download + own files](https://github.com/noahvl/birdman64/releases) · Status: Desktop releases · mobile experimental
  <br>Needs: Supply your own USA ROM and internet for the initial setup; desktop launchers are available, Android is experimental, and iPhone/iPad require self-building. · [code: MIT (project code). The code license grants no rights to the original game, artwork or commercial data.](https://github.com/NoahVl/Birdman64#license) · [Requirements & screenshots](https://remakelist.com/remakes/birdman64/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=birdman64-en)

- **[PeonPad](https://github.com/chrissotraidis/peonpad)** — Warcraft II · Engine reimplementation. A developer-preview iPad port of the Stratagus/Wargus Warcraft II engine with touch controls.
  <br>Platforms: iPadOS 16+ · Start: [Download + own files](https://github.com/chrissotraidis/peonpad/releases) · Status: Developer preview · unsigned IPA · user signing required
  <br>Needs: Requires iPadOS 16+, self-signing the unsigned IPA, and using Wargus on a Mac/PC to extract your own Warcraft II data into the complete data.Wargus folder. Copy that folder into the app manually; there is no App Store or TestFlight release. · [code: GPL-2.0 applies to the project’s original code only](https://github.com/chrissotraidis/peonpad/blob/main/LICENSE) · [Requirements & screenshots](https://remakelist.com/remakes/peonpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakes&utm_content=peonpad-en)

## Contribute and correct

Suggest a project, report outdated information or improve the list through a PR. Read the [contribution guide](CONTRIBUTING.md) for the sources we need. This selection comes from the published RemakeList directory. Per-entry source-review dates and official documentation are available in the [structured catalog](data/projects.json). See the [data notes](docs/data.md).

Functional alternatives, interface recreations and game projects are labeled separately. Not every entry is open source. A code license does not license the original game's assets; this repository supplies no game files, keys or install packages.

Original list text: [CC BY 4.0](LICENSE). Generator scripts: [MIT](scripts/LICENSE). Listed projects and third-party material retain their own licenses; see [NOTICE](NOTICE.md).
