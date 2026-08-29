'use client';

import React, { useState, useEffect, useRef } from 'react';

export default function MaintenancePage() {
  const [progress, setProgress] = useState(85);
  const [telemetry, setTelemetry] = useState({
    alt: '1,420 m',
    lat: '28°36\'44"N',
    lon: '77°12\'22"E',
    pitch: '+02.4°',
    roll: '-00.8°',
    targetsLocked: 3,
    signal: '99.4%',
  });
  const canvasRef = useRef(null);

  // Dynamic Progress bar micro-pulse and telemetry updates
  useEffect(() => {
    const progressTimer = setInterval(() => {
      setProgress((prev) => {
        const delta = (Math.random() * 0.4 - 0.18);
        return Math.min(88.4, Math.max(84.8, +(prev + delta).toFixed(1)));
      });
    }, 1800);

    const telemetryTimer = setInterval(() => {
      setTelemetry({
        alt: `${(1415 + Math.floor(Math.random() * 12)).toLocaleString()} m`,
        lat: `28°36'${(40 + Math.floor(Math.random() * 8))}."N`,
        lon: `77°12'${(20 + Math.floor(Math.random() * 8))}."E`,
        pitch: `${(Math.random() > 0.5 ? '+' : '-')}${String((Math.random() * 3).toFixed(1)).padStart(4, '0')}°`,
        roll: `${(Math.random() > 0.5 ? '+' : '-')}${String((Math.random() * 2).toFixed(1)).padStart(4, '0')}°`,
        targetsLocked: 3 + (Math.random() > 0.7 ? 1 : 0),
        signal: `${(98.5 + Math.random() * 1.4).toFixed(1)}%`,
      });
    }, 1200);

    return () => {
      clearInterval(progressTimer);
      clearInterval(telemetryTimer);
    };
  }, []);

  // Drone POV Canvas Simulation: Terrain Grid, Radar Sweep, and Technical Target Acquisition Box
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let animationFrameId;
    let scanAngle = 0;
    let gridOffset = 0;

    // Ground Armored & Tactical Vehicle Targets (Real Scale ~10-18m footprint at 2000ft altitude)
    const targets = [
      { x: 0.28, y: 0.35, id: 'TGT-ALPHA-01', type: 'BMP-2 / APC', lock: true, w: 14, h: 22 },
      { x: 0.74, y: 0.62, id: 'TGT-BRAVO-04', type: 'RADAR-TELAR', lock: true, w: 16, h: 26 },
      { x: 0.42, y: 0.72, id: 'TGT-GCS-09', type: 'T-90S BHISHMA', lock: false, w: 15, h: 24 },
      { x: 0.61, y: 0.22, id: 'TGT-DELTA-11', type: 'SAM BATTERY', lock: true, w: 18, h: 20 },
    ];

    // Real War-Condition Combat Fighter Sorties (True Physical Scale at 2000ft AGL Sensor Swath)
    // Su-30MKI: Length ~21.9m, Wingspan ~14.7m (~42px screen scale)
    // Rafale: Length ~15.3m, Wingspan ~10.9m (~34px screen scale)
    // Supersonic intercept speed: ~8.5 to 13.5 px/frame relative speed
    const jets = [
      {
        callsign: 'GARUDA-01 [SU-30MKI]',
        img: su30Img,
        x: -300,
        y: 200,
        speed: 10.5,
        angle: 0.24,
        altitude: '2,000 FT AGL // LOW-LEVEL INTERCEPT',
        mach: 'MACH 1.45 (1,110 KTS)',
        weapons: 'ASTRA-MK2 / BRAHMOS-A',
        trail: [],
        color: '#38bdf8',
        locked: true,
        size: 42,
      },
      {
        callsign: 'GOLDEN-ARROWS-03 [RAFALE DH]',
        img: rafaleImg,
        x: -250,
        y: 520,
        speed: 12.8,
        angle: -0.16,
        altitude: '2,400 FT AGL // STRIKE SWEEP',
        mach: 'MACH 1.62 (1,240 KTS)',
        weapons: 'METEOR / SCALP-EG',
        trail: [],
        color: '#10b981',
        locked: true,
        size: 35,
      },
      {
        callsign: 'THUNDERBOLT-02 [SU-30MKI]',
        img: su30Img,
        x: 200,
        y: -300,
        speed: 9.2,
        angle: 0.92,
        altitude: '1,800 FT AGL // COMBAT AIR PATROL',
        mach: 'MACH 1.30 (995 KTS)',
        weapons: 'R-77 / R-73 WVR',
        trail: [],
        color: '#f59e0b',
        locked: false,
        size: 42,
      }
    ];

    const resize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };
    resize();
    window.addEventListener('resize', resize);

    const drawFighterJet = (ctx, jet) => {
      ctx.save();
      ctx.translate(jet.x, jet.y);
      // Sprite orientation adjustment (facing up by default -> rotate + 90deg)
      ctx.rotate(jet.angle + Math.PI / 2);

      // 1. Realistic Supersonic Afterburner Shock Diamond Exhaust Flame
      const flameLen = 16 + Math.random() * 8;
      const flameWidth = jet.size * 0.22;
      
      const flameGrad = ctx.createLinearGradient(0, jet.size * 0.44, 0, jet.size * 0.44 + flameLen);
      flameGrad.addColorStop(0, '#ffffff');
      flameGrad.addColorStop(0.2, '#f59e0b');
      flameGrad.addColorStop(0.7, 'rgba(239, 68, 68, 0.85)');
      flameGrad.addColorStop(1, 'transparent');

      ctx.fillStyle = flameGrad;
      // Twin-engine thermal exhaust plumes
      ctx.beginPath();
      ctx.ellipse(-jet.size * 0.11, jet.size * 0.44 + flameLen / 2, flameWidth / 2, flameLen / 2, 0, 0, Math.PI * 2);
      ctx.ellipse(jet.size * 0.11, jet.size * 0.44 + flameLen / 2, flameWidth / 2, flameLen / 2, 0, 0, Math.PI * 2);
      ctx.fill();

      // 2. Real Thermal FLIR Fighter Aircraft Image Sprite
      if (jet.img && jet.img.complete && jet.img.naturalWidth > 0) {
        ctx.drawImage(
          jet.img,
          -jet.size / 2,
          -jet.size / 2,
          jet.size,
          jet.size
        );
      }

      ctx.restore();
    };

    const render = () => {
      const w = canvas.width;
      const h = canvas.height;

      ctx.clearRect(0, 0, w, h);

      // 1. Perspective Flight Grid (Defense UAV Terrain Mesh)
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.07)';
      ctx.lineWidth = 1;

      gridOffset = (gridOffset + 0.4) % 40;

      // Vertical perspective lines converging slightly
      const numLines = 24;
      for (let i = 0; i <= numLines; i++) {
        const x = (w / numLines) * i;
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x + (x - w / 2) * 0.15, h);
        ctx.stroke();
      }

      // Horizontal moving scan grid
      for (let y = gridOffset; y < h; y += 40) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(w, y);
        ctx.stroke();
      }

      // 2. Center Drone Reticle / Crosshair HUD
      const cx = w / 2;
      const cy = h / 2;

      // Center Artificial Horizon
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.22)';
      ctx.lineWidth = 1.5;

      // Pitch Ladders
      ctx.beginPath();
      ctx.moveTo(cx - 70, cy - 40);
      ctx.lineTo(cx - 30, cy - 40);
      ctx.lineTo(cx - 30, cy - 35);
      ctx.moveTo(cx + 70, cy - 40);
      ctx.lineTo(cx + 30, cy - 40);
      ctx.lineTo(cx + 30, cy - 35);

      ctx.moveTo(cx - 70, cy + 40);
      ctx.lineTo(cx - 30, cy + 40);
      ctx.lineTo(cx - 30, cy + 45);
      ctx.moveTo(cx + 70, cy + 40);
      ctx.lineTo(cx + 30, cy + 40);
      ctx.lineTo(cx + 30, cy + 45);
      ctx.stroke();

      // Outer Radar Sweep Ring
      const radarRadius = Math.min(w, h) * 0.38;
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.12)';
      ctx.beginPath();
      ctx.arc(cx, cy, radarRadius, 0, Math.PI * 2);
      ctx.stroke();

      ctx.beginPath();
      ctx.arc(cx, cy, radarRadius * 0.6, 0, Math.PI * 2);
      ctx.stroke();

      // Sweeping radar beam
      scanAngle = (scanAngle + 0.015) % (Math.PI * 2);
      const sweepX = cx + Math.cos(scanAngle) * radarRadius;
      const sweepY = cy + Math.sin(scanAngle) * radarRadius;

      const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, radarRadius);
      grad.addColorStop(0, 'rgba(56, 189, 248, 0.08)');
      grad.addColorStop(1, 'transparent');
      
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.arc(cx, cy, radarRadius, scanAngle - 0.4, scanAngle);
      ctx.closePath();
      ctx.fill();

      ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(sweepX, sweepY);
      ctx.stroke();

      // 3. Live Action Supersonic Fighter Jet Sorties Rendering
      jets.forEach((jet) => {
        // Flight dynamics
        jet.x += Math.cos(jet.angle) * jet.speed;
        jet.y += Math.sin(jet.angle) * jet.speed;

        // Store contrail history
        jet.trail.push({ x: jet.x, y: jet.y, alpha: 1.0 });
        if (jet.trail.length > 28) jet.trail.shift();

        // Loop / wrap back on screen for continuous sortie patrol
        if (jet.x > w + 200 || jet.y > h + 200 || jet.x < -250 || jet.y < -250) {
          if (jet.angle >= 0 && jet.angle < Math.PI / 2) {
            jet.x = -150;
            jet.y = Math.random() * (h * 0.6);
          } else if (jet.angle < 0) {
            jet.x = -150;
            jet.y = h * 0.5 + Math.random() * (h * 0.4);
          } else {
            jet.x = Math.random() * (w * 0.6);
            jet.y = -100;
          }
          jet.trail = [];
        }

        // Draw Supersonic Thermal Contrail Ribbon
        for (let i = 0; i < jet.trail.length - 1; i++) {
          const p1 = jet.trail[i];
          const p2 = jet.trail[i + 1];
          const progress = i / jet.trail.length;
          
          ctx.strokeStyle = `rgba(56, 189, 248, ${progress * 0.35})`;
          ctx.lineWidth = 1 + progress * 2.5;
          ctx.beginPath();
          ctx.moveTo(p1.x, p1.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.stroke();
        }

        // Velocity vector leader line
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.45)';
        ctx.setLineDash([3, 4]);
        ctx.beginPath();
        ctx.moveTo(jet.x, jet.y);
        ctx.lineTo(jet.x + Math.cos(jet.angle) * 70, jet.y + Math.sin(jet.angle) * 70);
        ctx.stroke();
        ctx.setLineDash([]);

        // Draw Real Thermal FLIR Fighter Aircraft & Thrust Plume
        drawFighterJet(ctx, jet);

        // Fighter Radar HUD Reticle & Tactical Callout
        const rSize = jet.size * 0.38;
        ctx.strokeStyle = jet.locked ? '#38bdf8' : 'rgba(245, 158, 11, 0.7)';
        ctx.lineWidth = 1.2;
        
        // Target diamond / box around the jet
        ctx.beginPath();
        ctx.strokeRect(jet.x - rSize, jet.y - rSize, rSize * 2, rSize * 2);

        // Tactical Data Tag (Real Military Callout)
        ctx.fillStyle = jet.locked ? '#38bdf8' : '#f59e0b';
        ctx.font = 'bold 9.5px "Roboto Mono", monospace';
        ctx.fillText(`▲ ${jet.callsign}`, jet.x + rSize + 8, jet.y - 10);
        ctx.fillStyle = 'rgba(226, 232, 240, 0.9)';
        ctx.font = '8.5px "Roboto Mono", monospace';
        ctx.fillText(`ALT: ${jet.altitude} | SPD: ${jet.mach}`, jet.x + rSize + 8, jet.y + 3);
        ctx.fillStyle = 'rgba(56, 189, 248, 0.85)';
        ctx.fillText(`ORDNANCE: ${jet.weapons}`, jet.x + rSize + 8, jet.y + 15);
        ctx.fillStyle = 'rgba(16, 185, 129, 0.95)';
        ctx.fillText(`IFF: HOSTILE AIR PURGE ACTIVE`, jet.x + rSize + 8, jet.y + 27);
      });

      // 4. Tactical Ground Target Tracking Boxes (BMP-2 / T-90 Armor Footprints)
      targets.forEach((tgt, index) => {
        const tx = w * tgt.x;
        const ty = h * tgt.y;
        const boxW = tgt.w || 16;
        const boxH = tgt.h || 24;

        ctx.strokeStyle = tgt.lock ? 'rgba(56, 189, 248, 0.75)' : 'rgba(20, 184, 166, 0.6)';
        ctx.lineWidth = 1.0;

        // Bounding Corners
        const hw = boxW / 2 + 3;
        const hh = boxH / 2 + 3;
        const cLen = 4;
        
        // Top-left
        ctx.beginPath();
        ctx.moveTo(tx - hw, ty - hh + cLen);
        ctx.lineTo(tx - hw, ty - hh);
        ctx.lineTo(tx - hw + cLen, ty - hh);
        // Top-right
        ctx.moveTo(tx + hw - cLen, ty - hh);
        ctx.lineTo(tx + hw, ty - hh);
        ctx.lineTo(tx + hw, ty - hh + cLen);
        // Bottom-left
        ctx.moveTo(tx - hw, ty + hh - cLen);
        ctx.lineTo(tx - hw, ty + hh);
        ctx.lineTo(tx - hw + cLen, ty + hh);
        // Bottom-right
        ctx.moveTo(tx + hw - cLen, ty + hh);
        ctx.lineTo(tx + hw, ty + hh);
        ctx.lineTo(tx + hw, ty + hh - cLen);
        ctx.stroke();

        // Target Metadata Label
        ctx.fillStyle = tgt.lock ? '#38bdf8' : '#14b8a6';
        ctx.font = '8px "Roboto Mono", monospace';
        ctx.fillText(`[ ${tgt.id} ]`, tx - hw, ty - hh - 4);
        ctx.fillStyle = 'rgba(148, 163, 184, 0.75)';
        ctx.fillText(tgt.type, tx - hw, ty + hh + 9);
      });

      animationFrameId = requestAnimationFrame(render);
    };

    render();

    return () => {
      window.removeEventListener('resize', resize);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return (
    <main style={{
      position: 'relative',
      minHeight: '100vh',
      width: '100vw',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '24px',
      overflow: 'hidden',
    }}>
      {/* ── Dynamic Defense Drone POV Background HUD & Real 2000ft Thermal Terrain ── */}
      <div className="drone-hud-bg">
        <div className="warground-terrain-layer" />
        <canvas ref={canvasRef} className="hud-canvas" />
        <div className="hud-vignette" />
        <div className="hud-scanline" />
      </div>

      {/* Top HUD Telemetry HUD Bar (Live Drone POV feed) */}
      <div style={{
        position: 'fixed',
        top: '16px',
        left: '24px',
        right: '24px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        zIndex: 10,
        fontFamily: "'Roboto Mono', monospace",
        fontSize: '11px',
        color: 'var(--cyan)',
        letterSpacing: '0.08em',
        pointerEvents: 'none',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <span className="pulsing-dot" />
          <span style={{ fontWeight: '700', color: '#ffffff' }}>UAV-047 // SURVEILLANCE POV</span>
          <span style={{ color: 'var(--text-dim)' }}>|</span>
          <span style={{ color: 'var(--text-muted)' }}>ALT: {telemetry.alt}</span>
        </div>

        <div style={{ display: 'flex', gap: '16px', color: 'var(--text-muted)' }}>
          <span>LAT: <strong style={{ color: '#fff' }}>{telemetry.lat}</strong></span>
          <span>LON: <strong style={{ color: '#fff' }}>{telemetry.lon}</strong></span>
          <span>LINK: <strong style={{ color: '#10b981' }}>{telemetry.signal}</strong></span>
        </div>
      </div>

      {/* ── Main Professional Glass Card (Centered) ── */}
      <div className="military-glass-card" style={{
        width: '100%',
        maxWidth: '560px',
        padding: '36px 32px',
        textAlign: 'center',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '26px',
        zIndex: 20,
      }}>
        {/* Reticle Corner Brackets */}
        <div className="corner-bracket top-left" />
        <div className="corner-bracket top-right" />
        <div className="corner-bracket bottom-left" />
        <div className="corner-bracket bottom-right" />

        {/* Original Shivnetra White Logo */}
        <img
          src="/logo_white.png"
          alt="SHIVNETRA 47"
          style={{
            height: '52px',
            width: 'auto',
            objectFit: 'contain',
            filter: 'drop-shadow(0 4px 12px rgba(0,0,0,0.6))',
          }}
        />

        {/* Bold Status Header */}
        <div>
          <h1 style={{
            fontFamily: "'Rajdhani', 'Inter', sans-serif",
            fontSize: 'clamp(26px, 4.5vw, 36px)',
            fontWeight: '800',
            letterSpacing: '1.5px',
            textTransform: 'uppercase',
            color: '#ffffff',
            marginBottom: '6px',
            lineHeight: '1.2',
          }}>
            SITE UNDER UPGRADE
          </h1>
          <p style={{
            fontSize: '14px',
            color: 'var(--text-muted)',
            lineHeight: '1.5',
            maxWidth: '420px',
            margin: '0 auto',
          }}>
            SHIV-NETRA47 Air Defence avionics & telemetry portals are undergoing scheduled modernization.
          </p>
        </div>

        {/* Interactive Dynamic Progress Bar & Load Stats */}
        <div style={{
          width: '100%',
          backgroundColor: 'rgba(6, 14, 26, 0.75)',
          border: '1px solid rgba(56, 189, 248, 0.22)',
          borderRadius: '8px',
          padding: '18px 20px',
        }}>
          <div style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginBottom: '10px',
            fontFamily: "'Roboto Mono', monospace",
            fontSize: '12px',
          }}>
            <span style={{ color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '1px', display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span className="pulsing-dot" />
              SYSTEM SYNCHRONIZATION
            </span>
            <span style={{ color: 'var(--cyan)', fontWeight: '700', fontSize: '13px' }}>
              {progress}% DONE
            </span>
          </div>

          {/* Dynamic Progress Bar */}
          <div style={{
            width: '100%',
            height: '8px',
            backgroundColor: 'rgba(255, 255, 255, 0.08)',
            borderRadius: '4px',
            overflow: 'hidden',
          }}>
            <div 
              className="progress-bar-glow"
              style={{
                width: `${progress}%`,
                height: '100%',
                borderRadius: '4px',
              }} 
            />
          </div>

          {/* Dynamic Target Acquisition Stat Counter */}
          <div style={{
            display: 'flex',
            justifyContent: 'space-between',
            marginTop: '12px',
            fontSize: '11px',
            fontFamily: "'Roboto Mono', monospace",
            color: 'var(--text-dim)',
          }}>
            <span>PITCH: {telemetry.pitch}</span>
            <span>ROLL: {telemetry.roll}</span>
            <span>NODES: <strong style={{ color: '#38bdf8' }}>{telemetry.targetsLocked} ACTIVE</strong></span>
          </div>
        </div>
      </div>

      {/* Bottom HUD Baseline */}
      <div style={{
        position: 'fixed',
        bottom: '14px',
        left: '0',
        right: '0',
        textAlign: 'center',
        fontFamily: "'Roboto Mono', monospace",
        fontSize: '10px',
        color: 'var(--text-dim)',
        letterSpacing: '1.5px',
        textTransform: 'uppercase',
        zIndex: 10,
        pointerEvents: 'none',
      }}>
        SHIV-NETRA47 AIR DEFENCE SYSTEM PRIVATE LIMITED • INDIGENOUS DEFENCE PLATFORMS
      </div>
    </main>
  );
}
