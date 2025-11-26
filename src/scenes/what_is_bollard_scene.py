from manim import *

Text.set_default(font="Segoe UI")

class WhatIsBollardScene(Scene):
    def construct(self):
        # Global settings
        self.camera.background_color = "#050505" # Nearly black

        # --- PHASE 1 – Title ---
        title = Text("What is a bollard?", font_size=48, color=WHITE)

        title.to_edge(UP, buff=0.5)

        self.play(FadeIn(title, run_time=1.0))
        
        # --- PHASE 2 – Context Diagram ---
        # Diagram container
        diagram = VGroup()

        # Ground line
        ground_line = Line(LEFT * 6, RIGHT * 6, color=WHITE, stroke_width=2)
        ground_line.shift(DOWN * 2)

        # Zones
        # Road: Left of x=0
        road_label = Text("Road", font_size=24, color=WHITE)

        road_label.move_to(LEFT * 3.5 + DOWN * 2.5)

        # Sidewalk: Right of x=0
        sidewalk_label = Text("Sidewalk / public space", font_size=24, color=WHITE)

        sidewalk_label.move_to(RIGHT * 3.5 + DOWN * 2.5)

        # Bollard: Center
        # Simple cylinder outline
        bollard_body = Rectangle(width=0.4, height=1.2, color=WHITE)
        bollard_body.set_stroke(width=2)
        bollard_body.set_fill(color=BLACK, opacity=1) # Cover background
        bollard_body.move_to(ground_line.get_center() + UP * 0.6)
        
        # Cyan highlight
        bollard_highlight = bollard_body.copy().set_color("#00FFFF").set_stroke(width=2, opacity=0.8)

        bollard_label = Text("Bollard", font_size=20, color="#00FFFF")

        bollard_label.next_to(bollard_body, UP, buff=0.2)
        
        bollard_group = VGroup(bollard_body, bollard_highlight, bollard_label)

        # Building: Far right background
        building = Rectangle(width=2.5, height=4, color=GREY)
        building.set_stroke(width=1)
        building.set_fill(color=GREY, opacity=0.1)
        # Align bottom with ground
        building.move_to(RIGHT * 5 + UP * (4/2 - 2)) 
        
        # Car Icon (Left)
        # Simple silhouette
        car_body = RoundedRectangle(corner_radius=0.2, width=1.8, height=0.6, color=WHITE)
        car_top = RoundedRectangle(corner_radius=0.2, width=1.0, height=0.5, color=WHITE)
        car_top.next_to(car_body, UP, buff=0)
        car_wheels = VGroup(
            Circle(radius=0.2, color=WHITE).move_to(car_body.get_bottom() + LEFT * 0.5),
            Circle(radius=0.2, color=WHITE).move_to(car_body.get_bottom() + RIGHT * 0.5)
        )
        car = VGroup(car_body, car_top, car_wheels)
        car.set_stroke(width=1.5)
        car.scale(0.6)
        car.move_to(LEFT * 4 + DOWN * 1.6) # On ground

        # Pedestrian Icon (Right)
        # Stick figure
        head = Circle(radius=0.15, color=WHITE)
        body_line = Line(UP*0.15, DOWN*0.4, color=WHITE)
        arms = Line(LEFT*0.3, RIGHT*0.3, color=WHITE).move_to(UP*0)
        legs = VGroup(
            Line(DOWN*0.4, DOWN*0.8 + LEFT*0.2, color=WHITE),
            Line(DOWN*0.4, DOWN*0.8 + RIGHT*0.2, color=WHITE)
        )
        pedestrian = VGroup(head, body_line, arms, legs)
        pedestrian.set_stroke(width=1.5)
        pedestrian.move_to(RIGHT * 2 + DOWN * 1.5)

        diagram.add(ground_line, road_label, sidewalk_label, bollard_group, building, car, pedestrian)

        # Animation Sequence
        # 1. Ground and zones
        self.play(Create(ground_line), FadeIn(road_label), FadeIn(sidewalk_label))
        
        # 2. Bollard
        self.play(Create(bollard_body), FadeIn(bollard_highlight), FadeIn(bollard_label))
        
        # 3. Building
        self.play(FadeIn(building))
        
        # 4. Car slide in
        self.play(FadeIn(car, shift=RIGHT))
        
        # 5. Pedestrian fade in
        self.play(FadeIn(pedestrian))

        # --- PHASE 3 – Definition Bullets ---
        bullets = VGroup()
        b1 = Text("• Safety device separating vehicles and pedestrians", font_size=28, color=WHITE)
        b2 = Text("• Rigid post embedded into the ground", font_size=28, color=WHITE)
        b3 = Text("• Placed between roads and public spaces", font_size=28, color=WHITE)
        
        bullets.add(b1, b2, b3)
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        
        # Position: Upper middle/right. Diagram is mostly bottom.
        bullets.next_to(title, DOWN, buff=0.5)
        
        for b in bullets:
            self.play(FadeIn(b))
            self.wait(0.5)

        # --- PHASE 4 – Purpose and Impact Illustration ---
        
        # 1. Impact arrow
        arrow_start = car.get_right() + RIGHT * 0.1
        arrow_end = bollard_body.get_left()
        impact_arrow = Arrow(start=arrow_start, end=arrow_end, color="#00FFFF", buff=0.1)
        
        self.play(GrowArrow(impact_arrow))

        # 2. Impact absorption
        # Glow
        impact_glow = bollard_body.copy().set_color("#00FFFF").set_stroke(width=4, opacity=0.5).scale(1.2)
        
        # Shield/Curved lines
        shield = Arc(radius=0.5, start_angle=PI/2, angle=PI, color="#00FFFF")
        shield.move_to(bollard_body.get_left())
        shield.set_stroke(width=2)
        
        # 3. Purpose bullet
        b4 = Text("• Absorbs vehicle impact to protect people and buildings", font_size=28, color="#00FFFF")

        b4.next_to(bullets, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(
            FadeIn(impact_glow),
            Create(shield),
            FadeIn(b4)
        )
        
        self.wait(2.0)

        # --- PHASE 5 – Exit ---
        self.play(
            FadeOut(impact_arrow),
            FadeOut(impact_glow),
            FadeOut(shield),
            run_time=1.0
        )
        self.play(
            FadeOut(car),
            FadeOut(pedestrian),
            run_time=1.0
        )
        self.play(
            FadeOut(bullets),
            FadeOut(b4),
            run_time=1.0
        )
        self.play(
            FadeOut(building),
            FadeOut(bollard_group),
            FadeOut(ground_line),
            FadeOut(road_label),
            FadeOut(sidewalk_label),
            run_time=1.0
        )
        self.play(FadeOut(title), run_time=1.0)
        
        self.wait(0.3)
