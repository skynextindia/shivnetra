import glob, re
from collections import defaultdict

img_pattern = re.compile(r'<img[^>]+src=[\"\']([^\"\']+)[\"\'][^>]*>')
images = defaultdict(list)

for f in sorted(glob.glob('pages/*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    for match in img_pattern.findall(content):
        if 'logo_white.png' in match: continue
        images[f].append(match)

all_images = []
for f, imgs in images.items():
    print(f'{f}: {imgs}')
    all_images.extend(imgs)

print("\n--- Duplicates ---")
from collections import Counter
counts = Counter(all_images)
for img, count in counts.items():
    if count > 1:
        print(f"DUPLICATE {count}x: {img}")

print("\n--- Space Between Audit ---")
for f in sorted(glob.glob('pages/*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if 'justify-content: space-between;' in content:
        print(f"WARN: space-between found in {f}")

print("\n--- Recommended / Extra Additions Audit ---")
for f in sorted(glob.glob('pages/*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if re.search(r'recommend', content, re.IGNORECASE):
        print(f"WARN: 'recommend' found in {f}")
    if re.search(r'extra', content, re.IGNORECASE):
        print(f"WARN: 'extra' found in {f}")
