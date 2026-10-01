# maliwize-website

The public Maliwize website, served at **maliwize.co.za**. The app lives in
`FrancoCastelyn/Powerstack` and moves to **app.maliwize.co.za** (scoping board Q-11, AC56).

Plain HTML and one stylesheet. No framework, no JavaScript, no build step at deploy: what is in
this repo is exactly what Netlify serves. That keeps it fast on a cheap phone and gives search
engines real text to read, which the app, drawn in the browser behind its launch gate, cannot.

## Edit

1. Change copy in `tools/pages.py` (every page, the header and the footer live there).
2. `python3 tools/pages.py` writes the HTML and `sitemap.xml`.
3. `node tools/check.mjs` must pass. Netlify runs it as the build command, so a failing page is
   never published.

Styles are in `assets/site.css`, on the brand tokens (Ink Navy, Deep Teal, Growth Green, Signal Lime,
Plus Jakarta Sans). Screens use the gradient once, in the hero.

## What the check enforces

- Copy rules: nothing ties rewards to spending, no "discount" or "voucher" for grocery coupons, no
  loans or credit, no wallet, no guarantees, and "financial advice" only in the line that says
  Maliwize does not give it.
- One `h1`, a title and a description of search-friendly length, `lang="en-ZA"`, and no scripts.
- Every internal link and image resolves; every sitemap entry exists; the header and footer are
  identical on every page; app links use the one `APP` address.

## Deploy

A Netlify project on this repo: publish directory `.`, build command `node tools/check.mjs`
(both set in `netlify.toml`, along with the security headers). Review it on the Netlify preview
address first. The domain moves only with the app move in `docs/APP-MOVE.md`.
