# Catalog data

`data/projects.json` is the machine-readable edition of this selection. All text is UTF-8. `schema_version` changes when field meanings change.

Each project has an ID, name, original reference, relationship, section, English/Chinese summary and requirements, platforms, starting route, development-stage text, code-license text and source URL, first-party documentation, official project URL, website paths and a source-review date.

`source_reviewed_at` is the date RemakeList checked the source material. It is not a runtime test, a last-commit date or a promise that a particular device works. `stage` is separate from the starting route: a downloadable project can still be an alpha. `original_files` distinguishes software that does not need an original installation, projects that need original data, and engines with a documented free/demo data route.

The list intentionally includes functional alternatives alongside reimplementations. `independent_functional_alternative` means similar functionality, not copied code or proof of reverse engineering. `code_status` distinguishes open source from source-available code; project-specific license terms remain authoritative.

`data/selection.json` holds the human-reviewed selection, section and short copy. `scripts/sync_from_site.py` refreshes only those selected IDs from the publicly deployed website. A selected ID missing from production stops the sync. URLs in the READMEs add campaign parameters to RemakeList links; official project links remain direct.

No authentication, private repository access, API key or external Python package is needed to generate or check the list. No scheduled publishing is configured.

## Original-file labels

- `not_applicable`: software tools that do not require an original application's installation files.
- `none`: a complete game or a documented free replacement-data route needs no owned original copy.
- `original`: the documented experience requires original commercial game files.
- `optional`: a documented full freeware or replacement-data route also exists; read each game's terms.
- `demo`: a legal, limited demo/shareware route exists; the full game still needs its own data.
- `acquired`: the official setup can fetch or import required original assets; this does not relicense them.

The prose requirements are authoritative when a specific edition, extraction, signing or installation step matters. These categories are not legal permissions.

## Reviewing upstream changes

Each entry includes a fingerprint of its published source fields and first-party links. If a source changes, synchronization stops before writing the catalog. Review the differences, correct the short copy in `data/selection.json`, then explicitly run:

```sh
python3 scripts/sync_from_site.py --accept-reviewed-source-changes
python3 scripts/build_readme.py
python3 scripts/check.py
```

This flag records a maintainer's review; it does not perform one. Public metadata updates must not silently attach a new review date to stale requirements. Live-link validation confirms reachability and page identity, not installation or gameplay.
