(function () {
  'use strict';

  /* --- Navigation toggle --- */
  var toggle = document.getElementById('nav-toggle');
  var menu = document.getElementById('mobile-menu');
  var lastFocus = null;
  function setMenu(open) {
    if (!toggle || !menu) return;
    menu.hidden = !open;
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    if (open) { lastFocus = document.activeElement; var first = menu.querySelector('a'); if (first) first.focus(); }
    else if (lastFocus) { lastFocus.focus(); }
  }
  if (toggle && menu) {
    toggle.addEventListener('click', function () { setMenu(menu.hidden); });
    document.addEventListener('keydown', function (event) { if (event.key === 'Escape' && !menu.hidden) setMenu(false); });
    menu.querySelectorAll('a').forEach(function (link) { link.addEventListener('click', function () { setMenu(false); }); });
  }
  var nav = document.getElementById('main-nav');
  if (nav) { var scrollState = function () { nav.classList.toggle('is-scrolled', window.scrollY > 8); }; addEventListener('scroll', scrollState, { passive: true }); scrollState(); }

  /* --- Search --- */
  var input = document.getElementById('site-search');
  var output = document.getElementById('search-results');
  var count = document.getElementById('search-count');
  if (input && output && Array.isArray(window.SPP_SEARCH_INDEX)) {
    function esc(value) { var el = document.createElement('span'); el.textContent = value || ''; return el.innerHTML; }
    function render() {
      var query = input.value.trim().toLowerCase();
      if (!query) { output.innerHTML = ''; count.textContent = ''; return; }
      var terms = query.split(/\s+/);
      var matches = window.SPP_SEARCH_INDEX.filter(function (item) { var hay = (item.title + ' ' + item.description + ' ' + item.section + ' ' + (item.body || '') + ' ' + (item.keywords || '')).toLowerCase(); return terms.every(function (term) { return hay.indexOf(term) !== -1; }); }).slice(0, 12);
      count.textContent = matches.length ? matches.length + (matches.length === 1 ? ' guide found' : ' guides found') : 'No exact matches. Try a component, system type, or simpler phrase.';
      output.innerHTML = matches.map(function (item) { return '<article><p class="eyebrow">' + esc(item.section === 'diy-off-grid-energy' ? 'Project Lab' : 'Field guide') + '</p><h2><a href="' + esc(item.url) + '">' + esc(item.title) + '</a></h2><p>' + esc(item.description) + '</p></article>'; }).join('');
    }
    input.addEventListener('input', render);
  }

  /* --- Accessibility enhancements --- */
  document.querySelectorAll('.prose div[id$="results"], .prose div[id$="result"], .prose p[id$="results"], .prose p[id$="result"]').forEach(function (el) {
    el.setAttribute('role', 'status');
    el.setAttribute('aria-live', 'polite');
  });
  document.querySelectorAll('.prose input[type="number"]').forEach(function (el) { el.setAttribute('inputmode', 'decimal'); });
  document.querySelectorAll('.prose table').forEach(function (table) {
    table.querySelectorAll('thead th').forEach(function (th) { th.setAttribute('scope', 'col'); });
    table.tabIndex = 0;
    table.setAttribute('aria-label', 'Data table — use arrow keys to scroll if it is wider than the screen.');
  });
  if (window.matchMedia('(max-width: 620px)').matches) {
    document.querySelectorAll('details.toc-details').forEach(function (d) { d.removeAttribute('open'); });
  }

  /* --- Rybbit Analytics (ported from airecorderguide spec) --- */
  /* Queue events until Rybbit script is ready; no PII; enum/bucket props only. */
  var queue = [];
  var rybbitReady = false;

  function flushQueue() {
    rybbitReady = true;
    queue.splice(0).forEach(function (obj) {
      try { window.rybbit.event(obj.event, obj.props || {}); } catch (e) {}
    });
  }

  function track(name, props) {
    var obj = { event: name, props: props };
    queue.push(obj);
    if (rybbitReady) flushQueue();
  }

  /* Wait for Rybbit */
  try {
    if (window.rybbit && typeof window.rybbit.onReady === 'function') {
      window.rybbit.onReady(flushQueue);
    } else {
      var tries = 0;
      var t = setInterval(function () {
        if (window.rybbit && typeof window.rybbit.event === 'function') {
          clearInterval(t);
          flushQueue();
        } else if (++tries > 50) { clearInterval(t); }
      }, 200);
    }
  } catch (e) {}

  /* --- Shared helpers --- */
  function pageId() {
    var p = location.pathname.replace(/\/+$/, '');
    return p === '' ? 'home' : p.split('/').pop();
  }

  function pageType() {
    var p = location.pathname;
    if (p === '/' || p === '/index.html') return 'home';
    if (/^\/best-/.test(p)) return 'hub';
    if (/-review\/$/.test(p)) return 'review';
    if (/-vs-|comparison/.test(p)) return 'vs';
    if (/^\/(calculator|tools)/.test(p)) return 'tool';
    if (/^\/(about|contact|affiliate-disclosure|editorial-policy|review-methodology|privacy-policy|terms)\/?$/.test(p) || /404/.test(p)) return 'trust';
    return 'informational';
  }

  /* --- scroll_depth: milestones 25/50/75/90 --- */
  var seenDepth = {};
  window.addEventListener('scroll', function () {
    var doc = document.documentElement;
    var pct = ((window.scrollY + window.innerHeight) / (doc.scrollHeight || 1)) * 100;
    [25, 50, 75, 90].forEach(function (m) {
      if (pct >= m && !seenDepth[m]) {
        seenDepth[m] = true;
        track('scroll_depth', { milestone: m, page_id: pageId(), page_type: pageType() });
      }
    });
  }, { passive: true });

  /* --- engagement: on tab hide, bucket seconds --- */
  var t0 = Date.now();
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'hidden') {
      var s = Math.round((Date.now() - t0) / 1000);
      var b = s < 5 ? 'lt5s' : s < 15 ? '5_15s' : s < 45 ? '15_45s' : s < 120 ? '45s_2m' : 'gt2m';
      track('engagement', { engagement_bucket: b, page_id: pageId(), page_type: pageType() });
    }
  });

  /* --- contact_submit: any form with action to contact endpoint --- */
  document.addEventListener('submit', function (e) {
    var form = e.target;
    if (!form || !form.getAttribute) return;
    var action = form.getAttribute('action') || '';
    if (action.indexOf('contact') !== -1 || form.id === 'contact-form') {
      track('contact_submit', { form_id: form.id || 'contact', page_id: pageId() });
    }
  }, { passive: true });

})();