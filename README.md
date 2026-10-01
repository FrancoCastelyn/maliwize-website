# maliwize-website

The public Maliwize website, served at **maliwize.co.za**. The app lives in
`FrancoCastelyn/Powerstack` at **app.maliwize.co.za** (scoping board Q-11, AC56).

Plain HTML and one stylesheet. No framework, no JavaScript, no build step at deploy: what is in
this repo is exactly what Netlify serves. That keeps it fast on a cheap phone and gives search
engines real text to read, which the app, drawn in the browser behind its launch gate, cannot.

The phones on the pages are not screenshots. They are the app's screens drawn in HTML and CSS
(`tools/phones.py`), in the app's own words, so they never go stale and weigh a few kilobytes.
Every animation is CSS: the hero phones rise and float, numbers count up, bars fill and the
Maliscore ring draws itself as you scroll. Each one has a correct final state when animation is
off (`prefers-reduced-motion`) or unsupported, and scroll-driven animation is a progressive
enhancement behind `@supports`.

## Edit

1. Change copy in `tools/pages.py` (every page, the header and the footer live there). Phone
   screens and their sample values live in `tools/phones.py`.
2. `python3 tools/pages.py` writes the HTML and `sitemap.xml`.
3. `node tools/check.mjs` must pass. Netlify runs it as the build command, so a failing page is
   never published.

Styles are in `assets/site.css`, on the brand tokens (Ink Navy, Deep Teal, Growth Green, Signal Lime,
Plus Jakarta Sans). Hey Fill's section and page use Hey Fill's own palette (blue `#0076CA`, cyan
`#00A2E7`, orange `#FD8514`, the logo red `#D70027`), scoped to `.hf-band`, `.hf-hero` and the `.hf`
screens; the header, footer, type family and copy rules stay the same around it. The brand SVGs are
`assets/heyfill-lockup*.svg` and `assets/heyfill-mark.svg`, from `HPS-Tech-Org/Hey-Fill`.

The site's Content Security Policy allows no inline styles, so bar and counter values are the
`p05`–`p100` and `n-…` utility classes at the end of `site.css`, never `style=` attributes.

## Retailers and products

`tools/catalogue.py` lists the retailers and products the pages show, from the Hey Fill coupon
catalogue. Logos and product pictures are files under `assets/` (the CSP allows no other image
host). To refresh them on a machine that can reach the catalogue's image hosts:

    python3 tools/fetch-catalogue-images.py   # originals into assets/products/originals (git-ignored)
    node tools/shrink-images.mjs              # 320px WebP files the pages use (needs Playwright)
    python3 tools/pages.py && node tools/check.mjs

Until a logo or picture is present the page shows the retailer's name, or a plain basket, instead.
Bump `CSS_VERSION` in `tools/pages.py` whenever `assets/site.css` changes, because `/assets/*` is
cached for a week.

## Pages

`/` · `/how-it-works/` · `/maliscore/` · `/rewards/` (Hey Fill Rewards) · `/contact/` (with `#partners`)
· `/privacy/` (linked from the footer) · `404.html`.

## What the check enforces

- Copy rules: nothing ties rewards to spending, no "discount" or "voucher" for grocery coupons, no
  loans or credit, no wallet, no guarantees, "financial advice" only in the line that says
  Maliwize does not give it, no retailer or partner names beyond the three approved ones, no prices,
  and no savings figure except "up to R1 750" or "up to R750" a month on a page that says savings
  depend on what you buy.
- One `h1`, a title and a description of search-friendly length, `lang="en-ZA"`, no scripts, no
  inline styles or event handlers (the CSP would block them).
- Every internal link and image resolves; every sitemap entry exists; the header and footer are
  identical on every page; app links use the one `APP` address; the `_redirects` rules send old app
  paths to the app without shadowing a website page.

## Deploy

A Netlify project on this repo: publish directory `.`, build command `node tools/check.mjs`
(both set in `netlify.toml`, along with the security headers). Review it on the Netlify preview
address first. The domain move is in `docs/APP-MOVE.md`.

`assets/og-image.png` is rendered from the live styles with headless Chromium (1200×630); re-render
it when the hero changes.
