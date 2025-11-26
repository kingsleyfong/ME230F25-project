# File: src/scenes/requirements_scene.py

from manim import *

Text.set_default(font="Segoe UI")

# Define cyan highlight color
CYAN = "#00CED1"

class RequirementsScene(Scene):
    def construct(self):
        # ------------------------------------------------------------
        # TITLE
        # ------------------------------------------------------------
        
        title = Text("Bollard requirements", color=WHITE, weight=BOLD)
        title.scale(0.85)
        title.to_edge(UP, buff=0.5)
        
        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)
        
        # ------------------------------------------------------------
        # TWO COLUMN LAYOUT - FUNCTIONAL REQUIREMENTS (LEFT)
        # ------------------------------------------------------------
        
        # Functional requirements header
        func_header = Text("Functional requirements", color=WHITE, weight=BOLD)
        func_header.scale(0.55)
        
        # Bullet 1: Stop vehicle penetration
        bullet1_bollard = Rectangle(width=0.15, height=0.6, color=WHITE, stroke_width=2, fill_opacity=0.2)
        bullet1_car_body = Rectangle(width=0.5, height=0.25, color=WHITE, stroke_width=1.5, fill_opacity=0.15)
        bullet1_wheel1 = Circle(radius=0.08, color=WHITE, stroke_width=1.5, fill_opacity=0.2)
        bullet1_wheel2 = Circle(radius=0.08, color=WHITE, stroke_width=1.5, fill_opacity=0.2)
        bullet1_wheel1.next_to(bullet1_car_body, DOWN, buff=0)
        bullet1_wheel1.shift(LEFT * 0.12)
        bullet1_wheel2.next_to(bullet1_car_body, DOWN, buff=0)
        bullet1_wheel2.shift(RIGHT * 0.12)
        bullet1_car = VGroup(bullet1_car_body, bullet1_wheel1, bullet1_wheel2)
        bullet1_car.next_to(bullet1_bollard, LEFT, buff=0.3)
        bullet1_arrow = Arrow(bullet1_car.get_right(), bullet1_bollard.get_left(), color=CYAN, stroke_width=3, buff=0.05, max_tip_length_to_length_ratio=0.2)
        bullet1_icon = VGroup(bullet1_bollard, bullet1_car, bullet1_arrow)
        bullet1_icon.scale(0.7)
        bullet1_text = Text("Stop vehicle penetration", color=WHITE)
        bullet1_text.scale(0.4)
        bullet1_text.next_to(bullet1_icon, RIGHT, buff=0.25)
        bullet1 = VGroup(bullet1_icon, bullet1_text)
        
        # Bullet 2: Allow pedestrian flow
        bullet2_person_head = Circle(radius=0.08, color=WHITE, stroke_width=2, fill_opacity=0.15)
        bullet2_person_body = Line(ORIGIN, DOWN * 0.3, color=WHITE, stroke_width=2)
        bullet2_person_leg1 = Line(ORIGIN, DOWN * 0.2 + LEFT * 0.1, color=WHITE, stroke_width=2)
        bullet2_person_leg2 = Line(ORIGIN, DOWN * 0.2 + RIGHT * 0.1, color=WHITE, stroke_width=2)
        bullet2_person_arm1 = Line(ORIGIN, DOWN * 0.15 + LEFT * 0.12, color=WHITE, stroke_width=2)
        bullet2_person_arm2 = Line(ORIGIN, DOWN * 0.15 + RIGHT * 0.12, color=WHITE, stroke_width=2)
        bullet2_person_body.next_to(bullet2_person_head, DOWN, buff=0)
        bullet2_person_leg1.next_to(bullet2_person_body, DOWN, buff=0)
        bullet2_person_leg2.next_to(bullet2_person_body, DOWN, buff=0)
        bullet2_person_arm1.next_to(bullet2_person_body, UP, buff=0.05)
        bullet2_person_arm2.next_to(bullet2_person_body, UP, buff=0.05)
        bullet2_person = VGroup(bullet2_person_head, bullet2_person_body, bullet2_person_leg1, bullet2_person_leg2, bullet2_person_arm1, bullet2_person_arm2)
        bullet2_bollard = Rectangle(width=0.12, height=0.5, color=WHITE, stroke_width=2, fill_opacity=0.2)
        bullet2_bollard.next_to(bullet2_person, RIGHT, buff=0.2)
        bullet2_icon = VGroup(bullet2_person, bullet2_bollard)
        bullet2_icon.scale(0.7)
        bullet2_text = Text("Allow pedestrian flow", color=WHITE)
        bullet2_text.scale(0.4)
        bullet2_text.next_to(bullet2_icon, RIGHT, buff=0.25)
        bullet2 = VGroup(bullet2_icon, bullet2_text)
        
        # Bullet 3: High visibility
        bullet3_bollard = Rectangle(width=0.15, height=0.6, color=WHITE, stroke_width=2, fill_opacity=0.2)
        bullet3_band = Rectangle(width=0.15, height=0.12, color=CYAN, stroke_width=2, fill_opacity=0.4)
        bullet3_band.move_to(bullet3_bollard.get_top() + DOWN * 0.08)
        bullet3_icon = VGroup(bullet3_bollard, bullet3_band)
        bullet3_icon.scale(0.7)
        bullet3_text = Text("High visibility", color=WHITE)
        bullet3_text.scale(0.4)
        bullet3_text.next_to(bullet3_icon, RIGHT, buff=0.25)
        bullet3 = VGroup(bullet3_icon, bullet3_text)
        
        # Bullet 4: Corrosion resistant
        bullet4_shield = Polygon(
            UP * 0.35, UP * 0.2 + LEFT * 0.2, DOWN * 0.35 + LEFT * 0.2,
            DOWN * 0.35, DOWN * 0.35 + RIGHT * 0.2, UP * 0.2 + RIGHT * 0.2,
            color=WHITE, stroke_width=2, fill_opacity=0.15
        )
        bullet4_droplet = Circle(radius=0.08, color=WHITE, stroke_width=2, fill_opacity=0.2)
        bullet4_droplet.move_to(bullet4_shield.get_center() + UP * 0.05)
        bullet4_slash = Line(UP * 0.15 + LEFT * 0.1, DOWN * 0.15 + RIGHT * 0.1, color=CYAN, stroke_width=2.5)
        bullet4_slash.move_to(bullet4_shield.get_center())
        bullet4_icon = VGroup(bullet4_shield, bullet4_droplet, bullet4_slash)
        bullet4_icon.scale(0.7)
        bullet4_text = Text("Corrosion resistant", color=WHITE)
        bullet4_text.scale(0.4)
        bullet4_text.next_to(bullet4_icon, RIGHT, buff=0.25)
        bullet4 = VGroup(bullet4_icon, bullet4_text)
        
        # Arrange functional bullets
        func_bullets = VGroup(bullet1, bullet2, bullet3, bullet4)
        func_bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        func_bullets.next_to(func_header, DOWN, buff=0.35)
        
        # Functional column group
        func_column = VGroup(func_header, func_bullets)
        func_column.move_to(LEFT * 3.2 + DOWN * 0.3)
        
        # Functional column panel
        func_panel = RoundedRectangle(
            width=func_column.width + 0.5,
            height=func_column.height + 0.5,
            corner_radius=0.15,
            color=CYAN,
            stroke_width=2,
            stroke_opacity=0.6,
            fill_opacity=0.05
        )
        func_panel.move_to(func_column.get_center())
        
        # ------------------------------------------------------------
        # TWO COLUMN LAYOUT - NON FUNCTIONAL REQUIREMENTS (RIGHT)
        # ------------------------------------------------------------
        
        # Non functional requirements header
        nonfunc_header = Text("Non functional requirements", color=WHITE, weight=BOLD)
        nonfunc_header.scale(0.55)
        
        # Bullet 1: Small footprint
        nonfunc_bullet1_box = Rectangle(width=0.5, height=0.5, color=WHITE, stroke_width=1.5, fill_opacity=0.1)
        nonfunc_bullet1_cylinder = Ellipse(width=0.2, height=0.08, color=WHITE, stroke_width=2, fill_opacity=0.2)
        nonfunc_bullet1_cylinder_body = Rectangle(width=0.2, height=0.3, color=WHITE, stroke_width=2, fill_opacity=0.2)
        nonfunc_bullet1_cylinder_body.next_to(nonfunc_bullet1_cylinder, DOWN, buff=0)
        nonfunc_bullet1_cyl = VGroup(nonfunc_bullet1_cylinder, nonfunc_bullet1_cylinder_body)
        nonfunc_bullet1_cyl.move_to(nonfunc_bullet1_box.get_center())
        nonfunc_bullet1_icon = VGroup(nonfunc_bullet1_box, nonfunc_bullet1_cyl)
        nonfunc_bullet1_icon.scale(0.7)
        nonfunc_bullet1_text = Text("Small footprint", color=WHITE)
        nonfunc_bullet1_text.scale(0.4)
        nonfunc_bullet1_text.next_to(nonfunc_bullet1_icon, RIGHT, buff=0.25)
        nonfunc_bullet1 = VGroup(nonfunc_bullet1_icon, nonfunc_bullet1_text)
        
        # Bullet 2: Safe
        nonfunc_bullet2_shield = Polygon(
            UP * 0.35, UP * 0.2 + LEFT * 0.2, DOWN * 0.35 + LEFT * 0.2,
            DOWN * 0.35, DOWN * 0.35 + RIGHT * 0.2, UP * 0.2 + RIGHT * 0.2,
            color=WHITE, stroke_width=2, fill_opacity=0.15
        )
        nonfunc_bullet2_check1 = Line(ORIGIN, DOWN * 0.15 + RIGHT * 0.08, color=CYAN, stroke_width=2.5)
        nonfunc_bullet2_check2 = Line(ORIGIN, UP * 0.25 + RIGHT * 0.15, color=CYAN, stroke_width=2.5)
        nonfunc_bullet2_check1.move_to(nonfunc_bullet2_shield.get_center() + LEFT * 0.05 + DOWN * 0.05)
        nonfunc_bullet2_check2.next_to(nonfunc_bullet2_check1, RIGHT, buff=0)
        nonfunc_bullet2_check2.shift(LEFT * 0.08)
        nonfunc_bullet2_icon = VGroup(nonfunc_bullet2_shield, nonfunc_bullet2_check1, nonfunc_bullet2_check2)
        nonfunc_bullet2_icon.scale(0.7)
        nonfunc_bullet2_text = Text("Safe", color=WHITE)
        nonfunc_bullet2_text.scale(0.4)
        nonfunc_bullet2_text.next_to(nonfunc_bullet2_icon, RIGHT, buff=0.25)
        nonfunc_bullet2 = VGroup(nonfunc_bullet2_icon, nonfunc_bullet2_text)
        
        # Bullet 3: Aesthetic
        nonfunc_bullet3_frame = Rectangle(width=0.5, height=0.5, color=WHITE, stroke_width=2, fill_opacity=0.1)
        nonfunc_bullet3_inner1 = Rectangle(width=0.25, height=0.25, color=CYAN, stroke_width=1.5, fill_opacity=0.15)
        nonfunc_bullet3_inner1.move_to(nonfunc_bullet3_frame.get_center() + UP * 0.1 + LEFT * 0.1)
        nonfunc_bullet3_inner2 = Circle(radius=0.08, color=CYAN, stroke_width=1.5, fill_opacity=0.2)
        nonfunc_bullet3_inner2.move_to(nonfunc_bullet3_frame.get_center() + DOWN * 0.08 + RIGHT * 0.1)
        nonfunc_bullet3_icon = VGroup(nonfunc_bullet3_frame, nonfunc_bullet3_inner1, nonfunc_bullet3_inner2)
        nonfunc_bullet3_icon.scale(0.7)
        nonfunc_bullet3_text = Text("Aesthetic", color=WHITE)
        nonfunc_bullet3_text.scale(0.4)
        nonfunc_bullet3_text.next_to(nonfunc_bullet3_icon, RIGHT, buff=0.25)
        nonfunc_bullet3 = VGroup(nonfunc_bullet3_icon, nonfunc_bullet3_text)
        
        # Bullet 4: Low cost
        nonfunc_bullet4_coin = Circle(radius=0.25, color=WHITE, stroke_width=2, fill_opacity=0.2)
        nonfunc_bullet4_dollar = Text("$", color=CYAN, weight=BOLD)
        nonfunc_bullet4_dollar.scale(0.5)
        nonfunc_bullet4_dollar.move_to(nonfunc_bullet4_coin.get_center())
        nonfunc_bullet4_icon = VGroup(nonfunc_bullet4_coin, nonfunc_bullet4_dollar)
        nonfunc_bullet4_icon.scale(0.7)
        nonfunc_bullet4_text = Text("Low cost", color=WHITE)
        nonfunc_bullet4_text.scale(0.4)
        nonfunc_bullet4_text.next_to(nonfunc_bullet4_icon, RIGHT, buff=0.25)
        nonfunc_bullet4 = VGroup(nonfunc_bullet4_icon, nonfunc_bullet4_text)
        
        # Bullet 5: Recyclable
        nonfunc_bullet5_arrow1 = Arrow(ORIGIN, UP * 0.25 + RIGHT * 0.15, color=CYAN, stroke_width=2.5, buff=0, max_tip_length_to_length_ratio=0.25)
        nonfunc_bullet5_arrow2 = Arrow(ORIGIN, DOWN * 0.25, color=CYAN, stroke_width=2.5, buff=0, max_tip_length_to_length_ratio=0.25)
        nonfunc_bullet5_arrow2.rotate(120 * DEGREES, about_point=ORIGIN)
        nonfunc_bullet5_arrow3 = Arrow(ORIGIN, DOWN * 0.25, color=CYAN, stroke_width=2.5, buff=0, max_tip_length_to_length_ratio=0.25)
        nonfunc_bullet5_arrow3.rotate(240 * DEGREES, about_point=ORIGIN)
        nonfunc_bullet5_icon = VGroup(nonfunc_bullet5_arrow1, nonfunc_bullet5_arrow2, nonfunc_bullet5_arrow3)
        nonfunc_bullet5_icon.scale(0.7)
        nonfunc_bullet5_text = Text("Recyclable", color=WHITE)
        nonfunc_bullet5_text.scale(0.4)
        nonfunc_bullet5_text.next_to(nonfunc_bullet5_icon, RIGHT, buff=0.25)
        nonfunc_bullet5 = VGroup(nonfunc_bullet5_icon, nonfunc_bullet5_text)
        
        # Bullet 6: Low environmental impact
        nonfunc_bullet6_leaf_body = Ellipse(width=0.15, height=0.35, color=WHITE, stroke_width=2, fill_opacity=0.2)
        nonfunc_bullet6_leaf_vein = Line(nonfunc_bullet6_leaf_body.get_bottom(), nonfunc_bullet6_leaf_body.get_top(), color=CYAN, stroke_width=1.5)
        nonfunc_bullet6_icon = VGroup(nonfunc_bullet6_leaf_body, nonfunc_bullet6_leaf_vein)
        nonfunc_bullet6_icon.scale(0.7)
        nonfunc_bullet6_text = Text("Low environmental impact", color=WHITE)
        nonfunc_bullet6_text.scale(0.4)
        nonfunc_bullet6_text.next_to(nonfunc_bullet6_icon, RIGHT, buff=0.25)
        nonfunc_bullet6 = VGroup(nonfunc_bullet6_icon, nonfunc_bullet6_text)
        
        # Arrange non functional bullets
        nonfunc_bullets = VGroup(nonfunc_bullet1, nonfunc_bullet2, nonfunc_bullet3, nonfunc_bullet4, nonfunc_bullet5, nonfunc_bullet6)
        nonfunc_bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        nonfunc_bullets.next_to(nonfunc_header, DOWN, buff=0.35)
        
        # Non functional column group
        nonfunc_column = VGroup(nonfunc_header, nonfunc_bullets)
        nonfunc_column.move_to(RIGHT * 3.0 + DOWN * 0.3)
        
        # Non functional column panel
        nonfunc_panel = RoundedRectangle(
            width=nonfunc_column.width + 0.5,
            height=nonfunc_column.height + 0.5,
            corner_radius=0.15,
            color=GRAY,
            stroke_width=2,
            stroke_opacity=0.4,
            fill_opacity=0.05
        )
        nonfunc_panel.move_to(nonfunc_column.get_center())
        
        # ------------------------------------------------------------
        # ANIMATION SEQUENCE - FUNCTIONAL REQUIREMENTS
        # ------------------------------------------------------------
        
        # Show functional panel with glow
        self.play(FadeIn(func_panel, run_time=0.7))
        self.wait(0.2)
        self.play(FadeIn(func_header, run_time=0.8))
        self.wait(0.4)
        
        # Show functional bullets one by one
        self.play(FadeIn(bullet1, run_time=0.7))
        self.wait(0.5)
        self.play(FadeIn(bullet2, run_time=0.7))
        self.wait(0.5)
        self.play(FadeIn(bullet3, run_time=0.7))
        self.wait(0.5)
        self.play(FadeIn(bullet4, run_time=0.7))
        self.wait(0.8)
        
        # Dim functional column and emphasize non functional
        self.play(
            func_panel.animate.set_stroke(opacity=0.3),
            func_panel.animate.set_fill(opacity=0.02),
            run_time=0.5
        )
        self.wait(0.2)
        
        # ------------------------------------------------------------
        # ANIMATION SEQUENCE - NON FUNCTIONAL REQUIREMENTS
        # ------------------------------------------------------------
        
        # Show non functional panel with glow
        self.play(FadeIn(nonfunc_panel, run_time=0.7))
        self.wait(0.2)
        self.play(FadeIn(nonfunc_header, run_time=0.8))
        self.wait(0.4)
        
        # Show non functional bullets one by one
        self.play(FadeIn(nonfunc_bullet1, run_time=0.7))
        self.wait(0.5)
        self.play(FadeIn(nonfunc_bullet2, run_time=0.7))
        self.wait(0.5)
        self.play(FadeIn(nonfunc_bullet3, run_time=0.7))
        self.wait(0.5)
        self.play(FadeIn(nonfunc_bullet4, run_time=0.7))
        self.wait(0.5)
        self.play(FadeIn(nonfunc_bullet5, run_time=0.7))
        self.wait(0.5)
        self.play(FadeIn(nonfunc_bullet6, run_time=0.7))
        self.wait(1.0)
        
        # ------------------------------------------------------------
        # EXIT
        # ------------------------------------------------------------
        
        # Fade out bullets
        self.play(
            FadeOut(func_bullets, run_time=1.0),
            FadeOut(nonfunc_bullets, run_time=1.0)
        )
        self.wait(0.2)
        
        # Fade out headers
        self.play(
            FadeOut(func_header, run_time=1.0),
            FadeOut(nonfunc_header, run_time=1.0)
        )
        self.wait(0.2)
        
        # Fade out panels
        self.play(
            FadeOut(func_panel, run_time=1.0),
            FadeOut(nonfunc_panel, run_time=1.0)
        )
        self.wait(0.2)
        
        # Fade out title last
        self.play(FadeOut(title, run_time=1.0))
        self.wait(0.3)
