# Pearl Counseling — Netlify + Decap CMS version

This is an alternate build of the same site, restructured so Lee Ann can
edit text, swap photos, and add her modalities herself through a
point-and-click editor (Decap CMS) instead of touching code — at the cost
of more setup up front. See the chat for the full comparison against the
plain-HTML/GitHub Pages version.

Visually and content-wise it's the same site. Under the hood:
- Built with **Eleventy** (a static site generator) instead of hand-written HTML
- All editable text lives in `src/_data/pages/*.json` — the templates in `src/*.njk` just fill those values into the same design (`styles.css` is untouched, byte-for-byte the same file)
- `src/admin/` is the Decap CMS editor interface

```
├── src/
│   ├── _includes/base.njk        shared header/nav/footer template
│   ├── _data/
│   │   ├── site.json                email, phone, business name, nav
│   │   └── pages/
│   │       ├── home.json, about.json, approach.json,
│   │       └── services.json, contact.json    ← editable page content
│   ├── index.njk, about.njk, approach.njk,
│   │   services.njk, contact.njk    page templates (rarely need editing)
│   ├── admin/
│   │   ├── index.html                 Decap CMS entry point
│   │   └── config.yml                  defines what's editable & how
│   ├── assets/images/                photos + logo
│   ├── styles.css / script.js
├── eleventy.config.js
├── netlify.toml
└── package.json
```

## 1. Deploy to Netlify (free)

1. Push this whole folder to a GitHub repo (same idea as before — a new repo, or reuse the existing one on a different branch).
2. Go to [netlify.com](https://netlify.com), sign up free, click **Add new site → Import an existing project**, and connect the GitHub repo.
3. Netlify will auto-detect `netlify.toml` (build command `npm run build`, publish folder `_site`) — just click **Deploy**.
4. In a minute or two, the site is live at something like `random-name-123.netlify.app`. You can rename that subdomain, or attach a real domain, under **Site configuration → Domain management**.

## 2. Turn on the content editor (Netlify Identity + Git Gateway)

This is what lets Lee Ann log in and edit content without a GitHub account.

1. In the Netlify dashboard for this site, go to **Site configuration → Identity** and click **Enable Identity**.
2. Under Identity → **Registration**, set it to **Invite only** (so random people can't sign up).
3. Under Identity → **Services → Git Gateway**, click **Enable Git Gateway**. This lets the CMS save changes back to GitHub on her behalf, without her needing her own GitHub login.
4. Go to the **Identity** tab (top-level, not settings) and click **Invite users** — enter Lee Ann's email. She'll get an email invite to set a password.
5. Open `src/admin/config.yml` and replace the two `REPLACE-WITH-YOUR-NETLIFY-URL` placeholders with the site's actual Netlify URL, then redeploy.

Once that's done, she goes to `yoursite.netlify.app/admin/`, logs in with the password from her invite email, and sees a form-based editor — one section per page, matching what's on this site.

## 3. Editing the modalities (or anything else)

In the CMS, under **My Approach Page**, there's a **Modalities** list field —
empty right now on purpose. Click **Add Modalities**, fill in a name and a
short description, repeat for each one, then **Publish**. The site rebuilds
automatically and the new section appears on the live Approach page within
a minute or two (it's hidden entirely until at least one modality is added,
so there's no empty placeholder showing in the meantime).

Every other page works the same way — click into a page in the left sidebar,
edit the fields, hit Publish.

## 4. The contact form (Netlify Forms — no third-party service)

The form on `contact.html` uses **Netlify Forms**, built into the same
hosting already being used — no separate account needed.

1. Once the site is deployed, Netlify automatically detects the form (it's looking for the `data-netlify="true"` attribute, already in the markup) and starts collecting submissions.
2. To get an email every time someone submits: **Site configuration → Forms → Form notifications → Add notification → Email notification**, and enter leeannchilderscounseling@gmail.com.
3. Submissions also live permanently in the Netlify dashboard under **Forms**, even without email notifications turned on.
4. There's a basic spam-blocking honeypot field already built in (invisible to real visitors, catches simple bots) — no setup needed.

Free Netlify plan includes 100 submissions/month, which is more than enough
for a small practice's contact form.

## 5. Testing locally before deploying

```
npm install
npm start
```
opens the site at `http://localhost:8080` with live-reload.

To test the CMS editor itself locally (optional — most people just test this
after it's live on Netlify):
```
npx decap-server
```
in a second terminal, and uncomment the `local_backend: true` line near the
top of `src/admin/config.yml`. Comment it back out before deploying — it's
only for local testing and shouldn't ship to production.

## Image credits

Same as the other version — most nature/lifestyle photography is from
Unsplash (free to use): Alysha Rosly, Amy Humphries, Andrew Seaman, Chetan
Kolte, Felix Ngo, Ioann-Mark Kuznietsov, Jon Flobrant, Jonathan Borba, Kelly
Sikkema, Luke Carliff, Phil Hearing, Saffu, Vince Fleming, and Wonderlane.
