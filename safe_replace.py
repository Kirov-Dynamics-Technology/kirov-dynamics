import re

with open('docs/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix typography mojibake
text = text.replace('ÔÇö', '—')
text = text.replace('┬À', '·')
text = text.replace('ÔÇÖ', "'")
text = text.replace('ÔÇ£', '"')
text = text.replace('ÔÇØ', '"')

# Divisions
divs = {
    'Digital Transformation': 'monitor-smartphone',
    'AI Solutions': 'bot',
    'Cybersecurity': 'shield-check',
    'Smart Infrastructure': 'building-2',
    'Engineering Technology': 'cog',
    'Government Technology': 'landmark',
    'Consulting': 'target'
}
for name, icon in divs.items():
    pattern = r'<div class="division-icon" aria-hidden="true">[^<]*</div>\s*<h3>' + re.escape(name) + r'</h3>'
    repl = f'<div class="division-icon" aria-hidden="true"><i data-lucide="{icon}"></i></div>\n        <h3>{name}</h3>'
    text = re.sub(pattern, repl, text)

# Services
srvs = {
    'Custom Software Development': 'code',
    'Cloud Architecture & Migration': 'cloud-cog',
    'Data Analytics & AI': 'brain-circuit',
    'Cybersecurity Solutions': 'shield-alert',
    'Enterprise Architecture': 'network',
    'Technology Consulting': 'lightbulb'
}
for name, icon in srvs.items():
    pattern = r'<span class="service-icon" aria-hidden="true">[^<]*</span>\s*<h3>' + re.escape(name) + r'</h3>'
    repl = f'<span class="service-icon" aria-hidden="true"><i data-lucide="{icon}"></i></span>\n          <h3>{name}</h3>'
    text = re.sub(pattern, repl, text)

# Industries
inds = {
    'Mining & Resources': 'pickaxe',
    'Financial Services': 'landmark',
    'Healthcare': 'heart-pulse',
    'Public Sector': 'building-2',
    'Agriculture': 'tractor',
    'Manufacturing': 'factory',
    'Logistics & Supply Chain': 'truck',
    'Telecommunications': 'satellite-dish',
    'Retail & E-commerce': 'shopping-cart',
    'Energy & Utilities': 'zap',
    'Education': 'graduation-cap',
    'Real Estate': 'home',
    'Media & Entertainment': 'clapperboard',
    'Hospitality & Tourism': 'plane'
}
for name, icon in inds.items():
    pattern = r'<span class="tile-icon" aria-hidden="true">[^<]*</span>\s*<span class="tile-name">' + re.escape(name) + r'</span>'
    repl = f'<span class="tile-icon" aria-hidden="true"><i data-lucide="{icon}"></i></span>\n          <span class="tile-name">{name}</span>'
    text = re.sub(pattern, repl, text)

# Products
prods = {
    'Enterprise AI Platforms': 'server',
    'Secure Cloud Architectures': 'cloud',
    'Data & Analytics Systems': 'bar-chart-3',
    'GovTech Solutions': 'landmark',
    'Agritech Systems': 'leaf',
    'Smart Logistics Platforms': 'truck',
    'FinTech Security': 'shield',
    'IoT Networks': 'wifi',
    'PropTech Platforms': 'building',
    'Robotic Process Automation': 'bot'
}
for name, icon in prods.items():
    pattern = r'<span class="product-icon" aria-hidden="true">[^<]*</span>\s*<h3>' + re.escape(name) + r'</h3>'
    repl = f'<span class="product-icon" aria-hidden="true"><i data-lucide="{icon}"></i></span>\n          <h3>{name}</h3>'
    text = re.sub(pattern, repl, text)

# Stats
stats = {
    'Projects Delivered': 'check-circle-2',
    'Lines of Code': 'code-2',
    'Uptime': 'activity',
    'Enterprise Clients': 'users'
}
for name, icon in stats.items():
    # stat-icon ... <div class="stat-number"...> ... <div class="stat-label">Projects Delivered</div>
    pattern = r'(<div class="stat-icon" aria-hidden="true">)[^<]*(</div>\s*<div class="stat-number"[^>]*>[^<]*</div>\s*<div class="stat-label">)' + re.escape(name) + r'(</div>)'
    text = re.sub(pattern, r'\g<1><i data-lucide="' + icon + r'"></i>\g<2>' + name + r'\g<3>', text)

# Generic fallback for any remaining division, service, product, or tile icons that didn't match the names
text = re.sub(r'<div class="division-icon" aria-hidden="true">[^<]+</div>', r'<div class="division-icon" aria-hidden="true"><i data-lucide="check-circle"></i></div>', text)
text = re.sub(r'<span class="service-icon" aria-hidden="true">[^<]+</span>', r'<span class="service-icon" aria-hidden="true"><i data-lucide="check-circle"></i></span>', text)
text = re.sub(r'<span class="tile-icon" aria-hidden="true">[^<]+</span>', r'<span class="tile-icon" aria-hidden="true"><i data-lucide="check-circle"></i></span>', text)
text = re.sub(r'<span class="product-icon" aria-hidden="true">[^<]+</span>', r'<span class="product-icon" aria-hidden="true"><i data-lucide="check-circle"></i></span>', text)

# Refresh redirect to top snippet
js_snippet = """
<script>
  // Ensure the page scrolls to top on refresh
  if (history.scrollRestoration) {
    history.scrollRestoration = 'manual';
  }
  window.onload = function() {
    window.scrollTo(0, 0);
    // Remove hash from URL to prevent jumping to section
    if (window.location.hash) {
      history.replaceState(null, null, ' ');
    }
  };
</script>
</body>
"""
text = text.replace('</body>', js_snippet)

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Safe replace complete!")
