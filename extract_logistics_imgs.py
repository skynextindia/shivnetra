import pymupdf as fitz
import os

pdf = r'new ref data\SHIV_NETRA47_India_Made_Defence_Logistics_VTOL_BCN.pdf'
out_dir = r'assets\extracted_logistics'
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf)
print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    imgs = page.get_images()
    for idx, img in enumerate(imgs):
        xref = img[0]
        base = doc.extract_image(xref)
        ext = base['ext']
        w = base['width']
        h = base['height']
        fname = f"page{i+1:02d}_img{idx+1}_{w}x{h}.{ext}"
        fpath = os.path.join(out_dir, fname)
        with open(fpath, "wb") as f:
            f.write(base['image'])
        print(f"Page {i+1} saved: {fname} ({w}x{h}, {len(base['image'])/1024:.1f} KB)")
