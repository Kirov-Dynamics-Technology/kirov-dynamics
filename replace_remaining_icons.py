import re

with open('docs/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 5. Services (service-icon)
srv_map = {
    'Custom Software Development': 'code',
    'Cloud Architecture & Migration': 'cloud-cog',
    'Data Analytics & AI': 'brain-circuit',
    'Cybersecurity Solutions': 'shield-alert',
    'Enterprise Architecture': 'network',
    'Technology Consulting': 'lightbulb'
}
for name, icon in srv_map.items():
    pattern = r'(<span class="service-icon" aria-hidden="true">).*?(</span>\s*<h3>' + re.escape(name) + r')'
    text = re.sub(pattern, r'\g<1><i data-lucide="' + icon + r'"></i>\g<2>', text, flags=re.DOTALL)

# 6. Industries (tile-icon)
ind_map = {
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
for name, icon in ind_map.items():
    pattern = r'(<span class="tile-icon" aria-hidden="true">).*?(</span>\s*<span class="tile-name">' + re.escape(name) + r')'
    text = re.sub(pattern, r'\g<1><i data-lucide="' + icon + r'"></i>\g<2>', text, flags=re.DOTALL)

# Fallback: remove ANY remaining strange unicode text inside elements that look like icons just in case we missed some:
text = re.sub(r'(class="(?:service|product|stat|division|tile)-icon".*?>)[^<]+(</(?:span|div)>)', r'\g<1><i data-lucide="check-circle"></i>\g<2>', text)

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Replaced all remaining mojibake icons!")
