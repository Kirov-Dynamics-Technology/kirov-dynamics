with open('docs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ---- Replace the entire body.light variable block ----
old_vars = """    body.light {
      --bg:          #ffffff;
      --bg-alt:      #ffffff;
      --text:        #0f172a;
      --muted:       #475569;
      --border:      rgba(37,99,235,0.2);
      /* Make cards slightly more opaque dark blue to contrast against white background */
      --bg-card:     rgba(13,22,37,0.95);
    }"""

new_vars = """    body.light {
      --bg:          #ffffff;
      --bg-alt:      #ffffff;
      --bg-card:     #ffffff;
      --text:        #0f172a;
      --muted:       #475569;
      --border:      rgba(37,99,235,0.15);
    }"""

content = content.replace(old_vars, new_vars)

# ---- Replace the old "FORCE ALL CARDS" block with a proper light card style ----
old_cards_block = """    /* FORCE ALL CARDS AND UI ELEMENTS TO HAVE WHITE TEXT (Since they use dark backgrounds) */
    body.light .why-card, body.light .division-card, body.light .product-card,
    body.light .project-card, body.light .testimonial-card, body.light .insight-card,
    body.light .career-card, body.light .resource-card, body.light .security-item,
    body.light .roadmap-year, body.light .leader-card, body.light .process-step,
    body.light .journey-step, body.light .map-country, body.light .industry-tile,
    body.light .stack-item, body.light .partner-logo, body.light .trusted-card,
    body.light .carousel-viewport, body.light .partners-viewport, body.light .expertise-card,
    body.light .consult-card, body.light .consult-option, body.light .engine-card {
       color: #f1f5f9 !important;
    }
    body.light .why-card h3, body.light .why-card h4, body.light .why-card p,
    body.light .division-card h3, body.light .division-card p,
    body.light .product-card h3, body.light .product-card p,
    body.light .project-card h3, body.light .project-card h4, body.light .project-card p,
    body.light .testimonial-card blockquote, body.light .testimonial-card h4,
    body.light .trusted-card h4, body.light .trusted-card p,
    body.light .stack-item h4, body.light .stack-item p,
    body.light .partner-logo span,
    body.light .expertise-card h4, body.light .expertise-card p,
    body.light .engine-card h3, body.light .engine-card h4, body.light .engine-card p, body.light .engine-card span {
       color: #f1f5f9 !important;
    }
    body.light .trusted-card p, body.light .expertise-card p { color: #94a3b8 !important; }"""

new_cards_block = """    /* =========  ALL LIGHT MODE CARDS → WHITE BACKGROUND + DARK TEXT  ========= */
    body.light .why-card, body.light .division-card, body.light .product-card,
    body.light .project-card, body.light .testimonial-card, body.light .insight-card,
    body.light .career-card, body.light .security-item,
    body.light .leader-card, body.light .process-step,
    body.light .journey-step, body.light .map-country, body.light .industry-tile,
    body.light .trusted-card, body.light .expertise-card,
    body.light .consult-card, body.light .engine-card {
      background: #ffffff !important;
      border: 1px solid rgba(37,99,235,0.12) !important;
      box-shadow: 0 2px 12px rgba(0,0,0,0.06) !important;
      color: #0f172a !important;
    }

    /* Dark text on headings / body for all light cards */
    body.light .why-card h3, body.light .why-card h4, body.light .why-card p,
    body.light .division-card h3, body.light .division-card h4, body.light .division-card p,
    body.light .product-card h3, body.light .product-card h4, body.light .product-card p,
    body.light .project-card h3, body.light .project-card h4, body.light .project-card p,
    body.light .testimonial-card blockquote, body.light .testimonial-card h4, body.light .testimonial-card p,
    body.light .trusted-card h4,
    body.light .stack-item h4,
    body.light .expertise-card h4,
    body.light .engine-card h3, body.light .engine-card h4, body.light .engine-card p, body.light .engine-card span,
    body.light .leader-card h4, body.light .leader-card p, body.light .leader-card span,
    body.light .career-card h3, body.light .career-card h4, body.light .career-card p,
    body.light .process-step h4, body.light .process-step p,
    body.light .journey-step h4, body.light .journey-step p {
      color: #0f172a !important;
    }

    /* Muted text for descriptions */
    body.light .why-card p, body.light .division-card p, body.light .product-card p,
    body.light .project-card p, body.light .testimonial-card blockquote,
    body.light .trusted-card p, body.light .expertise-card p, body.light .engine-card p,
    body.light .leader-card p, body.light .career-card p, body.light .process-step p,
    body.light .journey-step p {
      color: #475569 !important;
    }

    /* Carousel wrappers */
    body.light .carousel-viewport, body.light .partners-viewport {
      background: #f8fafc !important;
      border: 1px solid rgba(37,99,235,0.12) !important;
    }

    /* Stack + Partner items */
    body.light .stack-item, body.light .partner-logo {
      background: #ffffff !important;
      border: 1px solid rgba(37,99,235,0.1) !important;
    }
    body.light .stack-item h4, body.light .stack-item p, body.light .partner-logo span {
      color: #0f172a !important;
    }

    /* Consult options */
    body.light .consult-option {
      background: #ffffff !important;
      border: 1px solid rgba(37,99,235,0.2) !important;
    }

    /* Resource cards stay dark (they have dark image backgrounds) */
    body.light .resource-card {
      background: var(--bg-card) !important;
    }"""

content = content.replace(old_cards_block, new_cards_block)

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Full light mode card overhaul applied.")
