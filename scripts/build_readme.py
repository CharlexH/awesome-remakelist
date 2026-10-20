# SPDX-License-Identifier: MIT
"""Generate localized READMEs and factual SVG overviews from the published feed."""
import argparse
import html
import json
from pathlib import Path
from urllib.parse import urlencode

ROOT=Path(__file__).resolve().parents[1]
SECTIONS=['creative','everyday','classic_games','ports']


def copy():
    return json.loads((ROOT/'scripts/readme-copy.json').read_text())


def clean(value):
    return html.escape(str(value).replace('\n',' '),quote=False).replace('[','\\[').replace(']','\\]').replace('|','\\|')


def tracked(url,content):
    return url+'?'+urlencode({'utm_source':'github','utm_medium':'repository','utm_campaign':'awesome-remakelist','utm_content':content})


def site(p,locale):
    prefix=copy()[locale]['prefix']
    return 'https://remakelist.com/'+(prefix+'/' if prefix else '')+'remakes/'+p['id']+'/'


def overview(data,locale):
    u=copy()[locale];counts={key:sum(p['section']==key for p in data['projects']) for key in SECTIONS}
    total=sum(counts.values());colors=['#24272a','#666b72','#9da3aa','#cbd0d5']
    result=['<svg xmlns="http://www.w3.org/2000/svg" width="920" height="168" viewBox="0 0 920 168" role="img">',
            '<title>'+html.escape(u['overview'])+'</title>',
            '<rect x="0.5" y="0.5" width="919" height="167" rx="14" fill="#fafafa" stroke="#e1e4e8"/>',
            f'<text x="26" y="34" font-family="Arial,Helvetica,sans-serif" font-size="16" font-weight="700" fill="#24272a">{html.escape(u["overview"])}</text>',
            f'<text x="894" y="34" text-anchor="end" font-family="Arial,Helvetica,sans-serif" font-size="14" fill="#666b72">{total} {html.escape(u["projects_count"])}</text>']
    x=26
    for i,key in enumerate(SECTIONS):
        width=868*counts[key]/max(total,1)
        result.append(f'<rect x="{x:.2f}" y="54" width="{width:.2f}" height="24" fill="{colors[i]}"/>');x+=width
    for i,key in enumerate(SECTIONS):
        x=26+(i%2)*444;y=108+(i//2)*32
        result.extend([f'<rect x="{x}" y="{y-10}" width="10" height="10" rx="2" fill="{colors[i]}"/>',
                       f'<text x="{x+18}" y="{y}" font-family="Arial,Helvetica,sans-serif" font-size="13" fill="#454a50">{html.escape(u["sections"][key])}</text>',
                       f'<text x="{x+408}" y="{y}" text-anchor="end" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="700" fill="#24272a">{counts[key]}</text>'])
    result.append('</svg>');return '\n'.join(result)+'\n'


def render(data,locale='en'):
    labels=copy();u=labels[locale];prefix=u['prefix'];home='https://remakelist.com/'+(prefix+'/' if prefix else '')
    home=tracked(home,'intro-'+locale)
    text=f'<a href="{home}"><img src="assets/banner.svg" alt="RemakeList — software recreations and classic game ports" width="920"></a>\n\n# Awesome RemakeList\n\n{u["subtitle"]}\n\n'
    text+=' · '.join('**'+v['name']+'**' if key==locale else '['+v['name']+']('+v['file']+')' for key,v in labels.items())+'\n\n'
    text+=f'[{u["browse"]}]({home}) · [{u["suggest"]}](https://github.com/CharlexH/awesome-remakelist/issues/new?template=project.yml)\n\n'
    for workflow,title in [('check.yml','Catalog checks'),('sync.yml','Website sync')]:
        text+=f'[![{title}](https://github.com/CharlexH/awesome-remakelist/actions/workflows/{workflow}/badge.svg?branch=main)](https://github.com/CharlexH/awesome-remakelist/actions/workflows/{workflow}) '
    text=text.rstrip()+'\n\n'+u['intro']+'\n\n'
    text+=f'## {u["start_here"]}\n\n| {u["project"]} | {u["explore"]} | {u["start"]} |\n| --- | --- | --- |\n'
    by_id={p['id']:p for p in data['projects']}
    for key in data['featured_ids']:
        p=by_id[key];t=p['localized'][locale]
        text+=f'| [{clean(p["name"])}]({tracked(site(p,locale),key+"-featured-"+locale)}) | {clean(t["original"])} | [{u["starts"].get(p["start"],p["start"])}]({p["start_url"]}) |\n'
    text+=f'\n## {u["browse_category"]}\n\n'
    for section in SECTIONS:
        count=sum(p['section']==section for p in data['projects']);text+=f'- [{u["sections"][section]}](#{section}) · {count}\n'
    text+=f'\n<img src="assets/overview-{locale}.svg" alt="{html.escape(u["overview"],quote=True)}" width="920">\n'
    for section in SECTIONS:
        text+=f'\n<a id="{section}"></a>\n\n## {u["sections"][section]}\n\n'
        for p in data['projects']:
            if p['section']!=section:continue
            t=p['localized'][locale];relation=u['relations'].get(p['relationship'],p['relationship'])
            text+=f'### [{clean(p["name"])}]({p["official_url"]})\n\n{clean(t["summary"])}\n\n'
            text+=f'{u["original"]}: **{clean(t["original"])}** · {clean(relation)}  \n'
            text+=f'[{u["starts"].get(p["start"],p["start"])}]({p["start_url"]}) · [{u["browse"]}]({tracked(site(p,locale),p["id"]+"-"+locale)})\n\n'
            text+=f'<details>\n<summary>{u["details"]}</summary>\n\n'
            for field in ['platforms','status','needs','availability']:
                source={'status':'stage','needs':'requirements'}.get(field,field);text+=f'**{u[field]}:** {clean(t[source])}\n\n'
            text+=f'**{u["restricted"] if p["code_status"]=="source_available" else u["code"]}:** [{clean(p["code_license"])}]({p["code_license_url"]})  \n'
            text+=f'**{u["author"]}:** {clean(p["author"])}  \n[{u["docs"]}]({p["documentation_url"]}) · {u["reviewed"]}: {p["source_reviewed_at"]}\n\n</details>\n\n'
    text+=f'## {u["about"]}\n\n{u["about_text"]} [{u["data_notes"]}](docs/data.md)\n\n{u["scope_text"]}\n\n'
    text+=u['contribute']+f' [{u["suggest"]}](CONTRIBUTING.md)\n\n'+u['rights']+'\n\n[CC BY 4.0](LICENSE) · [MIT](scripts/LICENSE) · [NOTICE](NOTICE.md)\n'
    return text


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    data=json.loads((ROOT/'data/projects.json').read_text())
    for locale,u in copy().items():
        for path,expected in [(ROOT/u['file'],render(data,locale)),(ROOT/f'assets/overview-{locale}.svg',overview(data,locale))]:
            if args.check:
                if path.read_text()!=expected:raise SystemExit(str(path.relative_to(ROOT))+' is stale; regenerate')
            else:path.write_text(expected)
    print('Generated catalog and charts for '+', '.join(copy()))


if __name__=='__main__':main()
