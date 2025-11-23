from manim import *

Text.set_default(font="Segoe UI")

class BollardIntroScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # PHASE 1 - Title fade in
        title = Text("What is a Bollard?", color=WHITE)
        title.set_stroke(color=BLACK, width=1.5)
        title.move_to(ORIGIN)

        self.play(FadeIn(title, run_time=0.7))
        self.wait(0.5)
        self.play(title.animate.shift(UP * 2.5), run_time=1.0)

        # PHASE 2 - Bollard blueprint schematic
        # Colors
        blueprint_color = "#55cfff"  # Light cyan

        # Ground line
        ground_line = Line(start=LEFT * 4, end=RIGHT * 4, color=blueprint_color)
        ground_line.set_stroke(width=2)
        ground_line.shift(DOWN * 0.5)

        # Bollard body (above ground)
        bollard_width = 0.8
        bollard_height = 2.5
        bollard_body = RoundedRectangle(
            corner_radius=0.1,
            width=bollard_width,
            height=bollard_height,
            color=blueprint_color,
            fill_opacity=0.1,
            fill_color=blueprint_color
        )
        bollard_body.set_stroke(width=2)
        # Position: bottom of body sits on ground line
        bollard_body.move_to(ground_line.get_center() + UP * (bollard_height / 2))

        # Foundation (below ground)
        foundation_depth = 1.5
        foundation_block = Rectangle(
            width=bollard_width * 1.2,
            height=foundation_depth,
            color=blueprint_color,
            fill_opacity=0.05,
            fill_color=blueprint_color
        )
        foundation_block.set_stroke(width=2)
        # Position: top of foundation sits on ground line
        foundation_block.move_to(ground_line.get_center() + DOWN * (foundation_depth / 2))

        # Group diagram elements
        diagram = VGroup(foundation_block, bollard_body, ground_line)
        
        # Animate diagram creation
        self.play(
            Create(ground_line, run_time=1.0),
            FadeIn(bollard_body, shift=UP * 0.5, run_time=1.0),
            FadeIn(foundation_block, shift=DOWN * 0.5, run_time=1.0)
        )
        self.wait(0.5)

        # PHASE 3 - Sequential definition text
        # Define text styles
        def create_def_text(content):
            t = Text(content, color=WHITE, font_size=36)
            t.set_stroke(color=BLACK, width=1.5)
            # Constrain width to fit screen comfortably
            if t.width > config.frame_width * 0.8:
                t.scale_to_fit_width(config.frame_width * 0.8)
            t.to_edge(DOWN, buff=1.0)
            return t

        # Updated Bullet Points
        bullet_1 = create_def_text("Barrier between vehicles and pedestrians")
        bullet_2 = create_def_text("Rigid post embedded below ground")
        bullet_3 = create_def_text("Absorbs and redirects vehicle impact")

        # Sequence 1
        self.play(FadeIn(bullet_1))
        self.wait(5.0)
        self.play(FadeOut(bullet_1))

        # Sequence 2
        self.play(FadeIn(bullet_2))
        self.wait(5.0)
        self.play(FadeOut(bullet_2))

        # Sequence 3 + Phase 4 (Force Visualization)
        self.play(FadeIn(bullet_3))
        
        # PHASE 4 - Simple force visualization
        # Arrow representing vehicle impact
        impact_arrow = Arrow(
            start=LEFT * 5, 
            end=bollard_body.get_left(), 
            color=YELLOW, 
            buff=0.1,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.3
        )
        impact_arrow.shift(UP * 0.5) # Hit slightly above ground

        # Animate arrow
        self.play(GrowArrow(impact_arrow, run_time=0.8))
        
        # Impact effect
        self.play(
            Wiggle(bollard_body, scale_value=1.0, rotation_angle=0.03 * TAU, run_time=0.4),
            Flash(bollard_body.get_left() + UP * 0.5, color=YELLOW, line_length=0.5, num_lines=8, run_time=0.4)
        )
        
        self.play(FadeOut(impact_arrow, run_time=0.5))
        
        # Wait for the rest of the reading time for Bullet 3
        self.wait(4.0)

        # PHASE 5 - Fade out to black
        self.play(
            FadeOut(bullet_3),
            FadeOut(diagram),
            FadeOut(title),
            run_time=1.0
        )
        self.wait(0.5)
