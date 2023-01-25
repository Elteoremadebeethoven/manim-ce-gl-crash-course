from manimlib import *

class _01(Scene):
  def construct(self):
    self.add(
      Square(fill_opacity=1)
        .set_color(RED) # RED_C === RED
        .scale(3)
    )
    self.wait()

COLORS = [
  "#F00",
  "#FF0000",
  "#0F0",
  "#00F",
  "#FF0",
  "#0FF",
]

class _02(Scene):
  def construct(self):
    self.add(
      Square(
        fill_opacity=0.3,   # 30 % opacity
        fill_color=TEAL,
        stroke_opacity=0.6, # 60 % opacity
        stroke_color=RED,
        stroke_width=10 # 10% of camera unit === 0.1 camera unit
      )
        .scale(3)
    )
    self.wait()


class _03(Scene):
  def construct(self):
    self.add(
      Square().scale(3)
        # .set_color(RED)
        # .set_stroke(TEAL, 10, 0.5)
        # .set_fill(ORANGE, 0.1)
        # .set_opacity(0.5)
        # .set_style(
        #   fill_opacity=0.3,
        #   fill_color=TEAL,
        #   stroke_opacity=0.6,
        #   stroke_color=RED,
        #   stroke_width=10 
        # )
        # .match_style(Triangle(fill_opacity=1, fill_color=PINK))
    )
    self.wait()

# ManimGL uses * quadratic * bezier curves
# instead of * cubic * curves as in ManimCE

class _04(Scene):
  def construct(self):
    #             start,   handle,      end,
    coords = [ (-3,  1), ( 0,  3), ( 3,  1), 
               (-3, -1), ( 0, -3), ( 3, -1) ]
    dots = [ Dot([*coord,0]) for coord in coords ]
    xyz_coords = [ dot.get_center() for dot in dots ]
    coords_text = [
      Text(f"({x},{y})", font="Times")
        .next_to([x,y,0], np.sign(y)*UP)
      for x,y in coords
    ]

    vmob = VMobject(color=RED) # cannot use .set_points(...) here
    vmob.set_points(xyz_coords)
    # vmob_as_corners = VMobject(color=TEAL)
    # vmob_as_corners.set_points_as_corners(xyz_coords)
    # vmob_smoothly = VMobject(color=PURPLE)
    # vmob_smoothly.set_points_smoothly(xyz_coords)

    self.add(
      NumberPlane(), *dots,
      vmob,
      # vmob_as_corners,
      # vmob_smoothly,
      *coords_text
    )
    self.wait()


class _05(Scene):
  def construct(self):
    coords = [ (-3,  1), ( 0,  3), ( 3,  1)  ]
    vmob = VMobject()
    vmob.set_points([ (x,y,0)
                      for x,y in coords ])

    start_dot = Dot(vmob.get_start(), color=RED)
    end_dot = Dot(vmob.get_end(), color=BLUE)

    self.add(vmob, start_dot, end_dot)
    self.wait()


class _06(Scene):
  def construct(self):
    vmob = Circle().scale(3.4)
    # vmob.data["points"][0] += LEFT
    control_points = vmob.get_all_points()

    dots = [ Dot(point)
             for point in control_points ]

    self.add(vmob, *dots)
    self.wait()
