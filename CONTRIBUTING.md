# Contributing

Found a project worth trying, or a requirement we got wrong? Open a [project suggestion](https://github.com/CharlexH/awesome-remakelist/issues/new?template=project.yml) or a [correction](https://github.com/CharlexH/awesome-remakelist/issues/new?template=correction.yml). English and Chinese are both welcome.

## What belongs here

A software or interface recreation, classic-game engine, source port, compatibility project, or clearly identified functional alternative. It must have a first-party project page and an actual public route to try, download or build it. Early projects are welcome when their limitations are clear. Wishlist ideas and private demonstrations without a public implementation are not catalog entries.

Please provide:

- The official project URL and the original product or game it relates to.
- What it recreates or replaces; do not call an independent alternative a remake.
- Supported platforms, current stage and the first step a user can actually take.
- Code-license evidence, including source-available or unlicensed status where relevant.
- Any original-file, edition, account, build or signing requirement, with an official source.

Do not upload commercial artwork, game data, keys, install packages or other third-party materials. Link to the author's documentation instead. An issue is a suggestion, not a promise of inclusion.

## How updates work

RemakeList reviews suggestions and maintains the full directory. This repository is a curated selection of entries already published on the website. The selection and short English/Chinese summaries live in `data/selection.json`; published metadata and first-party sources are refreshed into `data/projects.json`.

To correct selection copy or improve the generator, submit a PR. Maintainers review changes to factual claims against official sources; website corrections are handled before refreshing the public metadata. For a new project, start with an issue so it can be checked and added to the website first.

```sh
python3 scripts/sync_from_site.py
python3 scripts/build_readme.py
python3 scripts/check.py
```

The sync only reads public website text data. It does not download or build any listed software. It never imports the website source tree or unpublished entries. `scripts/check.py` is offline; `python3 scripts/check.py --live` additionally checks published RemakeList destinations. A blocked request must be reported as unverified, not silently counted as a working link.

The READMEs are generated from the two JSON files. Edit those files and regenerate, rather than editing generated project lists directly. Source review dates come from the website; a successful link check does not change them.

## Reuse

Original contributions use the licenses described in [NOTICE.md](NOTICE.md). Do not submit copied competitor descriptions or anything you cannot permit us to publish under those terms.
