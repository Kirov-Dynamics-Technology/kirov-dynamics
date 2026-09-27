import os

pages = {
    "privacy.html": "Privacy Policy & Data Disclosure",
    "terms.html": "Terms of Use",
    "compliance.html": "Data & Compliance",
    "ip.html": "IP Infringement"
}

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Kirov Dynamics</title>
  <style>
    body {{ font-family: 'Inter', sans-serif; background: #03050a; color: #f1f5f9; margin: 0; padding: 40px; line-height: 1.6; }}
    .container {{ max-width: 800px; margin: 0 auto; }}
    h1 {{ color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 20px; }}
    a {{ color: #60a5fa; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .back {{ display: inline-block; margin-bottom: 20px; font-weight: 600; }}
  </style>
</head>
<body>
  <div class="container">
    <a href="index.html" class="back">&larr; Back to Home</a>
    <h1>{title}</h1>
    <p>This page is currently being updated. Please check back later for the full {title}.</p>
    <p>&copy; 2026 Kirov Dynamics Technology.</p>
  </div>
</body>
</html>
"""

for filename, title in pages.items():
    with open(f"docs/{filename}", "w", encoding="utf-8") as f:
        f.write(template.format(title=title))
