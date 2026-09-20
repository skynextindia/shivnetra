light_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 620" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Michroma&amp;family=Montserrat:wght@800&amp;display=swap');
      .emblem-top { fill: #0a192f; }
      .emblem-bot { fill: #1e293b; }
      .word-main {
        font-family: 'Michroma', sans-serif;
        font-size: 112px;
        fill: #0a192f;
        stroke: #0a192f;
        stroke-width: 4.8px;
        letter-spacing: 0.12em;
      }
      .word-num {
        font-family: 'Michroma', sans-serif;
        font-size: 112px;
        fill: #475569;
        stroke: #475569;
        stroke-width: 4.8px;
        letter-spacing: 0.12em;
      }
      .tagline {
        font-family: 'Montserrat', sans-serif;
        font-size: 30px;
        font-weight: 800;
        fill: #1e293b;
        letter-spacing: 0.38em;
      }
    </style>
  </defs>
  
  <!-- DELTA EMBLEM -->
  <g transform="translate(410, 0) scale(2.42)">
    <polygon class="emblem-top" points="5,105 239,6 125,95" />
    <polygon class="emblem-bot" points="56,107 118,98 175,154" />
  </g>
  
  <!-- WORDMARK -->
  <g transform="translate(700, 480)" text-anchor="middle">
    <text>
      <tspan class="word-main">SHIVNETRA</tspan><tspan class="word-num">47</tspan>
    </text>
  </g>
  
  <!-- SUBLINE -->
  <g transform="translate(90, 560)">
    <text class="tagline" x="0" y="24">MILITARY UAV SYSTEMS</text>
    <g transform="translate(940, 6) skewX(-25)">
      <rect x="0" y="0" width="80" height="20" rx="2" fill="#ff671f" />
      <rect x="86" y="0" width="80" height="20" rx="2" fill="#94a3b8" />
      <rect x="172" y="0" width="80" height="20" rx="2" fill="#046a38" />
    </g>
  </g>
</svg>"""

dark_svg = light_svg.replace('#0a192f', '#ffffff').replace('#1e293b', '#e2e8f0').replace('#475569', '#94a3b8').replace('#94a3b8', '#ffffff')

with open('assets/shivnetra_logo_original_light.svg', 'w', encoding='utf-8') as f:
    f.write(light_svg)

with open('assets/shivnetra_logo_original_dark.svg', 'w', encoding='utf-8') as f:
    f.write(dark_svg)

print('Saved SVG assets.')
