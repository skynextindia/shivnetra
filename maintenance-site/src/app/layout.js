import './globals.css';

export const metadata = {
  title: 'SHIV-NETRA47 | Site Under Upgrade',
  description: 'SHIV-NETRA47 Air Defence Systems. Scheduled upgrade in progress.',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=Rajdhani:wght@700&family=Roboto+Mono:wght@500;600&display=swap" rel="stylesheet" />
      </head>
      <body>{children}</body>
    </html>
  );
}
