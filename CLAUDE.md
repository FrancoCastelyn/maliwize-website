# CLAUDE.md — maliwize-website

Read `README.md` first. This repo is the public face of a South African fintech whose members are
often in debt review, so the copy carries the same rails as the app:

- **Rewards come from saving and budget discipline, never from spending.** No spend targets, no
  "spend more to earn more", no leaderboards of spend.
- **Grocery coupons are "coupons" or "rands off selected items"**, never "discounts" or "vouchers".
  Any savings claim says that savings depend on what you buy. The only rand figures for savings are
  the capped claims: up to R1 750 a month for a family of 5–6 and up to R750 for 2–4, grocery coupons
  only (Hey Fill CLAUDE.md §3.4; approved for the site by Franco, 1 Oct 2026).
- **Maliwize gives no financial advice, lends nothing, and holds or moves no money.** Never describe
  a wallet as live, never offer credit or buy-now-pay-later, never steer anyone to a financial product.
- **No demographic targeting**, in words or in images.
- **Privacy wording is a summary.** The policy members agree to lives in the app. Anything new about
  data handling goes past Franco first, and legal points are phrased as facts only once counsel agrees.
- No prices, partner names, retailer names or commercial terms until Franco says they are public.
  Public since 1 Oct 2026: the retailers Shoprite Checkers, Pick n Pay and Dis-Chem, their logos, and
  product pictures from the coupon catalogue (`tools/catalogue.py`).
- Do not say what is never shared with Hey Fill. Sharing may grow (Franco, 1 Oct 2026); the policy in
  the app is where the detail lives.
- Contact addresses: support@maliwize.co.za for members and data questions, info@maliwize.co.za for
  partners and general enquiries.

`node tools/check.mjs` must pass before any commit. Never merge; push a branch and open a PR.
