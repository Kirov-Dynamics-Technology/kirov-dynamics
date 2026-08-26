import re

with open('docs/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    '💻': '<i data-lucide="monitor"></i>',
    '🤖': '<i data-lucide="bot"></i>',
    '🔐': '<i data-lucide="shield-check"></i>',
    '🏙️': '<i data-lucide="building-2"></i>',
    '⚙️': '<i data-lucide="cog"></i>',
    '🏛️': '<i data-lucide="landmark"></i>',
    '🎯': '<i data-lucide="target"></i>',
    '🚀': '<i data-lucide="rocket"></i>',
    '🌍': '<i data-lucide="globe"></i>',
    '🏗️': '<i data-lucide="hard-hat"></i>',
    '🏥': '<i data-lucide="activity"></i>',
    '🎓': '<i data-lucide="graduation-cap"></i>',
    '🌱': '<i data-lucide="leaf"></i>',
    '⚡': '<i data-lucide="zap"></i>',
    '📡': '<i data-lucide="satellite"></i>',
    '✅': '<i data-lucide="check-circle-2"></i>',
    '💰': '<i data-lucide="coins"></i>',
    '🚜': '<i data-lucide="tractor"></i>',
    '✈️': '<i data-lucide="plane"></i>'
}

for emoji, lucide in replacements.items():
    text = text.replace(emoji, lucide)

if 'lucide@latest' not in text:
    text = text.replace('</body>', '  <!-- Lucide Icons -->\n  <script src="https://unpkg.com/lucide@latest"></script>\n  <script>\n    lucide.createIcons();\n  </script>\n</body>')

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Replaced emojis with Lucide icons.")
