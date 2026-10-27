<a href="https://remakelist.com/ja/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=intro-ja"><img src="assets/brand-banner.svg" alt="RemakeList — software recreations and classic game ports" width="920"></a>

# Awesome RemakeList

ソフトウェアの再実装、ゲームエンジン、移植作品と、試す前に必要な準備をまとめたリストです。

[English](README.md) · [简体中文](README.zh-CN.md) · **日本語** · [한국어](README.ko.md) · [Español](README.es.md)

[RemakeList を見る](https://remakelist.com/ja/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=intro-ja) · [プロジェクトを推薦](https://github.com/CharlexH/awesome-remakelist/issues/new?template=project.yml)

[![Catalog checks](https://github.com/CharlexH/awesome-remakelist/actions/workflows/check.yml/badge.svg?branch=main)](https://github.com/CharlexH/awesome-remakelist/actions/workflows/check.yml) [![Website sync](https://github.com/CharlexH/awesome-remakelist/actions/workflows/sync.yml/badge.svg?branch=main)](https://github.com/CharlexH/awesome-remakelist/actions/workflows/sync.yml)

プロジェクト名から作者の公開元へ移動できます。各項目を開くと、対応機器、ゲームデータ、ビルドの要件を確認できます。RemakeList にはスクリーンショットと導入の説明もあります。

## まずはこちら

| プロジェクト | 詳しく見る | 利用方法 |
| --- | --- | --- |
| [Graphite](https://remakelist.com/ja/remakes/graphite/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=graphite-featured-ja) | Adobe Illustrator | [ブラウザーで試す](https://editor.graphite.art/) |
| [Webamp](https://remakelist.com/ja/remakes/webamp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=webamp-featured-ja) | Winamp 2 | [ブラウザーで試す](https://webamp.org/) |
| [OpenTTD](https://remakelist.com/ja/remakes/openttd/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openttd-featured-ja) | Transport Tycoon Deluxe | [ダウンロード](https://www.openttd.org/) |
| [OpenRCT2](https://remakelist.com/ja/remakes/openrct2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openrct2-featured-ja) | RollerCoaster Tycoon 2 | [プログラムをダウンロード・ゲームデータは自分で用意](https://openrct2.io/download) |
| [D2R Mobile](https://remakelist.com/ja/remakes/d2r-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=d2r-mobile-featured-ja) | Diablo II: Resurrected | [自分でビルド・ゲームデータも用意](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) |
| [nxnative](https://remakelist.com/ja/remakes/nxnative/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nxnative-featured-ja) | Nintendo Switch ゲーム | [自分でビルド・ゲームデータも用意](https://github.com/seedds/nxnative#pack-an-ipa) |

## カテゴリを見る

- [デザイン・制作ツール](#creative) · 13
- [日常のツールとインターフェースの再現](#everyday) · 9
- [ゲームエンジンとゲームの再実装](#classic_games) · 26
- [移植・互換性プロジェクト](#ports) · 57

<img src="assets/overview-ja.svg" alt="目次" width="920">

<a id="creative"></a>

## デザイン・制作ツール

### [Compositor](https://github.com/robbietilton/Compositor)

Photoshop 型の作業手順を採用した、Apple silicon Mac 向けのレイヤー合成・ポスト処理エディター。

原作・参考元: **Adobe Photoshop** · 同様の機能を持つ独立した代替ツール  
[ダウンロード](https://github.com/robbietilton/Compositor/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/compositor/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=compositor-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Apple silicon Mac · macOS 26 以降

**開発状況:** 開発中 · 配布版あり

**必要なもの:** Photoshop のインストールは不要です。Apple silicon Mac と macOS 26 以降が必要で、ソースのビルドには Xcode 26 以降を使います。編集するメディアの権利は利用者が確認してください。

**現在利用できるもの:** 配布版の利用には Apple silicon Mac と macOS 26 以降が必要で、画面は現在英語のみです。PSD/PSB の読み込みは 8 ビット RGB に対応し、CMYK には非対応。一部のベクターや縦書き文字はラスタライズされます。ソースからのビルドには Xcode 26 以降が必要です。

**コードのライセンス:** [MIT](https://github.com/robbietilton/Compositor/blob/main/LICENSE)  
**作者:** robbietilton  
[公式ドキュメント](https://github.com/robbietilton/Compositor/blob/main/README.md) · 資料確認日: 2026-10-12

</details>

### [PhotoCraft](https://github.com/storytold/photocraft)

ArtCraft チームが Rust で再実装する、Photoshop 型の画像編集ツール。現在はアルファ版です。

原作・参考元: **Adobe Photoshop** · ワークフローの再実装  
[ダウンロード](https://github.com/storytold/photocraft/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/photocraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=photocraft-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / FreeBSD / ウェブ

**開発状況:** アルファ · 作業手順を開発中

**必要なもの:** Photoshop のインストールは不要です。編集画像には適切な権利が必要で、同梱フォントやアイコンには個別のライセンスがあります。ArtCraft の商標はコードのライセンスに含まれません。

**現在利用できるもの:** Photoshop なしで使えるアルファ版が配布されています。Windows、macOS、Linux、FreeBSD、ウェブへの対応が記載されていますが、PSD の互換性、ツールの充実度、プラグイン互換性は未完成で、業務全体を置き換える段階ではありません。

**コードのライセンス:** [MIT OR Apache-2.0](https://github.com/storytold/photocraft/blob/main/LICENSE-MIT)  
**作者:** storytold  
[公式ドキュメント](https://github.com/storytold/photocraft/blob/main/README.md) · 資料確認日: 2026-10-12

</details>

### [Graphite](https://github.com/GraphiteEditor/Graphite)

レイヤーとノードを組み合わせ、ブラウザーで非破壊編集ができるオープンソースのベクターデザインツール。

原作・参考元: **Adobe Illustrator** · 同様の機能を持つ独立した代替ツール  
[ブラウザーで試す](https://editor.graphite.art/) · [RemakeList を見る](https://remakelist.com/ja/remakes/graphite/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=graphite-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** ウェブ

**開発状況:** アルファ · ブラウザー版あり

**必要なもの:** Illustrator のインストールや原ソフトのファイルは不要です。画像、フォント、制作素材は自分で用意してください。

**現在利用できるもの:** ブラウザー版で、Illustrator なしにベクターデザインを試せます。まだアルファ版で、幅広い写真編集、モーション、出版、VFX 機能は発展途上です。Adobe の作業環境全体を置き換えるものではありません。

**コードのライセンス:** [MIT OR Apache-2.0](https://graphite.art/license/)  
**作者:** Graphite community  
[公式ドキュメント](https://github.com/GraphiteEditor/Graphite/blob/master/README.md) · 資料確認日: 2026-10-12

</details>

### [Friction](https://github.com/friction2d/friction)

ベクターとラスターのアニメーション、タイムライン、式に対応した、オープンソースの 2D モーショングラフィックスツール。

原作・参考元: **Adobe After Effects** · 同様の機能を持つ独立した代替ツール  
[ダウンロード](https://friction.graphics/#download) · [RemakeList を見る](https://remakelist.com/ja/remakes/friction/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=friction-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** デスクトップ版あり · 2D モーショングラフィックス

**必要なもの:** After Effects のインストールは不要です。画像、フォント、音声、動画素材は自分で用意してください。

**現在利用できるもの:** Windows、Linux、macOS 向けのダウンロードがあります。2D アニメーションとモーショングラフィックスを制作できますが、独自シェーダー効果は実験段階です。After Effects のプロジェクト、プラグイン、エフェクトチェーン全体の互換性は保証されていません。

**コードのライセンス:** [GPL-3.0-only](https://github.com/friction2d/friction/blob/main/LICENSE.md)  
**作者:** Ole-André Rodlie &amp; contributors  
[公式ドキュメント](https://friction.graphics/) · 資料確認日: 2026-10-12

</details>

### [OpenCut](https://github.com/OpenCut-app/OpenCut)

CapCut 型の編集を目指すオープンソース動画エディター。次期版を書き直している間、従来の初期ベータ版を公開しています。

原作・参考元: **CapCut** · 同様の機能を持つ独立した代替ツール  
[ブラウザーで試す](https://opencut.app/) · [RemakeList を見る](https://remakelist.com/ja/remakes/opencut/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=opencut-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** ウェブ

**開発状況:** 初期ベータ · 書き直し中

**必要なもの:** CapCut のインストールは不要です。利用する権利のある動画、画像、音声を取り込んでください。

**現在利用できるもの:** 公式サイトでは現在、従来の初期ベータ版を提供しています。そのソースはアーカイブされ、新版は書き直し中です。試す価値のある候補ですが、日常の CapCut の作業を全面的に引き継げると考える段階ではありません。

**コードのライセンス:** [MIT](https://github.com/OpenCut-app/OpenCut/blob/main/LICENSE)  
**作者:** OpenCut contributors  
[公式ドキュメント](https://github.com/OpenCut-app/OpenCut/blob/main/README.md) · 資料確認日: 2026-10-12

</details>

### [Penpot](https://github.com/penpot/penpot)

ホスト版でもセルフホストでも使える、オープンソースの共同デザイン・プロトタイピング基盤。

原作・参考元: **Figma** · 同様の機能を持つ独立した代替ツール  
[アカウント登録またはセルフホスト](https://design.penpot.app) · [RemakeList を見る](https://remakelist.com/ja/remakes/penpot/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=penpot-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** ブラウザー / セルフホスト

**開発状況:** 公式ドキュメントを参照

**必要なもの:** Figma のソフトや素材は不要です。移行には自分のデザインを書き出し、読み込む必要があります。

**現在利用できるもの:** ホスト版に登録するか、自分で設置して使えます。既存のデザインを移すには書き出しと読み込みが必要です。ホスト版のプランは料金ページを確認してください。

**コードのライセンス:** [MPL-2.0](https://github.com/penpot/penpot/blob/develop/LICENSE)  
**作者:** penpot  
[公式ドキュメント](https://penpot.app/penpot-vs-figma) · 資料確認日: 2026-10-11

</details>

### [VectorCraft](https://github.com/storytold/vectorcraft)

ArtCraft が Rust で再実装する Adobe Illustrator 型の制作環境。ペン描画、パスのブール演算、アピアランス効果、ベクターイラストを扱います。

原作・参考元: **Adobe Illustrator** · ワークフローの再実装  
[ダウンロード](https://getartcraft.com/apps/vectorcraft) · [RemakeList を見る](https://remakelist.com/ja/remakes/vectorcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vectorcraft-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / ウェブ

**開発状況:** アルファ

**必要なもの:** 市販の原ソフトは不要です。利用権限のある文書やメディアを用意してください。同梱のフォント、画像、ブランド商標には個別のライセンスがあります。

**現在利用できるもの:** アルファ版で、日常的なベクター描画を試せます。複雑なファイルの相互変換や効果の再現性は確認が必要です。デスクトップ用インストーラーがあり、対応環境とファイル互換性はプロジェクト資料で確認してください。

**コードのライセンス:** [MIT OR Apache-2.0](https://github.com/storytold/vectorcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[公式ドキュメント](https://github.com/storytold/vectorcraft/blob/main/README.md) · 資料確認日: 2026-10-12

</details>

### [FilmCraft](https://github.com/storytold/filmcraft)

ArtCraft が Rust で再実装する Adobe Premiere Pro 型の制作環境。ソース・プログラムモニター、複数トラックのタイムライン、トリム編集を備えます。

原作・参考元: **Adobe Premiere Pro** · ワークフローの再実装  
[ダウンロード](https://getartcraft.com/apps/filmcraft) · [RemakeList を見る](https://remakelist.com/ja/remakes/filmcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=filmcraft-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** アルファ

**必要なもの:** 市販の原ソフトは不要です。利用権限のある文書やメディアを用意してください。同梱のフォント、画像、ブランド商標には個別のライセンスがあります。

**現在利用できるもの:** アルファ版で、編集と書き出しの作業ができます。大容量メディアの性能、効果の描画、業務用プロジェクトの相互変換は未完成です。デスクトップ用インストーラーがあり、対応環境とファイル互換性はプロジェクト資料で確認してください。

**コードのライセンス:** [MIT OR Apache-2.0](https://github.com/storytold/filmcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[公式ドキュメント](https://github.com/storytold/filmcraft/blob/main/README.md) · 資料確認日: 2026-10-12

</details>

### [LightCraft](https://github.com/storytold/lightcraft)

ArtCraft が Rust で再実装する Adobe Lightroom 型の制作環境。写真ライブラリー管理、RAW 現像、非破壊の色調整を扱います。

原作・参考元: **Adobe Lightroom** · ワークフローの再実装  
[ダウンロード](https://getartcraft.com/apps/lightcraft) · [RemakeList を見る](https://remakelist.com/ja/remakes/lightcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=lightcraft-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / ウェブ

**開発状況:** アルファ

**必要なもの:** 市販の原ソフトは不要です。利用権限のある文書やメディアを用意してください。同梱のフォント、画像、ブランド商標には個別のライセンスがあります。

**現在利用できるもの:** アルファ版で、JPEG、DNG、多くのカメラ RAW 形式を試せます。カメラの色校正と一部の圧縮 RAW 形式は未完成です。デスクトップ用インストーラーがあり、対応環境とファイル互換性はプロジェクト資料で確認してください。

**コードのライセンス:** [MIT OR Apache-2.0](https://github.com/storytold/lightcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[公式ドキュメント](https://github.com/storytold/lightcraft/blob/main/README.md) · 資料確認日: 2026-10-12

</details>

### [EffectCraft](https://github.com/storytold/effectcraft)

ArtCraft が Rust で再実装する Adobe After Effects 型の制作環境。レイヤー合成、キーフレームアニメーション、モーショングラフィックス、効果を扱います。

原作・参考元: **Adobe After Effects** · ワークフローの再実装  
[ダウンロード](https://getartcraft.com/apps/effectcraft) · [RemakeList を見る](https://remakelist.com/ja/remakes/effectcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=effectcraft-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / ウェブ

**開発状況:** 開発初期

**必要なもの:** 市販の原ソフトは不要です。利用権限のある文書やメディアを用意してください。同梱のフォント、画像、ブランド商標には個別のライセンスがあります。

**現在利用できるもの:** 開発初期で、アニメーションと合成の実験向けです。顧客への納品向けではなく、AEP/AEPX プロジェクトと After Effects プラグインには非対応です。デスクトップ用インストーラーがあり、対応環境とファイル互換性はプロジェクト資料で確認してください。

**コードのライセンス:** [MIT OR Apache-2.0](https://github.com/storytold/effectcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[公式ドキュメント](https://github.com/storytold/effectcraft/blob/main/README.md) · 資料確認日: 2026-10-12

</details>

### [DesignCraft](https://github.com/storytold/designcraft)

ArtCraft が Rust で再実装する Adobe InDesign 型の制作環境。見開きレイアウト、連結テキストフレーム、親ページ、出版用文書を扱います。

原作・参考元: **Adobe InDesign** · ワークフローの再実装  
[ダウンロード](https://getartcraft.com/apps/designcraft) · [RemakeList を見る](https://remakelist.com/ja/remakes/designcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=designcraft-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / ウェブ

**開発状況:** 開発中

**必要なもの:** 市販の原ソフトは不要です。利用権限のある文書やメディアを用意してください。同梱のフォント、画像、ブランド商標には個別のライセンスがあります。

**現在利用できるもの:** 開発中で、レイアウトと書き出しを試せるビルドがあります。複雑な出版ファイル、組版、印刷製版は個別の確認が必要です。デスクトップ用インストーラーがあり、対応環境とファイル互換性はプロジェクト資料で確認してください。

**コードのライセンス:** [MIT OR Apache-2.0](https://github.com/storytold/designcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[公式ドキュメント](https://github.com/storytold/designcraft/blob/main/README.md) · 資料確認日: 2026-10-12

</details>

### [SoundCraft](https://github.com/storytold/soundcraft)

ArtCraft が Rust で再実装する Avid Pro Tools 型の制作環境。トラック録音、編集ウィンドウ、ミキサー、MIDI 編曲を備えます。

原作・参考元: **Avid Pro Tools** · ワークフローの再実装  
[ダウンロード](https://getartcraft.com/apps/soundcraft) · [RemakeList を見る](https://remakelist.com/ja/remakes/soundcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=soundcraft-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / ウェブ

**開発状況:** プレアルファ

**必要なもの:** 市販の原ソフトは不要です。利用権限のある文書やメディアを用意してください。同梱のフォント、画像、ブランド商標には個別のライセンスがあります。

**現在利用できるもの:** プレアルファ版で、録音、編集、ミキシング、バウンスの作業ができます。音声デバイス・バッファー選択、MIDI コントローラー録音、AAF/OMF の相互変換は未実装です。デスクトップ用インストーラーがあり、対応環境とファイル互換性はプロジェクト資料で確認してください。

**コードのライセンス:** [MIT OR Apache-2.0](https://github.com/storytold/soundcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[公式ドキュメント](https://github.com/storytold/soundcraft/blob/main/README.md) · 資料確認日: 2026-10-12

</details>

### [CADCraft](https://github.com/storytold/cadcraft)

ArtCraft が Rust で再実装する Autodesk AutoCAD 型の作業環境。コマンドライン製図、オブジェクトスナップ、レイヤー、寸法、図面レイアウトを扱います。

原作・参考元: **Autodesk AutoCAD** · ワークフローの再実装  
[ダウンロード](https://getartcraft.com/apps/cadcraft) · [RemakeList を見る](https://remakelist.com/ja/remakes/cadcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cadcraft-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / ウェブ

**開発状況:** 開発初期

**必要なもの:** 市販の原ソフトは不要です。利用権限のある文書やメディアを用意してください。同梱のフォント、画像、ブランド商標には個別のライセンスがあります。

**現在利用できるもの:** 開発初期で、2D 図面と PDF 出力を試す用途に向きます。AutoCAD の 3D、DWG、業界向けプラグインのすべてを代替するものではありません。デスクトップ用インストーラーがあり、対応環境とファイル互換性はプロジェクト資料で確認してください。

**コードのライセンス:** [MIT OR Apache-2.0](https://github.com/storytold/cadcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[公式ドキュメント](https://github.com/storytold/cadcraft/blob/main/README.md) · 資料確認日: 2026-10-12

</details>


<a id="everyday"></a>

## 日常のツールとインターフェースの再現

### [ONLYOFFICE Desktop Editors](https://github.com/ONLYOFFICE/DesktopEditors)

文書、表計算、プレゼンテーション、PDF を一つのデスクトップアプリでオフライン編集できる、オープンソースの Microsoft Office 代替。

原作・参考元: **Microsoft Office** · 同様の機能を持つ独立した代替ツール  
[ダウンロード](https://www.onlyoffice.com/download-desktop) · [RemakeList を見る](https://remakelist.com/ja/remakes/onlyoffice/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=onlyoffice-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** 安定版あり

**必要なもの:** ローカル編集に Microsoft Office のインストールやアカウントは不要です。クラウドでの共同作業には対応サービスが必要で、有料の場合があります。

**現在利用できるもの:** Windows、macOS、Linux 向けのインストーラーがあり、ローカル保存とオフライン編集に対応します。デスクトップ版は無料ですが、クラウドサービスや企業向け版には別のプランがあります。移行前に複雑な文書のレイアウトを確認してください。

**コードのライセンス:** [AGPL-3.0](https://github.com/ONLYOFFICE/DesktopEditors/blob/master/LICENSE)  
**作者:** ONLYOFFICE  
[公式ドキュメント](https://github.com/ONLYOFFICE/DesktopEditors) · 資料確認日: 2026-10-12

</details>

### [Grist](https://github.com/gristlabs/grist-core)

リレーショナルデータと表計算型の編集を組み合わせた、Excel や Airtable の作業に使えるオープンソースの代替。

原作・参考元: **Microsoft Excel / Airtable** · 同様の機能を持つ独立した代替ツール  
[ダウンロード](https://github.com/gristlabs/grist-desktop/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/grist/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=grist-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** 安定版あり

**必要なもの:** デスクトップ版はローカルファイルを編集します。セルフホストにはサーバー環境が必要です。ホスト版にはアカウントが必要で、使用量と機能に制限があります。

**現在利用できるもの:** Windows、macOS、Linux のデスクトップ版でローカルファイルを編集でき、Community 版はセルフホストも可能です。ホスト版の無料・有料プランは別で、企業向け機能のすべてがオープンソースの中核に含まれるわけではありません。

**コードのライセンス:** [Apache-2.0](https://github.com/gristlabs/grist-core/blob/main/LICENSE.txt)  
**作者:** Grist Labs  
[公式ドキュメント](https://github.com/gristlabs/grist-core) · 資料確認日: 2026-10-12

</details>

### [LibreOffice](https://github.com/LibreOffice/core)

文書の Writer、表計算の Calc、プレゼンテーションの Impress を備えた、無料・オープンソースの Microsoft Office 代替。

原作・参考元: **Microsoft Office** · 同様の機能を持つ独立した代替ツール  
[ダウンロード](https://www.libreoffice.org/download/download-libreoffice/) · [RemakeList を見る](https://remakelist.com/ja/remakes/libreoffice/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=libreoffice-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** 安定版あり

**必要なもの:** Microsoft Office のインストール、契約、アカウントは不要です。環境に合うデスクトップ版を入れ、編集権限のあるファイルを使用してください。

**現在利用できるもの:** Windows、macOS、Linux 向けに配布され、日常のオフィス作業をひと通り行えます。VBA マクロ、複雑な Office テンプレート、厳密なレイアウト再現が必要なら、先に自分のファイルで試してください。

**コードのライセンス:** [MPL-2.0 (primarily)](https://www.libreoffice.org/licenses/)  
**作者:** The Document Foundation  
[公式ドキュメント](https://www.libreoffice.org/) · 資料確認日: 2026-10-12

</details>

### [Webamp](https://github.com/captbaritone/webamp)

クラシックなプレーヤー画面とスキン対応を備えた、Winamp 2 のブラウザー再実装。

原作・参考元: **Winamp 2** · Web での再実装  
[ブラウザーで試す](https://webamp.org/) · [RemakeList を見る](https://remakelist.com/ja/remakes/webamp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=webamp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** ブラウザー

**開発状況:** 公式ドキュメントを参照

**必要なもの:** Winamp のインストールは不要です。音声や第三者のスキンにはそれぞれの権利が適用されます。

**現在利用できるもの:** オンラインプレーヤーをブラウザーで直接開けます。原ソフトは不要で、再生したい音声を自分で用意します。

**コードのライセンス:** [MIT](https://github.com/captbaritone/webamp/blob/master/LICENSE.txt)  
**作者:** captbaritone  
[公式ドキュメント](https://github.com/captbaritone/webamp/blob/master/README.md) · 資料確認日: 2026-10-11

</details>

### [WinXP in React](https://github.com/ShizukuIchi/winXP)

Windows XP のデスクトップ、スタートメニュー、定番の小さなアプリをブラウザーで再現。

原作・参考元: **Windows XP のデスクトップ** · インターフェースの再現  
[ブラウザーで試す](https://winxp.vercel.app/) · [RemakeList を見る](https://remakelist.com/ja/remakes/winxp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=winxp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** ブラウザー

**開発状況:** 公式ドキュメントを参照

**必要なもの:** Windows XP のインストールファイルは不要です。

**現在利用できるもの:** Windows XP のインストールファイルなしでオンラインデモを使えます。再現されたデスクトップとアプリが対象で、任意の XP ソフトを動かすことはできません。

**コードのライセンス:** [MIT (project code)](https://github.com/ShizukuIchi/winXP/blob/master/LICENSE)  
**作者:** ShizukuIchi  
[公式ドキュメント](https://github.com/ShizukuIchi/winXP/blob/master/README.md) · 資料確認日: 2026-10-11

</details>

### [PdfCraft](https://github.com/storytold/pdfcraft)

ArtCraft が Rust で再実装する Adobe Acrobat 型の作業環境。PDF 閲覧、注釈、ページ整理、結合、分割を扱います。

原作・参考元: **Adobe Acrobat** · ワークフローの再実装  
[ダウンロード](https://getartcraft.com/apps/pdfcraft) · [RemakeList を見る](https://remakelist.com/ja/remakes/pdfcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pdfcraft-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / ウェブ

**開発状況:** 初期アルファ

**必要なもの:** 市販の原ソフトは不要です。利用権限のある文書やメディアを用意してください。同梱のフォント、画像、ブランド商標には個別のライセンスがあります。

**現在利用できるもの:** 初期アルファ版で、閲覧とページ管理を利用できます。Acrobat の編集、署名、印刷製版の作業全体を代替するものではありません。デスクトップ用インストーラーがあり、対応環境とファイル互換性はプロジェクト資料で確認してください。

**コードのライセンス:** [MIT OR Apache-2.0](https://github.com/storytold/pdfcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[公式ドキュメント](https://github.com/storytold/pdfcraft/blob/main/README.md) · 資料確認日: 2026-10-12

</details>

### [WordCraft](https://github.com/storytold/wordcraft)

ArtCraft が Rust で再実装する Microsoft Word 型の作業環境。文書作成、スタイル、表、変更履歴、文書レイアウトを扱います。

原作・参考元: **Microsoft Word** · ワークフローの再実装  
[ダウンロード](https://getartcraft.com/apps/wordcraft) · [RemakeList を見る](https://remakelist.com/ja/remakes/wordcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wordcraft-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / ウェブ

**開発状況:** アルファ

**必要なもの:** 市販の原ソフトは不要です。利用権限のある文書やメディアを用意してください。同梱のフォント、画像、ブランド商標には個別のライセンスがあります。

**現在利用できるもの:** アルファ版で、文書作成と DOCX の作業を試せます。ページ区切り、グラフ・SmartArt の往復変換の再現性、ネイティブ印刷には改善が必要です。デスクトップ用インストーラーがあり、対応環境とファイル互換性はプロジェクト資料で確認してください。

**コードのライセンス:** [MIT OR Apache-2.0](https://github.com/storytold/wordcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[公式ドキュメント](https://github.com/storytold/wordcraft/blob/main/README.md) · 資料確認日: 2026-10-13

</details>

### [DeckCraft](https://github.com/storytold/deckcraft)

ArtCraft が Rust で再実装する Microsoft PowerPoint 型の制作環境。スライドマスター、テーマ、図形、アニメーション、スライドショー再生を備えます。

原作・参考元: **Microsoft PowerPoint** · ワークフローの再実装  
[ダウンロード](https://getartcraft.com/apps/deckcraft) · [RemakeList を見る](https://remakelist.com/ja/remakes/deckcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=deckcraft-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / ウェブ

**開発状況:** アルファ

**必要なもの:** 市販の原ソフトは不要です。利用権限のある文書やメディアを用意してください。同梱のフォント、画像、ブランド商標には個別のライセンスがあります。

**現在利用できるもの:** アルファ版で、資料の作成と発表ができます。複雑な PPTX ファイルやアニメーションが PowerPoint と同じように動くとは限りません。デスクトップ用インストーラーがあり、対応環境とファイル互換性はプロジェクト資料で確認してください。

**コードのライセンス:** [MIT OR Apache-2.0](https://github.com/storytold/deckcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[公式ドキュメント](https://github.com/storytold/deckcraft/blob/main/README.md) · 資料確認日: 2026-10-13

</details>

### [GridCraft](https://github.com/storytold/gridcraft)

ArtCraft が Rust で再実装する Microsoft Excel 型の作業環境。ワークシート、数式、テーブル、グラフ、ピボットテーブルを扱います。

原作・参考元: **Microsoft Excel** · ワークフローの再実装  
[ダウンロード](https://getartcraft.com/apps/gridcraft) · [RemakeList を見る](https://remakelist.com/ja/remakes/gridcraft/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gridcraft-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / ウェブ

**開発状況:** アルファ

**必要なもの:** 市販の原ソフトは不要です。利用権限のある文書やメディアを用意してください。同梱のフォント、画像、ブランド商標には個別のライセンスがあります。

**現在利用できるもの:** アルファ版で、基本的な表計算を試せます。実際の XLSX ファイルの再現性、大きなブックの性能、グラフ機能、旧形式の読み込みには改善が必要です。デスクトップ用インストーラーがあり、対応環境とファイル互換性はプロジェクト資料で確認してください。

**コードのライセンス:** [MIT OR Apache-2.0](https://github.com/storytold/gridcraft/blob/main/LICENSE-MIT)  
**作者:** ArtCraft  
[公式ドキュメント](https://github.com/storytold/gridcraft/blob/main/README.md) · 資料確認日: 2026-10-13

</details>


<a id="classic_games"></a>

## ゲームエンジンとゲームの再実装

### [Vanguard Engine](https://github.com/harshilmathur/openra2)

Red Alert 2 のデータ向けに作られた独立したブラウザー RTS エンジン。現在はソ連軍の一人用小規模戦に絞って開発されています。

原作・参考元: **Red Alert 2 / Yuri’s Revenge のデータ** · エンジンの再実装  
[ソースからビルド](https://github.com/harshilmathur/openra2/blob/master/README.md#quickstart) · [RemakeList を見る](https://remakelist.com/ja/remakes/vanguard/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vanguard-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** ブラウザー · ローカル開発サーバー

**開発状況:** 開発版 · 正式リリースなし

**必要なもの:** Classic モードには正規に所有する RA2/YR のファイルが必要です。Original モードはリポジトリ独自の素材を使い、原作は不要です。両モードは別です。Node.js 20.19 以降とローカル開発サーバーが必要です。

**現在利用できるもの:** 正式リリース前の開発版で、Node.js 20.19 以降とローカル開発サーバーが必要です。Classic モードには適法に入手した RA2/YR のファイルが必要ですが、Original モードに原作は不要です。連合軍、ネット対戦、Yuri のゲーム内容は未完成で、Red Alert 2 全体を再現したものではありません。

**コードのライセンス:** [GPL-3.0-or-later](https://github.com/harshilmathur/openra2/blob/master/LICENSE)  
**作者:** harshilmathur  
[公式ドキュメント](https://github.com/harshilmathur/openra2/blob/master/README.md) · 資料確認日: 2026-10-12

</details>

### [OpenTTD](https://github.com/OpenTTD/OpenTTD)

Transport Tycoon の遊びを現代の環境向けに作り直し、マルチプレイを拡充。

原作・参考元: **Transport Tycoon Deluxe** · ゲームの再実装  
[ダウンロード](https://www.openttd.org/) · [RemakeList を見る](https://remakelist.com/ja/remakes/openttd/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openttd-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** 公式ドキュメントを参照

**必要なもの:** 基本グラフィックが必要です。無料の OpenGFX2 または OpenGFX を利用できます。OpenSFX の効果音と OpenMSX の音楽は任意です。この無料の始め方では原作のファイルは不要です。

**現在利用できるもの:** デスクトップ版が配布されています。必須の基本グラフィックには無料の OpenGFX2 または OpenGFX を用意してください。OpenSFX の効果音と OpenMSX の音楽は任意です。この方法では原作のファイルは不要です。

**コードのライセンス:** [GPL-2.0; third-party components have separate licenses](https://github.com/OpenTTD/OpenTTD/blob/master/COPYING.md)  
**作者:** OpenTTD  
[公式ドキュメント](https://github.com/OpenTTD/OpenTTD/blob/master/README.md) · 資料確認日: 2026-10-11

</details>

### [OpenRCT2](https://github.com/OpenRCT2/OpenRCT2)

共同マルチプレイなどの改善を加え、RollerCoaster Tycoon 2 を現代の環境で。

原作・参考元: **RollerCoaster Tycoon 2** · ゲームの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://openrct2.io/download) · [RemakeList を見る](https://remakelist.com/ja/remakes/openrct2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openrct2-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** 公式ドキュメントを参照

**必要なもの:** RCT2 の原作データを自分で用意する必要があります。RCT1 のデータでシナリオを追加できます。

**現在利用できるもの:** 配布版はありますが、RCT2 の原作データを自分で用意する必要があります。RCT1 のデータを使うとそのシナリオも追加できます。無料のエンジンに市販の原作素材は含まれません。

**コードのライセンス:** [GPL-3.0-or-later](https://github.com/OpenRCT2/OpenRCT2/blob/develop/licence.txt)  
**作者:** OpenRCT2  
[公式ドキュメント](https://github.com/OpenRCT2/OpenRCT2/blob/develop/readme.md) · 資料確認日: 2026-10-11

</details>

### [OpenMW](https://github.com/OpenMW/openmw)

互換性と描画設定を改善した、Morrowind 向けの現代的なオープンソースエンジン。

原作・参考元: **The Elder Scrolls III: Morrowind** · エンジンの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://www.openmw.org) · [RemakeList を見る](https://remakelist.com/ja/remakes/openmw/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openmw-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** 公式ドキュメントを参照

**必要なもの:** Morrowind を遊ぶには原作を所有し、そのデータファイルを設定する必要があります。

**現在利用できるもの:** エンジンはダウンロードできますが、Morrowind を遊ぶには原作を所有し、データファイルを設定する必要があります。原作の MOD の一部は非対応のため、手持ちの構成を確認してください。

**コードのライセンス:** [GPLv3; some fonts separately licensed](https://github.com/OpenMW/openmw/blob/master/LICENSE)  
**作者:** OpenMW  
[公式ドキュメント](https://github.com/OpenMW/openmw/blob/master/README.md) · 資料確認日: 2026-10-11

</details>

### [OpenRA](https://github.com/OpenRA/OpenRA)

現代的な操作と三つの公式ゲーム MOD で、名作リアルタイム戦略ゲームを再構成。

原作・参考元: **Red Alert 1 / Command &amp; Conquer / Dune 2000** · ゲームの再構想  
[ダウンロード](https://www.openra.net/) · [RemakeList を見る](https://remakelist.com/ja/remakes/openra/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openra-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** 公式ドキュメントを参照

**必要なもの:** 原作のゲーム素材を使います。公式インストーラーは初回起動時に必要な素材を取得するか、原作ディスクから取り込めます。

**現在利用できるもの:** Windows、macOS、Linux 向けに配布されています。原作素材が必要ですが、プロジェクトによると初回設定で必要な素材を取得するか、原作ディスクから取り込めます。

**コードのライセンス:** [GPL-3.0-or-later (engine)](https://github.com/OpenRA/OpenRA/blob/bleed/COPYING)  
**作者:** OpenRA  
[公式ドキュメント](https://www.openra.net/about/) · 資料確認日: 2026-10-11

</details>

### [fheroes2](https://github.com/ihhub/fheroes2)

現代的な改善を加えた、デスクトップと Android 向けの Heroes of Might and Magic II エンジン再実装。

原作・参考元: **Heroes of Might and Magic II** · エンジンの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/ihhub/fheroes2/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/fheroes2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=fheroes2-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / Android

**開発状況:** 配布版あり · 原作またはデモデータが必要

**必要なもの:** 原作全体のデータ、または公式英語デモのデータが必要です。INSTALL.md に同梱のデモダウンロード手順があります。デモ素材で使えるのは、その許諾範囲の限られた内容のみです。

**現在利用できるもの:** 配布版には原作全体のデータ、または公式英語デモのデータが必要で、導入手順にデモの入手方法があります。デモの内容は限定的で、全編を遊ぶには適法に所有する原作素材が必要です。設定方法は環境によって異なります。

**コードのライセンス:** [GPL-2.0-or-later](https://github.com/ihhub/fheroes2/blob/master/LICENSE)  
**作者:** ihhub  
[公式ドキュメント](https://github.com/ihhub/fheroes2/blob/master/README.md) · 資料確認日: 2026-10-12

</details>

### [OpenXcom](https://github.com/OpenXcom/OpenXcom)

追加 MOD に対応した、初期の X-COM 二作品のデスクトップ再実装。

原作・参考元: **UFO: Enemy Unknown / Terror from the Deep** · ゲームの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/OpenXcom/OpenXcom/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/openxcom/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openxcom-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** デスクトップエンジン · 原作データが必要

**必要なもの:** UFO: Enemy Unknown または Terror from the Deep の未改変の原作データが必要です。Windows のインストーラーで所有する Steam 版から素材を抽出できます。

**現在利用できるもの:** デスクトップ版には、どちらかの原作の未改変データが必要です。Windows のインストーラーは所有する Steam 版から素材を抽出できます。追加 MOD には別の素材要件がある場合があります。

**コードのライセンス:** [GPL-3.0-or-later](https://github.com/OpenXcom/OpenXcom/blob/master/LICENSE.txt)  
**作者:** OpenXcom  
[公式ドキュメント](https://github.com/OpenXcom/OpenXcom/blob/master/README.md) · 資料確認日: 2026-10-12

</details>

### [VCMI](https://github.com/vcmi/vcmi)

デスクトップとモバイルに対応し、MODとマルチプレイを備えたオープンソースのHeroes IIIエンジン。

原作・参考元: **Heroes of Might and Magic III** · エンジンの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://vcmi.eu/download/) · [RemakeList を見る](https://remakelist.com/ja/remakes/vcmi/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=vcmi-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / Android / iOS

**開発状況:** 公開版 · 原作データが必要

**必要なもの:** 全編には、所有するHeroes III CompleteまたはShadow of Deathのデータが必要です。ランチャーからGOGのオフラインインストーラーや既存インストールを取り込めます。HD Edition単体では不足し、追加要素として使う場合もComplete/SoDが必要です。公式MOD一覧では内容限定のデモにも別途対応しています。

**現在利用できるもの:** 1.7.5版を公開。Windows、macOS、Linux、Android向けパッケージがあり、iOSはTestFlightまたはサイドロードを使用します。完全な互換性は保証されません。RemakeListでは実行していません。

**コードのライセンス:** [GPL-2.0-or-later code; VCMI-created assets CC-BY-SA 4.0; original game assets separate](https://github.com/vcmi/vcmi/blob/66fa496c6328a276c4eb14c0011b3a9d751dfac3/license.txt)  
**作者:** VCMI Team  
[公式ドキュメント](https://github.com/vcmi/vcmi/blob/66fa496c6328a276c4eb14c0011b3a9d751dfac3/docs/Readme.md) · 資料確認日: 2026-10-18

</details>

### [Julius](https://github.com/bvschaik/julius)

Caesar IIIのロジックを忠実に再実装し、原作の都市建設ゲームを現代のデスクトップやAndroidなどへ移植。

原作・参考元: **Caesar III** · ゲームの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/bvschaik/julius/releases/tag/v1.8.0) · [RemakeList を見る](https://remakelist.com/ja/remakes/julius/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=julius-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows · Linux · macOS · Android · Web（Emscripten）· PS Vita · Nintendo Switch

**開発状況:** 公開済み · 原作ゲームデータが必要

**必要なもの:** 所有するCD-ROM、GOG、Steam版Caesar IIIの完全なインストールデータを用意し、1.0.1.0へ更新してください。Juliusはそのデータフォルダーを使用し、セーブを書き込む権限を必要とします。コードのライセンスは原作素材を提供せず、その利用権も付与しません。

**現在利用できるもの:** 1.8.0版はWindows、Linux、macOS、Androidのほか、Vita、Switch、Emscripten向けパッケージを提供。ブラウザー版も設定と原作データが必要です。RemakeListでは実行していません。

**コードのライセンス:** [AGPL-3.0 · engine code; original Caesar III assets are separate](https://github.com/bvschaik/julius/blob/34d1ecd54befb845c0139b371fa8a0438210dac1/LICENSE.txt)  
**作者:** Bianca van Schaik and contributors  
[公式ドキュメント](https://github.com/bvschaik/julius/blob/34d1ecd54befb845c0139b371fa8a0438210dac1/README.md) · 資料確認日: 2026-10-18

</details>

### [CorsixTH](https://github.com/CorsixTH/CorsixTH)

現代のデスクトップ環境、高解像度、編集可能な病院経営キャンペーンに対応するTheme Hospitalのエンジン再実装。

原作・参考元: **Theme Hospital** · ゲームの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/CorsixTH/CorsixTH/releases/tag/v0.70.1) · [RemakeList を見る](https://remakelist.com/ja/remakes/corsixth/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=corsixth-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows · macOS · Linux · BSD

**開発状況:** 公開済み · 原作またはデモのデータが必要

**必要なもの:** 合法的に所有するTheme HospitalのCDまたはデジタル版のインストールデータを用意し、初回起動時にデータフォルダーを選択します。公式デモも利用できますが、1ステージのみで管理画面の大半はありません。エンジンのライセンスは原作素材の利用権を付与しません。

**現在利用できるもの:** バージョン0.70.1はWindowsとmacOS向けに公開され、LinuxではAppImageや各ディストリビューションのパッケージを利用できます。BSDにも対応。Mac版ではRtMidiによるハードウェアMIDIを無効化しています。RemakeListでは未実行です。

**コードのライセンス:** [MIT · engine code; Theme Hospital assets are separate](https://github.com/CorsixTH/CorsixTH/blob/master/LICENSE.txt)  
**作者:** CorsixTH team and contributors  
[公式ドキュメント](https://github.com/CorsixTH/CorsixTH/blob/master/README.md) · 資料確認日: 2026-10-19

</details>

### [Warzone 2100](https://github.com/Warzone2100/warzone2100)

1999年の3D戦略ゲームをコミュニティが継続開発。完全なキャンペーン、カスタマイズ可能なユニット、デスクトップ版のマルチプレイを提供します。

原作・参考元: **Warzone 2100 (1999)** · オープンソースでの継続開発  
[ダウンロード](https://wz2100.net/) · [RemakeList を見る](https://remakelist.com/ja/remakes/warzone2100/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=warzone2100-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows · macOS · Linux · Web

**開発状況:** 公開済み · デスクトップ版とブラウザー版

**必要なもの:** 原作の別途購入やディスクイメージは不要です。公式パッケージを使用してください。一部の環境ではキャンペーン動画を公式サイトから別途ダウンロードする必要があります。コード、ゲームデータ、各コンポーネントには、それぞれ明記されたライセンスが適用されます。

**現在利用できるもの:** 4.7.0はWindows、macOS、Linux向けに公開され、Mac版はIntelとApple siliconに対応。公式ブラウザー版ではキャンペーンとスカーミッシュを遊べますが、描画品質が低く、オンラインマルチプレイはありません。RemakeListでは未実行です。

**コードのライセンス:** [GPL-2.0-or-later and component licenses](https://github.com/Warzone2100/warzone2100/blob/master/COPYING)  
**作者:** Warzone 2100 Project  
[公式ドキュメント](https://github.com/Warzone2100/warzone2100/blob/master/README.md) · 資料確認日: 2026-10-19

</details>

### [ScummVM](https://github.com/scummvm/scummvm)

再実装されたゲームエンジンで、Monkey Island、Myst、Blade Runnerなどの名作アドベンチャーを現代のデバイスで動かせます。

原作・参考元: **名作アドベンチャーとRPG** · エンジンの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://www.scummvm.org/downloads/) · [RemakeList を見る](https://remakelist.com/ja/remakes/scummvm/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=scummvm-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / Android / iOS

**開発状況:** 公開済み · 互換性はゲームと対応環境により異なる

**必要なもの:** ScummVM自体にゲームは含まれません。商用作品の多くは、対応するゲームデータを自分で用意する必要があります。公式のFreeware GamesページではBeneath a Steel Skyなどの無料完全版を別途配布しており、Demosページの制限付き体験版とは異なります。選んだゲームをフォルダーに展開し、ランチャーでそのフォルダーを追加してください。各ゲームの配布条件はそれぞれに適用されます。

**現在利用できるもの:** 安定版2026.4.0はWindows、macOS、Linux向けに公開されています。2026年10月19日時点で、公式ダウンロードページではAndroidとiOSのビルドを旧版欄の2026.3.0として掲載しています。RemakeListではゲームを実行していません。

**コードのライセンス:** [GPL-3.0-or-later engine code; individual game data retains its own terms](https://github.com/scummvm/scummvm/blob/7d2709da5136866589f7602f5f5a7b17de03420e/COPYING)  
**作者:** ScummVM Team  
[公式ドキュメント](https://github.com/scummvm/scummvm/blob/7d2709da5136866589f7602f5f5a7b17de03420e/README.md) · 資料確認日: 2026-10-19

</details>

### [RigelEngine](https://github.com/lethal-guitar/RigelEngine)

ワイドスクリーン、滑らかな移動、クイックセーブ、改善されたゲームパッド対応を備えたDuke Nukem IIのネイティブエンジン。

原作・参考元: **Duke Nukem II** · エンジンの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/lethal-guitar/RigelEngine/releases/tag/v0.9.1) · [RemakeList を見る](https://remakelist.com/ja/remakes/rigelengine/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rigelengine-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** 公開済み · 保守段階

**必要なもの:** Duke Nukem IIのインストールデータからNUKEM2.CMPを用意してください。全4エピソードには登録版データが必要で、シェアウェアで遊べる内容は限定的です。NUKEM2.F1からNUKEM2.F5は任意のオープニング動画です。初回起動時にゲームデータのフォルダーを選択します。公式READMEにはシェアウェアのアーカイブと正規の完全版販売元へのリンクがあります。RemakeListは原作データを提供しません。

**現在利用できるもの:** 公式0.9.1パッケージにはWindows x64版ZIP、macOS x64版DMG、Linux x64版DEBがあります。Apple silicon向けには、リリースページから別の第三者製Macユニバーサルビルドを案内しています。READMEではWeb版を現在利用不可としています。RemakeListでは未実行です。

**コードのライセンス:** [GPL-2.0-or-later engine code; original Duke Nukem II data is separate](https://github.com/lethal-guitar/RigelEngine/blob/30afeff8f0b105eac77ee0a2fbd54b06e1a49b60/LICENSE.md)  
**作者:** Nikolai Wuttke and contributors  
[公式ドキュメント](https://github.com/lethal-guitar/RigelEngine/blob/30afeff8f0b105eac77ee0a2fbd54b06e1a49b60/README.md) · 資料確認日: 2026-10-19

</details>

### [OpenLoco](https://github.com/OpenLoco/OpenLoco)

Chris Sawyer’s Locomotionを現代のC++で再実装し、運輸会社の経営シミュレーションを現在のデスクトップ環境で楽しめるようにしたプロジェクト。

原作・参考元: **Chris Sawyer’s Locomotion** · ゲームの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://openloco.io/download/) · [RemakeList を見る](https://remakelist.com/ja/remakes/openloco/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openloco-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows x86/x64 · Linux x64 · macOS Apple silicon

**開発状況:** 公開済み · 原作ゲームのデータが必要

**必要なもの:** Steam版やGOG版など、合法的に所有するLocomotionのインストールデータを用意してください。原作ファイルはアプリと別に保管します。OpenGraphicsの追加後も、資料に記載された原作データの要件は変わりません。MITライセンスは商用ゲーム素材の利用権を付与しません。

**現在利用できるもの:** v26.09ではWindows 32/64ビット版ZIP、Linux x86-64版AppImage、macOS arm64ネイティブアプリを提供しています。Mac版はApple siliconが必要で、署名および公証はされていません。RemakeListではこれらのビルドを実行していません。

**コードのライセンス:** [MIT · engine code; original game assets are separate](https://github.com/OpenLoco/OpenLoco/blob/v26.09/LICENSE)  
**作者:** OpenLoco developers  
[公式ドキュメント](https://github.com/OpenLoco/OpenLoco/blob/v26.09/README.md) · 資料確認日: 2026-10-19

</details>

### [The Force Engine](https://github.com/TheForceEngine/TheForceEngine)

ワイドスクリーン、現代的なマウス操作、クイックセーブ、従来のコミュニティ製MODに対応した環境でDark Forcesを遊べます。

原作・参考元: **Star Wars: Dark Forces** · エンジンの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/TheForceEngine/TheForceEngine/releases/tag/v1.22.420) · [RemakeList を見る](https://remakelist.com/ja/remakes/the-force-engine/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=the-force-engine-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / Linux · macOSはソースからビルド

**開発状況:** リリース済み · Dark Forcesに対応

**必要なもの:** 購入済みDark Forcesのインストールデータが必要です。エンジンはSteamとGOGのインストール先の検出を試みます。見つからない場合はSettings &gt; Gameでゲームデータのディレクトリを選択します。エンジンのライセンスに商用ゲームのファイルは含まれません。

**現在利用できるもの:** 公式1.22.420のWindows用ZIPを配布しています。現在のREADMEはLinuxではFlathubを推奨し、macOS向けにはソースからのビルド手順を案内しています。そのままインストールできる公式Macパッケージは確認できていません。

**コードのライセンス:** [GPL-2.0 engine code; original Dark Forces assets are separate](https://github.com/TheForceEngine/TheForceEngine/blob/master/LICENSE)  
**作者:** Lucius and The Force Engine contributors  
[公式ドキュメント](https://github.com/TheForceEngine/TheForceEngine#readme) · 資料確認日: 2026-10-19

</details>

### [OpenJazz](https://github.com/AlisterT/openjazz)

所有するゲームファイルや原作のシェアウェアデータを使い、現代のデスクトップ環境で初代Jazz Jackrabbitを再び遊べます。

原作・参考元: **Jazz Jackrabbit** · エンジンの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/AlisterT/openjazz/releases/tag/20260301) · [RemakeList を見る](https://remakelist.com/ja/remakes/openjazz/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=openjazz-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** リリース済み · 原作またはシェアウェアのデータが必要

**必要なもの:** 所有する初代Jazz Jackrabbitのインストールファイルか、原作のシェアウェアデータを用意してください。無料のエンジンに完全版のデータは含まれず、シェアウェアで遊べるエピソードは限られます。展開したゲームファイルを同じフォルダーに保管し、そのディレクトリをOpenJazzに指定します。

**現在利用できるもの:** 20260301リリースはWindows x86-64とLinux x86-64の実行ファイルを提供し、Linux版にはglibc 2.35が必要です。Mac Source Portsは別途、Apple siliconとIntelに対応する署名済みUniversal 2 Macアプリを配布しています。

**コードのライセンス:** [GPL-2.0-or-later engine code; Jazz Jackrabbit data is separate](https://github.com/AlisterT/openjazz/blob/master/doc/licenses.txt)  
**作者:** AJ Thomson, Carsten Teibes and contributors  
[公式ドキュメント](https://github.com/AlisterT/openjazz#readme) · 資料確認日: 2026-10-19

</details>

### [cnc-port](https://github.com/dk8827/cnc-port)

EAが公開したTiberian Dawnのコードを現代のシステムに移植します。

原作・参考元: **Command &amp; Conquer: Tiberian Dawn** · オープンソースでの継続開発  
[自分でビルド・ゲームデータも用意](https://github.com/dk8827/cnc-port#readme) · [RemakeList を見る](https://remakelist.com/ja/remakes/cnc-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cnc-port-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** macOS · Android デバッグ · iOS Simulator

**開発状況:** ソース移植・モバイルは開発対象

**必要なもの:** C&amp;C Gold Windows 95版のGDI/Nodデータを自分で用意します。作者は過去の無料配布版のコミュニティミラーを案内しますが、データは同梱しません。 コードのライセンスは原作ゲーム、画像、商用データの権利を許諾しません。

**現在利用できるもの:** ソースビルドが必要です。Macのメニューと戦術プレイは作者が確認し、AndroidデバッグAPKとiOS Simulatorの手順も記載しています。 モバイルのビルドやSimulator起動は実機プレイの検証ではありません。ミラーはEA運営ではありません。

**コードのライセンス:** [GPLv3 with additional EA terms. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/dk8827/cnc-port#license-and-notice)  
**作者:** dk8827  
[公式ドキュメント](https://github.com/dk8827/cnc-port#readme) · 資料確認日: 2026-10-19

</details>

### [Generals Zero Hour for Mac, iPhone &amp; iPad](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad)

EA公開コードとGeneralsXに基づく、Apple向けGenerals: Zero Hourです。

原作・参考元: **Command &amp; Conquer: Generals — Zero Hour** · オープンソースでの継続開発  
[自分でビルド・ゲームデータも用意](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad#readme) · [RemakeList を見る](https://remakelist.com/ja/remakes/generals-apple/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=generals-apple-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Apple Silicon Mac / iPhone / iPad

**開発状況:** プレイ可能なソース移植・自己ビルド

**必要なもの:** 自分の製品版またはSteam版Zero Hourファイル、対応Apple Silicon Mac、指定されたビルドツールが必要です。 コードのライセンスは原作ゲーム、画像、商用データの権利を許諾しません。

**現在利用できるもの:** Macでソースビルドし、iPhone/iPadにはXcodeとApple署名も必要です。作者は戦役とスカーミッシュのプレイを報告しています。 EA公式モバイル版ではなくソースビルド方式です。ゲームデータと署名は別途必要です。

**コードのライセンス:** [GPLv3 with upstream terms. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad#readme)  
**作者:** ammaarreshi  
[公式ドキュメント](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad#readme) · 資料確認日: 2026-10-19

</details>

### [geow2](https://github.com/techknight/geow2)

geow2 — 6種類のモードとローカルマルチプレイ。 「Geometry Wars: Retro Evolved 2」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **Geometry Wars: Retro Evolved 2** · ゲームの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/techknight/geow2/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/geow2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=geow2-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS 11+ / Linux x64

**開発状況:** リリースパッケージがあります。

**必要なもの:** 自分が適法に取得したファイルを用意してください：Xbox Live Arcade · 584108FF · v0x102 · FFmpeg。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：Windows / macOS 11+ / Linux x64。リリースパッケージがあります。 使用するシステムに合う公式パッケージを選んでください。

**コードのライセンス:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/techknight/geow2/blob/main/LICENSE)  
**作者:** techknight  
[公式ドキュメント](https://github.com/techknight/geow2#readme) · 資料確認日: 2026-10-19

</details>

### [NOVA Swift](https://github.com/SirStig/NovaSwift)

NOVA Swift — 宇宙戦闘、物語、コミュニティのプラグイン。 「Escape Velocity Nova」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **Escape Velocity Nova** · エンジンの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://sirstig.github.io/NovaSwift/download.html) · [RemakeList を見る](https://remakelist.com/ja/remakes/nova-swift/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nova-swift-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** macOS / iOS / iPadOS / tvOS / Linux / Windows / Steam Deck

**開発状況:** ベータ版で、不具合や未検証項目が残ります。

**必要なもの:** 自分が適法に取得したファイルを用意してください：EV Nova · 原作のゲームデータ。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：macOS / iOS / iPadOS / tvOS / Linux / Windows / Steam Deck。ベータ版で、不具合や未検証項目が残ります。 使用するシステムに合う公式パッケージを選んでください。

**コードのライセンス:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/SirStig/NovaSwift/blob/main/LICENSE)  
**作者:** SirStig  
[公式ドキュメント](https://github.com/SirStig/NovaSwift#readme) · 資料確認日: 2026-10-19

</details>

### [PeonPad](https://github.com/chrissotraidis/peonpad)

PeonPad — タッチジェスチャーによるクラシックRTS操作。 「Warcraft II」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **Warcraft II** · エンジンの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/chrissotraidis/peonpad/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/peonpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=peonpad-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** iPadOS 16+

**開発状況:** 開発者プレビュー · 未署名IPA · 自分で署名が必要

**必要なもの:** 所有するWarcraft IIのファイルと、Wargusの抽出ツールを使えるMacまたはPCが必要です。完全なdata.Wargusフォルダーを作成し、署名済みアプリの導入後にコピーします。無料IPAはゲームデータを含まず、Blizzardの内容に関する権利も与えません。

**現在利用できるもの:** iPadOS 16以降向けの開発者プレビューです。GitHubのプレリリースにはWarcraft IIのデータを含まない未署名IPAがあります。自分で署名してインストールでき、アプリのコンパイルは任意です。MacかPCでWargusを使って所有するゲームからデータを抽出し、data.Wargusフォルダー全体をOn My iPad/PeonPad/data.Wargusへコピーします。アプリ内の取り込み機能、App Store版、TestFlightはありません。

**コードのライセンス:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/chrissotraidis/peonpad/blob/main/LICENSE)  
**作者:** chrissotraidis  
[公式ドキュメント](https://github.com/chrissotraidis/peonpad#readme) · 資料確認日: 2026-10-19

</details>

### [Pocket Wormhole](https://github.com/adamkulik/pocket-wormhole)

Pocket Wormhole — タッチ操作とftl.datのローカル取り込み。 「FTL: Faster Than Light」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **FTL: Faster Than Light** · エンジンの再実装  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/adamkulik/pocket-wormhole/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/pocket-wormhole/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pocket-wormhole-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Android 8+ · GLES 3.0

**開発状況:** プレイ可能または実験段階のプレビューです。

**必要なもの:** 自分が適法に取得したファイルを用意してください：Steam / GOG · ftl.dat · ~280 MB。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：Android 8+ · GLES 3.0。プレイ可能または実験段階のプレビューです。 異なるエンジン間のセーブ移行には制限があります。説明を読んでください。 使用するシステムに合う公式パッケージを選んでください。

**コードのライセンス:** [GPL-2.0-or-later applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/adamkulik/pocket-wormhole/blob/main/LICENSE)  
**作者:** adamkulik  
[公式ドキュメント](https://github.com/adamkulik/pocket-wormhole#readme) · 資料確認日: 2026-10-19

</details>

### [ra-port](https://github.com/dk8827/ra-port)

初代Red Alertを現代のシステムに移植します。原作データとソースビルドが必要で、ネット対戦は未実装です。

原作・参考元: **Command &amp; Conquer: Red Alert** · オープンソースでの継続開発  
[自分でビルド・ゲームデータも用意](https://github.com/dk8827/ra-port#readme) · [RemakeList を見る](https://remakelist.com/ja/remakes/ra-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ra-port-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** macOS / Linux / Android / iOS / iPadOS

**開発状況:** ソースビルド・原作が必要

**必要なもの:** 次の条件に合う合法的に取得した自分のファイルが必要です：Red Alert 1 · Allied + Soviet discs。商用ゲームの内容は別扱いで、RemakeListは提供しません。

**現在利用できるもの:** ソースビルドのみです。macOSとLinux、Android／iOSのローカルdebugビルドを文書化しています。Macアプリやモバイル製品版の配布、ネット対戦はありません。

**コードのライセンス:** [GPL-3.0 with EA additional terms](https://github.com/dk8827/ra-port#readme)  
**作者:** dk8827  
[公式ドキュメント](https://github.com/dk8827/ra-port#readme) · 資料確認日: 2026-10-19

</details>

### [Rugrats: Search for Reptar — Rust Port](https://github.com/toyz/rugrats)

PS1版Rugrats: Search for ReptarをRustで再実装するPC向けプロジェクトです。所有するディスクとソースビルドが必要です。

原作・参考元: **Rugrats: Search for Reptar** · ゲームの再実装  
[自分でビルド・ゲームデータも用意](https://github.com/toyz/rugrats#readme) · [RemakeList を見る](https://remakelist.com/ja/remakes/rugrats-rust-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rugrats-rust-port-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows

**開発状況:** ソースビルド・原作が必要

**必要なもの:** 次の条件に合う合法的に取得した自分のファイルが必要です：PlayStation USA · SLUS-00650 · owned disc。商用ゲームの内容は別扱いで、RemakeListは提供しません。

**現在利用できるもの:** 作者は全ステージからエンディングまでを記録しています。導入にはRustとソースビルドが必要で、すぐ使えるインストーラは確認していません。

**コードのライセンス:** [MIT OR Apache-2.0 authored code; original game data excluded](https://github.com/toyz/rugrats#readme)  
**作者:** toyz  
[公式ドキュメント](https://github.com/toyz/rugrats#readme) · 資料確認日: 2026-10-19

</details>

### [Rich4 Renew](https://github.com/iam567/rich4-renew-app)

PCとスマートフォン向けの非公式『Richman 4（大富翁4）』リメイク。高解像度で描き直したグラフィックを採用し、不動産取引、株式、カード、オンラインパーティープレイに対応。

原作・参考元: **Richman 4（大富翁4）** · ゲームの再実装  
[ダウンロード](https://github.com/iam567/rich4-renew-app/blob/main/README.md) · [RemakeList を見る](https://remakelist.com/ja/remakes/rich4-renew/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=rich4-renew-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Android / iOS

**開発状況:** v0.7.9 の情報を更新 · セットアップと素材の制限あり

**必要なもの:** ソースからの実行には、作者が別途提供する rich4-assets.tar が必要です。原作由来の素材、高解像度の描き直し、マップ、音声が含まれます。これらの素材は GPL の対象外で、作者により私的使用に限定されています。パッケージ作成スクリプトは素材をアプリに同梱しますが、配布パッケージの内容は独自に検査していません。無料でダウンロードできても、アートワークや原作素材の再配布が許可されるわけではありません。

**現在利用できるもの:** v0.7.9 は Windows ZIP、Intel・Apple Silicon 対応の Mac DMG、Android APK、未署名の iOS IPA を提供します。バックグラウンドから復帰した後、Jiqing Suiyue マップの放送局ニュースと音声が欠ける問題を修正します。iOS は自分での署名が必要です。公開ブラウザーデモは確認されていません。以前のパッケージ資料では macOS アプリは未公証、Android APK はデバッグ署名とされていましたが、今回の確認では v0.7.9 の署名やパッケージ内容を再検査していません。抽出された原作素材と描き直した画像は引き続き GPL の対象外です。作者の私的利用の説明は、原作権利者の許諾が得られていることを示しません。RemakeList ではインストールや実行を行っていません。

**コードのライセンス:** [GPL-3.0-or-later · code only](https://github.com/iam567/rich4-renew-app/blob/main/LICENSE)  
**作者:** iam567 (Liang)  
[公式ドキュメント](https://github.com/iam567/rich4-renew-app/blob/main/README.md) · 資料確認日: 2026-10-27

</details>

### [Supermodel-VK](https://github.com/Igloo-Garage/Supermodel-VK)

Sega Model 3 アーケードエミュレーター Supermodel の Vulkan 強化フォーク。無料・オープンソースで、ゲーム ROM は合法的に別途用意する必要がある。

原作・参考元: **Sega Model 3 アーケード／Supermodel** · emulator-enhancement-fork  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/Igloo-Garage/Supermodel-VK/releases/latest) · [RemakeList を見る](https://remakelist.com/ja/remakes/supermodel-vk/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=supermodel-vk-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10/11 x64、Linux x86-64、macOS 11 以降（Intel／Apple Silicon）

**開発状況:** 公開リリースあり。v0.9.2 は次期版のプレビューのみ。Linux と macOS は実環境での検証が比較的少ない。

**必要なもの:** ゲーム ROM は含まれない。Model 3 ROM の ZIP ファイルを合法的に別途用意する必要がある。コードの GPL ライセンスはゲームデータ、アート素材、商標には適用されない。

**現在利用できるもの:** Windows・Linux・macOS 向けの公開リリースは v0.9.0.3a-20261017。作者によると Linux／macOS は検証が少ない。macOS 版は未署名・未公証で、コマンドラインから ./supermodel で起動し、MoltenVK により性能が低下する場合がある。当サイトではインストール・動作確認を行っていない。カバーは作者による次期 v0.9.2 のゲーム内設定オーバーレイのプレビュー。v0.9.2 は未リリースで、画像内のすべての機能が現行版にあるとは限らない。

**コードのライセンス:** [GPL-3.0-or-later · emulator code](https://github.com/Igloo-Garage/Supermodel-VK/blob/master/Docs/LICENSE.txt)  
**作者:** Igloo-Garage · upstream: The Supermodel Team  
[公式ドキュメント](https://github.com/Igloo-Garage/Supermodel-VK/blob/master/README.md) · 資料確認日: 2026-10-20

</details>


<a id="ports"></a>

## 移植・互換性プロジェクト

### [D2R Mobile](https://github.com/jhaizhou-ops/d2r-mobile)

自分の Switch Diablo II: Resurrected と Reign of the Warlock のファイルを、Apple 機器、Android、HarmonyOS で使う互換レイヤーです。プラットフォームごとの準備が必要です。

原作・参考元: **Diablo II: Resurrected** · プラットフォーム互換レイヤー  
[自分でビルド・ゲームデータも用意](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) · [RemakeList を見る](https://remakelist.com/ja/remakes/d2r-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=d2r-mobile-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** iPhone／iPad／Apple Silicon Mac／Android ARM64／HarmonyOS NEXT

**開発状況:** v2.0.1 · 所有する Switch ファイルが必要 · 機器別の取り込み・ビルド

**必要なもの:** 合法的に購入した Switch の本編と Reign of the Warlock を本体表記1.0.34.0に更新し、ExeFS／RomFS を用意してください。ツールでは3.3.94012と表記されます。PC 版や他のコンソール版では代用できません。リソースは約5.6 GB で、古い Apple チップには自分のファイルから生成する約1 GB の追加テクスチャパックが必要です。Apple は A14／M1 以降が必要で、iOS 26以降と18〜25、macOS 26以降と15〜25で標準版または旧 API 版を選びます。Android は ARM64、Android 12以降、Vulkan 1.1 が必要です。HarmonyOS NEXT は開発者アカウント、署名ツール、自分で準備した実行用パックが必要です。

**現在利用できるもの:** v2.0.1 は Android APK、未署名の HarmonyOS HAP、2種類の iOS ビルド用 ZIP を提供します。Android はコンピューターで作成した取り込みパックも必要で、今回の修正では v2.0.0 のパックとセーブを引き継げます。HarmonyOS シェルと iOS の入力ファイルは変更されていません。HAP は自分の開発者証明書で再署名し、iOS ZIP はこのリリースのソースと組み合わせてアプリを作成・署名します。ZIP 自体は直接インストールできません。Mac は引き続きソースビルドが必要で、Mac 用添付ファイルはありません。オフライン専用でマルチプレイはありません。Android のタッチ操作には未完成の部分があり、一部 GPU ではシェーダーを省略したり効果が欠けたりします。取り込みには「すべてのファイルへのアクセス」が必要です。メモリ4 GB の Apple 端末は余裕が少なく、最低チップ要件を満たすだけでは動作確認済みとはいえません。サイドロードツールでの iOS 署名は未検証です。無料 Apple ID は7日ごとの再署名が必要で、iCloud 同期は使えません。ゲーム内容を含む自作パッケージを再配布しないでください。Apple TV はキャラクター選択までのプレビューであり、プレイ可能なプラットフォームとしては掲載していません。RemakeList ではビルド、インストール、プレイを行っていません。

**コードのライセンス:** [MIT covers project code; original game files and third-party components retain separate rights and licenses.](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/LICENSE)  
**作者:** joe jiang (@happyjoejiang)  
[公式ドキュメント](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/README.md) · 資料確認日: 2026-10-27

</details>

### [MW2 Recompiled](https://github.com/PaulCombal/mw2-recompiled)

Xbox 360 版 Modern Warfare 2 (2009) を Windows と Linux 向けに静的再コンパイルするプロジェクト。

原作・参考元: **Modern Warfare 2 (2009)** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/PaulCombal/mw2-recompiled/releases/tag/v0.8.1) · [RemakeList を見る](https://remakelist.com/ja/remakes/mw2-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mw2-recompiled-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows／Linux x64 · SSE4.2 · Vulkan 1.2

**開発状況:** v0.8.1 公開 · 原作データが必要

**必要なもの:** 合法的に入手した北米／欧州版 Xbox 360 バージョン1.0.557のディスク ISO を用意してください。ランチャーが検証後、Title Update 6 をダウンロードして適用します。x64 SSE4.2 対応 CPU、Vulkan 1.2、約8 GB のディスク容量、コントローラーが必要です。キーボードはメニュー操作のみです。実験的な PC カスタムマップの取り込みには、自分の PC 版の素材も必要です。

**現在利用できるもの:** v0.8.1 は Windows ZIP と Linux アーカイブを提供します。自分の ISO からインストールするには mw2-launcher を起動してください。通常の windows または linux パッケージを選びます。同じバージョンの -steam／-lan 添付ファイルは、旧ランチャーの更新用に置かれた同内容のコピーです。公開マッチメイキングやランク付きプレイリストは非対応で、カスタムマップはベータです。作者は原作ネットワークコードの既知の問題を修正したとしていますが、信頼できる相手とのプレイを引き続き推奨しています。RemakeList は独立したセキュリティ監査を行っていません。Steam SYSTEM LINK のゲームは他の Steam ユーザーに発見・参加される可能性があり、同じ中継サーバーや LAN のユーザーからも接続できます。全員が同じリリースを使用する必要があります。RemakeList ではインストールやプレイを行っていません。

**コードのライセンス:** [GPL-3.0-only](https://github.com/PaulCombal/mw2-recompiled/blob/master/LICENSE)  
**作者:** PaulCombal  
[公式ドキュメント](https://github.com/PaulCombal/mw2-recompiled/blob/master/README.md) · 資料確認日: 2026-10-27

</details>

### [Zelda 64: Recompiled](https://github.com/Zelda64Recomp/Zelda64Recomp)

ムジュラの仮面を静的再コンパイルし、現代的な操作と描画設定を備えたネイティブ版にするプロジェクト。

原作・参考元: **Majora’s Mask** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/Zelda64Recomp/Zelda64Recomp/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/zelda64-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=zelda64-recompiled-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / Linux / macOS

**開発状況:** 配布版あり · 原版素材が必要

**必要なもの:** 自分で用意した北米 N64 版ムジュラの仮面の ROM が必要。リポジトリと配布版にゲーム素材は含まれません。

**現在利用できるもの:** Windows、Linux、macOS 向け v1.2.2 配布版あり。対応する描画 API が必要。当サイトでは未実行です。

**コードのライセンス:** [GPL-3.0](https://github.com/Zelda64Recomp/Zelda64Recomp/blob/dev/COPYING)  
**作者:** Zelda64Recomp team  
[公式ドキュメント](https://github.com/Zelda64Recomp/Zelda64Recomp/blob/dev/README.md) · 資料確認日: 2026-10-14

</details>

### [MacNativeGames · Tears of the Kingdom](https://github.com/ly05010419/MacNativeGames)

自分の Switch ゲームから Apple シリコン Mac または iPhone/iPad 用の Tears of the Kingdom アプリをビルド。実験段階で、ローカルビルドと端末向け署名が必要です。

原作・参考元: **ゼルダの伝説 ティアーズ オブ ザ キングダム** · プラットフォーム互換レイヤー  
[自分でビルド・ゲームデータも用意](https://github.com/ly05010419/MacNativeGames#build-the-app) · [RemakeList を見る](https://remakelist.com/ja/remakes/zelda-totk-mac-research/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=zelda-totk-mac-research-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Apple シリコン Mac · macOS 26+；iPhone 14+ / iPad · iOS/iPadOS 26+

**開発状況:** 実験段階 · ローカルビルドと署名 · 正式版なし

**必要なもの:** 自分の本体から取り出した Switch v1.0.0 本体（XCI/NSP）、鍵、システムファイルが必要。Mac は別途 v1.1.2・v1.2.1・v1.4.3 更新（NSP/NSZ）も対応し、iOS は v1.4.3 のみ試験済み。Mac は Apple シリコン、macOS 26+、Metal 4、RAM 16 GB 推奨。入力ゲーム以外に本体ビルドで約 25 GB、APFS クローン不可なら約 17 GB 追加、更新込みの新規 Mac ビルドは約 40 GB。iOS は完全な Xcode 26+、iOS/iPadOS 26+、iPhone は 14 以降が必要で、メモリ上限拡張権限を保つ署名も必要。本体の新規作成は 45 GB、更新込みは 60 GB を確保。生成アプリには原作内容が入り、自分用に限ります。当サイトはゲーム、鍵、ファームウェア、署名アプリ、派生シェーダーを配布しません。

**現在利用できるもの:** ソースビルドが必要で正式 Releases はありません。作者は M4 Mac の試験と iPhone 14・A16 iPad での v1.4.3 プレイを報告しています。当サイトの実測ではありません。以前の Mac 約 90 FPS はキャッシュ準備後の観測で、全編クリアや安定速度の保証ではありません。iPhone 14 は約 4 GB を使用し、重い場面で約 8 分後に iOS に終了された例が 2 回あります。iOS で未収録のシェーダーがあると物体が欠け、Mac でも新場面で止まる場合があります。オンラインと amiibo は非対応です。

**コードのライセンス:** [Project code MIT · game rights and third-party licenses separate](https://github.com/ly05010419/MacNativeGames/blob/main/LICENSE)  
**作者:** Yong Li / liyong (@liyong2077)  
[公式ドキュメント](https://github.com/ly05010419/MacNativeGames/blob/b75be8cfa704df3701e86130c8ced268e79d6b11/README.md) · 資料確認日: 2026-10-20

</details>

### [Dusklight](https://github.com/TwilitRealm/dusklight)

高解像度、フレームレート設定、内蔵MODブラウザーに対応した『トワイライトプリンセス』のネイティブ移植。

原作・参考元: **ゼルダの伝説 トワイライトプリンセス** · 逆コンパイルに基づくプロジェクト  
[プログラムをダウンロード・ゲームデータは自分で用意](https://twilitrealm.dev/install/) · [RemakeList を見る](https://remakelist.com/ja/remakes/dusklight/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=dusklight-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / Linux / macOS / iOS / Android

**開発状況:** リリース済み · 原作素材が必要

**必要なもの:** 所有するゲームキューブ版またはWii版のディスクを自分でダンプする必要があります。韓国版Wiiディスクは非対応。プロジェクトは著作権で保護されたゲーム素材を提供しません。

**現在利用できるもの:** プロジェクトがデスクトップ・モバイル向けビルドを公開。iOSはサイドロードが必要です。D3D12、Vulkan 1.1以降、Metalを推奨。旧描画バックエンドは再現性と性能に制限があります。RemakeListでは未実行です。

**コードのライセンス:** [CC0-1.0 · project code; original game assets excluded](https://github.com/TwilitRealm/dusklight/blob/main/LICENSE.md)  
**作者:** Twilit Realm  
[公式ドキュメント](https://github.com/TwilitRealm/dusklight/blob/main/README.md) · 資料確認日: 2026-10-18

</details>

### [Mega Man X4 Recompiled](https://github.com/mstan/MegaManX4Recomp)

X と Zero の2人協力プレイをローカルまたはネットプレイで楽しめる、Mega Man X4 のネイティブ再コンパイル版です。現在のリリースは公開ベータ版です。

原作・参考元: **ロックマンX4** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/mstan/MegaManX4Recomp/releases/tag/v1.0.13) · [RemakeList を見る](https://remakelist.com/ja/remakes/mega-man-x4-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=mega-man-x4-recompiled-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows x64／Linux x86-64（glibc 2.38以降）

**開発状況:** 公開ベータ · 2人協力プレイ · 原作ディスクが必要

**必要なもの:** 変更されていない北米版 Mega Man X4（SLUS-00561）の .cue と .bin ディスクイメージを用意してください。MOD をすべて無効にしても必要です。パッチ済みディスク、音声差し替え版、再翻訳版には対応していません。OpenBIOS が含まれ、別途 BIOS を用意するかは任意です。原作コンテンツは MIT ライセンスの対象外です。

**現在利用できるもの:** v1.0.13 は Windows x64 ZIP と Linux x86-64 AppImage を提供し、シグマステージ2のボス扉間でのプレイヤー2のカメラを修正します。協力プレイには OpenGL が必要で、ネットプレイの両者は同じリリースを使用する必要があります。公開ベータ版には既知の問題が残り、独立カメラでの速度低下やオンラインのサインイン・起動に関する報告は調査中です。Linux には glibc 2.38以降が必要です。4人プレイの実験は含まれません。RemakeList ではインストールや実行を行っていません。

**コードのライセンス:** [MIT · original project code; dependencies retain their licenses](https://github.com/mstan/MegaManX4Recomp/blob/master/LICENSE)  
**作者:** Matthew Stanley  
[公式ドキュメント](https://github.com/mstan/MegaManX4Recomp/blob/master/README.md) · 資料確認日: 2026-10-27

</details>

### [Galaxy Android](https://github.com/OpenPort-Labs/Galaxy-Android)

タッチ操作、ゲームパッド、ウルトラワイド表示に対応した『スーパーマリオギャラクシー』の初期 Android ネイティブ移植。

原作・参考元: **スーパーマリオギャラクシー** · 逆コンパイルに基づくプロジェクト  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/OpenPort-Labs/Galaxy-Android/releases/tag/v0.0.4) · [RemakeList を見る](https://remakelist.com/ja/remakes/galaxy-android/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=galaxy-android-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Android 11以降 · ARM64 · Vulkan 1.0

**開発状況:** 公開リリース v0.0.4 · 原作データが必要

**必要なもの:** 合法的に吸い出した Wii Super Mario Galaxy のディスクイメージ（.rvz、.wbfs、.iso、.wia）を用意し、ローカルで展開・変換してください。動画なしで約2.5 GB、動画込みで約5 GB を確保してください。任意の Shield 由来素材は別の専有データであり、この掲載では提供しません。

**現在利用できるもの:** v0.0.4 は Android 11以降、ARM64、Vulkan 1.0、3 GB 以上のメモリが必要な公開 APK を提供します。作者は Vulkan 描画、実物のコントローラーの割り当て、タッチレイアウトの更新を挙げています。Vulkan 1.0 ドライバーがない端末は非対応です。作者は安定版としていますが、RemakeList は対応端末の範囲、持続的な性能、全編のプレイを検証しておらず、60 FPS を保証しません。カバーは pcddlXDDD による v0.0.1 のスクリーンショットを継続使用しており、今回のリリースのテスト画像ではありません。RemakeList ではインストールや実行を行っていません。

**コードのライセンス:** [GPL-3.0 · port code; original game assets excluded](https://github.com/OpenPort-Labs/Galaxy-Android/blob/main/LICENSE)  
**作者:** OpenPort Labs  
[公式ドキュメント](https://github.com/OpenPort-Labs/Galaxy-Android/blob/main/README.md) · 資料確認日: 2026-10-27

</details>

### [Tekken 3 Recompiled](https://github.com/FishB0nes98/Tekken3Recompiled)

ワイドスクリーン、衣装のカスタマイズ、任意の風間準の取り込みに対応する『鉄拳3』の Windows 向けハイブリッド再コンパイル・プレビュー。

原作・参考元: **鉄拳3** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/FishB0nes98/Tekken3Recompiled/releases/tag/v0.1.4) · [RemakeList を見る](https://remakelist.com/ja/remakes/tekken-3-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=tekken-3-recompiled-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows x64

**開発状況:** ハイブリッド再コンパイル・プレビュー · 自分のディスクが必要

**必要なもの:** 正当に所有する米国版『鉄拳3』SLUS-00402 の CUE/BIN が必要です。風間準の追加には、非結合形式の tektagt（World C1）と tekken3（World E1）のアーケード ZIP も必要です。なければ Include Jun Kazama を無効にできます。プロジェクトは製品版ゲームデータ、Sony BIOS、抽出済み素材を同梱せず、OpenBIOS を使用すると説明しています。コードのライセンスは元のゲーム素材の権利を付与しません。

**現在利用できるもの:** Windows x64 向け v0.1.4 Easy Setup プレビューを公開中。初回設定で固定バージョンのツールをダウンロードし、ローカルでビルドするため、インターネットと 4 GB 以上の作業領域が必要です。Linux と Steam Deck は未検証。RemakeList では未実行です。

**ソース公開・ライセンスによる制限あり:** [Source available under PolyForm Noncommercial 1.0.0; dependencies retain their licenses](https://github.com/FishB0nes98/Tekken3Recompiled/blob/main/LICENSE)  
**作者:** FishB0nes98  
[公式ドキュメント](https://github.com/FishB0nes98/Tekken3Recompiled/blob/main/README.md) · 資料確認日: 2026-10-18

</details>

### [DevilutionX](https://github.com/diasurgical/DevilutionX)

ワイドスクリーン、ゲームパッド、任意の操作改善を備え、現代のPCやスマートフォンでDiabloとHellfireを動かす移植版。

原作・参考元: **Diablo / Hellfire** · 逆コンパイルに基づくプロジェクト  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/diasurgical/DevilutionX/releases/tag/1.5.5) · [RemakeList を見る](https://remakelist.com/ja/remakes/devilutionx/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=devilutionx-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / Android / iOS

**開発状況:** 公開済み · 全編には原作データが必要

**必要なもの:** Diablo全編には、所有する原版CDまたは購入済みインストールから取得したDIABDAT.MPQが必要です。Hellfireにはhellfire.mpq、hfmonk.mpq、hfmusic.mpq、hfvoice.mpqも必要です。公式ガイドのspawn.mpqは内容を制限したシェアウェア版用で、全編を解放しません。中国語・日本語・韓国語の表示にはプロジェクトのfonts.mpqも必要です。

**現在利用できるもの:** 公式1.5.5版はWindows ZIP、ユニバーサルmacOS DMG、Linux版、Android APK、iOS IPAを提供。iOSはサイドロードが必要です。配布一覧と導入資料を確認しましたが、RemakeListではゲームを実行していません。

**ソース公開・ライセンスによる制限あり:** [Source available under Sustainable Use License 1.0; redistribution must be free of charge and non-commercial; original game assets excluded](https://github.com/diasurgical/DevilutionX/blob/0011dc9670c2093d5ab0084c1cdbeb086556563a/LICENSE.md)  
**作者:** diasurgical / DevilutionX contributors  
[公式ドキュメント](https://github.com/diasurgical/DevilutionX/blob/0011dc9670c2093d5ab0084c1cdbeb086556563a/README.md) · 資料確認日: 2026-10-18

</details>

### [ACFA-Port](https://github.com/sulphurs16/acfa-port)

手持ちのPS3データから作る、ARMORED CORE for Answerの非公式Windows移植です。

原作・参考元: **ARMORED CORE for Answer** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/sulphurs16/acfa-port/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/acfa-port/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=acfa-port-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows x64

**開発状況:** ランチャー公開済み・ローカルビルド

**必要なもの:** 米国版PS3 BLUS30187の自分のデータ、RPCS3、PS3システムソフトウェア4.93が必要です。更新01.35は任意です。 コードのライセンスは原作ゲーム、画像、商用データの権利を許諾しません。

**現在利用できるもの:** 作者のランチャーを取得し、手持ちのファイルを選ぶとローカルでゲームをビルドします。 ランチャー自体にゲームは含まれません。対応ファイルと初期設定が必要です。

**コードのライセンス:** [MIT. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/SulphurS16/ACFA-Port/blob/main/LICENSE)  
**作者:** SulphurS16  
[公式ドキュメント](https://github.com/sulphurs16/acfa-port#readme) · 資料確認日: 2026-10-19

</details>

### [AgePad](https://github.com/chrissotraidis/agepad)

手持ちのSteam Mac版Age of Empires II: Definitive Editionを使うiPad開発プレビューです。

原作・参考元: **Age of Empires II: Definitive Edition** · プラットフォーム互換レイヤー  
[自分でビルド・ゲームデータも用意](https://github.com/chrissotraidis/agepad#readme) · [RemakeList を見る](https://remakelist.com/ja/remakes/agepad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=agepad-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** iPad · 8 GB+ RAM

**開発状況:** 開発プレビュー・アカウントリスク未解決

**必要なもの:** Steam Mac版の所有、一致するゲームとSteamのバージョン、Mac、RAM 8GB以上・空き25GBのiPad、サイドロード署名が必要です。 コードのライセンスは原作ゲーム、画像、商用データの権利を許諾しません。

**現在利用できるもの:** 0.1.0プレビューではMacで作者の小さなパッケージに自分のゲームとSteamファイルを組み込み、署名してインストールします。 Steam互換性とアカウントの安全性は未確認です。オンライン対戦全体と作者のM2 iPad以外の端末は未検証です。

**コードのライセンス:** [MIT (AgePad code). The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/agepad#credits-and-license)  
**作者:** chrissotraidis  
[公式ドキュメント](https://github.com/chrissotraidis/agepad#readme) · 資料確認日: 2026-10-19

</details>

### [BearBirdPad](https://github.com/chrissotraidis/bearbirdpad)

BanjoRecompを使ったBanjo-KazooieのAppleモバイル向け統合です。

原作・参考元: **Banjo-Kazooie** · 静的再コンパイル  
[自分でビルド・ゲームデータも用意](https://github.com/chrissotraidis/bearbirdpad#readme) · [RemakeList を見る](https://remakelist.com/ja/remakes/bearbirdpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=bearbirdpad-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** iPhone / iPad · iOS 16+

**開発状況:** 自己ビルドの開発プレビュー

**必要なもの:** 自分のNTSC-U 1.0 ROM、XcodeのあるApple Silicon Mac、Appleの署名IDが必要です。 コードのライセンスは原作ゲーム、画像、商用データの権利を許諾しません。

**現在利用できるもの:** Apple Silicon MacでXcodeまたはPadMintを使い自分でビルド・署名します。リリースはレシピのみで、Appは含みません。 作者はiPhone 14とiPad Proで試験しています。実機コントローラーとライフサイクルの検証は未完了です。App Store/TestFlight配布はありません。

**コードのライセンス:** [GPL-3.0-or-later. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/bearbirdpad#legal-and-acknowledgements)  
**作者:** chrissotraidis  
[公式ドキュメント](https://github.com/chrissotraidis/bearbirdpad#readme) · 資料確認日: 2026-10-19

</details>

### [Birdman64](https://github.com/noahvl/birdman64)

自分の米国版ROMから作る、デスクトップ向けのネイティブPilotwings 64です。

原作・参考元: **Pilotwings 64** · 逆コンパイルに基づくプロジェクト  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/noahvl/birdman64/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/birdman64/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=birdman64-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / Linux · Android 実験版 · iOS 自己ビルド

**開発状況:** デスクトップ公開済み・モバイル実験中

**必要なもの:** 自分の米国版ROMと初回ビルド時のネット接続が必要です。ROMはダウンロードしません。 コードのライセンスは原作ゲーム、画像、商用データの権利を許諾しません。

**現在利用できるもの:** デスクトップ版は初回にローカルで準備します。Androidは実験版、iPhone/iPadは自己ビルドです。 モバイルの検証範囲は限定的で、インストール済み形式のiOS配布はありません。

**コードのライセンス:** [MIT (project code). The code license grants no rights to the original game, artwork or commercial data.](https://github.com/NoahVl/Birdman64#license)  
**作者:** NoahVl  
[公式ドキュメント](https://github.com/noahvl/birdman64#readme) · 資料確認日: 2026-10-19

</details>

### [Chupathingy](https://github.com/ChupathingyCE/chupathingyce)

Halo CEのデコンパイル成果とOpenCEに基づく、複数OS向けネイティブ移植です。

原作・参考元: **Halo: Combat Evolved** · 逆コンパイルに基づくプロジェクト  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/ChupathingyCE/chupathingyce/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/chupathingy/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=chupathingy-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / Android

**開発状況:** 公開済み・Xbox版データが必要

**必要なもの:** 自分のXbox版ディスクイメージまたはマップが必要です。追加のPC版・Custom Editionマップは別フォルダーで管理します。 コードのライセンスは原作ゲーム、画像、商用データの権利を許諾しません。

**現在利用できるもの:** Windows、Mac、Linux、Android版を公開しています。初回設定で自分のXboxマップを読み込みます。 PC版マップは中核のXboxマップの代わりになりません。通信互換性は相手のバージョン次第で、Androidには追加のメモリー制限があります。

**コードのライセンス:** [GPL-3.0-or-later from 0.8.0; earlier releases through 0.7.5d CC0. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/ChupathingyCE/chupathingyce#license)  
**作者:** Milenko (MrMilenko) and ChupathingyCE contributors; credits retain OpenCE and Halo decomp authors  
[公式ドキュメント](https://github.com/ChupathingyCE/chupathingyce#readme) · 資料確認日: 2026-10-19

</details>

### [CTRPad](https://github.com/chrissotraidis/ctrpad)

CTR NativeとCTR-ModSDKを使う、初代Crash Team RacingのApple向け統合です。

原作・参考元: **Crash Team Racing (1999)** · 逆コンパイルに基づくプロジェクト  
[自分でビルド・ゲームデータも用意](https://github.com/chrissotraidis/ctrpad#readme) · [RemakeList を見る](https://remakelist.com/ja/remakes/ctrpad/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ctrpad-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Apple Silicon Mac / iPhone / iPad

**開発状況:** 自己ビルド・Apple実機プレイ記録あり

**必要なもの:** 対応する北米NTSC-U版の単一トラックraw MODE2/2352 BIN、Apple Silicon Mac、Appleのビルド・署名ツールが必要です。 コードのライセンスは原作ゲーム、画像、商用データの権利を許諾しません。

**現在利用できるもの:** Apple Silicon MacのPadMintで自分のAppをビルドします。公開リリースはレシピで、インストール可能なAppではありません。 作者はMac、iPhone 14、iPad Proでプレイしていますが、実機コントローラー全体の検証は未完了です。App Store/TestFlight配布はありません。

**コードのライセンス:** [GPL-3.0. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/chrissotraidis/ctrpad#legal-and-acknowledgements)  
**作者:** chrissotraidis  
[公式ドキュメント](https://github.com/chrissotraidis/ctrpad#readme) · 資料確認日: 2026-10-19

</details>

### [Def Jam: Fight for NY Recompiled](https://github.com/vyanhursky/DefJamFFNY-recomp)

対応する北米版初代 Xbox の自分のデータから、Windows・Mac・Linux のネイティブ版 Def Jam: Fight for NY をビルドします。高解像度と最大4人のローカルプレイに対応し、ワイドスクリーンはベータ段階です。

原作・参考元: **Def Jam: Fight for NY** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/vyanhursky/DefJamFFNY-recomp/releases/tag/v0.12.1) · [RemakeList を見る](https://remakelist.com/ja/remakes/defjam-ffny-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=defjam-ffny-recompiled-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows x64（Direct3D 11）／Apple Silicon macOS／Linux x86-64／Steam Deck

**開発状況:** 公開リリース v0.12.1 · ローカルビルド · ワイドスクリーンはベータ

**必要なもの:** 作者の対応マニフェストに一致する、北米版初代 Xbox の自分のディスクイメージまたは展開済みデータを用意してください。PS2・GameCube 版では代用できません。セットアップが検証、再コンパイル、ビルドをローカルで行います。HD テクスチャの生成には追加の時間とディスク容量が必要です。コードライセンスは原作ゲームや画像の利用権を与えるものではありません。

**現在利用できるもの:** v0.12.1 は Windows x64、Apple Silicon macOS、Linux x86-64／Steam Deck 向けのセットアップツールを提供し、作成したキャラクターの顔画像やワイドスクリーンの HUD 位置を修正します。セットアップは自分のデータを検証し、ローカルでビルドします。既存の環境では Clean Update と再ビルドが必要です。作者によれば、セーブ、設定、MOD、テクスチャパックは保持されます。16:9／16:10 のワイドスクリーンはベータ、21:9／32:9 は実験段階で、マルチプレイはローカルのみです。ショップ読み込み時の停止、一部場面の不均一なフレーム間隔、既知のワイドスクリーンの問題が残ります。Steam Deck の音声と Story チュートリアルの性能は調査中です。macOS セットアップは未署名です。作者の回帰チェックは RemakeList による全編プレイの確認ではありません。RemakeList ではインストールや実行を行っていません。

**コードのライセンス:** [MIT project code; separate toolkit licenses. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/vyanhursky/DefJamFFNY-recomp#credits-and-licensing)  
**作者:** vyanhursky  
[公式ドキュメント](https://github.com/vyanhursky/DefJamFFNY-recomp#readme) · 資料確認日: 2026-10-27

</details>

### [DOAXVB Native PC Port](https://github.com/norain211/doaxvb-re)

自分のXbox版から作るDead or Alive Xtreme Beach VolleyballのネイティブPC移植です。

原作・参考元: **Dead or Alive Xtreme Beach Volleyball** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/norain211/doaxvb-re/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/doaxvb-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=doaxvb-native-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** プレイ可能なベータ・既知の描画問題

**必要なもの:** 自分の米国Xbox版ディスクイメージまたは展開データが必要です。生成したゲーム内容は自分のPCに保管します。 コードのライセンスは原作ゲーム、画像、商用データの権利を許諾しません。

**現在利用できるもの:** 作者のデスクトップ向けセットアップ手順に、自分の対応米国版ファイルを使います。 長時間プレイの記録がありますが、プールと描画の不具合が残ります。休暇終了後の継続は編集した14日目のセーブからの検証です。

**コードのライセンス:** [GPL-3.0-or-later. The code license grants no rights to the original game, artwork or commercial data.](https://github.com/norain211/doaxvb-re#license)  
**作者:** NoRain211  
[公式ドキュメント](https://github.com/norain211/doaxvb-re#readme) · 資料確認日: 2026-10-19

</details>

### [Forza Horizon 1: ReImagined](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined)

自分で用意した Xbox 360 Forza Horizon のファイルから、Windows・Linux のネイティブ移植をローカルでビルドします。コミュニティのオンラインサービス、車両チューニング、表示設定を備えます。

原作・参考元: **Forza Horizon** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined/releases/tag/v0.2.0) · [RemakeList を見る](https://remakelist.com/ja/remakes/forza-horizon-reimagined/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=forza-horizon-reimagined-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10/11 x64／Linux x86-64 · macOS はソースビルドの実験のみ

**開発状況:** v0.2.0 公開 · ローカルビルド · 実験的な VR

**必要なもの:** 合法的に入手した Xbox 360 Forza Horizon のディスクイメージ、Games on Demand パッケージ、または展開済みフォルダーを用意してください。Title Update 4 と DLC は別途必要です。Horizon Rally と 1000 Club には TU4 が必要です。約4 GB の空きメモリと15 GB のディスク空き容量を確保してください。Vulkan を使う場合は Vulkan 1.3 が必要で、Windows では Direct3D 12 も選べます。初期設定ではコンパイラーツールのダウンロードまたはインストールが必要です。

**現在利用できるもの:** v0.2.0 は Windows インストーラー、Linux x86-64 アーカイブ、Flatpak を提供します。ランチャーが自分のファイルからゲームをローカルで生成・コンパイルするため、更新後は一度再ビルドが必要です。macOS はソースビルドの実験段階で、Mac 用ダウンロードはありません。Steam Deck や低性能機器には性能上の制限があり、一部 GPU では描画不具合やクラッシュが発生します。作者の VR テストは Quest 3 と Linux WiVRn に限られ、Windows VR は未検証です。macOS ではレース全体、セーブの再読み込み、実物のコントローラーの検証が必要です。TU4 と基本版は別々のオンラインルームを使い、TU4 のセーブをそのまま基本版に戻すことはできません。RemakeList ではビルドやプレイを行っていません。

**コードのライセンス:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined/blob/main/LICENSE)  
**作者:** Dyotson  
[公式ドキュメント](https://github.com/FH1-ReImagined/ForzaHorizon1-ReImagined#readme) · 資料確認日: 2026-10-27

</details>

### [Gears of War 2 PC Port](https://github.com/santiquiroz/gears-of-war-2-pc-port)

自分の Xbox 360 Gears of War 2 ファイルを使用する非公式ネイティブ移植です。高解像度表示、画面分割、System Link 協力プレイを備えます。Android は実験段階で、キャンペーン全編の確認は済んでいません。

原作・参考元: **Gears of War 2** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/santiquiroz/gears-of-war-2-pc-port/releases/tag/v0.3.7) · [RemakeList を見る](https://remakelist.com/ja/remakes/gears-of-war-2-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gears-of-war-2-native-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10/11 x64（DirectX 12）／Android 10以降 ARM64（Vulkan、実験的）

**開発状況:** 公開リリース · キャンペーン確認は未完了 · Android は実験的

**必要なもの:** 合法的に入手した製品版 Xbox 360 Gears of War 2（タイトル ID 4D53082D）の ISO、または default.xex と GearGame を含む完全なフォルダーを用意してください。Windows での初回 ISO 展開には約8 GB が必要です。Android の取り込みではデータをアプリ領域にコピーするため、完全なデータをもう一組保存できる空き容量が必要です。RemakeList はゲームデータを提供しません。

**現在利用できるもの:** v0.3.7 は Windows 10/11 x64 ZIP と、実験的な Android 10以降 ARM64 APK を提供します。Windows には DirectX 12 対応 GPU、Android には Vulkan が必要です。更新では音声と字幕の言語を別々に選べます。作者が通してプレイしたのは Act 1 のみで、各章の短い確認は Acts 2〜5 の全編検証ではありません。Android の持続的な性能は発熱の影響を受けます。3人・4人協力プレイやインターネットプレイには未検証の場面が残り、全員が同じリリースを使用する必要があります。Windows ファイルは未署名のためブロックされる場合があります。作者によるスキャン結果は RemakeList の安全性認証ではありません。RemakeList ではビルド、インストール、実行を行っていません。

**コードのライセンス:** [BSD-3-Clause applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/santiquiroz/gears-of-war-2-pc-port/blob/master/LICENSE)  
**作者:** santiquiroz  
[公式ドキュメント](https://github.com/santiquiroz/gears-of-war-2-pc-port#readme) · 資料確認日: 2026-10-27

</details>

### [GoldenEye 007 PC Port](https://github.com/jkdansereau/goldeneye-pc-port)

GoldenEye 007 PC Port — ワイド画面、マウス操作、画面分割。 「GoldenEye 007」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **GoldenEye 007** · 逆コンパイルに基づくプロジェクト  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/jkdansereau/goldeneye-pc-port/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/goldeneye-007-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=goldeneye-007-pc-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / Linux / Steam Deck

**開発状況:** プレイ可能または実験段階のプレビューです。

**必要なもの:** 自分が適法に取得したファイルを用意してください：Nintendo 64 · GoldenEye 007 ROM · USA。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：Windows / Linux / Steam Deck。プレイ可能または実験段階のプレビューです。 PAL版と日本版ROMへの対応は未完成です。 使用するシステムに合う公式パッケージを選んでください。

**コードのライセンス:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/jkdansereau/goldeneye-pc-port/blob/main/LICENSE)  
**作者:** jkdansereau  
[公式ドキュメント](https://github.com/jkdansereau/goldeneye-pc-port#readme) · 資料確認日: 2026-10-19

</details>

### [Gravity Rush 2 Native Port](https://github.com/HayatoG/gr2_pc)

Gravity Rush 2 Native Port — PS4のサービスをデスクトップのVulkan描画に対応。 「Gravity Rush 2」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **Gravity Rush 2** · プラットフォーム互換レイヤー  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/hayatog/gr2_pc/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/gravity-rush-2-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gravity-rush-2-native-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Linux · Vulkan

**開発状況:** プレイ可能または実験段階のプレビューです。

**必要なもの:** 自分が適法に取得したファイルを用意してください：PS4 · CUSA03694 · 01.11 · libSceNgs2.sprx。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：Linux · Vulkan。プレイ可能または実験段階のプレビューです。 Linuxのプレイ記録があります。Windowsでのネイティブ実行は未検証です。 セーブとオープンワールドの検証が続いています。 使用するシステムに合う公式パッケージを選んでください。

**コードのライセンス:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/HayatoG/gr2_pc/blob/main/port/LICENSE)  
**作者:** HayatoG  
[公式ドキュメント](https://github.com/HayatoG/gr2_pc#readme) · 資料確認日: 2026-10-19

</details>

### [inFAMOUS Second Son Native Port](https://github.com/HayatoG/iss_pc)

inFAMOUS Second Son Native Port — PS4のサービスと描画をデスクトップ向けに適応。 「inFAMOUS Second Son」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **inFAMOUS Second Son** · プラットフォーム互換レイヤー  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/hayatog/iss_pc/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/infamous-second-son-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=infamous-second-son-native-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Linux · Vulkan

**開発状況:** プレイ可能または実験段階のプレビューです。

**必要なもの:** 自分が適法に取得したファイルを用意してください：PS4 · CUSA00223 · 1.00 + 1.07。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：Linux · Vulkan。プレイ可能または実験段階のプレビューです。 フレームレートと描画に問題が残ります。 使用するシステムに合う公式パッケージを選んでください。

**コードのライセンス:** [GPL-2.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/HayatoG/iss_pc/blob/main/port/LICENSE)  
**作者:** HayatoG  
[公式ドキュメント](https://github.com/HayatoG/iss_pc#readme) · 資料確認日: 2026-10-19

</details>

### [LAS Recomp](https://github.com/peiikai/LASRecomp)

自分の Switch Link’s Awakening 1.0.0、1.0.1、1.1.0 のファイルからネイティブのデスクトップ移植をローカルでビルドします。ワイドスクリーンやランダマイザーを備え、現在もベータ段階です。

原作・参考元: **The Legend of Zelda: Link’s Awakening** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/peiikai/LASRecomp/releases/tag/beta_5.3) · [RemakeList を見る](https://remakelist.com/ja/remakes/las-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=las-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows x64／Apple Silicon macOS／Linux x64 · Linux ARM64 は実験的

**開発状況:** beta_5.3 · 不具合と未検証部分が残る

**必要なもの:** 合法的に入手した Switch Link’s Awakening 1.0.0、1.0.1、1.1.0 の exefs・romfs を用意し、そのフォルダーを選んでローカルでコンパイルしてください。Mac は Apple Silicon と macOS 15以降が必要です。Windows 10/11 と Linux x64 は AVX2、FMA、Vulkan 1.3、8 GB 以上のメモリ、約12 GB のセットアップ容量が必要です。ゲームファイルや鍵は提供されません。

**現在利用できるもの:** beta_5.3 は Windows ZIP、Mac DMG、Linux x86-64／ARM64 AppImage を提供します。原作バージョン1.0.0、1.0.1、1.1.0に対応し、初回起動時にローカルでコンパイルします。GitHub のプレリリース設定がオフでも、作者は明確にベータとしています。Linux ARM64 はビルドされていますが、実機では未検証です。クラッシュ、クリア不能なランダマイザーのシード、ワイドスクリーンの描画不具合が起こる可能性があり、ダンジョンの部屋シャッフルは特に実験的です。Intel Mac と古い Intel 内蔵 GPU は非対応です。Beta 5 より前のシード ID では生成結果が変わります。作者の Steam Deck・Mac のフレームレート報告は、すべての機器での保証ではありません。RemakeList ではビルドやプレイを行っていません。

**コードのライセンス:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/peiikai/LASRecomp/blob/main/LICENSE)  
**作者:** peiikai  
[公式ドキュメント](https://github.com/peiikai/LASRecomp#readme) · 資料確認日: 2026-10-27

</details>

### [Lets Go Recomp](https://github.com/raulzrrs/letsgo-recomp)

Lets Go Recomp — 探索、捕獲、トレーナー戦。 「Pokémon: Let’s Go, Eevee! / Pikachu!」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **Pokémon: Let’s Go, Eevee! / Pikachu!** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/raulzrrs/letsgo-recomp/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/lets-go-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=lets-go-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10–11 x64 · Vulkan 1.3 · AVX2

**開発状況:** プレイ可能または実験段階のプレビューです。

**必要なもの:** 自分が適法に取得したファイルを用意してください：Nintendo Switch · exefs + romfs · Eevee 1.0.0。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：Windows 10–11 x64 · Vulkan 1.3 · AVX2。プレイ可能または実験段階のプレビューです。 ゲーム全編は検証されていません。 主な検証対象はEevee 1.0.0です。Pikachuや更新版の検証範囲は限定的です。 使用するシステムに合う公式パッケージを選んでください。

**コードのライセンス:** [MIT applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/raulzrrs/letsgo-recomp/blob/main/LICENSE)  
**作者:** raulzrrs  
[公式ドキュメント](https://github.com/raulzrrs/letsgo-recomp#readme) · 資料確認日: 2026-10-19

</details>

### [Muscle March Recomp](https://github.com/tmcleroy/muscle-march-recomp)

Muscle March Recomp — スティック、タッチ、キーボード操作。 「Muscle March」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **Muscle March** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/tmcleroy/muscle-march-recomp/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/muscle-march-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=muscle-march-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10–11 / macOS 13+ Apple silicon / Linux / Android 8+ ARM64

**開発状況:** ベータ版で、不具合や未検証項目が残ります。

**必要なもの:** 自分が適法に取得したファイルを用意してください：WiiWare · USA WAD + 自分のWiiの共通鍵。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：Windows 10–11 / macOS 13+ Apple silicon / Linux / Android 8+ ARM64。ベータ版で、不具合や未検証項目が残ります。 公開された性能は限られた機器の結果です。 作者によると、配布物はデータを含まなくても変換後のゲームコードを含みます。 使用するシステムに合う公式パッケージを選んでください。

**コードのライセンス:** [GPL-3.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/tmcleroy/muscle-march-recomp/blob/main/LICENSE)  
**作者:** tmcleroy  
[公式ドキュメント](https://github.com/tmcleroy/muscle-march-recomp#readme) · 資料確認日: 2026-10-19

</details>

### [NSMB Wii Multiplayer Recompilation](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation)

NSMB Wii Multiplayer Recompilation — タッチ操作とスマートフォン・PC間のLANマルチプレイ。 「New Super Mario Bros. Wii」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **New Super Mario Bros. Wii** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/nsmb-wii-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nsmb-wii-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Android 11+ ARM64 / Windows 10–11 x64

**開発状況:** プレイ可能または実験段階のプレビューです。

**必要なもの:** 自分が適法に取得したファイルを用意してください：Wii · USA SMNE01 · リビジョン1。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：Android 11+ ARM64 / Windows 10–11 x64。プレイ可能または実験段階のプレビューです。 作者によると、配布物はデータを含まなくても変換後のゲームコードを含みます。 使用するシステムに合う公式パッケージを選んでください。

**コードのライセンス:** [GPL-3.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation/blob/main/LICENSE)  
**作者:** WitherBlitz  
[公式ドキュメント](https://github.com/WitherBlitz/NSMB-Wii-Multiplayer-Recompilation#readme) · 資料確認日: 2026-10-19

</details>

### [OpenSA2](https://github.com/kittycache9/OpenSA2)

OpenSA2 — ネイティブ実行環境、Androidタッチ操作、任意の調整。 「Sonic Adventure 2」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **Sonic Adventure 2** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/kittycache9/OpenSA2/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/opensa2/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=opensa2-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / Linux / Android

**開発状況:** プレイ可能または実験段階のプレビューです。

**必要なもの:** 自分が適法に取得したファイルを用意してください：PC · Sonic Adventure 2 (2012) · 実行ファイルと素材。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：Windows / Linux / Android。プレイ可能または実験段階のプレビューです。 ゲーム全編は検証されていません。 使用するシステムに合う公式パッケージを選んでください。 公式パッケージは再コンパイルしたゲームロジックと移植の実行環境を含みます。対応する2012年PC版の実行ファイルと素材は引き続きインストーラーに自分で渡す必要があり、単なる空のアプリではありません。

**コードのライセンス:** [GPL-3.0-only applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/kittycache9/OpenSA2/blob/main/LICENSE)  
**作者:** kittycache9  
[公式ドキュメント](https://github.com/kittycache9/OpenSA2#readme) · 資料確認日: 2026-10-19

</details>

### [Ottsel](https://github.com/chrissotraidis/ottsel)

Ottsel — タッチ、コントローラー、外部画面に対応。 「Jak and Daxter: The Precursor Legacy」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **Jak and Daxter: The Precursor Legacy** · 逆コンパイルに基づくプロジェクト  
[自分でビルド・ゲームデータも用意](https://github.com/chrissotraidis/ottsel#readme) · [RemakeList を見る](https://remakelist.com/ja/remakes/ottsel/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ottsel-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** iPadOS 18.5+ / macOS Apple silicon

**開発状況:** 開発者向けプレビューで、ビルドや署名が必要です。

**必要なもの:** 自分が適法に取得したファイルを用意してください：PS2 · USA SCUS-97124 · Black Label。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：iPadOS 18.5+ / macOS Apple silicon。開発者向けプレビューで、ビルドや署名が必要です。 iPadとMacでの実行記録がありますが、実機iPhoneのプレイは未検証です。 公式手順でローカルビルドしてください。

**コードのライセンス:** [ISC applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/chrissotraidis/ottsel/blob/main/LICENSE)  
**作者:** chrissotraidis  
[公式ドキュメント](https://github.com/chrissotraidis/ottsel#readme) · 資料確認日: 2026-10-19

</details>

### [Phantom Hourglass Recomp](https://github.com/dguillot-gh/phantom-hourglass-recomp)

Phantom Hourglass Recomp — 再コンパイルしたARM9とmelonDSハードウェアコアによる柔軟な画面配置。 「The Legend of Zelda: Phantom Hourglass」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **The Legend of Zelda: Phantom Hourglass** · 静的再コンパイル  
[自分でビルド・ゲームデータも用意](https://github.com/dguillot-gh/phantom-hourglass-recomp#readme) · [RemakeList を見る](https://remakelist.com/ja/remakes/phantom-hourglass-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=phantom-hourglass-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / Android

**開発状況:** プレイ可能または実験段階のプレビューです。

**必要なもの:** 自分が適法に取得したファイルを用意してください：Nintendo DS · USA · ROM SHA-1: 4c8f52dd719918bbcd46e73a8bae8628139c1b85 / 7e0d26d143992f1eee182b24f1abb9e7f038eacf。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：Windows / Android。プレイ可能または実験段階のプレビューです。 生成されたアプリやゲーム由来のビルドは個人用です。再配布しないでください。 公式手順でローカルビルドしてください。

**コードのライセンス:** [GPL-3.0 applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/dguillot-gh/phantom-hourglass-recomp/blob/main/LICENSE)  
**作者:** dguillot-gh  
[公式ドキュメント](https://github.com/dguillot-gh/phantom-hourglass-recomp#readme) · 資料確認日: 2026-10-19

</details>

### [Pinyon Shift](https://github.com/arcanite24/pinyon-shift)

Pinyon Shift — 設定ランチャー、描画設定、Steam Deckの導入経路。 「Forza Horizon」を記載の機器向けに移植する独立プロジェクトです。

原作・参考元: **Forza Horizon** · 静的再コンパイル  
[自分でビルド・ゲームデータも用意](https://github.com/arcanite24/pinyon-shift#readme) · [RemakeList を見る](https://remakelist.com/ja/remakes/pinyon-shift/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pinyon-shift-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / Linux / macOS Apple silicon / Android

**開発状況:** プレイ可能または実験段階のプレビューです。

**必要なもの:** 自分が適法に取得したファイルを用意してください：Xbox 360 · Forza Horizon ディスク · 任意の所有済みTU4/DLC。プロジェクトは無料ですが原作は別途必要です。当サイトはゲームファイル、鍵、すぐ遊べるパッケージを提供しません。

**現在利用できるもの:** 公式の利用経路：Windows / Linux / macOS Apple silicon / Android。プレイ可能または実験段階のプレビューです。 Androidは実験段階です。 公式手順でローカルビルドしてください。

**コードのライセンス:** [BSD-3-Clause applies to the project’s original code only; original game content and third-party components have separate rights.](https://github.com/arcanite24/pinyon-shift/blob/main/LICENSE)  
**作者:** arcanite24  
[公式ドキュメント](https://github.com/arcanite24/pinyon-shift#readme) · 資料確認日: 2026-10-19

</details>

### [Red Alert 2 Recomp](https://github.com/sp00nznet/redalert2-recomp)

自分の Red Alert 2／Yuri’s Revenge のファイルから、インストーラーでネイティブ版をローカルにビルドします。ワイドスクリーンなど現行環境向けの表示設定を追加します。OpenRA、RA2WEB、Vanguard とは別のプロジェクトです。

原作・参考元: **Red Alert 2 / Yuri’s Revenge** · 静的再コンパイル  
[自分でビルド・ゲームデータも用意](https://github.com/sp00nznet/redalert2-recomp/releases/tag/v0.1.3) · [RemakeList を見る](https://remakelist.com/ja/remakes/redalert2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=redalert2-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows x64／Linux x64／macOS ARM64

**開発状況:** インストーラー公開 · ローカルビルド · 原作ゲームが必要

**必要なもの:** game.exe 1.006 と gamemd.exe 1.001 を含む、自分の Steam／EA App（Origin）版のインストールを用意してください。インストーラーがファイルを検出してローカルで生成・ビルドし、必要に応じてビルドツールをインストールします。生成された原作由来のコードとデータはローカルに残ります。

**現在利用できるもの:** v0.1.3 は Windows x64、Linux x64、macOS ARM64 向けインストーラーを提供し、自分の原作ファイルからローカルで生成・ビルドします。一部の Windows 起動失敗と、Linux／macOS で終了後もプロセスが残る問題を修正します。作者の目安では初回ビルドに30〜60分と約6 GB が必要です。インストーラーは未署名のため OS にブロックされる場合があります。ローカルビルドが必要で、原作ゲームファイルは含まれません。作者のスクリプトによる確認はメニュー、スカーミッシュ、キャンペーン開始までで、RemakeList による全編プレイの検証ではありません。MIT はプロジェクト独自のコードに適用され、EA のゲームコードや素材には別の権利があります。RemakeList ではビルド、インストール、実行を行っていません。

**コードのライセンス:** [MIT for project-authored tooling only; EA game code and assets retain separate rights.](https://github.com/sp00nznet/redalert2-recomp/blob/main/LICENSE)  
**作者:** sp00nznet  
[公式ドキュメント](https://github.com/sp00nznet/redalert2-recomp#readme) · 資料確認日: 2026-10-27

</details>

### [Road Trip Recomp](https://github.com/silentsudin/RoadTripAdventure-recomp)

Road Trip／Choro Q HG2をPCとAndroidで遊ぶ移植で、ワイド画面とステート保存に対応します。初回に所有する米国版ディスクイメージを処理します。

原作・参考元: **Road Trip / Choro Q HG2** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/silentsudin/RoadTripAdventure-recomp/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/road-trip-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=road-trip-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Android

**開発状況:** プレビュー・原作が必要

**必要なもの:** 次の条件に合う合法的に取得した自分のファイルが必要です：Road Trip USA · SLUS-20398 · CUE/BIN/ISO/CHD。商用ゲームの内容は別扱いで、RemakeListは提供しません。

**現在利用できるもの:** Windows ZIP、Mac DMG、Android APKへのリンクがあります。作者は冒険とクイックレースの動作を記録しています。MacはApple Silicon、macOS 13以降とCommand Line Tools、Androidは12以降とVulkanが必要です。

**コードのライセンス:** [GPL-3.0; third-party notices separate](https://github.com/silentsudin/RoadTripAdventure-recomp#readme)  
**作者:** silentsudin  
[公式ドキュメント](https://github.com/silentsudin/RoadTripAdventure-recomp#readme) · 資料確認日: 2026-10-19

</details>

### [Silent Hill — Native PC Port](https://github.com/SlickAmogus/silent-hill-decomp)

PS1版の逆コンパイル成果を使うSilent Hillのネイティブ移植で、任意の画面改善を備えます。Windowsが中心で、所有するディスクデータが必要です。

原作・参考元: **Silent Hill** · 逆コンパイルに基づくプロジェクト  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/SlickAmogus/silent-hill-decomp/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/silent-hill-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=silent-hill-native-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows

**開発状況:** プレビュー・原作が必要

**必要なもの:** 次の条件に合う合法的に取得した自分のファイルが必要です：PlayStation · Silent Hill disc image · SLUS-00707 USA。商用ゲームの内容は別扱いで、RemakeListは提供しません。

**現在利用できるもの:** Windowsが中心で、作者は全編をプレイ可能としています。LinuxとMacは不安定な開発中、Android／iOSは初期ビルドです。GPLは移植層だけに適用されます。

**コードのライセンス:** [GPL-3.0 for port layer only; decompilation and Konami material not relicensed](https://github.com/SlickAmogus/silent-hill-decomp#readme)  
**作者:** Chris Hardin / KushAstronaut / SlickAmogus  
[公式ドキュメント](https://github.com/SlickAmogus/silent-hill-decomp#readme) · 資料確認日: 2026-10-19

</details>

### [SpeedBreaker](https://github.com/speedbreakerproject/speedbreaker)

自分の Xbox 360 Need for Speed: Most Wanted を現行機器で動かし、ワイドスクリーン、画面分割、表示設定を追加します。iPhone／iPad のサイドロードは実験段階で、Windows はベータ版です。

原作・参考元: **Need for Speed: Most Wanted (2005)** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/speedbreakerproject/speedbreaker/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/speedbreaker/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=speedbreaker-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Linux／SteamOS／Apple Silicon macOS／実験的な iOS・iPadOS／Windows ベータ

**開発状況:** v0.2.0 公開 · Windows ベータ · iOS サイドロードは実験的

**必要なもの:** 合法的に入手した北米 NTSC-U または欧州 PAL スペイン語版 Xbox 360 Most Wanted の ISO、XISO、展開済みフォルダーを用意してください。Title Update は使いません。他の地域版、Games on Demand、PC 版は非対応です。約7.2 GB を確保してください。Windows／Linux x64 は AVX2 と Vulkan 1.2、Mac は Apple Silicon と macOS 15以降が必要です。iOS／iPadOS は17以降、A15 相当以降のチップ、コントローラーまたはキーボード、自分でのサイドロード署名が必要です。

**現在利用できるもの:** 本体の v0.2.0 リリースは SteamOS／Linux x86-64、Steam Frame ARM64、Apple Silicon Mac、実験的な iOS IPA を提供します。Windows は別の v0.2.0-windows-beta.2 プレリリースを使用します。Android ビルドはありません。SteamOS の2種類のアーキテクチャは互換ではありません。作者の Windows ベータのテストは限られた Intel 内蔵 GPU 機器のみです。iOS IPA 添付ファイル自体は実機にインストールされておらず、作者のテストには Xcode 署名済みビルドを使用しています。サイドロードの権限やメモリ制限で動かない場合があります。Mac アプリは公証されておらず、macOS 15 は仮想マシンでのみテストされています。Steam Frame は VR ではなく平面画面の表示です。ARM64 パッケージは他の Linux 機器で未検証です。Steam Deck OLED は60 Hz に設定してください。LCD モデルは未検証です。どの機器でも一定のフレームレートを保証するものではありません。RemakeList では実行していません。

**コードのライセンス:** [Project-authored code is GPL-3.0-or-later; bundled libraries retain their own licenses, and original game content is excluded.](https://github.com/speedbreakerproject/speedbreaker#readme)  
**作者:** project(u) / SpeedBreakerProject  
[公式ドキュメント](https://github.com/speedbreakerproject/speedbreaker#readme) · 資料確認日: 2026-10-27

</details>

### [Renegade Squadron — PC](https://github.com/gtteancum/starwars-renegadesquadron-pc)

PSP版Renegade Squadronを現代的な操作でWindowsに移植します。米国版の自分のファイルが必要で、フレーム間隔に既知の問題があります。

原作・参考元: **Star Wars Battlefront: Renegade Squadron** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/gtteancum/starwars-renegadesquadron-pc/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/renegade-squadron-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=renegade-squadron-pc-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows

**開発状況:** プレビュー・原作が必要

**必要なもの:** 次の条件に合う合法的に取得した自分のファイルが必要です：PSP USA · ULUS10292 · PSP_GAME folder。商用ゲームの内容は別扱いで、RemakeListは提供しません。

**現在利用できるもの:** Windows配布へのリンクがあり、作者は11マップの戦闘を記録しています。フレーム間隔のばらつきは既知の問題です。

**コードのライセンス:** [MIT for framework/port, third-party notices separate](https://github.com/gtteancum/starwars-renegadesquadron-pc#readme)  
**作者:** gtteancum  
[公式ドキュメント](https://github.com/gtteancum/starwars-renegadesquadron-pc#readme) · 資料確認日: 2026-10-19

</details>

### [Super Mario Bros. Wonder Recomp](https://github.com/BelmanteGu/SuperMarioWonderRecomp)

Super Mario Bros. WonderをPCとAndroid向けに静的再コンパイルします。ソースビルドと自分のゲーム、鍵、ファームウェアが必要です。

原作・参考元: **Super Mario Bros. Wonder** · 静的再コンパイル  
[自分でビルド・ゲームデータも用意](https://github.com/BelmanteGu/SuperMarioWonderRecomp#readme) · [RemakeList を見る](https://remakelist.com/ja/remakes/super-mario-wonder-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=super-mario-wonder-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux / Android

**開発状況:** ソースビルド・原作が必要

**必要なもの:** 次の条件に合う合法的に取得した自分のファイルが必要です：Switch · Wonder 1.0.0 · 010015100B514000 · own keys + firmware。商用ゲームの内容は別扱いで、RemakeListは提供しません。

**現在利用できるもの:** 自分のゲーム、鍵とファームウェアからソースビルドします。作者はMac、Windows、LinuxとGalaxy S23を記録していますが、GPUの問題やWindowsのキャラクター選択後のクラッシュが残ります。

**コードのライセンス:** [MIT authored code; Nintendo game and derivatives excluded](https://github.com/BelmanteGu/SuperMarioWonderRecomp#readme)  
**作者:** Projeto Belmante / BelmanteGu  
[公式ドキュメント](https://github.com/BelmanteGu/SuperMarioWonderRecomp#readme) · 資料確認日: 2026-10-19

</details>

### [Super Street Fighter II Turbo HD Remix — PC Port](https://github.com/saulob/ssf2t-hd-remix-recompiled)

Xbox Live Arcade版Super Street Fighter II Turbo HD RemixのWindows向け移植です。指定バージョンの所有パッケージが必要で、オンライン対戦はありません。

原作・参考元: **Super Street Fighter II Turbo HD Remix** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/saulob/ssf2t-hd-remix-recompiled/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/ssf2t-hd-remix-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=ssf2t-hd-remix-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows

**開発状況:** プレビュー・原作が必要

**必要なもの:** 次の条件に合う合法的に取得した自分のファイルが必要です：Xbox Live Arcade · 584108A4 · 0.0.1.3 · STFS LIVE。商用ゲームの内容は別扱いで、RemakeListは提供しません。

**現在利用できるもの:** Windows ZIPが文書化されています。Linux／Steam Deckは実験的で実機未検証、オンライン対戦はありません。同梱ランチャーの指定版には明確なライセンスがありません。

**コードのライセンス:** [GPL-2.0-only authored code; TRG launcher explicit license absent at pinned revision](https://github.com/saulob/ssf2t-hd-remix-recompiled#readme)  
**作者:** saulob  
[公式ドキュメント](https://github.com/saulob/ssf2t-hd-remix-recompiled#readme) · 資料確認日: 2026-10-19

</details>

### [The Last Guardian — PC](https://github.com/hayatog/tlg_pc)

The Last GuardianのPC向け互換移植です。作者はLinuxを検証していますが、Windowsのゲーム内動作は未検証です。自分のPS4ファイルが必要です。

原作・参考元: **The Last Guardian** · プラットフォーム互換レイヤー  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/hayatog/tlg_pc/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/last-guardian-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=last-guardian-pc-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Linux / Windows

**開発状況:** プレビュー・原作が必要

**必要なもの:** 次の条件に合う合法的に取得した自分のファイルが必要です：PS4 · CUSA03627 / CUSA03745 · update 01.03 · own libSceNgs2.sprx。商用ゲームの内容は別扱いで、RemakeListは提供しません。

**現在利用できるもの:** 作者はLinuxで10分超のセッションを検証しています。Windowsは自動ビルドのみでゲーム内未確認、Macは計画中です。ゲームと必要なPS4システムファイルは自分で用意します。

**コードのライセンス:** [GPL-2.0 per port/LICENSE and README; game/firmware excluded](https://github.com/hayatog/tlg_pc#readme)  
**作者:** HayatoG  
[公式ドキュメント](https://github.com/hayatog/tlg_pc#readme) · 資料確認日: 2026-10-19

</details>

### [Tiberian Sun Recomp](https://github.com/sp00nznet/tiberiansun-recomp)

所有するTiberian SunとFirestormのインストールからネイティブ版を生成します。小規模戦と戦役の冒頭を確認した初期段階で、全編は未検証です。

原作・参考元: **Tiberian Sun / Firestorm** · 静的再コンパイル  
[自分でビルド・ゲームデータも用意](https://github.com/sp00nznet/tiberiansun-recomp#readme) · [RemakeList を見る](https://remakelist.com/ja/remakes/tiberian-sun-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=tiberian-sun-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / Linux

**開発状況:** ソースビルド・原作が必要

**必要なもの:** 次の条件に合う合法的に取得した自分のファイルが必要です：Steam · Tiberian Sun + Firestorm · Game.exe / Language.dll / MIX。商用ゲームの内容は別扱いで、RemakeListは提供しません。

**現在利用できるもの:** 初期のプレイ可能なソースビルドです。作者は小規模戦と四つの戦役の最初の任務を確認していますが、全編は未確認です。MacはWineを使います。

**コードのライセンス:** [MIT authored tooling; EA game and generated C excluded](https://github.com/sp00nznet/tiberiansun-recomp#readme)  
**作者:** sp00nznet  
[公式ドキュメント](https://github.com/sp00nznet/tiberiansun-recomp#readme) · 資料確認日: 2026-10-19

</details>

### [Wind Waker HD Android — Plus](https://github.com/Nycolazs/WindWakerHD-Android-Plus)

Wind Waker HDのAndroid向けフォークで、ポルトガル語とタッチ操作の調整を追加します。所有するWii U版が必要です。

原作・参考元: **The Legend of Zelda: The Wind Waker HD** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/Nycolazs/WindWakerHD-Android-Plus/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/wind-waker-hd-android-plus/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wind-waker-hd-android-plus-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Android

**開発状況:** プレビュー・原作が必要

**必要なもの:** 次の条件に合う合法的に取得した自分のファイルが必要です：Wii U · Wind Waker HD · WUD/WUX + own keys / own WUA。商用ゲームの内容は別扱いで、RemakeListは提供しません。

**現在利用できるもの:** Android APKへのリンクがあり、Android 11以降、ARM64とVulkanが必要です。公開されたゲーム画像はSnapdragon 865搭載Galaxy S20 FE 5Gで撮影されています。

**コードのライセンス:** [MPL-2.0 code; translation/third-party notices separate](https://github.com/Nycolazs/WindWakerHD-Android-Plus#readme)  
**作者:** Nycolazs  
[公式ドキュメント](https://github.com/Nycolazs/WindWakerHD-Android-Plus#readme) · 資料確認日: 2026-10-19

</details>

### [Wind Waker HD — Mods Fork](https://github.com/asadsi/wwhd-recomp-mods)

Wind Waker HDの非公式フォークで、任意の海上イベントや操縦できる海賊船を追加します。自分のゲームが必要で、協力プレイは実験段階です。

原作・参考元: **The Legend of Zelda: The Wind Waker HD** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/asadsi/wwhd-recomp-mods/releases) · [RemakeList を見る](https://remakelist.com/ja/remakes/wind-waker-hd-mods/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wind-waker-hd-mods-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / macOS / Linux

**開発状況:** プレビュー・原作が必要

**必要なもの:** 次の条件に合う合法的に取得した自分のファイルが必要です：Wii U USA/EUR · Wind Waker HD · own disc dump + keys / WUA。商用ゲームの内容は別扱いで、RemakeListは提供しません。

**現在利用できるもの:** デスクトップ配布を文書化し、Androidは自分でビルドします。Modは選択式で協力機能は実験段階、所有するWii Uゲームのデータが必要です。

**コードのライセンス:** [MPL-2.0 code; Nintendo assets excluded](https://github.com/asadsi/wwhd-recomp-mods#readme)  
**作者:** AsadSi / asadsi  
[公式ドキュメント](https://github.com/asadsi/wwhd-recomp-mods#readme) · 資料確認日: 2026-10-19

</details>

### [nxnative](https://github.com/seedds/nxnative)

所有する対応 Switch ゲームのファイルを使い、Mac で iPhone、iPad、Apple シリコン Mac 向けアプリをビルドします。互換性はゲームのプロファイルとビルドによって異なります。

原作・参考元: **Nintendo Switch ゲーム** · プラットフォーム互換レイヤー  
[自分でビルド・ゲームデータも用意](https://github.com/seedds/nxnative#pack-an-ipa) · [RemakeList を見る](https://remakelist.com/ja/remakes/nxnative/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=nxnative-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** iPhone / iPad · iOS / iPadOS 26 以降；Apple シリコン Mac · ローカルビルド

**開発状況:** ローカルビルドが必要 · 互換性は作者報告

**必要なもの:** 所有するゲームの NSP、必要な更新・DLC、自分の prod.keys を用意し、Xcode と Homebrew のある Mac でローカルビルドします。iPhone／iPad 向けは未署名の IPA を生成し、署名とサイドロードは別途行います。Apple シリコン Mac では Mac アプリの作成手順を使います。生成したパッケージにはゲーム由来のコードとリソースが含まれ、個人用であり再配布用ではありません。当サイトは商用ゲーム、鍵、すぐにインストールできるゲームパッケージを提供しません。ファイルの使用権は自分で確認してください。

**現在利用できるもの:** ビルド前に作者の最新のゲーム動作状況表と各ゲームのプロファイルを確認してください。Tears of the Kingdom は現在 iPhone でプレイ可能と報告されています。60 fps オプションには更新 1.4.3 が必要ですが、すべての端末でそのフレームレートを保証するものではありません。Mac アプリの作成には --platform mac-app を使い、Apple シリコン Mac の Finder から起動できます。iPhone での報告は Mac の互換性を証明するものではありません。

**コードのライセンス:** [MIT project code · game rights and third-party licenses separate](https://github.com/seedds/nxnative/blob/main/LICENSE)  
**作者:** seedds and contributors  
[公式ドキュメント](https://github.com/seedds/nxnative/blob/main/README.md) · 資料確認日: 2026-10-25

</details>

### [Zelda-Mobile · Tears of the Kingdom](https://github.com/OJZen/totk-mobile)

Tears of the Kingdom v1.4.3 を Apple シリコン上でネイティブ実行する実験的移植。自分のゲームとソースビルドが必要で、iPhone でのプレイは未検証です。

原作・参考元: **ゼルダの伝説 ティアーズ オブ ザ キングダム** · プラットフォーム互換レイヤー  
[自分でビルド・ゲームデータも用意](https://github.com/OJZen/totk-mobile/blob/main/docs/getting-started.md) · [RemakeList を見る](https://remakelist.com/ja/remakes/totk-mobile/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=totk-mobile-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Apple シリコン Mac、M1+ iPad、iPhone 15 Pro · 実験段階

**開発状況:** 実験段階 · ソースビルド · 正式リリースなし

**必要なもの:** 自分の本体から取り出した Switch のゲーム本体、v1.4.3 更新（.nsz）、対応する prod.keys が必要です。この版のみ対応。Apple シリコン Mac に完全な Xcode、コマンドラインツール、Homebrew、約 60 GB の空きが必要です。iPhone/iPad は iOS/iPadOS 26 以降、開発署名、デベロッパモード、USB、端末に約 25 GB の空きも必要。ゲーム、鍵、署名済みアプリ、派生シェーダーは配布しません。コードの許諾は任天堂のゲーム内容の権利を含みません。

**現在利用できるもの:** 実験的なソースビルドで正式 Releases はありません。作者は Apple シリコン Mac でのセーブ読み込みと場面のプレイを報告していますが、全編クリアは未検証です。M1 以降の iPad は原作解像度で 60 FPS を大きく下回り、実物のコントローラーも検証途中。iPhone 15 Pro は開発署名インストール、データ転送、キャッシュ済み起動でタイトル画面までのみ確認。プレイ、速度、メモリ、発熱は未測定で、iPhone 13 Pro を含む他機種は未テストです。新しい場面ではシェーダー生成で一時停止する場合があります。

**コードのライセンス:** [Original code: Apache-2.0 · reused components retain their own licenses](https://github.com/OJZen/totk-mobile/blob/main/LICENSE)  
**作者:** JZen (@JZennm)  
[公式ドキュメント](https://github.com/OJZen/totk-mobile/blob/510d95b8da159c0a7da467ad51b10a5a7c7ac133/README.md) · 資料確認日: 2026-10-20

</details>

### [Melee Unlocked](https://github.com/Hero88go/melee-unlocked)

Slippi のオンライン対戦と高リフレッシュレート表示に対応する Super Smash Bros. Melee のネイティブ PC 移植。NTSC 1.02 の ISO を自分で用意する必要があります。

原作・参考元: **Super Smash Bros. Melee（NTSC 1.02）** · プラットフォーム互換レイヤー  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/Hero88go/melee-unlocked/releases/tag/v0.9.57) · [RemakeList を見る](https://remakelist.com/ja/remakes/melee-unlocked/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=melee-unlocked-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10/11 x64 / Linux x86-64（AVX2、OpenGL 4.5）

**開発状況:** ベータ v0.9.57 · Linux は実験段階 · ISO の用意が必要

**必要なもの:** 正規に入手した、変更や圧縮のない Super Smash Bros. Melee NTSC 1.02 の ISO を用意してください。元のゲームデータは含まれず、コードのライセンスはゲーム素材には適用されません。

**現在利用できるもの:** v0.9.57 は Windows x64 版と実験段階の Linux x86-64 版を提供。Linux には AVX2 と OpenGL 4.5 が必要です。Static Recomp は Windows 専用です。RemakeList はインストールやプレイによる検証を行っていません。

**コードのライセンス:** [GPL-3.0-or-later · port code; third-party components keep their own terms.](https://github.com/Hero88go/melee-unlocked/blob/main/LICENSE)  
**作者:** Hero88go / Melee Unlocked contributors  
[公式ドキュメント](https://github.com/Hero88go/melee-unlocked#readme) · 資料確認日: 2026-10-26

</details>

### [Brawl Recompiled](https://github.com/josiahg2502-glitch/BrawlRecompiled)

静的再コンパイルによる Super Smash Bros. Brawl のネイティブ PC 移植。Windows と Linux に対応し、USA RSBE01 revision 1 のディスクイメージを自分で用意する必要があります。

原作・参考元: **Super Smash Bros. Brawl（Wii、USA RSBE01 revision 1）** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/josiahg2502-glitch/BrawlRecompiled/releases/tag/v0.4.0) · [RemakeList を見る](https://remakelist.com/ja/remakes/brawl-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=brawl-recompiled-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / Linux 64 ビット（glibc 2.35+、Vulkan）

**開発状況:** 開発中 · v0.4.0 · 元のディスクイメージが必要

**必要なもの:** 適法に入手した Brawl のディスクイメージを自分で用意する必要があります。対象は USA、RSBE01、revision 1 で、ISO・CISO・WBFS に対応。展開に約 7 GB 使用します。RVZ・WIA・GCZ・NKit は先に通常の ISO に変換してください。RemakeList はディスクイメージを提供しません。

**現在利用できるもの:** v0.4.0 は Windows と Linux のパッケージを提供。Linux は 64 ビット、glibc 2.35 以降、Vulkan ドライバーが必要です。作者は VS 対戦の動作を報告していますが、Classic と Subspace は冒頭のみのテストです。RemakeList はインストールやプレイによる検証を行っていません。

**コードのライセンス:** [GPLv3 · project code only; original game artwork and third-party components have separate rights and terms.](https://github.com/josiahg2502-glitch/BrawlRecompiled/blob/v0.4.0/wiicompiled/LICENSE)  
**作者:** JosiahG  
[公式ドキュメント](https://github.com/josiahg2502-glitch/BrawlRecompiled/blob/v0.4.0/README.md) · 資料確認日: 2026-10-25

</details>

### [Splinter Cell: Double Agent — Xbox Recomp](https://github.com/TGP482/SCDA-XBERecomp)

初代 Xbox 版 Splinter Cell: Double Agent の Windows ネイティブ移植。キーボード・マウス、解像度とフレームレートの調整、協力プレイに対応。自分の Xbox ゲームファイルが必要です。

原作・参考元: **Splinter Cell: Double Agent (original Xbox, 2006)** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/TGP482/SCDA-XBERecomp/releases/tag/V2) · [RemakeList を見る](https://remakelist.com/ja/remakes/scda-xbe-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=scda-xbe-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10+ x64 · Direct3D 12

**開発状況:** V2 リリース · 初代 Xbox のファイルが必要

**必要なもの:** 自分が適法に取得した初代 Xbox 版 Double Agent が必要です。配布版は ISO または展開済みファイルを利用でき、default.xbe、sc4_adv.xbe と Default、Media、adv フォルダーをまとめて配置します。ソースからのビルドには展開済みファイルが必要です。PC・Xbox 360 版のファイルでは代用できません。ゲーム素材は同梱されません。

**現在利用できるもの:** V2 の SCDA-XBERecomp.zip を展開し、自分の ISO または展開済みゲームファイルを assets に入れて SCDA.exe を実行します。初回起動時にゲームコードをローカルでコンパイルします。Windows 10+ x64、Direct3D 12 GPU、SSE4.2 と POPCNT 対応の 2 コア CPU、4 GB RAM、約 6 GB の空き容量が必要です。

**コードのライセンス:** [MIT for the project code; original game content and third-party components retain their own rights.](https://github.com/TGP482/SCDA-XBERecomp/blob/main/LICENSE)  
**作者:** TGP482  
[公式ドキュメント](https://github.com/TGP482/SCDA-XBERecomp#readme) · 資料確認日: 2026-10-25

</details>

### [P.T. for PC](https://github.com/LoreanXavier/pt-pc)

PS4 の体験版 P.T. をデスクトップに移植し、キーボード、コントローラー、フォトモード操作を追加。自分で用意した PS4 ゲームデータが必要です。

原作・参考元: **P.T. (PS4, 2014)** · プラットフォーム互換レイヤー  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/LoreanXavier/pt-pc/releases/tag/v1.0.8) · [RemakeList を見る](https://remakelist.com/ja/remakes/pt-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pt-pc-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10/11 x64 / Linux x86-64 / macOS 14+

**開発状況:** v1.0.8 · 初期の移植 · 原作ファイルが必要

**必要なもの:** 合法的に入手した PS4 P.T. のデータを用意してください。作者のテスト対象は米国版 CUSA01127 で、暗号化されたストア PKG は使用できません。移植版とインストーラーに原作のファイルは含まれません。

**現在利用できるもの:** v1.0.8 は Windows／Linux のインストーラーとポータブル版、Apple silicon／Intel Mac 版を提供。Linux は glibc 2.38+、描画は Vulkan 1.3 が必要で、macOS は同梱の MoltenVK を使用します。RemakeList では実行していません。 Intel Mac 版は Intel Mac 実機で未テストです。VR の確認はシミュレーション環境のみです。macOS では一部のエフェクトやアップスケーラーが利用できず、対応範囲はハードウェアによって異なります。

**コードのライセンス:** [MIT for project code; original game content and third-party components retain their own rights and terms.](https://github.com/LoreanXavier/pt-pc/blob/main/LICENSE)  
**作者:** LoreanXavier  
[公式ドキュメント](https://github.com/LoreanXavier/pt-pc/blob/main/README.md) · 資料確認日: 2026-10-26

</details>

### [GT4Recomp](https://github.com/moesuito/gt4-staticrecomp)

解像度、コントローラー、テクスチャパックを設定できる Gran Turismo 4 の Windows 移植版。対応する PS2 ディスクイメージを自分で用意する必要があります。

原作・参考元: **Gran Turismo 4 (PS2)** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/moesuito/gt4-staticrecomp/releases/tag/v1.3.0-rc6) · [RemakeList を見る](https://remakelist.com/ja/remakes/gt4-staticrecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gt4-staticrecomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10/11 x64 · Vulkan / Direct3D 12 / Direct3D 11

**開発状況:** v1.3.0-rc6 · プレリリース · 原作ファイルが必要

**必要なもの:** 合法的に入手した Gran Turismo 4 米国版 v2.00（SCUS-97328）の通常の ISO が必要です。Spec II には、自分で用意した Spec II 1.10 イメージが別途必要です。ゲームや MOD のファイルは提供されません。

**現在利用できるもの:** v1.3.0-rc6 は Windows インストーラーとポータブル ZIP を提供する公開テスト版で、正式な 1.3.0 ではありません。Vulkan がテスト済みの標準で、Direct3D 12／11 は新しい選択肢です。Linux／Android は計画段階です。 候補版のため、一部のライセンスデモやメニュー背景は再生されません。ステアリングホイールは非対応で、長時間のプレイは十分に検証されていません。Performance Mode は光源のフレアと太陽のまぶしさを無効にします。Spec II のウルトラワイド HUD に問題が残り、性能はハードウェアに依存します。

**コードのライセンス:** [MIT for original project code; the separate PCSX2 GS process is GPL-3.0-or-later. Original game and mod content have separate rights.](https://github.com/moesuito/gt4-staticrecomp/blob/main/LICENSE)  
**作者:** moesuito  
[公式ドキュメント](https://github.com/moesuito/gt4-staticrecomp/blob/main/README.md) · 資料確認日: 2026-10-26

</details>

### [God of War PSP Recomp](https://github.com/DrummingBird1/gow-psp-recomp)

自分で用意した米国版ディスクイメージから PSP の God of War 2作品をローカルで再構築する Windows ランチャー。現代的な表示・入力設定を備えています。

原作・参考元: **God of War: Chains of Olympus / Ghost of Sparta (PSP)** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/DrummingBird1/gow-psp-recomp/releases/tag/v1.3.1) · [RemakeList を見る](https://remakelist.com/ja/remakes/gow-psp-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=gow-psp-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows · Linux／Steam Deck は計画段階

**開発状況:** v1.3.1 · 初期の移植 · 原作ファイルが必要

**必要なもの:** 合法的に入手した米国版 PSP の CHD または ISO を用意してください。対象は Chains of Olympus（UCUS98653）と Ghost of Sparta（UCUS98737）です。原作ゲームデータは提供されません。

**現在利用できるもの:** v1.3.1 は Windows 用ランチャー ZIP を提供します。最初の Build では確認後にポータブルツールをダウンロードし、選択したゲームをローカルでコンパイルします。現行のリリース対象は Windows で、両作品とも全編通しの動作確認は完了していません。 プレビュー版で、後半のステージ、ボス、エンディングに不具合が残る可能性があります。Linux／Steam Deck は計画段階です。ランチャーは未署名で、ビルドツールは初回にダウンロードが必要です。自動のステージ巡回は全編クリアの検証にはなりません。

**コードのライセンス:** [GPL-3.0-or-later for project code; original game content and third-party components retain their own rights and terms.](https://github.com/DrummingBird1/gow-psp-recomp/blob/main/LICENSE)  
**作者:** DrummingBird1  
[公式ドキュメント](https://github.com/DrummingBird1/gow-psp-recomp/blob/main/README.md) · 資料確認日: 2026-10-26

</details>

### [PrimeRecomp](https://github.com/gminustwo/primerecomp)

マウス操作に対応する Metroid Prime Remastered の初期デスクトップ移植版。セットアップには、自分で抽出した Switch v1.0.0 のファイルが必要です。

原作・参考元: **Metroid Prime Remastered (Switch)** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/gminustwo/primerecomp/releases/tag/v0.0.2) · [RemakeList を見る](https://remakelist.com/ja/remakes/primerecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=primerecomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows x64／実験的な Linux x86-64

**開発状況:** v0.0.2 · 初期の移植 · 原作ファイルが必要

**必要なもの:** 合法的に入手した Switch 版 Metroid Prime Remastered v1.0.0 の更新を含まないファイルを、exefs と romfs フォルダーに抽出して用意してください。原作ゲームデータは含まれません。

**現在利用できるもの:** 確認できたリリースは v0.0.2 で、Windows ZIP と実験的な Linux AppImage があります。AVX2、Vulkan 1.3、Linux では glibc 2.35+ が必要です。main の README は v0.0.3 に言及していますが、今回の確認時点では未リリースでした。 初期ベータです。v0.0.2 のリリース説明によると、当時の Linux 版はソフトウェアレンダラーでのみテストされ、Linux GPU 実機や Steam Deck では未検証でした。後日の README の記述は、このパッケージを遡って検証するものではありません。未踏のエリアではクラッシュや停止が起こる可能性があり、RemakeList ではプレイを検証していません。

**コードのライセンス:** [MIT for project code; original game content and third-party components retain their own rights and terms.](https://github.com/gminustwo/primerecomp/blob/main/LICENSE)  
**作者:** gminustwo  
[公式ドキュメント](https://github.com/gminustwo/primerecomp/blob/main/README.md) · 資料確認日: 2026-10-26

</details>

### [Wario Land: Shake It! Native PC](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC)

キーボード／コントローラー入力と描画設定を備えた Wii 版 Wario Land の Windows 移植版。対応する米国版ゲームイメージを自分で用意する必要があります。

原作・参考元: **Wario Land: Shake It! (Wii)** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC/releases/tag/v0.1.0) · [RemakeList を見る](https://remakelist.com/ja/remakes/wario-land-shake-it-pc/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=wario-land-shake-it-pc-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10/11 x64 · Direct3D 12 / Vulkan

**開発状況:** v0.1.0 · プレリリース · 原作ファイルが必要

**必要なもの:** 合法的に入手した未改変の米国版 Wii Wario Land: Shake It!（RWLE01）を、対応ディスクイメージまたは抽出済みの sys/files フォルダーとして用意してください。プロジェクトはゲーム本体を提供しません。

**現在利用できるもの:** v0.1.0 はプレリリースの Windows ZIP です。Windows 10/11 x64 と Direct3D 12 または Vulkan 対応 GPU が必要です。RemakeList ではインストールやプレイを行っていません。 プレリリースで、未テストのエリア、描画の問題、クラッシュの可能性があります。高フレームレートの補間は実験的機能で、互換性や性能を保証するものではありません。

**コードのライセンス:** [GPL-3.0 for project code; original game content and third-party components retain their own rights and terms.](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC/blob/main/LICENSE)  
**作者:** santiagovalencia109  
[公式ドキュメント](https://github.com/santiagovalencia109/Wario-Land-Shake-It-Native-PC/blob/main/README.md) · 資料確認日: 2026-10-26

</details>

### [PGR4 Native](https://github.com/shaunsingh/pgr4-native)

ネイティブ Direct3D 12 レンダラーを備えた Project Gotham Racing 4 の再コンパイル版。自分で用意したゲームと Title Update #2 を使い、Windows または Proton 経由で動作します。

原作・参考元: **Project Gotham Racing 4 (Xbox 360)** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/shaunsingh/pgr4-native/releases/tag/v0.2.1) · [RemakeList を見る](https://remakelist.com/ja/remakes/pgr4-native/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=pgr4-native-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows x64／Linux・Steam Deck は Proton 経由

**開発状況:** v0.2.1 · 初期の移植 · 原作ファイルが必要

**必要なもの:** 合法的に入手して抽出した PGR4 ディスクと Title Update #2 のパッケージまたはファイルを用意してください。作者によると PAL と NTSC のディスク内容は一致します。原作ゲームデータは含まれません。

**現在利用できるもの:** v0.2.1 は Windows x64 ZIP を提供します。Linux と Steam Deck では Proton を使うため、この配布物は Linux ネイティブ実行ファイルではありません。RemakeList ではプレイや性能を検証していません。対応するゲームと更新データの組み合わせ、および描画設定が必要です。互換性やフレームレートはハードウェアと、使用する場合は Proton に依存します。Steam Deck 全般で一定のフレームレートを保証するものではありません。

**コードのライセンス:** [MIT for project code; original game content and third-party components retain their own rights and terms.](https://github.com/shaunsingh/pgr4-native/blob/main/LICENSE)  
**作者:** shaunsingh  
[公式ドキュメント](https://github.com/shaunsingh/pgr4-native/blob/main/README.md) · 資料確認日: 2026-10-27

</details>

### [Sky Recomp](https://github.com/Apolinario-coder/SkyRecomp)

キーボード／マウス操作と描画設定を備えた Skyward Sword HD の実験的なデスクトップ移植版。自分で用意した Switch v1.0.0 のゲームファイルが必要です。

原作・参考元: **The Legend of Zelda: Skyward Sword HD (Switch)** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/Apolinario-coder/SkyRecomp/releases/tag/v2.0.2) · [RemakeList を見る](https://remakelist.com/ja/remakes/skyrecomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=skyrecomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows / Linux / macOS

**開発状況:** v2.0.2 · 初期の移植 · 原作ファイルが必要

**必要なもの:** 合法的に入手した Switch 版 Skyward Sword HD v1.0.0 の、更新を含まないファイルを用意してください。原作ゲームファイルは提供されません。任意のビジュアルパックには各作者の個別の条件が適用されます。

**現在利用できるもの:** v2.0.2 は Windows、Linux、macOS のパッケージを提供します。Windows／Linux は対応する Vulkan 1.3 ハードウェア、x86 ビルドは AVX2 が必要です。macOS はプロジェクトの Metal バックエンドを使用します。全編を通じた安定性は確認されていません。 実験段階で、クラッシュ、メニューの停止、描画の違いは調査中です。高フレームレートモードは実験的機能で、ハードウェアに依存します。RemakeList ではこれらのパッケージをインストールしたりプレイしたりしていません。

**コードのライセンス:** [MIT for original code; LAS Recomp and third-party components retain their notices. Texture packs and presets have separate authors and terms.](https://github.com/Apolinario-coder/SkyRecomp/blob/main/LICENSE)  
**作者:** Apolinario-coder  
[公式ドキュメント](https://github.com/Apolinario-coder/SkyRecomp/blob/main/README.md) · 資料確認日: 2026-10-26

</details>

### [Madden NFL 08 Recompiled](https://github.com/anishchandra24/MaddenNFL08-Recompiled)

Xbox 360 版 Madden NFL 08 の初期 Windows 移植版。セットアップがツールチェーンをダウンロードし、自分で抽出したゲームファイルからローカルでビルドします。

原作・参考元: **Madden NFL 08 (Xbox 360)** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/anishchandra24/MaddenNFL08-Recompiled/releases/tag/v0.1.0) · [RemakeList を見る](https://remakelist.com/ja/remakes/madden-nfl08-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=madden-nfl08-recompiled-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10/11 x64 · ROV 対応 Direct3D 12

**開発状況:** v0.1.0 · プレリリース · 原作ファイルが必要

**必要なもの:** 合法的に入手した Xbox 360 版 Madden NFL 08（Title ID 4541081D）を抽出し、default.xex と他のゲームファイルを同じ場所に置いてください。README で指定された実行ファイルのリビジョンのみ対応します。

**現在利用できるもの:** v0.1.0 はプレリリースのセットアップ実行ファイルで、そのまま遊べるゲームバイナリではありません。対応ゲームファイル、インターネット、Git、C++ ツールを含む Visual Studio 2022 Community、約 10 GB のビルド領域が必要です。 高速な CPU と Direct3D 12 の Rasterizer Ordered Views（ROV）が必要です。作者の低性能 PC では試合を快適にプレイできず、テスト対象は2台のみです。シェーダーの引っ掛かり、一部の映像／音声の問題、オンラインサービスの非対応が残っています。

**コードのライセンス:** [GPL-3.0 for project code; original game content and third-party components retain their own rights and terms.](https://github.com/anishchandra24/MaddenNFL08-Recompiled/blob/main/LICENSE)  
**作者:** anishchandra24  
[公式ドキュメント](https://github.com/anishchandra24/MaddenNFL08-Recompiled/blob/main/README.md) · 資料確認日: 2026-10-26

</details>

### [CPS-2 Recomp](https://github.com/tmcleroy/cps2recomp)

CPS-2 と CPS-1 の非公式アーケード移植集。共通ランチャー、格闘ゲームのトレーニング機能、3人同時プレイのベルトスクロールアクションを備えます。所有するアーケード基板から用意した、指定バージョンの ROM セットが必要です。

原作・参考元: **Capcom CPS-2／CPS-1 アーケードゲーム** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/tmcleroy/cps2recomp/releases/tag/v0.4.0-beta.6) · [RemakeList を見る](https://remakelist.com/ja/remakes/cps2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=cps2-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10/11 x64 · macOS 13以降（Apple Silicon／Intel）· Linux x86_64／SteamOS

**開発状況:** v0.4.0-beta.6 · ベータ版 · 指定の原作 ROM セットが必要

**必要なもの:** 所有するアーケード基板から、指定されたリビジョンの ROM セットを用意してください。CPS-2 のゲームには対応する鍵ファイルも必要です。ランチャーはチェックサムを検証し、他の地域版やリビジョンを受け付けません。一部のセットには親セットも必要です。ゲームファイルや鍵ファイルは提供されません。

**現在利用できるもの:** v0.4.0-beta.6 は Windows x64、macOS、Linux x86_64 のアーカイブを提供します。macOS は Apple Silicon と Intel に対応し、SteamOS／Steam Deck では Linux パッケージを使用します。README には Linux ARM64 対応の記載がありますが、このリリースに ARM64 のダウンロードはありません。GitHub のプレリリース設定がオフでも、プロジェクトはベータ版です。確認済みの機種やコントローラーは限られます。作者は格闘ゲームをエンディングまで確認したとしていますが、新しく追加されたベルトスクロールアクションの確認範囲は、スクリプト操作による序盤のステージまでです。RemakeList が独自に全編をプレイして確認したものではありません。

**コードのライセンス:** [Project code is GPL-3.0-only; third-party components retain their own notices. This license does not grant rights to Capcom or other rights holders’ game code, ROMs, keys, music or artwork.](https://github.com/tmcleroy/cps2recomp/blob/main/LICENSE)  
**作者:** tmcleroy  
[公式ドキュメント](https://github.com/tmcleroy/cps2recomp/blob/main/README.md) · 資料確認日: 2026-10-27

</details>

### [Free Riders Recompiled](https://github.com/YuutaTsubasa/Free-Riders-Recompiled)

Kinect がなくてもコントローラーやキーボードで遊べる、Xbox 360 版 Sonic Free Riders の非公式移植です。自分で用意した北米／欧州版ディスクイメージからゲームデータを取り込みます。現在も開発中です。

原作・参考元: **Sonic Free Riders (Xbox 360)** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/YuutaTsubasa/Free-Riders-Recompiled/releases/tag/v0.10.35) · [RemakeList を見る](https://remakelist.com/ja/remakes/free-riders-recompiled/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=free-riders-recompiled-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows／Linux x64 · Android arm64 · 実験的な macOS Apple Silicon／iOS 対応

**開発状況:** v0.10.35 · 開発中 · 原作ディスクが必要

**必要なもの:** 合法的に入手した北米／欧州版 Xbox 360 Sonic Free Riders のディスクイメージ（.iso）を用意してください。ランチャーがそこからモデル、テクスチャ、音声、映像を取り込みます。作者によれば、配布物には再コンパイルしたプログラムが含まれますが、これらの原作ゲームデータは含まれません。プロジェクトの GPL ライセンスは SEGA のコンテンツを許諾するものではありません。

**現在利用できるもの:** v0.10.35 は Windows x64、Linux x64、Android arm64、macOS arm64、iOS IPA のパッケージを提供します。Windows 10/11 と Linux には AVX が必要です。描画には Windows で Direct3D 12 または Vulkan 1.2、Linux で Vulkan 1.2 が必要です。Android は Android 9以降、Vulkan 1.1、ゲームのインストール用に約2 GB の空き容量が必要で、Android 10以降専用の APK もあります。Apple 向けは Apple Silicon 搭載の macOS 13.3以降、またはサイドロード可能な iOS 16.3以降が対象です。開発中のため、多くのモードは未検証で、Android の性能は端末に依存します。Apple 対応は実験段階です。README の動作要件には M1 でのレース速度低下や iOS 実機での未検証が残る一方、その後の更新履歴には Mac の性能改善や iOS の修正が記載されています。現時点の互換性には独立した確認が必要です。Kinect v2 や幅広い環境でのオンラインプレイも検証が限られています。

**コードのライセンス:** [Project code is GPL-3.0-or-later. The original game’s code and data remain SEGA’s and are outside that grant; third-party components and models retain their separate licenses.](https://github.com/YuutaTsubasa/Free-Riders-Recompiled/blob/main/COPYING)  
**作者:** YuutaTsubasa  
[公式ドキュメント](https://github.com/YuutaTsubasa/Free-Riders-Recompiled/blob/main/README.md) · 資料確認日: 2026-10-27

</details>

### [James Pond 2 Recompiled](https://github.com/griches/JamesPond2RobocodRecomp)

ワイドスクリーン、セーブスロット、滑らかな画面表示を追加した Amiga 版 James Pond 2 のコミュニティ移植です。自分で用意した対応 Kixx 版ディスクイメージ、または WHDLoad インストールデータが必要です。

原作・参考元: **James Pond 2: Codename RoboCod (Amiga)** · 静的再コンパイル  
[プログラムをダウンロード・ゲームデータは自分で用意](https://github.com/griches/JamesPond2RobocodRecomp/releases/tag/v1.0.0) · [RemakeList を見る](https://remakelist.com/ja/remakes/james-pond-2-recomp/?utm_source=github&utm_medium=repository&utm_campaign=awesome-remakelist&utm_content=james-pond-2-recomp-ja)

<details>
<summary>必要条件とスクリーンショット</summary>

**対応環境:** Windows 10/11 x64 · macOS 13以降（Apple Silicon／Intel）· Linux x86_64／Steam Deck · PS5 自作ソフト環境

**開発状況:** デスクトップ v1.0.0 · PS5 v1.0.2 · 原作ディスクが必要

**必要なもの:** 合法的に入手した Amiga Kixx 再発売版の標準 .adf ディスクイメージ、または対応する WHDLoad インストールデータを用意してください。.adf は gzip 圧縮した .adz や .zip 内のファイルでも利用できます。初期 Millennium 版のコピー保護付きディスク、拡張 ADF、.dms、.ipf には対応していません。ここでは原作ディスクのダウンロードを提供していません。

**現在利用できるもの:** Windows、macOS、Linux のデスクトップ向けダウンロードは v1.0.0 です。Steam Deck では Linux アーカイブを使用します。PS5 には別途 v1.0.2 があり、すでに自作ソフトを実行できる本体が必要です。v1.0.2 のリリースノートは、他のプラットフォームが v1.0.0 のままであることを明記しています。初期の公開版であり、別の版を所有していても、そのディスク形式が対応しているとは限りません。PS5 版は自作ソフト環境向けで、通常のコンソールストア配信ではありません。RemakeList ではインストールやプレイ、全編の互換性の独自検証を行っていません。

**コードのライセンス:** [The project’s own code is GPL-3.0. SDL3, Musashi, fonts and other dependencies retain their separate licenses; the original game’s code, artwork and music are not granted under the project license.](https://github.com/griches/JamesPond2RobocodRecomp/blob/main/LICENSE)  
**作者:** griches  
[公式ドキュメント](https://github.com/griches/JamesPond2RobocodRecomp/blob/main/README.md) · 資料確認日: 2026-10-27

</details>

## このリストについて

このリストは、RemakeList で公開済みの情報から生成しています。追加、変更、削除は、まずサイト側で確認し、その後 GitHub へ自動同期します。プロジェクトの説明を別々に管理することはありません。 [データと同期について](docs/data.md)

代替ツール、再実装、移植は、それぞれ異なる関係を表します。コードのライセンスは原作の素材を利用する許可ではありません。互換性や性能の説明は引用元の資料に基づいており、RemakeList による動作確認を意味しません。このリポジトリではゲームデータ、鍵、インストールパッケージを配布していません。ソースが公開されていても、ライセンスに制限があり、オープンソースではないプロジェクトも含みます。

プロジェクトの推薦や情報の訂正は Issue からお知らせください。必要な出典については投稿ガイドをご覧ください。自動生成されるプロジェクトデータと README の項目は、RemakeList を通じて更新します。 [プロジェクトを推薦](CONTRIBUTING.md)

リストの独自文章は CC BY 4.0、生成スクリプトは MIT ライセンスです。各プロジェクトと第三者のコンテンツには、それぞれのライセンスが適用されます。LICENSE と NOTICE.md をご覧ください。

[CC BY 4.0](LICENSE) · [MIT](scripts/LICENSE) · [NOTICE](NOTICE.md)
