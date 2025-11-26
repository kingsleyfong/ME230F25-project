from manim import *

# Set default font to Segoe UI with BOLD weight for better visibility
Text.set_default(font="Segoe UI", weight="BOLD")

class SteelManufacturingScene(Scene):
    def construct(self):
        # Global settings
        self.camera.background_color = "#050505"
        
        # Style constants
        TEXT_STROKE_WIDTH = 0 
        TEXT_COLOR = WHITE
        GEO_COLOR = WHITE
        HIGHLIGHT_COLOR = "#00FFFF" # Cyan

        # ----------------------------------------------------------
        # PHASE 1 – Title
        # ----------------------------------------------------------
        # Reduced buff to 0.2 to save vertical space
        title = Text("Typical manufacturing of steel bollards", font_size=48, color=TEXT_COLOR)
        title.to_edge(UP, buff=0.2)

        self.play(FadeIn(title, run_time=1.0))

        # ----------------------------------------------------------
        # PHASE 2 – Design phase pipeline
        # ----------------------------------------------------------
        
        def create_design_node(label_text, icon_mob):
            label = Text(label_text, font_size=24, color=TEXT_COLOR)
            
            icon_container = Rectangle(width=1.5, height=1.5, stroke_opacity=0)
            icon_mob.move_to(icon_container.get_center())
            
            group = VGroup(icon_container, icon_mob, label)
            label.next_to(icon_container, DOWN, buff=0.1)
            return group

        # Node 1 Icon: Sketch
        sketch_paper = Rectangle(width=0.8, height=1.0, color=GEO_COLOR)
        sketch_bollard = VGroup(
            Line(DOWN*0.3, UP*0.3, color=GEO_COLOR),
            Circle(radius=0.1, color=GEO_COLOR).move_to(UP*0.3)
        )
        sketch_icon = VGroup(sketch_paper, sketch_bollard)
        node1 = create_design_node("Rough sketches", sketch_icon)

        # Node 2 Icon: 3D CAD
        cad_cyl = Rectangle(width=0.4, height=0.8, color=GEO_COLOR)
        cad_top = Ellipse(width=0.4, height=0.15, color=GEO_COLOR).move_to(cad_cyl.get_top())
        cad_bottom = Ellipse(width=0.4, height=0.15, color=GEO_COLOR).move_to(cad_cyl.get_bottom())
        cad_icon = VGroup(cad_cyl, cad_top, cad_bottom)
        node2 = create_design_node("3D CAD model", cad_icon)

        # Node 3 Icon: Impact Test
        test_bollard = Line(DOWN*0.4, UP*0.4, stroke_width=4, color=GEO_COLOR)
        test_car = VGroup(
            RoundedRectangle(corner_radius=0.1, width=0.6, height=0.3, color=GEO_COLOR),
            Circle(radius=0.1, color=GEO_COLOR).shift(LEFT*0.2 + DOWN*0.15),
            Circle(radius=0.1, color=GEO_COLOR).shift(RIGHT*0.2 + DOWN*0.15)
        ).scale(0.6).next_to(test_bollard, LEFT, buff=0.3)
        test_arrow = Arrow(start=test_car.get_right(), end=test_bollard.get_left(), buff=0.05, max_tip_length_to_length_ratio=0.4, color=GEO_COLOR).scale(0.5)
        test_icon = VGroup(test_bollard, test_car, test_arrow)
        node3 = create_design_node("Prototype impact testing", test_icon)

        # Arrange Nodes
        # Moved UP to 2.4 to avoid title overlap and clear space below
        design_row = VGroup(node1, node2, node3).arrange(RIGHT, buff=2.0)
        design_row.move_to(UP * 2.4)

        # Arrows between nodes
        arrow1 = Arrow(start=node1.get_right(), end=node2.get_left(), buff=0.2, color=GEO_COLOR, stroke_width=2)
        arrow2 = Arrow(start=node2.get_right(), end=node3.get_left(), buff=0.2, color=GEO_COLOR, stroke_width=2)

        # Animation sequence
        self.play(FadeIn(node1))
        self.play(Create(arrow1))
        self.play(FadeIn(node2))
        self.play(Create(arrow2))
        self.play(FadeIn(node3))
        
        self.wait(0.5)

        # ----------------------------------------------------------
        # PHASE 3 – Manufacturing and assembly pipeline
        # ----------------------------------------------------------

        def create_manuf_panel(header_text, icon_mob):
            w, h = 3.0, 2.2 
            panel = RoundedRectangle(corner_radius=0.2, width=w, height=h, color=GEO_COLOR)
            header = Text(header_text, font_size=20, color=TEXT_COLOR)
            header.next_to(panel.get_top(), DOWN, buff=0.2)
            icon_mob.move_to(panel.get_center() + DOWN*0.2)
            return VGroup(panel, header, icon_mob)

        # Step 1: Raw Material
        raw_cyl = Rectangle(width=1.2, height=0.4, color=GEO_COLOR)
        raw_end1 = Ellipse(width=0.2, height=0.4, color=GEO_COLOR).move_to(raw_cyl.get_left())
        raw_end2 = Ellipse(width=0.2, height=0.4, color=GEO_COLOR).move_to(raw_cyl.get_right())
        step1_icon = VGroup(raw_cyl, raw_end1, raw_end2)
        panel1 = create_manuf_panel("Steel pipe as raw material", step1_icon)

        # Step 2: Machine base/cap
        base_plate = Rectangle(width=1.0, height=0.15, color=GEO_COLOR)
        cap_circle = Circle(radius=0.25, color=GEO_COLOR).next_to(base_plate, UP, buff=0.2)
        gear = VGroup()
        gear_body = Circle(radius=0.15, color=GEO_COLOR)
        for i in range(8):
            tooth = Rectangle(width=0.05, height=0.4, color=GEO_COLOR)
            tooth.rotate(i * PI / 4)
            gear.add(tooth)
        gear.add(gear_body)
        gear.scale(0.5).move_to(cap_circle.get_right() + RIGHT*0.3 + UP*0.1)
        step2_icon = VGroup(base_plate, cap_circle, gear)
        panel2 = create_manuf_panel("Machine base and cap", step2_icon)

        # Step 3: MIG Weld
        weld_base = Rectangle(width=0.8, height=0.1, color=GEO_COLOR)
        weld_pipe = Rectangle(width=0.3, height=0.8, color=GEO_COLOR).next_to(weld_base, UP, buff=0)
        torch = Triangle(color=GEO_COLOR).scale(0.15).rotate(135*DEGREES).move_to(weld_pipe.get_bottom() + RIGHT*0.3)
        spark = VGroup(*[Line(ORIGIN, UP*0.1, color="#FFFF00").rotate(angle) for angle in [0, 45*DEGREES, 90*DEGREES, -45*DEGREES]])
        spark.move_to(weld_pipe.get_bottom() + RIGHT*0.15).scale(0.5)
        step3_icon = VGroup(weld_base, weld_pipe, torch, spark)
        panel3 = create_manuf_panel("MIG weld components", step3_icon)

        # Step 4: Quality Inspection
        insp_bollard = Rectangle(width=0.2, height=0.8, color=GEO_COLOR)
        check = VGroup(
            Line(UP*0.1+LEFT*0.1, DOWN*0.1, color=GEO_COLOR),
            Line(DOWN*0.1, UP*0.2+RIGHT*0.2, color=GEO_COLOR)
        ).next_to(insp_bollard, RIGHT, buff=0.2)
        step4_icon = VGroup(insp_bollard, check)
        panel4 = create_manuf_panel("Quality inspection", step4_icon)

        # Assemble Manufacturing Line
        manuf_group = VGroup(panel1, panel2, panel3, panel4).arrange(RIGHT, buff=0.5)
        
        # MOVED UP: Shifted to UP*0.3 to create gap below
        manuf_group.move_to(UP * 0.3) 

        # Arrows between panels
        m_arrows = VGroup()
        for i in range(3):
            arr = Arrow(
                start=manuf_group[i].get_right(), 
                end=manuf_group[i+1].get_left(), 
                buff=0.1, 
                color=GEO_COLOR, 
                max_tip_length_to_length_ratio=0.5
            )
            m_arrows.add(arr)

        # Animation: Slide in
        self.play(
            FadeIn(manuf_group, shift=UP*0.5),
            run_time=1.5
        )

        # Animation: Process flow
        panels = [panel1, panel2, panel3, panel4]
        for i, panel in enumerate(panels):
            self.play(panel[0].animate.set_stroke(color=HIGHLIGHT_COLOR, width=3), run_time=0.5)
            self.play(panel[0].animate.set_stroke(color=GEO_COLOR, width=1), run_time=0.5)
            if i < 3:
                self.play(Create(m_arrows[i]), run_time=0.3)

        self.wait(0.5)

        # ----------------------------------------------------------
        # PHASE 4 – Surface treatment and visibility
        # ----------------------------------------------------------
        
        st_header = Text("Surface protection and visibility", font_size=28, color=TEXT_COLOR)
        
        def create_treatment_item(label_text, icon_mob):
            lbl = Text(label_text, font_size=22, color=TEXT_COLOR)
            icon_mob.scale(0.5)
            grp = VGroup(icon_mob, lbl).arrange(RIGHT, buff=0.2)
            return grp

        # T1: Galvanized
        t1_tank = Rectangle(width=1.0, height=0.6, color=GEO_COLOR)
        t1_liq = Line(t1_tank.get_left(), t1_tank.get_right(), color=GEO_COLOR).shift(DOWN*0.1)
        t1_bol = Line(UP*0.3, DOWN*0.1, stroke_width=4, color=GEO_COLOR).move_to(t1_tank.get_center())
        t1_icon = VGroup(t1_tank, t1_liq, t1_bol)
        t1_item = create_treatment_item("Galvanized for corrosion resistance", t1_icon)

        # T2: Powder coated
        t2_bol = Line(DOWN*0.3, UP*0.3, stroke_width=4, color=GEO_COLOR)
        t2_noz = Triangle(color=GEO_COLOR).scale(0.1).rotate(-90*DEGREES).next_to(t2_bol, LEFT, buff=0.2)
        t2_spray = Circle(radius=0.1, stroke_opacity=0, fill_color=WHITE, fill_opacity=0.5).next_to(t2_noz, RIGHT, buff=0)
        t2_icon = VGroup(t2_bol, t2_noz, t2_spray)
        t2_item = create_treatment_item("Powder coated for durability", t2_icon)

        # T3: Bright paint
        t3_bol = Rectangle(width=0.1, height=0.6, color=GEO_COLOR)
        t3_band = Rectangle(width=0.12, height=0.1, color=HIGHLIGHT_COLOR, fill_opacity=1).move_to(t3_bol.get_top() + DOWN*0.1)
        t3_icon = VGroup(t3_bol, t3_band)
        t3_item = create_treatment_item("Bright paint for visibility", t3_icon)

        treatments_list = VGroup(t1_item, t2_item, t3_item).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Central Evolving Bollard (REDUCED HEIGHT to fit frame)
        evolve_bollard_body = RoundedRectangle(corner_radius=0.1, width=0.8, height=1.8, color=GEO_COLOR)
        evolve_bollard = VGroup(evolve_bollard_body).set_stroke(width=2)
        
        content_group = VGroup(treatments_list, evolve_bollard).arrange(RIGHT, buff=1.5)
        phase4_group = VGroup(st_header, content_group).arrange(DOWN, buff=0.4)
        
        # MOVED DOWN: Shifted further down to 2.6
        phase4_group.move_to(DOWN * 2.6)

        # Animations Phase 4
        self.play(FadeIn(st_header))
        
        # Step 1
        self.play(FadeIn(t1_item), FadeIn(evolve_bollard))
        self.play(
            t1_item.animate.set_color(HIGHLIGHT_COLOR),
            evolve_bollard.animate.set_stroke(color=GREY_B, width=3), 
            run_time=1.0
        )
        self.play(t1_item.animate.set_color(WHITE))

        # Step 2
        self.play(FadeIn(t2_item))
        self.play(
            t2_item.animate.set_color(HIGHLIGHT_COLOR),
            evolve_bollard.animate.set_fill(color="#333333", opacity=1).set_stroke(color=WHITE, width=4),
            run_time=1.0
        )
        self.play(t2_item.animate.set_color(WHITE))

        # Step 3
        # Add bright band
        bright_band = Rectangle(width=0.82, height=0.4, color=HIGHLIGHT_COLOR, fill_opacity=1)
        # Adjust position based on new height
        bright_band.move_to(evolve_bollard.get_top() + DOWN*0.3)
        
        self.play(FadeIn(t3_item))
        self.play(
            t3_item.animate.set_color(HIGHLIGHT_COLOR),
            FadeIn(bright_band),
            run_time=1.0
        )
        self.play(t3_item.animate.set_color(WHITE))

        final_bollard_group = VGroup(evolve_bollard, bright_band)
        self.wait(2.0)

        # ----------------------------------------------------------
        # PHASE 5 – Exit
        # ----------------------------------------------------------
        self.play(
            FadeOut(phase4_group),
            FadeOut(final_bollard_group), 
            run_time=1.0
        )
        self.play(
            FadeOut(manuf_group),
            FadeOut(m_arrows),
            run_time=1.0
        )
        self.play(
            FadeOut(design_row),
            FadeOut(arrow1),
            FadeOut(arrow2),
            run_time=1.0
        )
        self.play(FadeOut(title), run_time=1.0)
        
        self.wait(0.3)