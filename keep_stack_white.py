with open('docs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The stack section already has a dark radial gradient background (set in CSS).
# In light mode the section stays dark (we preserved it), but the text
# may be turning dark due to the general body.light text overrides.
# Add targeted overrides to keep ALL text in #stack white in light mode.

dark_stack = """
    /* ======= KEEP TECHNOLOGY STACK SECTION TEXT WHITE IN LIGHT MODE ======= */
    html.light #stack,
    body.light #stack {
      background: radial-gradient(ellipse 80% 60% at 50% 50%, #0a1020, #03050a) !important;
    }
    body.light #stack .section-title {
      -webkit-text-fill-color: #ffffff !important;
      color: #ffffff !important;
      background: none !important;
    }
    body.light #stack .section-sub,
    body.light #stack p {
      color: #7a9ab8 !important;
    }
    body.light #stack .section-tag {
      color: var(--accent) !important;
      border-color: rgba(74,144,217,0.3) !important;
    }
    body.light #stack .stack-item {
      background: rgba(13,22,37,0.8) !important;
      border: 1px solid rgba(74,144,217,0.18) !important;
    }
    body.light #stack .stack-item h4,
    body.light #stack .stack-item p {
      color: #f0f4ff !important;
    }
    body.light #stack .stack-cat-title {
      color: var(--accent) !important;
    }
    """

# Inject after the trusted-by dark override block
insertion_point = '    /* KEEP HERO EXACTLY LIKE DARK MODE */'
content = content.replace(insertion_point, dark_stack + '\n    /* KEEP HERO EXACTLY LIKE DARK MODE */')

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done - stack section text stays white in light mode.")
