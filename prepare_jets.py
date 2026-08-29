from PIL import Image
import numpy as np

def make_transparent(input_path, output_path, bg_thresh=18):
    img = Image.open(input_path).convert("RGBA")
    data = np.array(img)
    r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    # Crop out surrounding hud text margins
    h, w, _ = data.shape
    
    # Simple smooth alpha keying on dark pixels
    brightness = np.maximum(np.maximum(r, g), b)
    alpha = np.clip((brightness.astype(float) - 12) * 5, 0, 255).astype(np.uint8)
    
    data[:, :, 3] = alpha
    
    # Save cleaned sprite
    Image.fromarray(data).save(output_path, "PNG")
    print(f"Saved: {output_path}")

make_transparent("C:/Users/rohan/.gemini/antigravity-ide/brain/1fb1483e-678c-4201-b487-b4125cd57e4f/flir_su30_topdown_1788011150642.jpg", "maintenance-site/public/su30_flir.png")
make_transparent("C:/Users/rohan/.gemini/antigravity-ide/brain/1fb1483e-678c-4201-b487-b4125cd57e4f/flir_rafale_topdown_1788011168692.jpg", "maintenance-site/public/rafale_flir.png")
