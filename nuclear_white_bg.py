with open('docs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Nuclear approach: directly override EVERY section background in light mode
# instead of relying on CSS var cascade (which mobile browsers can mishandle)

nuclear_css = """
    /* ======= NUCLEAR WHITE BACKGROUND FIX FOR MOBILE =======
       Do NOT rely on CSS var cascade — directly set background on every section */
    html.light body,
    body.light {
      background-color: #ffffff !important;
    }
    html.light #about,
    html.light #why,
    html.light #services,
    html.light #solutions,
    html.light #industries,
    html.light #process,
    html.light #testimonials,
    html.light #security,
    html.light #certifications,
    html.light #resources,
    html.light #roadmap,
    html.light #careers,
    html.light #contact,
    html.light #consult,
    html.light #projects,
    html.light #team,
    html.light #insights,
    html.light #partners,
    html.light #map,
    html.light #engine,
    html.light #journey,
    html.light footer,
    body.light #about,
    body.light #why,
    body.light #services,
    body.light #solutions,
    body.light #industries,
    body.light #process,
    body.light #testimonials,
    body.light #security,
    body.light #certifications,
    body.light #resources,
    body.light #roadmap,
    body.light #careers,
    body.light #contact,
    body.light #consult,
    body.light #projects,
    body.light #team,
    body.light #insights,
    body.light #partners,
    body.light #map,
    body.light #engine,
    body.light #journey,
    body.light footer {
      background-color: #ffffff !important;
      background-image: none !important;
    }
    /* Hero and Stack keep dark backgrounds */
    html.light #hero, body.light #hero {
      background-color: #03050a !important;
      background-image: none !important;
    }
    html.light #stack, body.light #stack {
      background: radial-gradient(ellipse 80% 60% at 50% 50%, #0a1020, #03050a) !important;
    }
"""

# Insert right after the opening <style> block in the head (before body.light { })
target = '    body.light {\n      --bg:          #ffffff;'
content = content.replace(target, nuclear_css + '\n    body.light {\n      --bg:          #ffffff;')

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Nuclear white background fix applied.")
