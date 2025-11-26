from manim import *

Text.set_default(font="Segoe UI")

CYAN = "#00CED1"


class FinalDecisionScene(Scene):
    def construct(self):
        # ================================================================
        # TITLE
        # ================================================================
        title = Text("Decision Matrix and Conclusion", font_size=38, weight=BOLD, disable_ligatures=True)
        title.to_edge(UP, buff=0.4)

        # ================================================================
        # LEFT SIDE - SUMMARY OF ANALYSIS
        # ================================================================
        left_header = Text("Material Analysis Summary", font_size=26, weight=BOLD, disable_ligatures=True)
        left_header.set_color(CYAN)

        # Check icon using geometric shapes
        check_bg = Circle(radius=0.25, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.3, stroke_width=3)
        check_line1 = Line(LEFT * 0.15 + DOWN * 0.05, ORIGIN + DOWN * 0.15, color=GREEN, stroke_width=4)
        check_line2 = Line(ORIGIN + DOWN * 0.15, RIGHT * 0.2 + UP * 0.15, color=GREEN, stroke_width=4)
        check_icon = VGroup(check_bg, check_line1, check_line2)

        best_text = Text(
            "440C Stainless Steel",
            font_size=22,
            weight=BOLD,
            disable_ligatures=True,
        )
        best_text.set_color(YELLOW)
        
        best_subtext = Text(
            "Lowest cost & CO2 among viable candidates",
            font_size=18,
            disable_ligatures=True,
        )

        best_group = VGroup(best_text, best_subtext).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        best_row = VGroup(check_icon, best_group).arrange(RIGHT, buff=0.35, aligned_edge=UP)

        # Bullet points with icons
        bullet_icon1 = Square(side_length=0.12, fill_color=BLUE, fill_opacity=1, stroke_width=0)
        bullet_1 = Text(
            "Sized using K4 impact case",
            font_size=19,
            weight=BOLD,
            disable_ligatures=True,
        )
        bullet_row1 = VGroup(bullet_icon1, bullet_1).arrange(RIGHT, buff=0.2)

        bullet_icon2 = Square(side_length=0.12, fill_color=BLUE, fill_opacity=1, stroke_width=0)
        bullet_2 = Text(
            "Thickness set by restrictive MPI",
            font_size=19,
            weight=BOLD,
            disable_ligatures=True,
        )
        bullet_row2 = VGroup(bullet_icon2, bullet_2).arrange(RIGHT, buff=0.2)

        bullet_icon3 = Square(side_length=0.12, fill_color=BLUE, fill_opacity=1, stroke_width=0)
        bullet_3 = Text(
            "Cost/CO2 scale with thickness",
            font_size=19,
            weight=BOLD,
            disable_ligatures=True,
        )
        bullet_row3 = VGroup(bullet_icon3, bullet_3).arrange(RIGHT, buff=0.2)

        bullets = VGroup(bullet_row1, bullet_row2, bullet_row3).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        left_column = VGroup(
            left_header,
            best_row,
            bullets,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        # ================================================================
        # RIGHT SIDE - COMPARISON TABLE
        # ================================================================
        right_header = Text(
            "440C vs Annt Stainless Bollard",
            font_size=26,
            weight=BOLD,
            disable_ligatures=True,
        )
        right_header.set_color(CYAN)

        # Create cleaner table with simple geometry
        table_data = [
            ["Wall thickness", "~29 mm", "Slightly thinner"],
            ["Relative cost", "Low", "Slightly lower"],
            ["CO2 output", "Low", "Slightly lower"],
        ]

        # Build table manually for better control
        rows = VGroup()
        colors = [WHITE, WHITE, WHITE]
        highlight_colors = [CYAN, GREEN, GREEN]
        
        # Header row
        header_cells = VGroup(
            Text("Property", font_size=20, weight=BOLD, disable_ligatures=True),
            Text("440C Stainless", font_size=20, weight=BOLD, disable_ligatures=True),
            Text("Annt Bollard", font_size=20, weight=BOLD, disable_ligatures=True),
        ).arrange(RIGHT, buff=0.8)
        
        # Data rows
        for i, row_data in enumerate(table_data):
            row_cells = VGroup(
                Text(row_data[0], font_size=19, weight=BOLD, disable_ligatures=True).set_color(colors[i]),
                Text(row_data[1], font_size=19, weight=BOLD, disable_ligatures=True).set_color(highlight_colors[i]),
                Text(row_data[2], font_size=19, weight=BOLD, disable_ligatures=True).set_color(highlight_colors[i]),
            ).arrange(RIGHT, buff=0.8)
            
            # Align columns
            for j in range(3):
                row_cells[j].align_to(header_cells[j], LEFT)
            
            rows.add(row_cells)

        # Align all rows
        table_content = VGroup(header_cells, *rows).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        
        # Table frame
        table_bg = RoundedRectangle(
            corner_radius=0.2,
            width=table_content.width + 1,
            height=table_content.height + 0.6,
            stroke_color=GRAY,
            stroke_width=2,
            fill_color=GRAY,
            fill_opacity=0.1,
        )
        table_content.move_to(table_bg.get_center())
        table_group = VGroup(table_bg, table_content)

        # Winner indicator
        winner_icon = Star(n=5, outer_radius=0.2, inner_radius=0.09, fill_color=YELLOW, fill_opacity=0.8, stroke_color=YELLOW)
        winner_text = Text(
            "Winner: Annt Bollard",
            font_size=21,
            weight=BOLD,
            color=YELLOW,
            disable_ligatures=True,
        )
        winner_row = VGroup(winner_icon, winner_text).arrange(RIGHT, buff=0.25)

        # Reason
        reason_text = Text(
            "Reason: Bulk purchasing provides cost advantage",
            font_size=17,
            color=GRAY_B,
            slant=ITALIC,
            weight=BOLD,
            disable_ligatures=True,
        )

        right_column = VGroup(
            right_header,
            table_group,
            winner_row,
            reason_text,
        ).arrange(DOWN, aligned_edge=ORIGIN, buff=0.3)

        # ================================================================
        # FINAL CHOICE BANNER
        # ================================================================
        banner_bg = RoundedRectangle(
            corner_radius=0.3,
            width=10,
            height=0.8,
            fill_color=BLUE_D,
            fill_opacity=0.3,
            stroke_color=CYAN,
            stroke_width=3,
        )
        
        final_choice = Text(
            "Final Choice: Annt Stainless Steel Bollard",
            font_size=26,
            weight=BOLD,
            color=CYAN,
            disable_ligatures=True,
        )
        final_choice.move_to(banner_bg.get_center())
        
        banner = VGroup(banner_bg, final_choice)

        thank_you = Text(
            "Thank you for your attention",
            font_size=24,
            weight=BOLD,
            disable_ligatures=True,
        )

        # ================================================================
        # LAYOUT
        # ================================================================
        columns = VGroup(left_column, right_column).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        columns.scale(0.75)
        columns.next_to(title, DOWN, buff=0.5)
        columns.move_to(ORIGIN + UP * 0.3)

        banner.next_to(columns, DOWN, buff=0.6)
        thank_you.next_to(banner, DOWN, buff=0.4)

        left_group, right_group = columns

        # ================================================================
        # ANIMATIONS
        # ================================================================
        # Title
        self.play(Write(title), run_time=1.0)
        self.wait(0.4)

        # Left summary with emphasis animations
        self.play(FadeIn(left_header, shift=DOWN * 0.3), run_time=0.8)
        self.wait(0.3)

        self.play(
            GrowFromCenter(check_icon),
            run_time=0.7
        )
        self.play(FadeIn(best_group, shift=RIGHT * 0.3), run_time=0.8)
        self.wait(0.4)

        # Bullets appear sequentially
        for bullet_row in bullets:
            self.play(
                FadeIn(bullet_row[0], scale=0.5),
                Write(bullet_row[1]),
                run_time=0.6
            )
            self.wait(0.2)
        self.wait(0.5)

        # Right comparison - header
        self.play(FadeIn(right_header, shift=DOWN * 0.3), run_time=0.8)
        self.wait(0.3)

        # Table background
        self.play(Create(table_bg), run_time=0.7)
        
        # Table header
        self.play(FadeIn(header_cells, lag_ratio=0.1), run_time=0.8)
        self.wait(0.3)

        # Table rows appear one by one
        for row in rows:
            self.play(FadeIn(row, shift=DOWN * 0.2), run_time=0.6)
            self.wait(0.2)
        self.wait(0.6)

        # Winner announcement with flash
        self.play(
            Flash(winner_icon, color=YELLOW, flash_radius=0.4),
            GrowFromCenter(winner_icon),
            run_time=0.8
        )
        self.play(Write(winner_text), run_time=0.9)
        self.wait(0.5)

        # Reason
        self.play(FadeIn(reason_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1.0)

        # Final choice banner with emphasis
        self.play(
            Create(banner_bg),
            run_time=0.8
        )
        self.play(
            Write(final_choice),
            banner_bg.animate.set_fill(opacity=0.5),
            run_time=1.0
        )
        self.wait(0.6)

        # Thank you
        self.play(Write(thank_you), run_time=1.0)
        self.wait(2.5)

        # ================================================================
        # EXIT
        # ================================================================
        self.play(
            FadeOut(thank_you),
            FadeOut(banner),
            FadeOut(right_group),
            FadeOut(left_group),
            FadeOut(title),
            run_time=1.3,
        )
        self.wait(0.5)
