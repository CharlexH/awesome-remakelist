# SPDX-License-Identifier: MIT
"""Generate the English and Chinese lists without third-party dependencies."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = {
    'creative': ('Creative tools', '设计与创作工具'),
    'everyday': ('Everyday tools and interface recreations', '办公工具与界面再现'),
    'classic_games': ('Classic game engines and recreations', '经典游戏引擎与重制'),
    'ports': ('Ports and compatibility projects', '移植与兼容项目'),
}
RELATIONS = {
    'independent_functional_alternative': ('Functional alternative', '独立功能平替'),
    'workflow-reimplementation': ('Workflow reimplementation', '工作流重实现'),
    'web-reimplementation': ('Web reimplementation', '网页重实现'),
    'interface-recreation': ('Interface recreation', '界面再现'),
    'game-reimplementation': ('Game reimplementation', '游戏重实现'),
    'engine-reimplementation': ('Engine reimplementation', '引擎重实现'),
    'game-reimagining': ('Reimagining', '玩法再创作'),
    'open-source-continuation': ('Open-source continuation', '开放源码续作'),
    'static-recompilation': ('Static recompilation', '静态重编译'),
    'platform-compatibility-reimplementation': ('Platform compatibility', '平台兼容层'),
    'decompilation': ('Decompilation-based port', '基于反编译的移植'),
}
STARTS = {
    'download': ('Download', '下载'), 'browser': ('Browser', '浏览器体验'),
    'hosted_signup_or_self_host': ('Sign up / self-host', '注册体验／自托管'),
    'download_with_original_assets': ('Download + own files', '下载程序＋自备文件'),
    'build_with_original_assets': ('Build + own files', '自行构建＋自备文件'),
    'development_build': ('Build', '自行构建'),
}


def clean(text):
    return text.replace('\n', ' ').replace('[', '\\[').replace(']', '\\]').replace('<', '&lt;').replace('>', '&gt;')


def tracked(url, content):
    return url + '?' + urlencode({'utm_source': 'github', 'utm_medium': 'repository', 'utm_campaign': 'awesome-remakelist', 'utm_content': content})


def render(data, chinese=False):
    lang = 1 if chinese else 0
    suffix = 'zh' if chinese else 'en'
    if chinese:
        head = '''# Awesome RemakeList

软件重实现、经典游戏引擎、跨平台移植，以及明确标注的功能平替。由 [RemakeList](SITE) 整理。

[English](README.md) · **简体中文** · [完整目录](DIRECTORY) · [推荐项目](https://github.com/CharlexH/awesome-remakelist/issues/new?template=project.yml)

每条都写明对应的原作、目前的阶段和开始前要准备的东西。先看清要求，再决定要不要动手。

- 想直接体验：先看每条的「开始方式」。浏览器演示、下载和自行构建是不同路线。
- 想玩老游戏：先看「需要什么」。免费引擎可能仍需自备特定版本的原版文件；演示数据通常只有部分内容。
- 想继续了解：项目名直达官方来源，「要求与截图」进入 RemakeList。所有兼容性和功能说明均基于所引资料，不代表本站已经安装或试玩。

## 目录

'''
    else:
        head = '''# Awesome RemakeList

Software recreations, classic game engines, native ports, and clearly labeled functional alternatives. Curated by [RemakeList](SITE).

**English** · [简体中文](README.zh-CN.md) · [Browse the directory](DIRECTORY) · [Suggest a project](https://github.com/CharlexH/awesome-remakelist/issues/new?template=project.yml)

Find what a project recreates or replaces, where it runs, and what you need before getting started.

- **Want to try something?** Check the starting route: a browser demo, a download and a personal build are different commitments.
- **Looking for an old game?** Read the file requirement first. A free engine may need a specific original edition; demo data usually covers limited content.
- **Need more detail?** Project names link directly to official sources. The accompanying RemakeList pages add screenshots and setup context. Compatibility and feature statements come from the cited sources, not a claim that we installed or played every project.

## Contents

'''
    head = head.replace('SITE', tracked('https://remakelist.com/zh/' if chinese else 'https://remakelist.com/', 'intro-' + suffix)).replace('DIRECTORY', tracked('https://remakelist.com/zh/' if chinese else 'https://remakelist.com/', 'directory-' + suffix))
    for _, labels in SECTIONS.items():
        title = labels[lang]
        # Explicit anchors keep links stable across both languages.
        section = next(key for key, value in SECTIONS.items() if value == labels)
        head += f'- [{title}](#{section})\n'
    text = head
    for section, labels in SECTIONS.items():
        text += f'\n<a id="{section}"></a>\n\n## {labels[lang]}\n\n'
        for p in data['projects']:
            if p['section'] != section:
                continue
            original = clean(p['original_zh' if chinese else 'original_en'])
            relation = RELATIONS[p['relationship']][lang]
            start = STARTS[p['start']][lang]
            platform = clean(p['platforms_zh' if chinese else 'platforms_en'])
            stage = clean(p['stage_zh' if chinese else 'stage_en'])
            summary = clean(p['summary_zh' if chinese else 'summary_en'])
            requirements = clean(p['requirements_zh' if chinese else 'requirements_en'])
            site = tracked(p['site_url_zh' if chinese else 'site_url'], p['id'] + '-' + suffix)
            license_label = p['code_license'].split(';')[0].split(' · ')[0]
            if 'Sustainable Use License 1.0' in p['code_license']:
                license_label = 'Sustainable Use License 1.0'
            status = ('源码可见；有限制许可' if chinese else 'source available; restricted license') if p['code_status'] == 'source_available' else ('代码许可' if chinese else 'code')
            punctuation = '。' if chinese else '. '
            text += f'- **[{clean(p["name"])}]({p["official_url"]})** — {original} · {relation}{punctuation}{summary}\n'
            text += f'  <br>{"平台" if chinese else "Platforms"}: {platform} · {"开始方式" if chinese else "Start"}: [{start}]({p["start_url"]}) · {"现状" if chinese else "Status"}: {stage}\n'
            text += f'  <br>{"需要什么" if chinese else "Needs"}: {requirements} · [{status}: {license_label}]({p["code_license_url"]}) · [{"要求与截图" if chinese else "Requirements & screenshots"}]({site})\n\n'
    if chinese:
        text += '''## 收录与纠错

可以通过 Issue 推荐项目或修正资料，也可以提交 PR 改进清单。[贡献说明](CONTRIBUTING.md)列出了需要提供的来源。首批条目来自已发布的 RemakeList 目录；资料核对日期和官方文档保存在[结构化数据](data/projects.json)中。[数据说明](docs/data.md)

这里同时收录功能平替、界面再现和游戏相关项目，不把它们都叫作「复刻」或「开源」。代码许可不等于原作素材许可；本仓库只提供清单，不提供游戏文件、密钥或安装包。

原创清单文字采用 [CC BY 4.0](LICENSE)，生成脚本采用 [MIT](scripts/LICENSE)。各项目及第三方内容保留自己的许可，见[说明](NOTICE.md)。
'''
    else:
        text += '''## Contribute and correct

Suggest a project, report outdated information or improve the list through a PR. Read the [contribution guide](CONTRIBUTING.md) for the sources we need. This selection comes from the published RemakeList directory. Per-entry source-review dates and official documentation are available in the [structured catalog](data/projects.json). See the [data notes](docs/data.md).

Functional alternatives, interface recreations and game projects are labeled separately. Not every entry is open source. A code license does not license the original game's assets; this repository supplies no game files, keys or install packages.

Original list text: [CC BY 4.0](LICENSE). Generator scripts: [MIT](scripts/LICENSE). Listed projects and third-party material retain their own licenses; see [NOTICE](NOTICE.md).
'''
    return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / 'data/projects.json').read_text())
    for name, chinese in [('README.md', False), ('README.zh-CN.md', True)]:
        expected = render(data, chinese)
        if args.check:
            if (ROOT / name).read_text() != expected:
                raise SystemExit(f'{name} is stale; run python3 scripts/build_readme.py')
        else:
            (ROOT / name).write_text(expected)
    print('README generation check passed' if args.check else 'Generated English and Chinese READMEs')


if __name__ == '__main__':
    main()
