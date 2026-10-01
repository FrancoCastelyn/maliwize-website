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
from catalogue import PRODUCTS, RETAILERS, ROOT  # noqa: E402

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


def fetch(dest, urls):
    if dest.exists() and not FORCE:
        print(f"keep   {dest.relative_to(ROOT)}")
        return True
    for url in urls:
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
    print(f"FAILED {dest.relative_to(ROOT)}")
    return False


ok = all([fetch(ROOT / "assets/retailers" / f, [u]) for _, f, u in RETAILERS]
         + [fetch(ROOT / "assets/products/originals" / f.replace(".webp", ".png"), urls) for _, _, _, f, urls in PRODUCTS])
sys.exit(0 if ok else 1)
