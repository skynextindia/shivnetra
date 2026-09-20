import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_master_infographic():
    W, H = 2400, 1150
    
    # 1. Base Deep Aerospace Navy Solid Background
    yy, xx = np.mgrid[0:H, 0:W]
    
    # Atmospheric radial glow behind key clusters
    g_center = np.clip(1.0 - (np.sqrt(((xx - 1180) / 1.6)**2 + (yy - 580)**2) / 680.0), 0.0, 1.0)
    g_vtol   = np.clip(1.0 - (np.sqrt(((xx - 450) / 1.5)**2 + (yy - 320)**2) / 580.0), 0.0, 1.0)
    g_gcs    = np.clip(1.0 - (np.sqrt(((xx - 1920) / 1.5)**2 + (yy - 600)**2) / 650.0), 0.0, 1.0)
    
    tot_glow = np.clip(g_center * 0.65 + g_vtol * 0.45 + g_gcs * 0.45, 0.0, 1.0)
    
    r = (4.0 + 9.0 * tot_glow).astype(np.uint8)
    g = (9.0 + 19.0 * tot_glow).astype(np.uint8)
    b = (22.0 + 36.0 * tot_glow).astype(np.uint8)
    
    canvas_arr = np.dstack([r, g, b, np.full((H, W), 255, dtype=np.uint8)])
    canvas = Image.fromarray(canvas_arr, 'RGBA')
    
    # Helper to draw translucent layers properly via alpha_composite
    def draw_translucent(draw_fn):
        nonlocal canvas
        layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ldraw = ImageDraw.Draw(layer)
        draw_fn(ldraw)
        canvas = Image.alpha_composite(canvas, layer)

    # 2. Precision Engineering Blueprint Grid (Rendered via alpha_composite)
    def render_grid(d):
        grid_sz = 60
        for x in range(0, W, grid_sz):
            alpha = 24 if x % (grid_sz * 4) == 0 else 10
            d.line([(x, 0), (x, H)], fill=(56, 189, 248, alpha), width=1)
        for y in range(0, H, grid_sz):
            alpha = 24 if y % (grid_sz * 4) == 0 else 10
            d.line([(0, y), (W, y)], fill=(56, 189, 248, alpha), width=1)
            
        # Crosshairs at 240px intervals
        for x in range(120, W - 100, 240):
            for y in range(120, H - 80, 240):
                d.line([(x - 6, y), (x + 6, y)], fill=(56, 189, 248, 55), width=1)
                d.line([(x, y - 6), (x, y + 6)], fill=(56, 189, 248, 55), width=1)
                d.ellipse([x - 1, y - 1, x + 1, y + 1], fill=(56, 189, 248, 140))
                
        # Concentric Radar / Wave Propagation Rings at RF Center (1180, 580)
        rcx, rcy = 1180, 580
        for rad in [140, 270, 430, 620, 820]:
            d.ellipse([rcx - rad, rcy - rad, rcx + rad, rcy + rad], 
                      outline=(56, 189, 248, 22), width=1)
                      
    draw_translucent(render_grid)

    # 3. Fonts Setup
    try:
        f_title    = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 26)
        f_node_h1  = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 26)
        f_node_h2  = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 16)
        f_badge    = ImageFont.truetype('C:/Windows/Fonts/bahnschrift.ttf', 14)
        f_mono     = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 14)
        f_mono_sm  = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 12)
        f_mono_bld = ImageFont.truetype('C:/Windows/Fonts/consolab.ttf', 13)
    except:
        f_title = f_node_h1 = f_node_h2 = f_badge = f_mono = f_mono_sm = f_mono_bld = ImageFont.load_default()

    # 4. Main HUD Frame, Header Banner & Footer
    def render_hud_frame(d):
        d.rectangle([20, 20, W - 20, H - 20], outline=(56, 189, 248, 70), width=1)
        
        # Corner brackets
        c_sz = 35
        for ox, oy, dx, dy in [(20, 20, 1, 1), (W - 20, 20, -1, 1), (20, H - 20, 1, -1), (W - 20, H - 20, -1, -1)]:
            d.line([(ox, oy), (ox + dx * c_sz, oy)], fill=(56, 189, 248, 240), width=3)
            d.line([(ox, oy), (ox, oy + dy * c_sz)], fill=(56, 189, 248, 240), width=3)

        # Top Header Bar
        d.rectangle([20, 20, W - 20, 78], fill=(6, 16, 36, 245), outline=(56, 189, 248, 70), width=1)
        d.text((45, 34), "SHIV-NETRA 47 // MULTI-TIER C2 & AUTONOMOUS SWARM ARCHITECTURE", fill=(255, 255, 255), font=f_title)
        
        # Badges on Top Right
        b1_x = W - 660
        d.rectangle([b1_x, 32, b1_x + 280, 66], fill=(255, 153, 51, 35), outline=(255, 153, 51, 180), width=1)
        d.text((b1_x + 14, 41), "MODULAR SOVEREIGN DEFENCE IP", fill=(255, 175, 75), font=f_badge)
        
        b2_x = b1_x + 295
        d.rectangle([b2_x, 32, W - 45, 66], fill=(56, 189, 248, 35), outline=(56, 189, 248, 180), width=1)
        d.text((b2_x + 14, 41), "STANAG 4586 / SAIL III READY", fill=(56, 189, 248), font=f_badge)

        # Bottom Telemetry Ribbon
        d.rectangle([20, H - 65, W - 20, H - 20], fill=(6, 16, 36, 245), outline=(56, 189, 248, 60), width=1)
        footer_text = "ENCRYPTION: AES-256 GCM (HARDWARE CRYPTO)  |  MANET RF: 1.4 GHz / 2.4 GHz COFDM  |  SWARM CONSENSUS: DECENTRALIZED RAFT  |  FAIL-OVER: AIRBORNE RELAY  |  LATENCY: <85ms"
        d.text((45, H - 49), footer_text, fill=(56, 189, 248, 220), font=f_mono)
        d.text((W - 270, H - 49), "SYS VER: 4.7-MIL-STD", fill=(255, 175, 75, 240), font=f_mono_bld)

    draw_translucent(render_hud_frame)

    # =========================================================================
    # 5. COMPONENT 1: OVERWATCH UAV (TOP-LEFT)
    # =========================================================================
    vtol_box_x, vtol_box_y = 50, 100
    
    def render_vtol_header(d):
        d.text((vtol_box_x, vtol_box_y), "1. OVERWATCH UAV (1 UNIT)", fill=(255, 255, 255), font=f_node_h1)
        d.text((vtol_box_x, vtol_box_y + 34), "AIRBORNE C2 MISSION COMMANDER & RELAY BACKBONE", fill=(56, 189, 248), font=f_node_h2)
        
        # Spec Pills
        spec_tags = ["[LRU-01] CARBON AIRFRAME", "150 KM C2 RANGE", "180 MIN ENDURANCE", "15 KG PAYLOAD"]
        cur_x = vtol_box_x
        for st in spec_tags:
            tw = len(st) * 8 + 16
            d.rectangle([cur_x, vtol_box_y + 64, cur_x + tw, vtol_box_y + 86], 
                        fill=(10, 26, 52, 220), outline=(56, 189, 248, 80), width=1)
            d.text((cur_x + 8, vtol_box_y + 68), st, fill=(190, 220, 250), font=f_mono_sm)
            cur_x += tw + 10
            
    draw_translucent(render_vtol_header)

    # Paste & Composite Authentic Cyan CAD Lines of VTOL
    try:
        cad = Image.open('assets/vtol_cad_white_lines.png').convert('RGBA')
        c_arr = np.array(cad)
        alpha = c_arr[:, :, 3].astype(float) / 255.0
        
        cyan_cad = np.zeros_like(c_arr)
        cyan_cad[:, :, 0] = (56 * alpha).astype(np.uint8)
        cyan_cad[:, :, 1] = (189 * alpha).astype(np.uint8)
        cyan_cad[:, :, 2] = (248 * alpha).astype(np.uint8)
        cyan_cad[:, :, 3] = (c_arr[:, :, 3] * 0.95).astype(np.uint8)
        
        cad_img = Image.fromarray(cyan_cad)
        cw = 650
        ch = int(cad_img.height * (cw / cad_img.width))
        cad_resized = cad_img.resize((cw, ch), Image.LANCZOS)
        
        v_px, v_py = vtol_box_x + 35, vtol_box_y + 115
        canvas.paste(cad_resized, (v_px, v_py), cad_resized)
        
        # Subsystem Callouts (Meticulously Spaced, Zero Text Overlap!)
        def render_vtol_callouts(d):
            # Translucent forward optical sensor cone
            cone = [
                (v_px + 90, v_py + 155),
                (v_px - 25, v_py + 335),
                (v_px + 175, v_py + 335)
            ]
            d.polygon(cone, fill=(56, 189, 248, 14), outline=(56, 189, 248, 40))
            d.text((v_px - 15, v_py + 342), "EO/IR 30x OPTICAL SCAN CONE", fill=(56, 189, 248, 180), font=f_mono_sm)

            # Callout 1: Wing (Left, Upper)
            c1_x, c1_y = v_px + 95, v_py + 110
            d.ellipse([c1_x - 3, c1_y - 3, c1_x + 3, c1_y + 3], fill=(255, 153, 51, 255))
            d.line([(c1_x, c1_y), (c1_x - 35, c1_y - 25), (c1_x - 110, c1_y - 25)], fill=(255, 153, 51, 220), width=1)
            d.text((c1_x - 110, c1_y - 42), "[LRU-01] QUICK-DISCONNECT WING", fill=(255, 175, 75), font=f_mono_sm)

            # Callout 2: Avionics Core (Upward & Leftward to avoid collision with lift rotors!)
            c2_x, c2_y = v_px + 235, v_py + 105
            d.ellipse([c2_x - 3, c2_y - 3, c2_x + 3, c2_y + 3], fill=(56, 189, 248, 255))
            d.line([(c2_x, c2_y), (c2_x - 20, c2_y - 50), (c2_x + 130, c2_y - 50)], fill=(56, 189, 248, 220), width=1)
            d.text((c2_x - 20, c2_y - 68), "[LRU-02/03] TRIPLE AHRS & AI CORE", fill=(56, 189, 248), font=f_mono_sm)

            # Callout 3: Lift Rotors (Upward & Rightward)
            c3_x, c3_y = v_px + 450, v_py + 85
            d.ellipse([c3_x - 3, c3_y - 3, c3_x + 3, c3_y + 3], fill=(56, 189, 248, 255))
            d.line([(c3_x, c3_y), (c3_x + 40, c3_y - 25), (c3_x + 175, c3_y - 25)], fill=(56, 189, 248, 220), width=1)
            d.text((c3_x + 45, c3_y - 42), "4x HYBRID VTOL LIFT ROTORS", fill=(56, 189, 248), font=f_mono_sm)

            # Callout 4: Payload Bay (Downward & Rightward)
            c4_x, c4_y = v_px + 370, v_py + 160
            d.ellipse([c4_x - 3, c4_y - 3, c4_x + 3, c4_y + 3], fill=(255, 153, 51, 255))
            d.line([(c4_x, c4_y), (c4_x + 45, c4_y + 35), (c4_x + 165, c4_y + 35)], fill=(255, 153, 51, 220), width=1)
            d.text((c4_x + 50, c4_y + 40), "[LRU-05] MODULAR PAYLOAD BAY", fill=(255, 175, 75), font=f_mono_sm)

        draw_translucent(render_vtol_callouts)

    except Exception as e:
        print("Error rendering VTOL CAD:", e)

    # =========================================================================
    # 6. COMPONENT 2: NANO-UAV SWARM (24+ UNITS) (BOTTOM-LEFT)
    # =========================================================================
    swarm_box_x, swarm_box_y = 50, 595
    
    def render_swarm_node(d):
        d.text((swarm_box_x, swarm_box_y), "2. NANO-UAV SWARM (24+ UNITS)", fill=(255, 255, 255), font=f_node_h1)
        d.text((swarm_box_x, swarm_box_y + 34), "AUTONOMOUS SATURATION GRID & MULTI-TARGET RECONNAISSANCE", fill=(255, 175, 75), font=f_node_h2)
        
        # Spec Pills
        swarm_tags = ["24 COOPERATIVE NODES", "AD-HOC MANET MESH", "SELF-HEALING TOPOLOGY", "<85ms LATENCY"]
        cur_x = swarm_box_x
        for st in swarm_tags:
            tw = len(st) * 8 + 16
            d.rectangle([cur_x, swarm_box_y + 64, cur_x + tw, swarm_box_y + 86], 
                        fill=(10, 26, 52, 220), outline=(255, 153, 51, 80), width=1)
            d.text((cur_x + 8, swarm_box_y + 68), st, fill=(255, 195, 120), font=f_mono_sm)
            cur_x += tw + 10

        # Draw 24-Drone Tactical Vector Mesh Formation
        s_rows, s_cols = 4, 6
        s_ox, s_oy = swarm_box_x + 25, swarm_box_y + 115
        s_cw, s_ch = 96, 68

        # Inter-Node Mesh Lines
        for r_i in range(s_rows):
            for c_i in range(s_cols):
                px = s_ox + c_i * s_cw + s_cw // 2
                py = s_oy + r_i * s_ch + s_ch // 2
                
                if c_i < s_cols - 1:
                    d.line([(px, py), (px + s_cw, py)], fill=(56, 189, 248, 60), width=1)
                if r_i < s_rows - 1:
                    d.line([(px, py), (px, py + s_ch)], fill=(56, 189, 248, 60), width=1)
                if c_i < s_cols - 1 and r_i < s_rows - 1:
                    d.line([(px, py), (px + s_cw, py + s_ch)], fill=(56, 189, 248, 25), width=1)
                    d.line([(px + s_cw, py), (px, py + s_ch)], fill=(56, 189, 248, 25), width=1)

        # Draw Each Individual Drone Machine Node
        for r_i in range(s_rows):
            for c_i in range(s_cols):
                px = s_ox + c_i * s_cw + s_cw // 2
                py = s_oy + r_i * s_ch + s_ch // 2
                
                # Ground coverage cones on bottom row
                if r_i == s_rows - 1:
                    cone = [(px, py), (px - 20, py + 34), (px + 20, py + 34)]
                    d.polygon(cone, fill=(56, 189, 248, 16), outline=(56, 189, 248, 45))
                    d.ellipse([px - 14, py + 32, px + 14, py + 36], fill=(56, 189, 248, 30))

                # Quadcopter central fuselage pod
                d.ellipse([px - 10, py - 6, px + 10, py + 6], fill=(10, 28, 56, 250), outline=(56, 189, 248, 220), width=1)
                
                # 4 Carbon motor arms
                arm_r = 16
                d.line([(px - arm_r, py - 9), (px + arm_r, py + 9)], fill=(56, 189, 248, 200), width=2)
                d.line([(px - arm_r, py + 9), (px + arm_r, py - 9)], fill=(56, 189, 248, 200), width=2)
                
                # 4 Motor pods & spinning rotor discs
                r_rx, r_ry = 6, 2
                for mx, my in [(-arm_r, -9), (arm_r, 9), (-arm_r, 9), (arm_r, -9)]:
                    d.ellipse([px + mx - r_rx, py + my - r_ry, px + mx + r_rx, py + my + r_ry],
                              fill=(20, 50, 95, 180), outline=(56, 189, 248, 180), width=1)
                    d.ellipse([px + mx - 1, py + my - 1, px + mx + 1, py + my + 1], fill=(255, 255, 255, 255))
                    
                # Optical seeker dot in center
                s_col = (255, 153, 51, 255) if (r_i == 0 and c_i == 0) else (56, 189, 248, 255)
                d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=s_col)

        # Swarm Status Ribbon
        d.rectangle([swarm_box_x + 25, swarm_box_y + 408, swarm_box_x + 600, swarm_box_y + 438], 
                    fill=(6, 18, 38, 235), outline=(56, 189, 248, 80), width=1)
        d.text((swarm_box_x + 40, swarm_box_y + 416), 
               "SWARM STATUS: 24/24 ONLINE  |  TOPOLOGY: MESH AD-HOC  |  CONSENSUS: LEADERLESS", 
               fill=(56, 189, 248), font=f_mono_sm)

    draw_translucent(render_swarm_node)

    # =========================================================================
    # 7. COMPONENT 3: SECURE DATA LINK (CENTER) - COFDM MANET HUB
    # =========================================================================
    dl_box_x, dl_box_y = 960, 100
    rcx, rcy = 1180, 580
    
    def render_datalink_node(d):
        d.text((dl_box_x, dl_box_y), "3. SECURE DATA LINK", fill=(255, 255, 255), font=f_node_h1)
        d.text((dl_box_x, dl_box_y + 34), "[LRU-04] MANET MESH NETWORK & ANTI-JAM RF HUB", fill=(56, 189, 248), font=f_node_h2)
        
        # Spec Pills in 2 Neat Compact Rows (Zero Overlap with GCS!)
        r1_tags = ["[LRU-04] SECURED MESH", "1.4 / 2.4 GHz DUAL-BAND"]
        cur_x = dl_box_x
        for rt in r1_tags:
            tw = len(rt) * 8 + 16
            d.rectangle([cur_x, dl_box_y + 64, cur_x + tw, dl_box_y + 86], 
                        fill=(10, 26, 52, 220), outline=(56, 189, 248, 80), width=1)
            d.text((cur_x + 8, dl_box_y + 68), rt, fill=(190, 220, 250), font=f_mono_sm)
            cur_x += tw + 10

        r2_tags = ["16x FREQ HOPPING", "AES-256 GCM"]
        cur_x = dl_box_x
        for rt in r2_tags:
            tw = len(rt) * 8 + 16
            d.rectangle([cur_x, dl_box_y + 92, cur_x + tw, dl_box_y + 114], 
                        fill=(10, 26, 52, 220), outline=(56, 189, 248, 80), width=1)
            d.text((cur_x + 8, dl_box_y + 96), rt, fill=(190, 220, 250), font=f_mono_sm)
            cur_x += tw + 10

        # Radiating Concentric Pulse Arcs
        for rad, alpha_val in [(55, 240), (95, 200), (145, 150), (205, 100), (275, 60)]:
            d.arc([rcx - rad, rcy - rad, rcx + rad, rcy + rad], start=125, end=235, fill=(56, 189, 248, alpha_val), width=3)
            d.arc([rcx - rad, rcy - rad, rcx + rad, rcy + rad], start=-55, end=55, fill=(56, 189, 248, alpha_val), width=3)

        # Transmission Mast Structure
        d.line([(rcx, rcy - 110), (rcx, rcy + 80)], fill=(56, 189, 248, 255), width=4)
        d.polygon([(rcx - 50, rcy + 120), (rcx + 50, rcy + 120), (rcx, rcy + 40)], 
                  fill=(8, 26, 56, 245), outline=(56, 189, 248, 240), width=2)
        d.line([(rcx - 30, rcy + 80), (rcx + 30, rcy + 80)], fill=(56, 189, 248, 200), width=2)
        d.line([(rcx - 18, rcy + 58), (rcx + 18, rcy + 58)], fill=(56, 189, 248, 200), width=2)
        
        # Radome & Transceiver Core
        d.ellipse([rcx - 20, rcy - 130, rcx + 20, rcy - 90], fill=(12, 36, 75, 255), outline=(56, 189, 248, 255), width=2)
        d.ellipse([rcx - 8, rcy - 118, rcx + 8, rcy - 102], fill=(255, 255, 255, 255))
        d.arc([rcx - 35, rcy - 85, rcx + 35, rcy - 55], start=180, end=360, fill=(56, 189, 248, 255), width=3)

        # Technical RF Parameter Readout Box
        rf_w, rf_h = 280, 106
        rf_bx, rf_by = rcx - rf_w // 2, rcy + 140
        d.rectangle([rf_bx, rf_by, rf_bx + rf_w, rf_by + rf_h], 
                    fill=(5, 14, 32, 245), outline=(56, 189, 248, 90), width=1)
        # HUD Corner markers
        d.line([(rf_bx, rf_by), (rf_bx + 12, rf_by)], fill=(56, 189, 248, 240), width=2)
        d.line([(rf_bx, rf_by), (rf_bx, rf_by + 12)], fill=(56, 189, 248, 240), width=2)
        d.line([(rf_bx + rf_w, rf_by + rf_h), (rf_bx + rf_w - 12, rf_by + rf_h)], fill=(56, 189, 248, 240), width=2)
        d.line([(rf_bx + rf_w, rf_by + rf_h), (rf_bx + rf_w, rf_by + rf_h - 12)], fill=(56, 189, 248, 240), width=2)
        
        d.text((rf_bx + 14, rf_by + 12), "MANET PROTOCOL: DUAL-BAND", fill=(56, 189, 248), font=f_mono_bld)
        d.text((rf_bx + 14, rf_by + 34), "BAND 1: 1.4 GHz C2 CONTROL", fill=(190, 215, 245), font=f_mono_sm)
        d.text((rf_bx + 14, rf_by + 56), "BAND 2: 2.4 GHz HD VIDEO (15 Mbps)", fill=(190, 215, 245), font=f_mono_sm)
        d.text((rf_bx + 14, rf_by + 78), "SECURITY: AES-256 ENCRYPTED", fill=(255, 175, 75), font=f_mono_bld)

    draw_translucent(render_datalink_node)

    # =========================================================================
    # 8. COMPONENT 4: GROUND CONTROL STATION (RIGHT) - PRECISION MACHINE CONSOLE
    # =========================================================================
    gcs_box_x, gcs_box_y = 1580, 100
    
    def render_gcs_node(d):
        d.text((gcs_box_x, gcs_box_y), "4. GROUND CONTROL STATION", fill=(255, 255, 255), font=f_node_h1)
        d.text((gcs_box_x, gcs_box_y + 34), "[LRU-06] TACTICAL PORTABLE GCS BRIEFCASE WORKSTATION", fill=(56, 189, 248), font=f_node_h2)
        
        # Spec Pills in 2 Neat Compact Rows
        r1_tags = ["17\" SUNLIGHT HUD", "MIL-STD-810H IP67"]
        cur_x = gcs_box_x
        for gt in r1_tags:
            tw = len(gt) * 8 + 16
            d.rectangle([cur_x, gcs_box_y + 64, cur_x + tw, gcs_box_y + 86], 
                        fill=(10, 26, 52, 220), outline=(56, 189, 248, 80), width=1)
            d.text((cur_x + 8, gcs_box_y + 68), gt, fill=(190, 220, 250), font=f_mono_sm)
            cur_x += tw + 10

        r2_tags = ["PILOT DUAL JOYSTICKS", "PORTABLE TABLET"]
        cur_x = gcs_box_x
        for gt in r2_tags:
            tw = len(gt) * 8 + 16
            d.rectangle([cur_x, gcs_box_y + 92, cur_x + tw, gcs_box_y + 114], 
                        fill=(10, 26, 52, 220), outline=(56, 189, 248, 80), width=1)
            d.text((cur_x + 8, gcs_box_y + 96), gt, fill=(190, 220, 250), font=f_mono_sm)
            cur_x += tw + 10

        # High-Tech Vector Machine of Briefcase Console
        gw_x, gw_y = gcs_box_x + 30, gcs_box_y + 145
        deck_y = gw_y + 195
        
        # 1. Lower Case (Chassis Body & Controls Deck)
        d.polygon([
            (gw_x, deck_y + 25),
            (gw_x + 500, deck_y + 25),
            (gw_x + 580, deck_y + 135),
            (gw_x + 80, deck_y + 135)
        ], fill=(10, 24, 48, 250), outline=(56, 189, 248, 180), width=2)
        
        # Heavy Rugged Front Lip / Handle
        d.rectangle([gw_x + 250, deck_y + 133, gw_x + 410, deck_y + 155], 
                    fill=(6, 16, 32, 255), outline=(56, 189, 248, 200), width=2)
        d.text((gw_x + 285, deck_y + 139), "MIL-STD-810H", fill=(56, 189, 248, 200), font=f_mono_sm)
        
        # Pilot Control Joysticks
        for jx in [gw_x + 170, gw_x + 480]:
            jy = deck_y + 80
            d.ellipse([jx - 24, jy - 14, jx + 24, jy + 14], fill=(6, 18, 38, 255), outline=(56, 189, 248, 140), width=1)
            d.line([(jx, jy - 16), (jx, jy + 10)], fill=(56, 189, 248, 220), width=3)
            d.ellipse([jx - 8, jy - 22, jx + 8, jy - 10], fill=(255, 153, 51, 240), outline=(255, 255, 255), width=1)
            
        # Keyboard & Switches
        d.rectangle([gw_x + 225, deck_y + 50, gw_x + 425, deck_y + 110], 
                    fill=(6, 16, 34, 230), outline=(56, 189, 248, 100), width=1)
        for k_row in range(3):
            for k_col in range(12):
                kx = gw_x + 235 + k_col * 15
                ky = deck_y + 60 + k_row * 15
                d.rectangle([kx, ky, kx + 10, ky + 10], fill=(16, 38, 70, 200))

        # 2. Main 17" Primary Sunlight-Readable Tactical Display (Top Lid)
        disp_x, disp_y = gw_x + 20, gw_y
        disp_w, disp_h = 490, 215
        
        d.rectangle([disp_x, disp_y, disp_x + disp_w, disp_y + disp_h], 
                    fill=(6, 16, 34, 255), outline=(56, 189, 248, 220), width=2)
        # Bezel Corner Bumpers
        b_sz = 14
        for bx, by in [(disp_x, disp_y), (disp_x + disp_w, disp_y), (disp_x, disp_y + disp_h), (disp_x + disp_w, disp_y + disp_h)]:
            d.rectangle([bx - b_sz//2, by - b_sz//2, bx + b_sz//2, by + b_sz//2], fill=(56, 189, 248, 200))
            
        # Screen Glass
        s_pad = 12
        sx1, sy1 = disp_x + s_pad, disp_y + s_pad
        sx2, sy2 = disp_x + disp_w - s_pad, disp_y + disp_h - s_pad
        d.rectangle([sx1, sy1, sx2, sy2], fill=(2, 10, 22, 255), outline=(56, 189, 248, 120), width=1)
        
        # Tactical Map Grid on Screen
        for gx in range(sx1, sx2, 35):
            d.line([(gx, sy1), (gx, sy2)], fill=(56, 189, 248, 20), width=1)
        for gy in range(sy1, sy2, 35):
            d.line([(sx1, gy), (sx2, gy)], fill=(56, 189, 248, 20), width=1)
            
        # Radar Sweep Circle
        rad_cx, rad_cy = sx1 + 145, sy1 + 95
        d.ellipse([rad_cx - 68, rad_cy - 68, rad_cx + 68, rad_cy + 68], outline=(56, 189, 248, 90), width=1)
        d.ellipse([rad_cx - 38, rad_cy - 38, rad_cx + 38, rad_cy + 38], outline=(56, 189, 248, 70), width=1)
        d.line([(rad_cx - 68, rad_cy), (rad_cx + 68, rad_cy)], fill=(56, 189, 248, 60), width=1)
        d.line([(rad_cx, rad_cy - 68), (rad_cx, rad_cy + 68)], fill=(56, 189, 248, 60), width=1)
        
        # Active Overwatch UAV Track Marker
        d.polygon([(rad_cx + 18, rad_cy - 26), (rad_cx + 26, rad_cy - 16), (rad_cx + 10, rad_cy - 16)], fill=(56, 189, 248, 255))
        d.text((rad_cx + 32, rad_cy - 28), "OW-01 [1800m]", fill=(56, 189, 248), font=f_mono_sm)
        
        # Swarm Cluster Dots on Radar
        for s_ang in [15, 60, 110, 160, 210, 270, 320]:
            s_r = 34
            s_dx = rad_cx + s_r * math.cos(math.radians(s_ang))
            s_dy = rad_cy + s_r * math.sin(math.radians(s_ang))
            d.ellipse([s_dx - 2, s_dy - 2, s_dx + 2, s_dy + 2], fill=(255, 153, 51, 240))
            
        # Screen Telemetry Panel on Right of Display
        t_px = sx1 + 285
        d.line([(t_px, sy1), (t_px, sy2)], fill=(56, 189, 248, 80), width=1)
        d.text((t_px + 10, sy1 + 10), "MISSION: SATURATION", fill=(255, 175, 75), font=f_mono_sm)
        d.text((t_px + 10, sy1 + 30), "SWARM: 24 NODES", fill=(56, 189, 248), font=f_mono_sm)
        d.text((t_px + 10, sy1 + 50), "GPS: NAVIC RTK FIXED", fill=(190, 215, 245), font=f_mono_sm)
        d.text((t_px + 10, sy1 + 70), "DATALINK: 99.8% RSSI", fill=(56, 189, 248), font=f_mono_sm)
        d.text((t_px + 10, sy1 + 90), "ENCRYPTION: AES-256", fill=(255, 175, 75), font=f_mono_sm)
        d.text((t_px + 10, sy1 + 125), "LAT: 28°36'14\"N", fill=(140, 170, 210), font=f_mono_sm)
        d.text((t_px + 10, sy1 + 145), "LON: 77°12'45\"E", fill=(140, 170, 210), font=f_mono_sm)

        # 3. Secondary Tactical Mission Tablet (Right Side)
        tab_x, tab_y = gw_x + 530, gw_y + 70
        tab_w, tab_h = 175, 200
        d.rectangle([tab_x, tab_y, tab_x + tab_w, tab_y + tab_h], fill=(8, 20, 42, 255), outline=(56, 189, 248, 200), width=2)
        d.rectangle([tab_x + 8, tab_y + 8, tab_x + tab_w - 8, tab_y + tab_h - 8], fill=(3, 12, 26, 255), outline=(56, 189, 248, 100), width=1)
        d.text((tab_x + 14, tab_y + 14), "TACTICAL TABLET", fill=(255, 175, 75), font=f_mono_sm)
        d.text((tab_x + 14, tab_y + 32), "PAYLOAD DISPATCH", fill=(56, 189, 248), font=f_mono_sm)
        for mr in range(3):
            for mc in range(4):
                mpx = tab_x + 28 + mc * 32
                mpy = tab_y + 75 + mr * 32
                d.ellipse([mpx - 3, mpy - 3, mpx + 3, mpy + 3], fill=(56, 189, 248, 200))
                if mc < 3:
                    d.line([(mpx, mpy), (mpx + 32, mpy)], fill=(56, 189, 248, 70), width=1)
                if mr < 2:
                    d.line([(mpx, mpy), (mpx, mpy + 32)], fill=(56, 189, 248, 70), width=1)

        # GCS Callouts (Cleanly routed above display)
        d.line([(disp_x + 150, disp_y), (disp_x + 150, disp_y - 22), (disp_x + 15, disp_y - 22)], fill=(56, 189, 248, 200), width=1)
        d.ellipse([disp_x + 148, disp_y - 2, disp_x + 152, disp_y + 2], fill=(56, 189, 248, 255))
        d.text((disp_x - 175, disp_y - 28), "17\" TACTICAL HUD (1000 NITS)", fill=(56, 189, 248), font=f_mono_sm)

        d.line([(tab_x + 80, tab_y), (tab_x + 80, tab_y - 22), (tab_x + 130, tab_y - 22)], fill=(255, 153, 51, 200), width=1)
        d.ellipse([tab_x + 78, tab_y - 2, tab_x + 82, tab_y + 2], fill=(255, 153, 51, 255))
        d.text((tab_x + 135, tab_y - 28), "PORTABLE CONTROLLER", fill=(255, 175, 75), font=f_mono_sm)

        # GCS Status Box Below
        gcs_stat_x, gcs_stat_y = gw_x, deck_y + 195
        d.rectangle([gcs_stat_x, gcs_stat_y, gcs_stat_x + 700, gcs_stat_y + 42], 
                    fill=(6, 18, 38, 235), outline=(56, 189, 248, 80), width=1)
        d.text((gcs_stat_x + 20, gcs_stat_y + 14), 
                  "C2 DISPATCH: REAL-TIME FLIGHT PLANNER  |  ENCRYPTION: AES-256 GCM  |  RUGGED: IP67 / MIL-STD-810H", 
                  fill=(56, 189, 248), font=f_mono_sm)

    draw_translucent(render_gcs_node)

    # =========================================================================
    # 9. HIGH-TECH VECTOR DATA PIPELINES (CLEAN, GLOWING, ZERO OVERLAP)
    # =========================================================================
    def render_pipelines(d):
        def draw_pipe(p1, p2, color=(56, 189, 248)):
            x1, y1 = p1
            x2, y2 = p2
            length = math.hypot(x2 - x1, y2 - y1)
            if length == 0:
                return
            dx = (x2 - x1) / length
            dy = (y2 - y1) / length
            
            # Subtle glow line
            d.line([p1, p2], fill=(color[0], color[1], color[2], 30), width=6)
            # Dashed core line
            dash_sz = 14
            gap_sz = 9
            curr = 0
            while curr < length - 18:
                sx = x1 + dx * curr
                sy = y1 + dy * curr
                ex = x1 + dx * min(curr + dash_sz, length - 18)
                ey = y1 + dy * min(curr + dash_sz, length - 18)
                d.line([(sx, sy), (ex, ey)], fill=(color[0], color[1], color[2], 240), width=2)
                curr += dash_sz + gap_sz
                
            # Directional Arrow Head
            ah_l = 15
            ah_w = 6
            bx = x2 - dx * ah_l
            by = y2 - dy * ah_l
            px = -dy * ah_w
            py = dx * ah_w
            d.polygon([(x2, y2), (bx + px, by + py), (bx - px, by - py)], fill=(color[0], color[1], color[2], 255))

        def draw_pipe_label(x, y, text, color=(56, 189, 248)):
            tw = len(text) * 8 + 18
            d.rectangle([x, y, x + tw, y + 26], fill=(4, 12, 28, 255), outline=(color[0], color[1], color[2], 160), width=1)
            d.text((x + 9, y + 5), text, fill=color, font=f_mono_sm)

        # Pipeline 1: Overwatch UAV <===> RF Datalink Hub (Bidirectional)
        draw_pipe((710, 290), (1020, 500), color=(56, 189, 248))
        draw_pipe((1020, 520), (710, 310), color=(56, 189, 248))
        draw_pipe_label(760, 370, "C2 RELAY BACKBONE (150 KM)", color=(56, 189, 248))

        # Pipeline 2: Swarm Grid <===> RF Datalink Hub (Bidirectional)
        draw_pipe((710, 770), (1020, 640), color=(56, 189, 248))
        draw_pipe((1020, 660), (710, 790), color=(56, 189, 248))
        draw_pipe_label(730, 725, "MANET INTRA-SWARM MESH (<85ms)", color=(56, 189, 248))

        # Pipeline 3: RF Datalink Hub <===> Ground Control Station (Bidirectional)
        draw_pipe((1340, 560), (1570, 560), color=(56, 189, 248))
        draw_pipe((1570, 580), (1340, 580), color=(255, 153, 51))
        draw_pipe_label(1330, 515, "MISSION DISPATCH & 1080P HD STREAM", color=(56, 189, 248))

        # Pipeline 4: Direct Vertical Swarm Command (Overwatch directly down to Swarm)
        draw_pipe((380, 485), (380, 585), color=(255, 153, 51))
        draw_pipe((405, 585), (405, 485), color=(255, 153, 51))
        # Place label cleanly to the right of the vertical arrows
        draw_pipe_label(425, 520, "DIRECT AIRBORNE C2", color=(255, 153, 51))

    draw_translucent(render_pipelines)

    # 10. Composite Onto Fully Opaque RGB Canvas & Save
    final_output = Image.new('RGB', (W, H), (4, 10, 24))
    final_output.paste(canvas, (0, 0), canvas)
    
    out_file = 'assets/swarm_architecture_blue_master.png'
    final_output.save(out_file, 'PNG', quality=100)
    print(f"Master Machine Infographic generated successfully: {out_file} ({W}x{H}) [OPAQUE RGB]")

if __name__ == '__main__':
    create_master_infographic()
