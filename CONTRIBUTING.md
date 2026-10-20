# Contributing

Found a project worth trying, or a requirement we got wrong? Open a [project suggestion](https://github.com/CharlexH/awesome-remakelist/issues/new?template=project.yml) or a [correction](https://github.com/CharlexH/awesome-remakelist/issues/new?template=correction.yml). English, Chinese, Japanese, Korean and Spanish are welcome.

## What belongs here

Software and interface recreations, classic-game engines, source ports, compatibility projects and clearly labeled functional alternatives. This public list includes projects already reviewed on RemakeList, with a public repository, stated code-license evidence and a browser, download or build route. Research-only reports, closed-source entries and unclear licenses can remain on the website but are excluded from this list.

Please provide the official project URL, its original/reference product, what it recreates or replaces, supported platforms, current stage and a public route to start. Include official evidence for code licensing and any original-file, specific-edition, account, build or signing requirement. Do not attach commercial artwork, game files, keys or install packages. A suggestion is reviewed before inclusion.

## One editorial source

Project facts are maintained on **RemakeList only**. The website build exports its reviewed entries to <https://remakelist.com/catalog/github.json>. This repository mirrors that feed into `data/projects.json` and generates all five localized READMEs and category charts. Do not edit project facts in this repository: report corrections, and maintainers update the website before synchronizing them here. There is no separate selection or short-description file to maintain.

The sync workflow runs after a verified website publish when triggered by the release process, and checks the published feed every six hours as a fallback. Only a real data difference produces a commit; scheduled runs may be delayed. It can also be started from the repository's Actions page.

PRs improving generation, validation, documentation or presentation are welcome:

```sh
python3 scripts/sync_from_site.py
python3 scripts/build_readme.py
python3 scripts/check.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

Sync reads one public JSON document and never imports a private website checkout. It validates the feed before replacing the snapshot, and fails without changing it when the feed is invalid or unavailable. Source-review dates come from the website; a link check does not change them. No listed software is downloaded, built, signed or tested by this process.

Original contributions use the licenses in [NOTICE.md](NOTICE.md). Do not submit copied descriptions, competitor databases, artwork or other material you cannot permit us to publish under those terms.
