import os
import subprocess
import pymupdf as fitz
import shutil

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge):
    edge = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

current_dir = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(current_dir, "pages", "brochure_page_01_landscape.html")
html_url = f"file:///{html_file.replace(os.sep, '/')}"

export_dir = os.path.join(current_dir, "exports")
os.makedirs(export_dir, exist_ok=True)

out_png = os.path.join(export_dir, "brochure_page_01_landscape.png")
out_pdf = os.path.join(export_dir, "SHIVNETRA47_Brochure_Page_01_Landscape.pdf")
artifact_dir = r"C:\Users\rohan\.gemini\antigravity-ide\brain\d47fcf79-9d28-4a3a-9bb7-8a7350a1df7c"

# 1. Capture Ultra High-Res A4 Landscape (3508 x 2480 px @ 300 DPI)
cmd = [
    edge,
    "--headless",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=3508,2480",
    f"--screenshot={out_png}",
    html_url
]
print("Rendering A4 Landscape (3508x2480 @ 300 DPI) via headless browser...")
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if not os.path.exists(out_png):
    print("Error: Failed to capture screenshot")
    exit(1)

# 2. Build exact A4 Landscape PDF using PyMuPDF (841.89 x 595.28 pt = 297 x 210 mm)
width_pt = 841.89   # 297 mm
height_pt = 595.28  # 210 mm

doc = fitz.open()
page = doc.new_page(width=width_pt, height=height_pt)
rect = fitz.Rect(0, 0, width_pt, height_pt)
page.insert_image(rect, filename=out_png)

doc.save(out_pdf, deflate=True, garbage=4)
doc.close()

# Copy to artifact dir for preview
artifact_png = os.path.join(artifact_dir, "brochure_page_01_landscape.png")
shutil.copyfile(out_png, artifact_png)

print(f"Successfully generated:")
print(f"  - PNG: {out_png} ({os.path.getsize(out_png) / (1024*1024):.2f} MB)")
print(f"  - PDF: {out_pdf} ({os.path.getsize(out_pdf) / (1024*1024):.2f} MB)")
