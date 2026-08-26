import re

with open('docs/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all characters that are non-ASCII and print them out with context
matches = re.finditer(r'([^\x00-\x7F]+)', text)
found_emojis = set()
for m in matches:
    char = m.group(1)
    if len(char) <= 4: # Likely an emoji
        found_emojis.add(char)

print("Found non-ascii characters:", list(found_emojis))
