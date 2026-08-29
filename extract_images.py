import fitz
import os

pdf_path = r'C:\Users\rohan\.gemini\antigravity-ide\brain\d1cf8b9e-1677-4e8e-a002-656648141668\.user_uploaded\media_1787922390494.pdf'
out_dir = r'C:\Users\rohan\.gemini\antigravity-ide\scratch\shivnetra47_presentation\assets\extracted_original'
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f'Total pages: {len(doc)}')

extracted = []
for page_num in range(len(doc)):
    page = doc[page_num]
    image_list = page.get_images(full=True)
    print(f'Page {page_num+1} has {len(image_list)} images')
    for img_idx, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image['image']
        image_ext = base_image['ext']
        w, h = base_image['width'], base_image['height']
        filename = f'page_{page_num+1:02d}_img_{img_idx}_{w}x{h}.{image_ext}'
        filepath = os.path.join(out_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(image_bytes)
        print(f'  Extracted: {filename} ({len(image_bytes)} bytes)')
        extracted.append(filename)

print(f'Total images extracted: {len(extracted)}')
