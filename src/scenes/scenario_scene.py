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
        title = Text("Scenario Setup", color=WHITE)
        title.set_stroke(color=BLACK, width=1.5)
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
        
        # 3. Car
        # Position: Left of bollard.
        # Gap between car nose and bollard surface.
        gap = 1.5 # m
        # Bollard surface x = bollard_x - BOLLARD_R
        bollard_surface_x = bollard_x - BOLLARD_R
        nose_x = bollard_surface_x - gap
        
        car_group = VGroup()
        
        # Define Car Points in Meters relative to Front Wheel Center (0, R)
        # Front wheel at (0, R)
        # Rear wheel at (-WB, R)
        
        fw_center = np.array([0, CAR_WHEEL_R, 0])
        rw_center = np.array([-CAR_WHEELBASE, CAR_WHEEL_R, 0])
        
        # Wheels
        w1 = Circle(radius=CAR_WHEEL_R * SCALE, color=WHITE, stroke_width=1.5).move_to(rw_center * SCALE)
        w2 = Circle(radius=CAR_WHEEL_R * SCALE, color=WHITE, stroke_width=1.5).move_to(fw_center * SCALE)
        
        # Arches
        arch_r = CAR_WHEEL_R + 0.05
        arch1 = Arc(radius=arch_r * SCALE, start_angle=0, angle=PI, color=WHITE, stroke_width=1.5).move_to(rw_center * SCALE)
        arch2 = Arc(radius=arch_r * SCALE, start_angle=0, angle=PI, color=WHITE, stroke_width=1.5).move_to(fw_center * SCALE)
        
        # Body Geometry (Meters)
        overhang_f = 0.9
        overhang_r = 1.0
        
        # Key X coordinates relative to front wheel (0)
        x_nose = overhang_f
        x_hood_base = -0.2
        x_roof_front = -0.8
        x_roof_rear = -2.0
        x_trunk_front = -2.5
        x_trunk_rear = -CAR_WHEELBASE - overhang_r + 0.2
        x_rear = -CAR_WHEELBASE - overhang_r
        
        # Key Y coordinates (Height from ground)
        y_nose = CAR_NOSE_H # 0.56
        y_hood = 0.85
        y_roof = 1.45
        y_trunk = 1.0
        y_bottom = 0.35
        
        # Points loop
        pts_m = [
            [x_rear, y_bottom, 0],
            [x_rear, 0.65, 0], # Rear bumper top
            [x_trunk_rear, y_trunk, 0],
            [x_trunk_front, y_trunk, 0],
            [x_roof_rear, y_roof, 0],
            [x_roof_front, y_roof, 0],
            [x_hood_base, y_hood, 0],
            [x_nose - 0.1, 0.8, 0], # Hood tip
            [x_nose, y_nose, 0], # Nose / Impact Point
            [x_nose - 0.1, y_bottom, 0]
        ]
        
        # Scale points
        pts_scaled = [np.array(p) * SCALE for p in pts_m]
        
        body_outline = VMobject(color=WHITE, stroke_width=1.5)
        body_outline.set_points_as_corners(pts_scaled)
        
        # Connect bottom lines
        # Rear bottom to Rear Arch Start
        l1 = Line(pts_scaled[0], arch1.get_start(), color=WHITE, stroke_width=1.5)
        # Rear Arch End to Front Arch Start
        l2 = Line(arch1.get_end(), arch2.get_start(), color=WHITE, stroke_width=1.5)
        # Front Arch End to Front Bottom
        l3 = Line(arch2.get_end(), pts_scaled[-1], color=WHITE, stroke_width=1.5)
        
        # Window detail
        win_line = Line(
            np.array([x_trunk_front, y_trunk - 0.05, 0]) * SCALE,
            np.array([x_hood_base, y_hood - 0.05, 0]) * SCALE,
            color=WHITE, stroke_width=1
        )
        
        car_design = VGroup(w1, w2, arch1, arch2, body_outline, l1, l2, l3, win_line)
        
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
        
        marker_label = Text(f"Impact height = {IMPACT_H} m", font_size=18, color=CYAN)
        marker_label.set_stroke(color=BLACK, width=1.5)
        marker_label.next_to(marker_line, UP, buff=0.1)
        
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
        text_config = {"font_size": 20, "color": WHITE}
        
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
            t.set_stroke(color=BLACK, width=1.5)
            
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
        
        t_label = Text("t = free variable", font_size=20, color=CYAN)
        t_label.set_stroke(color=BLACK, width=1.5)
        t_label.next_to(out_cap, UP, buff=0.5)
        
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
