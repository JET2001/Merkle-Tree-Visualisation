from manim import *

class Tute1(Scene):
    def construct(self):
       axes = Axes(x_range = [0,5,1], y_range = [0,3,1], x_length = 5, y_length = 3, axis_config = {"include_tip": True, "numbers_to_exclude": [0]}).add_coordinates()
       
       axes.to_edge(UR)
       axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")
       func_name = MathTex("f(x) = \\sqrt{x}")
       
       graph = axes.plot(lambda x: x**0.5, x_range = [0,4], color = YELLOW)

       func_name.move_to(graph.get_bottom())
       func_name.add_updater(lambda x: x.move_to(graph.get_bottom()))

       ### Plot is the updated get_graph function

       ## create a group of items, and move them 
       graphing_stuff = VGroup(axes, graph, axis_labels, func_name)
       
       ## Play the animation
       self.play(DrawBorderThenFill(axes), Write(axis_labels), run_time = 2)
       self.wait()
       self.play(Create(graph), Write(func_name))
       self.wait()
       self.play(graphing_stuff.animate.shift(DOWN*4), run_time = 3)
       self.play(axes.animate.shift(LEFT*3), run_time = 3)
       self.wait()
