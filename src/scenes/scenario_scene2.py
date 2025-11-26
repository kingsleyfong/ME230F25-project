from manim import *

# Set default font to Segoe UI with BOLD weight for better visibility
Text.set_default(font="Segoe UI", weight="BOLD")

class ScenarioScene(Scene):
    def construct(self):
        # PHASE 0 — Imports and global style
        self.camera.background_color = BLACK
        
        # Color constants
        WHITE = ManimColor.from_rgb((1.0, 1.0, 1.0))
        CYAN = ManimColor.from_rgb((0.0, 1.0, 1.0)) # Highlight color

        # ------------------------------------------------------------
        # PHASE 1 – Title and environment
        # ------------------------------------------------------------

        # Title
        title = Text("Scenario – K4 security bollard", color=WHITE, font_size=48)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title, run_time=1.0))

        # 1) Ground line (Y= -1.5)
        GROUND_Y = -1.5
        ground_line = Line(LEFT * config.frame_width / 2, RIGHT * config.frame_width / 2, color=WHITE, stroke_width=3)
        ground_line.move_to(np.array([0, GROUND_Y, 0]))
        self.play(Create(ground_line))

        # 2) Road region (Left Side)
        ROAD_X_LIMIT = -2.0
        # Darker gray band above the ground line on the left
        road_region = Rectangle(
            width=(config.frame_width / 2) + ROAD_X_LIMIT,
            height=0.5,
            fill_opacity=0.3,
            fill_color=GREY_E,
            stroke_width=0
        )
        road_region.move_to(np.array([ROAD_X_LIMIT - (road_region.width / 2), GROUND_Y + road_region.height / 2, 0]))
        road_label = Text("Busy road", font_size=24, color=WHITE).next_to(road_region, UP, buff=0.1).shift(LEFT*1.0)
        
        # 3) Public building (Right Side)
        BUILDING_X_START = 3.0
        BUILDING_HEIGHT = 4.0
        BUILDING_WIDTH = 3.0
        building = Rectangle(
            width=BUILDING_WIDTH, 
            height=BUILDING_HEIGHT, 
            color=WHITE, 
            fill_opacity=0.1, 
            stroke_width=2
        )
        building.align_to(ground_line, DOWN)
        building.to_edge(RIGHT, buff=0.5)

        building_label = Text("Public building", font_size=24, color=WHITE).next_to(building, UP, buff=0.1)

        self.play(
            FadeIn(building, shift=UP*0.5, run_time=0.7),
            FadeIn(building_label, run_time=0.7),
            FadeIn(road_region, run_time=0.7),
            FadeIn(road_label, run_time=0.7)
        )

        # 4) Bollard
        BOLLARD_X = ROAD_X_LIMIT + 0.1
        BOLLARD_H = 0.9 * 2 # Manim units, 1 unit = ~2.54cm, this is roughly 1.8 units high
        BOLLARD_D = 0.275 * 2 # Manim units, 0.55 units wide
        
        bollard_body = Rectangle(
            width=BOLLARD_D, 
            height=BOLLARD_H, 
            color=WHITE, 
            fill_opacity=1.0, 
            fill_color=WHITE
        ).set_stroke(color=CYAN, width=3) # Slight cyan outline
        
        bollard_cap = Circle(
            radius=BOLLARD_D/2, 
            color=WHITE, 
            fill_opacity=1.0, 
            fill_color=WHITE
        ).set_stroke(color=CYAN, width=3)
        
        bollard_body.align_to(ground_line, DOWN)
        bollard_cap.next_to(bollard_body, UP, buff=0.0)
        
        bollard = VGroup(bollard_body, bollard_cap)
        bollard.move_to(np.array([BOLLARD_X, GROUND_Y + BOLLARD_H/2, 0]))

        self.play(FadeIn(bollard, shift=UP*0.5, run_time=0.7))

        # 5) Vehicle (Van)
        VAN_WIDTH = 2.5
        VAN_HEIGHT = 1.0
        VAN_START_X = -6.0
        
        van_body = Rectangle(width=VAN_WIDTH, height=VAN_HEIGHT, color=WHITE, fill_color=GREY_C, fill_opacity=1.0)
        wheel1 = Circle(radius=0.2, color=BLACK, fill_color=BLACK, fill_opacity=1.0).next_to(van_body, DOWN, buff=0).shift(LEFT * (VAN_WIDTH/2 - 0.4))
        wheel2 = Circle(radius=0.2, color=BLACK, fill_color=BLACK, fill_opacity=1.0).next_to(van_body, DOWN, buff=0).shift(RIGHT * (VAN_WIDTH/2 - 0.4))
        van = VGroup(van_body, wheel1, wheel2)
        van.align_to(road_region, DOWN)
        van.move_to(np.array([VAN_START_X, van.get_center()[1], 0]))
        
        VAN_STOP_X = BOLLARD_X - 2.0
        
        self.play(
            FadeIn(van, shift=RIGHT*1.0), 
            run_time=0.5
        )
        self.play(
            van.animate.shift(RIGHT * (VAN_STOP_X - VAN_START_X)), 
            run_time=2.0, 
            rate_func=linear
        )
        self.wait(0.5)

        # ------------------------------------------------------------
        # PHASE 2 – K4 load parameters
        # ------------------------------------------------------------
        
        # Highlight impact point on bollard
        impact_point_y = GROUND_Y + 0.56 * 2
        impact_dot = Dot(point=np.array([BOLLARD_X + BOLLARD_D/2, impact_point_y, 0]), color=CYAN)
        self.add(impact_dot)

        # Impact Arrow (from vehicle bumper to bollard)
        impact_arrow = Arrow(
            start=van.get_right(), 
            end=impact_dot.get_left(), 
            color=CYAN, 
            stroke_width=6, 
            tip_length=0.3
        ).shift(DOWN*0.1)
        
        self.play(GrowArrow(impact_arrow), run_time=0.7)

        # K4 Parameters Panel Text
        K4_TEXT_SIZE = 24
        k4_lines = [
            "Vehicle mass m = 2000 kg",
            "Speed v = 57 km/h",
            "Impact energy ≈ 250 kJ",
            "Equivalent force ≈ 6267 kN"
        ]
        
        # FIX: Removed the invalid 'should_normalize=False' argument
        k4_mobjects = [Text(line, font_size=K4_TEXT_SIZE, color=WHITE) for line in k4_lines]
        
        k4_group_text = VGroup(*k4_mobjects).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        k4_group_text.next_to(title, DOWN, buff=0.3).to_edge(RIGHT, buff=0.5)
        
        # Panel Background
        k4_panel = RoundedRectangle(
            width=k4_group_text.width + 0.5, 
            height=k4_group_text.height + 0.5, 
            corner_radius=0.1, 
            fill_color=BLACK, 
            fill_opacity=0.6,
            stroke_color=CYAN,
            stroke_width=2
        )
        k4_panel.move_to(k4_group_text.get_center())
        
        k4_group = VGroup(k4_panel, k4_group_text)
        
        self.play(FadeIn(k4_panel), run_time=0.5)
        
        # Animate text lines individually
        for i, line_mob in enumerate(k4_mobjects):
            self.play(FadeIn(line_mob, shift=UP*0.1), run_time=0.4)
            if i < 3:
                self.wait(0.2)
        
        self.wait(1.5)

        # ------------------------------------------------------------
        # PHASE 3 – Geometry and free variable thickness
        # ------------------------------------------------------------

        # Prepare for geometry focus (slightly fade K4 panel)
        self.play(
            k4_panel.animate.set_opacity(0.4),
            FadeOut(impact_arrow),
            FadeOut(impact_dot),
            run_time=0.5
        )

        # 1) Bollard height h (0.9 m)
        height_brace = Brace(bollard_body, direction=RIGHT, sharpness=0.5)
        height_label = height_brace.get_text(r"h = 0.9 \text{ m}", font_size=28, color=WHITE)
        height_group = VGroup(height_brace, height_label)

        self.play(FadeIn(height_group, shift=RIGHT*0.2))

        # 2) Bollard diameter D (0.275 m)
        diameter_brace = Brace(bollard_body, direction=DOWN, sharpness=0.5)
        diameter_label = diameter_brace.get_text(r"D = 0.275 \text{ m}", font_size=28, color=WHITE)
        diameter_group = VGroup(diameter_brace, diameter_label)

        self.play(FadeIn(diameter_group, shift=DOWN*0.2))

        # 3) Impact height (0.56 m)
        impact_y_pos = ground_line.get_center()[1] + 0.56 * 2
        
        # Vertical dimension arrow (from ground to impact height)
        impact_marker = DashedLine(
            start=np.array([BOLLARD_X + BOLLARD_D/2, impact_y_pos, 0]), 
            end=np.array([BOLLARD_X + BOLLARD_D/2 + 1.0, impact_y_pos, 0]),
            color=CYAN
        )
        impact_brace = Brace(
            Line(np.array([BOLLARD_X - 1.0, GROUND_Y, 0]), np.array([BOLLARD_X - 1.0, impact_y_pos, 0])), 
            direction=LEFT
        )
        impact_label = impact_brace.get_text(r"\approx 0.56 \text{ m (bumper)}", font_size=24, color=CYAN)
        impact_group = VGroup(impact_marker, impact_brace, impact_label)

        self.play(FadeIn(impact_group, shift=LEFT*0.2))

        # 4) Thickness t as free variable
        # Cross-section visualization
        SECTION_X = BOLLARD_X - 3.0
        
        outer_circle = Circle(radius=0.4, color=CYAN, stroke_width=4).move_to(np.array([SECTION_X, 0, 0]))
        inner_circle = Circle(radius=0.3, color=WHITE, stroke_width=2).move_to(outer_circle.get_center())
        
        # Thickness annotation
        thick_line_start = outer_circle.point_at_angle(90*DEGREES + 10*DEGREES)
        thick_line_end = inner_circle.point_at_angle(90*DEGREES + 10*DEGREES)
        thick_arrow = DoubleArrow(thick_line_start, thick_line_end, buff=0, tip_length=0.1)
        thick_label = Text("t", font_size=32, color=CYAN).next_to(thick_arrow, RIGHT, buff=0.1)
        
        thickness_group_vis = VGroup(outer_circle, inner_circle, thick_arrow, thick_label)

        thickness_text = Text("Thickness t varies with material", font_size=28, color=WHITE)
        thickness_text.next_to(thickness_group_vis, DOWN, buff=0.5)
        
        thickness_group = VGroup(thickness_group_vis, thickness_text)

        self.play(
            FadeIn(thickness_group_vis), 
            run_time=0.7
        )
        self.play(
            FadeIn(thickness_text, shift=DOWN*0.1),
            run_time=0.7
        )

        # 5) Fixed base and concrete assumption
        # Indicate fixed base visually
        BASE_Y = GROUND_Y + 0.05
        base_fix = Line(
            np.array([BOLLARD_X - BOLLARD_D/2, BASE_Y, 0]), 
            np.array([BOLLARD_X + BOLLARD_D/2, BASE_Y, 0]), 
            stroke_width=8, 
            color=WHITE
        )
        
        # Concrete shading (ignore analysis label)
        concrete_shade = Rectangle(
            width=BOLLARD_D * 1.5, 
            height=1.0, 
            fill_color=GREY_A, 
            fill_opacity=0.3, 
            stroke_width=0
        )
        concrete_shade.next_to(base_fix, DOWN, buff=0)
        
        base_fix_text1 = Text("Assume fixed base", font_size=20, color=WHITE).next_to(base_fix, RIGHT, buff=0.5).shift(UP*0.2)
        base_fix_text2 = Text("Concrete region ignored in analysis", font_size=20, color=WHITE).next_to(base_fix_text1, DOWN, buff=0.1, aligned_edge=LEFT)
        
        base_group = VGroup(base_fix, concrete_shade, base_fix_text1, base_fix_text2)

        self.play(FadeIn(base_group, run_time=1.0))
        
        # Final hold
        self.wait(3.0)

        # ------------------------------------------------------------
        # PHASE 4 – Exit
        # ------------------------------------------------------------
        
        # 1. FadeOut K4 parameters panel and arrow (already done for arrow)
        self.play(
            FadeOut(k4_group, run_time=0.7)
        )
        
        # 2. FadeOut geometry annotations and labels
        self.play(
            FadeOut(height_group, run_time=0.7),
            FadeOut(diameter_group, run_time=0.7),
            FadeOut(impact_group, run_time=0.7),
            FadeOut(thickness_group, run_time=0.7),
            FadeOut(base_group, run_time=0.7),
        )

        # 3. FadeOut vehicle, building, and labels
        self.play(
            FadeOut(van, run_time=0.7),
            FadeOut(road_region, run_time=0.7),
            FadeOut(road_label, run_time=0.7),
            FadeOut(building, run_time=0.7),
            FadeOut(building_label, run_time=0.7),
        )

        # 4. FadeOut bollard and ground line
        self.play(
            FadeOut(bollard, run_time=0.7),
            FadeOut(ground_line, run_time=0.7),
        )

        # 5. FadeOut the title last
        self.play(
            FadeOut(title, run_time=1.0)
        )
        
        self.wait(0.3)