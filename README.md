# Pearl Counseling Website

A warm, professional website for Pearl Counseling (Lee Ann Childers), built
with plain HTML/CSS/JS — no build step, no framework, ready to host for free.

```
├── index.html          Home
├── about.html            About Me
├── approach.html      My Approach
├── services.html         Services
├── contact.html          Contact
├── styles.css              all styling (shared across pages)
├── script.js                nav menu, scroll animations, contact form
├── build.py                the script used to generate the 5 HTML pages
│                          from shared header/footer templates — re-run
│                          this after editing it, or just hand-edit the
│                          .html files directly, either works
└── assets/images/    photos, headshots, and logo (already optimized)
```

## 1. Put it on GitHub Pages (free hosting)

1. Create a new repository on GitHub (e.g. `pearl-counseling-site`).
2. Upload all the files in this folder to the repository, keeping the folder structure (the `assets` folder must stay in place). `build.py` is optional to include — it's only needed if you want to regenerate the pages later.
   - Easiest way if you don't use git: on the repo page, click **Add file → Upload files**, drag in everything, and commit.
3. In the repo, go to **Settings → Pages**.
4. Under "Build and deployment," set **Source** to "Deploy from a branch," pick the `main` branch and `/ (root)` folder, then **Save**.
5. GitHub will give you a URL like `https://your-username.github.io/pearl-counseling-site/` — it usually goes live within a minute or two.
6. (Optional) Once there's a custom domain (e.g. `pearlcounseling.com`), it can be pointed at GitHub Pages from that same Settings → Pages screen ("Custom domain").

## 2. Connect the contact form (Formspree — free)

The contact form on `contact.html` is already built and styled, it just needs
to be pointed at a real inbox. This site uses **Formspree**, a free service
made exactly for this (static sites with no backend).

1. Go to [formspree.io](https://formspree.io) and sign up for a free account.
2. Click **New Form**, give it a name (e.g. "Pearl Counseling — Contact"), and set it to send to leeannchilderscounseling@gmail.com.
3. Formspree will give you a form endpoint that looks like:
   `https://formspree.io/f/abcdwxyz`
4. Open `contact.html`, find this line (search for `YOUR_FORM_ID`):
   ```html
   <form id="contactForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```
   and replace `YOUR_FORM_ID` with the ID Formspree gave you.
5. Push/re-upload the updated `contact.html` to GitHub.
6. Submit the form once yourself from the live site — Formspree sends a confirmation email the first time, and you'll need to click "Confirm" there before it starts forwarding submissions.

The free Formspree plan includes 50 submissions/month, which is typically
plenty for a small practice's contact form. Formspree also has built-in spam
filtering.

## 3. The QR code (once the domain + form are live)

Once the site has its final home (either the github.io URL or a custom
domain) and the Formspree form is connected and confirmed, send whoever's
doing the printing a direct link to the live contact page — e.g.
`https://pearlcounseling.com/contact.html` (or whatever the final domain is).
Most printers/designers can generate the QR code themselves from that URL;
if not, free QR generators like qr-code-generator.com or the QR tool built
into Canva can turn that link into a downloadable PNG/SVG in a few seconds.
Happy to help with this step directly once the URL is final.

## 4. What's already on the site vs. what's still coming

Already included, per Lee Ann's latest notes:
- Email, phone, and contact form all shown together on the Contact page
- Both in-person and telehealth mentioned (no stated preference)
- Rate ($120/session) and "insurance not currently accepted" — no mention of sliding scale
- "Interested in scheduling appointments? Or just have a question?" heading, and a 48-business-hour response time note

Still to come, once she sends it:
- **Modalities** — there's a natural home for this on `approach.html`, right after the three Connection/Curiosity/Self-Compassion cards. Just send the list and it can be dropped in.
- Any additional contact-page details she wants after reviewing this version.

## 5. Editing text or images later

- Since this is now a 5-page site, the easiest way to make edits is through `build.py` — the page text lives in that file, organized by page (search for `index_body`, `about_body`, etc.), and the header/footer are defined once at the top and shared by all five pages. Edit the relevant string, then run:
  ```
  python3 build.py
  ```
  to regenerate the .html files.
- Alternatively, each `.html` file can be hand-edited directly — just know that if `build.py` is run again afterward, it will overwrite those files with whatever's in the script.
- To swap a photo, replace the file in `assets/images/` with a new one **using the same filename**, or update the `src="assets/images/..."` path.
- Colors and fonts are defined once at the top of `styles.css` under `:root` — changing a value there (e.g. `--terracotta`) updates it everywhere on the site.

## Image credits

Most of the nature/lifestyle photography is from Unsplash (free to use, no
attribution legally required, but credited here as good practice):
Alysha Rosly, Amy Humphries, Andrew Seaman, Chetan Kolte, Felix Ngo,
Ioann-Mark Kuznietsov, Jon Flobrant, Jonathan Borba, Kelly Sikkema,
Luke Carliff, Phil Hearing, Saffu, Vince Fleming, and Wonderlane.
