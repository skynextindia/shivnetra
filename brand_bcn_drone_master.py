import numpy as np
from PIL import Image, ImageDraw, ImageFont

def brand_drone():
    # 1. Load pristine original flight photo
    img_path = 'assets/ref_training_bcn/p06_img1_1642x1095.jpeg'
    img = Image.open(img_path).convert('RGB')
    arr = np.array(img, dtype=np.float32)

    # 2. Flawless Curvilinear Inpaint of 'CAT UAV'
    canopy_edges = {}
    for x in range(1140, 1250):
        col = arr[488:505, x]
        lum = 0.299 * col[:, 0] + 0.587 * col[:, 1] + 0.114 * col[:, 2]
        diff = np.diff(lum)
        y_edge = 488 + np.argmax(diff) + 1
        canopy_edges[x] = y_edge

    x1, x2 = 1152, 1230
    np.random.seed(42)

    for x in range(x1, x2):
        y_c = canopy_edges[x]
        t = (x - x1) / (x2 - x1)
        for d in range(1, 23):
            y = y_c + d
            if y >= 1095:
                continue
            ref_l = arr[canopy_edges[x1 - 2] + d, x1 - 2]
            ref_r = arr[canopy_edges[x2 + 2] + d, x2 + 2]
            ref_val = (1.0 - t) * ref_l + t * ref_r
            ref_lum = 0.299 * ref_val[0] + 0.587 * ref_val[1] + 0.114 * ref_val[2]
            cur_lum = 0.299 * arr[y, x, 0] + 0.587 * arr[y, x, 1] + 0.114 * arr[y, x, 2]
            if ref_lum - cur_lum > 3.0:
                arr[y, x] = ref_val + np.random.normal(0, 0.35, 3)

    base_clean = np.clip(arr, 0, 255).astype(np.uint8)

    # 3. Create High-Resolution Engineered Insignia (at 2x supersampling)
    scale = 2
    w_2x = 380
    h_2x = 64
    layer_2x = Image.new('RGBA', (w_2x, h_2x), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer_2x)

    font = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 28)

    brand_rgb_top = (35, 48, 66)
    brand_rgb_bot = (22, 34, 50)
    brand_text_rgb = (26, 38, 56)

    # Delta Arrowhead with 3D Center Crease (pointing forward/right toward nose tip)
    tip_x, tip_y = 52, 26
    top_x, top_y = 12, 10
    notch_x, notch_y = 26, 26
    bot_x, bot_y = 12, 42

    draw.polygon([(tip_x, tip_y), (top_x, top_y), (notch_x, notch_y)], fill=brand_rgb_top + (255,))
    draw.polygon([(tip_x, tip_y), (notch_x, notch_y), (bot_x, bot_y)], fill=brand_rgb_bot + (255,))
    draw.line([(tip_x, tip_y), (notch_x, notch_y)], fill=(16, 24, 38, 255), width=2)
    draw.polygon([(tip_x, tip_y), (top_x, top_y), (notch_x, notch_y), (bot_x, bot_y)], outline=(18, 26, 40, 255), width=1)

    # Official hyphenated brand name: 'SHIV-NETRA 47'
    text_x = 66
    text_y = 12
    text_str = 'SHIV-NETRA 47'
    draw.text((text_x, text_y), text_str, fill=brand_text_rgb + (255,), font=font)

    bbox_full = font.getbbox(text_str)
    bbox_shiv = font.getbbox('SHIV-')
    w_shiv = bbox_shiv[2] - bbox_shiv[0]

    # Tricolor Bar positioned neatly under NETRA 47
    tri_start_x = text_x + w_shiv + 12
    tri_y = text_y + (bbox_full[3] - bbox_full[1]) + 5
    tri_h = 5
    seg_w = 20
    gap = 3

    # Saffron segment
    draw.rectangle([tri_start_x, tri_y, tri_start_x + seg_w, tri_y + tri_h], fill=(255, 153, 51, 245))
    # White segment with crisp subtle border
    draw.rectangle([tri_start_x + seg_w + gap, tri_y, tri_start_x + 2 * seg_w + gap, tri_y + tri_h],
                   fill=(248, 250, 252, 245), outline=(150, 165, 180, 210), width=1)
    # India Green segment
    draw.rectangle([tri_start_x + 2 * seg_w + 2 * gap, tri_y, tri_start_x + 3 * seg_w + 2 * gap, tri_y + tri_h], fill=(19, 136, 8, 245))

    # Downsample with Lanczos for sub-pixel anti-aliasing
    layer_1x = layer_2x.resize((w_2x // scale, h_2x // scale), Image.Resampling.LANCZOS)

    # Rotate 3.4 degrees to match canopy slope and aerodynamic waterline
    rotated_brand = layer_1x.rotate(3.4, resample=Image.BICUBIC, expand=True)

    # 4. Composite onto side nose cheek with realistic physical lighting & grain
    img_clean = Image.fromarray(base_clean).convert('RGBA')
    decal_canvas = Image.new('RGBA', img_clean.size, (0, 0, 0, 0))
    paste_x, paste_y = 1130, 502
    decal_canvas.paste(rotated_brand, (paste_x, paste_y), rotated_brand)

    decal_arr = np.array(decal_canvas, dtype=np.float32)
    alpha = decal_arr[:, :, 3:4] / 255.0

    fuse_arr = np.array(img_clean, dtype=np.float32)[:, :, :3]
    fuse_lum = 0.299 * fuse_arr[:, :, 0:1] + 0.587 * fuse_arr[:, :, 1:2] + 0.114 * fuse_arr[:, :, 2:3]
    lum_factor = np.clip((fuse_lum / 168.0) ** 0.75, 0.82, 1.12)

    paint_rgb = decal_arr[:, :, :3] * lum_factor
    np.random.seed(123)
    noise = np.random.normal(0, 0.45, paint_rgb.shape)
    paint_rgb = np.clip(paint_rgb + noise, 0, 255)

    final_blended = (1.0 - alpha) * fuse_arr + alpha * paint_rgb
    final_blended = np.clip(final_blended, 0, 255).astype(np.uint8)

    final_rgb = Image.fromarray(final_blended)

    # Save to all target files
    final_rgb.save('assets/real_bcn_vtol_shivnetra.jpg', quality=96)
    final_rgb.save('assets/real_bcn_vtol_shivnetra.png')
    final_rgb.save('assets/real_bcn_vtol_branded.jpg', quality=96)
    final_rgb.save('assets/real_bcn_vtol_shivnetra_opt.jpg', quality=94)

    # Verification crop
    crop_verif = final_rgb.crop((1080, 460, 1330, 565))
    crop_verif.save('assets/crop_bcn_branded_verify.jpg')
    print("Flawlessly generated engineered livery on assets/real_bcn_vtol_shivnetra.jpg")

if __name__ == '__main__':
    brand_drone()

