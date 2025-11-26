from manim import *

Text.set_default(font="Segoe UI")

CYAN = "#00CED1"

class CobaltAnalysisScene(Scene):
    def construct(self):
        # ================================================================
        # LAYOUT
        # ================================================================

        # Title
        title = Text("Cobalt base superalloy MP35N analysis", font_size=40)
        title.to_edge(UP, buff=0.5)

        # ------------------------------------------------------------
        # LEFT SIDE – AS SUPPLIED MP35N (SLIDE 22)
        # ------------------------------------------------------------

        # Left subheader
        left_header = Text("As supplied alloy", font_size=30)

        # Composition box
        c1 = Text("Co Ni Cr Mo multiphase alloy", font_size=24)
        c2 = Text("Used in aerospace hardware", font_size=24)
        c3 = Text("Used in deep sea systems", font_size=24)

        comp_lines = VGroup(c1, c2, c3).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        comp_box = RoundedRectangle(
            corner_radius=0.2,
            width=comp_lines.width + 0.5,
            height=comp_lines.height + 0.5,
            stroke_color=GRAY,
        )
        comp_lines.move_to(comp_box.get_center())
        left_comp_group = VGroup(comp_box, comp_lines)

        # Thickness
        t_init = Text("Thickness from MPIs: t = 2.5 mm", font_size=28)
        t_init.set_color(CYAN)

        # Cost and CO2 icons with colors
        money_icon = Circle(radius=0.16, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.2)
        money_label = Text("$", font_size=20, color=GREEN).move_to(money_icon.get_center())
        money = VGroup(money_icon, money_label)

        co2_icon = Circle(radius=0.16, stroke_color=RED, fill_color=RED, fill_opacity=0.2)
        co2_label = Text("CO2", font_size=16, color=RED).move_to(co2_icon.get_center())
        co2 = VGroup(co2_icon, co2_label)

        # Cost and CO2 text with colors
        cost_text = Text("Cost ≈ 9900 dollars", font_size=24, color=GREEN)
        co2_text  = Text("CO2 ≈ 3800 kg", font_size=24, color=RED)

        # Rows
        cost_row = VGroup(money, cost_text).arrange(RIGHT, buff=0.2)
        co2_row  = VGroup(co2,  co2_text).arrange(RIGHT, buff=0.2)

        # Stack
        left_bottom = VGroup(cost_row, co2_row).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        # Pack the left column vertically
        left_column = VGroup(
            left_header,
            left_comp_group,
            t_init,
            left_bottom,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        # ------------------------------------------------------------
        # RIGHT SIDE – HEAT TREATED MP35N (SLIDE 23)
        # ------------------------------------------------------------

        right_header = Text("After heat treatment", font_size=30)

        ht1 = Text("Cold reduce by 50 percent", font_size=24)
        ht2 = Text("Age at 540 °C for 4 hours", font_size=24)
        ht3 = Text("Air cool, ordering strengthens alloy", font_size=24)

        ht_lines = VGroup(ht1, ht2, ht3).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        t_new = Text("Bending MPI: t = 1.9 mm", font_size=28)
        t_new.set_color(CYAN)

        money2_icon = Circle(radius=0.16, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.2)
        money2_label = Text("$", font_size=20, color=GREEN).move_to(money2_icon.get_center())
        money2 = VGroup(money2_icon, money2_label)

        co22_icon = Circle(radius=0.16, stroke_color=RED, fill_color=RED, fill_opacity=0.2)
        co22_label = Text("CO2", font_size=16, color=RED).move_to(co22_icon.get_center())
        co22 = VGroup(co22_icon, co22_label)

        cost2_text = Text("Cost ≈ 8000 dollars", font_size=24, color=GREEN)
        co22_text  = Text("CO2 ≈ 3400 kg", font_size=24, color=RED)

        cost2_row = VGroup(money2, cost2_text).arrange(RIGHT, buff=0.2)
        co22_row  = VGroup(co22,  co22_text).arrange(RIGHT, buff=0.2)

        right_bottom = VGroup(cost2_row, co22_row).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        caption = Text("Heat treatment reduces thickness, cost, and CO2.", font_size=24)

        right_column = VGroup(
            right_header,
            ht_lines,
            t_new,
            right_bottom,
            caption,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        # ------------------------------------------------------------
        # POSITION WHOLE GROUPS SO NOTHING IS OFF SCREEN
        # ------------------------------------------------------------

        left_group = left_column
        right_group = right_column

        # Scale both groups a bit so they fit nicely
        scale_factor = 0.9
        left_group.scale(scale_factor)
        right_group.scale(scale_factor)

        # Position relative to the title
        left_group.next_to(title, DOWN, buff=0.5)
        right_group.next_to(title, DOWN, buff=0.5)

        # Push them to left and right edges with some margin
        left_group.to_edge(LEFT, buff=0.7)
        right_group.to_edge(RIGHT, buff=0.7)

        # Now that positions are final, create the arrow
        arrow = Arrow(
            start=t_init.get_right() + RIGHT * 0.2,
            end=t_new.get_left()  + LEFT  * 0.2,
            stroke_color=CYAN,
        )

        # ================================================================
        # ANIMATION SEQUENCE
        # ================================================================

        # Title
        self.play(FadeIn(title), run_time=1.0)
        self.wait(0.3)

        # Left side stepwise
        self.play(FadeIn(left_header), run_time=0.8)
        self.wait(0.2)

        self.play(FadeIn(left_comp_group), run_time=1.0)
        self.wait(0.3)

        self.play(FadeIn(t_init), run_time=0.7)
        self.wait(0.2)

        self.play(FadeIn(cost_row), run_time=0.7)
        self.play(FadeIn(co2_row), run_time=0.7)
        self.wait(0.4)

        # Right side
        self.play(FadeIn(right_header), run_time=0.8)
        self.wait(0.2)

        self.play(FadeIn(ht_lines), run_time=1.0)
        self.wait(0.3)

        self.play(FadeIn(t_new), run_time=0.7)
        self.wait(0.2)

        self.play(GrowArrow(arrow), run_time=1.0)
        self.wait(0.3)

        self.play(FadeIn(cost2_row), run_time=0.7)
        self.play(FadeIn(co22_row), run_time=0.7)
        self.wait(0.4)

        self.play(FadeIn(caption), run_time=1.0)
        self.wait(2.0)

        # ================================================================
        # EXIT
        # ================================================================

        self.play(
            FadeOut(caption),
            FadeOut(right_group),
            FadeOut(arrow),
            FadeOut(left_group),
            FadeOut(title),
            run_time=1.0,
        )
        self.wait(0.3)
