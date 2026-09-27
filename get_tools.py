import re
f = open('docs/index.html', 'r', encoding='utf-8')
c = f.read()
f.close()

m = re.search(r'<section[^>]+id=[\'\"]tools[\'\"]', c)
if m:
    print(c[m.start():m.end()+3000])

m_css = re.search(r'\.tool-card[^}]*\{', c)
if m_css:
    print("\nCSS:")
    idx = max(0, m_css.start() - 100)
    print(c[idx:idx+800])
