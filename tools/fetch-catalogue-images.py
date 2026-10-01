#!/usr/bin/env python3
"""Downloads the retailer logos and product pictures listed in tools/catalogue.py into assets/.
Then shrink the product pictures and regenerate the pages so they use them:

    python3 tools/fetch-catalogue-images.py
    node tools/shrink-images.mjs
    python3 tools/pages.py
    node tools/check.mjs

Run it on a machine that can reach the catalogue's image hosts (the Supabase storage of
Hey-Fill-dev, the SA Coupons CDN and the wiGroup asset hosts). Existing files are kept unless you
pass --force. A product with more than one source tries them in order.
"""
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalogue import PRODUCTS, RETAILERS, ROOT, SHOW_LOGOS  # noqa: E402

FORCE = "--force" in sys.argv
MAX_BYTES = 3_000_000  # originals; shrink-images.mjs makes the files the pages use


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "maliwize-website/1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        ctype = r.headers.get("content-type", "")
        data = r.read()
    if not ctype.startswith("image/"):
        raise ValueError(f"not an image ({ctype})")
    return data


def fetch(base, urls):
    """`base` is the path without an extension; each download keeps its source's own type."""
    found = [p for p in base.parent.glob(base.name + ".*")] if base.parent.exists() else []
    if found and not FORCE:
        print(f"keep   {found[0].relative_to(ROOT)}")
        return True
    for url in urls:
        dest = base.with_name(base.name + "." + url.rsplit(".", 1)[-1].lower())
        try:
            data = get(url)
        except Exception as e:  # try the next source
            print(f"  miss {url}: {e}")
            continue
        if len(data) > MAX_BYTES:
            print(f"  skip {url}: {len(data)} bytes is too big for a tile")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        print(f"saved  {dest.relative_to(ROOT)} ({len(data) // 1024} KB)")
        return True
    print(f"FAILED {base.relative_to(ROOT)}")
    return False


logos = [fetch(ROOT / "assets/retailers" / f.rsplit(".", 1)[0], [u]) for _, f, u in RETAILERS] if SHOW_LOGOS else []
if not SHOW_LOGOS:
    print("logos skipped: SHOW_LOGOS is off in tools/catalogue.py until their use is approved")
ok = all(logos + [fetch(ROOT / "assets/products/originals" / f.rsplit(".", 1)[0], urls) for _, _, _, f, urls in PRODUCTS])
sys.exit(0 if ok else 1)
