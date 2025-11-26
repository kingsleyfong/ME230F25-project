from manim import *

Text.set_default(font="Segoe UI")

CYAN = "#00CED1"

class NickelAnalysisScene(Scene):
    def construct(self):
        # ================================================================
        # TITLE
        # ================================================================
        
        title = Text(
            "Nickel Co Cr Alloy Analysis",
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
        line1 = Text("• 45% Ni", font_size=24, color=GRAY_A)
        line2 = Text("• 25% Co", font_size=24, color=GRAY_A)
        line3 = Text("• 17% Cr", font_size=24, color=GRAY_A)
        line4 = Text("• < 5% other metals", font_size=24, color=GRAY_A)
        
        comp_group = VGroup(comp_title, line1, line2, line3, line4).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Thickness calculations
        t_yield = Text("Yield Strength MPI: t = 7.26 mm", font_size=24, color=WHITE)
        t_bending = Text("Bending Stress MPI: t = 40.5 mm", font_size=24, color=CYAN)
        t_stiffness = Text("Stiffness MPI: t = 2.8 mm", font_size=24, color=WHITE)
        
        t_group = VGroup(t_yield, t_bending, t_stiffness).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        # Cost and CO2
        cost_text = Text("Cost: $17,823.90", font_size=26, color=GREEN_B)
        co2_text = Text("CO2: 4,926.01 kg", font_size=26, color=RED_B)
        
        results_group = VGroup(cost_text, co2_text).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        # Assemble Left Column
        left_column = VGroup(left_header, comp_group, t_group, results_group)
        left_column.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Position Left Column
        # Move to left side of screen, but keep some margin
        # Position Left Column
        # Move to left side of screen, but keep some margin
        # Align vertically below the title with some buffer
        left_column.next_to(title, DOWN, buff=0.5)
        left_column.to_edge(LEFT, buff=1.0)
        
        # ================================================================
        # RIGHT SIDE - AFTER HEAT TREATMENT
        # ================================================================
        
        # Header
        right_header = Text("After Heat Treatment", font_size=32, color=BLUE_B)
        
        # Treatment details
        treat_title = Text("Treatment:", font_size=24, color=WHITE)
        treat1 = Text("• 53% Cold Reduction", font_size=24, color=GRAY_A)
        treat2 = Text("• Age at 538°C for 4hr", font_size=24, color=GRAY_A)
        
        treat_group = VGroup(treat_title, treat1, treat2).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        # New Thickness
        t_new = Text("Bending Stress MPI: t = 28.6 mm", font_size=24, color=CYAN)
        
        # New Cost and CO2
        cost2_text = Text("Cost: $12,565.20", font_size=26, color=GREEN_B)
        co22_text = Text("CO2: 3,472.66 kg", font_size=26, color=RED_B)
        
        results2_group = VGroup(cost2_text, co22_text).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        # Assemble Right Column
        right_column = VGroup(right_header, treat_group, t_new, results2_group)
        right_column.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Position Right Column
        # Align top with left column
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
        # "Nickle Cobalt Chromium alloy, containing 45% Ni, 25% Co, 17% Cr, <5% a number of other metals."
        self.play(FadeIn(left_header, shift=DOWN), run_time=0.8)
        self.play(FadeIn(comp_group, shift=RIGHT), run_time=2.0)
        self.wait(4.5) # Adjusted for ~20 words
        
        # "According to the yield strength MPI, t needs to be 7.26 mm,"
        self.play(FadeIn(t_yield, shift=RIGHT), run_time=1.0)
        self.wait(2.5)
        
        # "according to the bending stress MPI, t needs to be 40.5 mm,"
        self.play(FadeIn(t_bending, shift=RIGHT), run_time=1.0)
        self.wait(2.5)
        
        # "and according to the stiffness MPI, t needs to be 2.8 mm."
        self.play(FadeIn(t_stiffness, shift=RIGHT), run_time=1.0)
        self.wait(2.5)
        
        # "Taking the maximum value of 40.5 mm,"
        self.play(Indicate(t_bending, color=YELLOW, scale_factor=1.05), run_time=1.5)
        self.wait(1.0)
        
        # "we calculated the cost to be $17823.9 and CO2 output to be 4926.01 kg."
        self.play(FadeIn(results_group, shift=UP), run_time=1.5)
        self.wait(4.0)
        
        # --- SCRIPT PART 2 ---
        # "The best treatment for this nickel alloy to maximize strength was found to be 53% Cold Reduction, then aging it at 538°C for 4hr."
        self.play(FadeIn(right_header, shift=DOWN), run_time=0.8)
        self.play(FadeIn(treat_group, shift=RIGHT), run_time=2.0)
        self.wait(7.0) # Adjusted for ~25 words
        
        # "After this, the bending stress MPI allows a t = 28.6 mm,"
        self.play(
            GrowArrow(arrow),
            FadeIn(t_new, shift=RIGHT),
            run_time=2.0
        )
        self.wait(3.0)
        
        # "which lowers the cost to $12565.2 and CO2 output to 3472.66 kg"
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
