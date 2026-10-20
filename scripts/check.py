# SPDX-License-Identifier: MIT
"""Validate editorial data, generated READMEs and optionally live website pages."""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from build_readme import RELATIONS, ROOT, SECTIONS, STARTS, render, tracked
from sync_from_site import Detail, code_status, fetch


def check(live=False):
    payload = json.loads((ROOT / 'data/projects.json').read_text())
    selection = json.loads((ROOT / 'data/selection.json').read_text())
    assert payload['schema_version'] == selection['schema_version'] == 1
    projects = payload['projects']
    assert projects and len({p['id'] for p in projects}) == len(projects), 'Duplicate/empty catalog'
    assert [p['id'] for p in projects] == [p['id'] for p in selection['projects']], 'Selection mismatch'
    required = {'id', 'name', 'original_en', 'original_zh', 'relationship', 'section', 'summary_en', 'summary_zh',
                'requirements_en', 'requirements_zh', 'platforms_en', 'platforms_zh', 'start', 'start_url',
                'stage_en', 'stage_zh', 'code_license', 'code_license_url', 'code_license_sources', 'code_status',
                'source_requirements_en', 'source_requirements_zh', 'source_fingerprint', 'source_reviewed_at',
                'official_url', 'documentation_url', 'site_url', 'site_url_zh', 'original_files', 'author', 'author_url'}
    for p in projects:
        key = p['id']
        assert set(p) == required, f'{key}: unexpected/missing metadata'
        assert all(isinstance(p[f], str) and p[f].strip() for f in required - {'author_url', 'code_license_sources'}), key
        assert p['section'] in SECTIONS and p['relationship'] in RELATIONS and p['start'] in STARTS, key
        assert p['original_files'] in {'not_applicable', 'none', 'original', 'optional', 'demo', 'acquired'}, key
        assert p['code_status'] == code_status(p['code_license']), f'{key}: incorrect code status'
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', key), key
        assert re.fullmatch('[0-9a-f]{64}', p['source_fingerprint']), key
        assert datetime.date.fromisoformat(p['source_reviewed_at']) <= datetime.datetime.now(datetime.timezone.utc).date(), key
        for field in ['start_url', 'official_url', 'documentation_url', 'code_license_url', 'site_url', 'site_url_zh']:
            url = urlparse(p[field])
            assert url.scheme == 'https' and url.netloc and not url.username and not url.password, (key, field)
        for field, route in [('site_url', f'/remakes/{key}/'), ('site_url_zh', f'/zh/remakes/{key}/')]:
            u = urlparse(p[field]); assert u.netloc == 'remakelist.com' and u.path == route, (key, field)
            q = parse_qs(urlparse(tracked(p[field], key)).query)
            assert q['utm_source'] == ['github'] and q['utm_campaign'] == ['awesome-remakelist'], key
        assert p['code_license_url'] in p['code_license_sources'], key
    d2r = next((p for p in projects if p['id'] == 'd2r-mobile'), None)
    if d2r:
        assert 'happyjoejiang' in d2r['author'] and d2r['author_url'] == 'https://x.com/happyjoejiang'
        assert all(v in d2r['requirements_en'] for v in ['Switch', '1.0.34.0', '3.3.94012']), 'D2R edition requirements lost'
    for file, chinese in [('README.md', False), ('README.zh-CN.md', True)]:
        text = (ROOT / file).read_text()
        assert text == render(payload, chinese), f'{file}: stale generated copy'
        assert text.count('[Requirements & screenshots](' if not chinese else '[要求与截图](') == len(projects), file
        anchors = set(re.findall(r'<a id="([^"]+)"', text))
        for url in re.findall(r'\]\(([^)]+)\)', text):
            if url.startswith('https://'):
                continue
            if url.startswith('#'):
                assert url[1:] in anchors, (file, url)
            else:
                assert (ROOT / url.split('#')[0]).is_file(), (file, url)
    # The public package is text-only; credentials and website internals do not belong here.
    for file in ROOT.rglob('*'):
        relative = file.relative_to(ROOT)
        if not file.is_file() or any(part in {'.git', '.output', '__pycache__'} for part in relative.parts):
            continue
        assert file.stat().st_size < 2_000_000, str(relative)
        text = file.read_text()
        forbidden = [r'github' + r'_pat_[A-Za-z0-9_]{20,}', r'gh' + r'p_[A-Za-z0-9]{20,}',
                     '-----BEGIN ' + 'PRIVATE KEY-----', '/' + 'Users/', r'\.openai/hosting\.json']
        assert not any(re.search(pattern, text) for pattern in forbidden), f'Private material in {relative}'
    if live:
        for p in projects:
            for field in ['site_url', 'site_url_zh']:
                page = Detail(); page.feed(fetch(tracked(p[field], p['id'] + '-qa')))
                assert p['name'] in ''.join(page.text), (p['id'], field, 'identity')
                assert page.date == p['source_reviewed_at'], (p['id'], field, 'source date changed; review before refreshing')
            print('live pages passed', p['id'], flush=True)
    print(json.dumps({'projects': len(projects), 'languages': 2, 'generated_copy': 'passed',
                      'schema_and_privacy': 'passed', 'website_links': 'passed' if live else 'not requested'}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--live', action='store_true')
    args = parser.parse_args()
    try:
        check(args.live)
    except Exception as error:
        sys.exit(str(error))
