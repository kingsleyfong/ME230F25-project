from manim import *

Text.set_default(font="Segoe UI")

CYAN = "#00CED1"

class StainlessAnalysisScene(Scene):
    def construct(self):
        # ================================================================
        # TITLE
        # ================================================================
        
        title = Text(
            "Martensitic Stainless Steel 440C Analysis",
            font_size=40,
            color=WHITE,
            weight=BOLD
        )
        title.to_edge(UP, buff=0.5)
        
        # ================================================================
        # LEFT SIDE - AS SUPPLIED ALLOY
        # ================================================================
        
        # Header
        left_header = Text("As Supplied Alloy", font_size=32, color=BLUE_B)
        
        # Composition
        comp_title = Text("Composition:", font_size=24, color=WHITE)
        line1 = Text("• 78% Fe", font_size=24, color=GRAY_A)
        line2 = Text("• 16% Cr", font_size=24, color=GRAY_A)
        line3 = Text("• 1.2% C", font_size=24, color=GRAY_A)
        line4 = Text("• < 1% other metals", font_size=24, color=GRAY_A)
        
        comp_group = VGroup(comp_title, line1, line2, line3, line4).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Thickness calculations
        t_yield = Text("Yield Strength MPI: t = 7.66 mm", font_size=24, color=WHITE)
        t_bending = Text("Bending Stress MPI: t = 33.38 mm", font_size=24, color=CYAN)
        t_stiffness = Text("Stiffness MPI: t = 3.15 mm", font_size=24, color=WHITE)
        
        t_group = VGroup(t_yield, t_bending, t_stiffness).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        # Cost and CO2
        cost_text = Text("Cost: $477.93", font_size=26, color=GREEN_B)
        co2_text = Text("CO2: 441.50 kg", font_size=26, color=RED_B)
        
        results_group = VGroup(cost_text, co2_text).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        # Assemble Left Column
        left_column = VGroup(left_header, comp_group, t_group, results_group)
        left_column.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Position Left Column
        left_column.next_to(title, DOWN, buff=0.5)
        left_column.to_edge(LEFT, buff=1.0)
        
        # ================================================================
        # RIGHT SIDE - AFTER HEAT TREATMENT
        # ================================================================
        
        # Header
        right_header = Text("After Heat Treatment", font_size=32, color=BLUE_B)
        
        # Treatment details
        treat_title = Text("Treatment:", font_size=24, color=WHITE)
        treat1 = Text("• Temper at 150°C", font_size=24, color=GRAY_A)
        treat2 = Text("• Quench", font_size=24, color=GRAY_A)
        
        treat_group = VGroup(treat_title, treat1, treat2).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        # New Thickness
        t_new = Text("Bending Stress MPI: t = 28.82 mm", font_size=24, color=CYAN)
        
        # New Cost and CO2
        cost2_text = Text("Cost: $376.40", font_size=26, color=GREEN_B)
        co22_text = Text("CO2: 412.39 kg", font_size=26, color=RED_B)
        
        results2_group = VGroup(cost2_text, co22_text).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        # Assemble Right Column
        right_column = VGroup(right_header, treat_group, t_new, results2_group)
        right_column.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Position Right Column
        right_column.next_to(left_column, RIGHT, buff=2.0).align_to(left_column, UP)
        
        # Arrow
        arrow = Arrow(
            start=t_bending.get_right(),
            end=t_new.get_left(),
            color=CYAN,
            buff=0.2,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        # ================================================================
        # ANIMATION SCRIPT
        # ================================================================
        
        # 0. Intro Title
        self.play(Write(title), run_time=1.0)
        self.wait(0.5)
        
        # --- SCRIPT PART 1 ---
        # "Martensitic Stainless Steel 440C is 78% Fe, 16% Cr, 1.2% C, < 1% a number of other metals."
        self.play(FadeIn(left_header, shift=DOWN), run_time=0.8)
        self.play(FadeIn(comp_group, shift=RIGHT), run_time=2.0)
        self.wait(6.0) # Adjusted for ~20 words
        
        # "Solving the yield strength MPI for t gives 7.66 mm,"
        self.play(FadeIn(t_yield, shift=RIGHT), run_time=1.0)
        self.wait(2.5)
        
        # "Bending stress gives 33.38 mm,"
        self.play(FadeIn(t_bending, shift=RIGHT), run_time=1.0)
        self.wait(2.0)
        
        # "and Stiffness gives, 3.15 mm."
        self.play(FadeIn(t_stiffness, shift=RIGHT), run_time=1.0)
        self.wait(2.0)
        
        # "Taking the maximum value of t = 33.38 mm,"
        self.play(Indicate(t_bending, color=YELLOW, scale_factor=1.05), run_time=1.5)
        self.wait(1.5)
        
        # "the cost is equal to $477.93 and the CO2 output is 441.5 kg."
        self.play(FadeIn(results_group, shift=UP), run_time=1.5)
        self.wait(4.0)
        
        # --- SCRIPT PART 2 ---
        # "The best heat treatment to maximize strength is tempering at 150 degrees Celsius, then quenching it."
        self.play(FadeIn(right_header, shift=DOWN), run_time=0.8)
        self.play(FadeIn(treat_group, shift=RIGHT), run_time=2.0)
        self.wait(5.0) # Adjusted for ~18 words
        
        # "After this, the bending stress MPI gives a value of t equal to 28.82 mm."
        self.play(
            GrowArrow(arrow),
            FadeIn(t_new, shift=RIGHT),
            run_time=2.0
        )
        self.wait(4.0)
        
        # "This lowers the cost to $376.40 and the CO2 output to 412.39 kg."
        self.play(FadeIn(results2_group, shift=UP), run_time=1.5)
        self.wait(4.0)
        
        # Final pause
        self.wait(2.0)
        
        # Fade out
        self.play(
            FadeOut(left_column),
            FadeOut(right_column),
            FadeOut(arrow),
            FadeOut(title),
            run_time=1.5
        )
