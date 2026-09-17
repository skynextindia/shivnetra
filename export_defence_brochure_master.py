import os
import subprocess
import pymupdf as fitz
import shutil

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge):
    edge = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

current_dir = os.path.dirname(os.path.abspath(__file__))
pages_dir = os.path.join(current_dir, "pages")
export_dir = os.path.join(current_dir, "exports")
os.makedirs(export_dir, exist_ok=True)

brain_dir = r"C:\Users\rohan\.gemini\antigravity-ide\brain\acd8dede-c6fc-4b02-8d8c-5b2626ee9709"

pages = [
    ("brochure_cover.html", "brochure_cover.png", "SHIVNETRA47_Brochure_Cover_Front.pdf"),
    ("brochure_page_01.html", "brochure_page_01.png", "SHIVNETRA47_Brochure_Page_01.pdf"),
    ("brochure_page_02.html", "brochure_page_02.png", "SHIVNETRA47_Brochure_Page_02.pdf"),
    ("brochure_page_03.html", "brochure_page_03.png", "SHIVNETRA47_Brochure_Page_03.pdf"),
    ("brochure_page_04.html", "brochure_page_04.png", "SHIVNETRA47_Brochure_Page_04.pdf"),
    ("brochure_page_05.html", "brochure_page_05.png", "SHIVNETRA47_Brochure_Page_05.pdf"),
    ("brochure_page_06.html", "brochure_page_06.png", "SHIVNETRA47_Brochure_Page_06.pdf"),
    ("brochure_back.html", "brochure_back.png", "SHIVNETRA47_Brochure_Cover_Back.pdf"),
]

# Standard A4 dimensions in points @ 72 pt/inch
width_pt = 595.28   # 210 mm
height_pt = 841.89  # 297 mm

master_pdf_path = os.path.join(current_dir, "SHIVNETRA47_Defence_and_Swarm_UAS_Brochure_A4.pdf")
master_doc = fitz.open()

total_pages = len(pages)
print(f"Building Master Defence & Swarm UAS {total_pages}-Page A4 Publication (Front Cover + 6 Core Pages + Back Cover)...")

for idx, (html_name, png_name, pdf_name) in enumerate(pages, start=1):
    html_file = os.path.join(pages_dir, html_name)
    html_url = f"file:///{html_file.replace(os.sep, '/')}"
    out_png = os.path.join(export_dir, png_name)

    # Force clean high-res re-render
    print(f"[{idx}/{total_pages}] Rendering {html_name} -> {png_name} (2480x3508 @ 300 DPI)...")
    cmd = [
        edge,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        "--virtual-time-budget=4000",
        "--run-all-compositor-stages-before-draw",
        "--window-size=2480,3508",
        f"--screenshot={out_png}",
        html_url
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if not os.path.exists(out_png):
        print(f"Error: Failed to render {out_png}")
        exit(1)

    # Add page to master PDF
    page = master_doc.new_page(width=width_pt, height=height_pt)
    rect = fitz.Rect(0, 0, width_pt, height_pt)
    page.insert_image(rect, filename=out_png)

    # Also build individual page PDF
    single_pdf_path = os.path.join(export_dir, pdf_name)
    single_pdf_root = os.path.join(current_dir, pdf_name)
    single_doc = fitz.open()
    s_page = single_doc.new_page(width=width_pt, height=height_pt)
    s_page.insert_image(rect, filename=out_png)
    single_doc.save(single_pdf_path)
    single_doc.save(single_pdf_root)
    single_doc.close()

    # Copy to brain artifact directory
    if os.path.exists(brain_dir):
        brain_png = os.path.join(brain_dir, png_name)
        try:
            shutil.copyfile(out_png, brain_png)
        except Exception:
            pass

master_doc.save(master_pdf_path, deflate=True, garbage=4)
master_doc.close()

if os.path.exists(brain_dir):
    try:
        shutil.copyfile(master_pdf_path, os.path.join(brain_dir, "SHIVNETRA47_Defence_and_Swarm_UAS_Brochure_A4.pdf"))
    except Exception:
        pass

print("\n" + "="*70)
print("DEFENCE & SWARM UAS BROCHURE EXPORT COMPLETE")
print(f"Master 8-Page Publication: {master_pdf_path}")
print(f"File Size: {os.path.getsize(master_pdf_path) / (1024*1024):.2f} MB")
print("="*70)
