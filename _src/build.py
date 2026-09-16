#!/usr/bin/env python3
"""Cut _src/site.html into one real page per address.

The site is written as a single document holding every <main>. Google can only
rank an address, so this writes each page out on its own, carrying the shared
head, masthead and footer, with its own title, description and canonical.

Run from the repo root:  python3 _src/build.py
"""
import os, re, sys, json, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_src", "site.html")
SITE = "https://zejakov.com"

# slug -> (output path, <title>, meta description, nav href)
EN_TITLE = {
 "hjem": "ZEJAKOV MEDIA | Property film, photography and drone in Oslo",
 "arbeid": "Work | A home filmed and photographed in Oslo | ZEJAKOV MEDIA",
 "tjenester": "Property film, photography and drone in Oslo | ZEJAKOV MEDIA",
 "om": "About me | Property photographer and filmmaker in Oslo | ZEJAKOV MEDIA",
 "kontakt": "Contact | Book a walkthrough in Oslo | ZEJAKOV MEDIA",
 "personvern": "Privacy | ZEJAKOV MEDIA",
}
PAGES = {
 "hjem": ("index.html",
   "ZEJAKOV MEDIA | Boligfilm, boligfoto og drone i Oslo",
   "Medieproduksjon for eiendom i Oslo. Boligfilm, boligfoto og drone til visning "
   "og annonse, alt gjort av én person. Se arbeidet og book befaring.",
   "/"),
 "arbeid": ("arbeid/index.html",
   "Arbeid | Bolig filmet og fotografert i Oslo | ZEJAKOV MEDIA",
   "En hel bolig i Oslo, fotografert og filmet i samme besøk: stillbilder, "
   "film og drone fra Heyerdahls vei 8 B.",
   "/arbeid/"),
 "tjenester": ("tjenester/index.html",
   "Boligfilm, boligfoto og drone i Oslo | ZEJAKOV MEDIA",
   "Hele produksjonen av én person: stillbilder, film, drone og lys. For eiere "
   "og meglere som vil vise hvordan boligen faktisk er å bo i.",
   "/tjenester/"),
 "om": ("om/index.html",
   "Om meg | Boligfotograf og filmfotograf i Oslo | ZEJAKOV MEDIA",
   "Én person, spesialisert på eiendom i Oslo og omegn. Den som filmer er "
   "den samme som redigerer og leverer.",
   "/om/"),
 "kontakt": ("kontakt/index.html",
   "Kontakt | Book befaring i Oslo | ZEJAKOV MEDIA",
   "Fortell meg om boligen, så finner vi en dag. Oslo, Bærum, Asker og "
   "Nordre Follo.",
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


def meta(head, title, desc, url, slug):
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
    head = head.replace("</head>",
        '<script>window.DOCTITLE=%s</script>\n</head>'
        % json.dumps({"no": title, "en": EN_TITLE[slug]}, ensure_ascii=False), 1)
    return head


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
    before, mains, after = split(rest)

    written = []
    for slug in ORDER:
        path, title, desc, href = PAGES[slug]
        url = SITE + href
        page = mains[slug][2]
        # the page's own heading is the document heading, once it is a document
        if slug != "hjem":
            page = page.replace('<h2 data-t=', '<h1 data-t=', 1)
            page = page.replace('<h2><span data-t=', '<h1><span data-t=', 1)
            if "<h1" in page:
                i = page.index("<h1")
                j = page.index("</h2>", i)
                page = page[:j] + "</h1>" + page[j + len("</h2>"):]
        page = page.replace('<main class="page" id=', '<main class="page live" id=', 1)

        doc = meta(head, title, desc, url, slug) + links(before, slug) + page + links(after, slug)
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
