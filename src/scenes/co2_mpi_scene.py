# File: src/scenes/co2_mpi_scene.py

from manim import *
import numpy as np

Text.set_default(font="Segoe UI")

CYAN = "#00CED1"


class CO2MPIScene(Scene):
    def construct(self):
        # ================================================================
        # SLIDE 12: DERIVATION
        # ================================================================
        
        title = Text(
            "CO2 based material performance index",
            font_size=36,
            color=WHITE,
            weight=BOLD
        )
        title.to_edge(UP, buff=0.4)
        
        # 1. Base CO2 equation
        # Script: "We also want to minimize kg of CO2 output..."
        eq1 = MathTex(
            r"\text{CO2}_{\text{total}} = C_{CO2} \cdot m",
            font_size=40,
            color=WHITE
        )
        
        cloud_icon = VGroup(
            Ellipse(width=0.35, height=0.2, color=WHITE, stroke_width=2, fill_opacity=0.15),
            Circle(radius=0.08, color=WHITE, stroke_width=2, fill_opacity=0.15).shift(LEFT * 0.1 + UP * 0.05),
            Circle(radius=0.1, color=WHITE, stroke_width=2, fill_opacity=0.15).shift(UP * 0.08),
            Circle(radius=0.07, color=WHITE, stroke_width=2, fill_opacity=0.15).shift(RIGHT * 0.1 + UP * 0.03)
        ).move_to(ORIGIN)
        
        eq1_group = VGroup(cloud_icon, eq1).arrange(RIGHT, buff=0.3)
        
        # 2. Mass and Volume relation
        # Script: "...subbing that into the formula for kg of CO2 output..."
        # Implicitly m = rho * V and V ~ t
        eq2 = MathTex(
            r"m = \rho \cdot V \quad \text{and} \quad V \propto t",
            font_size=40,
            color=WHITE
        )
        
        weight_icon = VGroup(
            Rectangle(width=0.25, height=0.15, color=WHITE, stroke_width=2, fill_opacity=0.2),
            Arc(radius=0.125, start_angle=0, angle=PI, color=WHITE, stroke_width=2).shift(UP * 0.075)
        )
        
        eq2_group = VGroup(weight_icon, eq2).arrange(RIGHT, buff=0.3)
        
        # 3. Bending stress rearrangement
        # Script: "By rearranging the formula of bending stress for our free variable, thickness..."
        eq3 = MathTex(
            r"t \propto \frac{M}{\sigma}",
            font_size=40,
            color=WHITE
        )
        
        bend_icon = VGroup(
            Rectangle(width=0.3, height=0.08, color=WHITE, stroke_width=2, fill_opacity=0.15),
            Arrow(UP * 0.15, DOWN * 0.05, color=CYAN, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.25).shift(UP * 0.05)
        )
        
        eq3_group = VGroup(bend_icon, eq3).arrange(RIGHT, buff=0.3)
        
        # 4. Final Substitution
        # Script: "...we can see that the MPI is the material constant in kg/kg of CO2 is divided by the stress."
        # Note: Including rho to match the physics, even if script simplifies description
        eq4 = MathTex(
            r"\text{CO2}_{\text{total}} \propto \frac{C_{CO2} \cdot \rho}{\sigma}",
            font_size=40,
            color=WHITE
        )
        
        arrow_icon = Arrow(LEFT * 0.2, RIGHT * 0.2, color=CYAN, stroke_width=3, buff=0)
        
        eq4_group = VGroup(arrow_icon, eq4).arrange(RIGHT, buff=0.3)
        
        # Arrange equations
        equations = VGroup(eq1_group, eq2_group, eq3_group, eq4_group)
        equations.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        equations.move_to(ORIGIN)
        
        # MPI Box
        mpi_tex = MathTex(
            r"\text{Minimize } \frac{C_{CO2} \cdot \rho}{\sigma}",
            font_size=48,
            color=CYAN
        )
        
        mpi_box = RoundedRectangle(
            corner_radius=0.15,
            width=mpi_tex.width + 0.6,
            height=mpi_tex.height + 0.4,
            stroke_color=CYAN,
            stroke_width=3,
            fill_opacity=0.05,
            fill_color=CYAN
        )
        mpi_box.move_to(mpi_tex)
        mpi_group = VGroup(mpi_box, mpi_tex)
        mpi_group.next_to(equations, DOWN, buff=0.6)
        
        # ----------------------------------------------------------------
        # ANIMATION PHASE 1 (Derivation)
        # ----------------------------------------------------------------
        
        self.play(FadeIn(title, run_time=1.0))
        
        self.play(FadeIn(eq1_group, run_time=1.0))
        self.wait(1.0)
        
        self.play(FadeIn(eq3_group, run_time=1.0)) # t relation
        self.wait(1.0)
        
        self.play(FadeIn(eq2_group, run_time=1.0)) # m = rho V
        self.wait(1.0)
        
        self.play(FadeIn(eq4_group, run_time=1.0)) # Substitution
        self.wait(1.0)
        
        self.play(FadeIn(mpi_group, run_time=1.0))
        self.wait(2.0)
        
        # ================================================================
        # SLIDE 13: GRAPH
        # ================================================================
        
        # Transition: Move equations to left and fade out some to make room
        # Or better: Fade out derivation, Fade in Graph
        
        self.play(
            FadeOut(equations, run_time=0.8),
            FadeOut(mpi_group, run_time=0.8),
            title.animate.to_edge(UP, buff=0.2)
        )
        
        # Graph Setup
        # Script: "CO2 Primary Production (kg/kg) VS Tensile Strength"
        axes = Axes(
            x_range=[0, 1000, 200], # Tensile Strength in MPa
            y_range=[0, 10, 2],     # C_CO2 in kg/kg
            x_length=5,
            y_length=3.5,
            axis_config={"color": WHITE, "stroke_width": 2},
            tips=True
        )
        axes.move_to(ORIGIN).shift(LEFT * 1.5 + DOWN * 0.3)
        
        x_label = Text("Tensile Strength (MPa)", font_size=20, color=WHITE)
        x_label.next_to(axes.x_axis, DOWN, buff=0.3)
        
        y_label = Text("CO2 (kg/kg)", font_size=20, color=WHITE)
        y_label.next_to(axes.y_axis, LEFT, buff=0.4)
        y_label.rotate(90 * DEGREES)
        
        # Scatter points
        np.random.seed(42)
        points = VGroup()
        for _ in range(20):
            x = np.random.uniform(100, 900)
            y = np.random.uniform(0.5, 9.5)
            dot = Dot(axes.c2p(x, y), radius=0.05, color=WHITE, fill_opacity=0.7)
            points.add(dot)
            
        # MPI Line
        # Script: "...MPI line was set where it could eliminate many materials..."
        # Line represents constant C_CO2 / sigma (ignoring rho for the visual guide)
        line_start = axes.c2p(100, 1)
        line_end = axes.c2p(900, 7.5)
        mpi_line = Line(line_start, line_end, color=CYAN, stroke_width=3)
        
        line_label = Text("MPI Guide", font_size=16, color=CYAN, weight=BOLD)
        line_label.next_to(mpi_line.get_center(), UP + RIGHT, buff=0.2)
        
        # Explanation Text
        # Script: "Since density is dependent on the material... critical value cannot be determined"
        expl_text = Text(
            "Density varies per material,\nso a single critical line\nis approximate.",
            font_size=20,
            color=WHITE,
            line_spacing=1.0
        )
        expl_text.to_edge(RIGHT, buff=0.8).shift(UP * 0.5)
        
        expl_text2 = Text(
            "Line eliminates poor\ncandidates while keeping\noptions open.",
            font_size=20,
            color=WHITE,
            line_spacing=1.0
        )
        expl_text2.next_to(expl_text, DOWN, buff=0.6)
        
        # ----------------------------------------------------------------
        # ANIMATION PHASE 2 (Graph)
        # ----------------------------------------------------------------
        
        self.play(
            Create(axes, run_time=1.0),
            FadeIn(x_label, run_time=0.5),
            FadeIn(y_label, run_time=0.5)
        )
        
        self.play(FadeIn(points, lag_ratio=0.1, run_time=1.5))
        
        self.play(Create(mpi_line, run_time=1.0))
        self.play(FadeIn(line_label, run_time=0.5))
        
        self.play(FadeIn(expl_text, run_time=1.0))
        self.wait(2.0) # Wait for narration about density
        
        self.play(FadeIn(expl_text2, run_time=1.0))
        self.wait(3.0) # Wait for narration about eliminating materials
        
        # ================================================================
        # EXIT
        # ================================================================
        
        self.play(
            FadeOut(expl_text, run_time=0.5),
            FadeOut(expl_text2, run_time=0.5),
            FadeOut(mpi_line, run_time=0.5),
            FadeOut(line_label, run_time=0.5),
            FadeOut(points, run_time=0.5),
            FadeOut(axes, run_time=0.5),
            FadeOut(x_label, run_time=0.5),
            FadeOut(y_label, run_time=0.5),
            FadeOut(title, run_time=0.5)
        )
        self.wait(0.3)
