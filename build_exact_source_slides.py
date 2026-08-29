import fitz, os
from PIL import Image

pdf_path = r'C:\Users\rohan\.gemini\antigravity-ide\brain\d1cf8b9e-1677-4e8e-a002-656648141668\.user_uploaded\media_1787922390494.pdf'
pages_dir = r'C:\Users\rohan\.gemini\antigravity-ide\scratch\shivnetra47_presentation\pages'
assets_dir = r'C:\Users\rohan\.gemini\antigravity-ide\scratch\shivnetra47_presentation\assets'
export_dir = r'C:\Users\rohan\.gemini\antigravity-ide\scratch\shivnetra47_presentation\exports'
brain_dir = r'C:\Users\rohan\.gemini\antigravity-ide\brain\d1cf8b9e-1677-4e8e-a002-656648141668\slides'

os.makedirs(pages_dir, exist_ok=True)
os.makedirs(assets_dir, exist_ok=True)
os.makedirs(export_dir, exist_ok=True)
os.makedirs(brain_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f'Processing {len(doc)} pages of original SHIVNETRA47 document...')

slide_titles = [
    "01. Indigenous Swarm UAV Development Program",
    "02. Tactical Swarm UAV System (6 Units)",
    "03. Extended Range Swarm System (24+ Units)",
    "04. 1. Program Vision",
    "05. 2. Proposed System Architecture",
    "06. 3. Nano-UAV — Swarm Element",
    "07. 4. Overwatch UAV",
    "08. 5. In-House Development Model",
    "09. 6. Engineering Workstreams",
    "10. 7. Prototype, Integration & Flight-Test Program",
    "11. 8. Project Completion Deliverables",
    "12. 9. Execution Roadmap & Strategic Outcome",
    "13. 10. Reference Budget Framework"
]

# Delete page_14 and page_15 if present
for extra in [14, 15]:
    for p in [
        os.path.join(pages_dir, f'page_{extra:02d}.html'),
        os.path.join(export_dir, f'page_{extra:02d}.png'),
        os.path.join(brain_dir, f'page_{extra:02d}.png')
    ]:
        if os.path.exists(p):
            os.remove(p)

for i in range(len(doc)):
    page_num = i + 1
    page = doc[i]
    pix = page.get_pixmap(dpi=200)
    img_name = f'exact_doc_page_{page_num:02d}.png'
    pix.save(os.path.join(assets_dir, img_name))

    # Also render export directly to 1920x1080 canvas
    img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
    canvas = Image.new('RGB', (1920, 1080), (11, 16, 13))
    img.thumbnail((1920, 1080), Image.Resampling.LANCZOS)
    offset_x = (1920 - img.width) // 2
    offset_y = (1080 - img.height) // 2
    canvas.paste(img, (offset_x, offset_y))
    
    png_name = f'page_{page_num:02d}.png'
    canvas.save(os.path.join(export_dir, png_name))
    canvas.save(os.path.join(brain_dir, png_name))

    # Write HTML page
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Page {page_num:02d} - {slide_titles[i]}</title>
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
      background: #080d0a;
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
      <img src="../assets/{img_name}" alt="{slide_titles[i]}" class="slide-img">
    </div>
  </div>
</body>
</html>
'''
    html_path = os.path.join(pages_dir, f'page_{page_num:02d}.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f'Slide {page_num:02d} rendered & HTML generated: {slide_titles[i]}')

print('All 13 slides from exact SHIVNETRA47 source rebuilt perfectly!')
