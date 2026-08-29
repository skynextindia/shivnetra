import fitz
import os

pdf_path = r'C:\Users\rohan\.gemini\antigravity-ide\brain\d1cf8b9e-1677-4e8e-a002-656648141668\.user_uploaded\media_1787925134185.pdf'
out_dir = r'C:\Users\rohan\.gemini\antigravity-ide\scratch\shivnetra47_presentation\pages'
assets_dir = r'C:\Users\rohan\.gemini\antigravity-ide\scratch\shivnetra47_presentation\assets'

doc = fitz.open(pdf_path)
num_pages = len(doc)
print(f'Total pages in source PDF: {num_pages}')

# Titles for each page from OCR and source contents
page_titles = [
    "01. UAS Certification & European Framework",
    "02. Operational Authorisation & SORA Methodology",
    "03. Proposal — Design, Development & Construction (Breakup)",
    "04. Executive Cost Summary & Program Scope",
    "05. EU UAS Certification Overview",
    "06. EU UAS Regulation — Operation Categories",
    "07. EU UAS Regulation — Certification Requirements",
    "08. Open Category Certification & Regulation Requirements",
    "09. CIL Evaluation Tests (Part 1)",
    "10. CIL Evaluation Tests (Part 2)",
    "11. Specific Category Certification & Requirements",
    "12. Operational Authorisation Process & End-to-End Solution",
    "13. Certified Category Certification",
    "14. One Stop Shop Market Entry Support",
    "15. Contact & Institutional Accreditations"
]

# Render high-res slide images if not present
for i in range(num_pages):
    page_num = i + 1
    src_img_rel = f'../assets/src_page_{page_num:02d}.png'
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Page {page_num:02d} - {page_titles[i]}</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    body, html {{
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      background-color: #0b100d;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
    }}
    .slide-canvas {{
      width: 1920px;
      height: 1080px;
      position: relative;
      background: #0b100d;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-sizing: border-box;
      border: 1px solid rgba(109, 142, 118, 0.25);
    }}
    .slide-img-wrapper {{
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      background: #000000;
    }}
    .slide-img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}
  </style>
</head>
<body>
  <div class="slide-canvas">
    <div class="corner-tr"></div>
    <div class="corner-bl"></div>
    <div class="slide-img-wrapper">
      <img src="{src_img_rel}" alt="Page {page_num:02d} - {page_titles[i]}" class="slide-img">
    </div>
  </div>
</body>
</html>
'''
    target_file = os.path.join(out_dir, f'page_{page_num:02d}.html')
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f'Wrote {target_file}')

print('All 15 slide HTML files successfully generated directly from source PDF!')
