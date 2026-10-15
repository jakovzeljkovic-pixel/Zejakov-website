#!/usr/bin/env python3
"""Cut _src/site.html into one real page per address.

The site is written as a single document holding every <main>. Google can only
rank an address, so this writes each page out on its own, carrying the shared
head, masthead and footer, with its own title, description and canonical.

Run from the repo root:  python3 _src/build.py
"""
import os, re, sys, json, datetime

import tinycss2

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import en

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_src", "site.html")
SITE = "https://zejakov.com"

# slug -> (output path, <title>, meta description, address)
PAGES = {
 "hjem": ("index.html",
   "Boligfilm og boligfoto i Oslo | ZEJAKOV MEDIA",
   "Medieproduksjon for eiendom i Oslo. Boligfilm, boligfoto og drone til visning "
   "og annonse, alt gjort av samme person. Se arbeidet og book befaring.",
   "/"),
 "arbeid": ("arbeid/index.html",
   "Arbeid: boligfilm og boligfoto fra Oslo | ZEJAKOV MEDIA",
   "Boliger jeg har fotografert og filmet i Oslo og omegn. Hvert prosjekt "
   "med film, bilder og drone fra samme oppdrag.",
   "/arbeid/"),
 "heyerdahls": ("arbeid/heyerdahls-vei-8b/index.html",
   "Heyerdahls vei 8 B: boligfilm fra Oslo | ZEJAKOV MEDIA",
   "Enebolig i Oslo med utsikt over byen. Film, bilder og drone fra samme "
   "oppdrag, august 2026.",
   "/arbeid/heyerdahls-vei-8b/"),
 "tjenester": ("tjenester/index.html",
   "Boligfilm, boligfoto og drone i Oslo | ZEJAKOV MEDIA",
   "Hele jobben gjort av samme person: bilder, film, drone og lys. For eiere og "
   "meglere som vil vise hvordan det er å bo i boligen.",
   "/tjenester/"),
 "om": ("om/index.html",
   "Boligfotograf og filmfotograf i Oslo | ZEJAKOV MEDIA",
   "Foto og film siden 2023, i dag nesten bare boliger. Holder til i Oslo "
   "og tar oppdrag over hele verden.",
   "/om/"),
 "kontakt": ("kontakt/index.html",
   "Book befaring for boligfilm i Oslo | ZEJAKOV MEDIA",
   "Fortell meg om boligen, så finner vi en dag for befaring. Boligfilm, "
   "boligfoto og drone i Oslo, og oppdrag over hele verden.",
   "/kontakt/"),
 "ikkefunnet": ("404.html",
   "Siden finnes ikke | ZEJAKOV MEDIA",
   "Denne adressen finnes ikke på zejakov.com.",
   "/404.html"),
 "personvern": ("personvern/index.html",
   "Personvern | ZEJAKOV MEDIA",
   "Hva jeg lagrer og hvorfor. Siden setter ingen informasjonskapsler og har "
   "ingen sporing.",
   "/personvern/"),
}
ORDER = ["hjem", "arbeid", "heyerdahls", "tjenester", "om", "kontakt", "personvern", "ikkefunnet"]
# served by the host for any missing address; kept out of the sitemap and the index
HIDDEN = {"ikkefunnet"}
# a project lights up Arbeid in the menu
NAV = {"heyerdahls": "arbeid"}


def split(src):
    """head + chrome before the pages + each <main> + chrome after them."""
    mains = {}
    for m in re.finditer(r'<main class="page[^"]*" id="p-([a-z0-9]+)">', src):
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


def _without_not(sel):
    """Drop :not(...) groups; what they name does not have to exist for the rule to apply."""
    out, i = [], 0
    while i < len(sel):
        if sel.startswith(":not(", i):
            depth, i = 1, i + 5
            while i < len(sel) and depth:
                depth += {"(": 1, ")": -1}.get(sel[i], 0)
                i += 1
        else:
            out.append(sel[i])
            i += 1
    return "".join(out)


def _split_selectors(sel):
    parts, depth, cur = [], 0, ""
    for ch in sel:
        depth += {"(": 1, ")": -1}.get(ch, 0)
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    return parts + [cur]


def _alive(sel, words):
    bare = re.sub(r"\[[^\]]*\]", "", _without_not(sel))
    return all(t in words for t in re.findall(r"[.#]([A-Za-z_][A-Za-z0-9_-]*)", bare))


def _pruned(nodes, words):
    out = []
    for n in nodes:
        if n.type == "qualified-rule":
            sels = [s for s in _split_selectors(_selector(n.prelude)) if _alive(s, words)]
            if sels:
                out.append("%s{%s}" % (",".join(sels), _declarations(n.content)))
        elif n.type == "at-rule" and n.content is not None and n.lower_at_keyword in ("media", "supports"):
            inner = _pruned(tinycss2.parse_rule_list(n.content, skip_comments=True, skip_whitespace=True), words)
            if inner:
                out.append("@%s %s{%s}" % (n.lower_at_keyword, _ws(tinycss2.serialize(n.prelude)), inner))
        else:
            out.append(_rules([n]))
    return "".join(out)


def prune_style(doc):
    """A page ships only the rules that can match something on it.

    Every word in the page outside the stylesheet counts, scripts included,
    so classes that scripts add later survive."""
    a = doc.index("<style>") + len("<style>")
    b = doc.index("</style>", a)
    words = set(re.findall(r"[A-Za-z_][A-Za-z0-9_-]*", doc[:a] + doc[b:]))
    css = _pruned(tinycss2.parse_stylesheet(doc[a:b], skip_comments=True, skip_whitespace=True), words)
    used = set(re.findall(r"animation(?:-name)?:[^;}]*", css))
    def keep(m):
        return m.group(0) if any(re.search(r"\b%s\b" % re.escape(m.group(1)), u) for u in used) else ""
    css = re.sub(r"@keyframes ([A-Za-z0-9_-]+)\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}", keep, css)
    return doc[:a] + css + doc[b:]


def hero_preload(src):
    """The home page's largest picture is a stylesheet background, which the
    browser finds late. Ask for the right size up front."""
    small = re.search(r'\.hero\.vhero\{--poster:url\("([^"]+)"\)', src).group(1)
    large = re.search(r'@media \(min-width:761px\)\{\s*\.hero\.vhero\{--poster:url\("([^"]+)"\)', src).group(1)
    return ('<link rel="preload" as="image" href="%s" media="(max-width: 760px)" fetchpriority="high">'
            '<link rel="preload" as="image" href="%s" media="(min-width: 761px)" fetchpriority="high">' % (small, large))


def minify_style(head):
    """The stylesheet ships without comments or spacing; the source keeps both."""
    a = head.index("<style>") + len("<style>")
    b = head.index("</style>", a)
    css = tinycss2.parse_stylesheet(head[a:b], skip_comments=True, skip_whitespace=True)
    return head[:a] + _rules(css) + head[b:]


def links(chunk, current, paths=None):
    """Hash routes become real addresses, and the current one is marked."""
    paths = paths or {k: v[3] for k, v in PAGES.items()}
    def fix(m):
        href = paths.get(m.group(1), paths["hjem"])
        on = ' class="on"' if m.group(1) == current else ""
        return '<a href="%s"%s' % (href, on)
    chunk = re.sub(r'<a href="#([a-z]+)"(?: class="on")?', fix, chunk)
    return chunk


# ---------- languages ----------

NB_PATHS = {k: v[3] for k, v in PAGES.items()}


def _segment(key):
    """a key matches only a whole text node, attribute value or quoted string"""
    return re.compile(r'(?<=[>"\'])(\s*)' + re.escape(key) + r'(\s*)(?=[<"\'])')


SEGMENTS = sorted(en.T.items(), key=lambda kv: -len(kv[0]))
USED = set()


def to_english(doc):
    a = doc.index("<style>")
    b = doc.index("</style>", a)
    head, css, tail = doc[:a], doc[a:b], doc[b:]
    for part in ("head", "tail"):
        text = head if part == "head" else tail
        for nb, eng in SEGMENTS:
            text, n = _segment(nb).subn(lambda m: m.group(1) + eng + m.group(2), text)
            if n:
                USED.add(nb)
        for nb, eng in en.RAW:
            if nb in text:
                USED.add(nb)
                text = text.replace(nb, eng)
        if part == "head":
            head = text
        else:
            tail = text
    # internal addresses point at the English pages
    def addr(m):
        for slug, nbp in NB_PATHS.items():
            if slug in en.PATHS and m.group(1) == nbp:
                return 'href="%s"' % en.PATHS[slug]
        return m.group(0)
    head = re.sub(r'href="(/[^"#?]*)"', addr, head)
    tail = re.sub(r'href="(/[^"#?]*)"', addr, tail)
    return head + css + tail


NB_WORDS = re.compile(r"[æøåÆØÅ]|\b(og|jeg|det|ikke|som|på|til|med|av|er|du|en|et|der|hva|hvor|bilder|bolig\w*)\b")
KEEP = ("Heyerdahls vei", "Bærum", "Frognerveien", "Datatilsynet", "Izazovi Avanturu", "Nordre Follo",
        "Zeljković", "ZEJAKOV", "youtube-nocookie", "Sending …")


def leftovers(doc):
    """Norwegian still visible on an English page: text, alt, aria-label, placeholder, content."""
    body = re.sub(r"<style>.*?</style>", "", doc, flags=re.S)
    body = re.sub(r"<script\b[^>]*>.*?</script>", "", body, flags=re.S)
    bits = re.findall(r">([^<>]+)<", body) + re.findall(r'(?:alt|aria-label|placeholder|title|content)="([^"]+)"', body)
    out = []
    for t in bits:
        t = " ".join(t.split())
        if not t or t.startswith(("http", "/")) or not NB_WORDS.search(t):
            continue
        if any(k in t for k in KEEP) and not re.search(r"\b(og|jeg|ikke|som|på|med|av|er|du)\b", t):
            continue
        out.append(t)
    return out


def lang_switch(doc, slug, lang):
    """NO / EN pill: each points at this same page in that language; the current one is lit"""
    nb_href = NB_PATHS[slug]
    en_href = en.PATHS.get(slug, en.PATHS["hjem"])
    for code, href in (("nb", nb_href), ("en", en_href)):
        on = ' class="on" aria-current="page"' if code == lang else ""
        doc = doc.replace('<a href="#lang-%s"' % code, '<a href="%s"%s' % (href, on), 1)
    return doc


def alternates(slug):
    if slug not in en.PATHS:
        return ""
    nb_url, en_url = SITE + NB_PATHS[slug], SITE + en.PATHS[slug]
    return ('<link rel="alternate" hreflang="nb" href="%s"><link rel="alternate" hreflang="en" href="%s">'
            '<link rel="alternate" hreflang="x-default" href="%s">' % (nb_url, en_url, nb_url))


def main():
    src = open(SRC, encoding="utf-8").read()
    head_end = src.index("</head>") + len("</head>")
    head, rest = src[:head_end], src[head_end:]
    head = minify_style(head)
    before, mains, after = split(rest)

    written, problems = [], []
    jobs = [("nb", s) for s in ORDER] + [("en", s) for s in ORDER if s in en.PATHS]
    for lang, slug in jobs:
        path, title, desc, href = PAGES[slug]
        if lang == "en":
            title, desc = en.META[slug]
            href = en.PATHS[slug]
            path = href.strip("/") + "/index.html"
        url = SITE + href
        page = mains[slug][2]
        # the page's own heading is the document heading, once it is a document
        if slug != "hjem":
            i = page.index("<h2")
            j = page.index("</h2>", i)
            page = page[:i] + "<h1" + page[i + 3:j] + "</h1>" + page[j + len("</h2>"):]
        page = page.replace('<main class="page" id=', '<main class="page live" id=', 1)

        nav = NAV.get(slug, slug)
        paths = NB_PATHS if lang == "nb" else dict(NB_PATHS, **en.PATHS)
        doc = meta(head, title, desc, url) + links(before, nav, paths) + page + links(after, nav, paths)
        if lang == "en":
            doc = to_english(doc)
            problems += [(path, t) for t in leftovers(doc)]
        doc = lang_switch(doc, slug, lang)
        doc = doc.replace("</head>", alternates(slug) + "</head>", 1)
        if slug in HIDDEN:
            doc = re.sub(r'<link rel="canonical" href="[^"]*">', '<meta name="robots" content="noindex">', doc, count=1)
        # the skip link lands on this page's own content
        doc = doc.replace('href="#innhold"', 'href="#p-%s"' % slug, 1)
        doc = prune_style(doc)
        if slug == "hjem":
            doc = doc.replace("</head>", hero_preload(src) + "</head>", 1)
        out = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        open(out, "w", encoding="utf-8").write(doc)
        written.append((path, len(doc)))

    today = datetime.date.today().isoformat()
    locs = [PAGES[s][3] for s in ORDER if s not in HIDDEN] + [en.PATHS[s] for s in ORDER if s in en.PATHS]
    urls = "\n".join('  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>' % (SITE, h, today) for h in locs)
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % urls)

    for path, n in written:
        print("%-24s %6.1f KB" % (path, n / 1024))
    print("sitemap.xml              %d urls" % len(locs))
    unused = [k for k in list(en.T) + [a for a, b in en.RAW] if k not in USED]
    for k in unused:
        print("EN: not found in the source any more:", k[:90])
    for path, t in problems:
        print("EN: Norwegian left on %s: %s" % (path, t[:110]))
    if not unused and not problems:
        print("EN: every piece translated")


if __name__ == "__main__":
    main()
