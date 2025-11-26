from manim import *

Text.set_default(font="Segoe UI")

CYAN = "#00CED1"


class AluminumAnalysisScene(Scene):
    def construct(self):
        # ================================================================
        # TITLE
        # ================================================================
        title = Text("Aluminum 6063 analysis", font_size=36)
        title.to_edge(UP, buff=0.5)

        # ------------------------------------------------------------
        # LEFT SIDE - LAB 2 ALUMINUM SAMPLE
        # ------------------------------------------------------------
        left_header = Text("Lab 2 aluminum sample", font_size=28)

        # Small alloy icon
        al_icon_circle = Circle(
            radius=0.22,
            stroke_color=BLUE_E,
            fill_color=BLUE_E,
            fill_opacity=0.25,
        )
        al_icon_label = Text("Al", font_size=22, color=WHITE).move_to(
            al_icon_circle.get_center()
        )
        al_icon = VGroup(al_icon_circle, al_icon_label)

        l1 = Text("Alloy 6063 aluminum", font_size=22)
        l2 = Text("Lab 2 tensile specimen", font_size=22)
        l3 = Text("Peak aged at 18 hours", font_size=22)

        info_lines = VGroup(l1, l2, l3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.08
        )

        info_box = RoundedRectangle(
            corner_radius=0.2,
            width=info_lines.width + 0.6,
            height=info_lines.height + 0.6,
            stroke_color=GRAY,
        )
        info_lines.move_to(info_box.get_center())
        info_group = VGroup(info_box, info_lines)

        ys_text = Text(
            "Average yield strength: 258.47 MPa",
            font_size=24,
        )
        ys_text.set_color(CYAN)

        left_column = VGroup(
            left_header,
            VGroup(al_icon, info_group).arrange(RIGHT, buff=0.3),
            ys_text,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        # ------------------------------------------------------------
        # RIGHT SIDE - THICKNESS REQUIREMENT
        # ------------------------------------------------------------
        right_header = Text("Thickness requirement", font_size=28)

        t_line = Text("Required thickness t = 228.6 mm", font_size=24)
        t_line.set_color(CYAN)

        d_line = Text("Outer diameter d = 137.5 mm", font_size=24)

        compare_line = Text("t is larger than d", font_size=24, color=YELLOW)

        # Not viable icon
        cross_circle = Circle(
            radius=0.22,
            stroke_color=RED_E,
            fill_color=RED_E,
            fill_opacity=0.25,
        )
        cross_1 = Line(LEFT * 0.12 + UP * 0.12, RIGHT * 0.12 + DOWN * 0.12, color=RED_E)
        cross_2 = Line(LEFT * 0.12 + DOWN * 0.12, RIGHT * 0.12 + UP * 0.12, color=RED_E)
        cross_icon = VGroup(cross_circle, cross_1, cross_2)

        not_viable_text = Text(
            "Aluminum 6063 is not viable for this bollard",
            font_size=22,
            color=RED_E,
        )

        not_viable_row = VGroup(cross_icon, not_viable_text).arrange(
            RIGHT, buff=0.3
        )

        caption = Text(
            "Required wall thickness exceeds the pipe diameter.",
            font_size=22,
        )

        right_column = VGroup(
            right_header,
            t_line,
            d_line,
            compare_line,
            not_viable_row,
            caption,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # ------------------------------------------------------------
        # POSITION GROUPS AND ARROW
        # ------------------------------------------------------------
        columns = VGroup(left_column, right_column).arrange(
            RIGHT, buff=1.2, aligned_edge=UP
        )

        columns.scale(0.8)
        columns.next_to(title, DOWN, buff=0.4)
        columns.move_to(ORIGIN + DOWN * 0.1)

        left_group, right_group = columns

        arrow = Arrow(
            start=left_group.get_right() + RIGHT * 0.2,
            end=right_group.get_left() + LEFT * 0.2,
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

        self.play(
            FadeIn(al_icon),
            FadeIn(info_group),
            run_time=1.0,
        )
        self.wait(0.3)

        self.play(FadeIn(ys_text), run_time=0.8)
        self.wait(0.4)

        # Right side
        self.play(GrowArrow(arrow), run_time=1.0)
        self.wait(0.3)

        self.play(FadeIn(right_header), run_time=0.8)
        self.wait(0.2)

        self.play(FadeIn(t_line), run_time=0.7)
        self.wait(0.2)

        self.play(FadeIn(d_line), run_time=0.7)
        self.wait(0.2)

        self.play(FadeIn(compare_line), run_time=0.7)
        self.wait(0.3)

        self.play(FadeIn(not_viable_row), run_time=0.9)
        self.wait(0.3)

        self.play(FadeIn(caption), run_time=0.9)
        self.wait(2.0)

        # ================================================================
        # EXIT
        # ================================================================
        self.play(
            FadeOut(caption),
            FadeOut(not_viable_row),
            FadeOut(compare_line),
            FadeOut(d_line),
            FadeOut(t_line),
            FadeOut(right_header),
            FadeOut(arrow),
            FadeOut(ys_text),
            FadeOut(info_group),
            FadeOut(al_icon),
            FadeOut(left_header),
            FadeOut(title),
            run_time=1.0,
        )
        self.wait(0.3)
