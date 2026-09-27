with open('docs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Find the nuclear CSS block and replace it
nuclear_start = content.find('/* ======= NUCLEAR WHITE BACKGROUND FIX FOR MOBILE =======')
nuclear_end = content.find('/* Hero and Stack keep dark backgrounds */')

if nuclear_start != -1 and nuclear_end != -1:
    old_nuclear = content[nuclear_start:nuclear_end]
    
    # New nuclear CSS with correct IDs
    new_nuclear = """/* ======= NUCLEAR WHITE BACKGROUND FIX FOR MOBILE =======
       Do NOT rely on CSS var cascade — directly set background on every section */
    html.light body,
    body.light {
      background-color: #ffffff !important;
    }
    
    html.light section, body.light section,
    html.light header, body.light header,
    html.light footer, body.light footer,
    html.light #why-choose, body.light #why-choose,
    html.light #solutions, body.light #solutions,
    html.light #products, body.light #products,
    html.light #industries, body.light #industries,
    html.light #roi, body.light #roi,
    html.light #assessment, body.light #assessment,
    html.light #tools, body.light #tools,
    html.light #projects, body.light #projects,
    html.light #process, body.light #process,
    html.light #testimonials, body.light #testimonials,
    html.light #leadership, body.light #leadership,
    html.light #about, body.light #about,
    html.light #divisions, body.light #divisions,
    html.light #services, body.light #services,
    html.light #industries-deep, body.light #industries-deep,
    html.light #platforms, body.light #platforms,
    html.light #security, body.light #security,
    html.light #partners, body.light #partners,
    html.light #trusted-by, body.light #trusted-by,
    html.light #insights, body.light #insights,
    html.light #africa-map, body.light #africa-map,
    html.light #consultation, body.light #consultation,
    html.light #resources, body.light #resources,
    html.light #careers, body.light #careers,
    html.light #roadmap, body.light #roadmap,
    html.light #journey, body.light #journey,
    html.light #contact, body.light #contact,
    html.light #metrics, body.light #metrics {
      background-color: #ffffff !important;
      background-image: none !important;
    }
    """
    
    content = content.replace(old_nuclear, new_nuclear)

    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed nuclear CSS with correct section IDs.")
else:
    print("Could not find nuclear CSS block.")
