#!/usr/bin/env python3
"""Cut _src/site.html into one real page per address.

The site is written as a single document holding every <main>. Google can only
rank an address, so this writes each page out on its own, carrying the shared
head, masthead and footer, with its own title, description and canonical.

Run from the repo root:  python3 _src/build.py
"""
import os, re, sys, json, datetime

import tinycss2

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_src", "site.html")
SITE = "https://zejakov.com"

# slug -> (output path, <title>, meta description, nav href)
PAGES = {
 "hjem": ("index.html",
   "Boligfilm og boligfoto i Oslo | ZEJAKOV MEDIA",
   "Medieproduksjon for eiendom i Oslo. Boligfilm, boligfoto og drone til visning "
   "og annonse, alt gjort av én person. Se arbeidet og book befaring.",
   "/"),
 "arbeid": ("arbeid/index.html",
   "Boligfilm fra Oslo: Heyerdahls vei 8 B | ZEJAKOV MEDIA",
   "En hel bolig i Oslo, fotografert og filmet i samme besøk: stillbilder, "
   "film og drone fra Heyerdahls vei 8 B.",
   "/arbeid/"),
 "tjenester": ("tjenester/index.html",
   "Boligfilm, boligfoto og drone i Oslo | ZEJAKOV MEDIA",
   "Hele produksjonen av én person: stillbilder, film, drone og lys. For eiere "
   "og meglere som vil vise hvordan boligen faktisk er å bo i.",
   "/tjenester/"),
 "om": ("om/index.html",
   "Boligfotograf og filmfotograf i Oslo | ZEJAKOV MEDIA",
   "Én person, spesialisert på eiendom i Oslo og omegn. Den som filmer er "
   "den samme som redigerer og leverer.",
   "/om/"),
 "kontakt": ("kontakt/index.html",
   "Book befaring for boligfilm i Oslo | ZEJAKOV MEDIA",
   "Fortell meg om boligen, så finner vi en dag for befaring. Boligfilm, "
   "boligfoto og drone i Oslo, Bærum, Asker og Nordre Follo.",
   "/kontakt/"),
 "personvern": ("personvern/index.html",
   "Personvern | ZEJAKOV MEDIA",
   "Hva jeg lagrer og hvorfor. Ingen informasjonskapsler, ingen sporing, og "
   "ingenting lagret i nettleseren din.",
   "/personvern/"),
}
ORDER = ["hjem", "arbeid", "tjenester", "om", "kontakt", "personvern"]


def split(src):
    """head + chrome before the pages + each <main> + chrome after them."""
    mains = {}
    for m in re.finditer(r'<main class="page[^"]*" id="p-([a-z]+)">', src):
        slug = m.group(1)
        end = src.index("</main>", m.start()) + len("</main>")
        mains[slug] = (m.start(), end, src[m.start():end])
    assert set(mains) == set(PAGES), "pages in the source: %s" % sorted(mains)
    first = min(v[0] for v in mains.values())
    last = max(v[1] for v in mains.values())
    return src[:first], mains, src[last:]


def meta(head, title, desc, url):
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % title, head, count=1, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">',
                  '<meta name="description" content="%s">' % desc, head, count=1)
    head = re.sub(r'<link rel="canonical" href="[^"]*">',
                  '<link rel="canonical" href="%s">' % url, head, count=1)
    head = re.sub(r'<meta property="og:url" content="[^"]*">',
                  '<meta property="og:url" content="%s">' % url, head, count=1)
    head = re.sub(r'<meta property="og:title" content="[^"]*">',
                  '<meta property="og:title" content="%s">' % title, head, count=1)
    head = re.sub(r'<meta property="og:description" content="[^"]*">',
                  '<meta property="og:description" content="%s">' % desc, head, count=1)
    return head


def _ws(text):
    return re.sub(r"\s+", " ", text).strip()


def _selector(prelude):
    sel = _ws(tinycss2.serialize(prelude))
    return re.sub(r"\s*([,>+~])\s*", r"\1", sel)


def _declarations(content):
    out = []
    for d in tinycss2.parse_declaration_list(content, skip_comments=True, skip_whitespace=True):
        if d.type != "declaration":
            continue
        out.append("%s:%s%s" % (d.name if d.name.startswith("--") else d.lower_name,
                                _ws(tinycss2.serialize(d.value)),
                                "!important" if d.important else ""))
    return ";".join(out)


def _rules(nodes):
    out = []
    for n in nodes:
        if n.type == "qualified-rule":
            out.append("%s{%s}" % (_selector(n.prelude), _declarations(n.content)))
        elif n.type == "at-rule":
            kw, pre = n.lower_at_keyword, _ws(tinycss2.serialize(n.prelude))
            if n.content is None:
                out.append("@%s %s;" % (kw, pre))
            elif kw in ("media", "supports", "keyframes"):
                inner = tinycss2.parse_rule_list(n.content, skip_comments=True, skip_whitespace=True)
                out.append("@%s %s{%s}" % (kw, pre, _rules(inner)))
            else:
                out.append("@%s%s{%s}" % (kw, (" " + pre) if pre else "", _declarations(n.content)))
    return "".join(out)


def minify_style(head):
    """The stylesheet ships without comments or spacing; the source keeps both."""
    a = head.index("<style>") + len("<style>")
    b = head.index("</style>", a)
    css = tinycss2.parse_stylesheet(head[a:b], skip_comments=True, skip_whitespace=True)
    return head[:a] + _rules(css) + head[b:]


def links(chunk, current):
    """Hash routes become real addresses, and the current one is marked."""
    def fix(m):
        href = PAGES[m.group(1)][3] if m.group(1) in PAGES else "/"
        on = ' class="on"' if m.group(1) == current else ""
        return '<a href="%s"%s' % (href, on)
    chunk = re.sub(r'<a href="#([a-z]+)"(?: class="on")?', fix, chunk)
    return chunk


def main():
    src = open(SRC, encoding="utf-8").read()
    head_end = src.index("</head>") + len("</head>")
    head, rest = src[:head_end], src[head_end:]
    head = minify_style(head)
    before, mains, after = split(rest)

    written = []
    for slug in ORDER:
        path, title, desc, href = PAGES[slug]
        url = SITE + href
        page = mains[slug][2]
        # the page's own heading is the document heading, once it is a document
        if slug != "hjem":
            i = page.index("<h2")
            j = page.index("</h2>", i)
            page = page[:i] + "<h1" + page[i + 3:j] + "</h1>" + page[j + len("</h2>"):]
        page = page.replace('<main class="page" id=', '<main class="page live" id=', 1)

        doc = meta(head, title, desc, url) + links(before, slug) + page + links(after, slug)
        out = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        open(out, "w", encoding="utf-8").write(doc)
        written.append((path, len(doc)))

    today = datetime.date.today().isoformat()
    urls = "\n".join('  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>'
                     % (SITE, PAGES[s][3], today) for s in ORDER)
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % urls)

    for path, n in written:
        print("%-24s %6.1f KB" % (path, n / 1024))
    print("sitemap.xml              %d urls" % len(ORDER))


if __name__ == "__main__":
    main()
