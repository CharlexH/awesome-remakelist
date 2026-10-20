# One source, two presentations

The website's published <https://remakelist.com/catalog/github.json> is the only editorial source for this public list. `data/projects.json` is a generated mirror, not a second editable database. The English, Simplified Chinese, Japanese, Korean and Spanish READMEs are generated from it. New eligible entries, updates and removals follow the website automatically.

The website exports an explicit whitelist of public facts in the five supported languages. It never exports its source tree, internal editorial fields, credentials, original game assets or image files. The public GitHub list is narrower than the full website: it requires a public repository, stated license evidence and an actual browser, download or build route. Research reports, closed-source projects and unclear licenses remain out of this feed.

## Contract

`schema_version: 2`, `publisher`, `source`, `featured_ids`, `languages`, `projects`, `content_sha256` form the document. The hash covers the exact JSON payload excluding `content_sha256`, with compact UTF-8 serialization and preserved field order. The feed has no generated timestamp: unchanged editorial data must stay byte-stable.

Each project includes its name, relationship, category group, code-license evidence, author, source-review date, official links and website URLs. Its `localized` block contains `original`, `summary`, `requirements`, `availability`, `platforms` and `stage` for each supported language. These strings come directly from the website translations. The status is separate from its starting route. Downloadable projects can be early or incomplete.

`code_status` is the website's stated status; absent classification is `license_stated`, not an inferred open-source claim. `source_available` remains visibly distinct. Linked code licenses never license the commercial original's assets.

`original_files` uses the website's labels: `not_applicable` for software without an original installation requirement; `none` for a self-contained/free-data route; `original` for required original data; `optional` for an alternative free-data route; `demo` for a limited demo/shareware route; `acquired` for original assets fetched/imported through official setup. The full requirements and availability text govern specific editions and installation steps.

Source-review dates indicate a documentation check, not an installation test or a release date. Compatibility and performance claims remain attributable to their sources.

## Synchronization

The `Sync published website catalog` workflow can be dispatched after a website deployment and checks the feed every six hours as a fallback. It validates the source, hash, fields and URLs; atomically replaces the snapshot; regenerates all localized lists and category charts; runs checks and tests; and commits only changed generated files. It uses a repository-scoped GitHub Actions token, not access to the private website repository. No external credentials are needed to fetch the feed.

A failed feed or validation preserves the previous snapshot and fails the workflow. Website publishing and GitHub sync are separate completion checks. A website release is not called synchronized until its live feed hash matches the public snapshot and the workflow succeeds.
