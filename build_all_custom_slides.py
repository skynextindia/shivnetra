import os

pages_dir = r'C:\Users\rohan\.gemini\antigravity-ide\scratch\shivnetra47_presentation\pages'

# Slide 01
p01 = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Page 01 - Indigenous Swarm UAV Development Program | SHIVNETRA47</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    .hero-layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 36px;
      height: 100%;
      align-items: stretch;
    }
    .hero-left {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }
    .program-badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      padding: 6px 14px;
      border-radius: 2px;
      font-family: var(--font-mono);
      font-size: 11px;
      letter-spacing: 1.5px;
      color: var(--sage);
      text-transform: uppercase;
      margin-bottom: 16px;
    }
    .hero-title {
      font-family: var(--font-heading);
      font-size: 44px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.12;
      letter-spacing: -0.5px;
      margin-bottom: 16px;
      text-transform: uppercase;
    }
    .hero-subtitle {
      font-family: var(--font-subheading);
      font-size: 19px;
      color: var(--text-secondary);
      font-weight: 500;
      letter-spacing: 0.2px;
      margin-bottom: 20px;
      line-height: 1.4;
    }
    .system-elements-box {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-left: 3px solid var(--olive-light);
      padding: 18px 22px;
      border-radius: 3px;
      margin-bottom: 18px;
    }
    .elements-title {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--sage);
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 6px;
    }
    .elements-text {
      font-family: var(--font-heading);
      font-size: 18px;
      font-weight: 600;
      color: #ffffff;
      line-height: 1.3;
    }
    .mission-focus-card {
      background: var(--bg-card);
      border: 1px solid var(--border-saffron);
      padding: 16px 20px;
      border-radius: 3px;
      display: flex;
      gap: 16px;
      align-items: center;
    }
    .mission-focus-tag {
      background: var(--saffron);
      color: #ffffff;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1px;
      padding: 6px 12px;
      border-radius: 2px;
      white-space: nowrap;
      text-transform: uppercase;
    }
    .mission-focus-desc {
      font-size: 14px;
      color: var(--text-secondary);
      line-height: 1.5;
    }
    .hero-right-visual {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .hero-img-box {
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #080d0a;
    }
    .hero-img-box img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      padding: 10px;
    }
    .hero-img-tag {
      position: absolute;
      bottom: 14px;
      left: 16px;
      background: rgba(11, 16, 13, 0.92);
      border: 1px solid var(--border-strong);
      padding: 5px 14px;
      border-radius: 2px;
      font-family: var(--font-mono);
      font-size: 11.5px;
      color: #ffffff;
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }
    .hero-stats-bar {
      background: var(--bg-surface);
      border-top: 1px solid var(--border-medium);
      padding: 14px 20px;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      text-align: center;
    }
    .stat-lbl {
      font-family: var(--font-mono);
      font-size: 10px;
      color: var(--sage);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .stat-val {
      font-family: var(--font-heading);
      font-size: 16px;
      font-weight: 700;
      color: #ffffff;
      margin-top: 3px;
    }
  </style>
</head>
<body>
  <div class="slide-canvas">
    <div class="corner-tr"></div>
    <div class="corner-bl"></div>

    <header class="slide-header">
      <div class="header-brand">
        <img src="../assets/logo_white.png" alt="SHIVNETRA 47" class="brand-logo-img">
        <div class="brand-divider"></div>
        <div class="brand-subtitle">
          <span class="brand-subtitle-main">Air Defence System Private Limited</span>
          <span class="brand-subtitle-sub">Defence Aerospace & Autonomous UAV Systems</span>
        </div>
      </div>
      <div class="header-meta">
        <div class="meta-tag classified">DEFENCE SENSITIVE</div>
        <div class="meta-tag">IAF MISSION STANDARD</div>
        <div class="tricolor-indicator">
          <div class="tricolor-saffron"></div>
          <div class="tricolor-white"></div>
          <div class="tricolor-green"></div>
        </div>
      </div>
    </header>

    <main class="slide-body">
      <div class="hero-layout">
        <div class="hero-left">
          <div>
            <div class="program-badge">
              <span>●</span> Sovereign Defense R&D • Make In India
            </div>
            <h1 class="hero-title">
              Indigenous Swarm UAV<br>
              Development Program
            </h1>
            <p class="hero-subtitle">
              Designed, flight-validated, and industrialized in-house with the BCN engineering team.
            </p>
          </div>

          <div class="system-elements-box">
            <div class="elements-title">Tactical Multi-Node Triad</div>
            <div class="elements-text">
              Nano-UAV Swarm Elements &nbsp;+&nbsp; Tactical Overwatch VTOL &nbsp;+&nbsp; Dual-Screen GCS
            </div>
          </div>

          <div>
            <div class="mission-focus-card">
              <div class="mission-focus-tag">Mission Focus</div>
              <div class="mission-focus-desc">
                Persistent tactical surveillance • distributed sensing • autonomous coordination
              </div>
            </div>
            <div style="font-family: var(--font-mono); font-size: 11.5px; color: var(--text-muted); margin-top: 14px;">
              Concept presentation | Based on the supplied reference specifications and budget framework
            </div>
          </div>
        </div>

        <div class="hero-right-visual">
          <div class="hero-img-box">
            <img src="../assets/overwatch_uav.jpg" alt="SHIVNETRA47 Tactical Overwatch UAV Platform">
            <div class="hero-img-tag">SHIVNETRA47 Tactical Overwatch UAV • IAF Roundel Livery</div>
          </div>

          <div class="hero-stats-bar">
            <div>
              <div class="stat-lbl">Configuration</div>
              <div class="stat-val">Twin-Boom VTOL</div>
            </div>
            <div>
              <div class="stat-lbl">Propulsion</div>
              <div class="stat-val">Hybrid 4+1 Electric</div>
            </div>
            <div>
              <div class="stat-lbl">Operational Role</div>
              <div class="stat-val">Swarm C2 Relay</div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <footer class="slide-footer">
      <div class="footer-left">
        <span>SHIVNETRA47 AIR DEFENCE SYSTEM PRIVATE LIMITED</span>
        <span class="footer-bullet">■</span>
        <span>PROGRAM ID: SN47-SWARM-SYS-2026</span>
      </div>
      <div class="footer-center">Indigenous Defence Aerospace Architecture</div>
      <div class="footer-right">
        <div class="slide-number">01 / 13</div>
      </div>
    </footer>
  </div>
</body>
</html>"""

# Slide 02 (6 Units)
p02 = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Page 02 - Indigenous Swarm UAV System (6 Units) | SHIVNETRA47</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    .brochure-layout {
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 36px;
      height: 100%;
      align-items: stretch;
    }
    .visual-spread {
      display: flex;
      flex-direction: column;
      gap: 16px;
      height: 100%;
    }
    .hero-photo-box {
      height: 310px;
      flex-shrink: 0;
      background: #080d0a;
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .hero-photo-box img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      padding: 6px;
    }
    .photo-tag {
      position: absolute;
      bottom: 10px;
      left: 12px;
      background: rgba(11, 16, 13, 0.92);
      border: 1px solid var(--border-strong);
      padding: 4px 12px;
      border-radius: 2px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: #ffffff;
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }
    .cad-schematic-box {
      height: 200px;
      flex-shrink: 0;
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 12px 20px;
    }
    .cad-schematic-box img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }
    .schematic-tag {
      position: absolute;
      top: 10px;
      left: 14px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--sand);
      letter-spacing: 1px;
      text-transform: uppercase;
    }
    .specs-table-card {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      padding: 14px 18px;
      flex: 1;
      display: flex;
      align-items: center;
    }
    .specs-2col-table {
      width: 100%;
      border-collapse: collapse;
      font-family: var(--font-mono);
      font-size: 12px;
    }
    .specs-2col-table td {
      padding: 4px 8px;
      border-bottom: 1px solid rgba(109, 142, 118, 0.1);
    }
    .specs-2col-table tr:last-child td { border-bottom: none; }
    .specs-2col-table .lbl { color: var(--text-muted); }
    .specs-2col-table .val { text-align: right; color: #ffffff; font-weight: 600; }

    .content-spread {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 18px;
      height: 100%;
    }
    .spread-header h2 {
      font-family: var(--font-heading);
      font-size: 28px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.15;
      text-transform: uppercase;
    }
    .spread-header p {
      font-family: var(--font-subheading);
      font-size: 15px;
      color: var(--sage);
      margin-top: 4px;
    }
    .triad-architecture-card {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      padding: 16px 20px;
    }
    .triad-title {
      font-family: var(--font-heading);
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 12px;
      padding-bottom: 6px;
      border-bottom: 1px solid var(--border-fine);
      display: flex;
      justify-content: space-between;
    }
    .triad-nodes-row {
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      gap: 16px;
      align-items: center;
      margin-bottom: 12px;
    }
    .node-item {
      background: var(--bg-surface);
      border: 1px solid var(--border-fine);
      border-radius: 3px;
      padding: 12px;
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .node-item img { height: 48px; max-width: 75px; object-fit: contain; }
    .node-item h5 {
      font-family: var(--font-heading);
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
      text-transform: uppercase;
    }
    .node-item p { font-family: var(--font-mono); font-size: 11px; color: var(--text-secondary); margin-top: 2px; }
    .mesh-link-indicator {
      text-align: center;
      font-family: var(--font-mono);
      font-size: 10px;
      color: var(--saffron-bright);
      font-weight: 700;
    }
    .nano-swarm-strip {
      background: var(--bg-surface);
      border: 1px solid var(--border-fine);
      border-radius: 3px;
      padding: 10px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .nano-swarm-left { display: flex; align-items: center; gap: 12px; }
    .nano-swarm-left img { height: 32px; object-fit: contain; }

    .conops-doctrine-card {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      padding: 16px 20px;
    }
    .conops-title {
      font-family: var(--font-heading);
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 10px;
      padding-bottom: 6px;
      border-bottom: 1px solid var(--border-fine);
    }
    .conops-step-row {
      display: flex;
      gap: 12px;
      align-items: flex-start;
      margin-bottom: 8px;
      font-size: 13px;
      color: var(--text-secondary);
      line-height: 1.45;
    }
    .conops-step-row:last-child { margin-bottom: 0; }
    .conops-num {
      width: 22px;
      height: 22px;
      background: var(--bg-elevated);
      border: 1px solid var(--border-medium);
      border-radius: 2px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono);
      font-size: 11.5px;
      font-weight: 700;
      color: var(--saffron-bright);
      flex-shrink: 0;
      margin-top: 1px;
    }
    .conops-step-row strong {
      color: #ffffff;
      font-family: var(--font-heading);
      font-size: 13.5px;
      text-transform: uppercase;
    }
    .caps-card {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      padding: 14px 20px;
    }
    .caps-title {
      font-family: var(--font-heading);
      font-size: 13px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 8px;
      padding-bottom: 4px;
      border-bottom: 1px solid var(--border-fine);
    }
    .caps-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px 14px;
    }
    .caps-entry {
      font-size: 12.5px;
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .caps-entry::before {
      content: '■';
      color: var(--olive-light);
      font-size: 8px;
    }
  </style>
</head>
<body>
  <div class="slide-canvas">
    <div class="corner-tr"></div>
    <div class="corner-bl"></div>

    <header class="slide-header">
      <div class="header-brand">
        <img src="../assets/logo_white.png" alt="SHIVNETRA 47" class="brand-logo-img">
        <div class="brand-divider"></div>
        <div class="brand-subtitle">
          <span class="brand-subtitle-main">Air Defence System Private Limited</span>
          <span class="brand-subtitle-sub">Tactical Reconnaissance & Multi-Node Fleet</span>
        </div>
      </div>
      <div class="header-meta">
        <div class="meta-tag">6-UNIT SWARM BASELINE</div>
        <div class="meta-tag classified">SYSTEM OVERVIEW</div>
        <div class="tricolor-indicator">
          <div class="tricolor-saffron"></div>
          <div class="tricolor-white"></div>
          <div class="tricolor-green"></div>
        </div>
      </div>
    </header>

    <main class="slide-body">
      <div class="brochure-layout">
        <div class="visual-spread">
          <div class="hero-photo-box">
            <img src="../assets/full_uncropped_sys6.png" alt="6-Unit Tactical System Overview">
            <div class="photo-tag">6-Unit Tactical Triad • Overwatch + Swarm + GCS</div>
          </div>

          <div class="cad-schematic-box">
            <img src="../assets/vtol_cad_clean_transparent.png" alt="Aerodynamic Line Drawing">
            <div class="schematic-tag">Airframe Engineering Wireframe • Hybrid VTOL</div>
          </div>

          <div class="specs-table-card">
            <table class="specs-2col-table">
              <tr>
                <td class="lbl">Overwatch Platform MTOW:</td>
                <td class="val">~20 kg</td>
                <td class="lbl" style="padding-left: 18px;">Nano-UAV Element MTOW:</td>
                <td class="val">350 – 450 g</td>
              </tr>
              <tr>
                <td class="lbl">Flight Endurance (Full Payload):</td>
                <td class="val">~20 min</td>
                <td class="lbl" style="padding-left: 18px;">Nano-UAV Sprint Endurance:</td>
                <td class="val">~8 min</td>
              </tr>
              <tr>
                <td class="lbl">Operational Coverage Range:</td>
                <td class="val">Up to 50 km</td>
                <td class="lbl" style="padding-left: 18px;">Swarm Reconnaissance Range:</td>
                <td class="val">250 – 500 m</td>
              </tr>
              <tr>
                <td class="lbl">Overwatch Service Ceiling:</td>
                <td class="val">8,000 ft AMSL</td>
                <td class="lbl" style="padding-left: 18px;">Operating Altitude (AGL):</td>
                <td class="val">~100 m AGL</td>
              </tr>
              <tr>
                <td class="lbl">Airborne Sensor Payload:</td>
                <td class="val">Dual EO / IR Gimbal</td>
                <td class="lbl" style="padding-left: 18px;">Modular Effector Capacity:</td>
                <td class="val">30 – 40 g class</td>
              </tr>
            </table>
          </div>
        </div>

        <div class="content-spread">
          <div class="spread-header">
            <h2>SHIVNETRA47 • Tactical Swarm UAV System</h2>
            <p>Indigenous Triad Architecture: Overwatch VTOL + Swarm Reconnaissance + Edge GCS</p>
          </div>

          <div class="triad-architecture-card">
            <div class="triad-title">
              <span>Operational Deployment Triad</span>
              <span style="font-family: var(--font-mono); font-size: 11px; color: var(--sage);">ENCRYPTED FREQ-HOPPING MESH</span>
            </div>

            <div class="triad-nodes-row">
              <div class="node-item">
                <img src="../assets/vtol_hero_isolated.png" alt="Overwatch UAV">
                <div>
                  <h5>Overwatch UAV</h5>
                  <p>Airborne Relay • 1 Unit</p>
                </div>
              </div>

              <div class="mesh-link-indicator">
                <div style="font-size: 18px;">📡</div>
                <div>SECURE<br>MESH</div>
              </div>

              <div class="node-item">
                <img src="../assets/original_gcs_tablet.png" alt="GCS Console">
                <div>
                  <h5>Ground Station</h5>
                  <p>Tactical Dual-Screen C2</p>
                </div>
              </div>
            </div>

            <div class="nano-swarm-strip">
              <div class="nano-swarm-left">
                <img src="../assets/nano_drone_clean_cutout.png" alt="Nano-UAV">
                <div>
                  <span style="font-family: var(--font-heading); font-size: 12.5px; font-weight: 700; color: #ffffff; text-transform: uppercase;">Nano-UAV Swarm Elements (6 Units)</span>
                  <span style="font-family: var(--font-mono); font-size: 10.5px; color: var(--sage); margin-left: 10px;">Coordinated Target Scouting • Area Saturation</span>
                </div>
              </div>
              <span style="font-family: var(--font-mono); font-size: 10.5px; color: var(--saffron-bright); font-weight: 700;">6-NODE MESH ACTIVE</span>
            </div>
          </div>

          <div class="conops-doctrine-card">
            <div class="conops-title">Operational Workflow</div>
            <div class="conops-step-row">
              <div class="conops-num">1</div>
              <div><strong>Deployment:</strong> Overwatch aircraft ascends with nano-UAV payload to loiter altitude.</div>
            </div>
            <div class="conops-step-row">
              <div class="conops-num">2</div>
              <div><strong>Swarm Release:</strong> Nano-UAV elements deployed over designated coordinates.</div>
            </div>
            <div class="conops-step-row">
              <div class="conops-num">3</div>
              <div><strong>Coordinated Mission:</strong> Autonomous distributed scanning; Overwatch acts as data bridge.</div>
            </div>
            <div class="conops-step-row">
              <div class="conops-num">4</div>
              <div><strong>Edge AI Fusion:</strong> Multi-sensor feeds processed at Ground Control Station in real time.</div>
            </div>
            <div class="conops-step-row">
              <div class="conops-num">5</div>
              <div><strong>Recovery:</strong> Automated return-to-base sequence with swift field turnaround.</div>
            </div>
          </div>

          <div class="caps-card">
            <div class="caps-title">Technical Capabilities</div>
            <div class="caps-grid">
              <div class="caps-entry">Autonomous Swarm Operations</div>
              <div class="caps-entry">Low Acoustic Signature</div>
              <div class="caps-entry">Real-Time Surveillance & ISR</div>
              <div class="caps-entry">Rapid Field Assembly</div>
              <div class="caps-entry">Edge AI Target Detection</div>
              <div class="caps-entry">Modular Effector Integration</div>
              <div class="caps-entry">Secure Anti-Jam Communication</div>
              <div class="caps-entry">100% Indigenous Architecture</div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <footer class="slide-footer">
      <div class="footer-left">
        <span>SHIVNETRA47 AIR DEFENCE SYSTEM PRIVATE LIMITED</span>
        <span class="footer-bullet">■</span>
        <span>100% INDIGENOUS SOVEREIGN ARCHITECTURE • MAKE IN INDIA</span>
      </div>
      <div class="footer-center">Vision. Intelligence. Dominance.</div>
      <div class="footer-right">
        <div class="slide-number">02 / 13</div>
      </div>
    </footer>
  </div>
</body>
</html>"""

# Slide 03 (24+ Units)
p03 = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Page 03 - Extended Range Swarm System (24+ Units) | SHIVNETRA47</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    .brochure-layout {
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 36px;
      height: 100%;
      align-items: stretch;
    }
    .visual-spread {
      display: flex;
      flex-direction: column;
      gap: 16px;
      height: 100%;
    }
    .hero-photo-box {
      height: 310px;
      flex-shrink: 0;
      background: #080d0a;
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .hero-photo-box img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      padding: 6px;
    }
    .photo-tag {
      position: absolute;
      bottom: 10px;
      left: 12px;
      background: rgba(11, 16, 13, 0.92);
      border: 1px solid var(--border-saffron);
      padding: 4px 12px;
      border-radius: 2px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--saffron-bright);
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }
    .cad-schematic-box {
      height: 200px;
      flex-shrink: 0;
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 8px;
    }
    .cad-schematic-box img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }
    .schematic-tag {
      position: absolute;
      top: 10px;
      left: 14px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--sand);
      letter-spacing: 1px;
      text-transform: uppercase;
    }
    .specs-table-card {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      padding: 14px 18px;
      flex: 1;
      display: flex;
      align-items: center;
    }
    .specs-2col-table {
      width: 100%;
      border-collapse: collapse;
      font-family: var(--font-mono);
      font-size: 12px;
    }
    .specs-2col-table td {
      padding: 4px 8px;
      border-bottom: 1px solid rgba(109, 142, 118, 0.1);
    }
    .specs-2col-table tr:last-child td { border-bottom: none; }
    .specs-2col-table .lbl { color: var(--text-muted); }
    .specs-2col-table .val { text-align: right; color: #ffffff; font-weight: 600; }

    .content-spread {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 18px;
      height: 100%;
    }
    .spread-header h2 {
      font-family: var(--font-heading);
      font-size: 28px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.15;
      text-transform: uppercase;
    }
    .spread-header p {
      font-family: var(--font-subheading);
      font-size: 15px;
      color: var(--sage);
      margin-top: 4px;
    }
    .triad-architecture-card {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      padding: 16px 20px;
    }
    .triad-title {
      font-family: var(--font-heading);
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 12px;
      padding-bottom: 6px;
      border-bottom: 1px solid var(--border-fine);
      display: flex;
      justify-content: space-between;
    }
    .triad-nodes-row {
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      gap: 16px;
      align-items: center;
      margin-bottom: 12px;
    }
    .node-item {
      background: var(--bg-surface);
      border: 1px solid var(--border-fine);
      border-radius: 3px;
      padding: 12px;
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .node-item img { height: 48px; max-width: 75px; object-fit: contain; }
    .node-item h5 {
      font-family: var(--font-heading);
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
      text-transform: uppercase;
    }
    .node-item p { font-family: var(--font-mono); font-size: 11px; color: var(--text-secondary); margin-top: 2px; }
    .mesh-link-indicator {
      text-align: center;
      font-family: var(--font-mono);
      font-size: 10px;
      color: var(--saffron-bright);
      font-weight: 700;
    }
    .nano-swarm-strip {
      background: var(--bg-surface);
      border: 1px solid var(--border-fine);
      border-radius: 3px;
      padding: 10px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .nano-swarm-left { display: flex; align-items: center; gap: 12px; }
    .nano-swarm-left img { height: 32px; object-fit: contain; }

    .conops-doctrine-card {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      padding: 16px 20px;
    }
    .conops-title {
      font-family: var(--font-heading);
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 10px;
      padding-bottom: 6px;
      border-bottom: 1px solid var(--border-fine);
    }
    .conops-step-row {
      display: flex;
      gap: 12px;
      align-items: flex-start;
      margin-bottom: 8px;
      font-size: 13px;
      color: var(--text-secondary);
      line-height: 1.45;
    }
    .conops-step-row:last-child { margin-bottom: 0; }
    .conops-num {
      width: 22px;
      height: 22px;
      background: var(--bg-elevated);
      border: 1px solid var(--border-medium);
      border-radius: 2px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono);
      font-size: 11.5px;
      font-weight: 700;
      color: var(--saffron-bright);
      flex-shrink: 0;
      margin-top: 1px;
    }
    .conops-step-row strong {
      color: #ffffff;
      font-family: var(--font-heading);
      font-size: 13.5px;
      text-transform: uppercase;
    }
    .caps-card {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      padding: 14px 20px;
    }
    .caps-title {
      font-family: var(--font-heading);
      font-size: 13px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 8px;
      padding-bottom: 4px;
      border-bottom: 1px solid var(--border-fine);
    }
    .caps-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px 14px;
    }
    .caps-entry {
      font-size: 12.5px;
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .caps-entry::before {
      content: '■';
      color: var(--saffron);
      font-size: 8px;
    }
  </style>
</head>
<body>
  <div class="slide-canvas">
    <div class="corner-tr"></div>
    <div class="corner-bl"></div>

    <header class="slide-header">
      <div class="header-brand">
        <img src="../assets/logo_white.png" alt="SHIVNETRA 47" class="brand-logo-img">
        <div class="brand-divider"></div>
        <div class="brand-subtitle">
          <span class="brand-subtitle-main">Air Defence System Private Limited</span>
          <span class="brand-subtitle-sub">Extended Range Swarm System (24+ Multi-Node Fleet)</span>
        </div>
      </div>
      <div class="header-meta">
        <div class="meta-tag">24+ UNIT SWARM FLEET</div>
        <div class="meta-tag classified">THEATER INTEGRATION</div>
        <div class="tricolor-indicator">
          <div class="tricolor-saffron"></div>
          <div class="tricolor-white"></div>
          <div class="tricolor-green"></div>
        </div>
      </div>
    </header>

    <main class="slide-body">
      <div class="brochure-layout">
        <div class="visual-spread">
          <div class="hero-photo-box">
            <img src="../assets/full_uncropped_sys24.png" alt="24-Unit Extended Swarm System Overview">
            <div class="photo-tag">Theater Architecture • 24+ Unit Extended Fleet</div>
          </div>

          <div class="cad-schematic-box">
            <img src="../assets/gcs_console.jpg" alt="Ground Control Station Console">
            <div class="schematic-tag">Tactical GCS Console • Dual-Display Mission Command</div>
          </div>

          <div class="specs-table-card">
            <table class="specs-2col-table">
              <tr>
                <td class="lbl">Overwatch Platform MTOW:</td>
                <td class="val">~20 kg</td>
                <td class="lbl" style="padding-left: 18px;">Nano-UAV Fleet Size:</td>
                <td class="val">24+ Units</td>
              </tr>
              <tr>
                <td class="lbl">Overwatch Endurance (Loiter):</td>
                <td class="val">~120 min</td>
                <td class="lbl" style="padding-left: 18px;">Nano-UAV Endurance:</td>
                <td class="val">60 – 90 min</td>
              </tr>
              <tr>
                <td class="lbl">Operational Stand-Off Range:</td>
                <td class="val">Up to 100 km</td>
                <td class="lbl" style="padding-left: 18px;">Swarm Mesh Network:</td>
                <td class="val">Frequency Hopping</td>
              </tr>
              <tr>
                <td class="lbl">Service Ceiling (AMSL):</td>
                <td class="val">8,000 ft AMSL</td>
                <td class="lbl" style="padding-left: 18px;">Swarm Penetration Range:</td>
                <td class="val">25 – 50 km</td>
              </tr>
              <tr>
                <td class="lbl">Airborne Sensor Suite:</td>
                <td class="val">EO / IR Multi-Sensor</td>
                <td class="lbl" style="padding-left: 18px;">Swarm Effector Payload:</td>
                <td class="val">30 – 40 g class</td>
              </tr>
            </table>
          </div>
        </div>

        <div class="content-spread">
          <div class="spread-header">
            <h2>SHIVNETRA47 • Extended Range Swarm System</h2>
            <p>Theater-Scale Multi-Node Swarm with Multi-Hop Anti-Jamming Datalink</p>
          </div>

          <div class="triad-architecture-card">
            <div class="triad-title">
              <span>Theater-Scale Architecture (24+ UAVs)</span>
              <span style="font-family: var(--font-mono); font-size: 11px; color: var(--saffron-bright);">ANTI-JAMMING FHSS PROTOCOL</span>
            </div>

            <div class="triad-nodes-row">
              <div class="node-item">
                <img src="../assets/vtol_hero_isolated.png" alt="Overwatch UAV">
                <div>
                  <h5>Overwatch UAV</h5>
                  <p>120 Min Loiter • 100 km</p>
                </div>
              </div>

              <div class="mesh-link-indicator">
                <div style="font-size: 18px;">🛰</div>
                <div>MULTI-HOP<br>FHSS</div>
              </div>

              <div class="node-item">
                <img src="../assets/original_gcs_tablet.png" alt="Tactical GCS">
                <div>
                  <h5>Tactical GCS</h5>
                  <p>Multi-Swarm C2 Console</p>
                </div>
              </div>
            </div>

            <div class="nano-swarm-strip">
              <div class="nano-swarm-left">
                <img src="../assets/nano_drone_clean_cutout.png" alt="Nano-UAV Fleet">
                <div>
                  <span style="font-family: var(--font-heading); font-size: 12.5px; font-weight: 700; color: #ffffff; text-transform: uppercase;">Nano-UAV Fleet (24+ Multi-Node Elements)</span>
                  <span style="font-family: var(--font-mono); font-size: 10.5px; color: var(--sage); margin-left: 10px;">Persistent Theater Saturation • Multi-Vector Loiter</span>
                </div>
              </div>
              <span style="font-family: var(--font-mono); font-size: 10.5px; color: var(--saffron-bright); font-weight: 700;">SELF-HEALING MESH</span>
            </div>
          </div>

          <div class="conops-doctrine-card">
            <div class="conops-title">Extended Fleet Doctrine</div>
            <div class="conops-step-row">
              <div class="conops-num">1</div>
              <div><strong>Staggered Launch:</strong> 24+ nano-units launched in coordinated waves across multiple sectors.</div>
            </div>
            <div class="conops-step-row">
              <div class="conops-num">2</div>
              <div><strong>Multi-Hop Daisy Chaining:</strong> Autonomous node routing relays signals beyond terrain obstructions.</div>
            </div>
            <div class="conops-step-row">
              <div class="conops-num">3</div>
              <div><strong>Continuous Target Tracking:</strong> Sensor elements dynamically cycle on-station for 24/7 coverage.</div>
            </div>
            <div class="conops-step-row">
              <div class="conops-num">4</div>
              <div><strong>Direct C2 Downlink:</strong> Prioritized high-value target telemetry downlinked directly to field commanders.</div>
            </div>
            <div class="conops-step-row">
              <div class="conops-num">5</div>
              <div><strong>Automated Staged Retrieval:</strong> Automated return-to-base with rapid turnaround recharging units.</div>
            </div>
          </div>

          <div class="caps-card">
            <div class="caps-title">Extended Fleet Capabilities</div>
            <div class="caps-grid">
              <div class="caps-entry">Saturated Swarm C2</div>
              <div class="caps-entry">Self-Healing RF Mesh</div>
              <div class="caps-entry">Persistent 120 Min Loiter</div>
              <div class="caps-entry">Rapid Field Turnaround</div>
              <div class="caps-entry">Edge Multi-Target Tracking</div>
              <div class="caps-entry">Modular Effector Integration</div>
              <div class="caps-entry">Anti-Jam Frequency Hopping</div>
              <div class="caps-entry">100% Indigenous Architecture</div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <footer class="slide-footer">
      <div class="footer-left">
        <span>SHIVNETRA47 AIR DEFENCE SYSTEM PRIVATE LIMITED</span>
        <span class="footer-bullet">■</span>
        <span>100% INDIGENOUS SOVEREIGN ARCHITECTURE • MAKE IN INDIA</span>
      </div>
      <div class="footer-center">Vision. Intelligence. Dominance.</div>
      <div class="footer-right">
        <div class="slide-number">03 / 13</div>
      </div>
    </footer>
  </div>
</body>
</html>"""

# Slide 06 (Nano-UAV)
p06 = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Page 06 - Nano-UAV Swarm Element Technical Specification | SHIVNETRA47</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    .specs-grid-layout {
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 36px;
      height: 100%;
      align-items: stretch;
    }
    .left-datasheet {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
      height: 100%;
    }
    .spec-cards-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }
    .spec-metric-card {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      padding: 16px 20px;
      position: relative;
    }
    .spec-metric-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 3px;
      height: 100%;
      background: var(--olive-light);
    }
    .spec-metric-card.highlight::before { background: var(--saffron); }
    .card-label {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--sage);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 6px;
    }
    .card-value {
      font-family: var(--font-heading);
      font-size: 28px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.1;
    }
    .doctrine-box {
      background: var(--bg-card);
      border: 1px solid var(--border-saffron);
      border-left: 3px solid var(--saffron);
      padding: 16px 20px;
      border-radius: 4px;
    }
    .doctrine-title {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--saffron-bright);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 6px;
    }
    .doctrine-text {
      font-size: 13.5px;
      color: var(--text-secondary);
      line-height: 1.5;
    }
    .showcase-panel {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
      position: relative;
    }
    .drone-main-view {
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #080d0a;
    }
    .drone-main-view img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      padding: 16px;
    }
    .callout-overlay {
      position: absolute;
      bottom: 14px;
      left: 16px;
      background: rgba(11, 16, 13, 0.92);
      border: 1px solid var(--border-medium);
      padding: 6px 14px;
      border-radius: 2px;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .callout-tag {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }
    .specs-ribbon {
      background: var(--bg-surface);
      border-top: 1px solid var(--border-medium);
      padding: 14px 20px;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      text-align: center;
    }
    .ribbon-lbl {
      font-family: var(--font-mono);
      font-size: 10px;
      color: var(--sage);
      text-transform: uppercase;
    }
    .ribbon-val {
      font-family: var(--font-heading);
      font-size: 15px;
      font-weight: 700;
      color: #ffffff;
      margin-top: 3px;
    }
  </style>
</head>
<body>
  <div class="slide-canvas">
    <div class="corner-tr"></div>
    <div class="corner-bl"></div>

    <header class="slide-header">
      <div class="header-brand">
        <img src="../assets/logo_white.png" alt="SHIVNETRA 47" class="brand-logo-img">
        <div class="brand-divider"></div>
        <div class="brand-subtitle">
          <span class="brand-subtitle-main">Nano-UAV Technical Specifications</span>
          <span class="brand-subtitle-sub">Tactical Micro Reconnaissance Swarm Node</span>
        </div>
      </div>
      <div class="header-meta">
        <div class="meta-tag classified">MIL-SPEC DATASHEET</div>
        <div class="meta-tag">SWARM TACTICAL NODE</div>
        <div class="tricolor-indicator">
          <div class="tricolor-saffron"></div>
          <div class="tricolor-white"></div>
          <div class="tricolor-green"></div>
        </div>
      </div>
    </header>

    <main class="slide-body">
      <div class="specs-grid-layout">
        <div class="left-datasheet">
          <div class="page-title-row">
            <div class="page-category">Platform Technical Specification</div>
            <h1 class="page-title">3. Nano-UAV — Swarm Element</h1>
            <div class="page-subtitle">Reference performance envelope from the supplied document</div>
          </div>

          <div class="spec-cards-grid">
            <div class="spec-metric-card">
              <div class="card-label">Maximum Take-Off Weight (MTOW)</div>
              <div class="card-value">350 – 450 g</div>
            </div>
            <div class="spec-metric-card highlight">
              <div class="card-label">Modular Payload Capacity</div>
              <div class="card-value">30 – 40 g class*</div>
            </div>
            <div class="spec-metric-card">
              <div class="card-label">Flight Endurance</div>
              <div class="card-value">~8 min</div>
            </div>
            <div class="spec-metric-card">
              <div class="card-label">Operating Altitude (AGL)</div>
              <div class="card-value">~100 m AGL</div>
            </div>
            <div class="spec-metric-card">
              <div class="card-label">Range / Station Distance</div>
              <div class="card-value">250 – 300 m</div>
            </div>
            <div class="spec-metric-card">
              <div class="card-label">Service Ceiling (AMSL)</div>
              <div class="card-value">8,000 ft AMSL</div>
            </div>
            <div class="spec-metric-card">
              <div class="card-label">Maximum Airspeed</div>
              <div class="card-value">~10 m/s</div>
            </div>
            <div class="spec-metric-card highlight">
              <div class="card-label">Swarm Deployment Size</div>
              <div class="card-value">6 to 24+ Units</div>
            </div>
          </div>

          <div class="doctrine-box">
            <div class="doctrine-title">Swarm Role</div>
            <div class="doctrine-text">
              Fast deployment • distributed sensing • cooperative mission execution • replaceable attrition units
            </div>
          </div>

          <div style="font-family: var(--font-mono); font-size: 10.5px; color: var(--text-muted);">
            * Payload wording is retained at high level; final payload definition is subject to design freeze, safety review and applicable approvals.
          </div>
        </div>

        <div class="showcase-panel">
          <div class="drone-main-view">
            <img src="../assets/nano_uav.jpg" alt="SHIVNETRA47 Nano-UAV Element">
            <div class="callout-overlay">
              <div class="callout-tag">SHIVNETRA47 Nano-UAV Element</div>
              <span style="font-family: var(--font-mono); font-size: 11px; color: var(--sage);">AUTHENTIC HARDWARE</span>
            </div>
          </div>

          <div class="specs-ribbon">
            <div>
              <div class="ribbon-lbl">Airframe</div>
              <div class="ribbon-val">Micro Quadcopter</div>
            </div>
            <div>
              <div class="ribbon-lbl">Datalink</div>
              <div class="ribbon-val">Anti-Jam Mesh</div>
            </div>
            <div>
              <div class="ribbon-lbl">Sensor</div>
              <div class="ribbon-val">Micro EO / IR</div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <footer class="slide-footer">
      <div class="footer-left">
        <span>SHIVNETRA47 AIR DEFENCE SYSTEM PRIVATE LIMITED</span>
        <span class="footer-bullet">■</span>
        <span>BCN IN-HOUSE ENGINEERING TEAM</span>
      </div>
      <div class="footer-center">Section 03 : Nano-UAV Swarm Element</div>
      <div class="footer-right">
        <div class="slide-number">06 / 13</div>
      </div>
    </footer>
  </div>
</body>
</html>"""

# Slide 07 (Overwatch UAV)
p07 = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Page 07 - Tactical Overwatch UAV Technical Specification | SHIVNETRA47</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    .specs-grid-layout {
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 36px;
      height: 100%;
      align-items: stretch;
    }
    .left-datasheet {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
      height: 100%;
    }
    .key-metrics-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
    }
    .metric-badge {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 3px;
      padding: 14px 12px;
      text-align: center;
      position: relative;
    }
    .metric-badge::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 2px;
      background: var(--olive-light);
    }
    .metric-badge.saffron::before { background: var(--saffron); }
    .mb-val {
      font-family: var(--font-heading);
      font-size: 28px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.1;
    }
    .mb-val.saffron { color: var(--saffron-bright); }
    .mb-lbl {
      font-family: var(--font-mono);
      font-size: 10px;
      color: var(--sage);
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-top: 4px;
    }

    .specs-table-card {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      padding: 16px 20px;
    }
    .specs-title {
      font-family: var(--font-heading);
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 10px;
      padding-bottom: 6px;
      border-bottom: 1px solid var(--border-fine);
      display: flex;
      justify-content: space-between;
    }
    .tech-table {
      width: 100%;
      border-collapse: collapse;
      font-family: var(--font-mono);
      font-size: 11.5px;
    }
    .tech-table td {
      padding: 6px 4px;
      border-bottom: 1px solid rgba(109, 142, 118, 0.1);
    }
    .tech-table tr:last-child td { border-bottom: none; }
    .tech-table .lbl { color: var(--text-muted); }
    .tech-table .val { text-align: right; color: #ffffff; font-weight: 600; }

    .roles-card {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      padding: 16px 20px;
    }
    .roles-title {
      font-family: var(--font-heading);
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 10px;
      padding-bottom: 6px;
      border-bottom: 1px solid var(--border-fine);
    }
    .roles-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .roles-list li {
      font-size: 13px;
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .roles-list li::before {
      content: '■';
      color: var(--olive-light);
      font-size: 8px;
    }

    .right-visual-spread {
      display: flex;
      flex-direction: column;
      gap: 16px;
      height: 100%;
    }
    .visual-flight-box {
      flex: 1.35;
      background: #080d0a;
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .visual-flight-box img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      background: #080d0a;
    }
    .visual-flight-tag {
      position: absolute;
      bottom: 12px;
      left: 14px;
      background: rgba(11, 16, 13, 0.92);
      border: 1px solid var(--border-strong);
      padding: 4px 10px;
      border-radius: 2px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: #ffffff;
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }
    .visual-cad-box {
      flex: 0.85;
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 12px 20px;
    }
    .visual-cad-box img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }
    .cad-blueprint-tag {
      position: absolute;
      top: 10px;
      left: 14px;
      font-family: var(--font-mono);
      font-size: 10.5px;
      color: var(--sand);
      letter-spacing: 1px;
      text-transform: uppercase;
    }
  </style>
</head>
<body>
  <div class="slide-canvas">
    <div class="corner-tr"></div>
    <div class="corner-bl"></div>

    <header class="slide-header">
      <div class="header-brand">
        <img src="../assets/logo_white.png" alt="SHIVNETRA 47" class="brand-logo-img">
        <div class="brand-divider"></div>
        <div class="brand-subtitle">
          <span class="brand-subtitle-main">Tactical Overwatch UAV Platform</span>
          <span class="brand-subtitle-sub">Medium-Altitude Airborne C2 & Sensor Relay</span>
        </div>
      </div>
      <div class="header-meta">
        <div class="meta-tag classified">AIRBORNE RELAY TIER</div>
        <div class="meta-tag">IAF INTEGRATION READY</div>
        <div class="tricolor-indicator">
          <div class="tricolor-saffron"></div>
          <div class="tricolor-white"></div>
          <div class="tricolor-green"></div>
        </div>
      </div>
    </header>

    <main class="slide-body">
      <div class="specs-grid-layout">
        <div class="left-datasheet">
          <div class="page-title-row">
            <div class="page-category">Platform Technical Specification</div>
            <h1 class="page-title">4. Overwatch UAV</h1>
            <div class="page-subtitle">The higher-endurance platform provides observation, coordination and mission support</div>
          </div>

          <div class="key-metrics-row">
            <div class="metric-badge">
              <div class="mb-val">~20 kg</div>
              <div class="mb-lbl">MTOW</div>
            </div>
            <div class="metric-badge saffron">
              <div class="mb-val saffron">~20 min</div>
              <div class="mb-lbl">Full-Payload Endurance</div>
            </div>
            <div class="metric-badge">
              <div class="mb-val">Up to 500 m</div>
              <div class="mb-lbl">Station Distance</div>
            </div>
            <div class="metric-badge">
              <div class="mb-val">~300 m AGL</div>
              <div class="mb-lbl">Operating Altitude</div>
            </div>
          </div>

          <div class="roles-card">
            <div class="roles-title">Primary Functions</div>
            <ul class="roles-list">
              <li>EO/IR sensor carriage</li>
              <li>Persistent overwatch of the swarm area</li>
              <li>Communications / coordination support</li>
              <li>Mission-level situational awareness</li>
              <li>Higher-capacity platform for system expansion</li>
            </ul>
          </div>

          <div class="specs-table-card">
            <div class="specs-title">
              <span>Design Principle</span>
              <span style="font-family: var(--font-mono); font-size: 11px; color: var(--sage);">COMMON ARCHITECTURE</span>
            </div>
            <p style="font-size: 13.5px; color: var(--text-secondary); line-height: 1.5;">
              The overwatch aircraft is developed as part of the same system architecture so the GCS, communications, mission software and operator workflow remain common across the fleet.
            </p>
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--saffron-bright); margin-top: 8px;">
              Maximum speed: TBC at design freeze | Service ceiling: 8,000 ft AMSL
            </div>
          </div>
        </div>

        <div class="right-visual-spread">
          <div class="visual-flight-box">
            <img src="../assets/real_flight_vtol_clean.png" alt="SHIVNETRA47 Flight Test Aircraft">
            <div class="visual-flight-tag">Flight Validated Airframe • In Flight</div>
          </div>

          <div class="visual-cad-box">
            <img src="../assets/vtol_cad_sand_lines.png" alt="Aerodynamic CAD Blueprint">
            <div class="cad-blueprint-tag">Aerodynamic CAD Schematic • SORA Compliant</div>
          </div>
        </div>
      </div>
    </main>

    <footer class="slide-footer">
      <div class="footer-left">
        <span>SHIVNETRA47 AIR DEFENCE SYSTEM PRIVATE LIMITED</span>
        <span class="footer-bullet">■</span>
        <span>BCN IN-HOUSE ENGINEERING TEAM</span>
      </div>
      <div class="footer-center">Section 04 : Tactical Overwatch UAV</div>
      <div class="footer-right">
        <div class="slide-number">07 / 13</div>
      </div>
    </footer>
  </div>
</body>
</html>"""

# Slide 09 (Engineering Workstreams)
p09 = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Page 09 - Engineering Workstreams | SHIVNETRA47</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    .workstreams-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-bottom: 24px;
    }
    .workstream-card {
      background: var(--bg-card);
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      padding: 22px 20px;
      position: relative;
      display: flex;
      flex-direction: column;
    }
    .workstream-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: var(--olive-light);
    }
    .workstream-card.highlight::before { background: var(--saffron); }
    .ws-idx {
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 700;
      color: var(--saffron-bright);
      margin-bottom: 6px;
    }
    .ws-title {
      font-family: var(--font-heading);
      font-size: 20px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-bottom: 10px;
      padding-bottom: 6px;
      border-bottom: 1px solid var(--border-fine);
    }
    .ws-desc {
      font-size: 14px;
      color: var(--text-secondary);
      line-height: 1.5;
      flex: 1;
    }
    .tarmac-hero-banner {
      background: #080d0a;
      border: 1px solid var(--border-medium);
      border-radius: 4px;
      overflow: hidden;
      position: relative;
      height: 180px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .tarmac-hero-banner img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .tarmac-tag {
      position: absolute;
      bottom: 12px;
      left: 16px;
      background: rgba(11, 16, 13, 0.92);
      border: 1px solid var(--border-strong);
      padding: 4px 12px;
      border-radius: 2px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: #ffffff;
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }
  </style>
</head>
<body>
  <div class="slide-canvas">
    <div class="corner-tr"></div>
    <div class="corner-bl"></div>

    <header class="slide-header">
      <div class="header-brand">
        <img src="../assets/logo_white.png" alt="SHIVNETRA 47" class="brand-logo-img">
        <div class="brand-divider"></div>
        <div class="brand-subtitle">
          <span class="brand-subtitle-main">Air Defence System Private Limited</span>
          <span class="brand-subtitle-sub">Parallel Development Packages</span>
        </div>
      </div>
      <div class="header-meta">
        <div class="meta-tag classified">SECTION 6.0</div>
        <div class="meta-tag">6 WORK PACKAGES</div>
        <div class="tricolor-indicator">
          <div class="tricolor-saffron"></div>
          <div class="tricolor-white"></div>
          <div class="tricolor-green"></div>
        </div>
      </div>
    </header>

    <main class="slide-body">
      <div class="page-title-row">
        <div class="page-category">Engineering Leadership</div>
        <h1 class="page-title">6. Engineering Workstreams</h1>
        <div class="page-subtitle">Parallel work packages compress the development cycle</div>
      </div>

      <div class="workstreams-grid">
        <div class="workstream-card">
          <div class="ws-idx">01</div>
          <div class="ws-title">System Engineering</div>
          <div class="ws-desc">Requirements, architecture, interfaces, configuration baseline.</div>
        </div>

        <div class="workstream-card highlight">
          <div class="ws-idx">02</div>
          <div class="ws-title">Air Vehicle</div>
          <div class="ws-desc">Nano-UAV and overwatch airframes, propulsion, power and avionics.</div>
        </div>

        <div class="workstream-card">
          <div class="ws-idx">03</div>
          <div class="ws-title">Autonomy</div>
          <div class="ws-desc">Mission logic, swarm coordination, navigation and operator controls.</div>
        </div>

        <div class="workstream-card">
          <div class="ws-idx">04</div>
          <div class="ws-title">Sensing</div>
          <div class="ws-desc">EO/IR and other approved sensing interfaces; edge processing.</div>
        </div>

        <div class="workstream-card">
          <div class="ws-idx">05</div>
          <div class="ws-title">GCS</div>
          <div class="ws-desc">Ground station, tablet workflow, telemetry, mission planning and monitoring.</div>
        </div>

        <div class="workstream-card highlight">
          <div class="ws-idx">06</div>
          <div class="ws-title">Test & Qualification</div>
          <div class="ws-desc">Bench tests, flight trials, reliability, safety and acceptance evidence.</div>
        </div>
      </div>

      <div class="tarmac-hero-banner">
        <img src="../assets/military_tarmac_uav.png" alt="Aerospace Industrial Test Facility">
        <div class="tarmac-tag">Airfield Flight-Line Integration & Environmental Qualification Base</div>
      </div>
    </main>

    <footer class="slide-footer">
      <div class="footer-left">
        <span>SHIVNETRA47 AIR DEFENCE SYSTEM PRIVATE LIMITED</span>
        <span class="footer-bullet">■</span>
        <span>BCN IN-HOUSE ENGINEERING TEAM</span>
      </div>
      <div class="footer-center">Section 06 : Engineering Workstreams</div>
      <div class="footer-right">
        <div class="slide-number">09 / 13</div>
      </div>
    </footer>
  </div>
</body>
</html>"""

for fname, content in [
    ('page_01.html', p01),
    ('page_02.html', p02),
    ('page_03.html', p03),
    ('page_06.html', p06),
    ('page_07.html', p07),
    ('page_09.html', p09)
]:
    with open(os.path.join(pages_dir, fname), 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Wrote custom design for {fname}')

print('All custom design slides generated successfully!')
