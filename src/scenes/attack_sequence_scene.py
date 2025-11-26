from manim import *

Text.set_default(font="Segoe UI")

class AttackSequenceScene(Scene):
    def construct(self):
        # Global settings
        self.camera.background_color = BLACK

        # --- 1. TITLE CARD ---
        # "Vehicle as a Weapon Attacks"
        # "2016 to 2018"
        
        title = Text("Vehicle as a Weapon Attacks", font_size=48, color=WHITE)
        title.set_stroke(color=BLACK, width=2)
        title.move_to(UP * 0.5)

        subtitle = Text("2016 to 2018", font_size=36, color=WHITE)
        subtitle.set_stroke(color=BLACK, width=2)
        subtitle.next_to(title, DOWN, buff=0.5)

        title_group = VGroup(title, subtitle)

        # Animation: FadeIn 1.0s, Hold 1.5s, FadeOut 0.8s
        self.play(FadeIn(title_group, run_time=1.0))
        self.wait(1.5)
        self.play(FadeOut(title_group, run_time=0.8))

        # --- 2. ATTACK IMAGE SEQUENCE ---
        
        # Helper to create image group
        def create_image_slide(image_name, caption_text, year_text):
            # Load image
            # Assuming assets/attack_images/ exists relative to execution dir
            # If not found, Manim usually raises FileNotFoundError or shows placeholder.
            # We will use try-except block or just assume it works as per prompt.
            img_path = f"assets/images/attacks/{image_name}"
            
            # Create ImageMobject
            # We need to handle potential missing files gracefully if possible, 
            # but for this code generation we assume they exist.
            img = ImageMobject(img_path)
            
            # Scale to fit height of screen with some margin, or width
            # Screen height is 8 units (approx).
            img.height = 6.0 
            
            # Vignette
            # Full screen rectangle, black, opacity 0.3
            vignette = Rectangle(
                width=config.frame_width,
                height=config.frame_height,
                color=BLACK,
                fill_opacity=0.3,
                stroke_width=0
            )
            # Vignette goes on top of image? 
            # "Place this rectangle behind any captions but in front of the background."
            # And "Group the image and vignette together".
            # If it's in front of background but behind caption, it should be:
            # [Background] [Image] [Vignette] [Caption]
            # But the prompt says "Group the image and vignette together so they animate as one."
            # So Image + Vignette.
            
            # Caption
            # "Nice, France 2016"
            full_caption = f"{caption_text}  {year_text}"
            caption = Text(full_caption, font_size=32, color=WHITE)
            caption.set_stroke(color=BLACK, width=2)
            caption.to_edge(DOWN, buff=1.0)
            
            # Group: Image, Vignette (on top of image), Caption (on top of vignette)
            # Wait, if vignette is full screen, it covers the image.
            # If we group them, FadeIn(group) fades them all in.
            
            # Let's verify Z-order.
            # We want Image at back, Vignette over it, Caption over Vignette.
            
            # However, if vignette is full screen, it might darken the whole scene including previous elements?
            # But previous elements are faded out.
            
            slide_group = Group(img, vignette, caption)
            return slide_group

        # Define sequence data
        # (Image file, Caption Text, Year/Suffix, FadeIn, Hold, FadeOut)
        sequence_data = [
            ("nice_2016.jpg", "Nice, France", "2016", 1.0, 6.0, 0.8),
            ("berlin_2016.jpg", "Berlin", "2016", 0.7, 1.2, 0.5),
            ("london_2017.jpg", "London", "2017", 0.7, 1.0, 0.5),
            ("barcelona_2017.jpg", "Barcelona", "2017", 0.7, 1.0, 0.5),
            ("toronto_2018.jpg", "Toronto", "2018", 0.7, 1.5, 0.8),
        ]

        for img_file, cap_text, year, t_in, t_hold, t_out in sequence_data:
            # Create slide
            # Note: We create it fresh each time
            
            # Image path
            img_path = f"assets/images/attacks/{img_file}"
            
            # Image
            image = ImageMobject(img_path)
            # Scale to cover most of screen but keep aspect ratio
            # Let's scale to height 7.5 to leave room for caption
            image.height = 7.5
            
            # Vignette
            vignette = Rectangle(
                width=config.frame_width,
                height=config.frame_height,
                color=BLACK,
                fill_opacity=0.3,
                stroke_width=0
            )
            
            # Caption
            caption_str = f"{cap_text}  {year}"
            caption = Text(caption_str, font_size=36, color=WHITE)
            caption.set_stroke(color=BLACK, width=2)
            caption.to_edge(DOWN, buff=0.5)
            
            # Group
            # Order matters for display
            slide = Group(image, vignette, caption)
            
            # Animation
            self.play(FadeIn(slide, run_time=t_in))
            self.wait(t_hold)
            self.play(FadeOut(slide, run_time=t_out))


        # --- 3. END CARD ---
        # "How do we stop this?"
        
        end_text = Text("How do we stop this?", font_size=48, color=WHITE)
        end_text.set_stroke(color=BLACK, width=2)
        end_text.move_to(ORIGIN)

        # Animation: FadeIn 1.0s, Hold 1.5s, FadeOut 1.0s
        self.play(FadeIn(end_text, run_time=1.0))
        self.wait(1.5)
        self.play(FadeOut(end_text, run_time=1.0))
