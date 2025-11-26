from manim import *

Text.set_default(font="Segoe UI")

CYAN = "#00CED1"

class IronAnalysisScene(Scene):
    def construct(self):
        # ================================================================
        # LAYOUT
        # ================================================================

        # Title
        title = Text("Iron base superalloy analysis", font_size=40)
        title.to_edge(UP, buff=0.5)

        # ------------------------------------------------------------
        # LEFT SIDE - AS SUPPLIED IRON SUPERALLOY (SLIDE 26)
        # ------------------------------------------------------------

        # Left subheader
        left_header = Text("As supplied alloy", font_size=30)

        # Composition bullets
        c1 = Text("50 percent Fe", font_size=24)
        c2 = Text("25 percent Ni", font_size=24)
        c3 = Text("15 percent Cr", font_size=24)
        c4 = Text("2 percent Ti", font_size=24)
        c5 = Text("Minor alloying additions", font_size=24)

        comp_lines = VGroup(c1, c2, c3, c4, c5).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        # Composition box
        comp_box = RoundedRectangle(
            corner_radius=0.2,
            width=comp_lines.width + 0.5,
            height=comp_lines.height + 0.5,
            stroke_color=GRAY,
        )
        comp_lines.move_to(comp_box.get_center())
        left_comp_group = VGroup(comp_box, comp_lines)

        # Thickness line
        t_init = Text("Thickness from MPIs: t = 3.34 mm", font_size=28)
        t_init.set_color(CYAN)

        # Cost and CO2 icons
        money_icon = Circle(radius=0.16, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.2)
        money_label = Text("$", font_size=20, color=GREEN).move_to(money_icon.get_center())
        money = VGroup(money_icon, money_label)

        co2_icon = Circle(radius=0.16, stroke_color=RED, fill_color=RED, fill_opacity=0.2)
        co2_label = Text("CO2", font_size=16, color=RED).move_to(co2_icon.get_center())
        co2 = VGroup(co2_icon, co2_label)

        # Cost and CO2 text
        cost_text = Text("Cost ≈ 2103.57 dollars", font_size=24, color=GREEN)
        co2_text  = Text("CO2 ≈ 1095.57 kg", font_size=24, color=RED)

        # Rows
        cost_row = VGroup(money, cost_text).arrange(RIGHT, buff=0.2)
        co2_row  = VGroup(co2,  co2_text).arrange(RIGHT, buff=0.2)

        # Stack
        left_bottom = VGroup(cost_row, co2_row).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        # Pack left column
        left_column = VGroup(
            left_header,
            left_comp_group,
            t_init,
            left_bottom,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        # ------------------------------------------------------------
        # RIGHT SIDE - AFTER HEAT TREATMENT (SLIDE 27)
        # ------------------------------------------------------------

        # Right subheader
        right_header = Text("After heat treatment", font_size=30)

        # Heat treatment description
        ht1 = Text("Austenitize to dissolve carbides", font_size=24)
        ht2 = Text("Quench to form martensite", font_size=24)
        ht3 = Text("Temper to recover toughness", font_size=24)
        ht4 = Text("and keep strength", font_size=24)

        ht_lines = VGroup(ht1, ht2, ht3, ht4).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        # Constraint note
        constraint_note = Text("Design now controlled by deflection", font_size=22)

        # New thickness
        t_new = Text("Deflection limit: t = 2.5 mm", font_size=28)
        t_new.set_color(CYAN)

        # Updated cost and CO2
        money2_icon = Circle(radius=0.16, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.2)
        money2_label = Text("$", font_size=20, color=GREEN).move_to(money2_icon.get_center())
        money2 = VGroup(money2_icon, money2_label)

        co22_icon = Circle(radius=0.16, stroke_color=RED, fill_color=RED, fill_opacity=0.2)
        co22_label = Text("CO2", font_size=16, color=RED).move_to(co22_icon.get_center())
        co22 = VGroup(co22_icon, co22_label)

        cost2_text = Text("Cost ≈ 1600 dollars", font_size=24, color=GREEN)
        co22_text  = Text("CO2 ≈ 820 kg", font_size=24, color=RED)

        cost2_row = VGroup(money2, cost2_text).arrange(RIGHT, buff=0.2)
        co22_row  = VGroup(co22,  co22_text).arrange(RIGHT, buff=0.2)

        right_bottom = VGroup(cost2_row, co22_row).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        # Caption (split into two lines)
        caption_line1 = Text("Higher yield strength shifts control from", font_size=22)
        caption_line2 = Text("bending to deflection and reduces cost and CO2.", font_size=22)
        caption = VGroup(caption_line1, caption_line2).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        # Right column
        right_column = VGroup(
            right_header,
            ht_lines,
            constraint_note,
            t_new,
            right_bottom,
            caption,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        # ------------------------------------------------------------
        # POSITION GROUPS AND ARROW
        # ------------------------------------------------------------

        # Create groups
        left_group = left_column
        right_group = right_column

        # Scale slightly to fit
        scale_factor = 0.85
        left_group.scale(scale_factor)
        right_group.scale(scale_factor)

        # Position below title
        left_group.next_to(title, DOWN, buff=0.5)
        right_group.next_to(title, DOWN, buff=0.5)

        # Push to edges
        left_group.to_edge(LEFT, buff=0.7)
        right_group.to_edge(RIGHT, buff=0.7)

        # Now create arrow after positions are final
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

        self.play(FadeIn(constraint_note), run_time=0.7)
        self.wait(0.2)

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