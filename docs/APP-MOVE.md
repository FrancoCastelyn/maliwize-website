# Moving the app to app.maliwize.co.za (scoping board AC56)

**Progress, 1 Oct 2026:** `app.maliwize.co.za` is live on the app's Netlify project (covered by the
existing `*.maliwize.co.za` certificate), Supabase Site URL, redirect URLs and `APP_BASE_URL` are
set, and sign-in works there. `_redirects` in this repo and the site's sign-in links already point
at the app. What remains is the domain move itself and the checks after it.

Done as its own release, after the site has been reviewed on its Netlify preview address.

## Before the switch (Franco, dashboards)

1. **Netlify, app project (`maliwize`)**: add the domain `app.maliwize.co.za`.
2. **Supabase Auth, production project**: set Site URL to `https://app.maliwize.co.za` and add it to
   the redirect URLs. Keep `https://maliwize.co.za/**` in the list until the switch is done.
3. **Function secret `APP_BASE_URL`** on production: `https://app.maliwize.co.za`. The links in SMS
   and email are built from it.
4. **PayFast**: return, cancel and notify URLs to the new host.
5. **SendGrid templates and any printed material** that name maliwize.co.za for signing in.

## At the switch

1. Move `maliwize.co.za` and `www` from the app's Netlify project to this site's.
2. Add `_redirects` to this repo, so links already sent keep working. Claim links matter most:

   ```
   /r/*          https://app.maliwize.co.za/r/:splat          301
   /login        https://app.maliwize.co.za/auth              301
   /auth/*       https://app.maliwize.co.za/auth/:splat       301
   /settings/*   https://app.maliwize.co.za/settings/:splat   301
   /admin/*      https://app.maliwize.co.za/admin/:splat      301
   ```

   Take the full route list from `src/App.tsx` in Powerstack at the time of the move; the list above
   is what exists on 30 Sep 2026 and is not complete.
3. Change `APP` in `tools/pages.py` and `tools/check.mjs` to `https://app.maliwize.co.za`,
   regenerate, and check.

## After

- Sign in, a claim link from an old SMS, a password reset email and a PayFast sandbox payment, all
  end to end.
- Verify maliwize.co.za in Google Search Console and submit `https://maliwize.co.za/sitemap.xml`.
