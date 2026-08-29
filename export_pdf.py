import os
import glob
from PIL import Image

def convert_slides_to_pdf(exports_dir="exports", output_pdf="SHIVNETRA47_Master_Slide_Deck.pdf"):
    png_files = sorted(glob.glob(os.path.join(exports_dir, "page_*.png")))
    if not png_files:
        print(f"No PNG files found in {exports_dir}")
        return
    
    images = []
    for f in png_files:
        img = Image.open(f).convert("RGB")
        images.append(img)
    
    # Save the images as a high-quality multi-page PDF
    images[0].save(
        output_pdf,
        save_all=True,
        append_images=images[1:],
        quality=95
    )
    print(f"Successfully generated {output_pdf} with {len(images)} slides ({os.path.getsize(output_pdf) / (1024*1024):.2f} MB)")

if __name__ == "__main__":
    convert_slides_to_pdf()
