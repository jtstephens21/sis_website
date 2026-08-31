import os

OUT = "/home/claude/work2"

NAME = "Lee Ann Childers"
EMAIL = "leeannchilderscounseling@gmail.com"
PHONE = "(615) 549-8145"
PHONE_TEL = "+16155498145"
EMAIL_DISPLAY = EMAIL.replace("@", "<wbr>@")

PAGES = ["index", "about", "approach", "services", "contact"]
NAV_LABELS = {
    "index": ("Home", "index.html"),
    "about": ("About", "about.html"),
    "approach": ("My Approach", "approach.html"),
    "services": ("Services", "services.html"),
    "contact": ("Contact", "contact.html"),
}

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">

<link rel="icon" type="image/png" href="assets/images/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,500;1,9..144,600&family=Work+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
"""

def nav(active):
    links = ""
    for key in ["about", "approach", "services", "contact"]:
        label, href = NAV_LABELS[key]
        cls = ' class="active"' if key == active else ""
        links += f'        <li><a href="{href}"{cls}>{label}</a></li>\n'
    home_active = ' class="active"' if active == "index" else ""
    return f"""<header class="site-header" id="siteHeader">
  <div class="nav-inner">
    <a href="index.html" class="brand">
      <img src="assets/images/logo.png" alt="Pearl Counseling logo">
    </a>
    <nav>
      <ul class="nav-links" id="navLinks">
{links}      </ul>
    </nav>
    <div class="nav-cta">
      <a href="contact.html" class="btn btn-primary">Reach Out</a>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
"""

FOOTER = f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="assets/images/logo.png" alt="Pearl Counseling logo">
        <span>Pearl Counseling</span>
      </div>
      <ul class="footer-links">
        <li><a href="about.html">About</a></li>
        <li><a href="approach.html">My Approach</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
    <div class="footer-top" style="border-bottom:none; padding-top:26px;">
      <div style="display:flex; gap:28px; flex-wrap:wrap; font-size:14.5px;">
        <a href="mailto:{EMAIL}" style="color:rgba(250,246,238,0.85);">{EMAIL_DISPLAY}</a>
        <a href="tel:{PHONE_TEL}" style="color:rgba(250,246,238,0.85);">{PHONE}</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year"></span> Pearl Counseling. All rights reserved.</span>
      <span class="crisis-note"><strong>In crisis?</strong> Call or text 988 (Suicide &amp; Crisis Lifeline), or go to your nearest emergency room.</span>
    </div>
  </div>
</footer>

<script src="script.js"></script>
</body>
</html>
"""

def write_page(slug, title, desc, active, body):
    html = HEAD.replace("__TITLE__", title).replace("__DESC__", desc)
    html += nav(active)
    html += "\n<main>\n"
    html += body
    html += "\n</main>\n\n"
    html += FOOTER
    with open(os.path.join(OUT, f"{slug}.html"), "w") as f:
        f.write(html)
    print("wrote", slug + ".html", len(html), "bytes")

print("Templates ready. NAME =", NAME)

# ============================================================
# HOME
# ============================================================
index_body = """
  <!-- ============ HERO ============ -->
  <section class="hero">
    <div class="container hero-inner">
      <div class="hero-copy reveal">
        <span class="eyebrow">Lee Ann Childers &middot; Marriage &amp; Family Therapist</span>
        <h1>A space to feel <em>heard</em>, understood, and supported.</h1>
        <p class="hero-sub">Individual, couples, and family therapy rooted in connection, curiosity, and self-compassion &mdash; so you can move toward the life and relationships you want.</p>
        <div class="hero-ctas">
          <a href="contact.html" class="btn btn-primary">Reach Out</a>
          <a href="approach.html" class="btn btn-ghost">Learn About My Approach</a>
        </div>
      </div>
      <div class="hero-media reveal">
        <svg class="blob-shape" viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <path fill="#E7E9D8" d="M420,300Q430,400,330,440Q230,480,150,410Q70,340,90,240Q110,140,210,100Q310,60,380,140Q450,220,420,300Z"></path>
        </svg>
        <svg class="blob-shape" style="opacity:.6; transform: scale(.82) translate(6%, 8%);" viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <path fill="#EFE7F3" d="M400,260Q420,360,320,420Q220,480,140,400Q60,320,100,220Q140,120,240,90Q340,60,390,150Q440,240,400,260Z"></path>
        </svg>
        <div class="hero-photo">
          <img src="assets/images/hero-headshot.jpg" alt="Lee Ann Childers smiling warmly, seated outdoors" loading="eager">
        </div>
      </div>
    </div>
  </section>

  <!-- ============ INTRO / PULL QUOTE ============ -->
  <section class="intro-strip">
    <div class="container">
      <div class="intro-inner reveal">
        <div class="intro-photo">
          <img src="assets/images/growth-in-dark.jpg" alt="A small green plant growing amid dry leaves" loading="lazy">
        </div>
        <p class="intro-quote">&ldquo;I believe that everyone has a story, and sometimes the experiences, relationships, and messages we have carried throughout our lives can shape the way we see ourselves and connect with others.&rdquo;</p>
      </div>
    </div>
  </section>

  <!-- ============ BREAK: LIGHT RAYS ============ -->
  <section class="break-section reveal" style="background-image:url('assets/images/light-rays.jpg');">
    <blockquote>You do not have to navigate it alone.</blockquote>
  </section>

  <!-- ============ EXPLORE TEASERS ============ -->
  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Get to Know Pearl Counseling</span>
        <h2>Where would you like to start?</h2>
      </div>
      <div class="card-grid reveal">
        <a href="about.html" class="card">
          <div class="card-media"><img src="assets/images/about-headshot.jpg" alt="Lee Ann Childers, therapist" loading="lazy"></div>
          <div class="card-body">
            <h3>About Me</h3>
            <p>A little about who I am, and the belief that everyone has a story worth understanding.</p>
            <span class="teaser-link">Read my story <span class="arrow">&rarr;</span></span>
          </div>
        </a>
        <a href="approach.html" class="card">
          <div class="card-media"><img src="assets/images/curiosity.jpg" alt="Seedlings sprouting from soil" loading="lazy"></div>
          <div class="card-body">
            <h3>My Approach</h3>
            <p>How connection, curiosity, and self-compassion shape the way we work together.</p>
            <span class="teaser-link">See my approach <span class="arrow">&rarr;</span></span>
          </div>
        </a>
        <a href="services.html" class="card">
          <div class="card-media"><img src="assets/images/family-therapy.jpg" alt="A family sitting together outdoors" loading="lazy"></div>
          <div class="card-body">
            <h3>Services</h3>
            <p>Individual, couples, and family therapy &mdash; support for wherever you're starting from.</p>
            <span class="teaser-link">Explore services <span class="arrow">&rarr;</span></span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- ============ NOTEBOOK QUOTE ============ -->
  <section class="section section-alt">
    <div class="container notebook-strip reveal">
      <img src="assets/images/quote-notebook.jpg" alt="Hand-lettered note reading: Difficult roads often lead to beautiful destinations" loading="lazy">
    </div>
  </section>

  <!-- ============ CTA ============ -->
  <section class="cta-banner reveal">
    <h2>Ready to take the first step?</h2>
    <p>Reach out today to ask about availability and getting started. I look forward to hearing from you.</p>
    <a href="contact.html" class="btn btn-primary">Reach Out</a>
  </section>
"""

write_page(
    "index",
    "Pearl Counseling | Marriage & Family Therapy",
    "Pearl Counseling offers warm, compassionate individual, couples, and family therapy with Lee Ann Childers. A space to feel heard, understood, and supported.",
    "index",
    index_body,
)

# ============================================================
# ABOUT
# ============================================================
about_body = """
  <section class="page-hero reveal">
    <div class="container">
      <span class="eyebrow">About Me</span>
      <h1>Welcome to Pearl Counseling.</h1>
    </div>
  </section>

  <section class="section" style="padding-top:20px;">
    <div class="container">
      <div class="about-grid">
        <div class="about-media reveal">
          <div class="about-photo-main">
            <img src="assets/images/about-headshot.jpg" alt="Lee Ann Childers standing outdoors, smiling softly" loading="lazy">
          </div>
          <div class="about-photo-accent">
            <img src="assets/images/about-headshot-alt.jpg" alt="Lee Ann Childers portrait, close up" loading="lazy">
          </div>
        </div>
        <div class="about-body reveal">
          <p>I believe that everyone has a story, and sometimes the experiences, relationships, and messages we have carried throughout our lives can shape the way we see ourselves and connect with others.</p>
          <p>As a Marriage and Family Therapist, I provide a warm, compassionate space where individuals, couples, and families can feel heard, understood, and supported. I work with clients to explore the patterns that may be keeping them stuck, develop a deeper understanding of themselves, and create meaningful change in their lives and relationships.</p>
          <p>My approach is grounded in the belief that healing happens through connection, curiosity, and self-compassion. I help clients better understand how past experiences may be showing up in the present while developing new ways of responding to difficult emotions, relationships, and life challenges.</p>
          <p>Whether you are struggling with anxiety, relationship concerns, the effects of past experiences, life transitions, or simply feeling disconnected from yourself or others, you do not have to navigate it alone. My goal is to meet you where you are and walk alongside you as you discover your strengths, heal old wounds, and move toward the life and relationships you want.</p>
          <p>At Pearl Counseling, I strive to create a space where you can feel safe enough to be honest, supported enough to grow, and empowered to make lasting changes.</p>
          <div class="callout">
            <p><strong>Faith-integrated care, if you'd like it.</strong><br>For clients who wish to incorporate their faith into the counseling process, I am happy to integrate faith-based perspectives and beliefs in a way that feels meaningful and authentic to them.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-banner reveal">
    <h2>Curious how I work with clients?</h2>
    <p>Take a look at the approach and values that guide every session.</p>
    <a href="approach.html" class="btn btn-primary">My Approach</a>
  </section>
"""

write_page(
    "about",
    "About | Pearl Counseling",
    "Meet Lee Ann Childers, Marriage and Family Therapist and founder of Pearl Counseling.",
    "about",
    about_body,
)

# ============================================================
# APPROACH
# ============================================================
approach_body = """
  <section class="page-hero reveal">
    <div class="container">
      <span class="eyebrow">My Approach</span>
      <h1>Connection, curiosity, and self&#8209;compassion</h1>
      <p>Healing happens through relationship &mdash; not a clinical checklist. Here's what that looks like in our work together.</p>
    </div>
  </section>

  <section class="section" style="padding-top:20px;">
    <div class="container">
      <div class="card-grid reveal">
        <div class="card">
          <div class="card-media"><img src="assets/images/connection.jpg" alt="Two hands passing a small paper heart" loading="lazy"></div>
          <div class="card-body">
            <h3>Connection</h3>
            <p>Real change starts in a relationship where you feel truly heard. Our sessions are a warm, collaborative space, built around you.</p>
          </div>
        </div>
        <div class="card">
          <div class="card-media"><img src="assets/images/curiosity.jpg" alt="Seedlings sprouting from soil" loading="lazy"></div>
          <div class="card-body">
            <h3>Curiosity</h3>
            <p>Together we get curious about the patterns that keep you stuck, and how past experience may be showing up in your life today.</p>
          </div>
        </div>
        <div class="card">
          <div class="card-media"><img src="assets/images/self-compassion.jpg" alt="A small green leaf growing between two stones" loading="lazy"></div>
          <div class="card-body">
            <h3>Self-Compassion</h3>
            <p>Growth isn't about fixing what's broken. It's meeting yourself with understanding as you build new ways forward.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="break-section small reveal" style="background-image:url('assets/images/transitions-banner.jpg');">
    <h3>Life Transitions</h3>
    <p>Change is rarely simple. Whatever transition brought you here, I'll walk alongside you as you find your footing.</p>
  </section>

  <section class="cta-banner reveal">
    <h2>See how this looks in practice</h2>
    <p>Individual, couples, and family therapy &mdash; explore the ways we can work together.</p>
    <a href="services.html" class="btn btn-primary">View Services</a>
  </section>
"""

write_page(
    "approach",
    "My Approach | Pearl Counseling",
    "Learn about Lee Ann Childers' therapeutic approach at Pearl Counseling, grounded in connection, curiosity, and self-compassion.",
    "approach",
    approach_body,
)

# ============================================================
# SERVICES
# ============================================================
services_body = """
  <section class="page-hero reveal">
    <div class="container">
      <span class="eyebrow">Services</span>
      <h1>Ways we can work together</h1>
      <p>Support for anxiety, relationship concerns, past experiences, and life's transitions &mdash; wherever you're starting from. Sessions are available in person and via telehealth.</p>
    </div>
  </section>

  <section class="section" style="padding-top:20px;">
    <div class="container">
      <div class="card-grid reveal">
        <div class="card">
          <div class="card-media"><img src="assets/images/individual-therapy.jpg" alt="A monarch butterfly resting on a fingertip" loading="lazy"></div>
          <div class="card-body">
            <h3>Individual Therapy</h3>
            <p>For anxiety, life transitions, and the effects of past experiences &mdash; a space to better understand yourself and move toward the life you want.</p>
          </div>
        </div>
        <div class="card">
          <div class="card-media"><img src="assets/images/couples-therapy.jpg" alt="A couple embracing, foreheads touching in warm sunlight" loading="lazy"></div>
          <div class="card-body">
            <h3>Couples Therapy</h3>
            <p>For partners navigating relationship concerns and disconnection &mdash; rebuilding understanding, communication, and closeness.</p>
          </div>
        </div>
        <div class="card">
          <div class="card-media"><img src="assets/images/family-therapy.jpg" alt="A family sitting together outdoors, seen from behind" loading="lazy"></div>
          <div class="card-body">
            <h3>Family Therapy</h3>
            <p>For families working through patterns that leave everyone feeling stuck &mdash; creating a home where every voice is heard.</p>
          </div>
          <div class="card-duo">
            <img src="assets/images/family-detail-1.jpg" alt="A child's hand resting on a parent's hand, both painted with color" loading="lazy">
            <img src="assets/images/family-detail-2.jpg" alt="A child painting with a watercolor palette" loading="lazy">
          </div>
        </div>
      </div>

      <div class="faith-banner reveal">
        <img class="faith-bg" src="assets/images/flower-bloom.jpg" alt="">
        <div class="faith-banner-icon">&#10047;</div>
        <div class="faith-banner-text">
          <h4>Faith-Integrated Care Available</h4>
          <p>For clients who wish to incorporate their faith into the counseling process, I am happy to integrate faith-based perspectives and beliefs in a way that feels meaningful and authentic to them.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-banner reveal">
    <h2>Ready to get started?</h2>
    <p>Reach out to ask about availability, rates, and how to schedule your first session.</p>
    <a href="contact.html" class="btn btn-primary">Contact Me</a>
  </section>
"""

write_page(
    "services",
    "Services | Pearl Counseling",
    "Individual, couples, and family therapy with Lee Ann Childers at Pearl Counseling. In-person and telehealth sessions available.",
    "services",
    services_body,
)

# ============================================================
# CONTACT
# ============================================================
contact_body = f"""
  <section class="page-hero reveal">
    <div class="container">
      <span class="eyebrow">Contact</span>
      <h1>Interested in scheduling appointments? Or just have a question?</h1>
      <p>Fill out the form below, call, or send an email &mdash; whatever's easiest. I aim to return calls and messages within 48 business hours.</p>
    </div>
  </section>

  <section class="section" style="padding-top:10px;">
    <div class="container">

      <div class="info-grid reveal">
        <div class="info-card">
          <div class="info-icon">&#9993;</div>
          <h4>Email</h4>
          <a href="mailto:{EMAIL}">{EMAIL_DISPLAY}</a>
        </div>
        <div class="info-card">
          <div class="info-icon">&#9742;</div>
          <h4>Phone</h4>
          <a href="tel:{PHONE_TEL}">{PHONE}</a>
        </div>
        <div class="info-card">
          <div class="info-icon">&#8962;</div>
          <h4>Session Format</h4>
          <p>In person &amp; telehealth</p>
        </div>
        <div class="info-card">
          <div class="info-icon">&#9670;</div>
          <h4>Rate</h4>
          <p>$120 per session<br><span style="font-size:13.5px; color:var(--ink-soft);">Insurance is not currently accepted</span></p>
        </div>
      </div>

      <div class="section-head reveal">
        <span class="eyebrow">Getting Started</span>
        <h2>Three simple steps</h2>
        <div class="intro-photo" style="margin: 24px auto 0;">
          <img src="assets/images/grow-pots.jpg" alt="A potted plant labeled &quot;grow&quot; on a sunlit windowsill" loading="lazy">
        </div>
      </div>
      <div class="steps reveal" style="margin-bottom:80px;">
        <div class="step">
          <div class="step-num">1</div>
          <h3>Reach Out</h3>
          <p>Send a message, call, or email to ask about availability and whether we're a good fit.</p>
        </div>
        <div class="step">
          <div class="step-num">2</div>
          <h3>Schedule a Consultation</h3>
          <p>We'll set up a time to talk through what brings you to therapy and answer any questions you have.</p>
        </div>
        <div class="step">
          <div class="step-num">3</div>
          <h3>Begin Your Sessions</h3>
          <p>Start meeting regularly in a space built around your goals, your story, and your pace.</p>
        </div>
      </div>

      <div class="contact-grid reveal">
        <div class="contact-media">
          <div class="contact-photo">
            <img src="assets/images/contact-headshot.jpg" alt="Lee Ann Childers smiling, arms crossed, standing outdoors" loading="lazy">
          </div>
          <div class="contact-note">
            <strong>Please note:</strong> this form is not a secure or monitored line for emergencies. If you are experiencing a mental health crisis, please call or text <strong>988</strong> (Suicide &amp; Crisis Lifeline) or go to your nearest emergency room.
          </div>
        </div>

        <div class="form-card">
          <!--
            SETUP NOTE: This form uses Formspree (a free third-party form
            backend that works with static sites like GitHub Pages).
            Replace YOUR_FORM_ID below with your own Formspree endpoint.
            Full instructions are in README.md.
          -->
          <form id="contactForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
            <div class="form-two">
              <div class="form-row">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required autocomplete="name">
              </div>
              <div class="form-row">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required autocomplete="email">
              </div>
            </div>
            <div class="form-row">
              <label for="phone">Phone <span style="font-weight:400;color:var(--ink-soft);">(optional)</span></label>
              <input type="tel" id="phone" name="phone" autocomplete="tel">
            </div>
            <div class="form-row">
              <label for="message">What brings you here today?</label>
              <textarea id="message" name="message" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary form-submit">Send Message</button>
            <p class="form-status" id="formStatus"></p>
          </form>
        </div>
      </div>
    </div>
  </section>
"""

write_page(
    "contact",
    "Contact | Pearl Counseling",
    "Contact Lee Ann Childers at Pearl Counseling to schedule an appointment or ask a question.",
    "contact",
    contact_body,
)
