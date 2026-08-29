import glob, re

pages_to_images = {
    'pages/page_04.html': ('hero_vtol_cityscape.png', 'SHIVNETRA47 Vision & Strategy'),
    'pages/page_05.html': ('full_uncropped_workflow.png', 'System Architecture & Operations'),
    'pages/page_06.html': ('nano_uav.jpg', 'Nano UAV Swarm Node'),
    'pages/page_08.html': ('gcs_console.jpg', 'In-House Engineering Ecosystem'),
    'pages/page_09.html': ('source_workflow_panel.png', 'Industrial Production Line'),
    'pages/page_10.html': ('orig_system_overview_6.jpg', 'Flight Test & Validation'),
    'pages/page_11.html': ('clean_sys_diagram_24.png', 'Deliverables & Logistics'),
    'pages/page_12.html': ('source_key_capabilities.png', 'Execution Strategy'),
    'pages/page_13.html': ('source_sys_overview_6_clean.png', 'Financial Framework')
}

for page_path, (img_name, img_alt) in pages_to_images.items():
    with open(page_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Special handling for page 06
    if 'page_06' in page_path:
        # Wrap everything after page-title-row inside a new brochure-layout
        match = re.search(r'<main class=\"slide-body\">\s*<div class=\"page-title-row\"[^\n]*\n[^\n]*\n[^\n]*\n[^\n]*\n\s*</div>', html)
        if match:
            start_idx = match.end()
            end_match = re.search(r'</main>', html)
            end_idx = end_match.start()
            original_content = html[start_idx:end_idx]
            
            # extract only the left-datasheet content
            left_match = re.search(r'<div class=\"left-datasheet\">(.*?)</div>\s*<!-- Right:', original_content, re.DOTALL)
            if left_match:
                extracted = left_match.group(1)
            else:
                extracted = original_content
                
            new_content = f'''
      <div class="brochure-layout">
        <!-- Left: Visual Spread -->
        <div class="visual-spread" style="flex: 1.3; min-height: 0;">
          <div class="hero-photo-box" style="flex: 1; min-height: 0;">
            <img src="../assets/{img_name}" alt="{img_alt}">
            <div class="photo-tag">{img_alt.upper()}</div>
          </div>
        </div>
        
        <!-- Right: Content Spread -->
        <div class="content-spread" style="flex: 1; justify-content: flex-start; gap: 24px; padding-left: 12px; min-height: 0;">
          {extracted.strip()}
        </div>
      </div>
      '''
            html = html[:start_idx] + new_content + html[end_idx:]

    elif 'page_09' in page_path:
        match = re.search(r'<main class=\"slide-body\">\s*<div class=\"page-title-row\"[^\n]*\n[^\n]*\n[^\n]*\n[^\n]*\n\s*</div>', html)
        if match:
            start_idx = match.end()
            end_match = re.search(r'</main>', html)
            end_idx = end_match.start()
            original_content = html[start_idx:end_idx]
            
            # extract only the left-workstreams
            left_match = re.search(r'<div class=\"left-workstreams\">(.*?)</div>\s*</div>', original_content, re.DOTALL)
            if left_match:
                extracted = left_match.group(1)
            else:
                extracted = original_content

            new_content = f'''
      <div class="brochure-layout">
        <!-- Left: Visual Spread -->
        <div class="visual-spread" style="flex: 1.3; min-height: 0;">
          <div class="hero-photo-box" style="flex: 1; min-height: 0;">
            <img src="../assets/{img_name}" alt="{img_alt}">
            <div class="photo-tag">{img_alt.upper()}</div>
          </div>
        </div>
        
        <!-- Right: Content Spread -->
        <div class="content-spread" style="flex: 1; justify-content: flex-start; gap: 24px; padding-left: 12px; min-height: 0;">
          {extracted.strip()}
        </div>
      </div>
      '''
            html = html[:start_idx] + new_content + html[end_idx:]

    else:
        # General case
        match = re.search(r'<main class=\"slide-body\">\s*<div class=\"page-title-row\"[^\n]*\n[^\n]*\n[^\n]*\n[^\n]*\n\s*</div>', html)
        if match:
            start_idx = match.end()
            end_match = re.search(r'</main>', html)
            end_idx = end_match.start()
            original_content = html[start_idx:end_idx]
            
            # Strip out outer layout divs if they exist to prevent double wrapping
            original_content = re.sub(r'^\s*<div class=\"[a-z-]+-layout\">\s*', '', original_content)
            original_content = re.sub(r'\s*</div>\s*$', '', original_content)

            new_content = f'''
      <div class="brochure-layout">
        <!-- Left: Visual Spread -->
        <div class="visual-spread" style="flex: 1.3; min-height: 0;">
          <div class="hero-photo-box" style="flex: 1; min-height: 0;">
            <img src="../assets/{img_name}" alt="{img_alt}">
            <div class="photo-tag">{img_alt.upper()}</div>
          </div>
        </div>
        
        <!-- Right: Content Spread -->
        <div class="content-spread" style="flex: 1; justify-content: flex-start; gap: 24px; padding-left: 12px; min-height: 0; overflow-y: auto;">
          {original_content.strip()}
        </div>
      </div>
      '''
            html = html[:start_idx] + new_content + html[end_idx:]

    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(html)
