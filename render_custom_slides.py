import os
import subprocess

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge):
    edge = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

pages_dir = r"C:\Users\rohan\.gemini\antigravity-ide\scratch\shivnetra47_presentation\pages"
export_dir = r"C:\Users\rohan\.gemini\antigravity-ide\scratch\shivnetra47_presentation\exports"
brain_dir = r"C:\Users\rohan\.gemini\antigravity-ide\brain\d1cf8b9e-1677-4e8e-a002-656648141668\slides"

os.makedirs(export_dir, exist_ok=True)
os.makedirs(brain_dir, exist_ok=True)

print("Starting headless Edge rendering of all 13 customized HTML slides...")

for i in range(1, 14):
    pnum = f"{i:02d}"
    html_file = os.path.join(pages_dir, f"page_{pnum}.html")
    html_url = f"file:///{html_file.replace(os.sep, '/')}"
    out_png = os.path.join(export_dir, f"page_{pnum}.png")
    brain_png = os.path.join(brain_dir, f"page_{pnum}.png")
    
    cmd = [
        edge,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1920,1080",
        f"--screenshot={out_png}",
        html_url
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(out_png):
        sz = os.path.getsize(out_png)
        # Copy to brain slides
        with open(out_png, "rb") as f_in, open(brain_png, "wb") as f_out:
            f_out.write(f_in.read())
        print(f"Slide {pnum} rendered: {sz // 1024} KB")
    else:
        print(f"Slide {pnum} FAILED")

print("All 13 customized slides rendered and synced to viewer!")
