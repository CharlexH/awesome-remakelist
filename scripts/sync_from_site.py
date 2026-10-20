# SPDX-License-Identifier: MIT
"""Refresh selected metadata from published RemakeList JSON and detail pages."""
import argparse
import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://remakelist.com'


def fetch(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; RemakeListCatalog/1.0)'})
    with urlopen(request, timeout=30) as response:
        if response.status != 200:
            raise ValueError(f'{url}: HTTP {response.status}')
        return response.read().decode('utf-8')


def read_module(text):
    prefix = 'export const browserData='
    if not text.startswith(prefix):
        raise ValueError('Public catalog format changed; refusing to evaluate JavaScript')
    value, end = json.JSONDecoder().raw_decode(text[len(prefix):])
    if text[len(prefix) + end:].strip() != ';':
        raise ValueError('Unexpected JavaScript after public JSON')
    return value


class Detail(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.text = []
        self.links = []
        self.date = None
        self.dt_text = None
        self.fact_key = None
        self.in_dd = False
        self.fact_links = {}
        self.fact_text = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'dt':
            self.dt_text = []
        elif tag == 'dd':
            self.in_dd = True
            self.fact_text[self.fact_key] = []
        self.stack.append((tag, attrs)) if tag not in {'img', 'input', 'meta', 'link', 'br', 'hr'} else None
        if tag == 'time' and not self.date:
            self.date = attrs.get('datetime')
        if tag == 'a':
            self.links.append((attrs.get('href', ''), attrs.get('aria-label', '').removesuffix(' (opens in a new tab)')))
            if self.in_dd:
                self.fact_links.setdefault(self.fact_key, []).append(attrs.get('href', ''))

    def handle_endtag(self, tag):
        if tag == 'dt' and self.dt_text is not None:
            self.fact_key = ''.join(self.dt_text).strip()
            self.dt_text = None
        elif tag == 'dd':
            self.in_dd = False
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, text):
        if self.dt_text is not None:
            self.dt_text.append(text)
        if self.in_dd:
            self.fact_text[self.fact_key].append(text)
        if self.stack and self.stack[-1][0] not in {'script', 'style'}:
            self.text.append(text)


def code_status(license_text):
    if re.search(r'Sustainable Use|PolyForm|non-commercial|noncommercial', license_text, re.I):
        return 'source_available'
    if re.search(r'MIT|Apache|GPL|MPL|BSD|ISC|CC0', license_text):
        return 'open'
    return 'unknown'


def sync(accept_reviewed=False):
    selection = json.loads((ROOT / 'data/selection.json').read_text())
    path = ROOT / 'data/projects.json'
    previous = {p['id']: p for p in json.loads(path.read_text())['projects']} if path.exists() else {}
    en = read_module(fetch(ORIGIN + '/assets/data/en.mjs'))
    zh = read_module(fetch(ORIGIN + '/assets/data/zh.mjs'))
    items = {item['id']: item for item in en['items']}
    projects = []
    for chosen in selection['projects']:
        key = chosen['id']
        if key not in items:
            raise ValueError(f'{key}: not in the published catalog')
        item = items[key]
        a, b = en['itemTranslations'][key], zh['itemTranslations'][key]
        page = ORIGIN + '/remakes/' + item['slug'] + '/'
        detail = Detail()
        detail.feed(fetch(page))
        if item['name'] not in ''.join(detail.text):
            raise ValueError(f'{key}: page identity mismatch')
        if not detail.date or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', detail.date):
            raise ValueError(f'{key}: no source-review date')
        source = next((url for url, label in detail.links if label == 'Source'), None)
        docs = next((url for url, label in detail.links if label == 'Project documentation'), None)
        license_urls = detail.fact_links.get('License', [])
        license_url = license_urls[0] if license_urls else None
        if not all((source, docs, license_url)):
            raise ValueError(f'{key}: official source, docs or code-license link missing')
        critical = {'public_item': item, 'en': a, 'zh': b, 'source': source, 'documentation': docs,
                    'license_urls': license_urls, 'author': ''.join(detail.fact_text.get('Author', [])).strip()}
        fingerprint = hashlib.sha256(json.dumps(critical, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        if key in previous and previous[key]['source_fingerprint'] != fingerprint and not accept_reviewed:
            raise ValueError(f'{key}: published facts changed. Review the short copy and file requirements, '
                             'then rerun with --accept-reviewed-source-changes. Prior data is unchanged.')
        project = {
            **chosen,
            'name': item['name'],
            'original_en': a['reference_en'],
            'original_zh': b['reference_en'],
            'relationship': item['relationship'],
            'platforms_en': a['platform'],
            'platforms_zh': b['platform'],
            'start': item['experience_type'],
            'start_url': item['experience_url'],
            'stage_en': a.get('development_state_en') or chosen['stage_fallback_en'],
            'stage_zh': b.get('development_state_en') or chosen['stage_fallback_zh'],
            'code_license': a['license_en'],
            'code_license_url': license_url,
            'code_license_sources': license_urls,
            'code_status': code_status(a['license_en']),
            'source_requirements_en': a['assets_en'],
            'source_requirements_zh': b['assets_en'],
            'source_fingerprint': fingerprint,
            'author': critical['author'],
            'author_url': next(iter(detail.fact_links.get('Author', [])), None),
            'official_url': source,
            'documentation_url': docs,
            'source_reviewed_at': detail.date,
            'site_url': page,
            'site_url_zh': ORIGIN + '/zh/remakes/' + item['slug'] + '/',
        }
        del project['stage_fallback_en'], project['stage_fallback_zh']
        projects.append(project)
        print('refreshed', key, flush=True)
    payload = {'schema_version': 1, 'publisher': 'RemakeList', 'source': ORIGIN, 'projects': projects}
    # Write only after every selected entry has passed; a failed fetch preserves the prior file.
    (ROOT / 'data/projects.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    print(f'Refreshed {len(projects)} published entries. No software or game data downloaded.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--accept-reviewed-source-changes', action='store_true',
                        help='Only after reviewing source differences and correcting selection copy')
    args = parser.parse_args()
    try:
        sync(args.accept_reviewed_source_changes)
    except Exception as error:
        sys.exit(str(error))
