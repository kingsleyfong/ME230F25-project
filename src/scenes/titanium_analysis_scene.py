from manim import *

Text.set_default(font="Segoe UI")

CYAN = "#00CED1"


class TitaniumAnalysisScene(Scene):
    def construct(self):
        # ================================================================
        # TITLE
        # ================================================================
        title = Text("Alpha beta titanium alloy analysis", font_size=36)
        title.to_edge(UP, buff=0.5)

        # ------------------------------------------------------------
        # LEFT SIDE - AS SUPPLIED TITANIUM (SLIDE 24)
        # ------------------------------------------------------------
        left_header = Text("As supplied alloy", font_size=28)

        c1 = Text("Alpha beta titanium alloy", font_size=22)
        c2 = Text("Used in jet engine components", font_size=22)
        c3 = Text("High strength with low density", font_size=22)

        comp_lines = VGroup(c1, c2, c3).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        comp_box = RoundedRectangle(
            corner_radius=0.2,
            width=comp_lines.width + 0.5,
            height=comp_lines.height + 0.5,
            stroke_color=GRAY,
        )
        comp_lines.move_to(comp_box.get_center())
        left_comp_group = VGroup(comp_box, comp_lines)

        t_init = Text("Thickness from MPIs: t = 5.15 mm", font_size=26)
        t_init.set_color(CYAN)

        money_icon = Circle(
            radius=0.14,
            stroke_color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.2,
        )
        money_label = Text("$", font_size=18, color=GREEN).move_to(
            money_icon.get_center()
        )
        money = VGroup(money_icon, money_label)

        co2_icon = Circle(
            radius=0.14,
            stroke_color=RED,
            fill_color=RED,
            fill_opacity=0.2,
        )
        co2_label = Text("CO2", font_size=14, color=RED).move_to(
            co2_icon.get_center()
        )
        co2 = VGroup(co2_icon, co2_label)

        cost_text = Text("Cost ≈ 3900 dollars", font_size=22, color=GREEN)
        co2_text = Text("CO2 ≈ 1900 kg", font_size=22, color=RED)

        cost_row = VGroup(money, cost_text).arrange(RIGHT, buff=0.2)
        co2_row = VGroup(co2, co2_text).arrange(RIGHT, buff=0.2)

        left_bottom = VGroup(cost_row, co2_row).arrange(
            DOWN, aligned_edge=LEFT, buff=0.12
        )

        left_column = VGroup(
            left_header,
            left_comp_group,
            t_init,
            left_bottom,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        # ------------------------------------------------------------
        # RIGHT SIDE - AFTER HEAT TREATMENT (SLIDE 25)
        # ------------------------------------------------------------
        right_header = Text("After heat treatment", font_size=28)

        ht1 = Text(
            "Solution treat in beta or alpha plus beta region",
            font_size=20,
        )
        ht2 = Text("Quench to retain high strength phase", font_size=20)
        ht3 = Text("Age to precipitate strengthening phases", font_size=20)

        ht_lines = VGroup(ht1, ht2, ht3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.07
        )

        t_new = Text("Bending MPI: t = 4.3 mm", font_size=26)
        t_new.set_color(CYAN)

        money2_icon = money_icon.copy()
        money2_label = Text("$", font_size=18, color=GREEN).move_to(
            money2_icon.get_center()
        )
        money2 = VGroup(money2_icon, money2_label)

        co22_icon = co2_icon.copy()
        co22_label = Text("CO2", font_size=14, color=RED).move_to(
            co22_icon.get_center()
        )
        co22 = VGroup(co22_icon, co22_label)

        cost2_text = Text("Cost ≈ 3500 dollars", font_size=22, color=GREEN)
        co22_text = Text("CO2 ≈ 1200 kg", font_size=22, color=RED)

        cost2_row = VGroup(money2, cost2_text).arrange(RIGHT, buff=0.2)
        co22_row = VGroup(co22, co22_text).arrange(RIGHT, buff=0.2)

        right_bottom = VGroup(cost2_row, co22_row).arrange(
            DOWN, aligned_edge=LEFT, buff=0.12
        )

        caption = Text(
            "Heat treatment allows a thinner wall and lower environmental impact.",
            font_size=22,
        )

        right_column = VGroup(
            right_header,
            ht_lines,
            t_new,
            right_bottom,
            caption,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        # ------------------------------------------------------------
        # POSITION GROUPS AND ARROW (CENTERED, NO OFF SCREEN)
        # ------------------------------------------------------------
        # Arrange left and right columns horizontally and center them
        columns = VGroup(left_column, right_column).arrange(
            RIGHT, buff=1.2, aligned_edge=UP
        )

        # Scale down slightly so everything fits comfortably
        columns.scale(0.8)

        # Place the pair under the title and center on screen
        columns.next_to(title, DOWN, buff=0.4)
        columns.move_to(ORIGIN + DOWN * 0.2)

        # Unpack for animation
        left_group, right_group = columns

        # Arrow between old and new thickness (after layout is final)
        arrow = Arrow(
            start=t_init.get_right() + RIGHT * 0.2,
            end=t_new.get_left() + LEFT * 0.2,
            stroke_color=CYAN,
        )

        # ================================================================
        # ANIMATION SEQUENCE
        # ================================================================
        self.play(FadeIn(title), run_time=1.0)
        self.wait(0.3)

        # Left side
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
