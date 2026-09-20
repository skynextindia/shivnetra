import os
import subprocess
import pymupdf as fitz
import shutil

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge):
    edge = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

current_dir = os.path.dirname(os.path.abspath(__file__))
pages_dir = os.path.join(current_dir, "pages_corporate")
export_dir = os.path.join(current_dir, "exports")
os.makedirs(export_dir, exist_ok=True)

brain_dir = r"C:\Users\rohan\.gemini\antigravity-ide\brain\648aec05-8088-4c12-9c73-c7ba743b2da6"

pages = [
    ("brochure_cover.html", "brochure_cover_corporate.png", "SHIVNETRA47_Brochure_Cover_Front_Corporate.pdf"),
    ("brochure_page_01.html", "brochure_page_01_corporate.png", "SHIVNETRA47_Brochure_Page_01_Corporate.pdf"),
    ("brochure_page_02.html", "brochure_page_02_corporate.png", "SHIVNETRA47_Brochure_Page_02_Corporate.pdf"),
    ("brochure_page_03.html", "brochure_page_03_corporate.png", "SHIVNETRA47_Brochure_Page_03_Corporate.pdf"),
    ("brochure_back.html", "brochure_back_corporate.png", "SHIVNETRA47_Brochure_Cover_Back_Corporate.pdf"),
]

# Standard A4 dimensions in points @ 72 pt/inch
width_pt = 595.28   # 210 mm
height_pt = 841.89  # 297 mm

master_pdf_name = "SHIVNETRA47_Defence_and_Swarm_UAS_Brochure_Corporate.pdf"
master_pdf_path = os.path.join(current_dir, master_pdf_name)
master_doc = fitz.open()

total_pages = len(pages)
print(f"Building Master Serious Corporate Defence & Swarm UAS {total_pages}-Page A4 Publication...", flush=True)

for idx, (html_name, png_name, pdf_name) in enumerate(pages, start=1):
    html_file = os.path.join(pages_dir, html_name)
    html_url = f"file:///{html_file.replace(os.sep, '/')}"
    out_png = os.path.join(export_dir, png_name)

    print(f"[{idx}/{total_pages}] Rendering {html_name} -> {png_name} (2480x3508 @ 300 DPI)...", flush=True)
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
        print(f"Error: Failed to render {out_png}", flush=True)
        exit(1)

    # Add page to master PDF
    page = master_doc.new_page(width=width_pt, height=height_pt)
    page.insert_image(fitz.Rect(0, 0, width_pt, height_pt), filename=out_png)

    # Also save standalone single-page PDF
    single_doc = fitz.open()
    sp = single_doc.new_page(width=width_pt, height=height_pt)
    sp.insert_image(fitz.Rect(0, 0, width_pt, height_pt), filename=out_png)
    single_pdf_path = os.path.join(current_dir, pdf_name)
    single_doc.save(single_pdf_path, deflate=True)
    single_doc.close()

    # Copy to brain dir if exists
    if os.path.exists(brain_dir):
        shutil.copy2(out_png, os.path.join(brain_dir, png_name))

# Save Master PDF with deflate compression
master_doc.save(master_pdf_path, deflate=True)
master_doc.close()

# Copy master PDF to brain dir
if os.path.exists(brain_dir):
    shutil.copy2(master_pdf_path, os.path.join(brain_dir, master_pdf_name))

size_mb = os.path.getsize(master_pdf_path) / (1024 * 1024)
print("\n" + "=" * 70, flush=True)
print("SERIOUS CORPORATE DEFENCE BROCHURE EXPORT COMPLETE", flush=True)
print(f"Master {total_pages}-Page PDF: {master_pdf_path}", flush=True)
print(f"File Size: {size_mb:.2f} MB", flush=True)
print("=" * 70 + "\n", flush=True)
