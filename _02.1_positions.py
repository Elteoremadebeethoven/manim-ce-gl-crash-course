from manimlib import *

"""
                            ┌───▶mob.move_to(mob|vector)                          
                            │                                                     
            ┌───▶Absolute───┼───▶mob.to_edge(unit-vector, buff)                   
            │               │                                                     
            │               └───▶mob.to_corner(corner-vector, buff)               
Positions───┤                                                                     
            │               ┌───▶mob.shift(vector)                                
            │               │                                                     
            └───▶Relative───┼───▶mob.next_to(mob|vec, vec, buff, unit-vector)     
                            │                                                     
                            └───▶mob.align_to(mob|vec, unit-vector)   
"""

class _01(Scene):
    def construct(self):
        number_plane = NumberPlane()
        self.add(number_plane)


class _02(Scene):
    def construct(self):
        number_plane = NumberPlane()

        dot = Dot().move_to([-1,1,0])

        self.add(number_plane)
        self.add(dot)

"""
ORIGIN = np.array([ 0, 0, 0])
UP    = np.array([ 0, 1, 0])
DOWN  = np.array([ 0,-1, 0])
RIGHT = np.array([ 1, 0, 0])
LEFT  = np.array([-1, 0, 0])
OUT   = np.array([ 0, 0, 1])
IN    = np.array([ 0, 0,-1])
UR = UP   + RIGHT = np.array([ 1, 1, 0])
DR = DOWN + RIGHT = np.array([ 1,-1, 0])
UL = UP   + LEFT  = np.array([-1, 1, 0])
DL = DOWN + LEFT  = np.array([-1, 1, 0])
"""

class _03(Scene):
    def construct(self):
        number_plane = NumberPlane()

        dot = Dot().move_to(2 * RIGHT + 3 * DOWN)

        self.add(number_plane, dot)


class _04(Scene):
    def construct(self):
        number_plane = NumberPlane()

        dot = Dot()
        dot.move_to(2 * RIGHT + 3 * DOWN)
        dot.move_to(2 * RIGHT + 3 * DOWN)
        dot.move_to(2 * RIGHT + 3 * DOWN)

        self.add(number_plane, dot)


class _05(Scene):
    def construct(self):
        number_plane = NumberPlane()

        sq = Square().move_to(UP * 2 + RIGHT * 2)
        dot = Dot().move_to(sq)

        self.add(number_plane, sq, dot)


class _06(Scene):
    def construct(self):
        number_plane = NumberPlane()

        sq = Square().move_to(UP * 2 + RIGHT * 2)
        dot = Dot().move_to(sq.get_center() + RIGHT * 2)

        self.add(number_plane, sq, dot)


class _07(Scene):
    def construct(self):
        number_plane = NumberPlane()

        sq = Square().move_to(UP * 2 + RIGHT * 2)
        dot = Dot().move_to(sq.get_right())

        self.add(number_plane, sq, dot)


class _08(Scene):
    def construct(self):
        number_plane = NumberPlane()

        c = Circle().move_to(UP * 1 + RIGHT * 3)
        # c.to_edge(UP)

        self.add(number_plane, c)


class _09(Scene):
    def construct(self):
        number_plane = NumberPlane()

        c = Circle().move_to(UP * 1 + RIGHT * 3)
        c.to_edge(UP, buff=0) # buff(er) = gap between edges

        self.add(number_plane, c)


class _10(Scene):
    def construct(self):
        number_plane = NumberPlane()
        # buff can also be negative
        c = Circle().to_edge(UR, buff=0)

        self.add(number_plane, c)


class _11(Scene):
    def construct(self):
        number_plane = NumberPlane()
        # Unlike .move_to(vec), .shift(vec) multiple times
        # is different from shifting just once.
        c = Circle().move_to(RIGHT+UP)
        # c.shift(RIGHT)
        # c.shift(RIGHT)
        # c.shift(RIGHT)

        self.add(number_plane, c)


class _12(Scene):
    def construct(self):
        number_plane = NumberPlane()

        s = Square().move_to(RIGHT * 2 + UP * 2)
        c = Circle().next_to(s, DOWN)

        self.add(number_plane, s, c)


class _13(Scene):
    def construct(self):
        number_plane = NumberPlane()

        s = Square().move_to(RIGHT * 2 + UP * 2)
        c = Circle().next_to(s, DOWN, buff=0)

        self.add(number_plane, s, c)


class _14(Scene):
    def construct(self):
        number_plane = NumberPlane()

        s = Square().move_to(RIGHT * 2 + UP * 2)
        t = Text("A").next_to(s, DOWN, aligned_edge=ORIGIN)

        self.add(number_plane, s, t)


class _15(Scene):
    def construct(self):
        number_plane = NumberPlane()

        s = Square().move_to(RIGHT * 2 + UP * 2)
        t = Text("A").next_to(s, DOWN)

        # t.align_to(s, RIGHT)

        self.add(number_plane, s, t)
