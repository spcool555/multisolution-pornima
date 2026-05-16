/* main.js – Shared JavaScript for all static pages */

'use strict';

// ─── Year ──────────────────────────────────────
document.querySelectorAll('.year, #year').forEach(el => {
  el.textContent = new Date().getFullYear();
});

// ─── Mobile Hamburger ──────────────────────────
const hamburger  = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');
const iconMenu   = document.getElementById('iconMenu');
const iconClose  = document.getElementById('iconClose');

if (hamburger && mobileMenu) {
  hamburger.addEventListener('click', () => {
    const open = mobileMenu.classList.toggle('open');
    hamburger.setAttribute('aria-expanded', open);
    if (iconMenu)  iconMenu.style.display  = open ? 'none'  : 'block';
    if (iconClose) iconClose.style.display = open ? 'block' : 'none';
  });

  // Close menu when a link is clicked
  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
      if (iconMenu)  iconMenu.style.display  = 'block';
      if (iconClose) iconClose.style.display = 'none';
    });
  });
}

// ─── Scroll-to-Top ─────────────────────────────
const scrollBtn = document.getElementById('scroll-top');
if (scrollBtn) {
  window.addEventListener('scroll', () => {
    scrollBtn.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });
  scrollBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// ─── Intersection Observer (fade-in animations) ──
const fadeEls = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');
if (fadeEls.length) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        // staggered delay for sibling cards
        const delay = entry.target.dataset.delay || 0;
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, Number(delay));
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

  fadeEls.forEach((el, i) => {
    // Auto-stagger siblings inside same parent grid
    const siblings = el.parentElement.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');
    siblings.forEach((sib, j) => { sib.dataset.delay = j * 90; });
    observer.observe(el);
  });
}

// ─── Contact Form (client-side only) ─────────────
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  const alertSuccess = document.getElementById('alertSuccess');
  const alertError   = document.getElementById('alertError');
  const errorMsg     = document.getElementById('errorMsg');
  const submitBtn    = document.getElementById('submitBtn');
  const btnText      = document.getElementById('btnText');

  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Hide any previous alerts
    alertSuccess.classList.remove('show');
    alertError.classList.remove('show');

    // Simple validation
    const fields = contactForm.querySelectorAll('[required]');
    let valid = true;
    fields.forEach(f => {
      f.style.borderColor = '';
      if (!f.value.trim()) {
        f.style.borderColor = '#f87171';
        valid = false;
      }
    });
    if (!valid) {
      if (errorMsg) errorMsg.textContent = 'Please fill in all required fields.';
      alertError.classList.add('show');
      return;
    }

    // Simulate sending (no backend)
    submitBtn.disabled = true;
    if (btnText) btnText.textContent = 'Sending...';

    await new Promise(r => setTimeout(r, 1200)); // simulate async

    submitBtn.disabled = false;
    if (btnText) btnText.textContent = 'Submit Inquiry';

    // Show success (form stays as-is; in a real static deploy you'd use Formspree/Netlify)
    alertSuccess.classList.add('show');
    contactForm.reset();

    // Auto-hide success after 6s
    setTimeout(() => alertSuccess.classList.remove('show'), 6000);
  });
}

// ─── Smooth scroll for anchor links (e.g. services#traffic) ──
document.querySelectorAll('a[href*="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const href = this.getAttribute('href');
    // Only handle same-page anchors
    if (!href.includes('.html') && !href.startsWith('http')) {
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  });
});
