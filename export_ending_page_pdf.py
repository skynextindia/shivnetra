import os
import subprocess
from PIL import Image
import fitz  # PyMuPDF

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge):
    edge = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

current_dir = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(current_dir, "pages", "ending_page_12x8.html")
html_url = f"file:///{html_file.replace(os.sep, '/')}"

export_dir = os.path.join(current_dir, "exports")
os.makedirs(export_dir, exist_ok=True)

out_png = os.path.join(export_dir, "ending_page_12x8.png")
out_pdf = os.path.join(current_dir, "SHIVNETRA47_Ending_Page_12x8.pdf")
out_pdf_exports = os.path.join(export_dir, "SHIVNETRA47_Ending_Page_12x8.pdf")

# 1. Capture Ultra High-Res 12x8 Landscape Screenshot (2880 x 1920, 3:2 ratio = 12x8)
cmd = [
    edge,
    "--headless",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=2880,1920",
    f"--screenshot={out_png}",
    html_url
]
print("Capturing 12x8 high-res render via headless browser...")
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if not os.path.exists(out_png):
    print("Error: Failed to capture screenshot")
    exit(1)

# 2. Build 12x8 inch Landscape PDF using PyMuPDF for exact print dimensions (12 in x 8 in = 864 x 576 points)
width_pt = 12.0 * 72.0  # 864 pt
height_pt = 8.0 * 72.0  # 576 pt

doc = fitz.open()
page = doc.new_page(width=width_pt, height=height_pt)
rect = fitz.Rect(0, 0, width_pt, height_pt)
page.insert_image(rect, filename=out_png)

doc.save(out_pdf, deflate=True, garbage=4)
doc.save(out_pdf_exports, deflate=True, garbage=4)
doc.close()

print(f"Successfully generated: {out_pdf} ({os.path.getsize(out_pdf) / (1024*1024):.2f} MB)")
print(f"Page dimensions: 12.0 in x 8.0 in (Landscape)")
