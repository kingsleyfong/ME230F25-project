# File: src/scenes/e_vs_yield_mpi_scene.py

from manim import *

Text.set_default(font="Segoe UI")

CYAN = "#00CED1"


class EVsYieldMPIScene(Scene):
    def construct(self):
        # ================================================================
        # TITLE
        # ================================================================
        
        title = Text(
            "Stiffness and strength material performance index",
            font_size=36,
            color=WHITE,
            weight=BOLD
        )
        title.to_edge(UP, buff=0.4)
        
        # ================================================================
        # LEFT COLUMN - GOALS
        # ================================================================
        
        # Goal 1: Maximize Stiffness
        # Script: "We want to maximize the ratio between stress and strain, or Youngs modulus..."
        goal1_text = Text("Maximize Stiffness (E)", font_size=28, color=WHITE)
        goal1_sub = MathTex(r"E = \sigma / \epsilon", font_size=28, color=WHITE)
        
        # Icon: Spring
        spring_path = VMobject()
        spring_path.set_points_as_corners([
            UP * 0.15, 
            UP * 0.1 + RIGHT * 0.1, 
            UP * 0.05 + LEFT * 0.1, 
            ORIGIN + RIGHT * 0.1, 
            DOWN * 0.05 + LEFT * 0.1, 
            DOWN * 0.1 + RIGHT * 0.1, 
            DOWN * 0.15
        ])
        spring_path.set_color(WHITE).set_stroke(width=2)
        spring_icon = VGroup(Rectangle(width=0.3, height=0.4, stroke_opacity=0), spring_path)
        
        goal1_group = VGroup(spring_icon, VGroup(goal1_text, goal1_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.1))
        goal1_group.arrange(RIGHT, buff=0.3)
        
        # Goal 2: Maximize Strength
        # Script: "...and also maximize the yield strength of the material."
        goal2_text = Text("Maximize Strength (σy)", font_size=28, color=WHITE)
        
        # Icon: Gauge
        gauge_arc = Arc(radius=0.15, start_angle=0, angle=PI, color=WHITE, stroke_width=2)
        gauge_needle = Line(ORIGIN, UP * 0.12 + RIGHT * 0.08, color=CYAN, stroke_width=2).shift(DOWN * 0.02)
        gauge_base = Line(LEFT * 0.15, RIGHT * 0.15, color=WHITE, stroke_width=2)
        gauge_icon = VGroup(gauge_arc, gauge_needle, gauge_base)
        
        goal2_group = VGroup(gauge_icon, goal2_text).arrange(RIGHT, buff=0.3)
        
        # Benefits
        # Script: "This will limit deflection, and increase the amount of force that can be applied before plastic deformation."
        benefit1 = Text("• Limit deflection", font_size=24, color=WHITE)
        benefit2 = Text("• Increase force before plastic deformation", font_size=24, color=WHITE)
        
        goals_layout = VGroup(goal1_group, goal2_group, benefit1, benefit2)
        goals_layout.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        goals_layout.to_edge(LEFT, buff=1.0).shift(UP * 0.5)
        
        # ================================================================
        # RIGHT COLUMN - DERIVATION
        # ================================================================
        
        # Script: "By rearranging the equations for elastic strain and bending..."
        deriv_header = Text("Derivation:", font_size=24, color=CYAN)
        
        # Elastic strain eq
        eq1 = MathTex(
            r"\text{Elastic Strain: } \epsilon = \frac{\sigma}{E}",
            font_size=32,
            color=WHITE
        )
        
        # Bending eq (symbolic)
        eq2 = MathTex(
            r"\text{Bending: } \sigma = \frac{M \cdot y}{I}",
            font_size=32,
            color=WHITE
        )
        
        # Arrow pointing down
        arrow = Arrow(UP, DOWN, color=WHITE).scale(0.5)
        
        deriv_layout = VGroup(deriv_header, eq1, eq2, arrow)
        deriv_layout.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        deriv_layout.next_to(goals_layout, RIGHT, buff=1.5).align_to(goals_layout, UP)
        
        # ================================================================
        # MPI BOX (BOTTOM CENTER)
        # ================================================================
        
        # Script: "...we get that the MPI = Yield strength squared over Youngs Modulus."
        mpi = MathTex(
            r"\text{MPI} = \frac{\sigma_y^2}{E}",
            font_size=48,
            color=CYAN
        )
        
        mpi_box = RoundedRectangle(
            corner_radius=0.15,
            width=mpi.width + 0.8,
            height=mpi.height + 0.5,
            stroke_color=CYAN,
            stroke_width=3,
            fill_opacity=0.05,
            fill_color=CYAN
        )
        mpi_box.move_to(mpi)
        
        mpi_group = VGroup(mpi_box, mpi)
        mpi_group.to_edge(DOWN, buff=1.0)
        
        # ================================================================
        # ANIMATION SEQUENCE
        # ================================================================
        
        # 1. Title
        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)
        
        # 2. Goals (Left side)
        self.play(FadeIn(goal1_group, run_time=0.8))
        self.wait(0.5)
        self.play(FadeIn(goal2_group, run_time=0.8))
        self.wait(0.5)
        
        # 3. Benefits
        self.play(FadeIn(benefit1, run_time=0.6))
        self.play(FadeIn(benefit2, run_time=0.6))
        self.wait(1.5)
        
        # 4. Derivation (Right side)
        self.play(FadeIn(deriv_header, run_time=0.5))
        self.play(FadeIn(eq1, run_time=0.8))
        self.play(FadeIn(eq2, run_time=0.8))
        self.wait(1.0)
        
        self.play(GrowArrow(arrow))
        self.wait(0.5)
        
        # 5. MPI
        self.play(FadeIn(mpi_group, run_time=1.0))
        self.wait(3.0)
        
        # ================================================================
        # EXIT
        # ================================================================
        
        self.play(
            FadeOut(mpi_group),
            FadeOut(deriv_layout),
            FadeOut(goals_layout),
            FadeOut(title),
            run_time=1.0
        )
        self.wait(0.3)
