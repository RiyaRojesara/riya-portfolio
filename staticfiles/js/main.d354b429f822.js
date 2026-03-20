/* ═══════════════════════════════════════════════════════════
   PORTFOLIO — MAIN JAVASCRIPT
   ═══════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide icons
  lucide.createIcons();

  // Initialize everything
  initLoader();
  initCursor();
  initNavbar();
  initHamburger();
  initScrollReveal();
  initSectionHighlight();
  initTabs();
  initSkillBars();
  initBackToTop();
  initChat();
});

/* ══════════════════════════════════════════
   LOADER
══════════════════════════════════════════ */
function initLoader() {
  const loader = document.getElementById('loader');
  window.addEventListener('load', () => {
    setTimeout(() => {
      loader.classList.add('hidden');
      document.body.style.overflow = 'auto';
    }, 600);
  });
  // Fallback if load fires slowly
  setTimeout(() => loader.classList.add('hidden'), 2500);
}

/* ══════════════════════════════════════════
   CUSTOM CURSOR
══════════════════════════════════════════ */
function initCursor() {
  const cursor    = document.getElementById('cursor');
  const cursorDot = document.getElementById('cursor-dot');
  if (!cursor || !cursorDot) return;

  let mouseX = 0, mouseY = 0;
  let curX = 0, curY = 0;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    cursorDot.style.left = mouseX + 'px';
    cursorDot.style.top  = mouseY + 'px';
  });

  // Smooth trailing cursor
  function animate() {
    curX += (mouseX - curX) * 0.12;
    curY += (mouseY - curY) * 0.12;
    cursor.style.left = curX + 'px';
    cursor.style.top  = curY + 'px';
    requestAnimationFrame(animate);
  }
  animate();

  // Hover effect on interactive elements
  document.querySelectorAll('a, button, .tab-btn, .suggestion-btn, .project-card, .exp-card, .contact-card').forEach(el => {
    el.addEventListener('mouseenter', () => cursor.classList.add('cursor-hover'));
    el.addEventListener('mouseleave', () => cursor.classList.remove('cursor-hover'));
  });
}

/* ══════════════════════════════════════════
   NAVBAR — scroll behavior
══════════════════════════════════════════ */
function initNavbar() {
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 60) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }, { passive: true });

  // Smooth scroll for nav links
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const target = document.querySelector(link.getAttribute('href'));
      if (target) {
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top, behavior: 'smooth' });
        // Close mobile menu if open
        closeMobileMenu();
      }
    });
  });
}

/* ══════════════════════════════════════════
   HAMBURGER MENU
══════════════════════════════════════════ */
function initHamburger() {
  const hamburger  = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  if (!hamburger || !mobileMenu) return;

  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    mobileMenu.classList.toggle('open');
  });

  // Close on outside click
  document.addEventListener('click', (e) => {
    if (!hamburger.contains(e.target) && !mobileMenu.contains(e.target)) {
      closeMobileMenu();
    }
  });
}

function closeMobileMenu() {
  const hamburger  = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  if (hamburger) hamburger.classList.remove('open');
  if (mobileMenu) mobileMenu.classList.remove('open');
}

/* ══════════════════════════════════════════
   SCROLL REVEAL
══════════════════════════════════════════ */
function initScrollReveal() {
  const revealEls = document.querySelectorAll('.reveal');

  if (!revealEls.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        // Don't unobserve — keep visible
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  revealEls.forEach(el => observer.observe(el));
}

/* ══════════════════════════════════════════
   ACTIVE NAV HIGHLIGHT
══════════════════════════════════════════ */
function initSectionHighlight() {
  const sections  = document.querySelectorAll('section[id]');
  const navLinks  = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
      const top = section.getBoundingClientRect().top;
      if (top <= 120) current = section.id;
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.dataset.section === current) {
        link.classList.add('active');
      }
    });
  }, { passive: true });
}

/* ══════════════════════════════════════════
   PORTFOLIO TABS
══════════════════════════════════════════ */
function initTabs() {
  const tabBtns     = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;

      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));

      btn.classList.add('active');
      document.getElementById('tab-' + target).classList.add('active');

      // Trigger skill bar animation when tech stack tab is shown
      if (target === 'techstack') {
        triggerSkillBars();
      }

      // Re-observe reveal elements in newly visible tab
      document.querySelectorAll('#tab-' + target + ' .reveal').forEach(el => {
        el.classList.add('visible');
      });
    });
  });
}

/* ══════════════════════════════════════════
   SKILL BARS
══════════════════════════════════════════ */
function initSkillBars() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        triggerSkillBars();
        observer.disconnect();
      }
    });
  }, { threshold: 0.2 });

  const stackSection = document.getElementById('tab-techstack');
  if (stackSection) observer.observe(stackSection);
}

function triggerSkillBars() {
  document.querySelectorAll('.skill-fill').forEach(bar => {
    const level = bar.dataset.level;
    setTimeout(() => {
      bar.style.width = level + '%';
    }, 100);
  });
}

/* ══════════════════════════════════════════
   BACK TO TOP
══════════════════════════════════════════ */
function initBackToTop() {
  const btn = document.getElementById('back-to-top');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      btn.classList.add('show');
    } else {
      btn.classList.remove('show');
    }
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ══════════════════════════════════════════
   AI CHAT
══════════════════════════════════════════ */
function initChat() {
  const input    = document.getElementById('chat-input');
  const sendBtn  = document.getElementById('chat-send');
  const window_  = document.getElementById('chat-window');

  if (!input || !sendBtn || !window_) return;

  // Send on button click
  sendBtn.addEventListener('click', handleSend);

  // Send on Enter
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  });

  async function handleSend() {
    const msg = input.value.trim();
    if (!msg) return;

    // Hide suggestions
    const suggestions = document.getElementById('suggestions');
    if (suggestions) suggestions.style.display = 'none';

    // Add user message
    appendMessage(msg, 'user');
    input.value = '';
    sendBtn.disabled = true;

    // Show typing indicator
    const typingId = showTyping();

    try {
      const response = await fetch('/chat/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg }),
      });

      const data = await response.json();
      removeTyping(typingId);

      // Small delay for natural feel
      setTimeout(() => {
        appendMessage(data.reply || "Sorry, I couldn't respond to that.", 'bot');
        sendBtn.disabled = false;
        input.focus();
      }, 200);

    } catch (err) {
      removeTyping(typingId);
      appendMessage("Oops! Something went wrong. Please try again. 🙏", 'bot');
      sendBtn.disabled = false;
    }
  }

  function appendMessage(text, sender) {
    const msgEl = document.createElement('div');
    msgEl.classList.add('chat-msg', sender === 'user' ? 'user-msg' : 'bot-msg');

    const now = new Date();
    const time = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    const avatar = sender === 'user' ? '👤' : '🤖';
    const avatarClass = sender === 'user' ? 'user-avatar' : 'bot-avatar';

    msgEl.innerHTML = `
      <div class="msg-avatar ${avatarClass}">${avatar}</div>
      <div class="msg-bubble">
        <p>${escapeHtml(text)}</p>
        <span class="msg-time">${time}</span>
      </div>
    `;

    window_.appendChild(msgEl);
    window_.scrollTop = window_.scrollHeight;
  }

  function showTyping() {
    const id = 'typing-' + Date.now();
    const el = document.createElement('div');
    el.id = id;
    el.classList.add('chat-msg', 'bot-msg');
    el.innerHTML = `
      <div class="msg-avatar bot-avatar">🤖</div>
      <div class="typing-indicator">
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
      </div>
    `;
    window_.appendChild(el);
    window_.scrollTop = window_.scrollHeight;
    return id;
  }

  function removeTyping(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
  }

  function escapeHtml(str) {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }
}

/* Called from HTML suggestion buttons */
function sendSuggestion(btn) {
  const input = document.getElementById('chat-input');
  if (!input) return;
  input.value = btn.textContent;
  document.getElementById('chat-send').click();
}
