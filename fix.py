import os, glob, re

# 1. Safely replace height: 100% with flex: 1
for f in glob.glob('pages/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('height: 100%;', 'flex: 1;')
    with open(f, 'w', encoding='utf-8') as out:
        out.write(content)

# 2. Fix page 13 recommended step & sub-breakdown box alignment
p13_path = 'pages/page_13.html'
with open(p13_path, 'r', encoding='utf-8') as file:
    p13 = file.read()
p13 = re.sub(r'<div class="rationale-note">.*?</div>', '', p13, flags=re.DOTALL)
p13 = p13.replace('justify-content: space-between;', 'justify-content: flex-start;\n      gap: 20px;')
with open(p13_path, 'w', encoding='utf-8') as out:
    out.write(p13)

# 3. Remove tarmac-hero-banner from page 09
p09_path = 'pages/page_09.html'
with open(p09_path, 'r', encoding='utf-8') as file:
    p09 = file.read()
p09 = re.sub(r'<div class="tarmac-hero-banner">.*?</div>', '', p09, flags=re.DOTALL)
with open(p09_path, 'w', encoding='utf-8') as out:
    out.write(p09)

# 4. Remove black frames from images in 01, 06, 07
def fix_frame(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We just explicitly strip the background/border lines that make frames
    content = content.replace('background: var(--bg-card);', 'background: transparent;')
    content = content.replace('border: 1px solid var(--border-medium);', '')
    content = content.replace('background: #080d0a;', 'background: transparent;')
    
    with open(file_path, 'w', encoding='utf-8') as out:
        out.write(content)

fix_frame('pages/page_01.html')
fix_frame('pages/page_06.html')
fix_frame('pages/page_07.html')
