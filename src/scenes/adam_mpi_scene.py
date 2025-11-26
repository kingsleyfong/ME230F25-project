# File: src/scenes/adam_mpi_scene.py

from manim import *
Text.set_default(font="Segoe UI")

CYAN = "#00CED1"


class AdamMPIScene(Scene):
    def construct(self):
        # ================================================================
        # TITLE
        # ================================================================
        
        title = Text(
            "Adam's material performance index for cost",
            font_size=36,
            color=WHITE,
            weight=BOLD
        )
        title.to_edge(UP, buff=0.4)
        
        # ================================================================
        # EQUATIONS BLOCK WITH ICONS (CENTER)
        # ================================================================
        
        # 1. Cost equation
        # Script: "For the cost equation we have that cost = the material constant of cost per meters cubed times the volume."
        eq1 = MathTex(
            r"\text{Cost} = C_{m^3} \cdot V",
            font_size=40,
            color=WHITE
        )
        
        # Dollar icon
        dollar_circle = Circle(radius=0.2, color=WHITE, stroke_width=2, fill_opacity=0.2)
        dollar_symbol = Text("$", color=CYAN, weight=BOLD).scale(0.4)
        dollar_symbol.move_to(dollar_circle.get_center())
        dollar_icon = VGroup(dollar_circle, dollar_symbol)
        
        eq1_group = VGroup(dollar_icon, eq1).arrange(RIGHT, buff=0.3)
        
        # 2. Bending moment rearrangement
        # Script: "Rearranging the formula for bending moment gives us t..."
        eq2 = MathTex(
            r"\sigma = \frac{M}{Z} \implies t \propto \frac{M}{\sigma_y \cdot D^2}",
            font_size=40,
            color=WHITE
        )
        
        # Bending icon
        bend_rect = Rectangle(width=0.3, height=0.08, color=WHITE, stroke_width=2, fill_opacity=0.15)
        bend_arrow = Arrow(UP * 0.15, DOWN * 0.05, color=CYAN, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.25)
        bend_arrow.next_to(bend_rect, UP, buff=0.05)
        bend_icon = VGroup(bend_rect, bend_arrow)
        
        eq2_group = VGroup(bend_icon, eq2).arrange(RIGHT, buff=0.3)
        
        # 3. Substitution into volume
        # Script: "...which we can sub into the volume of the cost equation."
        eq3 = MathTex(
            r"\text{Cost} = C_{m^3} \cdot (A_{\text{surface}} \cdot t)",
            font_size=40,
            color=WHITE
        )
        
        # Arrow icon
        arrow_icon = Arrow(
            LEFT * 0.2, RIGHT * 0.2,
            color=CYAN,
            stroke_width=3,
            buff=0,
            max_tip_length_to_length_ratio=0.3
        )
        
        eq3_group = VGroup(arrow_icon, eq3).arrange(RIGHT, buff=0.3)
        
        # 4. Separating constants
        # Script: "Putting out the material constants..."
        eq4 = MathTex(
            r"\text{Cost} \propto \left( \frac{C_{m^3}}{\sigma_y} \right) \cdot \frac{M \cdot A_{\text{surface}}}{D^2}",
            font_size=36,
            color=WHITE
        )
        
        # Material block icon
        material_block = Rectangle(width=0.3, height=0.3, color=WHITE, stroke_width=2, fill_opacity=0.15)
        stress_line1 = Line(
            material_block.get_left() + RIGHT * 0.025,
            material_block.get_right() + LEFT * 0.025,
            color=CYAN,
            stroke_width=2
        )
        stress_line1.move_to(material_block.get_top() + DOWN * 0.1)
        stress_line2 = Line(
            material_block.get_left() + RIGHT * 0.025,
            material_block.get_right() + LEFT * 0.025,
            color=CYAN,
            stroke_width=2
        )
        stress_line2.move_to(material_block.get_center())
        material_icon = VGroup(material_block, stress_line1, stress_line2)
        
        eq4_group = VGroup(material_icon, eq4).arrange(RIGHT, buff=0.3)
        
        # Arrange all equation groups vertically
        eqs = VGroup(eq1_group, eq2_group, eq3_group, eq4_group)
        eqs.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        eqs.shift(UP * 0.5)
        
        # ================================================================
        # FINAL MPI (BOTTOM)
        # ================================================================
        
        # Script: "...gives us an MPI of cost per meter cubed over yield strength that we are trying to minimize..."
        mpi_minimize = MathTex(
            r"\text{Minimize } \frac{C_{m^3}}{\sigma_y}",
            font_size=48,
            color=WHITE
        )
        
        # Script: "...as shown on the granta plot, we will flip our MPI to yield strength over cost per meter cubed."
        mpi_maximize = MathTex(
            r"\text{Maximize } \text{MPI} = \frac{\sigma_y}{C_{m^3}}",
            font_size=48,
            color=CYAN
        )
        
        # Position them
        mpi_minimize.next_to(eqs, DOWN, buff=0.8)
        mpi_maximize.move_to(mpi_minimize)
        
        # Create highlight box
        box = RoundedRectangle(
            corner_radius=0.15,
            width=mpi_maximize.width + 0.5,
            height=mpi_maximize.height + 0.3,
            stroke_color=CYAN,
            stroke_width=3,
            fill_opacity=0.05,
            fill_color=CYAN
        )
        box.move_to(mpi_maximize)
        
        mpi_group = VGroup(box, mpi_minimize) # Initially with minimize text
        
        # ================================================================
        # ANIMATION SEQUENCE
        # ================================================================
        
        # 1. FadeIn title
        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)
        
        # 2. Eq 1: Cost equation
        self.play(FadeIn(dollar_icon, run_time=0.5))
        self.play(FadeIn(eq1, run_time=0.8))
        self.wait(2.0)
        
        # 3. Eq 2: Rearranging for t
        self.play(FadeIn(bend_icon, run_time=0.5))
        self.play(FadeIn(eq2, run_time=0.8))
        self.wait(2.0)
        
        # 4. Eq 3: Substitution
        self.play(FadeIn(arrow_icon, run_time=0.5))
        self.play(FadeIn(eq3, run_time=0.8))
        self.wait(2.0)
        
        # 5. Eq 4: Separating constants
        self.play(FadeIn(material_icon, run_time=0.5))
        self.play(FadeIn(eq4, run_time=0.8))
        self.wait(2.0)
        
        # 6. Show Minimize form
        self.play(FadeIn(box, run_time=0.5))
        self.play(FadeIn(mpi_minimize, run_time=0.8))
        self.wait(2.0)
        
        # 7. Flip to Maximize form
        self.play(
            ReplacementTransform(mpi_minimize, mpi_maximize),
            run_time=1.0
        )
        self.play(Indicate(mpi_maximize, color=CYAN, scale_factor=1.1))
        self.wait(3.0)
        
        # ================================================================
        # EXIT
        # ================================================================
        
        self.play(
            FadeOut(box, run_time=1.0),
            FadeOut(mpi_maximize, run_time=1.0),
            FadeOut(eqs, run_time=1.0),
            FadeOut(title, run_time=1.0)
        )
        
        self.wait(0.3)
