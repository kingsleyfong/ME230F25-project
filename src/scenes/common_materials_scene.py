from manim import *

Text.set_default(font="Segoe UI")

class CommonMaterialsScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # PHASE 1 - Title and three icons
        title = Text("Common Bollard Materials", color=WHITE)
        title.set_stroke(color=BLACK, width=1.5)
        title.to_edge(UP, buff=1.0)

        self.play(FadeIn(title, run_time=0.7))
        self.wait(0.5)

        # Helper to create base bollard shape
        def create_bollard_icon(color, width, height, label_text, stroke_color=WHITE, fill_opacity=0.2):
            ground = Line(LEFT * 1.5, RIGHT * 1.5, color=WHITE, stroke_width=2)
            post = RoundedRectangle(
                corner_radius=0.1,
                width=width,
                height=height,
                color=stroke_color,
                fill_color=color,
                fill_opacity=fill_opacity,
                stroke_width=2
            )
            post.move_to(ground.get_center() + UP * (height / 2))
            foundation = Rectangle(
                width=width * 1.2,
                height=0.8,
                color=stroke_color,
                fill_color=color,
                fill_opacity=fill_opacity * 0.5,
                stroke_width=2
            )
            foundation.move_to(ground.get_center() + DOWN * 0.4)
            
            # Create label
            label = Text(label_text, font_size=24, color=WHITE)
            label.set_stroke(color=BLACK, width=1.5)
            label.next_to(post, UP, buff=0.5)
            
            return VGroup(foundation, post, ground, label), post, label

        # Concrete Icon
        concrete_group, concrete_post, concrete_label = create_bollard_icon(GRAY, 0.8, 2.0, "Concrete", stroke_color=GRAY_A, fill_opacity=0.3)
        
        # Steel Icon
        steel_group, steel_post, steel_label = create_bollard_icon(GRAY_C, 0.6, 2.0, "Steel", stroke_color=WHITE, fill_opacity=0.4)
        # Add subtle band
        steel_band = Line(steel_post.get_left(), steel_post.get_right(), color=WHITE, stroke_width=1).shift(UP * 0.5)
        steel_group.add(steel_band)

        # Polymer Icon
        polymer_group, polymer_post, polymer_label = create_bollard_icon(YELLOW, 0.7, 2.0, "Polymer", stroke_color=YELLOW, fill_opacity=0.3)
        # Round top more
        polymer_cap = Arc(radius=0.35, start_angle=0, angle=PI, color=YELLOW, stroke_width=2)
        polymer_cap.move_to(polymer_post.get_top() + DOWN * 0.1) # Adjust position slightly
        # For simplicity, just use the rounded rect, but maybe add a colored sleeve effect
        # Let's keep it simple as per instructions, the color distinguishes it.

        # Arrange icons
        icons = VGroup(concrete_group, steel_group, polymer_group)
        icons.arrange(RIGHT, buff=2.0)
        icons.move_to(ORIGIN)

        self.play(
            FadeIn(icons, shift=UP * 0.5, run_time=0.8)
        )
        self.wait(0.5)

        # Helper for bullets
        def create_bullets(text1, text2):
            b1 = Text(text1, font_size=24, color=WHITE)
            b1.set_stroke(color=BLACK, width=1.5)
            b2 = Text(text2, font_size=24, color=WHITE)
            b2.set_stroke(color=BLACK, width=1.5)
            g = VGroup(b1, b2).arrange(DOWN, buff=0.2)
            g.to_edge(DOWN, buff=1.0)
            return g

        # PHASE 2 - Focus on Concrete
        self.play(
            concrete_group.animate.scale(1.1),
            steel_group.animate.set_opacity(0.3),
            polymer_group.animate.set_opacity(0.3),
            run_time=0.5
        )

        bullets_concrete = create_bullets("Low cost, simple to install", "Handles small hits, cracks under heavy impact")
        self.play(FadeIn(bullets_concrete, run_time=0.5))
        self.wait(7.0) # Wait for narration

        # Impact Concrete
        arrow_concrete = Arrow(start=LEFT, end=RIGHT, color=YELLOW).next_to(concrete_post, LEFT, buff=1.0)
        self.play(arrow_concrete.animate.next_to(concrete_post, LEFT, buff=0.1), run_time=1.0)
        
        # Crack effect
        crack = VGroup(
            Line(concrete_post.get_center(), concrete_post.get_corner(UR), color=BLACK, stroke_width=2),
            Line(concrete_post.get_center(), concrete_post.get_corner(DL), color=BLACK, stroke_width=2),
            Line(concrete_post.get_center() + UP*0.2, concrete_post.get_right(), color=BLACK, stroke_width=2)
        )
        self.play(Create(crack, run_time=0.3))
        self.play(concrete_group.animate.rotate(0.05 * TAU).rotate(-0.05 * TAU), run_time=0.2) # Shake
        
        self.wait(6.0) # Hold result
        self.play(FadeOut(arrow_concrete), FadeOut(crack))
        self.play(FadeOut(bullets_concrete))

        # PHASE 3 - Focus on Steel
        self.play(
            concrete_group.animate.scale(1/1.1),
            steel_group.animate.scale(1.1).set_opacity(1),
            run_time=0.5
        )

        bullets_steel = create_bullets("High strength, ductile metal", "Good one time barrier, can deform permanently")
        self.play(FadeIn(bullets_steel, run_time=0.5))
        self.wait(7.0) # Wait for narration

        # Impact Steel
        arrow_steel = Arrow(start=LEFT, end=RIGHT, color=YELLOW).next_to(steel_post, LEFT, buff=1.0)
        self.play(arrow_steel.animate.next_to(steel_post, LEFT, buff=0.1), run_time=1.0)

        # Bend effect
        # Rotate post around its bottom center
        self.play(
            Rotate(steel_post, angle=-15*DEGREES, about_point=steel_post.get_bottom(), run_time=0.5),
            Rotate(steel_band, angle=-15*DEGREES, about_point=steel_post.get_bottom(), run_time=0.5)
        )
        
        self.wait(6.0) # Hold result
        self.play(FadeOut(arrow_steel))
        self.play(FadeOut(bullets_steel))

        # PHASE 4 - Focus on Polymer
        self.play(
            steel_group.animate.scale(1/1.1).set_opacity(0.3), # Dim steel
            concrete_group.animate.set_opacity(0.3), # Keep concrete dim
            polymer_group.animate.scale(1.1).set_opacity(1),
            run_time=0.5
        )

        bullets_polymer = create_bullets("Flexible shell over core", "Springs back after small collisions")
        self.play(FadeIn(bullets_polymer, run_time=0.5))
        self.wait(7.0) # Wait for narration

        # Impact Polymer
        arrow_polymer = Arrow(start=LEFT, end=RIGHT, color=YELLOW).next_to(polymer_post, LEFT, buff=1.0)
        self.play(arrow_polymer.animate.next_to(polymer_post, LEFT, buff=0.1), run_time=1.0)

        # Elastic bend effect
        self.play(Rotate(polymer_post, angle=-25*DEGREES, about_point=polymer_post.get_bottom(), run_time=0.4))
        self.play(Rotate(polymer_post, angle=25*DEGREES, about_point=polymer_post.get_bottom(), run_time=0.6)) # Spring back

        self.wait(6.0) # Hold result
        self.play(FadeOut(arrow_polymer))
        self.play(FadeOut(bullets_polymer))

        # PHASE 5 - Quick comparison wrap and fade out
        self.play(
            concrete_group.animate.set_opacity(1),
            steel_group.animate.set_opacity(1),
            polymer_group.animate.scale(1/1.1),
            run_time=0.5
        )

        summary_text = Text("Different materials trade off cost, durability, and collision behavior.", font_size=28, color=WHITE)
        summary_text.set_stroke(color=BLACK, width=1.5)
        summary_text.to_edge(DOWN, buff=1.0)

        self.play(FadeIn(summary_text, run_time=0.7))
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(icons),
            FadeOut(summary_text),
            run_time=1.0
        )
        self.wait(0.5)
