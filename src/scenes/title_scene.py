from manim import *

Text.set_default(font="Segoe UI")

class TitleScene(Scene):
    def construct(self):
        # Global settings
        self.camera.background_color = "#050505"  # Nearly black

        # --- TEXT CONTENT ---
        
        # Main title (large)
        # "Stopping Vehicles. Saving Lives."
        # Centered slightly above vertical center of the screen.
        # Using font_size=72 for sharpness (approx scale 1.5 from default 48)
        main_title = Text("Stopping Vehicles. Saving Lives.", font_size=72, color=WHITE)
        main_title.set_stroke(color=BLACK, width=1.5)
        main_title.move_to(UP * 0.5)

        # Subtitle line 1
        # "ME230 Bollard Materials Selection Project"
        # Directly below the main title.
        # Scale 0.7 -> font_size ~34
        sub_line_1 = Text("ME230 Bollard Materials Selection Project", font_size=36, color=WHITE)
        sub_line_1.set_stroke(color=BLACK, width=1.2)
        sub_line_1.next_to(main_title, DOWN, buff=0.5)

        # Subtitle line 2
        # "University of Waterloo   Fall 2025"
        # Below subtitle line 1.
        # Scale 0.6 -> font_size ~30
        sub_line_2 = Text("University of Waterloo   Fall 2025", font_size=30, color=WHITE)
        sub_line_2.set_stroke(color=BLACK, width=1.0)
        sub_line_2.next_to(sub_line_1, DOWN, buff=0.3)

        # Team line
        # "Team members: Adam Benaissa   Joseph Schuurman   Kingsley Fong"
        # Smaller, near the bottom center.
        # Scale 0.5 -> font_size ~24
        team_line = Text("Team members: Adam Benaissa   Joseph Schuurman   Kingsley Fong", font_size=24, color=WHITE)
        team_line.set_stroke(color=BLACK, width=0.8)
        team_line.to_edge(DOWN, buff=1.0)

        # Group text for alignment and fading
        text_group = VGroup(main_title, sub_line_1, sub_line_2, team_line)

        # --- VISUAL ELEMENTS ---

        # 1. Background grid
        # Subtle cyan grid lines, low opacity.
        grid = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": "#49A88F",  # Dark cyan (Teal E)
                "stroke_width": 1,
                "stroke_opacity": 0.2
            },
            axis_config={"stroke_opacity": 0}  # Hide axes
        )

        # 2. Wireframe bollard
        # Centered behind the title text.
        # White outlines with cyan highlights on edges.
        bollard_group = VGroup()

        # Cylinder body (rectangle)
        cylinder_body = Rectangle(width=1.5, height=4.0, color=WHITE)
        cylinder_body.set_stroke(width=2)
        cylinder_body.set_fill(opacity=0)

        # Top ellipse (3D effect)
        top_ellipse = Ellipse(width=1.5, height=0.4, color=WHITE)
        top_ellipse.set_stroke(width=2)
        top_ellipse.move_to(cylinder_body.get_top())

        # Bottom ellipse (base)
        bottom_ellipse = Ellipse(width=1.5, height=0.4, color=WHITE)
        bottom_ellipse.set_stroke(width=2)
        bottom_ellipse.move_to(cylinder_body.get_bottom())
        # Make bottom ellipse dashed to suggest it's on the ground or hidden? 
        # Prompt says "Add a base plate or ground anchor line"
        # Let's add a slightly larger ellipse for base plate
        base_plate = Ellipse(width=2.0, height=0.6, color="#49A88F")
        base_plate.set_stroke(width=1, opacity=0.5)
        base_plate.move_to(cylinder_body.get_bottom())

        # Cyan highlights on vertical edges
        left_highlight = Line(cylinder_body.get_corner(UL), cylinder_body.get_corner(DL), color="#00FFFF", stroke_opacity=0.6)
        right_highlight = Line(cylinder_body.get_corner(UR), cylinder_body.get_corner(DR), color="#00FFFF", stroke_opacity=0.6)

        bollard_group.add(base_plate, cylinder_body, top_ellipse, bottom_ellipse, left_highlight, right_highlight)
        bollard_group.set_opacity(0.3)  # Low opacity
        bollard_group.move_to(ORIGIN)

        # 3. Optional street hints
        # Horizontal ground line
        ground_line = Line(LEFT * 8, RIGHT * 8, color=GREY)
        ground_line.set_stroke(width=1, opacity=0.2)
        ground_line.to_edge(DOWN, buff=2.0)

        # Faint vertical lines
        v_line_left = Line(DOWN*2, UP*2, color=GREY, stroke_opacity=0.1).move_to(LEFT * 4)
        v_line_right = Line(DOWN*2, UP*2, color=GREY, stroke_opacity=0.1).move_to(RIGHT * 4)
        
        street_hints = VGroup(ground_line, v_line_left, v_line_right)

        all_visuals = VGroup(grid, street_hints, bollard_group)

        # --- ANIMATION PLAN ---

        # PHASE 1 – Background and grid
        # Fade in from black over about 1.0 second.
        self.wait(0.1)
        self.play(
            FadeIn(grid, run_time=1.0),
            FadeIn(street_hints, run_time=1.0)
        )

        # PHASE 2 – Wireframe bollard
        # Create animations
        self.play(Create(bollard_group, run_time=2.0))

        # Soft pulsating glow ring
        glow_ring = Circle(radius=0.8, color="#00FFFF")
        glow_ring.set_stroke(width=4, opacity=0.5)
        glow_ring.move_to(bollard_group.get_center())
        
        self.play(
            glow_ring.animate.scale(1.5).set_stroke(opacity=0),
            run_time=1.0
        )

        # PHASE 3 – Title text
        # 1. Main title: FadeIn and slight scale up from 0.9 to 1.0
        main_title.scale(0.9)
        self.play(
            FadeIn(main_title),
            main_title.animate.scale(1.0/0.9),
            run_time=1.0
        )

        # 2. Subtitle line 1: FadeIn from below
        self.play(FadeIn(sub_line_1, shift=UP*0.5), run_time=0.8)

        # 3. Subtitle line 2: FadeIn from below, slightly delayed
        self.play(FadeIn(sub_line_2, shift=UP*0.5), run_time=0.8)

        # 4. Team line: FadeIn from the bottom center
        self.play(FadeIn(team_line, shift=UP*0.3), run_time=1.0)

        # PHASE 4 – Hold
        # Hold for 3 to 4 seconds
        # Breathing effect
        self.play(
            grid.animate.set_opacity(0.3),
            bollard_group.animate.set_opacity(0.4),
            run_time=2.0
        )
        self.play(
            grid.animate.set_opacity(0.2),
            bollard_group.animate.set_opacity(0.3),
            run_time=2.0
        )

        # PHASE 5 – Exit
        # Fade out everything
        self.play(
            FadeOut(text_group),
            FadeOut(all_visuals),
            run_time=1.5
        )

        self.wait(0.3)
