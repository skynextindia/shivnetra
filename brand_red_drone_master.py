import numpy as np
from PIL import Image, ImageDraw, ImageFont

def brand_red_drone():
    # 1. Load original red drone image
    src_path = 'new ref data/WhatsApp Image 2026-09-16 at 3.55.54 PM.jpeg'
    img = Image.open(src_path).convert('RGB')
    arr = np.array(img, dtype=np.float32)

    # 2. Inpaint the white "RIGITECH" logo
    # Box: y in [222, 255], x in [600, 712]
    y1, y2 = 222, 255
    x1, x2 = 600, 712

    # Logo pixels are white/pink (G + B > 125)
    sub = arr[y1:y2, x1:x2]
    logo_mask = (sub[:, :, 1] + sub[:, :, 2]) > 120

    # Dilate 1 px
    dil = logo_mask.copy()
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            dil |= np.roll(np.roll(logo_mask, dy, axis=0), dx, axis=1)

    # Clean red reference from top (y=218:221) and bottom (y=255:258)
    top_clean = arr[y1-3:y1, x1:x2].mean(axis=0) # (w, 3)
    bot_clean = arr[y2:y2+3, x1:x2].mean(axis=0) # (w, 3)
    
    h_box = y2 - y1
    y_weights = np.linspace(0, 1, h_box)[:, None, None]
    clean_red = (1.0 - y_weights) * top_clean[None, :, :] + y_weights * bot_clean[None, :, :]

    np.random.seed(42)
    clean_red += np.random.normal(0, 0.8, clean_red.shape)

    # Replace logo pixels
    sub_blended = np.where(dil[:, :, None], clean_red, sub)
    arr[y1:y2, x1:x2] = sub_blended

    arr = np.clip(arr, 0, 255).astype(np.uint8)
    base_img = Image.fromarray(arr).convert('RGBA')

    # 3. Load authentic original logo lockup (white pure)
    logo = Image.open('assets/logo_white_horizontal_hd.png')
    
    # Scale to fit red fuselage nicely (width ~ 145px)
    target_w = 145
    target_h = int(logo.height * (target_w / logo.width))
    logo_scaled = logo.resize((target_w, target_h), Image.LANCZOS)

    # Slight rotation to match red drone fuselage pitch (-2.2 deg)
    rotated_logo = logo_scaled.rotate(2.2, resample=Image.BICUBIC, expand=True)

    # Paste onto red fuselage
    paste_x = 582
    paste_y = 230
    base_img.alpha_composite(rotated_logo, (paste_x, paste_y))

    # Convert to RGB and save master asset
    final_rgb = base_img.convert('RGB')
    final_rgb.save('assets/real_red_vtol_shivnetra.jpg', quality=96)

    # Verification crop
    crop = final_rgb.crop((520, 180, 750, 290))
    crop.save('assets/crop_red_branded_verify.jpg')
    print("Successfully branded red drone with authentic original logo!")

if __name__ == '__main__':
    brand_red_drone()
