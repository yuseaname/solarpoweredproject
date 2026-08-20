(function () {
  'use strict';
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
  var input = document.getElementById('site-search');
  var output = document.getElementById('search-results');
  var count = document.getElementById('search-count');
  if (input && output && Array.isArray(window.SPP_SEARCH_INDEX)) {
    function esc(value) { var el = document.createElement('span'); el.textContent = value || ''; return el.innerHTML; }
    function render() {
      var query = input.value.trim().toLowerCase();
      if (!query) { output.innerHTML = ''; count.textContent = ''; return; }
      var terms = query.split(/\s+/);
      var matches = window.SPP_SEARCH_INDEX.filter(function (item) { var hay = (item.title + ' ' + item.description + ' ' + item.section).toLowerCase(); return terms.every(function (term) { return hay.indexOf(term) !== -1; }); }).slice(0, 12);
      count.textContent = matches.length ? matches.length + (matches.length === 1 ? ' guide found' : ' guides found') : 'No exact matches. Try a component, system type, or simpler phrase.';
      output.innerHTML = matches.map(function (item) { return '<article><p class="eyebrow">' + esc(item.section === 'diy-off-grid-energy' ? 'Project Lab' : 'Field guide') + '</p><h2><a href="' + esc(item.url) + '">' + esc(item.title) + '</a></h2><p>' + esc(item.description) + '</p></article>'; }).join('');
    }
    input.addEventListener('input', render);
  }
})();
