import os
import subprocess
import pymupdf as fitz

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge):
    edge = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

current_dir = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(current_dir, "pages", "brochure_page_02.html")
html_url = f"file:///{html_file.replace(os.sep, '/')}"

export_dir = os.path.join(current_dir, "exports")
os.makedirs(export_dir, exist_ok=True)

out_png = os.path.join(export_dir, "brochure_page_02.png")
out_pdf = os.path.join(export_dir, "SHIVNETRA47_Brochure_Page_02.pdf")
out_pdf_root = os.path.join(current_dir, "SHIVNETRA47_Brochure_Page_02.pdf")

# 1. Capture Ultra High-Res A4 Portrait (2480 x 3508 px @ 300 DPI)
cmd = [
    edge,
    "--headless",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=2480,3508",
    f"--screenshot={out_png}",
    html_url
]
print("Rendering A4 Portrait Screenshot (2480x3508) via headless browser...")
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if not os.path.exists(out_png):
    print("Error: Failed to capture screenshot")
    exit(1)

# 2. Build exact A4 Portrait PDF using PyMuPDF (595.28 x 841.89 pt)
width_pt = 595.28  # 210 mm
height_pt = 841.89  # 297 mm

doc = fitz.open()
page = doc.new_page(width=width_pt, height=height_pt)
rect = fitz.Rect(0, 0, width_pt, height_pt)
page.insert_image(rect, filename=out_png)

doc.save(out_pdf, deflate=True, garbage=4)
doc.save(out_pdf_root, deflate=True, garbage=4)
doc.close()

print(f"Successfully generated:")
print(f"  - PNG: {out_png} ({os.path.getsize(out_png) / (1024*1024):.2f} MB)")
print(f"  - PDF: {out_pdf} ({os.path.getsize(out_pdf) / (1024*1024):.2f} MB)")
