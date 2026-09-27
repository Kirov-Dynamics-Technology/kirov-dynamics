import re

f = open('docs/index.html', 'r', encoding='utf-8')
c = f.read()
f.close()

# Find all section tags with IDs
sections = re.findall(r'<section[^>]+id=["\']([^"\']+)["\']', c)
print('SECTION IDs:', sections)

# Also find the background patterns to see what classes/IDs are used
bg_lines = [(c.count('\n',0,m.start())+1, m.group()) for m in re.finditer(r'background:var\(--bg-alt\)', c)]
print('\nLines using var(--bg-alt) as background:')
for line, txt in bg_lines:
    # Get the selector above it
    snippet = c[max(0, c.rfind('{', 0, c.rfind(txt))-60):c.rfind(txt)+30]
    print(f'  Line {line}')
