---
title: "Webshop"
description: "



  
  
  CloudStudio Restoration OFX Plugins
  
  
    :root {
      --bg: #0b1020;
      --panel: rgba(255,255,255,0.06);
      --panel2: rgba(255..."
pubDate: 2026-04-12
author: "blake2019"
---


<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>CloudStudio Restoration OFX Plugins</title>
  <meta name="description" content="CloudStudio Restoration OFX plugins for DaVinci Resolve. Buy the full suite or individual plugins." />
  <style>
    :root {
      --bg: #0b1020;
      --panel: rgba(255,255,255,0.06);
      --panel2: rgba(255,255,255,0.08);
      --text: #e8eeff;
      --muted: rgba(232,238,255,0.72);
      --muted2: rgba(232,238,255,0.55);
      --accent: #7c5cff;
      --accent2: #2dd4bf;
      --danger: #ef4444;
      --shadow: rgba(0,0,0,0.35);
      --ring: rgba(124,92,255,0.55);
    }

    * { box-sizing: border-box; }
    html, body { height: 100%; }
    body {
      margin: 0;
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji";
      color: var(--text);
      background:
        radial-gradient(1200px 800px at 20% 0%, rgba(124,92,255,0.25), transparent 60%),
        radial-gradient(1000px 700px at 80% 10%, rgba(45,212,191,0.18), transparent 55%),
        linear-gradient(180deg, #070a14 0%, var(--bg) 55%, #060816 100%);
      line-height: 1.35;
    }

    a { color: inherit; text-decoration: none; }

    .container {
      max-width: 1100px;
      margin: 0 auto;
      padding: 28px 18px 64px;
    }

    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 14px 14px;
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 16px;
      background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
      box-shadow: 0 18px 60px var(--shadow);
      backdrop-filter: blur(8px);
    }

    .brand {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .brand .title {
      font-size: 16px;
      letter-spacing: 0.2px;
      font-weight: 650;
    }
    .brand .subtitle {
      font-size: 13px;
      color: var(--muted);
    }

    .toplinks {
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
      justify-content: flex-end;
    }

    .chip {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 10px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.12);
      background: rgba(255,255,255,0.05);
      color: var(--muted);
      font-size: 13px;
      transition: transform 140ms ease, border-color 140ms ease;
    }
    .chip:hover { transform: translateY(-1px); border-color: rgba(255,255,255,0.22); }

    .hero {
      margin-top: 26px;
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 18px;
    }

    .heroCard {
      border-radius: 18px;
      border: 1px solid rgba(255,255,255,0.10);
      background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
      box-shadow: 0 18px 60px var(--shadow);
      padding: 22px;
      position: relative;
      overflow: hidden;
    }

    .heroCard h1 {
      margin: 0;
      font-size: 34px;
      line-height: 1.06;
      letter-spacing: -0.4px;
    }

    .heroCard p {
      margin: 12px 0 0;
      color: var(--muted);
      font-size: 15px;
      max-width: 62ch;
    }

    .badges {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 14px;
    }

    .badge {
      font-size: 12px;
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(124,92,255,0.14);
      border: 1px solid rgba(124,92,255,0.25);
      color: rgba(232,238,255,0.86);
    }

    .badge.alt {
      background: rgba(45,212,191,0.12);
      border-color: rgba(45,212,191,0.25);
    }

    .cta {
      margin-top: 18px;
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 10px 14px;
      border-radius: 12px;
      border: 1px solid rgba(255,255,255,0.14);
      background: rgba(255,255,255,0.06);
      color: var(--text);
      font-weight: 600;
      font-size: 14px;
      box-shadow: 0 12px 40px rgba(0,0,0,0.25);
      transition: transform 150ms ease, border-color 150ms ease, background 150ms ease;
    }
    .btn:hover { transform: translateY(-1px); border-color: rgba(255,255,255,0.24); }

    .btn.primary {
      background: linear-gradient(135deg, rgba(124,92,255,0.95), rgba(45,212,191,0.75));
      border-color: rgba(124,92,255,0.55);
      box-shadow: 0 18px 70px rgba(124,92,255,0.22);
    }

    .btn.primary:focus, .btn:focus {
      outline: none;
      box-shadow: 0 0 0 4px var(--ring), 0 18px 70px rgba(124,92,255,0.22);
    }

    .sidebar {
      display: grid;
      gap: 12px;
    }

    .mini {
      border-radius: 18px;
      border: 1px solid rgba(255,255,255,0.10);
      background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
      padding: 18px;
      box-shadow: 0 18px 60px var(--shadow);
    }

    .mini h3 {
      margin: 0;
      font-size: 14px;
      letter-spacing: 0.2px;
    }
    .mini p {
      margin: 8px 0 0;
      color: var(--muted);
      font-size: 13px;
    }

    .section {
      margin-top: 26px;
      border-radius: 18px;
      border: 1px solid rgba(255,255,255,0.10);
      background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
      padding: 20px;
      box-shadow: 0 18px 60px var(--shadow);
    }

    .section h2 {
      margin: 0 0 12px;
      font-size: 16px;
      letter-spacing: 0.2px;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
    }

    .card {
      border-radius: 16px;
      border: 1px solid rgba(255,255,255,0.10);
      background: rgba(255,255,255,0.05);
      padding: 16px;
      position: relative;
      overflow: hidden;
    }

    .card .name {
      font-weight: 700;
      letter-spacing: 0.2px;
      font-size: 14px;
      margin: 0;
    }

    .card .desc {
      margin: 8px 0 0;
      color: var(--muted);
      font-size: 13px;
      min-height: 38px;
    }

    .priceRow {
      margin-top: 12px;
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 10px;
      flex-wrap: wrap;
    }

    .price {
      font-weight: 800;
      font-size: 18px;
      letter-spacing: -0.2px;
    }

    .small {
      font-size: 12px;
      color: var(--muted2);
    }

    .divider {
      height: 1px;
      background: rgba(255,255,255,0.10);
      margin: 14px 0;
    }

    .videoWrap {
      margin-top: 14px;
      border-radius: 16px;
      border: 1px solid rgba(255,255,255,0.10);
      background: rgba(255,255,255,0.04);
      overflow: hidden;
      box-shadow: 0 18px 60px var(--shadow);
    }

    .video {
      display: block;
      width: 100%;
      height: auto;
      background: #000;
    }

    .list {
      display: grid;
      gap: 8px;
      margin: 0;
      padding: 0;
      list-style: none;
    }

    .list li {
      display: flex;
      gap: 10px;
      align-items: flex-start;
      color: var(--muted);
      font-size: 13px;
    }

    .dot {
      width: 8px;
      height: 8px;
      margin-top: 6px;
      border-radius: 999px;
      background: rgba(45,212,191,0.9);
      flex: 0 0 auto;
      box-shadow: 0 0 0 4px rgba(45,212,191,0.12);
    }

    footer {
      margin-top: 26px;
      text-align: center;
      color: var(--muted2);
      font-size: 12px;
    }

    @media (max-width: 980px) {
      .hero { grid-template-columns: 1fr; }
      .grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    }

    @media (max-width: 620px) {
      .grid { grid-template-columns: 1fr; }
      .heroCard h1 { font-size: 28px; }
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="brand">
        <div class="title">CloudStudio Restoration OFX</div>
        <div class="subtitle">Professional film restoration plugins for DaVinci Resolve (OFX)</div>
      </div>
      <nav class="toplinks">
        <a class="chip" href="#suite">Suite</a>
        <a class="chip" href="#plugins">Plugins</a>
        <a class="chip" href="#software">Software</a>
        <a class="chip" href="#mobile">Mobile Apps</a>
        <a class="chip" href="#demo">Demo</a>
        <a class="chip" href="#how">How it works</a>
        <a class="chip" href="colorist.html">Colorist</a>
        <a class="chip" href="biography.html">Biography</a>
        <a class="chip" href="mailto:info@cloudstudio.me">Questions: info@cloudstudio.me</a>
      </nav>
    </header>

    <div class="hero">
      <section class="heroCard">
        <h1>Restore, stabilise and clean your scans — fast.</h1>

        <p>
          A set of OFX plugins designed for high‑quality restoration workflows in DaVinci Resolve.
          Buy the full suite or individual tools. Offline licensing with a simple activation workflow.
        </p>
        <div class="badges">
          <span class="badge">DaVinci Resolve (OFX)</span>
          <span class="badge alt">Offline license</span>
          <span class="badge">macOS</span>
          <span class="badge">Windows (beta)</span>
        </div>
        <div class="cta">
          <a class="btn primary" href="https://paypal.me/blakejones209/1200" target="_blank" rel="noreferrer" aria-label="Buy Restoration OFX Suite for 1200 EUR">Buy Suite — €1200</a>
          <a class="btn" href="#plugins">View individual plugins</a>
          <a class="btn" href="mailto:info@cloudstudio.me">Ask a question</a>
        </div>
        <div class="divider"></div>
        <ul class="list">
          <li><span class="dot"></span><span><strong>Suite license</strong> unlocks all plugins.</span></li>

          <li><span class="dot"></span><span><strong>Individual licenses</strong> available per plugin.</span></li>

          <li><span class="dot"></span><span>After purchase you’ll receive a license key by email (or contact <a href="mailto:info@cloudstudio.me"><u>info@cloudstudio.me</u></a>).</span></li>
        </ul>

        <div class="divider"></div>
        <p style="margin:0;color:var(--muted);font-size:14px;">
          <strong>Try / install:</strong>
          <a href="/downloads/CreativeRestoration-PluginBundle.dmg" download style="color:var(--accent2);text-decoration:underline;">Download macOS DMG</a> ·
          <a href="/downloads/CreativeRestoration-Instructions.pdf" download style="color:var(--accent2);text-decoration:underline;">Install &amp; license guide (PDF)</a>
        </p>
      </section>

      <aside class="sidebar">
        <div class="mini" id="suite">
          <h3>Restoration OFX Suite</h3>

          <p>Everything included. Best value if you’re restoring film regularly.</p>

          <div class="priceRow">
            <div class="price">€1200</div>
            <div class="small">One suite key unlocks all</div>
          </div>
          <div class="divider"></div>
          <a class="btn primary" href="https://paypal.me/blakejones209/1200" target="_blank" rel="noreferrer">Pay with PayPal</a>
        </div>

        <div class="mini">
          <h3>Need help?</h3>
          <p>
            Questions about installation, licensing or workflow? Email
            <a href="mailto:info@cloudstudio.me"><u>info@cloudstudio.me</u></a>.
          </p>
        </div>
      </aside>
    </div>

    <section class="section" id="plugins">
      <h2>Individual Plugins — from €150</h2>

      <div class="grid">
        <div class="card">
          <p class="name">Film Grain Removal</p>
          <p class="desc">Reduce grain while preserving detail. Spatial/temporal options.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Film Stabilizer 3D</p>
          <p class="desc">Stabilisation with marker workflow for tricky archival footage.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Vertical Scratch Fix</p>
          <p class="desc">Reduce vertical scratches and scanning artefacts.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Blue Stain Fix</p>
          <p class="desc">Remove blue/yellow staining with mask and eyedropper tools.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Film Warp Fix</p>
          <p class="desc">Correct warp and distortion for improved stability and alignment.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Technicolor Registration Fix</p>
          <p class="desc">Align color channels and reduce Technicolor registration errors.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Technicolor Look</p>
          <p class="desc">Classic film look emulation with fine-tuned controls.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Optical Sound to WAV</p>
          <p class="desc">Convert optical soundtrack scans into WAV audio output.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Film Colorize AI</p>
          <p class="desc">AI-assisted black & white to color using on-device CoreML models.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Bleach Stain Fix</p>
          <p class="desc">Restore faded / chemically damaged regions with targeted correction controls.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Scratch Paint Fix</p>
          <p class="desc">Manual paint and repair workflow for scratches and small defects.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Detail Recovery</p>
          <p class="desc">Recover perceived detail and texture after heavy restoration processing.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Color Equilizer</p>
          <p class="desc">Fixed-vector Hue & Saturation controls for Red, Green, Blue, Yellow, Cyan and Magenta.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Media Clean</p>
          <p class="desc">Reduce dropouts, dust, dirt and scratches with Fast/Quality modes for timeline and final render.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Noise Reduction</p>
          <p class="desc">Fast spatial + temporal denoise with GPU acceleration (Metal) and detail preservation.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Forensic Enhancement</p>
          <p class="desc">Reveal fine detail with targeted enhancement controls for investigative / archival work.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Look Creator</p>
          <p class="desc">Build custom looks quickly with creative film-style controls and fine tuning.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Cinematic Look Creator</p>
          <p class="desc">Cinematic looks with one dropdown (Neutral, Nitrate, Bleach Bypass, Orange‑Teal, Film Print, Noir, Cyberpunk) plus strength, contrast, saturation and finishing controls.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Dust Buster</p>
          <p class="desc">Automatically detect and remove dust spots and dirt from scanned film frames.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Frame Reconstruction AI</p>
          <p class="desc">AI-powered reconstruction of missing, torn or severely damaged frames using surrounding context.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Image Stabilizer</p>
          <p class="desc">Stabilise footage using still-image reference alignment for rock-solid archival output.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Perf Stabilizer</p>
          <p class="desc">Sprocket-hole / perforation-based stabilisation for precise gate weave correction.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Litho Wash</p>
          <p class="desc">Create stylised lithographic and wash effects with strength, contrast, threshold, smoothness and custom shadow, highlight and wash colours.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Polarizer</p>
          <p class="desc">Simulate polarising-filter effects in post — suppress specular highlights and reflections, darken skies, boost saturation and reduce haze.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Video Inpaint Pro</p>
          <p class="desc">ProPainter-style video inpainting. Remove objects or fill damaged regions across an entire shot with strong temporal consistency.</p>
          <div class="priceRow">
            <div class="price">€150</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/150" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>

        <div class="card">
          <p class="name">Prefer the full suite?</p>
          <p class="desc">Unlock everything with one suite key.</p>
          <div class="priceRow">
            <div class="price">€1200</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/1200" target="_blank" rel="noreferrer">Buy Suite</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="software">
      <h2>Software</h2>
      <div class="grid">
        <div class="card">
          <p class="name">Video Kiosk</p>
          <p class="desc">Touchscreen video browser for exhibits and installations. Runs fullscreen on Windows 11, scans your Videos folder automatically, supports mouse and touch. Play, seek and control volume — no keyboard needed.</p>
          <div class="badges" style="margin:10px 0 0;">
            <span class="badge">Windows 11</span>
            <span class="badge alt">Touch &amp; Mouse</span>
            <span class="badge">Exhibit / Kiosk</span>
          </div>
          <div class="priceRow">
            <div class="price">€45</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/45" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>
        <div class="card">
          <img src="data:image/jpeg;base64,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r3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b/GqtFAFr7de/8/Ev/fbf40fbr3/n4l/77b/GqtFAFr7de/8APxL/AN9t/jR9uvf+fiX/AL7b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" alt="WaveScope — segmented peak meters, phase scope and video preview" style="width:100%;border-radius:10px;margin:0 0 12px;display:block;">
          <p class="name">WaveScope</p>
          <p class="desc">Audio/video analyser with segmented peak meters, goniometer-style phase scope and correlation metering. Scrub and 2&times; playback, mono-to-multichannel metering. For macOS, Windows and Linux.</p>
          <div class="badges" style="margin:10px 0 0;">
            <span class="badge">macOS</span>
            <span class="badge">Windows</span>
            <span class="badge">Linux</span>
            <span class="badge alt">Meters + Phase Scope</span>
          </div>
          <div class="priceRow">
            <div class="price">€10</div>
            <a class="btn primary" href="https://paypal.me/blakejones209/10" target="_blank" rel="noreferrer">Buy</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="mobile">
      <h2>Mobile Apps</h2>
      <div class="grid">
        <div class="card">
          <p class="name">Monitor Calibration App</p>
          <p class="desc">Turn your iPhone into a monitor calibration probe. Measure and tune display accuracy on the go.</p>
          <div class="badges" style="margin:10px 0 0;">
            <span class="badge">iOS</span>
            <span class="badge alt">iPhone</span>
          </div>
          <div class="priceRow">
            <div class="price">App Store</div>
            <a class="btn primary" href="https://apps.apple.com/us/app/monitor-calibrator/id6780020540" target="_blank" rel="noreferrer">Download</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="demo">
      <h2>Demo</h2>

      <p class="small">Example of the plugins in use (including Noise Reduction).</p>
      <div class="videoWrap" aria-label="Product demo video">
        <div style="position:relative;padding-top:56.25%;">
          <iframe
            src="https://www.youtube.com/embed/wAAc96TKLck"
            title="YouTube video player"
            style="position:absolute;inset:0;width:100%;height:100%;border:0;"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen>
          </iframe>
        </div>
      </div>
    </section>

    <section class="section" id="downloads">
      <h2>Downloads</h2>
      <ul class="list">
        <li><span class="dot"></span><span><a href="/downloads/CreativeRestoration-PluginBundle.dmg" download style="color:var(--accent2);text-decoration:underline;"><strong>Creative Restoration OFX Bundle — macOS DMG</strong></a></span></li>
        <li><span class="dot"></span><span><a href="/downloads/CreativeRestoration-Instructions.pdf" download style="color:var(--accent2);text-decoration:underline;"><strong>Installation, licensing &amp; usage instructions (PDF)</strong></a></span></li>
      </ul>
      <div class="divider"></div>
      <p class="small">
        The DMG contains the signed OFX plugin bundles plus install/uninstall scripts.
        The PDF explains how to install, request a license, and activate individual plugins or the full suite.
      </p>
    </section>

    <section class="section" id="how">
      <h2>How purchase &amp; delivery works</h2>

      <ul class="list">
        <li><span class="dot"></span><span><strong>Pay with PayPal</strong> using the buttons above.</span></li>
        <li><span class="dot"></span><span><strong>Delivery:</strong> after payment you will receive installation + licensing instructions and your license key.</span></li>
        <li><span class="dot"></span><span><strong>Platforms:</strong> macOS supported. <strong>Windows version available (beta) for all plugins.</strong></span></li>
        <li><span class="dot"></span><span><strong>Support:</strong> email <a href="mailto:info@cloudstudio.me"><u>info@cloudstudio.me</u></a> for questions.</span></li>
      <div class="divider"></div>
      <p class="small">
        Note: PayPal links open in a new tab. If you prefer an invoice or a different payment method, contact
        <a href="mailto:info@cloudstudio.me"><u>info@cloudstudio.me</u></a>.
      </p>
    </section>

   
    <footer>
      © <span id="y"></span> CloudStudio • Contact: <a href="mailto:info@cloudstudio.me"><u>info@cloudstudio.me</u></a>
    </footer>
  </div>

  <script>
    document.getElementById('y').textContent = new Date().getFullYear();
  </script>
</body>
</html>

