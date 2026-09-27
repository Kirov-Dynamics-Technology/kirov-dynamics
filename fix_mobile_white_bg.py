with open('docs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─── 1. Fix the top inline script — apply body.light IMMEDIATELY, not after DOMContentLoaded ───
old_top = """  <script>
    (function(){
      var t = localStorage.getItem('kirov-theme');
      if (t === 'light') {
        document.documentElement.classList.add('light');
        window.addEventListener('DOMContentLoaded', function() { document.body.classList.add('light'); });
      }
    })();
  </script>
  <style>html.light body, body.light { background: #ffffff !important; }</style>"""

new_top = """  <script>
    (function(){
      var t = localStorage.getItem('kirov-theme');
      if (t === 'light') {
        document.documentElement.classList.add('light');
        // Apply immediately to <html> so CSS vars resolve correctly before body paints
      }
    })();
  </script>
  <style>
    /* Apply light CSS variables to html.light so sections resolve var(--bg-alt) correctly
       even before <body> is parsed. This eliminates grey flash and mobile grey sections. */
    html.light, html.light body {
      --bg:       #ffffff !important;
      --bg-alt:   #ffffff !important;
      --bg-card:  #ffffff !important;
      --text:     #0f172a !important;
      --muted:    #475569 !important;
      --border:   rgba(37,99,235,0.15) !important;
      background: #ffffff !important;
    }
    /* Belt carousels keep slight tint so they stand out */
    html.light .carousel-viewport, html.light .partners-viewport {
      background: #f8fafc !important;
    }
  </style>"""

content = content.replace(old_top, new_top)

# ─── 2. Fix the bottom toggle — also toggle html class and update CSS vars at runtime ───
old_toggle_fn = """  function switchTheme() {
    body.classList.toggle('light');
    document.documentElement.classList.toggle('light');
    var isLight = body.classList.contains('light');
    localStorage.setItem('kirov-theme', isLight ? 'light' : 'dark');"""

new_toggle_fn = """  function switchTheme() {
    body.classList.toggle('light');
    document.documentElement.classList.toggle('light');
    var isLight = body.classList.contains('light');
    localStorage.setItem('kirov-theme', isLight ? 'light' : 'dark');
    // Force background immediately so no grey flash on toggle
    document.body.style.background = isLight ? '#ffffff' : '';"""

content = content.replace(old_toggle_fn, new_toggle_fn)

# ─── 3. Remove the now-redundant carousel bg from the batch fixes (it was #f8fafc grey) ───
# Keep it in — it's good for carousels, just ensure body sections are white.

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done — CSS vars now applied on <html> immediately before body renders.")
