"""The retailers and products the site shows, taken from the Hey Fill coupon catalogue (the
`retailer` and `offer` tables on Hey-Fill-dev, read 1 Oct 2026). Approved for the public site by
Franco on 1 Oct 2026.

The site's Content Security Policy only allows images served from the site itself, so every logo
and product picture is a file under assets/. `python3 tools/fetch-catalogue-images.py` downloads
them from the catalogue's own image hosts. Until a file is there, the pages show the retailer's
name, or a plain basket, in its place, so the site always builds and never shows a broken image.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SB = "https://qgxgmtffegwdvmghkbqd.supabase.co/storage/v1/object/public/offer-images"
CDN = "https://sac-prod.ams3.cdn.digitaloceanspaces.com/public/images"

# (name, file under assets/retailers/, source URL)
RETAILERS = [
    ("Shoprite Checkers", "shoprite-checkers.png", f"{CDN}/retailers/3Y8PuA3Cln6c0Jx87EqRe25p8VU297RCJgePZ2hF.png"),
    ("Pick n Pay", "pick-n-pay.png", f"{CDN}/retailers/95CYxtZdZGSLV4GxUOXDZ0rn08EZj4RsMjWBWmLQ.png"),
    ("Dis-Chem", "dis-chem.png", f"{CDN}/retailers/LPBnf0qSWLsal026mZSI2IGUoujNjv9j94TpYvUy.png"),
]

# (key, product name, retailer, file under assets/products/, [source URLs]). Pictures are stored as
# small WebP files (320px wide); tools/shrink-images.mjs makes them from what the fetch script saves.
S3 = "https://wiproduct-za-vsp-prod-cvs.s3-eu-west-1.amazonaws.com/images"
PRODUCTS = [
    ("milk", "Parmalat Everfresh Milk 6 x 1L", "Pick n Pay", "parmalat-milk.webp", [f"{S3}/06765ab0b5a17273181c7bf6cdc48c6ba026a0db.png"]),
    ("peanut", "Black Cat Peanut Butter 800g", "Pick n Pay", "black-cat-peanut-butter.webp", [f"{S3}/c758902075a60084cee5f940d9d43a63ae29f917.png"]),
    ("allgold", "All Gold Squeeze Bottle 500ml", "Pick n Pay", "all-gold-squeeze.webp", [f"{S3}/7230256887fdf1c0c2c1ea8d625b9aa02b443b79.png"]),
    ("washing", "Bio Classic Washing Powder 3kg", "Pick n Pay", "bio-classic-washing-powder.webp", [f"{S3}/1fee8acc76ffda035984082fa4fd57fcf23f0e3a.png"]),
    ("smartfood", "Futurelife Smartfood 500g", "Pick n Pay", "futurelife-smartfood.webp", [f"{S3}/2fd3de2d46b228ea4fd5eaf42dec99bca94592eb.png"]),
    ("oats", "Futurelife Smart Oats 500g", "Dis-Chem", "futurelife-smart-oats.webp", [f"{S3}/5d15c7b645d0761d639a7295796b14fc43fc3d79.png"]),
    ("crunch", "Futurelife Crunch 425g", "Dis-Chem", "futurelife-crunch.webp", [f"{S3}/b3039fd861c69f1f01ae201d81716e994fefdb45.png"]),
    ("worcester", "Colmans Holbrooks Worcestershire Sauce 500ml", "Pick n Pay", "holbrooks-worcestershire.webp", [f"{S3}/b7baed20e18eadb82d4a998ba9e1b56544f4bfef.png"]),
    # Shoprite Checkers pictures live on the SA Coupons CDN and Hey-Fill-dev storage.
    ("maize", "Pride Super Maize Meal 12.5kg", "Shoprite Checkers", "pride-maize-meal.webp",
     [f"{SB}/coupon-30578.png", f"{CDN}/products/72taTEnURemybPiffGuSxfIdqurlWsAiM87BXaNx.png"]),
    ("rice", "Allsome Parboiled Rice 10kg", "Shoprite Checkers", "allsome-rice.webp",
     [f"{SB}/coupon-18694.png", f"{CDN}/products/QnahTH55Qanw47D5plQixFKgZrIBMHJtmXcSlULY.png"]),
]

BY_KEY = {p[0]: p for p in PRODUCTS}

BASKET = (
    '<svg class="basket-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9h18l-2 10.5a1.5 1.5 0 0 1-1.5 1.2h-11A1.5 1.5 0 0 1 5 19.5zM8 9l4-5.5L16 9" '
    'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'
)


def has(rel):
    return (ROOT / rel).is_file()


def product_img(key, alt=""):
    """The product picture, or a plain basket until the file has been fetched."""
    _, name, _, file, _ = BY_KEY[key]
    rel = f"assets/products/{file}"
    if has(rel):
        return f'<img src="/{rel}" alt="{alt}" loading="lazy" decoding="async" width="160" height="160">'
    return BASKET


def retailer_mark(name, file):
    rel = f"assets/retailers/{file}"
    if has(rel):
        return f'<img src="/{rel}" alt="{name}" loading="lazy" decoding="async" width="200" height="80">'
    return f'<span class="retailer-name">{name}</span>'


def retailers_row():
    items = "".join(f'<li class="retailer">{retailer_mark(n, f)}</li>' for n, f, _ in RETAILERS)
    return f'<ul class="retailers" aria-label="Where you can use your coupons">{items}</ul>'


def product_grid(keys):
    cards = []
    for k in keys:
        _, name, retailer, _, _ = BY_KEY[k]
        cards.append(
            f'<li class="pcard reveal"><div class="pcard-pic">{product_img(k)}<span class="pcard-off">Rands off</span></div>'
            f'<b>{name}</b><span>{retailer}</span></li>'
        )
    return f'<ul class="pgrid">{"".join(cards)}</ul>'
