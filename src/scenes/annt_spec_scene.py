from manim import *

Text.set_default(font="Segoe UI")

class AnntSpecScene(Scene):
    def construct(self):
        # PHASE 0 — Imports and global style
        self.camera.background_color = BLACK

        # PHASE 1 — Title
        title = Text("ANNT Stainless Steel Bollard", color=WHITE)
        title.set_stroke(color=BLACK, width=1.5)
        title.to_edge(UP, buff=0.5)

        self.play(FadeIn(title, run_time=0.7))
        
        # PHASE 2 — Spec Sheet Pages (Side by Side)
        # Load images
        page1 = ImageMobject("assets/images/annt_spec/annt_spec_page1.jpg")
        page2 = ImageMobject("assets/images/annt_spec/annt_spec_page2.jpg")

        # Match heights so tops align
        page2.match_height(page1)

        # Arrange temporarily to calculate scale
        temp_group = Group(page1, page2).arrange(RIGHT, buff=0.5)
        target_width = config.frame_width * 0.7
        
        # Scale images to fit target width
        # Reduced scale slightly to avoid overlap with title
        scale_factor = (target_width / temp_group.width) * 0.85
        page1.scale(scale_factor)
        page2.scale(scale_factor)

        # Create backing elements (Shadow + Vignette)
        def create_backing(image):
            # Vignette (semi-transparent black rectangle behind)
            vignette = Rectangle(
                width=image.width * 1.05,
                height=image.height * 1.05,
                color=BLACK,
                fill_color=BLACK,
                fill_opacity=0.2,
                stroke_width=0
            )
            vignette.move_to(image)
            vignette.set_z_index(image.z_index - 2)

            # Drop shadow (offset black rect)
            shadow = Rectangle(
                width=image.width,
                height=image.height,
                color=BLACK,
                fill_color=BLACK,
                fill_opacity=0.5,
                stroke_width=0
            )
            # Offset shadow slightly down-right
            shadow.move_to(image.get_center() + DR * 0.1)
            shadow.set_z_index(image.z_index - 1)
            
            return vignette, shadow

        # Group images to center them
        image_group = Group(page1, page2).arrange(RIGHT, buff=0.5)
        # Shift down to avoid title overlap
        image_group.move_to(DOWN * 0.5)

        # Now create backings at the correct positions
        vig1, shad1 = create_backing(page1)
        vig2, shad2 = create_backing(page2)

        # Create groups for animation
        group1 = Group(vig1, shad1, page1)
        group2 = Group(vig2, shad2, page2)

        # Store final positions
        group1_target = group1.get_center()
        group2_target = group2.get_center()

        # Set initial positions for slide-in
        # Left image slides in from left
        group1.move_to(LEFT * (config.frame_width / 2 + group1.width))
        
        # Right image slides in from right
        group2.move_to(RIGHT * (config.frame_width / 2 + group2.width))

        # Animate slide in
        self.play(
            group1.animate.move_to(group1_target),
            group2.animate.move_to(group2_target),
            run_time=1.5,
            rate_func=smooth
        )

        # PHASE 3 — Caption
        caption_lines = [
            "AISI 304 stainless steel construction",
            "Commercial bollard model from ANNT",
            "Baseline material for comparison"
        ]
        
        caption_objs = []
        for line in caption_lines:
            t = Text(line, color=WHITE, font_size=24)
            t.set_stroke(color=BLACK, width=1.5)
            caption_objs.append(t)
        
        caption = VGroup(*caption_objs).arrange(DOWN, buff=0.2)
        caption.next_to(image_group, DOWN, buff=0.5)

        self.play(FadeIn(caption, run_time=1.0))
        self.wait(8.0) # Extended wait for voiceover

        # PHASE 4 — Exit Transition
        self.play(FadeOut(caption, run_time=0.5))
        self.play(
            FadeOut(group1, run_time=0.5),
            FadeOut(group2, run_time=0.5)
        )
        self.play(FadeOut(title, run_time=0.5))
        
        self.wait(0.3)
