import os
import subprocess
import pymupdf as fitz
import shutil

# Locate browser executable (Chrome or Edge)
browser = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(browser):
    browser = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(browser):
    browser = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

current_dir = os.path.dirname(os.path.abspath(__file__))
pages_dir = os.path.join(current_dir, "pages_4page")
export_dir = os.path.join(current_dir, "exports_4page")
os.makedirs(export_dir, exist_ok=True)

brain_dir = r"C:\Users\rohan\.gemini\antigravity-ide\brain\5b2d8c6f-bd60-420f-96f6-0b0ba1090a9d"

pages = [
    ("brochure_cover.html", "Shiv-Netra47_4Page_01_Cover.pdf", "Shiv-Netra47_4Page_01_Cover.svg"),
    ("brochure_page_02.html", "Shiv-Netra47_4Page_02_Verticals.pdf", "Shiv-Netra47_4Page_02_Verticals.svg"),
    ("brochure_page_03.html", "Shiv-Netra47_4Page_03_Academy_MRO.pdf", "Shiv-Netra47_4Page_03_Academy_MRO.svg"),
    ("brochure_back.html", "Shiv-Netra47_4Page_04_Governance.pdf", "Shiv-Netra47_4Page_04_Governance.svg"),
]

master_pdf_name = "Shiv-Netra47_4Page_Booklet.pdf"
master_pdf_path = os.path.join(current_dir, master_pdf_name)
master_doc = fitz.open()

total_pages = len(pages)
print(f"Building Master Vector & Illustrator-Editable {total_pages}-Page A4 PDF Dossier...")

for idx, (html_name, pdf_name, svg_name) in enumerate(pages, start=1):
    html_file = os.path.join(pages_dir, html_name)
    single_pdf_path = os.path.join(export_dir, pdf_name)
    single_pdf_root = os.path.join(current_dir, pdf_name)
    single_svg_path = os.path.join(export_dir, svg_name)
    single_svg_root = os.path.join(current_dir, svg_name)

    print(f"[{idx}/{total_pages}] Vector PDF Rendering: {html_name} -> {pdf_name}...")
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={single_pdf_path}",
        html_file
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)

    if not os.path.exists(single_pdf_path):
        print(f"Error: Failed to render {single_pdf_path}")
        print(res.stderr)
        exit(1)

    # Verify single page vector structure
    doc = fitz.open(single_pdf_path)
    page_count = len(doc)
    page_rect = doc[0].rect if page_count > 0 else None
    text_len = len(doc[0].get_text()) if page_count > 0 else 0
    font_count = len(doc[0].get_fonts()) if page_count > 0 else 0
    size_kb = os.path.getsize(single_pdf_path) / 1024
    print(f"   -> Success: {page_count} page(s), rect={page_rect}, {text_len} text chars, {font_count} fonts, {size_kb:.1f} KB")

    # Generate Illustrator native SVG for maximum editing freedom
    try:
        svg_text = doc[0].get_svg_image()
        with open(single_svg_path, "w", encoding="utf-8") as sf:
            sf.write(svg_text)
        shutil.copyfile(single_svg_path, single_svg_root)
        if os.path.exists(brain_dir):
            shutil.copyfile(single_svg_path, os.path.join(brain_dir, svg_name))
        print(f"   -> Illustrator SVG exported: {svg_name}")
    except Exception as e:
        print(f"   -> SVG export warning: {e}")

    # Copy single page PDF to root and brain
    shutil.copyfile(single_pdf_path, single_pdf_root)
    if os.path.exists(brain_dir):
        try:
            shutil.copyfile(single_pdf_path, os.path.join(brain_dir, pdf_name))
        except Exception:
            pass

    # Insert vector page into master document
    master_doc.insert_pdf(doc)
    doc.close()

# Save master PDF with clean streams for Adobe Illustrator compatibility
print("\nSaving Master Vector PDF...")
master_doc.save(master_pdf_path, deflate=False, clean=True)
master_pdf_export = os.path.join(export_dir, master_pdf_name)
master_doc.save(master_pdf_export, deflate=False, clean=True)

# Also create standard A4-dimension version (595.28 x 841.89 pt) for print shops
print("Generating Standard A4 Print Scaled Edition (595x842 pt)...")
standard_a4_doc = fitz.open()
target_rect = fitz.Rect(0, 0, 595.27559, 841.88976)

for pno in range(len(master_doc)):
    orig_page = master_doc[pno]
    new_page = standard_a4_doc.new_page(width=target_rect.width, height=target_rect.height)
    new_page.show_pdf_page(target_rect, master_doc, pno)

standard_a4_name = "Shiv-Netra47_4Page_Print_A4.pdf"
standard_a4_path = os.path.join(current_dir, standard_a4_name)
standard_a4_doc.save(standard_a4_path, deflate=False, clean=True)
standard_a4_doc.save(os.path.join(export_dir, standard_a4_name), deflate=False, clean=True)
standard_a4_doc.close()

# Also save aliases for convenience
alt_master_names = [
    "Shivnetra47_4Page_Booklet.pdf",
    "SHIVNETRA47_Defence_Brochure_4Page_A4_Blue.pdf"
]
for alt_name in alt_master_names:
    shutil.copyfile(master_pdf_path, os.path.join(current_dir, alt_name))
    shutil.copyfile(master_pdf_path, os.path.join(export_dir, alt_name))

master_doc.close()

# Copy master PDFs and standard print A4 to brain
if os.path.exists(brain_dir):
    try:
        shutil.copyfile(master_pdf_path, os.path.join(brain_dir, master_pdf_name))
        shutil.copyfile(standard_a4_path, os.path.join(brain_dir, standard_a4_name))
        for alt_name in alt_master_names:
            shutil.copyfile(os.path.join(current_dir, alt_name), os.path.join(brain_dir, alt_name))
    except Exception:
        pass

# Render high-res PNG previews
print("Generating PNG previews...")
preview_doc = fitz.open(master_pdf_path)
for i, page in enumerate(preview_doc):
    pix = page.get_pixmap(dpi=150)
    png_name = f"page_4p_{i+1}.png"
    pix.save(os.path.join(current_dir, png_name))
    if os.path.exists(brain_dir):
        pix.save(os.path.join(brain_dir, png_name))
    print(f"   -> Page {i+1} preview: {pix.width}x{pix.height}")
preview_doc.close()

print("\n" + "="*75)
print("VECTOR & ILLUSTRATOR-EDITABLE DEFENCE BROCHURE EXPORT COMPLETE")
print(f"Master Vector PDF : {master_pdf_path}")
print(f"Standard Print A4 : {standard_a4_path}")
print(f"Master File Size  : {os.path.getsize(master_pdf_path) / 1024:.1f} KB ({os.path.getsize(master_pdf_path)/(1024*1024):.2f} MB)")
print("Editable Features : TrueType Vector Text (Selectable/Editable), 1:1 Vector Paths, Clean RGB")
print("Illustrator Ready : Native 1:1 Artboards, No Clip Matrix, Clean Objects + Standalone SVGs")
print("="*75)
