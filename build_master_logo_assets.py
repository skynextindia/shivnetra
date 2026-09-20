import subprocess
import os
from PIL import Image

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
current_dir = os.path.dirname(os.path.abspath(__file__))
scratch_dir = os.path.join(current_dir, "scratch")
assets_dir = os.path.join(current_dir, "assets")

template_path = os.path.join(scratch_dir, "template_logo.html")
with open(template_path, "r", encoding="utf-8") as f:
    template_content = f.read()

for theme in ["dark", "light"]:
    theme_html_path = os.path.join(scratch_dir, f"render_logo_{theme}.html")
    with open(theme_html_path, "w", encoding="utf-8") as f:
        f.write(template_content.replace("THEME_CLASS", f"theme-{theme}"))
    
    out_raw = os.path.join(scratch_dir, f"logo_raw_{theme}.png")
    html_url = "file:///" + theme_html_path.replace("\\", "/")
    
    cmd = [
        edge,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--default-background-color=00000000",
        "--virtual-time-budget=4000",
        "--window-size=2000,1200",
        f"--screenshot={out_raw}",
        html_url
    ]
    subprocess.run(cmd)
    
    if os.path.exists(out_raw):
        im = Image.open(out_raw)
        # crop transparent border
        bbox = im.getbbox()
        pad = 20
        cropped = im.crop((
            max(0, bbox[0] - pad),
            max(0, bbox[1] - pad),
            min(im.width, bbox[2] + pad),
            min(im.height, bbox[3] + pad)
        ))
        
        target_path = os.path.join(assets_dir, f"shivnetra_logo_original_{theme}.png")
        cropped.save(target_path)
        print(f"Successfully rendered and saved {target_path} ({cropped.size})")
        
        if theme == "dark":
            cropped.save(os.path.join(assets_dir, "logo_white.png"))
            print("Also updated assets/logo_white.png")
        if theme == "light":
            cropped.save(os.path.join(assets_dir, "logo_original.png"))
            print("Also updated assets/logo_original.png")
