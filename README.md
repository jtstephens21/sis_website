# Pearl Counseling Website

A warm, professional one-page website for Pearl Counseling, built with plain
HTML/CSS/JS — no build step, no framework, ready to host for free.

```
├── index.html          the whole site (one scrolling page)
├── styles.css           all styling
├── script.js             nav menu, scroll animations, contact form
├── assets/images/    your photos, headshots, and logo (already optimized)
└── README.md          (this file)
```

## 1. Put it on GitHub Pages (free hosting)

1. Create a new repository on GitHub (e.g. `pearl-counseling-site`). It can be public or private — Pages works with both on a free plan, but a private repo's site is still publicly visible once Pages is on.
2. Upload all the files in this folder to the repository, keeping the folder structure (the `assets` folder must stay in place).
   - Easiest way if you don't use git: on the repo page, click **Add file → Upload files**, drag in everything, and commit.
3. In the repo, go to **Settings → Pages**.
4. Under "Build and deployment," set **Source** to "Deploy from a branch," pick the `main` branch and `/ (root)` folder, then **Save**.
5. GitHub will give you a URL like `https://your-username.github.io/pearl-counseling-site/` — it usually goes live within a minute or two.
6. (Optional) If she buys a custom domain later (e.g. `pearlcounseling.com`), you can point it at GitHub Pages under the same Settings → Pages screen ("Custom domain").

## 2. Connect the contact form (Formspree — free)

The contact form is already built and styled, it just needs to be pointed at
a real inbox. This site uses **Formspree**, a free service made exactly for
this (static sites with no backend).

1. Go to [formspree.io](https://formspree.io) and sign up for a free account.
2. Click **New Form**, give it a name (e.g. "Pearl Counseling — Contact"), and set it to send to her email.
3. Formspree will give you a form endpoint that looks like:
   `https://formspree.io/f/abcdwxyz`
4. Open `index.html`, find this line (search for `YOUR_FORM_ID`):
   ```html
   <form id="contactForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```
   and replace `YOUR_FORM_ID` with the ID Formspree gave you.
5. Push/re-upload the updated `index.html` to GitHub.
6. Submit the form once yourself from the live site — Formspree will send a confirmation email the first time, and you'll need to click "Confirm" there before it starts forwarding submissions.

The free Formspree plan includes 50 submissions/month, which is typically
plenty for a small practice's contact form. Formspree also has built-in spam
filtering.

## 3. What still needs her input

The site was built entirely from the bio and photos provided. A few things
were left out on purpose because they weren't specified, and should be added
before this goes fully live:

- **Session format** — the site doesn't currently state whether sessions are in-person, telehealth, or both. Add a line to the hero subhead or the Services section once that's confirmed.
- **Email/phone** — per your request, only the contact form is shown (no email or phone listed directly). If she'd like a direct email or phone number displayed too, that can be added to the footer or Contact section.
- **Credentials/license info** — most therapist sites list license type and number (e.g. state licensing board requirements vary). Worth checking what her state requires.
- **Practice location/service area** — not currently mentioned anywhere on the site.

## 4. Editing text or images later

- All the visible text lives in `index.html` — search for the section you want (each is marked with a `<!-- ============ SECTION ============ -->` comment) and edit directly.
- To swap a photo, replace the file in `assets/images/` with a new one **using the same filename**, or update the `src="assets/images/..."` path in `index.html` if you rename it.
- Colors and fonts are defined once at the top of `styles.css` under `:root` — changing a value there (e.g. `--terracotta`) updates it everywhere on the site.

## Image credits

Most of the nature/lifestyle photography is from Unsplash (free to use, no
attribution legally required, but credited here as good practice):
Alysha Rosly, Amy Humphries, Andrew Seaman, Chetan Kolte, Felix Ngo,
Ioann-Mark Kuznietsov, Jon Flobrant, Jonathan Borba, Kelly Sikkema,
Luke Carliff, Phil Hearing, Saffu, Vince Fleming, and Wonderlane.
