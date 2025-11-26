# File: src/scenes/scenario_scene.py

from manim import *

Text.set_default(font="Segoe UI")

# Define cyan highlight color
CYAN = "#00CED1"

class ScenarioScene(Scene):
    def construct(self):
        # ------------------------------------------------------------
        # PHASE 1 - Title and environment
        # ------------------------------------------------------------
        
        # Title at top center
        title = Text("Scenario - K4 security bollard", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        title.scale(0.8)
        title.to_edge(UP, buff=0.5)
        
        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)
        
        # Ground line slightly below center
        ground_line = Line(LEFT * 7, RIGHT * 7, color=WHITE, stroke_width=2)
        ground_line.shift(DOWN * 1.5)
        
        self.play(Create(ground_line, run_time=0.8))
        self.wait(0.3)
        
        # Road region (left side) - darker band above ground
        road_region = Rectangle(width=5, height=0.4, color=GRAY, fill_opacity=0.3, stroke_width=0)
        road_region.next_to(ground_line, UP, buff=0)
        road_region.shift(LEFT * 2.5)
        
        road_label = Text("Busy road", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        road_label.scale(0.4)
        road_label.next_to(road_region, UP, buff=0.2)
        road_label.shift(LEFT * 1)
        
        # Public building (right side)
        building = Rectangle(width=2, height=4, color=WHITE, stroke_width=2, fill_opacity=0.1)
        building.next_to(ground_line, UP, buff=0)
        building.shift(RIGHT * 3.5)
        
        building_label = Text("Public building", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        building_label.scale(0.4)
        building_label.next_to(building, UP, buff=0.2)
        
        self.play(FadeIn(building, run_time=0.8))
        self.wait(0.2)
        self.play(FadeIn(road_region), FadeIn(road_label, run_time=0.8))
        self.wait(0.3)
        
        # Bollard - vertical cylinder at boundary
        bollard_body = Rectangle(width=0.275, height=0.9, color=WHITE, stroke_width=2, fill_opacity=0.15)
        bollard_body.next_to(ground_line, UP, buff=0)
        bollard_body.shift(RIGHT * 0.5)
        
        bollard_top = Arc(radius=0.275/2, angle=PI, color=CYAN, stroke_width=3)
        bollard_top.move_to(bollard_body.get_top())
        bollard_top.shift(UP * 0.01)
        
        bollard = VGroup(bollard_body, bollard_top)
        
        self.play(FadeIn(bollard, run_time=0.8))
        self.wait(0.3)
        
        # Vehicle (left) - simple van shape
        vehicle_body = Rectangle(width=1.5, height=0.8, color=WHITE, stroke_width=2, fill_opacity=0.2)
        vehicle_roof = Rectangle(width=0.7, height=0.3, color=WHITE, stroke_width=2, fill_opacity=0.2)
        vehicle_roof.next_to(vehicle_body, UP, buff=0)
        vehicle_roof.shift(LEFT * 0.2)
        
        wheel1 = Circle(radius=0.15, color=WHITE, stroke_width=2, fill_opacity=0.3)
        wheel2 = Circle(radius=0.15, color=WHITE, stroke_width=2, fill_opacity=0.3)
        wheel1.next_to(vehicle_body, DOWN, buff=0)
        wheel1.shift(LEFT * 0.4)
        wheel2.next_to(vehicle_body, DOWN, buff=0)
        wheel2.shift(RIGHT * 0.4)
        
        vehicle = VGroup(vehicle_body, vehicle_roof, wheel1, wheel2)
        vehicle.next_to(ground_line, UP, buff=0)
        vehicle.shift(LEFT * 6)
        
        # Slide vehicle in from left
        self.play(FadeIn(vehicle, run_time=0.5))
        self.wait(0.2)
        self.play(vehicle.animate.shift(RIGHT * 3.5), run_time=2.0, rate_func=smooth)
        self.wait(0.5)
        
        # ------------------------------------------------------------
        # PHASE 2 - K4 load parameters
        # ------------------------------------------------------------
        
        # Cyan arrow from vehicle to bollard at bumper height
        arrow_start = vehicle_body.get_right() + UP * 0.1
        arrow_end = bollard_body.get_left() + UP * 0.45
        
        impact_arrow = Arrow(arrow_start, arrow_end, color=CYAN, stroke_width=4, buff=0.1)
        
        self.play(GrowArrow(impact_arrow, run_time=0.8))
        self.wait(0.3)
        
        # K4 parameters panel
        param_text1 = Text("Vehicle mass m = 2000 kg", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        param_text1.scale(0.35)
        
        param_text2 = Text("Speed v = 57 km/h", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        param_text2.scale(0.35)
        
        param_text3 = Text("Impact energy ≈ 250 kJ", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        param_text3.scale(0.35)
        
        param_text4 = Text("Equivalent force ≈ 6267 kN", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        param_text4.scale(0.35)
        
        param_group = VGroup(param_text1, param_text2, param_text3, param_text4)
        param_group.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        panel_bg = RoundedRectangle(
            width=param_group.width + 0.4,
            height=param_group.height + 0.3,
            corner_radius=0.1,
            color=GRAY,
            fill_opacity=0.2,
            stroke_width=1
        )
        panel_bg.move_to(param_group.get_center())
        
        param_group.move_to(impact_arrow.get_center() + UP * 1.2 + LEFT * 0.5)
        panel_bg.move_to(param_group.get_center())
        
        self.play(FadeIn(panel_bg, run_time=0.5))
        self.wait(0.2)
        self.play(FadeIn(param_text1, run_time=0.6))
        self.wait(0.4)
        self.play(FadeIn(param_text2, run_time=0.6))
        self.wait(0.4)
        self.play(FadeIn(param_text3, run_time=0.6))
        self.wait(0.4)
        self.play(FadeIn(param_text4, run_time=0.6))
        self.wait(1.2)
        
        # ------------------------------------------------------------
        # PHASE 3 - Geometry and free variable thickness
        # ------------------------------------------------------------
        
        # Fade K4 panel slightly
        self.play(panel_bg.animate.set_opacity(0.1), param_group.animate.set_opacity(0.5), run_time=0.5)
        self.wait(0.3)
        
        # Bollard height dimension
        height_brace = Brace(bollard_body, direction=LEFT, color=CYAN)
        height_label = Text("h = 0.9 m", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        height_label.scale(0.35)
        height_label.next_to(height_brace, LEFT, buff=0.1)
        
        self.play(FadeIn(height_brace), FadeIn(height_label, run_time=0.8))
        self.wait(0.5)
        
        # Bollard diameter dimension
        diameter_brace = Brace(bollard_body, direction=UP, color=CYAN)
        diameter_label = Text("D = 0.275 m", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        diameter_label.scale(0.35)
        diameter_label.next_to(diameter_brace, UP, buff=0.1)
        
        self.play(FadeIn(diameter_brace), FadeIn(diameter_label, run_time=0.8))
        self.wait(0.5)
        
        # Impact height dimension
        impact_point = bollard_body.get_bottom() + UP * 0.56
        impact_tick = Line(LEFT * 0.15, RIGHT * 0.15, color=CYAN, stroke_width=2)
        impact_tick.move_to(impact_point)
        
        impact_height_line = Line(
            bollard_body.get_bottom() + RIGHT * 0.3,
            impact_point + RIGHT * 0.3,
            color=CYAN,
            stroke_width=2
        )
        impact_height_arrow_down = Arrow(
            impact_height_line.get_start(),
            impact_height_line.get_start() + DOWN * 0.1,
            color=CYAN,
            stroke_width=2,
            buff=0,
            max_tip_length_to_length_ratio=0.3
        )
        impact_height_arrow_up = Arrow(
            impact_height_line.get_end(),
            impact_height_line.get_end() + UP * 0.1,
            color=CYAN,
            stroke_width=2,
            buff=0,
            max_tip_length_to_length_ratio=0.3
        )
        
        impact_height_label = Text("Impact height ≈ 0.56 m (bumper)", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        impact_height_label.scale(0.3)
        impact_height_label.next_to(impact_height_line, RIGHT, buff=0.15)
        
        impact_height_group = VGroup(impact_tick, impact_height_line, impact_height_arrow_down, impact_height_arrow_up, impact_height_label)
        
        self.play(FadeIn(impact_height_group, run_time=0.8))
        self.wait(0.5)
        
        # Thickness cross section
        cross_section_outer = Circle(radius=0.4, color=WHITE, stroke_width=2)
        cross_section_inner = Circle(radius=0.28, color=WHITE, stroke_width=2)
        
        thickness_arrow = DoubleArrow(
            cross_section_inner.point_at_angle(0),
            cross_section_outer.point_at_angle(0),
            color=CYAN,
            stroke_width=2,
            buff=0,
            max_tip_length_to_length_ratio=0.25
        )
        
        thickness_t_label = Text("t", color=CYAN, stroke_color=BLACK, stroke_width=1.5)
        thickness_t_label.scale(0.4)
        thickness_t_label.next_to(thickness_arrow, RIGHT, buff=0.1)
        
        cross_section = VGroup(cross_section_outer, cross_section_inner, thickness_arrow, thickness_t_label)
        cross_section.scale(0.6)
        cross_section.move_to(bollard.get_center() + RIGHT * 2.2 + UP * 0.5)
        
        thickness_label = Text("Thickness t varies with material", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        thickness_label.scale(0.32)
        thickness_label.next_to(cross_section, DOWN, buff=0.3)
        
        self.play(FadeIn(cross_section, run_time=0.8))
        self.wait(0.2)
        self.play(FadeIn(thickness_label, run_time=0.6))
        self.wait(0.5)
        
        # Fixed base and concrete assumption
        base_rect = Rectangle(width=0.5, height=0.15, color=WHITE, stroke_width=2, fill_opacity=0.3)
        base_rect.move_to(bollard_body.get_bottom())
        base_rect.shift(DOWN * 0.075)
        
        bracket_left = Line(UP * 0.1, DOWN * 0.1, color=CYAN, stroke_width=3)
        bracket_left.move_to(base_rect.get_left())
        bracket_left.shift(LEFT * 0.05)
        
        bracket_right = Line(UP * 0.1, DOWN * 0.1, color=CYAN, stroke_width=3)
        bracket_right.move_to(base_rect.get_right())
        bracket_right.shift(RIGHT * 0.05)
        
        concrete_region = Rectangle(width=1.2, height=0.6, color=GRAY, stroke_width=1, fill_opacity=0.15)
        concrete_region.next_to(ground_line, DOWN, buff=0)
        concrete_region.shift(RIGHT * 0.5)
        
        base_text1 = Text("Assume fixed base", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        base_text1.scale(0.28)
        base_text1.next_to(base_rect, DOWN, buff=0.5)
        base_text1.shift(LEFT * 0.8)
        
        base_text2 = Text("Concrete region ignored in analysis", color=WHITE, stroke_color=BLACK, stroke_width=1.5)
        base_text2.scale(0.28)
        base_text2.next_to(base_text1, DOWN, buff=0.1)
        
        base_group = VGroup(base_rect, bracket_left, bracket_right, concrete_region, base_text1, base_text2)
        
        self.play(FadeIn(base_group, run_time=0.8))
        self.wait(2.0)
        
        # ------------------------------------------------------------
        # PHASE 4 - Exit
        # ------------------------------------------------------------
        
        # FadeOut K4 panel and arrow
        self.play(FadeOut(panel_bg), FadeOut(param_group), FadeOut(impact_arrow, run_time=1.0))
        self.wait(0.2)
        
        # FadeOut geometry annotations
        geometry_annotations = VGroup(
            height_brace, height_label,
            diameter_brace, diameter_label,
            impact_height_group,
            cross_section, thickness_label,
            base_group
        )
        self.play(FadeOut(geometry_annotations, run_time=1.0))
        self.wait(0.2)
        
        # FadeOut vehicle and building
        self.play(FadeOut(vehicle), FadeOut(building), FadeOut(building_label, run_time=1.0))
        self.wait(0.2)
        
        # FadeOut bollard and ground
        self.play(FadeOut(bollard), FadeOut(ground_line), FadeOut(road_region), FadeOut(road_label, run_time=1.0))
        self.wait(0.2)
        
        # FadeOut title
        self.play(FadeOut(title, run_time=1.0))
        self.wait(0.3)
