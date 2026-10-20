# SPDX-License-Identifier: MIT
"""Mirror the reviewed catalog published by RemakeList; no separate editorial data."""
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
FEED_URL = 'https://remakelist.com/catalog/github.json'


def digest(payload):
    core = {key: value for key, value in payload.items() if key != 'content_sha256'}
    return hashlib.sha256(json.dumps(core, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()


def validate_feed(data):
    if data.get('schema_version') != 2 or data.get('publisher') != 'RemakeList' or data.get('source') != 'https://remakelist.com':
        raise ValueError('Unexpected catalog schema or publisher')
    if set(data) != {'schema_version', 'publisher', 'source', 'featured_ids', 'languages', 'projects', 'content_sha256'}:
        raise ValueError('Unexpected catalog fields')
    if data['content_sha256'] != digest(data):
        raise ValueError('Catalog hash does not match its contents')
    languages = ['en','zh-CN','ja','ko','es']
    if data['languages'] != languages:
        raise ValueError('The catalog must contain the supported five languages')
    required = {'id','name','relationship','section','localized','start','start_url','code_license',
                'code_license_url','code_license_sources','code_status','source_reviewed_at','official_url',
                'documentation_url','site_url','site_url_zh','original_files','author','author_url'}
    projects = data['projects']
    if not isinstance(projects, list) or not 1 <= len(projects) <= 2000:
        raise ValueError('Empty or oversized catalog')
    seen = set()
    for p in projects:
        if set(p) != required:
            raise ValueError(f'{p.get("id")}: unexpected or missing project fields')
        key = p['id']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', key) or key in seen:
            raise ValueError('Invalid or duplicate project ID')
        seen.add(key)
        for field in required - {'author_url','code_license_sources','localized'}:
            if not isinstance(p[field], str) or not p[field].strip() or len(p[field]) > 20000:
                raise ValueError(f'{key}: invalid {field}')
        if set(p['localized']) != set(languages):
            raise ValueError(f'{key}: incomplete language set')
        for locale, copy in p['localized'].items():
            if set(copy) != {'original','summary','requirements','availability','platforms','stage'} or not all(isinstance(v,str) and v.strip() and len(v)<20000 for v in copy.values()):
                raise ValueError(f'{key}: incomplete {locale} copy')
        for field in ['official_url','documentation_url','code_license_url','start_url','site_url','site_url_zh']:
            url = urlparse(p[field])
            if url.scheme != 'https' or not url.netloc or url.username or url.password:
                raise ValueError(f'{key}: unsafe {field}')
        for field, path in [('site_url',f'/remakes/{key}/'),('site_url_zh',f'/zh/remakes/{key}/')]:
            url = urlparse(p[field])
            if url.netloc != 'remakelist.com' or url.path != path or url.query:
                raise ValueError(f'{key}: unexpected website destination')
        if p['section'] not in {'creative','everyday','classic_games','ports'}:
            raise ValueError(f'{key}: unknown section')
        if p['code_status'] not in {'open','source_available','license_stated'}:
            raise ValueError(f'{key}: ineligible code status')
        if not isinstance(p['code_license_sources'], list) or p['code_license_url'] not in p['code_license_sources']:
            raise ValueError(f'{key}: license evidence missing')
    if not isinstance(data['featured_ids'], list) or not set(data['featured_ids']) <= seen:
        raise ValueError('Featured projects must exist in the published catalog')
    return data


def fetch_feed():
    request = Request(FEED_URL, headers={'User-Agent':'Mozilla/5.0 (compatible; RemakeListCatalog/2.0)','Cache-Control':'no-cache'})
    with urlopen(request, timeout=45) as response:
        raw = response.read(8_000_001)
        if len(raw) > 8_000_000:
            raise ValueError('Catalog response too large')
        return json.loads(raw)


def sync():
    data = validate_feed(fetch_feed())
    target = ROOT / 'data/projects.json'
    content = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    if target.exists() and target.read_text() == content:
        print(f'Already current: {len(data["projects"])} projects · {data["content_sha256"]}')
        return
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',dir=target.parent,prefix='.catalog-',suffix='.tmp',delete=False) as out:
            temporary = out.name
            out.write(content)
        os.replace(temporary,target)
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)
    print(f'Synchronized {len(data["projects"])} published projects · {data["content_sha256"]}')


if __name__ == '__main__':
    try:
        sync()
    except Exception as error:
        sys.exit(str(error))
