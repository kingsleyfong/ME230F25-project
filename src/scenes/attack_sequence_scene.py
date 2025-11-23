from manim import *
Text.set_default(font="Segoe UI")

class AttackSequenceScene(Scene):
    def construct(self):
        # 1. Background: Pure black
        self.camera.background_color = BLACK

        # List of attacks: (Image Path, Caption Text)
        attacks = [
            ("assets/images/attacks/nice_2016.jpg", "Nice, France 2016"),
            ("assets/images/attacks/berlin_2016.jpg", "Berlin, Germany 2016"),
            ("assets/images/attacks/london_2017.jpg", "London, United Kingdom 2017"),
            ("assets/images/attacks/barcelona_2017.jpg", "Barcelona, Spain 2017"),
            ("assets/images/attacks/nyc_2017.jpg", "New York City, United States 2017"),
            ("assets/images/attacks/toronto_2018.jpg", "Toronto, Canada 2018"),
        ]

        for image_path, caption_text in attacks:
            # 2. Image setup
            image = ImageMobject(image_path)
            # Centered on screen at approx 70 percent of the frame width
            image.scale_to_fit_width(config.frame_width * 0.7)

            # 3. Vignette effect
            # Implemented using a VGroup with the image and layered rectangles
            # to simulate a soft, medium-strength black vignette.
            
            # Layer 1: Base darkening (subtle)
            vignette_base = Rectangle(
                width=image.width,
                height=image.height,
                color=BLACK,
                fill_opacity=0.15,
                stroke_width=0
            )
            
            # Layer 2: Soft border (simulating gradient edge)
            vignette_border = Rectangle(
                width=image.width,
                height=image.height,
                color=BLACK,
                fill_opacity=0,
                stroke_width=30,
                stroke_opacity=0.3
            )

            # Grouping image and vignette layers
            image_group = Group(image, vignette_base, vignette_border)

            # 6. & 7. Caption setup
            # White text with a thin black outline, bottom center
            caption = Text(caption_text, font_size=36, color=WHITE)
            caption.set_stroke(color=BLACK, width=2, opacity=1)
            caption.to_edge(DOWN, buff=1.0)

            # 4. Animation Sequence
            # Fade in over 0.5 seconds
            self.play(
                FadeIn(image_group, run_time=0.5),
                FadeIn(caption, run_time=0.5)
            )

            # Hold for 1.5 seconds
            self.wait(1.5)

            # Fade out over 0.7 seconds
            self.play(
                FadeOut(image_group, run_time=0.7),
                FadeOut(caption, run_time=0.7)
            )

        # 8. Final fade to black (implicit) and hold
        # The scene is already black after fade out, so we just wait.
        self.wait(1.0)
