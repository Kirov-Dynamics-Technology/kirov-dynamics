import re

with open('docs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the trusted-by section
m = re.search(r'<section[^>]+id=["\']trusted-by["\'][^>]*>', content)
if m:
    print("Found trusted-by at:", m.start())
    print(content[m.start():m.start()+1500])
else:
    print("Not found - searching for 'Trusted by'")
    idx = content.find('Trusted by Customers')
    if idx == -1:
        idx = content.find('Trusted by')
    if idx != -1:
        print(content[max(0,idx-300):idx+800])
