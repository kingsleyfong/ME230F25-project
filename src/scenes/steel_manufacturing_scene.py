from manim import *

Text.set_default(font="Segoe UI")

class SteelManufacturingScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # PHASE 1 - Title and horizontal process pipeline
        title = Text("Typical Steel Bollard Manufacturing", color=WHITE)
        title.set_stroke(color=BLACK, width=1.5)
        title.to_edge(UP, buff=0.5)

        self.play(FadeIn(title, run_time=0.7))
        self.wait(0.5)

        # Pipeline
        pipeline_line = Line(LEFT * 5, RIGHT * 5, color=WHITE, stroke_width=2).shift(UP * 2)
        
        labels = ["Design", "Testing", "Fabrication", "Finishing"]
        nodes = VGroup()
        for i, label_text in enumerate(labels):
            pos = pipeline_line.point_from_proportion(i / (len(labels) - 1))
            dot = Dot(point=pos, color=WHITE, radius=0.15)
            text = Text(label_text, font_size=20, color=WHITE).next_to(dot, UP, buff=0.2)
            text.set_stroke(color=BLACK, width=1.5)
            nodes.add(VGroup(dot, text))

        pipeline = VGroup(pipeline_line, nodes)
        
        self.play(Create(pipeline_line, run_time=1.0))
        self.play(FadeIn(nodes, run_time=1.0))
        self.wait(0.5)

        # Helper for bullets
        def create_bullets(text1, text2):
            b1 = Text(text1, font_size=24, color=WHITE)
            b1.set_stroke(color=BLACK, width=1.5)
            b2 = Text(text2, font_size=24, color=WHITE)
            b2.set_stroke(color=BLACK, width=1.5)
            g = VGroup(b1, b2).arrange(DOWN, buff=0.2)
            g.to_edge(DOWN, buff=1.0)
            return g

        # PHASE 2 - Design Phase
        # Script: "The design phase of bollards is pretty typical, starting with rough sketches, moving to 3D models,"
        design_node = nodes[0]
        self.play(
            design_node[0].animate.scale(1.5).set_color(BLUE),
            nodes[1].animate.set_opacity(0.3),
            nodes[2].animate.set_opacity(0.3),
            nodes[3].animate.set_opacity(0.3),
            run_time=0.5
        )

        # Panel 1: Rough Sketch
        sketch = VGroup(
            Line(DOWN, UP, color=GRAY),
            Line(LEFT, RIGHT, color=GRAY).shift(DOWN),
            Line(DOWN+LEFT*0.2, UP+RIGHT*0.2, color=GRAY).set_opacity(0.5)
        ).scale(1.5).shift(LEFT * 3)

        # Panel 2: CAD Model
        cad_model = VGroup(
            Rectangle(width=0.5, height=2.0, color=BLUE_B, stroke_width=2),
            Line(LEFT*0.5, RIGHT*0.5, color=BLUE_B).shift(DOWN)
        ).scale(1.5)

        # Panel 3: Prototype
        prototype = VGroup(
            RoundedRectangle(corner_radius=0.1, width=0.6, height=2.2, color=WHITE, stroke_width=3),
            Line(LEFT*0.8, RIGHT*0.8, color=WHITE).shift(DOWN*1.1)
        ).scale(1.5).shift(RIGHT * 3)
        
        # Checkmark for prototype
        check = Text("✓", color=GREEN, font_size=40).next_to(prototype, UP)

        self.play(FadeIn(sketch))
        self.play(FadeIn(cad_model))
        self.play(FadeIn(prototype), FadeIn(check))

        bullets_design = create_bullets("Concept sketches and rough dimensions", "3D CAD model and prototype")
        self.play(FadeIn(bullets_design))
        self.wait(5.0) # Hold for narration part 1
        self.play(FadeOut(bullets_design))
        
        # Dim design visuals
        design_visuals = VGroup(sketch, cad_model, prototype, check)
        self.play(design_visuals.animate.set_opacity(0.2))

        # PHASE 3 - Testing Phase
        # Script: "then after the prototype withstands the proper impact resistance and load testing, the bollard is manufactured."
        testing_node = nodes[1]
        self.play(
            design_node[0].animate.scale(1/1.5).set_color(WHITE).set_opacity(0.3),
            testing_node.animate.scale(1.5).set_color(BLUE).set_opacity(1),
            run_time=0.5
        )
        
        self.play(FadeOut(design_visuals))

        # Test Rig
        ground = Line(LEFT*3, RIGHT*3, color=WHITE)
        test_bollard = RoundedRectangle(corner_radius=0.1, width=0.6, height=2.0, color=WHITE).move_to(ground.get_center() + UP)
        sled = Rectangle(width=1.0, height=1.0, color=RED, fill_opacity=0.5).move_to(ground.get_left() + UP*0.5 + RIGHT*0.5)
        force_arrow = Arrow(sled.get_right(), test_bollard.get_left(), color=RED, buff=0.1)

        test_rig = VGroup(ground, test_bollard, sled, force_arrow)
        self.play(FadeIn(test_rig))

        # Impact Animation
        self.play(
            sled.animate.next_to(test_bollard, LEFT, buff=0),
            force_arrow.animate.put_start_and_end_on(sled.get_right() + RIGHT*2, test_bollard.get_left()), # Hacky arrow move
            run_time=1.0
        )
        # Deflection
        self.play(test_bollard.animate.rotate(-10*DEGREES, about_point=test_bollard.get_bottom()), run_time=0.2)
        self.play(test_bollard.animate.rotate(10*DEGREES, about_point=test_bollard.get_bottom()), run_time=0.2)
        
        # Pass
        pass_check = Text("✓ PASS", color=GREEN, font_size=40).next_to(test_bollard, UP, buff=0.5)
        self.play(FadeIn(pass_check))

        bullets_testing = create_bullets("Impact and load tests on prototype", "Verify required safety performance")
        self.play(FadeIn(bullets_testing))
        self.wait(6.0) # Hold for narration part 2
        self.play(FadeOut(bullets_testing))
        self.play(FadeOut(test_rig), FadeOut(pass_check))

        # PHASE 4 - Fabrication Phase
        # Script: "The material is either laser cut or cast into shape, and smaller parts are machined. Everything is then welded together."
        fab_node = nodes[2]
        self.play(
            testing_node[0].animate.scale(1/1.5).set_color(WHITE).set_opacity(0.3),
            fab_node.animate.scale(1.5).set_color(BLUE).set_opacity(1),
            run_time=0.5
        )

        # Frame 1: Raw Stock
        raw_plate = Rectangle(width=1.5, height=1.0, color=GRAY, fill_opacity=0.3).shift(LEFT*4)
        raw_tube = Rectangle(width=0.4, height=2.0, color=GRAY, fill_opacity=0.3).next_to(raw_plate, RIGHT, buff=0.5)
        frame1 = VGroup(raw_plate, raw_tube)
        
        # Frame 2: Cutting
        laser = Triangle(color=YELLOW, fill_opacity=1).scale(0.2).rotate(180*DEGREES).move_to(raw_plate.get_top() + UP*0.2)
        cut_plate = Rectangle(width=1.2, height=0.8, color=WHITE).move_to(raw_plate)
        frame2 = VGroup(laser, cut_plate)

        # Frame 3: Machining
        lathe_tool = Square(side_length=0.3, color=ORANGE, fill_opacity=1).move_to(raw_tube.get_right())
        machined_tube = RoundedRectangle(corner_radius=0.1, width=0.4, height=2.0, color=WHITE).move_to(raw_tube)
        frame3 = VGroup(lathe_tool, machined_tube)

        # Frame 4: Welding
        weld_plate = cut_plate.copy().move_to(RIGHT*3 + DOWN*1)
        weld_tube = machined_tube.copy().move_to(weld_plate.get_top() + UP*1)
        weld_spark = Star(color=YELLOW, fill_opacity=1).scale(0.2).move_to(weld_tube.get_bottom())
        frame4 = VGroup(weld_plate, weld_tube, weld_spark)

        # Sequence
        self.play(FadeIn(frame1))
        self.wait(0.5)
        self.play(Transform(frame1, frame2)) # Visualize cut
        self.wait(0.5)
        self.play(Transform(frame1, frame3)) # Visualize machine
        self.wait(0.5)
        self.play(Transform(frame1, frame4)) # Visualize weld
        self.wait(0.5)

        bullets_fab = create_bullets("Steel plate and tube cut and machined", "Components welded into one bollard")
        self.play(FadeIn(bullets_fab))
        self.wait(7.0) # Hold for narration part 3
        self.play(FadeOut(bullets_fab))
        self.play(FadeOut(frame1)) # frame1 holds the transformed mobject

        # PHASE 5 - Finishing Phase
        # Script: "Finally, the bollard is galvanized and given a powder coating for corrosion resistance. Lastly, a layer of bright paint is added for visibility."
        finish_node = nodes[3]
        self.play(
            fab_node[0].animate.scale(1/1.5).set_color(WHITE).set_opacity(0.3),
            finish_node.animate.scale(1.5).set_color(BLUE).set_opacity(1),
            run_time=0.5
        )

        # Base bollard for finishing
        fin_bollard = VGroup(
            Rectangle(width=1.2, height=0.2, color=WHITE), # Base
            RoundedRectangle(corner_radius=0.1, width=0.4, height=2.0, color=WHITE).shift(UP*1.1)
        ).move_to(ORIGIN)

        # Step 1: Galvanizing
        bath = Rectangle(width=3, height=1.5, color=BLUE_A, fill_opacity=0.3).shift(DOWN*0.5)
        bath_label = Text("Zinc Bath", font_size=20).next_to(bath, DOWN)
        
        self.play(FadeIn(fin_bollard), FadeIn(bath), FadeIn(bath_label))
        self.play(fin_bollard.animate.shift(DOWN*0.5).set_color(GRAY_B), run_time=1.0) # Dip
        self.play(fin_bollard.animate.shift(UP*0.5), run_time=1.0) # Remove
        self.play(FadeOut(bath), FadeOut(bath_label))

        # Step 2: Powder Coating
        nozzle = Rectangle(width=0.5, height=0.2, color=GRAY).next_to(fin_bollard, LEFT, buff=1.0)
        spray = VGroup(*[Dot(color=WHITE, radius=0.03).move_to(nozzle.get_right() + RIGHT*i*0.1 + UP*np.random.uniform(-0.2, 0.2)) for i in range(10)])
        
        self.play(FadeIn(nozzle))
        self.play(ShowPassingFlash(spray, run_time=1.0), fin_bollard.animate.set_color(WHITE)) # Coat
        self.play(FadeOut(nozzle))

        # Step 3: Paint
        brush = Line(UP, DOWN, color=YELLOW, stroke_width=5).next_to(fin_bollard, RIGHT, buff=0.5)
        self.play(FadeIn(brush))
        self.play(
            brush.animate.shift(LEFT*0.5 + UP*1),
            fin_bollard[1].animate.set_fill(YELLOW, opacity=1).set_stroke(color=YELLOW), # Paint post yellow
            run_time=1.0
        )
        self.play(FadeOut(brush))

        bullets_finish = create_bullets("Hot dip galvanizing for corrosion resistance", "Powder coat and paint for protection and visibility")
        self.play(FadeIn(bullets_finish))
        self.wait(8.0) # Hold for narration part 4
        self.play(FadeOut(bullets_finish))

        # PHASE 6 - Wrap up
        self.play(
            finish_node[0].animate.scale(1/1.5).set_color(WHITE),
            nodes.animate.set_opacity(1),
            run_time=0.5
        )
        
        # Add checkmarks to all nodes
        checks = VGroup()
        for node in nodes:
            c = Text("✓", color=GREEN, font_size=24).next_to(node[0], DOWN, buff=0.1)
            checks.add(c)
        self.play(FadeIn(checks))

        summary = Text("From sketch to finished steel bollard ready for installation", font_size=28, color=WHITE)
        summary.set_stroke(color=BLACK, width=1.5)
        summary.to_edge(DOWN, buff=1.0)
        
        self.play(FadeIn(summary))
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(pipeline),
            FadeOut(fin_bollard),
            FadeOut(checks),
            FadeOut(summary),
            run_time=1.0
        )
        self.wait(0.5)
