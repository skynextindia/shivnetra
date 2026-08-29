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
        pitch: `${(Math.random() > 0.5 ? '+' : '-')}${Math.abs((Math.random() * 3).toFixed(1)).padStart(4, '0')}°`,
        roll: `${(Math.random() > 0.5 ? '+' : '-')}${Math.abs((Math.random() * 2).toFixed(1)).padStart(4, '0')}°`,
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

    // Simulated Target coordinates
    const targets = [
      { x: 0.28, y: 0.35, id: 'TGT-ALPHA-01', type: 'RADAR-NODE', lock: true },
      { x: 0.74, y: 0.62, id: 'TGT-BRAVO-04', type: 'TELEMETRY-RELAY', lock: true },
      { x: 0.42, y: 0.72, id: 'TGT-GCS-09', type: 'DATA-LINK-UAV', lock: false },
    ];

    const resize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };
    resize();
    window.addEventListener('resize', resize);

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

      // 3. Technical Drone Target Tracking Boxes
      targets.forEach((tgt, index) => {
        const tx = w * tgt.x;
        const ty = h * tgt.y;
        const boxSize = 34 + Math.sin(Date.now() * 0.003 + index) * 2;

        ctx.strokeStyle = tgt.lock ? 'rgba(56, 189, 248, 0.75)' : 'rgba(20, 184, 166, 0.6)';
        ctx.lineWidth = 1.2;

        // Bounding Corners
        const s = boxSize / 2;
        const cLen = 7;
        // Top-left
        ctx.beginPath();
        ctx.moveTo(tx - s, ty - s + cLen);
        ctx.lineTo(tx - s, ty - s);
        ctx.lineTo(tx - s + cLen, ty - s);
        // Top-right
        ctx.moveTo(tx + s - cLen, ty - s);
        ctx.lineTo(tx + s, ty - s);
        ctx.lineTo(tx + s, ty - s + cLen);
        // Bottom-left
        ctx.moveTo(tx - s, ty + s - cLen);
        ctx.lineTo(tx - s, ty + s);
        ctx.lineTo(tx - s + cLen, ty + s);
        // Bottom-right
        ctx.moveTo(tx + s - cLen, ty + s);
        ctx.lineTo(tx + s, ty + s);
        ctx.lineTo(tx + s, ty + s - cLen);
        ctx.stroke();

        // Target Metadata Label
        ctx.fillStyle = tgt.lock ? '#38bdf8' : '#14b8a6';
        ctx.font = '9px "Roboto Mono", monospace';
        ctx.fillText(`[ ${tgt.id} ]`, tx - s, ty - s - 5);
        ctx.fillStyle = 'rgba(148, 163, 184, 0.8)';
        ctx.fillText(tgt.type, tx - s, ty + s + 12);
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
      {/* ── Dynamic Defense Drone POV Background HUD ── */}
      <div className="drone-hud-bg">
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
