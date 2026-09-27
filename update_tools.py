with open('docs/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Find the tools section boundaries
m = re.search(r'<section id=[\"\']tools[\"\'][^>]*>', content)
if m:
    start = m.start()
    depth = 0
    tag_pattern = re.compile(r'<\s*section[^>]*>|<\s*/\s*section\s*>', re.IGNORECASE)
    end = -1
    for match in tag_pattern.finditer(content, start):
        if '/' not in match.group():
            depth += 1
        else:
            depth -= 1
        if depth == 0:
            end = match.end()
            break
            
    if end != -1:
        new_tools = """<section id="tools" class="section" style="background:var(--bg-alt)" aria-labelledby="tools-title">
  <div class="container">
    <div class="reveal text-center" style="margin-bottom: 48px;">
      <div style="display:flex; align-items:center; justify-content:center; gap:12px; margin-bottom:12px;">
        <i data-lucide="settings" style="color:var(--accent); width:28px; height:28px;"></i>
        <h2 class="section-title" id="tools-title" style="margin:0; font-size:1.8rem;">Project & Business Calculators</h2>
      </div>
      <p class="section-sub" style="margin:0 auto">Quickly calculate costs, margins and estimates for your projects.</p>
    </div>
    
    <style>
      .tools-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
      }
      .card-tool {
        background: var(--bg-card);
        border: 1px solid rgba(37,99,235,0.3);
        border-radius: 12px;
        padding: 24px;
        display: flex;
        flex-direction: column;
        height: 100%;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
      }
      .card-tool:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        border-color: rgba(37,99,235,0.6);
      }
      .card-tool-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 24px;
      }
      .card-tool-badge {
        background: #2563eb;
        color: #fff;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 700;
      }
      .card-tool-body {
        flex: 1;
        display: flex;
        flex-direction: column;
        gap: 12px;
      }
      .card-tool-row {
        display: flex;
        gap: 12px;
      }
      .card-tool-input {
        width: 100%;
        background: rgba(15,23,42,0.6);
        border: 1px solid rgba(37,99,235,0.3);
        border-radius: 6px;
        padding: 12px;
        color: #fff;
        font-size: 0.9rem;
        outline: none;
      }
      .card-tool-input:focus {
        border-color: #2563eb;
      }
      html.light .card-tool-input {
        background: #fff;
        color: #0f172a;
      }
      .card-tool-btn {
        width: 100%;
        padding: 12px;
        border: none;
        border-radius: 6px;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 0.95rem;
        cursor: pointer;
        margin-top: auto;
        text-align: center;
        transition: opacity 0.2s;
        text-decoration: none;
        display: inline-block;
      }
      .card-tool-btn:hover {
        opacity: 0.9;
      }
      .sec-check-label {
        display: flex;
        gap: 10px;
        align-items: flex-start;
        color: var(--muted);
        font-size: 0.85rem;
        cursor: pointer;
        line-height: 1.4;
      }
      .sec-check-label input {
        margin-top: 3px;
      }
      
      /* Responsive */
      @media (max-width: 992px) {
        .tools-grid { grid-template-columns: repeat(2, 1fr); }
      }
      @media (max-width: 768px) {
        .tools-grid { grid-template-columns: 1fr; }
        /* Make Project Cost and Cyber side-by-side on mobile if possible, but 1fr is safer for inputs */
      }
    </style>

    <div class="reveal tools-grid">
      <!-- 1. VAT Calculator -->
      <div class="card-tool">
        <div class="card-tool-header">
          <i data-lucide="percent" style="color:var(--accent);width:28px;height:28px"></i>
          <span class="card-tool-badge">VAT Calculator</span>
        </div>
        <div class="card-tool-body">
          <input type="number" id="vat-amount" placeholder="Enter amount (R)" class="card-tool-input">
          <div id="vat-result" class="card-tool-result" style="color:var(--muted);font-size:0.85rem;margin-bottom:12px"></div>
          <button id="calc-vat-btn" class="card-tool-btn" style="background:#0ea5e9;color:#fff">Calculate</button>
        </div>
      </div>

      <!-- 2. Profit Margin Calculator -->
      <div class="card-tool">
        <div class="card-tool-header">
          <i data-lucide="trending-up" style="color:var(--green);width:28px;height:28px"></i>
          <span class="card-tool-badge">Profit Margin Calculator</span>
        </div>
        <div class="card-tool-body">
          <div class="card-tool-row">
            <input type="number" id="pm-revenue" placeholder="Revenue (R)" class="card-tool-input">
            <input type="number" id="pm-cost" placeholder="Cost (R)" class="card-tool-input">
          </div>
          <div id="pm-result" class="card-tool-result" style="color:var(--muted);font-size:0.85rem;margin-bottom:12px"></div>
          <button id="calc-margin-btn" class="card-tool-btn" style="background:#10b981;color:#fff">Calculate Margin</button>
        </div>
      </div>

      <!-- 3. Fleet Fuel Cost -->
      <div class="card-tool">
        <div class="card-tool-header">
          <i data-lucide="fuel" style="color:var(--gold);width:28px;height:28px"></i>
          <span class="card-tool-badge">Fleet Fuel Cost Calculator</span>
        </div>
        <div class="card-tool-body">
          <div class="card-tool-row">
            <input type="number" id="fuel-km" placeholder="Monthly km" class="card-tool-input">
            <input type="number" id="fuel-l100" placeholder="Litres / 100km" class="card-tool-input">
          </div>
          <input type="number" id="fuel-price" placeholder="Fuel price (R/L)" class="card-tool-input">
          <div id="fuel-result" class="card-tool-result" style="color:var(--muted);font-size:0.85rem;margin-bottom:12px"></div>
          <button id="calc-fuel-btn" class="card-tool-btn" style="background:#f59e0b;color:#fff">Calculate Cost</button>
        </div>
      </div>

      <!-- 4. Project Cost Estimator -->
      <div class="card-tool">
        <div class="card-tool-header">
          <i data-lucide="hard-hat" style="color:var(--gold);width:28px;height:28px"></i>
          <span class="card-tool-badge">Project Cost Estimator</span>
        </div>
        <div class="card-tool-body">
          <input type="number" id="pc-labour" placeholder="Labour cost (R)" class="card-tool-input">
          <input type="number" id="pc-materials" placeholder="Materials cost (R)" class="card-tool-input">
          <input type="number" id="pc-margin" placeholder="Target margin (%)" class="card-tool-input">
          <div id="pc-result" class="card-tool-result" style="color:var(--muted);font-size:0.85rem;margin-bottom:12px"></div>
          <button id="calc-project-btn" class="card-tool-btn" style="background:#f59e0b;color:#fff">Calculate Quote</button>
        </div>
      </div>

      <!-- 5. Cybersecurity Checklist -->
      <div class="card-tool">
        <div class="card-tool-header">
          <i data-lucide="shield-check" style="color:#0ea5e9;width:28px;height:28px"></i>
          <span class="card-tool-badge">Cybersecurity Checklist</span>
        </div>
        <div class="card-tool-body" style="gap:8px;">
          <label class="sec-check-label"><input type="checkbox" id="sec1"> Multi-factor authentication (MFA) enabled</label>
          <label class="sec-check-label"><input type="checkbox" id="sec2"> Regular automated backups</label>
          <label class="sec-check-label"><input type="checkbox" id="sec3"> Antivirus/EDR on all devices</label>
          <label class="sec-check-label"><input type="checkbox" id="sec4"> Employee security training done</label>
          <label class="sec-check-label"><input type="checkbox" id="sec5"> POPIA privacy policy in place</label>
          <div id="sec-result" class="card-tool-result" style="color:var(--muted);font-size:0.85rem;margin-bottom:6px"></div>
          <button id="calc-security-btn" class="card-tool-btn" style="background:#0ea5e9;color:#fff">Check My Score</button>
        </div>
      </div>

      <!-- 6. More Tools Coming -->
      <div class="card-tool" style="justify-content:space-between;">
        <div>
          <div class="card-tool-header" style="justify-content:center; margin-bottom:16px;">
            <i data-lucide="wrench" style="color:#3b82f6;width:36px;height:36px"></i>
          </div>
          <div style="text-align:center; margin-bottom:16px;">
            <span class="card-tool-badge" style="display:inline-block; margin-bottom:12px;">More Tools Coming</span>
            <p style="color:var(--muted);font-size:0.85rem;line-height:1.5;">Payroll estimator, invoice generator, construction BOQ helper, AI readiness score and more.</p>
          </div>
        </div>
        <div class="card-tool-body">
          <a href="#contact" class="card-tool-btn" style="background:#2563eb;color:#fff;margin-top:auto;">Request a tool →</a>
        </div>
      </div>
    </div>
  </div>
</section>"""
        
        content = content[:start] + new_tools + content[end:]
        with open('docs/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Replaced tools section successfully.")
else:
    print("Could not find tools section!")
