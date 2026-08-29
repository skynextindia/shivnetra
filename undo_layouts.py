import glob, re

for f in sorted(glob.glob('pages/*.html')):
    if 'page_01' in f or 'page_02' in f or 'page_03' in f or 'page_07' in f:
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
        
    # Extract original content from inside content-spread
    match = re.search(r'<!-- Right: Content Spread -->\s*<div class=\"content-spread\"[^>]*>\s*(.*?)\s*</div>\s*</div>\s*</main>', html, re.DOTALL)
    if not match:
        print(f'Could not find content-spread in {f}')
        continue
        
    original_content = match.group(1)
    
    # Restore the stripped layouts
    if 'page_06' in f:
        original_content = f'<div class=\"specs-layout\">\n        <div class=\"left-datasheet\">\n{original_content}\n        </div>\n      </div>'
    elif 'page_09' in f:
        original_content = f'<div class=\"infrastructure-layout\">\n        <div class=\"left-workstreams\">\n{original_content}\n        </div>\n      </div>'
    elif 'page_13' in f:
        original_content = f'<div class=\"budget-layout\">\n{original_content}\n      </div>'
    
    # Replace the whole brochure-layout with original content
    html = re.sub(r'<div class=\"brochure-layout\">\s*<!-- Left: Visual Spread -->.*?</div>\s*</div>\s*</main>', original_content + '\n    </main>', html, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)
        
    print(f'Restored {f}')
