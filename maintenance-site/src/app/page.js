export default function MaintenancePage() {
  return (
    <main style={{
      width: '100%',
      maxWidth: '640px',
      margin: '0 auto',
      padding: '40px 24px',
      textAlign: 'center',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: '32px',
    }}>
      {/* Original Logo */}
      <img
        src="/logo_white.png"
        alt="SHIVNETRA 47"
        style={{
          height: '56px',
          width: 'auto',
          objectFit: 'contain',
        }}
      />

      {/* Main Bold Status Header */}
      <div>
        <h1 style={{
          fontFamily: "'Rajdhani', 'Inter', sans-serif",
          fontSize: 'clamp(28px, 5vw, 40px)',
          fontWeight: '800',
          letterSpacing: '1px',
          textTransform: 'uppercase',
          color: '#ffffff',
          marginBottom: '8px',
          lineHeight: '1.2',
        }}>
          SITE UNDER UPGRADE
        </h1>
        <p style={{
          fontSize: '15px',
          color: '#94a3b8',
          lineHeight: '1.5',
        }}>
          We are upgrading our systems and will be back live shortly.
        </p>
      </div>

      {/* Load Stats (85% Done) */}
      <div style={{
        width: '100%',
        maxWidth: '460px',
        backgroundColor: '#0d1726',
        border: '1px solid rgba(56, 189, 248, 0.25)',
        borderRadius: '8px',
        padding: '20px 24px',
      }}>
        <div style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          marginBottom: '10px',
          fontFamily: "'Roboto Mono', monospace",
          fontSize: '13px',
        }}>
          <span style={{ color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '1px' }}>
            Upgrade Status
          </span>
          <span style={{ color: '#38bdf8', fontWeight: '700' }}>
            85% Done
          </span>
        </div>

        {/* Progress Bar */}
        <div style={{
          width: '100%',
          height: '8px',
          backgroundColor: 'rgba(255, 255, 255, 0.1)',
          borderRadius: '4px',
          overflow: 'hidden',
        }}>
          <div style={{
            width: '85%',
            height: '100%',
            backgroundColor: '#0284c7',
            borderRadius: '4px',
          }} />
        </div>
      </div>
    </main>
  );
}
