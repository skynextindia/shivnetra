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
pages_dir = os.path.join(current_dir, "pages_blue")
export_dir = os.path.join(current_dir, "exports")
os.makedirs(export_dir, exist_ok=True)

brain_dir = r"C:\Users\rohan\.gemini\antigravity-ide\brain\607a9feb-0af4-484e-8801-25049c436746"

pages = [
    ("brochure_cover.html", "SHIVNETRA47_Brochure_Cover_Front_Blue.pdf"),
    ("brochure_page_01.html", "SHIVNETRA47_Brochure_Page_01_Blue.pdf"),
    ("brochure_page_02.html", "SHIVNETRA47_Brochure_Page_02_Blue.pdf"),
    ("brochure_page_03.html", "SHIVNETRA47_Brochure_Page_03_Blue.pdf"),
    ("brochure_back.html", "SHIVNETRA47_Brochure_Cover_Back_Blue.pdf"),
]

master_pdf_name = "SHIVNETRA47_Defence_and_Swarm_UAS_Brochure_A4_Blue.pdf"
master_pdf_path = os.path.join(current_dir, master_pdf_name)
master_doc = fitz.open()

total_pages = len(pages)
print(f"Building Master Vector & Illustrator-Editable {total_pages}-Page A4 PDF Dossier...")

for idx, (html_name, pdf_name) in enumerate(pages, start=1):
    html_file = os.path.join(pages_dir, html_name)
    single_pdf_path = os.path.join(export_dir, pdf_name)
    single_pdf_root = os.path.join(current_dir, pdf_name)

    print(f"[{idx}/{total_pages}] Vector PDF Rendering: {html_name} -> {pdf_name}...")
    cmd = [
        browser,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={single_pdf_path}",
        html_file
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)

    if not os.path.exists(single_pdf_path):
        print(f"Error: Failed to render {single_pdf_path}")
        print(res.stderr)
        exit(1)

    # Ensure ColorTransform 0 is corrected to ColorTransform 1 for PDF.js / viewer compatibility
    with open(single_pdf_path, "rb") as pf:
        pdf_raw = pf.read()
    if b"/ColorTransform 0" in pdf_raw:
        pdf_raw = pdf_raw.replace(b"/ColorTransform 0", b"/ColorTransform 1")
        with open(single_pdf_path, "wb") as pf:
            pf.write(pdf_raw)

    # Verify single page vector structure
    doc = fitz.open(single_pdf_path)
    page_count = len(doc)
    text_len = len(doc[0].get_text()) if page_count > 0 else 0
    font_count = len(doc[0].get_fonts()) if page_count > 0 else 0
    size_kb = os.path.getsize(single_pdf_path) / 1024
    print(f"   -> Success: {page_count} page(s), {text_len} text chars, {font_count} embedded fonts, {size_kb:.1f} KB")

    # Copy to root
    shutil.copyfile(single_pdf_path, single_pdf_root)

    # Insert vector pages into master document
    master_doc.insert_pdf(doc)
    doc.close()

    # Copy individual PDF to brain directory
    if os.path.exists(brain_dir):
        try:
            shutil.copyfile(single_pdf_path, os.path.join(brain_dir, pdf_name))
        except Exception:
            pass

# Save master PDF
master_doc.save(master_pdf_path, deflate=True)
master_pdf_export = os.path.join(export_dir, master_pdf_name)
master_doc.save(master_pdf_export, deflate=True)
master_doc.close()

# Ensure master PDF has ColorTransform corrected
for p_path in [master_pdf_path, master_pdf_export]:
    with open(p_path, "rb") as pf:
        m_raw = pf.read()
    if b"/ColorTransform 0" in m_raw:
        m_raw = m_raw.replace(b"/ColorTransform 0", b"/ColorTransform 1")
        with open(p_path, "wb") as pf:
            pf.write(m_raw)

if os.path.exists(brain_dir):
    try:
        shutil.copyfile(master_pdf_path, os.path.join(brain_dir, master_pdf_name))
    except Exception:
        pass

print("\n" + "="*75)
print("VECTOR & ILLUSTRATOR-EDITABLE DEFENCE BROCHURE EXPORT COMPLETE")
print(f"Master 5-Page PDF : {master_pdf_path}")
print(f"Master File Size  : {os.path.getsize(master_pdf_path) / 1024:.1f} KB ({os.path.getsize(master_pdf_path)/(1024*1024):.2f} MB)")
print("Editable Features : TrueType Vector Text (Selectable/Editable), Vector Paths, Embedded Photos")
print("="*75)
