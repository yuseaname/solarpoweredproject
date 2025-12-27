(() => {
  const navs = document.querySelectorAll(".site-header .nav");
  if (!navs.length) return;

  const path = window.location.pathname || "";
  const href = path.includes("/pages/")
    ? "../diy-off-grid-energy/"
    : path.includes("/diy-off-grid-energy/")
      ? "index.html"
      : "diy-off-grid-energy/";

  navs.forEach((nav) => {
    const hasDiyLink = Array.from(nav.querySelectorAll("a")).some((a) =>
      (a.getAttribute("href") || "").includes("diy-off-grid-energy")
    );
    if (hasDiyLink) return;

    const link = document.createElement("a");
    link.href = href;
    link.textContent = "DIY Experiments";
    nav.appendChild(link);
  });
})();

const revealTargets = document.querySelectorAll(
  ".hero-content, .hero-card, .card, .cta, .section-header"
);

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.2 }
);

revealTargets.forEach((el, index) => {
  el.classList.add("reveal");
  el.style.transitionDelay = `${Math.min(index * 80, 240)}ms`;
  observer.observe(el);
});
