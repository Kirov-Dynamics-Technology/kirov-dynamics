import re

f = open('docs/index.html', 'r', encoding='utf-8')
c = f.read()
f.close()

# Look for btn classes next to each other
matches = re.finditer(r'<a[^>]*class=["\'][^"\']*btn[^"\']*["\'][^>]*>.*?</a>', c, re.DOTALL)
btns = []
for m in matches:
    line = c.count('\n', 0, m.start()) + 1
    btns.append((line, m.group()))

for i in range(len(btns)-1):
    if btns[i+1][0] - btns[i][0] < 5:
        print(f"Buttons close together around line {btns[i][0]}:")
        print(f"  {btns[i][1][:80]}")
        print(f"  {btns[i+1][1][:80]}\n")

