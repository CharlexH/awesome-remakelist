# SPDX-License-Identifier: MIT
"""Check the public source snapshot, generated lists and content boundaries."""
import datetime
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs,urlparse
from build_readme import ROOT,SECTIONS,copy,render,tracked,overview
from sync_from_site import validate_feed


def check():
    data=validate_feed(json.loads((ROOT/'data/projects.json').read_text()))
    projects=data['projects']
    assert not (ROOT/'data/selection.json').exists(),'Project copy must have one editorial source'
    for p in projects:
        assert p['start'] in copy()['en']['starts'],p['id']
        assert datetime.date.fromisoformat(p['source_reviewed_at']) <= datetime.datetime.now(datetime.timezone.utc).date(),p['id']
        q=parse_qs(urlparse(tracked(p['site_url'],p['id'])).query)
        assert q['utm_source']==['github'] and q['utm_campaign']==['awesome-remakelist']
    d2r=next((p for p in projects if p['id']=='d2r-mobile'),None)
    if d2r:
        assert 'happyjoejiang' in d2r['author'] and d2r['author_url']=='https://x.com/happyjoejiang'
        assert all(x in d2r['localized']['en']['requirements'] for x in ['Switch','1.0.34.0','3.3.94012'])
    for locale,u in copy().items():
        name=u['file'];text=(ROOT/name).read_text();assert text==render(data,locale),name+' is stale'
        assert text.count('<details>')==len(projects),name
        assert (ROOT/f'assets/overview-{locale}.svg').read_text()==overview(data,locale)
        anchors=set(re.findall(r'<a id="([^"]+)"',text))
        for url in re.findall(r'\]\(([^)]+)\)',text):
            if url.startswith('https://'):continue
            if url.startswith('#'):assert url[1:] in anchors,(name,url)
            else:assert (ROOT/url.split('#')[0]).is_file(),(name,url)
    for file in ROOT.rglob('*'):
        relative=file.relative_to(ROOT)
        if not file.is_file() or any(part in {'.git','.output','__pycache__'} for part in relative.parts):continue
        assert file.stat().st_size<3_000_000,str(relative)
        text=file.read_text()
        forbidden=[r'github'+r'_pat_[A-Za-z0-9_]{20,}',r'gh'+r'p_[A-Za-z0-9]{20,}','-----BEGIN '+'PRIVATE KEY-----','/'+'Users/',r'\.openai/hosting\.json']
        assert not any(re.search(pattern,text) for pattern in forbidden),'Private material in '+str(relative)
    print(json.dumps({'projects':len(projects),'languages':len(copy()),'generated_copy':'passed','source_contract_and_privacy':'passed','content_sha256':data['content_sha256']}))


if __name__=='__main__':
    try:check()
    except Exception as error:sys.exit(str(error))
