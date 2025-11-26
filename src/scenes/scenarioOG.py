from manim import *

Text.set_default(font="Segoe UI")
CYAN = "#00FFFF"

class ScenarioScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # --- Parameters (in meters) ---
        # We define everything in real-world units first, then scale them.
        SCALE = 1.8 # Units per meter
        
        # Dimensions
        BOLLARD_H = 1.2      # m (Visual height adjusted)
        BOLLARD_D = 0.275    # m
        BOLLARD_R = BOLLARD_D / 2
        WALL_T = 0.04        # m (Visual thickness)
        
        IMPACT_H = 0.56      # m
        
        CAR_WHEEL_R = 0.3    # m
        CAR_WHEELBASE = 2.7  # m
        CAR_NOSE_H = IMPACT_H # m (Align bumper with impact)
        
        # --- Phase 1: Title ---
        title = Text("Scenario Setup", font_size=48, color=WHITE, weight=BOLD)
        title.set_stroke(color=BLACK, width=6.0, background=True)
        title.to_edge(UP, buff=0.5)
        
        self.play(FadeIn(title, run_time=1.2))
        self.wait(0.5)
        
        # --- Phase 2: Diagram Construction ---
        diagram = VGroup()
        
        # 1. Ground Line
        ground_len = 10.0 # m
        ground_line = Line(LEFT * (ground_len/2) * SCALE, RIGHT * (ground_len/2) * SCALE, color=WHITE, stroke_width=2)
        # We will position the whole diagram later, so build relative to origin (0,0) as ground center for now.
        # Actually, let's build with y=0 as ground level.
        ground_line.move_to(ORIGIN)
        
        # 2. Bollard
        # Position: To the right
        bollard_x = 2.0 # m from center
        
        # Visual Height Adjustment:
        # The bollard is a cylinder. In 2D projection (blueprint), it's a rectangle with ellipses.
        # The "height" 0.9m is from ground to the very top.
        # Top ellipse center is at y = H - cap_radius_y.
        # Let's define cap visual height.
        cap_h_visual = BOLLARD_D * 0.35 # Visual squash factor
        cap_r_y = cap_h_visual / 2
        
        rect_h = BOLLARD_H - cap_r_y
        
        # Create Bollard Group
        bollard_group = VGroup()
        
        # Outer Body (Rectangle)
        # Center of rect is at x=bollard_x, y=rect_h/2
        body = Rectangle(
            width=BOLLARD_D * SCALE, 
            height=rect_h * SCALE, 
            color=WHITE, 
            stroke_width=2
        )
        body.move_to(np.array([bollard_x * SCALE, (rect_h/2) * SCALE, 0]))
        
        # Caps
        top_cap = Ellipse(
            width=BOLLARD_D * SCALE, 
            height=cap_h_visual * SCALE, 
            color=WHITE, 
            stroke_width=2
        )
        top_cap.move_to(body.get_top())
        
        bottom_cap = Ellipse(
            width=BOLLARD_D * SCALE, 
            height=cap_h_visual * SCALE, 
            color=WHITE, 
            stroke_width=2
        )
        bottom_cap.move_to(body.get_bottom())
        
        # Inner Wall (Thin-walled)
        inner_d = BOLLARD_D - 2*WALL_T
        inner_w = inner_d * SCALE
        
        inner_left = DashedLine(
            start=body.get_bottom() + LEFT * (inner_w/2),
            end=body.get_top() + LEFT * (inner_w/2),
            color=GRAY, stroke_width=1
        )
        inner_right = DashedLine(
            start=body.get_bottom() + RIGHT * (inner_w/2),
            end=body.get_top() + RIGHT * (inner_w/2),
            color=GRAY, stroke_width=1
        )
        
        inner_cap = Ellipse(
            width=inner_w, 
            height=(inner_d * 0.35) * SCALE, # Keep aspect ratio roughly same
            color=GRAY, 
            stroke_width=1
        )
        inner_cap.move_to(body.get_top())
        
        bollard_group.add(body, top_cap, bottom_cap, inner_left, inner_right, inner_cap)
        
        # 3. Mercedes Sprinter Van (Refined Wireframe)
        # Position: Left of bollard.
        gap = 1.5 # m
        bollard_surface_x = bollard_x - BOLLARD_R
        nose_x = bollard_surface_x - gap
        
        car_group = VGroup()
        
        # Wheel positioning
        fw_center = np.array([0, CAR_WHEEL_R, 0])
        rw_center = np.array([-CAR_WHEELBASE, CAR_WHEEL_R, 0])
        
        # Wheels - outer tires
        w1 = Circle(radius=CAR_WHEEL_R * SCALE, color=WHITE, stroke_width=2).move_to(rw_center * SCALE)
        w2 = Circle(radius=CAR_WHEEL_R * SCALE, color=WHITE, stroke_width=2).move_to(fw_center * SCALE)
        
        # Inner rims
        rim1 = Circle(radius=(CAR_WHEEL_R * 0.45) * SCALE, color=WHITE, stroke_width=1).move_to(rw_center * SCALE)
        rim2 = Circle(radius=(CAR_WHEEL_R * 0.45) * SCALE, color=WHITE, stroke_width=1).move_to(fw_center * SCALE)
        
        # Sprinter Body Geometry - Accurate Proportions
        overhang_f = 0.9
        overhang_r = 1.0
        
        # X coordinates - refined for Sprinter profile
        x_nose = overhang_f
        x_bumper_mid = 0.8
        x_bumper_low = 0.7
        x_grille_top = 0.65
        x_hood_end = 0.45
        x_hood_start = 0.1
        x_cowl = -0.05  # Where hood meets windshield
        x_windshield_top = -0.55
        x_a_pillar_top = -0.65
        x_a_pillar_base = -0.5
        x_b_pillar = -1.3
        x_c_pillar = -1.95
        x_d_pillar = -2.5
        x_rear_corner = -CAR_WHEELBASE - overhang_r + 0.25
        x_rear = -CAR_WHEELBASE - overhang_r
        
        # Y coordinates - High-roof Sprinter
        y_ground = 0.35
        y_rocker = 0.48  # Lower body panel
        y_bumper_bottom = CAR_NOSE_H  # 0.56 - impact height
        y_bumper_mid = 0.7
        y_bumper_top = 0.82
        y_grille_top = 0.95
        y_hood_surface = 1.08
        y_cowl = 1.12  # Base of windshield
        y_windshield_mid = 1.65
        y_windshield_top = 1.82
        y_roof = 1.95
        y_window_top = 1.78
        y_window_bottom = 1.12
        y_body_character = 1.18  # Character line height
        y_door_top = 1.72
        y_door_bottom = 0.52
        
        # Main body outline - more accurate Sprinter profile
        body_points = [
            # Start from rear bottom
            [x_rear, y_ground, 0],
            [x_rear, y_door_top, 0],
            # Rear cargo area curve to roof
            [x_rear_corner, y_door_top + 0.12, 0],
            [x_d_pillar + 0.1, y_roof - 0.03, 0],
            # Roof line (flat)
            [x_d_pillar, y_roof, 0],
            [x_c_pillar, y_roof, 0],
            [x_b_pillar, y_roof, 0],
            [x_a_pillar_top - 0.05, y_roof, 0],
            [x_a_pillar_top, y_roof - 0.02, 0],
            # Windshield (more reclined angle)
            [x_windshield_top, y_windshield_top, 0],
            [x_a_pillar_base, y_windshield_mid, 0],
            [x_cowl, y_cowl, 0],
            # Hood
            [x_hood_start, y_hood_surface, 0],
            [x_hood_end, y_hood_surface, 0],
            # Front grille area
            [x_grille_top, y_grille_top, 0],
            # Bumper (sloped, not vertical)
            [x_bumper_low, y_bumper_top, 0],
            [x_bumper_mid, y_bumper_mid, 0],
            [x_nose, y_bumper_bottom, 0],
            # Bottom front (rounded transition)
            [x_nose - 0.02, y_rocker, 0],
            [x_nose - 0.05, y_ground, 0]
        ]
        
        body_scaled = [np.array(p) * SCALE for p in body_points]
        body_outline = VMobject(color=WHITE, stroke_width=2)
        body_outline.set_points_as_corners(body_scaled)
        
        # Wheel arches - properly positioned to avoid overlaps
        arch_r = CAR_WHEEL_R + 0.06
        # Front arch - positioned to avoid body overlap
        front_arch_start = fw_center + np.array([arch_r * np.cos(2.9), arch_r * np.sin(2.9), 0])
        front_arch_end = fw_center + np.array([arch_r * np.cos(0.24), arch_r * np.sin(0.24), 0])
        arch2 = Arc(radius=arch_r * SCALE, start_angle=0.24, angle=2.66, color=WHITE, stroke_width=2).move_to(fw_center * SCALE)
        
        # Rear arch
        rear_arch_start = rw_center + np.array([arch_r * np.cos(2.9), arch_r * np.sin(2.9), 0])
        rear_arch_end = rw_center + np.array([arch_r * np.cos(0.24), arch_r * np.sin(0.24), 0])
        arch1 = Arc(radius=arch_r * SCALE, start_angle=0.24, angle=2.66, color=WHITE, stroke_width=2).move_to(rw_center * SCALE)
        
        # Bottom body panel - connects rear to front with wheel arches
        # Rear section to rear wheel
        rocker_rear_start = np.array([x_rear, y_rocker, 0]) * SCALE
        rocker_rear_wheel = (rw_center + np.array([arch_r * np.cos(2.9), arch_r * np.sin(2.9), 0])) * SCALE
        bottom_l1 = Line(rocker_rear_start, rocker_rear_wheel, color=WHITE, stroke_width=2)
        
        # Between wheels
        rocker_mid_start = (rw_center + np.array([arch_r * np.cos(0.24), arch_r * np.sin(0.24), 0])) * SCALE
        rocker_mid_end = (fw_center + np.array([arch_r * np.cos(2.9), arch_r * np.sin(2.9), 0])) * SCALE
        bottom_l2 = Line(rocker_mid_start, rocker_mid_end, color=WHITE, stroke_width=2)
        
        # Front wheel to front
        rocker_front_wheel = (fw_center + np.array([arch_r * np.cos(0.24), arch_r * np.sin(0.24), 0])) * SCALE
        rocker_front_end = body_scaled[-1]
        bottom_l3 = Line(rocker_front_wheel, rocker_front_end, color=WHITE, stroke_width=2)
        
        # === WINDOWS ===
        # Front windshield - polygon for accurate shape
        windshield = Polygon(
            np.array([x_windshield_top, y_windshield_top - 0.02, 0]) * SCALE,
            np.array([x_cowl + 0.03, y_cowl + 0.02, 0]) * SCALE,
            np.array([x_a_pillar_base - 0.02, y_cowl + 0.02, 0]) * SCALE,
            np.array([x_a_pillar_top - 0.02, y_roof - 0.08, 0]) * SCALE,
            color=WHITE, stroke_width=1.5, fill_opacity=0
        )
        
        # Driver/passenger side window
        driver_win_w = (x_a_pillar_top - x_b_pillar - 0.12) * SCALE
        driver_win_h = (y_window_top - y_window_bottom) * SCALE
        driver_window = Rectangle(
            width=driver_win_w,
            height=driver_win_h,
            color=WHITE, stroke_width=1.5
        ).move_to(np.array([(x_a_pillar_top + x_b_pillar)/2 - 0.06, (y_window_top + y_window_bottom)/2, 0]) * SCALE)
        
        # Cargo window 1 (between B and C pillar)
        cargo_win_1_w = (x_b_pillar - x_c_pillar - 0.2) * SCALE
        cargo_win_1_h = (y_window_top - y_window_bottom - 0.08) * SCALE
        cargo_window_1 = Rectangle(
            width=cargo_win_1_w,
            height=cargo_win_1_h,
            color=WHITE, stroke_width=1.5
        ).move_to(np.array([(x_b_pillar + x_c_pillar)/2, (y_window_top + y_window_bottom)/2 - 0.04, 0]) * SCALE)
        
        # Cargo window 2 (between C and D pillar)
        cargo_win_2_w = (x_c_pillar - x_d_pillar - 0.2) * SCALE
        cargo_win_2_h = (y_window_top - y_window_bottom - 0.08) * SCALE
        cargo_window_2 = Rectangle(
            width=cargo_win_2_w,
            height=cargo_win_2_h,
            color=WHITE, stroke_width=1.5
        ).move_to(np.array([(x_c_pillar + x_d_pillar)/2, (y_window_top + y_window_bottom)/2 - 0.04, 0]) * SCALE)
        
        # === PANEL LINES & DETAILS ===
        # Sliding door outline (between B and C pillars)
        slide_door_w = (x_b_pillar - x_c_pillar - 0.08) * SCALE
        slide_door_h = (y_door_top - y_door_bottom) * SCALE
        sliding_door = Rectangle(
            width=slide_door_w,
            height=slide_door_h,
            color=GRAY, stroke_width=1.2
        ).move_to(np.array([(x_b_pillar + x_c_pillar)/2, (y_door_top + y_door_bottom)/2, 0]) * SCALE)
        
        # Door handle
        door_handle = Line(
            np.array([x_b_pillar - 0.2, y_window_bottom + 0.2, 0]) * SCALE,
            np.array([x_b_pillar - 0.35, y_window_bottom + 0.2, 0]) * SCALE,
            color=WHITE, stroke_width=1.5
        )
        
        # Rear cargo door separation line
        rear_door_sep = Line(
            np.array([x_rear_corner + 0.18, y_rocker + 0.05, 0]) * SCALE,
            np.array([x_rear_corner + 0.18, y_door_top, 0]) * SCALE,
            color=GRAY, stroke_width=1.2
        )
        
        # Body character line (runs full length)
        character_line = Line(
            np.array([x_hood_end, y_body_character, 0]) * SCALE,
            np.array([x_rear - 0.03, y_body_character - 0.12, 0]) * SCALE,
            color=GRAY, stroke_width=1
        )
        
        # Rocker panel line (lower edge)
        rocker_line = Line(
            np.array([x_bumper_mid, y_rocker, 0]) * SCALE,
            np.array([x_rear, y_rocker, 0]) * SCALE,
            color=GRAY, stroke_width=0.8
        )
        
        # Roof drip rail/gutter
        roof_rail = Line(
            np.array([x_a_pillar_top, y_roof - 0.06, 0]) * SCALE,
            np.array([x_d_pillar, y_roof - 0.06, 0]) * SCALE,
            color=GRAY, stroke_width=0.8
        )
        
        # === FRONT END DETAILS ===
        # Grille rectangle
        grille_w = 0.14 * SCALE
        grille_h = (y_grille_top - y_bumper_top - 0.08) * SCALE
        grille = Rectangle(
            width=grille_w,
            height=grille_h,
            color=WHITE, stroke_width=1.5
        ).move_to(np.array([x_grille_top - 0.07, (y_grille_top + y_bumper_top)/2 + 0.04, 0]) * SCALE)
        
        # Grille horizontal slats
        grille_slats = VGroup()
        for i in range(3):
            slat_y = y_bumper_top + 0.08 + (y_grille_top - y_bumper_top - 0.16) * (i + 1) / 4
            slat = Line(
                np.array([x_grille_top - 0.02, slat_y, 0]) * SCALE,
                np.array([x_grille_top - 0.12, slat_y, 0]) * SCALE,
                color=GRAY, stroke_width=1
            )
            grille_slats.add(slat)
        
        # Mercedes star emblem
        emblem = Circle(
            radius=0.045 * SCALE,
            color=WHITE,
            stroke_width=1.5
        ).move_to(np.array([x_grille_top - 0.07, (y_grille_top + y_bumper_top)/2 + 0.04, 0]) * SCALE)
        
        # Headlight
        headlight = Ellipse(
            width=0.2 * SCALE,
            height=0.11 * SCALE,
            color=WHITE,
            stroke_width=1.5
        ).move_to(np.array([x_hood_end + 0.02, y_grille_top + 0.08, 0]) * SCALE)
        
        # Front turn signal/marker light (small)
        marker_light = Ellipse(
            width=0.08 * SCALE,
            height=0.045 * SCALE,
            color=WHITE,
            stroke_width=1
        ).move_to(np.array([x_grille_top + 0.02, y_bumper_mid - 0.03, 0]) * SCALE)
        
        # Side mirror
        mirror_mount = Line(
            np.array([x_windshield_top - 0.1, y_windshield_top - 0.18, 0]) * SCALE,
            np.array([x_windshield_top - 0.2, y_windshield_top - 0.08, 0]) * SCALE,
            color=WHITE, stroke_width=1.5
        )
        mirror_housing = Ellipse(
            width=0.16 * SCALE,
            height=0.09 * SCALE,
            color=WHITE,
            stroke_width=1.5
        ).move_to(np.array([x_windshield_top - 0.24, y_windshield_top - 0.05, 0]) * SCALE)
        
        # Front lower air dam detail
        air_dam = Line(
            np.array([x_bumper_low - 0.05, y_bumper_bottom + 0.02, 0]) * SCALE,
            np.array([x_bumper_mid - 0.03, y_bumper_bottom + 0.02, 0]) * SCALE,
            color=GRAY, stroke_width=0.8
        )
        
        # Assemble complete van
        car_design = VGroup(
            # Wheels and arches
            w1, w2, rim1, rim2, arch1, arch2,
            # Main body
            body_outline, bottom_l1, bottom_l2, bottom_l3,
            # Windows
            windshield, driver_window, cargo_window_1, cargo_window_2,
            # Doors and panels
            sliding_door, door_handle, rear_door_sep,
            # Body lines
            character_line, rocker_line, roof_rail,
            # Front details
            grille, grille_slats, emblem, headlight, marker_light, air_dam,
            # Mirror
            mirror_mount, mirror_housing
        )
        
        # Now position the car
        # The car design is centered around front wheel at (0,0) in local design space (scaled).
        # We want the Nose (x_nose * SCALE) to be at `nose_x * SCALE` in the scene.
        # Current Nose X in design = x_nose * SCALE
        # Target Nose X in scene = nose_x * SCALE
        # Shift = (nose_x - x_nose) * SCALE
        
        shift_vec = np.array([(nose_x - x_nose) * SCALE, 0, 0])
        car_design.shift(shift_vec)
        
        car_group.add(car_design)
        
        # 4. Impact Elements
        # Impact Height Line
        impact_y = IMPACT_H * SCALE
        
        # Line from car nose to bollard
        # Car nose x = nose_x * SCALE
        # Bollard left x = (bollard_x - BOLLARD_R) * SCALE
        
        p_start = np.array([nose_x * SCALE + 0.2, impact_y, 0])
        p_end = np.array([(bollard_x - BOLLARD_R) * SCALE - 0.2, impact_y, 0])
        
        marker_line = DashedLine(start=p_start, end=p_end, color=CYAN, stroke_width=1.5)
        
        marker_label = Text(f"Impact height = {IMPACT_H} m", font_size=26, color=CYAN, weight=BOLD)
        marker_label.set_stroke(color=BLACK, width=5.0, background=True)
        marker_label.next_to(marker_line, UP, buff=0.15)
        
        # Arrow
        arrow_start = np.array([nose_x * SCALE, impact_y, 0])
        arrow_end = np.array([(bollard_x - BOLLARD_R) * SCALE, impact_y, 0])
        
        impact_arrow = Arrow(
            start=arrow_start, 
            end=arrow_end, 
            color=CYAN, 
            buff=0.1,
            max_tip_length_to_length_ratio=0.25
        )
        impact_arrow.set_color_by_gradient(WHITE, CYAN)
        arrow_glow = impact_arrow.copy().set_stroke(width=8, opacity=0.3).set_color(CYAN)
        
        impact_group = VGroup(marker_line, marker_label, impact_arrow, arrow_glow)
        
        # Combine Diagram
        diagram.add(ground_line, bollard_group, car_group, impact_group)
        
        # Center Diagram
        diagram.move_to(ORIGIN + DOWN * 0.5)
        
        # --- Phase 3: Text Layout ---
        text_config = {"font_size": 28, "color": WHITE, "weight": BOLD}
        
        # Top Left
        t1 = Text("Public building scenario", **text_config)
        t2 = Text(f"Vehicle impact at {IMPACT_H} m", **text_config)
        group_tl = VGroup(t1, t2).arrange(DOWN, aligned_edge=LEFT).to_corner(UL, buff=0.5)
        
        # Top Right
        t3 = Text("Energy: 250 kJ", **text_config)
        t4 = Text("Force: 6.27 MN", **text_config)
        group_tr = VGroup(t3, t4).arrange(DOWN, aligned_edge=RIGHT).to_corner(UR, buff=0.5)
        
        # Bottom Left (Dimensions) - Moved to Right of Bollard
        t5 = Text("h = 0.9 m", **text_config)
        t6 = Text(f"d = {BOLLARD_D} m", **text_config)
        group_bl = VGroup(t5, t6).arrange(DOWN, aligned_edge=LEFT)
        group_bl.next_to(bollard_group, RIGHT, buff=0.5)
        
        # Bottom Right (Notes) - Moved to Center Bottom
        t7 = Text("Thickness t depends on material", **text_config)
        t8 = Text("Assume fixed base", **text_config)
        group_br = VGroup(t7, t8).arrange(DOWN, aligned_edge=ORIGIN).to_edge(DOWN, buff=0.5)
        
        all_text = VGroup(group_tl, group_tr, group_bl, group_br)
        for t in all_text:
            t.set_stroke(color=BLACK, width=5.0, background=True)
            
        # --- Animation ---
        
        # 1. Environment
        self.play(Create(ground_line, run_time=1.0))
        self.play(Create(bollard_group, run_time=1.0))
        self.play(FadeIn(car_group, shift=RIGHT, run_time=1.5))
        
        # 2. Impact Info
        self.play(Create(marker_line), FadeIn(marker_label), run_time=1.0)
        self.play(FadeIn(arrow_glow), GrowArrow(impact_arrow), run_time=1.0)
        
        # 3. Text Part 1
        self.play(FadeIn(group_tl), FadeIn(group_tr), run_time=1.0)
        self.wait(15.0)
        
        # 4. Text Part 2
        self.play(FadeIn(group_bl), FadeIn(group_br), run_time=1.0)
        
        # 5. Highlight t
        # Get current bollard parts
        # diagram -> bollard_group (index 1)
        # bollard_group -> top_cap (index 1), inner_cap (index 5)
        
        # Since we moved the diagram, we need to access the moved mobjects
        # But VGroup structure is preserved.
        
        b_grp = diagram[1]
        out_cap = b_grp[1]
        in_cap = b_grp[5]
        
        t_ring = Difference(out_cap, in_cap, color=CYAN, fill_opacity=0.5, stroke_width=0)
        t_ring.set_z_index(10)
        
        # Highlight side walls (thin rectangles)
        # Left wall: from left edge to left edge + wall thickness
        # Right wall: from right edge - wall thickness to right edge
        
        # We need dimensions in scene units
        # bollard_group -> body is index 0
        body_rect = b_grp[0]
        
        # Wall thickness in scene units
        wall_t_scene = WALL_T * SCALE
        
        # Create rectangles for walls
        # Left wall
        wall_l = Rectangle(
            width=wall_t_scene,
            height=body_rect.height,
            color=CYAN,
            fill_opacity=0.5,
            stroke_width=0
        )
        # Position: Left edge aligns with body left edge
        wall_l.move_to(body_rect.get_left() + RIGHT * (wall_t_scene/2))
        
        # Right wall
        wall_r = Rectangle(
            width=wall_t_scene,
            height=body_rect.height,
            color=CYAN,
            fill_opacity=0.5,
            stroke_width=0
        )
        # Position: Right edge aligns with body right edge
        wall_r.move_to(body_rect.get_right() + LEFT * (wall_t_scene/2))
        
        wall_l.set_z_index(10)
        wall_r.set_z_index(10)
        
        t_label = Text("t = free variable", font_size=28, color=CYAN, weight=BOLD)
        t_label.set_stroke(color=BLACK, width=5.0, background=True)
        t_label.next_to(out_cap, UP, buff=0.6)
        
        self.play(
            FadeIn(t_ring), 
            FadeIn(wall_l), 
            FadeIn(wall_r), 
            FadeIn(t_label), 
            run_time=1.0
        )
        self.play(
            Flash(t_ring, color=CYAN, line_length=0.2),
            Flash(wall_l, color=CYAN, line_length=0.2),
            Flash(wall_r, color=CYAN, line_length=0.2)
        )
        
        self.wait(15.0)
        
        # 6. Exit
        self.play(
            FadeOut(diagram),
            FadeOut(all_text),
            FadeOut(t_ring),
            FadeOut(t_label),
            FadeOut(title),
            run_time=1.5
        )
        self.wait(0.5)
