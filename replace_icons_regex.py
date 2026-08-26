import re

with open('docs/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add Lucide JS at the end if not already present
if 'lucide@latest' not in text:
    text = text.replace('</body>', '  <!-- Lucide Icons -->\n  <script src="https://unpkg.com/lucide@latest"></script>\n  <script>\n    lucide.createIcons();\n  </script>\n</body>')

# 1. Divisions
div_map = {
    'Digital Transformation': 'monitor-smartphone',
    'AI Solutions': 'bot',
    'Cybersecurity': 'shield-check',
    'Smart Infrastructure': 'building-2',
    'Engineering Technology': 'cog',
    'Government Technology': 'landmark',
    'Consulting': 'target'
}
for name, icon in div_map.items():
    pattern = r'(<div class="division-icon" aria-hidden="true">).*?(</div>\s*<h3>' + re.escape(name) + r')'
    text = re.sub(pattern, r'\g<1><i data-lucide="' + icon + r'"></i>\g<2>', text, flags=re.DOTALL)

# 2. Products/Services (product-icon)
prod_map = {
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
for name, icon in prod_map.items():
    pattern = r'(<span class="product-icon" aria-hidden="true">).*?(</span>\s*<h3>' + re.escape(name) + r')'
    text = re.sub(pattern, r'\g<1><i data-lucide="' + icon + r'"></i>\g<2>', text, flags=re.DOTALL)

# 3. Stats (stat-icon)
stat_map = {
    'Projects Delivered': 'check-circle-2',
    'Lines of Code': 'code-2',
    'Uptime': 'activity',
    'Enterprise Clients': 'users'
}
for name, icon in stat_map.items():
    pattern = r'(<div class="stat-icon" aria-hidden="true">).*?(</div>\s*<div class="stat-number".*?>.*?</div>\s*<div class="stat-label">' + re.escape(name) + r'</div>)'
    text = re.sub(pattern, r'\g<1><i data-lucide="' + icon + r'"></i>\g<2>', text, flags=re.DOTALL)

# 4. Service list checkmarks
text = re.sub(r'<li>\s*<span aria-hidden="true">.*?</span>', r'<li><span aria-hidden="true"><i data-lucide="check" style="color:var(--teal); width:18px; height:18px; margin-right:8px;"></i></span>', text)

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Replacement complete!")
