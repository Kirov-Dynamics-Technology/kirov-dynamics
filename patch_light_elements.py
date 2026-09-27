with open('docs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix icon-tile to use light blue box (not dark navy) in light mode
old_icon_tile = """    body.light .icon-tile {
      background: #ffffff !important;
      border: 1px solid rgba(37,99,235,0.2) !important;
      color: #1a3664 !important;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
    }
    body.light .icon-tile::after { background: none !important; }
    body.light .icon-tile i, body.light .icon-tile svg { color: #1a3664 !important; stroke: #1a3664 !important; }"""

new_icon_tile = """    body.light .icon-tile {
      background: rgba(37,99,235,0.08) !important;
      border: 1px solid rgba(37,99,235,0.2) !important;
      color: #2563eb !important;
      box-shadow: none !important;
    }
    body.light .icon-tile::after { background: none !important; }
    body.light .icon-tile i, body.light .icon-tile svg { color: #2563eb !important; stroke: #2563eb !important; }"""

content = content.replace(old_icon_tile, new_icon_tile)

# Fix roadmap — keep white background but dark blue heading, dark text items
old_roadmap = """    body.light .roadmap-year h3 { color: #60a5fa !important; }
    body.light .roadmap-year ul li { color: #ffffff !important; background: rgba(255,255,255,0.07) !important; border-color: rgba(255,255,255,0.12) !important; }
    body.light .roadmap-year ul li::before { background: #60a5fa !important; }"""

new_roadmap = """    body.light .roadmap-year h3 { color: #1e40af !important; }
    body.light .roadmap-year ul li { color: #0f172a !important; background: rgba(37,99,235,0.06) !important; border-color: rgba(37,99,235,0.15) !important; }
    body.light .roadmap-year ul li::before { background: #2563eb !important; }"""

content = content.replace(old_roadmap, new_roadmap)

# Fix journey steps — white cards → dark text
old_journey = """    body.light .journey-step h4 { color: #ffffff !important; }
    body.light .journey-step { color: #ffffff !important; }
    body.light .journey-arrow { color: #60a5fa !important; }
    body.light .j-icon { color: #ffffff !important; }"""

new_journey = """    body.light .journey-step h4 { color: #0f172a !important; }
    body.light .journey-step { color: #0f172a !important; }
    body.light .journey-arrow { color: #2563eb !important; }
    body.light .j-icon { color: #2563eb !important; }"""

content = content.replace(old_journey, new_journey)

# Fix contact form heading
old_contact = """    body.light .contact-form h3 { color: #ffffff !important; }
    body.light .contact-form label { color: #94a3b8 !important; }"""

new_contact = """    body.light .contact-form h3 { color: #0f172a !important; }
    body.light .contact-form label { color: #475569 !important; }"""

content = content.replace(old_contact, new_contact)

# Fix career cards
old_career = """    body.light .career-card h4 { color: #ffffff !important; }
    body.light .career-card p { color: #94a3b8 !important; }
    body.light .career-card h3 { color: #ffffff !important; }"""

new_career = """    body.light .career-card h4 { color: #0f172a !important; }
    body.light .career-card p { color: #475569 !important; }
    body.light .career-card h3 { color: #0f172a !important; }"""

content = content.replace(old_career, new_career)

# Fix consult card headings and resource cards that were forced dark
old_consult_c = """    body.light .consult-card h3 { color: #ffffff !important; }
    body.light .consult-card p { color: #94a3b8 !important; }"""
new_consult_c = """    body.light .consult-card h3 { color: #0f172a !important; }
    body.light .consult-card p { color: #475569 !important; }"""
content = content.replace(old_consult_c, new_consult_c)

# Resource cards — keep dark since they have image overlays
old_res = """    /* Resource cards — white text in light mode */
    body.light .resource-card { color: #ffffff !important; }
    body.light .resource-card h4 { color: #ffffff !important; }
    body.light .resource-card p { color: #94a3b8 !important; }
    body.light .resource-card a { color: #60a5fa !important; }
    body.light .resource-card a:hover { color: #ffffff !important; }"""
new_res = """    /* Resource cards — keep dark background since they have image overlays */
    body.light .resource-card { background: #0d1625 !important; color: #ffffff !important; }
    body.light .resource-card h4 { color: #ffffff !important; }
    body.light .resource-card p { color: #94a3b8 !important; }
    body.light .resource-card a { color: #60a5fa !important; }
    body.light .resource-card a:hover { color: #ffffff !important; }"""
content = content.replace(old_res, new_res)

# Fix trusted-icon-box to use blue tint instead of white
old_trusted_icon = """    body.light .trusted-icon-box {
      color: #ffffff !important;
    }
    body.light .trusted-icon-box i, body.light .trusted-icon-box svg {
      color: #ffffff !important;
      stroke: #ffffff !important;
    }"""
new_trusted_icon = """    body.light .trusted-icon-box {
      background: rgba(37,99,235,0.08) !important;
      border: 1px solid rgba(37,99,235,0.2) !important;
      color: #2563eb !important;
    }
    body.light .trusted-icon-box i, body.light .trusted-icon-box svg {
      color: #2563eb !important;
      stroke: #2563eb !important;
    }"""
content = content.replace(old_trusted_icon, new_trusted_icon)

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Light mode icon and text patches applied.")
