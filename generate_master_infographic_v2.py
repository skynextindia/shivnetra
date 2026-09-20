import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def build_infographic():
    W, H = 2400, 1150
    
    # 1. Base Canvas & Deep Aerospace Vignette Background
    # High-end aerospace navy palette
    base_bg = Image.new('RGBA', (W, H), (4, 10, 24, 255))
    
    # Subtle multidimensional lighting:
    # Glow 1: Behind VTOL (top left)
    # Glow 2: Behind RF Hub (center)
    # Glow 3: Behind GCS (right)
    yy, xx = np.mgrid[0:H, 0:W]
    
    dist_center = np.sqrt(((xx - 1180) / 1.5)**2 + (yy - 580)**2)
    glow_center = np.clip(1.0 - (dist_center / 700.0), 0.0, 1.0)
    
    dist_vtol = np.sqrt(((xx - 500) / 1.4)**2 + (yy - 300)**2)
    glow_vtol = np.clip(1.0 - (dist_vtol / 600.0), 0.0, 1.0)
    
    dist_gcs = np.sqrt(((xx - 1900) / 1.4)**2 + (yy - 580)**2)
    glow_gcs = np.clip(1.0 - (dist_gcs / 650.0), 0.0, 1.0)
    
    total_glow = np.clip(glow_center * 0.7 + glow_vtol * 0.5 + glow_gcs * 0.4, 0.0, 1.0)
    
    r = 4.0 + 8.0 * total_glow
    g = 10.0 + 22.0 * total_glow
    b = 24.0 + 42.0 * total_glow
    
    bg_arr = np.dstack([r, g, b, np.full((H, W), 255.0)]).astype(np.uint8)
    canvas = Image.fromarray(bg_arr)
    draw = ImageDraw.Draw(canvas, 'RGBA')
    
    # 2. Precision Engineering Blueprint Grid
    grid_sz = 60
    for x in range(0, W, grid_sz):
        alpha = 24 if x % (grid_sz * 4) == 0 else 10
        draw.line([(x, 0), (x, H)], fill=(56, 189, 248, alpha), width=1)
    for y in range(0, H, grid_sz):
        alpha = 24 if y % (grid_sz * 4) == 0 else 10
        draw.line([(0, y), (W, y)], fill=(56, 189, 248, alpha), width=1)
        
    # Crosshairs at major grid junctions
    for x in range(120, W - 100, grid_sz * 4):
        for y in range(120, H - 80, grid_sz * 4):
            draw.line([(x - 6, y), (x + 6, y)], fill=(56, 189, 248, 55), width=1)
            draw.line([(x, y - 6), (x, y + 6)], fill=(56, 189, 248, 55), width=1)
            draw.ellipse([x - 1, y - 1, x + 1, y + 1], fill=(56, 189, 248, 120))
            
    # Concentric Radar / Wave Propagation Rings at RF Datalink Center
    rcx, rcy = 1180, 580
    for rad in [140, 260, 420, 600, 800]:
        draw.ellipse([rcx - rad, rcy - rad, rcx + rad, rcy + rad], 
                     outline=(56, 189, 248, 22), width=1)
        # Degree tick marks on rings
        for ang in range(0, 360, 45):
            rad_ang = math.radians(ang)
            x1 = rcx + (rad - 5) * math.cos(rad_ang)
            y1 = rcy + (rad - 5) * math.sin(rad_ang)
            x2 = rcx + (rad + 5) * math.cos(rad_ang)
            y2 = rcy + (rad + 5) * math.sin(rad_ang)
            draw.line([(x1, y1), (x2, y2)], fill=(56, 189, 248, 40), width=1)

    # 3. Typography Setup
    try:
        f_title = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 26)
        f_sub = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 16)
        f_node_h1 = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 28)
        f_node_h2 = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 17)
        f_badge = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 14)
        f_body = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 15)
        f_mono = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 14)
        f_mono_sm = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 12)
        f_mono_bold = ImageFont.truetype('C:/Windows/Fonts/consolab.ttf', 14)
    except:
        f_title = f_sub = f_node_h1 = f_node_h2 = f_badge = f_body = f_mono = f_mono_sm = f_mono_bold = ImageFont.load_default()

    # 4. Outer Defense HUD Border & Header / Footer
    draw.rectangle([20, 20, W - 20, H - 20], outline=(56, 189, 248, 50), width=1)
    
    # Corner HUD brackets
    c_sz = 35
    for ox, oy, dx, dy in [(20, 20, 1, 1), (W - 20, 20, -1, 1), (20, H - 20, 1, -1), (W - 20, H - 20, -1, -1)]:
        draw.line([(ox, oy), (ox + dx * c_sz, oy)], fill=(56, 189, 248, 230), width=3)
        draw.line([(ox, oy), (ox, oy + dy * c_sz)], fill=(56, 189, 248, 230), width=3)

    # Top Status Banner
    draw.rectangle([20, 20, W - 20, 78], fill=(6, 16, 36, 235), outline=(56, 189, 248, 60), width=1)
    draw.text((45, 34), "AUTONOMOUS MULTI-TIER C2 & SWARM SYSTEM ARCHITECTURE", fill=(255, 255, 255), font=f_title)
    
    # Top Right Badges
    badge_x = W - 660
    draw.rectangle([badge_x, 32, badge_x + 280, 66], fill=(255, 153, 51, 28), outline=(255, 153, 51, 150), width=1)
    draw.text((badge_x + 14, 41), "MODULAR SOVEREIGN DEFENCE IP", fill=(255, 175, 75), font=f_badge)
    
    badge2_x = badge_x + 295
    draw.rectangle([badge2_x, 32, W - 45, 66], fill=(56, 189, 248, 28), outline=(56, 189, 248, 140), width=1)
    draw.text((badge2_x + 14, 41), "STANAG 4586 / SAIL III READY", fill=(56, 189, 248), font=f_badge)

    # Bottom Telemetry Ribbon
    draw.rectangle([20, H - 65, W - 20, H - 20], fill=(6, 16, 36, 235), outline=(56, 189, 248, 50), width=1)
    footer_text = "ENCRYPTION: AES-256 GCM (HARDWARE CRYPTO)  |  MANET RF: 1.4 GHz / 2.4 GHz COFDM  |  SWARM CONSENSUS: DECENTRALIZED RAFT  |  FAIL-OVER: DUAL AIRBORNE RELAY  |  LATENCY: <85ms"
    draw.text((45, H - 50), footer_text, fill=(56, 189, 248, 200), font=f_mono)
    draw.text((W - 270, H - 50), "SYS VER: 4.7-MIL-STD", fill=(255, 175, 75, 220), font=f_mono_bold)

    # =========================================================================
    # 5. NODE 1: OVERWATCH UAV (TOP-LEFT) - PRECISION MACHINE CAD
    # =========================================================================
    vtol_box_x, vtol_box_y = 45, 100
    draw.text((vtol_box_x, vtol_box_y), "1. OVERWATCH UAV (1 UNIT)", fill=(255, 255, 255), font=f_node_h1)
    draw.text((vtol_box_x, vtol_box_y + 36), "AIRBORNE C2 MISSION COMMANDER & HIGH-ALTITUDE RELAY BACKBONE", fill=(56, 189, 248), font=f_node_h2)
    
    # Spec Tags Row
    spec_tags = ["150 KM LINE-OF-SIGHT", "180 MIN ENDURANCE", "15 KG PAYLOAD", "NAVIC TRIPLE GNSS"]
    cur_tx = vtol_box_x
    for st in spec_tags:
        t_w = len(st) * 8 + 16
        draw.rectangle([cur_tx, vtol_box_y + 66, cur_tx + t_w, vtol_box_y + 88], fill=(12, 28, 56, 200), outline=(56, 189, 248, 70), width=1)
        draw.text((cur_tx + 8, vtol_box_y + 70), st, fill=(190, 215, 245), font=f_mono_sm)
        cur_tx += t_w + 10

    # Render Glowing Cyan CAD Wireframe of the Authentic VTOL
    try:
        cad = Image.open('assets/vtol_cad_white_lines.png').convert('RGBA')
        c_arr = np.array(cad)
        alpha = c_arr[:, :, 3].astype(float) / 255.0
        
        # Colorize to luminous electric cyan
        cyan_cad = np.zeros_like(c_arr)
        cyan_cad[:, :, 0] = (56 * alpha).astype(np.uint8)
        cyan_cad[:, :, 1] = (189 * alpha).astype(np.uint8)
        cyan_cad[:, :, 2] = (248 * alpha).astype(np.uint8)
        cyan_cad[:, :, 3] = (c_arr[:, :, 3] * 0.96).astype(np.uint8)
        
        cad_img = Image.fromarray(cyan_cad)
        cw = 620
        ch = int(cad_img.height * (cw / cad_img.width))
        cad_resized = cad_img.resize((cw, ch), Image.LANCZOS)
        
        vtol_render_x, vtol_render_y = vtol_box_x + 35, vtol_box_y + 115
        canvas.paste(cad_resized, (vtol_render_x, vtol_render_y), cad_resized)
        
        # Optical Gimbal Scanner Beam from Nose
        beam_poly = [
            (vtol_render_x + 100, vtol_render_y + 160),
            (vtol_render_x - 30, vtol_render_y + 360),
            (vtol_render_x + 220, vtol_render_y + 360)
        ]
        draw.polygon(beam_poly, fill=(56, 189, 248, 16), outline=(56, 189, 248, 45))
        draw.text((vtol_render_x - 10, vtol_render_y + 365), "EO/IR 30x OPTICAL SCAN FOOTPRINT", fill=(56, 189, 248, 180), font=f_mono_sm)

        # Technical LRU Callout Leader Lines (Clean, no overlap)
        # LRU-01: Carbon Airframe
        c1_x, c1_y = vtol_render_x + 95, vtol_render_y + 110
        draw.ellipse([c1_x - 3, c1_y - 3, c1_x + 3, c1_y + 3], fill=(255, 153, 51, 255))
        draw.line([(c1_x, c1_y), (c1_x - 40, c1_y - 30), (c1_x - 110, c1_y - 30)], fill=(255, 153, 51, 220), width=1)
        draw.text((c1_x - 110, c1_y - 48), "[LRU-01] QUICK-DISCONNECT WING", fill=(255, 175, 75), font=f_mono_sm)

        # LRU-02 & 03: Triple AHRS & AI Core
        c2_x, c2_y = vtol_render_x + 240, vtol_render_y + 105
        draw.ellipse([c2_x - 3, c2_y - 3, c2_x + 3, c2_y + 3], fill=(56, 189, 248, 255))
        draw.line([(c2_x, c2_y), (c2_x + 15, c2_y - 35), (c2_x + 160, c2_y - 35)], fill=(56, 189, 248, 220), width=1)
        draw.text((c2_x + 20, c2_y - 52), "[LRU-02/03] TRIPLE AHRS & AI EDGE CORE", fill=(56, 189, 248), font=f_mono_sm)

        # Hybrid Lift Rotors
        c3_x, c3_y = vtol_render_x + 440, vtol_render_y + 90
        draw.ellipse([c3_x - 3, c3_y - 3, c3_x + 3, c3_y + 3], fill=(56, 189, 248, 255))
        draw.line([(c3_x, c3_y), (c3_x + 40, c3_y - 20), (c3_x + 150, c3_y - 20)], fill=(56, 189, 248, 220), width=1)
        draw.text((c3_x + 45, c3_y - 38), "4x HYBRID VTOL ROTORS", fill=(56, 189, 248), font=f_mono_sm)

        # Pusher Propulsion
        c4_x, c4_y = vtol_render_x + 360, vtol_render_y + 155
        draw.ellipse([c4_x - 3, c4_y - 3, c4_x + 3, c4_y + 3], fill=(255, 153, 51, 255))
        draw.line([(c4_x, c4_y), (c4_x + 40, c4_y + 40), (c4_x + 140, c4_y + 40)], fill=(255, 153, 51, 220), width=1)
        draw.text((c4_x + 45, c4_y + 45), "[LRU-05] MODULAR PAYLOAD BAY", fill=(255, 175, 75), font=f_mono_sm)

    except Exception as e:
        print("Error rendering VTOL CAD:", e)

    # =========================================================================
    # 6. NODE 2: NANO-UAV SWARM (24+ UNITS) (BOTTOM-LEFT)
    # =========================================================================
    swarm_box_x, swarm_box_y = 45, 595
    draw.text((swarm_box_x, swarm_box_y), "2. NANO-UAV SWARM (24+ UNITS)", fill=(255, 255, 255), font=f_node_h1)
    draw.text((swarm_box_x, swarm_box_y + 36), "AUTONOMOUS SATURATION GRID & MULTI-TARGET RECONNAISSANCE", fill=(255, 175, 75), font=f_node_h2)
    
    # Swarm Specs
    swarm_tags = ["24 COOPERATIVE NODES", "MANET AD-HOC MESH", "SELF-HEALING ROUTING", "TARGET HANDOVER"]
    cur_stx = swarm_box_x
    for st in swarm_tags:
        t_w = len(st) * 8 + 16
        draw.rectangle([cur_stx, swarm_box_y + 66, cur_stx + t_w, swarm_box_y + 88], fill=(12, 28, 56, 200), outline=(255, 153, 51, 70), width=1)
        draw.text((cur_stx + 8, swarm_box_y + 70), st, fill=(255, 195, 120), font=f_mono_sm)
        cur_stx += t_w + 10

    # Draw 24-Drone High-Tech Vector Tactical Swarm Mesh
    s_rows, s_cols = 4, 6
    s_orig_x, s_orig_y = swarm_box_x + 25, swarm_box_y + 115
    s_cell_w, s_cell_h = 95, 68

    # Draw Inter-Node MANET Mesh Links (Vector Lines)
    for r_i in range(s_rows):
        for c_i in range(s_cols):
            px = s_orig_x + c_i * s_cell_w + s_cell_w // 2
            py = s_orig_y + r_i * s_cell_h + s_cell_h // 2
            
            # Horizontal mesh link
            if c_i < s_cols - 1:
                nx = px + s_cell_w
                draw.line([(px, py), (nx, py)], fill=(56, 189, 248, 55), width=1)
            # Vertical mesh link
            if r_i < s_rows - 1:
                ny = py + s_cell_h
                draw.line([(px, py), (px, ny)], fill=(56, 189, 248, 55), width=1)
            # Diagonal cross-mesh links
            if c_i < s_cols - 1 and r_i < s_rows - 1:
                draw.line([(px, py), (px + s_cell_w, py + s_cell_h)], fill=(56, 189, 248, 25), width=1)
                draw.line([(px + s_cell_w, py), (px, py + s_cell_h)], fill=(56, 189, 248, 25), width=1)

    # Draw Each Individual Drone Machine Node
    for r_i in range(s_rows):
        for c_i in range(s_cols):
            px = s_orig_x + c_i * s_cell_w + s_cell_w // 2
            py = s_orig_y + r_i * s_cell_h + s_cell_h // 2
            
            # Bottom row sensor coverage cones onto ground
            if r_i == s_rows - 1:
                s_cone = [(px, py), (px - 22, py + 36), (px + 22, py + 36)]
                draw.polygon(s_cone, fill=(56, 189, 248, 18), outline=(56, 189, 248, 50))
                draw.ellipse([px - 14, py + 34, px + 14, py + 38], fill=(56, 189, 248, 30))

            # Quadcopter central avionics pod
            draw.ellipse([px - 10, py - 6, px + 10, py + 6], fill=(10, 30, 60, 245), outline=(56, 189, 248, 220), width=1)
            
            # 4 Carbon motor arms
            arm_r = 16
            draw.line([(px - arm_r, py - 9), (px + arm_r, py + 9)], fill=(56, 189, 248, 190), width=2)
            draw.line([(px - arm_r, py + 9), (px + arm_r, py - 9)], fill=(56, 189, 248, 190), width=2)
            
            # 4 Motor pods & spinning rotor discs
            rotor_rx, rotor_ry = 6, 2
            for mx, my in [(-arm_r, -9), (arm_r, 9), (-arm_r, 9), (arm_r, -9)]:
                draw.ellipse([px + mx - rotor_rx, py + my - rotor_ry, px + mx + rotor_rx, py + my + rotor_ry],
                             fill=(20, 55, 100, 160), outline=(56, 189, 248, 180), width=1)
                draw.ellipse([px + mx - 1, py + my - 1, px + mx + 1, py + my + 1], fill=(255, 255, 255, 240))
                
            # Optical seeker dot in center
            seeker_color = (255, 153, 51, 255) if (r_i == 0 and c_i == 0) else (56, 189, 248, 255)
            draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=seeker_color)

    # Swarm Topology Status Bar
    draw.rectangle([swarm_box_x + 25, swarm_box_y + 410, swarm_box_x + 590, swarm_box_y + 440], 
                   fill=(6, 18, 38, 230), outline=(56, 189, 248, 80), width=1)
    draw.text((swarm_box_x + 40, swarm_box_y + 418), 
              "SWARM STATUS: 24/24 ONLINE  |  TOPOLOGY: MESH AD-HOC  |  CONSENSUS: LEADERLESS", 
              fill=(56, 189, 248), font=f_mono_sm)

    # =========================================================================
    # 7. NODE 3: SECURE DATA LINK (CENTER) - COFDM MANET RELAY
    # =========================================================================
    dl_box_x, dl_box_y = 960, 100
    draw.text((dl_box_x, dl_box_y), "3. SECURE DATA LINK", fill=(255, 255, 255), font=f_node_h1)
    draw.text((dl_box_x, dl_box_y + 36), "MANET MESH NETWORK & ANTI-JAM RF HUB", fill=(56, 189, 248), font=f_node_h2)
    
    # RF Specs Row
    rf_tags = ["[LRU-04] SECURED MESH", "1.4 & 2.4 GHz DUAL-BAND", "16x FREQ HOPPING", "AES-256 GCM"]
    cur_rfx = dl_box_x
    for rt in rf_tags:
        t_w = len(rt) * 8 + 16
        draw.rectangle([cur_rfx, dl_box_y + 66, cur_rfx + t_w, dl_box_y + 88], fill=(12, 28, 56, 200), outline=(56, 189, 248, 70), width=1)
        draw.text((cur_rfx + 8, dl_box_y + 70), rt, fill=(190, 215, 245), font=f_mono_sm)
        cur_rfx += t_w + 10

    # Center RF Transmission Tower (rcx = 1180, rcy = 580)
    # Radiating High-Tech Wavefront Arcs
    for rad, alpha_val in [(55, 240), (95, 200), (145, 160), (205, 110), (275, 70)]:
        # Left-pointing waves towards UAVs
        draw.arc([rcx - rad, rcy - rad, rcx + rad, rcy + rad], start=120, end=240, fill=(56, 189, 248, alpha_val), width=3)
        # Right-pointing waves towards GCS
        draw.arc([rcx - rad, rcy - rad, rcx + rad, rcy + rad], start=-60, end=60, fill=(56, 189, 248, alpha_val), width=3)

    # Transmission Tower Geometry
    draw.line([(rcx, rcy - 110), (rcx, rcy + 80)], fill=(56, 189, 248, 255), width=4)
    # Tower base truss
    draw.polygon([(rcx - 50, rcy + 120), (rcx + 50, rcy + 120), (rcx, rcy + 40)], 
                 fill=(8, 26, 56, 240), outline=(56, 189, 248, 240), width=2)
    draw.line([(rcx - 30, rcy + 80), (rcx + 30, rcy + 80)], fill=(56, 189, 248, 200), width=2)
    draw.line([(rcx - 18, rcy + 58), (rcx + 18, rcy + 58)], fill=(56, 189, 248, 200), width=2)
    
    # Antenna Radome Sphere & Transceiver
    draw.ellipse([rcx - 20, rcy - 130, rcx + 20, rcy - 90], fill=(12, 36, 75, 255), outline=(56, 189, 248, 255), width=2)
    draw.ellipse([rcx - 8, rcy - 118, rcx + 8, rcy - 102], fill=(255, 255, 255, 255))
    
    # Parabolic dish reflector
    draw.arc([rcx - 35, rcy - 85, rcx + 35, rcy - 55], start=180, end=360, fill=(56, 189, 248, 255), width=3)

    # Technical RF Parameter Readout Box
    rf_box_w, rf_box_h = 270, 105
    rf_bx, rf_by = rcx - rf_box_w // 2, rcy + 140
    draw.rectangle([rf_bx, rf_by, rf_bx + rf_box_w, rf_by + rf_box_h], 
                   fill=(5, 14, 32, 235), outline=(56, 189, 248, 80), width=1)
    # HUD Corner markers on RF box
    draw.line([(rf_bx, rf_by), (rf_bx + 12, rf_by)], fill=(56, 189, 248, 240), width=2)
    draw.line([(rf_bx, rf_by), (rf_bx, rf_by + 12)], fill=(56, 189, 248, 240), width=2)
    draw.line([(rf_bx + rf_box_w, rf_by + rf_box_h), (rf_bx + rf_box_w - 12, rf_by + rf_box_h)], fill=(56, 189, 248, 240), width=2)
    draw.line([(rf_bx + rf_box_w, rf_by + rf_box_h), (rf_bx + rf_box_w, rf_by + rf_box_h - 12)], fill=(56, 189, 248, 240), width=2)
    
    draw.text((rf_bx + 14, rf_by + 12), "MANET PROTOCOL: DUAL-BAND", fill=(56, 189, 248), font=f_mono_bold)
    draw.text((rf_bx + 14, rf_by + 34), "BAND 1: 1.4 GHz C2 CONTROL", fill=(190, 215, 245), font=f_mono_sm)
    draw.text((rf_bx + 14, rf_by + 56), "BAND 2: 2.4 GHz HD VIDEO (15 Mbps)", fill=(190, 215, 245), font=f_mono_sm)
    draw.text((rf_bx + 14, rf_by + 78), "SECURITY: AES-256 ENCRYPTED", fill=(255, 175, 75), font=f_mono_bold)

    # =========================================================================
    # 8. NODE 4: GROUND CONTROL STATION (RIGHT) - HIGH-TECH BLUEPRINT CONSOLE
    # =========================================================================
    gcs_box_x, gcs_box_y = 1580, 100
    draw.text((gcs_box_x, gcs_box_y), "4. GROUND CONTROL STATION", fill=(255, 255, 255), font=f_node_h1)
    draw.text((gcs_box_x, gcs_box_y + 36), "[LRU-06] TACTICAL PORTABLE GCS BRIEFCASE WORKSTATION", fill=(56, 189, 248), font=f_node_h2)
    
    # GCS Specs
    gcs_tags = ["DUAL SUNLIGHT HUD", "MIL-STD-810H IP67", "HOT-SWAP BATTERY", "MULTI-UAV DISPATCH"]
    cur_gcx = gcs_box_x
    for gt in gcs_tags:
        t_w = len(gt) * 8 + 16
        draw.rectangle([cur_gcx, gcs_box_y + 66, cur_gcx + t_w, gcs_box_y + 88], fill=(12, 28, 56, 200), outline=(56, 189, 248, 70), width=1)
        draw.text((cur_gcx + 8, gcs_box_y + 70), gt, fill=(190, 215, 245), font=f_mono_sm)
        cur_gcx += t_w + 10

    # Draw Precision High-Tech Blueprint Vector Machine of the GCS Console!
    # Instead of a rough cutout photo, we render a pristine tactical command workstation
    # with dual illuminated screens showing live tactical radar maps and telemetry ribbons!
    gw_x, gw_y = gcs_box_x + 40, gcs_box_y + 130
    
    # Outer Briefcase Chassis Dimensions
    bc_w, bc_h = 680, 360
    
    # 1. Lower Case (Chassis Body & Controls Deck)
    deck_y = gw_y + 190
    draw.polygon([
        (gw_x, deck_y + 30),
        (gw_x + 500, deck_y + 30),
        (gw_x + 580, deck_y + 140),
        (gw_x + 80, deck_y + 140)
    ], fill=(10, 24, 48, 250), outline=(56, 189, 248, 180), width=2)
    
    # Heavy Rugged Front Lip / Handle
    draw.rectangle([gw_x + 250, deck_y + 138, gw_x + 410, deck_y + 160], 
                   fill=(6, 16, 32, 255), outline=(56, 189, 248, 200), width=2)
    draw.text((gw_x + 285, deck_y + 144), "MIL-STD-810H", fill=(56, 189, 248, 200), font=f_mono_sm)
    
    # Pilot Control Joysticks (Left & Right)
    for jx in [gw_x + 170, gw_x + 480]:
        jy = deck_y + 85
        draw.ellipse([jx - 24, jy - 14, jx + 24, jy + 14], fill=(6, 18, 38, 255), outline=(56, 189, 248, 140), width=1)
        draw.line([(jx, jy - 16), (jx, jy + 10)], fill=(56, 189, 248, 220), width=3)
        draw.ellipse([jx - 8, jy - 22, jx + 8, jy - 10], fill=(255, 153, 51, 240), outline=(255, 255, 255), width=1)
        
    # Keyboard & Switch Array Deck
    draw.rectangle([gw_x + 225, deck_y + 55, gw_x + 425, deck_y + 115], 
                   fill=(6, 16, 34, 230), outline=(56, 189, 248, 100), width=1)
    for k_row in range(3):
        for k_col in range(12):
            kx = gw_x + 235 + k_col * 15
            ky = deck_y + 65 + k_row * 15
            draw.rectangle([kx, ky, kx + 10, ky + 10], fill=(16, 38, 70, 200))

    # 2. Main 17" Primary Sunlight-Readable Tactical Display (Top Lid tilted upright)
    disp_x, disp_y = gw_x + 25, gw_y
    disp_w, disp_h = 490, 215
    
    # Screen Outer Bezel
    draw.rectangle([disp_x, disp_y, disp_x + disp_w, disp_y + disp_h], 
                   fill=(6, 16, 34, 255), outline=(56, 189, 248, 220), width=2)
    # Bezel Corner Reinforced Bumpers
    b_sz = 14
    for bx, by in [(disp_x, disp_y), (disp_x + disp_w, disp_y), (disp_x, disp_y + disp_h), (disp_x + disp_w, disp_y + disp_h)]:
        draw.rectangle([bx - b_sz//2, by - b_sz//2, bx + b_sz//2, by + b_sz//2], fill=(56, 189, 248, 200))
        
    # Active Screen Glass Area
    s_pad = 12
    sx1, sy1 = disp_x + s_pad, disp_y + s_pad
    sx2, sy2 = disp_x + disp_w - s_pad, disp_y + disp_h - s_pad
    draw.rectangle([sx1, sy1, sx2, sy2], fill=(2, 10, 22, 255), outline=(56, 189, 248, 120), width=1)
    
    # Tactical HUD on Main Screen:
    # Tactical Map Grid
    for gx in range(sx1, sx2, 35):
        draw.line([(gx, sy1), (gx, sy2)], fill=(56, 189, 248, 20), width=1)
    for gy in range(sy1, sy2, 35):
        draw.line([(sx1, gy), (sx2, gy)], fill=(56, 189, 248, 20), width=1)
        
    # Radar Sweep Circle
    rad_cx, rad_cy = sx1 + 170, sy1 + 95
    draw.ellipse([rad_cx - 75, rad_cy - 75, rad_cx + 75, rad_cy + 75], outline=(56, 189, 248, 90), width=1)
    draw.ellipse([rad_cx - 45, rad_cy - 45, rad_cx + 45, rad_cy + 45], outline=(56, 189, 248, 70), width=1)
    draw.line([(rad_cx - 75, rad_cy), (rad_cx + 75, rad_cy)], fill=(56, 189, 248, 60), width=1)
    draw.line([(rad_cx, rad_cy - 75), (rad_cx, rad_cy + 75)], fill=(56, 189, 248, 60), width=1)
    
    # Active Overwatch UAV Track Marker
    draw.polygon([(rad_cx + 25, rad_cy - 30), (rad_cx + 33, rad_cy - 20), (rad_cx + 17, rad_cy - 20)], fill=(56, 189, 248, 255))
    draw.text((rad_cx + 38, rad_cy - 34), "OW-01 [ALT: 1800m]", fill=(56, 189, 248), font=f_mono_sm)
    
    # Swarm Cluster Dots on Radar
    for s_ang in [15, 60, 110, 160, 210, 270, 320]:
        s_r = 38
        s_dx = rad_cx + s_r * math.cos(math.radians(s_ang))
        s_dy = rad_cy + s_r * math.sin(math.radians(s_ang))
        draw.ellipse([s_dx - 2, s_dy - 2, s_dx + 2, s_dy + 2], fill=(255, 153, 51, 240))
        
    # Screen Side Telemetry Panel
    t_px = sx1 + 325
    draw.line([(t_px, sy1), (t_px, sy2)], fill=(56, 189, 248, 80), width=1)
    draw.text((t_px + 10, sy1 + 10), "MISSION: SATURATION", fill=(255, 175, 75), font=f_mono_sm)
    draw.text((t_px + 10, sy1 + 30), "SWARM: 24 NODES", fill=(56, 189, 248), font=f_mono_sm)
    draw.text((t_px + 10, sy1 + 50), "GPS: NAVIC RTK FIXED", fill=(190, 215, 245), font=f_mono_sm)
    draw.text((t_px + 10, sy1 + 70), "DATALINK: 99.8% RSSI", fill=(56, 189, 248), font=f_mono_sm)
    draw.text((t_px + 10, sy1 + 90), "ENCRYPTION: AES-256", fill=(255, 175, 75), font=f_mono_sm)
    draw.text((t_px + 10, sy1 + 125), "LAT: 28°36'14\"N", fill=(140, 170, 210), font=f_mono_sm)
    draw.text((t_px + 10, sy1 + 145), "LON: 77°12'45\"E", fill=(140, 170, 210), font=f_mono_sm)

    # 3. Secondary Tactical Mission Tablet (Standing to the right of the briefcase)
    tab_x, tab_y = gw_x + 535, gw_y + 70
    tab_w, tab_h = 165, 195
    # Tablet body
    draw.rectangle([tab_x, tab_y, tab_x + tab_w, tab_y + tab_h], fill=(8, 20, 42, 255), outline=(56, 189, 248, 200), width=2)
    # Tablet active screen
    draw.rectangle([tab_x + 8, tab_y + 8, tab_x + tab_w - 8, tab_y + tab_h - 8], fill=(3, 12, 26, 255), outline=(56, 189, 248, 100), width=1)
    draw.text((tab_x + 14, tab_y + 14), "TACTICAL TABLET", fill=(255, 175, 75), font=f_mono_sm)
    draw.text((tab_x + 14, tab_y + 32), "PAYLOAD DIRECT", fill=(56, 189, 248), font=f_mono_sm)
    # Mini mesh formation view on tablet
    for mr in range(3):
        for mc in range(4):
            mpx = tab_x + 25 + mc * 32
            mpy = tab_y + 70 + mr * 32
            draw.ellipse([mpx - 3, mpy - 3, mpx + 3, mpy + 3], fill=(56, 189, 248, 200))
            if mc < 3:
                draw.line([(mpx, mpy), (mpx + 32, mpy)], fill=(56, 189, 248, 70), width=1)
            if mr < 2:
                draw.line([(mpx, mpy), (mpx, mpy + 32)], fill=(56, 189, 248, 70), width=1)

    # Technical Callouts on GCS
    draw.line([(disp_x + 150, disp_y), (disp_x + 150, disp_y - 25), (disp_x + 25, disp_y - 25)], fill=(56, 189, 248, 200), width=1)
    draw.ellipse([disp_x + 148, disp_y - 2, disp_x + 152, disp_y + 2], fill=(56, 189, 248, 255))
    draw.text((disp_x - 170, disp_y - 33), "17\" TACTICAL HUD (1000 NITS)", fill=(56, 189, 248), font=f_mono_sm)

    draw.line([(tab_x + 80, tab_y), (tab_x + 80, tab_y - 25), (tab_x + 120, tab_y - 25)], fill=(255, 153, 51, 200), width=1)
    draw.ellipse([tab_x + 78, tab_y - 2, tab_x + 82, tab_y + 2], fill=(255, 153, 51, 255))
    draw.text((tab_x + 130, tab_y - 33), "PORTABLE SWARM CONTROLLER", fill=(255, 175, 75), font=f_mono_sm)

    # GCS Status Box Below
    gcs_stat_x, gcs_stat_y = gw_x, deck_y + 195
    draw.rectangle([gcs_stat_x, gcs_stat_y, gcs_stat_x + bc_w + 20, gcs_stat_y + 45], 
                   fill=(6, 18, 38, 230), outline=(56, 189, 248, 80), width=1)
    draw.text((gcs_stat_x + 20, gcs_stat_y + 14), 
              "C2 DISPATCH: REAL-TIME FLIGHT PLANNER  |  ENCRYPTION: AES-256 GCM  |  RUGGED: IP67 / MIL-STD-810H", 
              fill=(56, 189, 248), font=f_mono_sm)

    # =========================================================================
    # 9. HIGH-TECH VECTOR DATA PIPELINES (CRISP & BEAUTIFULLY ROUTED)
    # =========================================================================
    def draw_glowing_pipeline(p1, p2, label="", color=(56, 189, 248), label_offset=(-50, -20)):
        x1, y1 = p1
        x2, y2 = p2
        length = math.hypot(x2 - x1, y2 - y1)
        if length == 0:
            return
        dx = (x2 - x1) / length
        dy = (y2 - y1) / length
        
        # Outer soft glow line
        draw.line([p1, p2], fill=(color[0], color[1], color[2], 35), width=7)
        # Inner dashed data line
        dash_sz = 14
        gap_sz = 9
        curr = 0
        while curr < length - 20:
            s_x = x1 + dx * curr
            s_y = y1 + dy * curr
            e_x = x1 + dx * min(curr + dash_sz, length - 20)
            e_y = y1 + dy * min(curr + dash_sz, length - 20)
            draw.line([(s_x, s_y), (e_x, e_y)], fill=(color[0], color[1], color[2], 240), width=2)
            curr += dash_sz + gap_sz
            
        # Directional Arrow Head at endpoint
        ah_l = 15
        ah_w = 6
        bx = x2 - dx * ah_l
        by = y2 - dy * ah_l
        px = -dy * ah_w
        py = dx * ah_w
        draw.polygon([(x2, y2), (bx + px, by + py), (bx - px, by - py)], fill=(color[0], color[1], color[2], 255))
        
        # Center Label with badge background if present
        if label:
            mx = (x1 + x2) / 2.0 + label_offset[0]
            my = (y1 + y2) / 2.0 + label_offset[1]
            tw = len(label) * 8 + 16
            draw.rectangle([mx, my, mx + tw, my + 24], fill=(4, 12, 28, 230), outline=(color[0], color[1], color[2], 140), width=1)
            draw.text((mx + 8, my + 4), label, fill=color, font=f_mono_sm)

    # Pipeline 1: Overwatch UAV <===> RF Datalink Hub (Bidirectional)
    draw_glowing_pipeline((710, 290), (1020, 500), label="C2 RELAY BACKBONE (150 KM)", color=(56, 189, 248), label_offset=(-120, -35))
    draw_glowing_pipeline((1020, 520), (710, 310), color=(56, 189, 248))

    # Pipeline 2: Swarm Array <===> RF Datalink Hub (Bidirectional)
    draw_glowing_pipeline((710, 770), (1020, 640), label="MANET INTRA-SWARM MESH (<85ms)", color=(56, 189, 248), label_offset=(-140, 15))
    draw_glowing_pipeline((1020, 660), (710, 790), color=(56, 189, 248))

    # Pipeline 3: RF Datalink Hub <===> Ground Control Station (Bidirectional)
    draw_glowing_pipeline((1340, 560), (1570, 560), label="MISSION DISPATCH & 1080P HD STREAM", color=(56, 189, 248), label_offset=(-125, -35))
    draw_glowing_pipeline((1570, 580), (1340, 580), color=(255, 153, 51))

    # Pipeline 4: Direct Vertical Swarm Command (Overwatch directly down to Swarm)
    draw_glowing_pipeline((380, 485), (380, 585), label="DIRECT AIRBORNE C2", color=(255, 153, 51), label_offset=(15, -45))
    draw_glowing_pipeline((405, 585), (405, 485), color=(255, 153, 51))

    # 10. Save Output Master Infographic
    out_file = 'assets/swarm_architecture_blue_master.png'
    canvas.save(out_file, 'PNG', quality=100)
    print(f"Master Machine Infographic generated successfully: {out_file} ({W}x{H})")

if __name__ == '__main__':
    build_infographic()
