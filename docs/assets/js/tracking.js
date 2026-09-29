/* Kirov Dynamics — cookieless analytics (Umami Cloud).
   Served from our own domain; loads Umami Cloud's script.js.

   CONFIG.host      = Umami Cloud (cloud.umami.is)
   CONFIG.websiteId = the kirov-dynamics website created there
   Other events (kdt.track) are opt-in and documented in events.md. */
(function () {
  'use strict';

  var CONFIG = {
    host: "https://cloud.umami.is",    /* Umami Cloud */
    websiteId: "2710875c-7962-4d56-85e0-0d6af2c2e879",
    domains: "kirov-dynamics-technology.github.io"  /* restrict to our own domains */
  };

  /* window.kdt.track(name, data) — fires custom events into Umami when loaded.
     Fails closed: before activation, and if umami is absent, it is a no-op. */
  var kdt = window.kdt || {};
  function track(name, data) {
    try {
      if (window.umami && typeof window.umami.track === "function") {
        window.umami.track(name, data || {});
      }
    } catch (e) { /* never break the page */ }
  }
  kdt.track = track;
  window.kdt = kdt;

  /* Load Umami Cloud script.js. */
  if (CONFIG.host && CONFIG.websiteId) {
    var s = document.createElement("script");
    s.defer = true;
    s.src = CONFIG.host.replace(/\/+$/, "") + "/script.js";
    s.setAttribute("data-website-id", CONFIG.websiteId);
    s.setAttribute("data-host-url", CONFIG.host);
    s.setAttribute("data-domains", CONFIG.domains);
    document.head.appendChild(s);
  }

  /* CTA clicks toward assessment/contact → cta_click */
  document.addEventListener("click", function (ev) {
    var a = ev.target && ev.target.closest ? ev.target.closest("a[href]") : null;
    if (!a) return;
    var href = a.getAttribute("href") || "";
    if (href.indexOf("#contact") === 0 || href.indexOf("#assessment") === 0) {
      track("cta_click", { cta: "assessment", page: location.pathname });
    }
  }, true);

  /* One-shot tool usage for the ROI calculator (real user input only).
     First real interaction = tool_used + assessment_complete (the tool yields a
     result instantly), so the funnel is: pageview → tool_used → assessment_complete. */
  var roiFired = false;
  var roiIds = ["roi-emp", "roi-hrs", "roi-rate", "roi-red"];
  document.addEventListener("input", function (ev) {
    if (ev.target && ev.target.id && roiIds.indexOf(ev.target.id) !== -1) {
      if (!roiFired) {
        roiFired = true;
        track("tool_used", { tool: "roi" });
        track("assessment_complete", { tool: "roi" });
      }
    }
  }, true);

  /* Tech-score: fire assessment_start when the section is actually viewed
     (it is a static readiness visual, so interaction = reading it). */
  (function () {
    if (!("IntersectionObserver" in window)) return;
    var ts = document.getElementById("tech-score");
    if (!ts) return;
    var tsFired = false;
    new IntersectionObserver(function (entries) {
      if (!tsFired && entries[0].isIntersecting) {
        tsFired = true;
        track("assessment_start", { tool: "tech-score" });
      }
    }, { threshold: 0.4 }).observe(ts);
  })();

  /* Generic hook: an element with data-track="name" fires named event on click. */
  document.addEventListener("click", function (ev) {
    var el = ev.target && ev.target.closest ? ev.target.closest("[data-track]") : null;
    if (el) track(el.getAttribute("data-track") || "custom", {});
  }, true);
})();