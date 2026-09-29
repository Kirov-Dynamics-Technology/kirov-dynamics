/* Kirov Dynamics — cookieless analytics (Umami).
   Served from our own domain; inert until configured below.

   To activate: set CONFIG.host to your Umami instance (Umami Cloud or self-hosted)
   and CONFIG.websiteId to the website id created in that instance. Until then this
   file loads nothing and tracks nothing, so the site stays privacy-honest. */
(function () {
  'use strict';

  var CONFIG = {
    host: "",                          /* e.g. "https://analytics.example.com" or Umami Cloud URL */
    websiteId: "",                     /* the website id from your Umami instance */
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

  /* Load Umami only when configured with real values. */
  if (CONFIG.host && CONFIG.websiteId) {
    var s = document.createElement("script");
    s.async = true;
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

  /* One-shot tool usage for the ROI calculator (real user input only). */
  var roiFired = false;
  var roiIds = ["roi-emp", "roi-hrs", "roi-rate", "roi-red"];
  document.addEventListener("input", function (ev) {
    if (roiFired) return;
    if (ev.target && ev.target.id && roiIds.indexOf(ev.target.id) !== -1) {
      roiFired = true;
      track("tool_used", { tool: "roi" });
    }
  }, true);

  /* Generic hook: an element with data-track="name" fires named event on click. */
  document.addEventListener("click", function (ev) {
    var el = ev.target && ev.target.closest ? ev.target.closest("[data-track]") : null;
    if (el) track(el.getAttribute("data-track") || "custom", {});
  }, true);
})();