import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_machine_infographic():
    W, H = 2400, 1100
    
    # 1. Base deep aerospace navy background: #071226
    canvas = Image.new('RGBA', (W, H), (7, 18, 38, 255))
    
    # Subtle radial aerospace glow
    yy, xx = np.mgrid[0:H, 0:W]
    dist = np.sqrt(((xx - 1200) / 1.7)**2 + (yy - 550)**2)
    glow = np.clip(1.0 - (dist / 1100.0), 0.0, 1.0)
    
    r = 5.0 + 8.0 * glow
    g = 12.0 + 16.0 * glow
    b = 26.0 + 34.0 * glow
    bg = np.dstack([r, g, b, np.full((H, W), 255.0)]).astype(np.uint8)
    canvas = Image.fromarray(bg)
    draw = ImageDraw.Draw(canvas, 'RGBA')
    
    # 2. Engineering Blueprint Grid
    grid_sz = 60
    for x in range(0, W, grid_sz):
        draw.line([(x, 0), (x, H)], fill=(56, 189, 248, 14), width=1)
    for y in range(0, H, grid_sz):
        draw.line([(0, y), (W, y)], fill=(56, 189, 248, 14), width=1)
        
    # Crosshairs at major intersections
    for x in range(120, W, grid_sz * 3):
        for y in range(120, H, grid_sz * 3):
            draw.line([(x - 6, y), (x + 6, y)], fill=(56, 189, 248, 45), width=1)
            draw.line([(x, y - 6), (x, y + 6)], fill=(56, 189, 248, 45), width=1)

    # 3. Radar & MANET Range Concentric Rings (Centered at RF Hub: x=1180, y=550)
    cx, cy = 1180, 550
    for rad in [160, 310, 470, 640]:
        draw.ellipse([cx - rad, cy - rad, cx + rad, cy + rad],
                     outline=(56, 189, 248, 22), width=1)
                     
    # Load Fonts
    try:
        font_main_hdr = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 24)
        font_sec_hdr = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 16)
        font_node_title = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 30)
        font_node_sub = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 22)
        font_badge = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 15)
        font_desc = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 16)
        font_mono = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 14)
        font_callout = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 13)
    except:
        font_main_hdr = font_sec_hdr = font_node_title = font_node_sub = font_badge = font_desc = font_mono = font_callout = ImageFont.load_default()

    # Range Labels
    draw.text((cx + 170, cy - 10), "50 KM RELAY", fill=(56, 189, 248, 80), font=font_mono)
    draw.text((cx + 320, cy - 10), "100 KM RELAY", fill=(56, 189, 248, 80), font=font_mono)
    draw.text((cx + 480, cy - 10), "150 KM RELAY", fill=(56, 189, 248, 80), font=font_mono)

    # 4. Outer Technical HUD Frame
    draw.rectangle([24, 24, W - 24, H - 24], outline=(56, 189, 248, 60), width=1)
    
    # Corner brackets
    c_len = 38
    for ox, oy, dx, dy in [(24, 24, 1, 1), (W - 24, 24, -1, 1), (24, H - 24, 1, -1), (W - 24, H - 24, -1, -1)]:
        draw.line([(ox, oy), (ox + dx * c_len, oy)], fill=(56, 189, 248, 240), width=3)
        draw.line([(ox, oy), (ox, oy + dy * c_len)], fill=(56, 189, 248, 240), width=3)
        
    # Top Status Ribbon
    draw.rectangle([24, 24, W - 24, 76], fill=(3, 10, 24, 230), outline=(56, 189, 248, 60), width=1)
    draw.text((50, 36), "SYSTEM OVERVIEW // MULTI-TIER C2 & AUTONOMOUS SWARM INFOGRAPHIC", fill=(255, 255, 255), font=font_main_hdr)
    
    draw.rectangle([W - 640, 33, W - 45, 67], fill=(255, 153, 51, 25), outline=(255, 153, 51, 120), width=1)
    draw.text((W - 625, 41), "ENGINEERING BLUEPRINT • 24-NODE AUTONOMOUS MESH", fill=(255, 175, 75), font=font_badge)

    # Bottom Telemetry Ribbon
    draw.text((50, H - 55), "ENCRYPTION: AES-256 GCM  |  MANET DUAL-BAND: 1.4 GHz / 2.4 GHz  |  FAIL-OVER: DUAL AUTONOMOUS RELAY  |  SWARM LATENCY: <85ms", 
              fill=(56, 189, 248, 160), font=font_mono)

    # 5. COMPONENT 1: OVERWATCH UAV (TOP-LEFT) - IN MACHINE CAD BLUEPRINT STYLE
    ov_x, ov_y = 70, 105
    draw.text((ov_x, ov_y), "OVERWATCH UAV (1 UNIT)", fill=(255, 255, 255), font=font_node_title)
    
    # Badge
    draw.rectangle([ov_x, ov_y + 42, ov_x + 290, ov_y + 70], fill=(56, 189, 248, 30), outline=(56, 189, 248, 140), width=1)
    draw.text((ov_x + 12, ov_y + 47), "AIRBORNE C2 RELAY & DIRECTOR", fill=(56, 189, 248), font=font_badge)
    draw.text((ov_x, ov_y + 80), "High-Altitude Relay Backbone • 150 km C2 MANET • Autonomous Mission Commander", fill=(190, 210, 230), font=font_desc)
    
    # Place Glowing Cyan CAD Machine Wireframe
    try:
        cad = Image.open('assets/vtol_cad_white_lines.png').convert('RGBA')
        c_arr = np.array(cad)
        alpha = c_arr[:,:,3].astype(float) / 255.0
        
        cyan_cad = np.zeros_like(c_arr)
        cyan_cad[:,:,0] = (56 * alpha).astype(np.uint8)
        cyan_cad[:,:,1] = (189 * alpha).astype(np.uint8)
        cyan_cad[:,:,2] = (248 * alpha).astype(np.uint8)
        cyan_cad[:,:,3] = (c_arr[:,:,3] * 0.95).astype(np.uint8)
        
        cad_img = Image.fromarray(cyan_cad)
        cw = 600
        ch = int(cad_img.height * (cw / cad_img.width))
        cad_resized = cad_img.resize((cw, ch), Image.LANCZOS)
        
        vtol_pos_x, vtol_pos_y = ov_x + 30, ov_y + 115
        canvas.paste(cad_resized, (vtol_pos_x, vtol_pos_y), cad_resized)
        
        # Technical Subsystem Callouts with clean non-overlapping leader lines
        # Callout 1: Quick-Disconnect Wing
        draw.line([(vtol_pos_x + 120, vtol_pos_y + 110), (vtol_pos_x + 70, vtol_pos_y + 35), (vtol_pos_x + 5, vtol_pos_y + 35)], fill=(56, 189, 248, 200), width=1)
        draw.ellipse([vtol_pos_x + 118, vtol_pos_y + 108, vtol_pos_x + 122, vtol_pos_y + 112], fill=(56, 189, 248, 255))
        draw.text((vtol_pos_x + 5, vtol_pos_y + 18), "LRU-01 // QUICK-DISCONNECT WING", fill=(56, 189, 248), font=font_callout)
        
        # Callout 2: AI Mission Computer & Avionics Core
        draw.line([(vtol_pos_x + 250, vtol_pos_y + 105), (vtol_pos_x + 250, vtol_pos_y + 35), (vtol_pos_x + 310, vtol_pos_y + 35)], fill=(56, 189, 248, 200), width=1)
        draw.ellipse([vtol_pos_x + 248, vtol_pos_y + 103, vtol_pos_x + 252, vtol_pos_y + 107], fill=(56, 189, 248, 255))
        draw.text((vtol_pos_x + 315, vtol_pos_y + 20), "LRU-02/03 // TRIPLE AHRS & AI CORE", fill=(56, 189, 248), font=font_callout)

        # Callout 3: Hybrid Vertical Lift Motor & Prop
        draw.line([(vtol_pos_x + 430, vtol_pos_y + 90), (vtol_pos_x + 480, vtol_pos_y + 55), (vtol_pos_x + 550, vtol_pos_y + 55)], fill=(255, 175, 75, 200), width=1)
        draw.ellipse([vtol_pos_x + 428, vtol_pos_y + 88, vtol_pos_x + 432, vtol_pos_y + 92], fill=(255, 175, 75, 255))
        draw.text((vtol_pos_x + 490, vtol_pos_y + 40), "4x HYBRID LIFT ROTORS", fill=(255, 175, 75), font=font_callout)

        # Callout 4: High-Efficiency Pusher Propulsion
        draw.line([(vtol_pos_x + 350, vtol_pos_y + 155), (vtol_pos_x + 400, vtol_pos_y + 205), (vtol_pos_x + 480, vtol_pos_y + 205)], fill=(56, 189, 248, 200), width=1)
        draw.ellipse([vtol_pos_x + 348, vtol_pos_y + 153, vtol_pos_x + 352, vtol_pos_y + 157], fill=(56, 189, 248, 255))
        draw.text((vtol_pos_x + 410, vtol_pos_y + 210), "PUSHER PROPULSION POD", fill=(56, 189, 248), font=font_callout)

    except Exception as e:
        print("CAD VTOL error:", e)

    # 6. COMPONENT 2: NANO-UAV SWARM (BOTTOM-LEFT) - IN MACHINE INFOGRAPHIC STYLE
    sw_x, sw_y = 70, 560
    draw.text((sw_x, sw_y), "NANO-UAV SWARM (24+ UNITS)", fill=(255, 255, 255), font=font_node_title)
    
    # Badge
    draw.rectangle([sw_x, sw_y + 42, sw_x + 300, sw_y + 70], fill=(255, 153, 51, 30), outline=(255, 153, 51, 160), width=1)
    draw.text((sw_x + 12, sw_y + 47), "AUTONOMOUS SATURATION GRID", fill=(255, 175, 75), font=font_badge)
    draw.text((sw_x, sw_y + 80), "24 Coordinated Micro-UAVs • Anti-Jam Mesh • Perimeter Reconnaissance & Saturation", fill=(190, 210, 230), font=font_desc)
    
    # Draw Technical 24-Drone Grid with Vector Wireframe Nodes + Sensor Coverage Cones
    grid_origin_x, grid_origin_y = sw_x + 20, sw_y + 125
    rows, cols = 4, 6
    cell_w = 95
    cell_h = 66
    
    # Mesh Grid Conduits
    for r_i in range(rows):
        for c_i in range(cols):
            px = grid_origin_x + c_i * cell_w + cell_w // 2
            py = grid_origin_y + r_i * cell_h + cell_h // 2
            
            if c_i < cols - 1:
                nx = px + cell_w
                draw.line([(px, py), (nx, py)], fill=(56, 189, 248, 60), width=1)
            if r_i < rows - 1:
                ny = py + cell_h
                draw.line([(px, py), (px, ny)], fill=(56, 189, 248, 60), width=1)
            if c_i < cols - 1 and r_i < rows - 1:
                draw.line([(px, py), (px + cell_w, py + cell_h)], fill=(56, 189, 248, 25), width=1)

    # Draw Each Drone as a Clean Vector Machine Node
    for r_i in range(rows):
        for c_i in range(cols):
            px = grid_origin_x + c_i * cell_w + cell_w // 2
            py = grid_origin_y + r_i * cell_h + cell_h // 2
            
            # Scanning cone on bottom row
            if r_i == rows - 1:
                cone = [(px, py), (px - 20, py + 32), (px + 20, py + 32)]
                draw.polygon(cone, fill=(56, 189, 248, 22), outline=(56, 189, 248, 60))
            
            # Central avionics pod
            draw.ellipse([px - 9, py - 5, px + 9, py + 5], fill=(12, 34, 68, 240), outline=(56, 189, 248, 220), width=1)
            
            # 4 Motor Arms
            arm_len = 15
            draw.line([(px - arm_len, py - 8), (px + arm_len, py + 8)], fill=(56, 189, 248, 180), width=2)
            draw.line([(px - arm_len, py + 8), (px + arm_len, py - 8)], fill=(56, 189, 248, 180), width=2)
            
            # 4 Rotor Disks
            r_rad = 5
            for rx, ry in [(-arm_len, -8), (arm_len, 8), (-arm_len, 8), (arm_len, -8)]:
                draw.ellipse([px + rx - r_rad, py + ry - 2, px + rx + r_rad, py + ry + 2], 
                             outline=(56, 189, 248, 160), fill=(20, 50, 90, 180), width=1)
                
            # Optical EO/IR Sensor Glowing Dot
            draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(255, 175, 75, 255))
            
    # Swarm Telemetry Tag
    draw.rectangle([sw_x + 20, sw_y + 415, sw_x + 360, sw_y + 442], fill=(4, 14, 30, 220), outline=(56, 189, 248, 80), width=1)
    draw.text((sw_x + 30, sw_y + 421), "SWARM TOPOLOGY: 24 NODES • MESH RESILIENT", fill=(56, 189, 248), font=font_callout)

    # 7. COMPONENT 3: SECURE DATA LINK (CENTER)
    dl_x, dl_y = 960, 135
    draw.text((dl_x, dl_y), "SECURE DATA LINK", fill=(255, 255, 255), font=font_node_title)
    draw.text((dl_x, dl_y + 40), "(MESH NETWORK)", fill=(56, 189, 248), font=font_node_sub)
    
    draw.rectangle([dl_x, dl_y + 82, dl_x + 270, dl_y + 110], fill=(56, 189, 248, 30), outline=(56, 189, 248, 140), width=1)
    draw.text((dl_x + 12, dl_y + 87), "AES-256 MANET ENCRYPTION", fill=(56, 189, 248), font=font_badge)
    draw.text((dl_x, dl_y + 120), "Tactical Frequency Hopping • Dual 1.4 / 2.4 GHz", fill=(190, 210, 230), font=font_desc)

    # Central Transmission Array (x=1180, y=550)
    tx, ty = 1180, 550
    
    # Radiating RF Waves
    for rad in [50, 85, 125, 170]:
        alpha_val = int(240 - rad * 1.1)
        draw.arc([tx - rad, ty - rad, tx + rad, ty + rad], start=125, end=235, fill=(56, 189, 248, alpha_val), width=3)
        draw.arc([tx - rad, ty - rad, tx + rad, ty + rad], start=-55, end=55, fill=(56, 189, 248, alpha_val), width=3)
        
    draw.line([(tx, ty - 80), (tx, ty + 70)], fill=(56, 189, 248, 255), width=4)
    draw.polygon([(tx - 40, ty + 105), (tx + 40, ty + 105), (tx, ty + 35)], 
                 outline=(56, 189, 248, 240), fill=(10, 35, 75, 230), width=2)
    draw.line([(tx - 25, ty + 70), (tx + 25, ty + 70)], fill=(56, 189, 248, 200), width=2)
    draw.line([(tx - 15, ty + 50), (tx + 15, ty + 50)], fill=(56, 189, 248, 200), width=2)
    draw.ellipse([tx - 16, ty - 96, tx + 16, ty - 64], fill=(56, 189, 248, 255), outline=(255, 255, 255), width=2)
    draw.ellipse([tx - 6, ty - 86, tx + 6, ty - 74], fill=(255, 255, 255, 255))
    
    # RF Parameter Box
    draw.rectangle([tx - 120, ty + 120, tx + 120, ty + 195], fill=(4, 12, 28, 220), outline=(56, 189, 248, 70), width=1)
    draw.text((tx - 105, ty + 128), "FREQ: 1.4 GHz / 2.4 GHz", fill=(56, 189, 248), font=font_callout)
    draw.text((tx - 105, ty + 148), "CHANNELS: 16x HOPPING", fill=(190, 210, 230), font=font_callout)
    draw.text((tx - 105, ty + 168), "THROUGHPUT: 15 Mbps HD", fill=(255, 175, 75), font=font_callout)

    # 8. COMPONENT 4: GROUND CONTROL STATION (RIGHT)
    gcs_x, gcs_y = 1570, 105
    draw.text((gcs_x, gcs_y), "GROUND CONTROL STATION", fill=(255, 255, 255), font=font_node_title)
    draw.text((gcs_x, gcs_y + 40), "(Command, Control & Analysis)", fill=(56, 189, 248), font=font_node_sub)
    
    draw.rectangle([gcs_x, gcs_y + 82, gcs_x + 360, gcs_y + 110], fill=(56, 189, 248, 30), outline=(56, 189, 248, 140), width=1)
    draw.text((gcs_x + 12, gcs_y + 87), "MIL-STD RUGGED DUAL-SCREEN BRIEFCASE", fill=(56, 189, 248), font=font_badge)
    draw.text((gcs_x, gcs_y + 120), "Multi-UAV Mission Planning • HD Video Streams • AI Telemetry Fusion", fill=(190, 210, 230), font=font_desc)

    bw_x, bw_y = gcs_x + 30, gcs_y + 210
    
    # Place GCS Console
    try:
        gcs_img = Image.open('assets/gcs_clean_isolated.png').convert('RGBA')
        gw = 660
        gh = int(gcs_img.height * (gw / gcs_img.width))
        gcs_resized = gcs_img.resize((gw, gh), Image.LANCZOS)
        canvas.paste(gcs_resized, (bw_x, bw_y), gcs_resized)
        
        # Technical Callouts on GCS
        draw.line([(bw_x + 280, bw_y + 100), (bw_x + 280, bw_y - 25), (bw_x + 340, bw_y - 25)], fill=(56, 189, 248, 200), width=1)
        draw.ellipse([bw_x + 278, bw_y + 98, bw_x + 282, bw_y + 102], fill=(56, 189, 248, 255))
        draw.text((bw_x + 350, bw_y - 32), "17\" SUNLIGHT-READABLE TACTICAL HUD", fill=(56, 189, 248), font=font_callout)
        
        draw.line([(bw_x + 530, bw_y + 190), (bw_x + 570, bw_y + 130), (bw_x + 630, bw_y + 130)], fill=(56, 189, 248, 200), width=1)
        draw.ellipse([bw_x + 528, bw_y + 188, bw_x + 532, bw_y + 192], fill=(56, 189, 248, 255))
        draw.text((bw_x + 570, bw_y + 115), "TACTICAL TABLET", fill=(56, 189, 248), font=font_callout)
        
        draw.line([(bw_x + 160, bw_y + 240), (bw_x + 160, bw_y + 290), (bw_x + 220, bw_y + 290)], fill=(255, 175, 75, 200), width=1)
        draw.ellipse([bw_x + 158, bw_y + 238, bw_x + 162, bw_y + 242], fill=(255, 175, 75, 255))
        draw.text((bw_x + 225, bw_y + 283), "MIL-STD-810H IP67 CASE", fill=(255, 175, 75), font=font_callout)

    except Exception as e:
        print("GCS paste error:", e)

    # 9. VECTOR DATALINK TELEMETRY PATHWAYS
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

    # Vector 1: Overwatch UAV <===> Data Link Mesh Hub
    draw_dashed_vector((680, 270), (1000, 480), color=(56, 189, 248, 240), width=3, arrow=True)
    draw_dashed_vector((1000, 498), (680, 288), color=(56, 189, 248, 240), width=3, arrow=True)
    draw.text((790, 345), "AES-256 AIRBORNE C2 RELAY (150 KM)", fill=(56, 189, 248), font=font_callout)
    
    # Vector 2: Data Link Mesh Hub <===> Ground Control Station
    draw_dashed_vector((1360, 540), (1585, 540), color=(56, 189, 248, 240), width=3, arrow=True)
    draw_dashed_vector((1585, 558), (1360, 558), color=(56, 189, 248, 240), width=3, arrow=True)
    draw.text((1385, 515), "TACTICAL C2 & HD STREAM", fill=(56, 189, 248), font=font_callout)
    
    # Vector 3: Swarm Nodes <===> Data Link Mesh Hub
    draw_dashed_vector((680, 740), (1000, 620), color=(56, 189, 248, 240), width=3, arrow=True)
    draw_dashed_vector((1000, 638), (680, 758), color=(56, 189, 248, 240), width=3, arrow=True)
    draw.text((720, 675), "MANET INTRA-SWARM MESH (<85ms)", fill=(56, 189, 248), font=font_callout)

    # Vector 4: Vertical Direct C2 Control (Overwatch UAV down to Swarm Grid)
    draw_dashed_vector((350, 440), (350, 545), color=(255, 175, 75, 240), width=3, arrow=True)
    draw_dashed_vector((375, 545), (375, 440), color=(255, 175, 75, 240), width=3, arrow=True)
    draw.text((390, 485), "DIRECT SWARM C2", fill=(255, 175, 75), font=font_callout)

    # 10. Save High-Res Master Infographic
    out_path = 'assets/swarm_architecture_blue_master.png'
    canvas.save(out_path, 'PNG', quality=100)
    print(f"Refined Master Machine Infographic saved to {out_path} ({W}x{H})")

if __name__ == '__main__':
    create_machine_infographic()
