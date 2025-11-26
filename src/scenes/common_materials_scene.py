from manim import *

Text.set_default(font="Segoe UI")

class CommonMaterialsScene(Scene):
    def construct(self):
        # Global settings
        self.camera.background_color = "#050505" # Nearly black

        # --- PHASE 1 – Title ---
        title = Text("Common bollard materials and design baseline", font_size=40, color=WHITE)
        title.set_stroke(color=BLACK, width=1.5)
        title.to_edge(UP, buff=0.5)

        self.play(FadeIn(title, run_time=1.0))

        # --- PHASE 2 – Material classes ---
        
        # Helper to create a card
        def create_card(header_text, bullets_list, icon_mobject, position):
            card_width = 4.0
            card_height = 5.5
            
            # Card outline
            outline = RoundedRectangle(corner_radius=0.2, width=card_width, height=card_height, color=WHITE)
            outline.set_stroke(width=1.5)
            
            # Header
            header = Text(header_text, font_size=28, color=WHITE)
            header.set_stroke(color=BLACK, width=1.5)
            header.next_to(outline.get_top(), DOWN, buff=0.3)
            
            # Cyan accent line
            accent = Line(LEFT * (card_width/2 - 0.2), RIGHT * (card_width/2 - 0.2), color="#00FFFF")
            accent.next_to(header, DOWN, buff=0.1)
            
            # Icon placement
            icon_mobject.next_to(accent, DOWN, buff=0.3)
            
            # Bullets
            bullet_group = VGroup()
            for b_text in bullets_list:
                dot = Text("•", font_size=20, color=WHITE)
                txt = Text(b_text, font_size=20, color=WHITE)
                line = VGroup(dot, txt).arrange(RIGHT, buff=0.1, aligned_edge=UP)
                bullet_group.add(line)
            
            bullet_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            bullet_group.next_to(icon_mobject, DOWN, buff=0.4)
            
            # Group everything
            card_group = VGroup(outline, header, accent, icon_mobject, bullet_group)
            card_group.move_to(position)
            return card_group, bullet_group

        # 1. Concrete Icon
        concrete_icon = Square(side_length=1.0, color=WHITE)
        crack1 = Line(concrete_icon.get_top() + LEFT*0.2, concrete_icon.get_center() + RIGHT*0.1, color=WHITE)
        crack2 = Line(concrete_icon.get_center() + RIGHT*0.1, concrete_icon.get_bottom() + LEFT*0.1, color=WHITE)
        concrete_icon_grp = VGroup(concrete_icon, crack1, crack2)

        # 2. Polymer Icon (Bent post)
        poly_path = VMobject(color=WHITE)
        poly_path.set_points_smoothly([
            UP*0.5 + LEFT*0.2,
            UP*0.2 + LEFT*0.1,
            ORIGIN,
            DOWN*0.2 + RIGHT*0.1,
            DOWN*0.5 + RIGHT*0.2
        ])
        # Make it a thick line or outline
        poly_icon = poly_path.set_stroke(width=4)
        # Or a shape
        poly_shape = VGroup(
            Line(UP*0.5, UP*0.2, color=WHITE),
            Arc(radius=0.5, start_angle=PI, angle=-PI/4, color=WHITE).shift(RIGHT*0.5),
        ) # Simplified bent shape
        # Let's use a simple curved rectangle approximation
        poly_icon_grp = RoundedRectangle(corner_radius=0.2, width=0.4, height=1.0, color=WHITE)
        poly_icon_grp.apply_function(lambda p: p + np.array([0.1 * (p[1]**2), 0, 0])) # Bend it slightly

        # 3. Metal Icon (Cylinder)
        metal_body = Rectangle(width=0.4, height=1.0, color=WHITE)
        metal_top = Ellipse(width=0.4, height=0.15, color=WHITE).move_to(metal_body.get_top())
        metal_icon_grp = VGroup(metal_body, metal_top)

        # Create Cards
        # Positions: Left (-4), Center (0), Right (4)
        concrete_card, concrete_bullets = create_card(
            "Concrete", 
            ["Brittle failure", "Poor energy absorption", "Quality varies"], 
            concrete_icon_grp, 
            LEFT * 4.2
        )
        
        polymer_card, polymer_bullets = create_card(
            "Polymers", 
            ["Good for low speed", "Not for high energy impacts"], 
            poly_icon_grp, 
            ORIGIN
        )
        
        metal_card, metal_bullets = create_card(
            "Metals", 
            ["High strength", "Better energy absorption", "Suitable for K4 type impacts"], 
            metal_icon_grp, 
            RIGHT * 4.2
        )

        # Animation 1: Slide in cards
        self.play(
            FadeIn(concrete_card, shift=RIGHT),
            FadeIn(polymer_card, shift=RIGHT),
            FadeIn(metal_card, shift=RIGHT),
            run_time=1.0
        )

        # Animation 2-4: FadeIn bullets
        for b in concrete_bullets:
            self.play(FadeIn(b, run_time=0.3))
        self.wait(0.2)
        
        for b in polymer_bullets:
            self.play(FadeIn(b, run_time=0.3))
        self.wait(0.2)
        
        for b in metal_bullets:
            self.play(FadeIn(b, run_time=0.3))
        self.wait(0.5)

        # Highlight Metals
        # Dim others
        self.play(
            concrete_card.animate.set_opacity(0.3),
            polymer_card.animate.set_opacity(0.3),
            run_time=1.0
        )
        
        # Glow for metals
        metal_glow = metal_card[0].copy().set_color("#00FFFF").set_stroke(width=4, opacity=0.5)
        self.play(FadeIn(metal_glow))

        # Bottom text
        focus_text = Text("This study focuses on metal bollards.", font_size=32, color=WHITE)
        focus_text.set_stroke(color=BLACK, width=1.5)
        focus_text.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(focus_text))
        self.wait(1.0)

        # --- PHASE 3 – Steel focus ---
        # Transition: Fade out others, Move Metal card to left
        self.play(
            FadeOut(concrete_card),
            FadeOut(polymer_card),
            FadeOut(focus_text),
            FadeOut(metal_glow), # Remove glow during move
            metal_card.animate.to_edge(LEFT, buff=1.0).scale(1.1),
            run_time=1.5
        )

        # Update Header to "Steel bollards"
        # metal_card children: 0:outline, 1:header, 2:accent, 3:icon, 4:bullets
        old_header = metal_card[1]
        new_header = Text("Steel bollards", font_size=28, color=WHITE)
        new_header.set_stroke(color=BLACK, width=1.5)
        new_header.move_to(old_header.get_center())
        
        self.play(Transform(old_header, new_header))

        # Update Bullets
        # 1. "Most common bollard type"
        # 2. "Relatively low cost"
        # 3. "One major impact can deform steel and crack the base"
        
        new_bullet_texts = [
            "Most common bollard type",
            "Relatively low cost",
            "One major impact can deform steel and crack the base"
        ]
        
        # Rebuild bullets group
        new_bullets_grp = VGroup()
        for b_text in new_bullet_texts:
            dot = Text("•", font_size=20, color=WHITE)
            # Wrap text if too long? "One major impact..." might be long.
            # Manim Text doesn't auto wrap easily, but we can scale or break lines manually if needed.
            # Let's try fitting it.
            if "One major impact" in b_text:
                txt = Text("One major impact can deform\nsteel and crack the base", font_size=20, color=WHITE, line_spacing=1.0)
            else:
                txt = Text(b_text, font_size=20, color=WHITE)
            line = VGroup(dot, txt).arrange(RIGHT, buff=0.1, aligned_edge=UP)
            new_bullets_grp.add(line)
            
        new_bullets_grp.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        # Position where old bullets were
        # metal_card[4] is the old bullets group
        new_bullets_grp.move_to(metal_card[4].get_center(), aligned_edge=LEFT)
        # Adjust vertical alignment if needed
        new_bullets_grp.next_to(metal_card[3], DOWN, buff=0.4)
        
        self.play(FadeOut(metal_card[4]), FadeIn(new_bullets_grp))
        # Update the reference in the group so it moves with it if we moved it again (not needed here but good practice)
        metal_card.remove(metal_card[4])
        metal_card.add(new_bullets_grp)

        # Impact Animation
        # Add concrete base
        # metal_card[3] is the icon group
        icon = metal_card[3]
        base = Rectangle(width=0.8, height=0.2, color=GREY)
        base.set_fill(GREY, opacity=0.5)
        base.next_to(icon, DOWN, buff=0)
        self.play(FadeIn(base))
        
        # Impact: Nudge icon
        self.play(icon.animate.shift(RIGHT * 0.1), run_time=0.1)
        self.play(icon.animate.shift(LEFT * 0.1), run_time=0.1)
        
        # Deform icon
        # Skew or rotate slightly
        bent_icon = icon.copy()
        # Simple rotation for bending
        bent_icon.rotate(-10 * DEGREES, about_point=bent_icon.get_bottom())
        # Shift top part more?
        
        # Crack in base
        base_crack = Line(base.get_top(), base.get_bottom() + RIGHT*0.1, color=BLACK, stroke_width=2)
        
        self.play(
            Transform(icon, bent_icon),
            Create(base_crack),
            run_time=1.0
        )
        
        self.wait(1.0)

        # --- PHASE 4 – Standards and K4 baseline ---
        
        # Standards Panel (Right side)
        standards_panel = VGroup()
        s_outline = RoundedRectangle(corner_radius=0.2, width=5.0, height=3.0, color=WHITE)
        s_header = Text("Vehicle impact standards", font_size=24, color=WHITE)
        s_header.next_to(s_outline.get_top(), DOWN, buff=0.2)
        s_accent = Line(LEFT*2, RIGHT*2, color="#00FFFF").next_to(s_header, DOWN, buff=0.1)
        
        s_bullets = VGroup(
            Text("• ASTM F2656", font_size=20, color=WHITE),
            Text("• ASTM F3016", font_size=20, color=WHITE),
            Text("• IWA 14", font_size=20, color=WHITE),
            Text("• U.S. DoS K ratings (K4, K8, K12)", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        s_bullets.next_to(s_accent, DOWN, buff=0.3)
        
        standards_panel.add(s_outline, s_header, s_accent, s_bullets)
        standards_panel.move_to(RIGHT * 3.5 + UP * 1.5)
        
        # K4 Baseline Card (Below Standards)
        k4_panel = VGroup()
        k_outline = RoundedRectangle(corner_radius=0.2, width=5.0, height=3.0, color=WHITE)
        k_header = Text("Baseline for this study", font_size=24, color=WHITE)
        k_header.next_to(k_outline.get_top(), DOWN, buff=0.2)
        k_accent = Line(LEFT*2, RIGHT*2, color="#00FFFF").next_to(k_header, DOWN, buff=0.1)
        
        k_bullets = VGroup(
            Text("• K4 rating: 2000 kg at 57 km/h", font_size=20, color=WHITE),
            Text("• All loads, thickness sizing, and\n  MPIs reference this scenario", font_size=20, color=WHITE, line_spacing=1.0)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        k_bullets.next_to(k_accent, DOWN, buff=0.2)
        
        # Schematic Icon
        # Car -> Arrow -> Bollard
        schematic = VGroup()
        s_car = RoundedRectangle(corner_radius=0.1, width=0.6, height=0.3, color=WHITE)
        s_bollard = Rectangle(width=0.1, height=0.4, color=WHITE)
        s_arrow = Arrow(start=LEFT*0.5, end=RIGHT*0.5, color="#00FFFF", buff=0, max_tip_length_to_length_ratio=0.3)
        
        s_car.next_to(s_arrow, LEFT, buff=0.1)
        s_bollard.next_to(s_arrow, RIGHT, buff=0.1)
        
        schematic.add(s_car, s_arrow, s_bollard)
        schematic.next_to(k_bullets, DOWN, buff=0.3)
        
        # Labels
        l_mass = Text("2000 kg", font_size=16, color="#00FFFF").next_to(s_car, UP, buff=0.1)
        l_speed = Text("57 km/h", font_size=16, color="#00FFFF").next_to(s_arrow, UP, buff=0.1)
        
        k4_panel.add(k_outline, k_header, k_accent, k_bullets, schematic, l_mass, l_speed)
        k4_panel.move_to(RIGHT * 3.5 + DOWN * 2.0)

        # Animations Phase 4
        self.play(FadeIn(standards_panel))
        self.play(FadeIn(k4_panel))
        self.play(GrowArrow(s_arrow))
        self.play(FadeIn(l_mass), FadeIn(l_speed))
        
        self.wait(2.0)

        # --- PHASE 5 – Exit ---
        self.play(
            FadeOut(standards_panel),
            FadeOut(k4_panel),
            run_time=1.0
        )
        self.play(
            FadeOut(metal_card),
            FadeOut(base),
            FadeOut(base_crack),
            run_time=1.0
        )
        # "This study focuses..." was already faded out earlier.
        self.play(FadeOut(title), run_time=1.0)
        
        self.wait(0.3)
