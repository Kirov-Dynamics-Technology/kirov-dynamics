with open('docs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where the nuclear white bg CSS is — we'll inject the trusted-by dark overrides right after

dark_keep = """
    /* ======= KEEP TRUSTED-BY SECTION DARK IN LIGHT MODE =======
       These dark-background sections should remain dark regardless of mode */

    /* Section background stays dark */
    html.light #trusted-by,
    body.light #trusted-by {
      background: #06080f !important;
      background-color: #06080f !important;
    }

    /* Cards keep dark background */
    body.light .trusted-card {
      background: rgba(13,22,37,0.95) !important;
      border: 1px solid rgba(74,144,217,0.18) !important;
      box-shadow: 0 4px 24px rgba(0,0,0,0.3) !important;
    }

    /* Text stays white */
    body.light .trusted-card h4 {
      color: #f0f4ff !important;
    }
    body.light .trusted-card p {
      color: #7a9ab8 !important;
    }

    /* Section heading + sub text stay white */
    body.light #trusted-by .section-title {
      -webkit-text-fill-color: #ffffff !important;
      color: #ffffff !important;
      background: none !important;
    }
    body.light #trusted-by .section-sub {
      color: #7a9ab8 !important;
    }
    body.light #trusted-by .section-tag {
      color: var(--accent) !important;
      border-color: rgba(74,144,217,0.3) !important;
    }
    body.light #trusted-by .divider {
      background: var(--accent) !important;
    }

    /* Icon boxes stay dark glass */
    body.light #trusted-by .trusted-icon-box,
    body.light .trusted-icon-box {
      background: rgba(255,255,255,0.03) !important;
      border: 1px solid rgba(255,255,255,0.08) !important;
      color: var(--accent) !important;
    }
    body.light #trusted-by .trusted-icon-box i,
    body.light #trusted-by .trusted-icon-box svg,
    body.light .trusted-icon-box i,
    body.light .trusted-icon-box svg {
      color: var(--accent) !important;
      stroke: var(--accent) !important;
    }
    """

# Inject after the body.light variables block
insertion_point = '    /* KEEP HERO EXACTLY LIKE DARK MODE */'
content = content.replace(insertion_point, dark_keep + '\n    /* KEEP HERO EXACTLY LIKE DARK MODE */')

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done - trusted-by section will stay dark in light mode.")
