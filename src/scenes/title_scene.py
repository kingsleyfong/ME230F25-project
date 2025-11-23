from manim import *
Text.set_default(font="Segoe UI")

class TitleScene(MovingCameraScene):
    def construct(self):
        # Phase 1: Background and main title
        # Optional subtle background gradient effect
        background_shape = Circle(radius=10, color=BLUE_E, fill_opacity=0.1).set_z_index(-1)
        
        # Create all text elements first to plan layout
        title = Text("ME230 Materials Selection Project", font_size=42, color=WHITE)
        subtitle = Text("Ram Raid Resistant Bollard Design", font_size=32, color=BLUE_B)
        course_text = Text("Mechanical Engineering, University of Waterloo", font_size=20, color=GRAY_B)
        term_text = Text("Fall 2025", font_size=20, color=GRAY_B)
        
        # Group top elements
        title_group = VGroup(title, subtitle, course_text, term_text).arrange(DOWN, buff=0.3)
        # Adjust internal spacing of title group slightly if needed
        subtitle.next_to(title, DOWN, buff=0.4)
        course_text.next_to(subtitle, DOWN, buff=0.6)
        term_text.next_to(course_text, DOWN, buff=0.2)
        
        # Move title group up to leave room for members
        title_group.move_to(UP * 1.5)

        # Phase 1 Animation
        self.play(FadeIn(background_shape, run_time=2.0), Write(title, run_time=1.2))
        self.wait(0.5)

        # Phase 2: Subtitle
        self.play(FadeIn(subtitle, run_time=1.0))
        self.wait(0.5)

        # Phase 3: Course and term lines
        course_info = VGroup(course_text, term_text)
        self.play(FadeIn(course_info, run_time=0.8))
        self.wait(1.0)

        # Phase 4: Group members block
        member_header = Text("Group Members", font_size=24, color=GRAY_C)
        member_1 = Text("Adam Benaissa", font_size=22, color=GRAY_C)
        member_2 = Text("Joseph Schuurman", font_size=22, color=GRAY_C)
        member_3 = Text("Kingsley Fong", font_size=22, color=GRAY_C)
        
        members_block = VGroup(member_header, member_1, member_2, member_3).arrange(DOWN, buff=0.2)
        
        # Position members block relative to the title group to ensure no overlap
        # Or place it at a fixed position lower down
        members_block.next_to(title_group, DOWN, buff=1.5)
        
        self.play(FadeIn(members_block, run_time=1.0))
        self.wait(1.5)

        # Phase 5: Subtle camera zoom
        # Zoom in slightly to create a dynamic feel
        self.play(
            self.camera.frame.animate.scale(0.95),
            run_time=3.0
        )

        # Phase 6: Fade out to transition
        all_elements = VGroup(background_shape, title_group, members_block)
        self.play(FadeOut(all_elements, run_time=1.0))
        self.wait(0.5)
