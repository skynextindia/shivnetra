import glob, re

img_pattern = re.compile(r'<img[^>]+src=[\"\']([^\"\']+)[\"\'][^>]*>')

for f in sorted(glob.glob('pages/*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    imgs = [m for m in img_pattern.findall(content) if 'logo_white.png' not in m]
    
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content)
    title = title_match.group(1) if title_match else 'NO TITLE'
    
    print(f'{f}: {title}')
    print(f'  Images: {imgs}')
    
    layouts = re.findall(r'class=\"([^\"]*(?:layout|spread|box)[^\"]*)\"', content)
    print(f'  Layout classes: {layouts}')
    print('-'*40)
