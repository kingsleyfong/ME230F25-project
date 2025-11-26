# File: src/scenes/additional_and_selected_scene.py

from manim import *

Text.set_default(font="Segoe UI")

CYAN = "#00CED1"


class AdditionalAndSelectedScene(Scene):
    def construct(self):
        # ================================================================
        # TITLE
        # ================================================================
        
        title = Text(
            "Additional durability filters and selected materials",
            font_size=36,
            color=WHITE,
            weight=BOLD
        )
        title.to_edge(UP, buff=0.4)
        
        # ================================================================
        # PHASE 1 - DURABILITY GRID
        # ================================================================
        
        durability_header = Text(
            "Durability and safety requirements",
            font_size=24,
            color=WHITE
        )
        durability_header.next_to(title, DOWN, buff=0.3)
        
        # Define common scale for icons and text
        icon_scale = 0.6
        text_size = 20
        
        # 1. Resistant to fresh water
        drop1 = Circle(radius=0.15, color=WHITE, stroke_width=2, fill_opacity=0.2)
        drop1_top = Triangle(color=WHITE, stroke_width=2, fill_opacity=0.2).scale(0.15)
        drop1_top.move_to(drop1.get_top() + UP * 0.05)
        icon1 = VGroup(drop1, drop1_top).scale(icon_scale)
        label1 = Text("Resistant to fresh water", font_size=text_size, color=WHITE)
        group1 = VGroup(icon1, label1).arrange(RIGHT, buff=0.2)
        
        # 2. Resistant to salt water
        drop2 = Circle(radius=0.15, color=WHITE, stroke_width=2, fill_opacity=0.2)
        drop2_top = Triangle(color=WHITE, stroke_width=2, fill_opacity=0.2).scale(0.15)
        drop2_top.move_to(drop2.get_top() + UP * 0.05)
        salt_grain = Square(side_length=0.05, color=WHITE, fill_opacity=0.5)
        salt_grain.move_to(drop2.get_center())
        icon2 = VGroup(drop2, drop2_top, salt_grain).scale(icon_scale)
        label2 = Text("Resistant to salt water", font_size=text_size, color=WHITE)
        group2 = VGroup(icon2, label2).arrange(RIGHT, buff=0.2)
        
        # 3. Resistant to organic solvents
        beaker1 = Polygon(
            LEFT * 0.15 + UP * 0.2,
            RIGHT * 0.15 + UP * 0.2,
            RIGHT * 0.2 + DOWN * 0.2,
            LEFT * 0.2 + DOWN * 0.2,
            color=WHITE, stroke_width=2, fill_opacity=0.15
        )
        icon3 = VGroup(beaker1).scale(icon_scale)
        label3 = Text("Resistant to organic solvents", font_size=text_size, color=WHITE)
        group3 = VGroup(icon3, label3).arrange(RIGHT, buff=0.2)
        
        # 4. Resistant to weak acids
        beaker2 = Polygon(
            LEFT * 0.15 + UP * 0.2,
            RIGHT * 0.15 + UP * 0.2,
            RIGHT * 0.2 + DOWN * 0.2,
            LEFT * 0.2 + DOWN * 0.2,
            color=WHITE, stroke_width=2, fill_opacity=0.15
        )
        bubble = Circle(radius=0.05, color=WHITE, stroke_width=1)
        bubble.next_to(beaker2, UP, buff=0.05)
        icon4 = VGroup(beaker2, bubble).scale(icon_scale)
        label4 = Text("Resistant to weak acids", font_size=text_size, color=WHITE)
        group4 = VGroup(icon4, label4).arrange(RIGHT, buff=0.2)
        
        # 5. Resistant to UV radiation
        sun_core = Circle(radius=0.1, color=WHITE, stroke_width=2, fill_opacity=0.2)
        rays = VGroup()
        for i in range(8):
            ray = Line(UP * 0.12, UP * 0.18, color=WHITE, stroke_width=2)
            ray.rotate(i * PI / 4, about_point=ORIGIN)
            rays.add(ray)
        icon5 = VGroup(sun_core, rays).scale(icon_scale)
        label5 = Text("Resistant to UV radiation", font_size=text_size, color=WHITE)
        group5 = VGroup(icon5, label5).arrange(RIGHT, buff=0.2)
        
        # 6. Non flammable
        flame = Polygon(
            DOWN * 0.2,
            RIGHT * 0.15 + DOWN * 0.1,
            RIGHT * 0.05 + UP * 0.1,
            UP * 0.2,
            LEFT * 0.05 + UP * 0.1,
            LEFT * 0.15 + DOWN * 0.1,
            color=WHITE, stroke_width=2, fill_opacity=0.15
        )
        cross = Line(LEFT * 0.2 + DOWN * 0.2, RIGHT * 0.2 + UP * 0.2, color=CYAN, stroke_width=3)
        icon6 = VGroup(flame, cross).scale(icon_scale)
        label6 = Text("Non flammable", font_size=text_size, color=WHITE)
        group6 = VGroup(icon6, label6).arrange(RIGHT, buff=0.2)
        
        # 7. Recyclable
        arrow1 = Arrow(LEFT * 0.15 + DOWN * 0.1, UP * 0.15, color=WHITE, stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.3)
        arrow2 = Arrow(UP * 0.15, RIGHT * 0.15 + DOWN * 0.1, color=WHITE, stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.3)
        arrow3 = Arrow(RIGHT * 0.15 + DOWN * 0.1, LEFT * 0.15 + DOWN * 0.1, color=WHITE, stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.3)
        icon7 = VGroup(arrow1, arrow2, arrow3).scale(0.5) # Scale down recyclable icon more
        label7 = Text("Recyclable", font_size=text_size, color=WHITE)
        group7 = VGroup(icon7, label7).arrange(RIGHT, buff=0.2)
        
        # Grid arrangement
        # Use 2 columns instead of 3 to fit text better
        durability_grid = VGroup(
            group1, group2, 
            group3, group4, 
            group5, group6,
            group7
        ).arrange_in_grid(rows=4, cols=2, buff=(1.0, 0.5), cell_alignment=LEFT)
        
        # Center the last item (Recyclable) in the grid manually if needed, 
        # or just let it be in the 4th row, 1st column.
        # Let's center the whole grid
        durability_grid.move_to(ORIGIN).shift(DOWN * 0.3)
        
        # Summary line
        summary_line = Text(
            "Only materials meeting these durability criteria were retained.",
            font_size=18,
            color=WHITE
        )
        summary_line.next_to(durability_grid, DOWN, buff=0.5)
        
        # ================================================================
        # PHASE 2 - SELECTED MATERIALS
        # ================================================================
        
        final_header = Text(
            "Final materials selected for detailed analysis",
            font_size=24,
            color=WHITE
        )
        final_header.next_to(title, DOWN, buff=0.3)
        
        # Material list
        mat_size = 32
        mat1 = Text("• Nickel Co Cr alloy AEREX 350", font_size=mat_size, color=WHITE)
        mat2 = Text("• Stainless steel martensitic AISI 440C", font_size=mat_size, color=WHITE)
        mat3 = Text("• Cobalt base superalloy MP35N", font_size=mat_size, color=WHITE)
        mat4 = Text("• Titanium alpha beta alloy", font_size=mat_size, color=WHITE)
        mat5 = Text("• Iron base Cr Ni superalloy A 286", font_size=mat_size, color=WHITE)
        mat6 = Text("• Aluminum alloy from Lab 2", font_size=mat_size, color=WHITE)
        
        material_list = VGroup(mat1, mat2, mat3, mat4, mat5, mat6)
        material_list.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        material_list.move_to(ORIGIN).shift(DOWN * 0.2)
        
        final_caption = Text(
            "Thousands of initial candidates were reduced to about three hundred, then to this short list.",
            font_size=18,
            color=WHITE
        )
        final_caption.next_to(material_list, DOWN, buff=0.6)
        
        # ================================================================
        # ANIMATION SEQUENCE
        # ================================================================
        
        # 1. FadeIn title
        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)
        
        # 2. Phase 1: Durability grid
        self.play(FadeIn(durability_header, run_time=0.8))
        self.wait(0.3)
        
        # FadeIn grid items sequentially
        grid_items = [group1, group2, group3, group4, group5, group6, group7]
        self.play(FadeIn(VGroup(*grid_items), lag_ratio=0.2, run_time=2.0))
        self.wait(0.5)
        
        self.play(FadeIn(summary_line, run_time=0.8))
        self.wait(2.0)
        
        # 3. Phase 2: Transition to selected materials
        
        # Completely FadeOut grid and header/summary to clear screen
        self.play(
            FadeOut(durability_grid, run_time=0.8),
            FadeOut(durability_header, run_time=0.8),
            FadeOut(summary_line, run_time=0.8)
        )
        self.wait(0.2)
        
        # Show new header
        self.play(FadeIn(final_header, run_time=0.8))
        self.wait(0.5)
        
        # Show materials one by one with highlight
        for mat in material_list:
            self.play(FadeIn(mat, run_time=0.5))
            self.play(mat.animate.set_color(CYAN), run_time=0.2)
            self.wait(0.1)
            self.play(mat.animate.set_color(WHITE), run_time=0.2)
        
        self.wait(0.5)
        
        # Show final caption
        self.play(FadeIn(final_caption, run_time=1.0))
        self.wait(3.0)
        
        # ================================================================
        # EXIT
        # ================================================================
        
        self.play(
            FadeOut(final_caption, run_time=1.0),
            FadeOut(material_list, run_time=1.0),
            FadeOut(final_header, run_time=1.0),
            FadeOut(title, run_time=1.0)
        )
        
        self.wait(0.3)
