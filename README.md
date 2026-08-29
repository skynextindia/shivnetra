# SHIVNETRA 47 - Air Defence & Autonomous UAV Systems

Repository containing the official web assets, master slide deck, presentation builder tools, and the Next.js maintenance portal for **SHIV-NETRA47 AIR DEFENCE SYSTEM PRIVATE LIMITED**.

---

## 📁 Repository Structure

```
.
├── maintenance-site/           # Next.js Single Page Maintenance Website
│   ├── src/app/
│   │   ├── globals.css         # Minimal theme styling
│   │   ├── layout.js          # Root layout & typography
│   │   └── page.js            # Maintenance page (Logo + 85% Load status)
│   ├── public/                # Web assets & original logos
│   └── package.json           # Next.js dependencies
│
├── pages/                     # High-resolution slide pages (12x8 HTML/CSS)
│   ├── slide_01.html ... slide_15.html
│   └── ending_page_12x8.html  # Official presentation closing page
│
├── assets/                    # Original vector logos, UAV renders & technical diagrams
├── exports/                   # Rendered high-res PNG slide exports
│
├── index.html                 # Master presentation viewer & slide deck navigator
├── build_all_custom_slides.py # Automated presentation generator
├── export_ending_page_pdf.py  # Headless Chromium PDF export utility
└── export_pptx.py             # PowerPoint presentation builder
```

---

## 🚀 Running the Maintenance Site

```bash
cd maintenance-site
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the portal.

---

## 📄 Presentation Decks
- `SHIVNETRA47_Master_Slide_Deck.pdf`
- `SHIVNETRA47_Master_Slide_Deck.pptx`
- `SHIVNETRA47_Ending_Page_12x8.pdf`

---

© 2026 SHIV-NETRA47 AIR DEFENCE SYSTEM PRIVATE LIMITED. All rights reserved.
