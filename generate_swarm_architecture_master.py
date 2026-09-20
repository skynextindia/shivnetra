import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

def build_seamless_swarm_architecture():
    W, H = 2400, 1100
    
    # 1. Base deep aerospace dark navy: #071226 (matches brochure container background)
    # Subtle radial gradient for aerospace depth
    yy, xx = np.mgrid[0:H, 0:W]
    dist = np.sqrt(((xx - 1200) / 1.6)**2 + (yy - 540)**2)
    glow = np.clip(1.0 - (dist / 1100.0), 0.0, 1.0)
    
    r = 5.0 + 9.0 * glow
    g = 12.0 + 18.0 * glow
    b = 26.0 + 36.0 * glow
    
    bg = np.dstack([r, g, b, np.full((H, W), 255.0)]).astype(np.uint8)
    canvas = Image.fromarray(bg)
    draw = ImageDraw.Draw(canvas, 'RGBA')
    
    # 2. Fine Tactical Blueprint Grid
    grid_sz = 60
    for x in range(0, W, grid_sz):
        draw.line([(x, 0), (x, H)], fill=(56, 189, 248, 15), width=1)
    for y in range(0, H, grid_sz):
        draw.line([(0, y), (W, y)], fill=(56, 189, 248, 15), width=1)
        
    # Crosshairs at grid intersections
    for x in range(120, W, grid_sz * 3):
        for y in range(120, H, grid_sz * 3):
            draw.line([(x - 6, y), (x + 6, y)], fill=(56, 189, 248, 50), width=1)
            draw.line([(x, y - 6), (x, y + 6)], fill=(56, 189, 248, 50), width=1)

    # 3. Concentric Radar / Datalink Range Rings (Centered at Antenna: x=1120, y=580)
    cx, cy = 1120, 580
    for rad in [150, 290, 440, 600]:
        draw.ellipse([cx - rad, cy - rad, cx + rad, cy + rad],
                     outline=(56, 189, 248, 24), width=1)
                     
    # Load fonts
    try:
        font_hdr = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 24)
        font_node_title = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 32)
        font_node_sub = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 24)
        font_badge = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 16)
        font_desc = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 17)
        font_mono = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 14)
    except:
        font_hdr = font_node_title = font_node_sub = font_badge = font_desc = font_mono = ImageFont.load_default()
        
    # Range labels
    draw.text((cx + 155, cy - 10), "50 KM RANGE", fill=(56, 189, 248, 75), font=font_mono)
    draw.text((cx + 295, cy - 10), "100 KM RANGE", fill=(56, 189, 248, 75), font=font_mono)
    draw.text((cx + 445, cy - 10), "150 KM RANGE", fill=(56, 189, 248, 75), font=font_mono)

    # 4. Outer Defense HUD Border & Telemetry
    draw.rectangle([24, 24, W - 24, H - 24], outline=(56, 189, 248, 60), width=1)
    
    # Corner brackets
    c_len = 36
    for ox, oy, dx, dy in [(24, 24, 1, 1), (W - 24, 24, -1, 1), (24, H - 24, 1, -1), (W - 24, H - 24, -1, -1)]:
        draw.line([(ox, oy), (ox + dx * c_len, oy)], fill=(56, 189, 248, 240), width=3)
        draw.line([(ox, oy), (ox, oy + dy * c_len)], fill=(56, 189, 248, 240), width=3)
        
    # Top Status Ribbon
    draw.rectangle([24, 24, W - 24, 76], fill=(3, 10, 24, 230), outline=(56, 189, 248, 60), width=1)
    draw.text((50, 36), "SYSTEM OVERVIEW // MULTI-TIER C2 & AUTONOMOUS SWARM TOPOLOGY", fill=(255, 255, 255), font=font_hdr)
    
    # Status badges on top right
    draw.rectangle([W - 620, 33, W - 45, 67], fill=(255, 153, 51, 25), outline=(255, 153, 51, 120), width=1)
    draw.text((W - 605, 41), "AUTHENTIC BCN ARCHITECTURE • 24-NODE MANET MESH", fill=(255, 175, 75), font=font_badge)

    # Bottom Telemetry Ribbon
    draw.text((50, H - 55), "ENCRYPTION: AES-256 GCM  |  MANET DUAL-BAND: 1.4 GHz / 2.4 GHz  |  FAIL-OVER: DUAL AUTONOMOUS RELAY  |  SWARM LATENCY: <85ms", 
              fill=(56, 189, 248, 150), font=font_mono)

    # 5. COMPONENT 1: OVERWATCH UAV (TOP-LEFT)
    ov_x, ov_y = 70, 110
    draw.text((ov_x, ov_y), "OVERWATCH UAV (1 UNIT)", fill=(255, 255, 255), font=font_node_title)
    
    # Badge
    draw.rectangle([ov_x, ov_y + 44, ov_x + 280, ov_y + 72], fill=(56, 189, 248, 30), outline=(56, 189, 248, 140), width=1)
    draw.text((ov_x + 12, ov_y + 49), "AIRBORNE C2 RELAY & DIRECTOR", fill=(56, 189, 248), font=font_badge)
    draw.text((ov_x, ov_y + 82), "High-Altitude Relay Backbone • 150 km MANET Datalink • Swarm Director", fill=(190, 210, 230), font=font_desc)
    
    # Place Clean VTOL Drone
    try:
        vtol_img = Image.open('assets/clean_orig_vtol_perfect.png').convert('RGBA')
        # Slightly brighten and boost contrast
        enhancer = ImageEnhance.Contrast(vtol_img)
        vtol_img = enhancer.enhance(1.15)
        enhancer_b = ImageEnhance.Brightness(vtol_img)
        vtol_img = enhancer_b.enhance(1.1)
        
        vw = 540
        vh = int(vtol_img.height * (vw / vtol_img.width))
        vtol_resized = vtol_img.resize((vw, vh), Image.LANCZOS)
        canvas.paste(vtol_resized, (ov_x + 10, ov_y + 115), vtol_resized)
    except Exception as e:
        print("VTOL paste error:", e)

    # 6. COMPONENT 2: NANO-UAV SWARM (BOTTOM-LEFT)
    sw_x, sw_y = 70, 560
    draw.text((sw_x, sw_y), "NANO-UAV SWARM (24+ UNITS)", fill=(255, 255, 255), font=font_node_title)
    
    # Badge
    draw.rectangle([sw_x, sw_y + 44, sw_x + 295, sw_y + 72], fill=(255, 153, 51, 30), outline=(255, 153, 51, 160), width=1)
    draw.text((sw_x + 12, sw_y + 49), "AUTONOMOUS SATURATION GRID", fill=(255, 175, 75), font=font_badge)
    draw.text((sw_x, sw_y + 82), "24 Coordinated Micro-UAVs • Anti-Jam Mesh • Perimeter Reconnaissance", fill=(190, 210, 230), font=font_desc)
    
    # Place Swarm 24-drone grid
    try:
        swarm_img = Image.open('assets/part_swarm_trans.png').convert('RGBA')
        sw_w, sw_h = swarm_img.size
        swarm_img = swarm_img.crop((0, 0, sw_w, min(165, sw_h)))
        
        # Boost brightness and contrast of the swarm drones so they pop against dark navy
        enhancer_c = ImageEnhance.Contrast(swarm_img)
        swarm_img = enhancer_c.enhance(1.25)
        enhancer_b = ImageEnhance.Brightness(swarm_img)
        swarm_img = enhancer_b.enhance(1.35)
        
        target_sw_w = 600
        target_sw_h = int(swarm_img.height * (target_sw_w / swarm_img.width))
        swarm_resized = swarm_img.resize((target_sw_w, target_sw_h), Image.LANCZOS)
        
        # Draw micro mesh grid behind the swarm nodes
        grid_origin_x, grid_origin_y = sw_x + 10, sw_y + 130
        rows, cols = 4, 6
        
        for r_i in range(rows):
            for c_i in range(cols):
                px = int(grid_origin_x + (c_i + 0.5) * (target_sw_w / cols))
                py = int(grid_origin_y + (r_i + 0.5) * (target_sw_h / rows))
                if c_i < cols - 1:
                    nx = int(grid_origin_x + (c_i + 1.5) * (target_sw_w / cols))
                    draw.line([(px, py), (nx, py)], fill=(56, 189, 248, 55), width=1)
                if r_i < rows - 1:
                    ny = int(grid_origin_y + (r_i + 1.5) * (target_sw_h / rows))
                    draw.line([(px, py), (px, ny)], fill=(56, 189, 248, 55), width=1)

        canvas.paste(swarm_resized, (grid_origin_x, grid_origin_y), swarm_resized)
        
        # Add subtle glowing cyan dots at drone optical sensor locations
        for r_i in range(rows):
            for c_i in range(cols):
                px = int(grid_origin_x + (c_i + 0.5) * (target_sw_w / cols))
                py = int(grid_origin_y + (r_i + 0.5) * (target_sw_h / rows) + 3)
                draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(56, 189, 248, 220))
    except Exception as e:
        print("Swarm paste error:", e)

    # 7. COMPONENT 3: SECURE DATA LINK (CENTER)
    dl_x, dl_y = 920, 160
    draw.text((dl_x, dl_y), "SECURE DATA LINK", fill=(255, 255, 255), font=font_node_title)
    draw.text((dl_x, dl_y + 42), "(MESH NETWORK)", fill=(56, 189, 248), font=font_node_sub)
    
    draw.rectangle([dl_x, dl_y + 85, dl_x + 265, dl_y + 113], fill=(56, 189, 248, 30), outline=(56, 189, 248, 140), width=1)
    draw.text((dl_x + 12, dl_y + 90), "AES-256 MANET ENCRYPTION", fill=(56, 189, 248), font=font_badge)
    draw.text((dl_x, dl_y + 124), "Tactical Frequency Hopping • Dual 1.4 / 2.4 GHz", fill=(190, 210, 230), font=font_desc)

    # Central Transmission Tower Graphic (x=1120, y=580)
    tx, ty = 1120, 580
    
    # Glowing RF electromagnetic waves radiating outwards
    for rad in [45, 75, 110, 150]:
        alpha_val = int(240 - rad * 1.2)
        # Left arcs
        draw.arc([tx - rad, ty - rad, tx + rad, ty + rad], start=125, end=235, fill=(56, 189, 248, alpha_val), width=3)
        # Right arcs
        draw.arc([tx - rad, ty - rad, tx + rad, ty + rad], start=-55, end=55, fill=(56, 189, 248, alpha_val), width=3)
        
    # Tower Mast
    draw.line([(tx, ty - 70), (tx, ty + 60)], fill=(56, 189, 248, 255), width=4)
    # Triangular Base
    draw.polygon([(tx - 35, ty + 90), (tx + 35, ty + 90), (tx, ty + 30)], 
                 outline=(56, 189, 248, 240), fill=(10, 35, 75, 230), width=2)
    # Cross Struts
    draw.line([(tx - 20, ty + 60), (tx + 20, ty + 60)], fill=(56, 189, 248, 210), width=2)
    # Transmitter tip glowing beacon
    draw.ellipse([tx - 15, ty - 84, tx + 15, ty - 54], fill=(56, 189, 248, 255), outline=(255, 255, 255), width=2)
    draw.ellipse([tx - 6, ty - 75, tx + 6, ty - 63], fill=(255, 255, 255, 255))

    # 8. COMPONENT 4: GROUND CONTROL STATION (RIGHT)
    gcs_x, gcs_y = 1570, 110
    draw.text((gcs_x, gcs_y), "GROUND CONTROL STATION", fill=(255, 255, 255), font=font_node_title)
    draw.text((gcs_x, gcs_y + 42), "(Command, Control & Analysis)", fill=(56, 189, 248), font=font_node_sub)
    
    draw.rectangle([gcs_x, gcs_y + 85, gcs_x + 360, gcs_y + 113], fill=(56, 189, 248, 30), outline=(56, 189, 248, 140), width=1)
    draw.text((gcs_x + 12, gcs_y + 90), "MIL-STD RUGGED DUAL-SCREEN BRIEFCASE", fill=(56, 189, 248), font=font_badge)
    draw.text((gcs_x, gcs_y + 124), "Multi-UAV Mission Planning • HD Video Streams • AI Telemetry Fusion", fill=(190, 210, 230), font=font_desc)

    # Place GCS Hardware Photo
    try:
        gcs_img = Image.open('assets/gcs_clean_isolated.png').convert('RGBA')
        gw = 720
        gh = int(gcs_img.height * (gw / gcs_img.width))
        gcs_resized = gcs_img.resize((gw, gh), Image.LANCZOS)
        canvas.paste(gcs_resized, (gcs_x + 15, gcs_y + 190), gcs_resized)
    except Exception as e:
        print("GCS paste error:", e)

    # 9. VECTOR DATALINK TELEMETRY PATHWAYS (DASHED ARROWS WITH GLOW)
    def draw_dashed_vector(p1, p2, color=(56, 189, 248, 240), width=3, dash_len=14, gap_len=9, arrow=True):
        x1, y1 = p1
        x2, y2 = p2
        length = math.hypot(x2 - x1, y2 - y1)
        if length == 0:
            return
        dx = (x2 - x1) / length
        dy = (y2 - y1) / length
        
        curr = 0
        while curr < length - (18 if arrow else 0):
            seg_start = curr
            seg_end = min(curr + dash_len, length - (18 if arrow else 0))
            sx1 = x1 + dx * seg_start
            sy1 = y1 + dy * seg_start
            sx2 = x1 + dx * seg_end
            sy2 = y1 + dy * seg_end
            draw.line([(sx1, sy1), (sx2, sy2)], fill=color, width=width)
            curr += dash_len + gap_len
            
        if arrow:
            ah_len = 16
            ah_w = 7
            base_x = x2 - dx * ah_len
            base_y = y2 - dy * ah_len
            perp_x = -dy * ah_w
            perp_y = dx * ah_w
            draw.polygon([(x2, y2), (base_x + perp_x, base_y + perp_y), (base_x - perp_x, base_y - perp_y)], fill=color)

    # Vector 1: Overwatch UAV <===> Data Link Mesh Hub (Bidirectional)
    draw_dashed_vector((630, 275), (960, 500), color=(56, 189, 248, 240), width=3, arrow=True)
    draw_dashed_vector((960, 518), (630, 293), color=(56, 189, 248, 240), width=3, arrow=True)
    
    # Vector 2: Data Link Mesh Hub <===> Ground Control Station (Bidirectional)
    # Stop before the GCS left bezel at x=1560
    draw_dashed_vector((1280, 570), (1555, 570), color=(56, 189, 248, 240), width=3, arrow=True)
    draw_dashed_vector((1555, 588), (1280, 588), color=(56, 189, 248, 240), width=3, arrow=True)
    
    # Vector 3: Swarm Nodes <===> Data Link Mesh Hub (Bidirectional)
    draw_dashed_vector((690, 770), (960, 650), color=(56, 189, 248, 240), width=3, arrow=True)
    draw_dashed_vector((960, 668), (690, 788), color=(56, 189, 248, 240), width=3, arrow=True)

    # Vector 4: Vertical Direct C2 Control (Overwatch UAV directly down to Swarm Grid)
    draw_dashed_vector((350, 420), (350, 545), color=(255, 175, 75, 240), width=3, arrow=True)
    draw_dashed_vector((375, 545), (375, 420), color=(255, 175, 75, 240), width=3, arrow=True)
    draw.text((390, 470), "AIRBORNE C2", fill=(255, 175, 75), font=font_mono)

    # Save to assets
    out_path = 'assets/swarm_architecture_blue_master.png'
    canvas.save(out_path, 'PNG', quality=100)
    print(f"Master graphic successfully built and saved to {out_path} ({W}x{H})")

if __name__ == '__main__':
    build_seamless_swarm_architecture()
