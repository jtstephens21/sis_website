// Pearl Counseling — small interactions

document.addEventListener('DOMContentLoaded', () => {

  /* ---- Sticky header shadow on scroll ---- */
  const header = document.getElementById('siteHeader');
  const onScroll = () => {
    if (window.scrollY > 8) header.classList.add('is-scrolled');
    else header.classList.remove('is-scrolled');
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---- Mobile nav toggle ---- */
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  navToggle.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('is-open');
    navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('is-open');
      navToggle.setAttribute('aria-expanded', 'false');
    });
  });

  /* ---- Reveal on scroll ---- */
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('is-visible'));
  }

  /* ---- Footer year ---- */
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---- Contact form (Netlify Forms AJAX submit) ---- */
  const form = document.getElementById('contactForm');
  const status = document.getElementById('formStatus');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type="submit"]');
      submitBtn.disabled = true;
      submitBtn.textContent = 'Sending…';
      status.className = 'form-status';
      status.textContent = '';

      // Netlify Forms expects a standard URL-encoded POST body (not
      // multipart), sent to the page the form lives on.
      const body = new URLSearchParams(new FormData(form)).toString();

      try {
        const response = await fetch(form.action, {
          method: 'POST',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body,
        });
        if (response.ok) {
          form.reset();
          status.textContent = "Thank you — your message has been sent. I'll be in touch soon.";
          status.classList.add('success');
        } else {
          status.textContent = "Something went wrong. Please try again, or reach out directly.";
          status.classList.add('error');
        }
      } catch (err) {
        status.textContent = "Something went wrong. Please check your connection and try again.";
        status.classList.add('error');
      } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Send Message';
      }
    });
  }

});
