with open('docs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_css = """      /* Responsive */
      @media (max-width: 992px) {
        .tools-grid { grid-template-columns: repeat(2, 1fr); }
      }
      @media (max-width: 768px) {
        .tools-grid { grid-template-columns: 1fr; }
        /* Make Project Cost and Cyber side-by-side on mobile if possible, but 1fr is safer for inputs */
      }"""

new_css = """      /* Responsive */
      @media (max-width: 1100px) {
        .tools-grid { grid-template-columns: repeat(2, 1fr); }
      }
      @media (max-width: 640px) {
        .tools-grid { grid-template-columns: 1fr; }
        .card-tool-row { flex-direction: column; }
      }"""

content = content.replace(old_css, new_css)

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Breakpoints fixed.")
