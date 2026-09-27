import re
f = open('docs/index.html', 'r', encoding='utf-8')
c = f.read()
f.close()

m = re.search(r'<section id=[\"\']tools[\"\'][^>]*>', c)
if m:
    start = m.start()
    end = c.find('</section>', start) + 10
    with open('tools_section.html', 'w', encoding='utf-8') as out:
        out.write(c[start:end])
    print('Saved to tools_section.html')
