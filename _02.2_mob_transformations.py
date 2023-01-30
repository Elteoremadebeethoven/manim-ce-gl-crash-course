from manimlib import *

"""
                                     ┌───▶mob.set() | MCE                         
                                     │                                            
                                     ├───▶mob.set_width() | MGL                   
                                     │                                            
                                     ├───▶mob.set_height() | MGL                  
                                     │                                            
                                     ├───▶mob.scale_to_fit_width() | MCE          
                    ┌────▶Without ───┤                                            
                    │     stretch    ├───▶mob.scale_to_fit_height() | MCE         
                    │                │                                            
                    │                ├───▶mob.match_width() | MCE-MGL             
                    │                │                                            
                    │                ├───▶mob.match_height() | MCE-MGL            
                    │                │                                            
Transformations─────┤                └───▶mob.scale() | MCE-MGL                   
                    │                                                             
                    │               ┌────▶mob.stretch_to_fit_width() | MCE-MGL    
                    ├────▶With ─────┤                                             
                    │     stretch   └────▶mob.stretch_to_fit_height() | MCE-MGL   
                    │                                                             
                    │                 ┌──▶mob.rotate() | MCE-MGL                  
                    ├────▶Rotations───┤                                           
                    │                 └──▶mob.flip() | MCE-MGL                    
                    │                                                             
                    └────▶Specific───────▶mob.apply_matrix() | MCE-MGL            
        
"""

"""
__        ___ _   _                 _         _            _       _     
\ \      / (_) |_| |__   ___  _   _| |_   ___| |_ _ __ ___| |_ ___| |__  
 \ \ /\ / /| | __| '_ \ / _ \| | | | __| / __| __| '__/ _ \ __/ __| '_ \ 
  \ V  V / | | |_| | | | (_) | |_| | |_  \__ \ |_| | |  __/ || (__| | | |
   \_/\_/  |_|\__|_| |_|\___/ \__,_|\__| |___/\__|_|  \___|\__\___|_| |_|
"""

class _01(Scene):
    def construct(self):
        mob = Square()

        mob.set_width(4)
        # mob.set_height(6)

        self.add(NumberPlane(), mob)


class _02(Scene):
    def construct(self):
        mob = Square()
        t = Text("2")

        # t.match_width(mob)
        # t.match_height(mob)

        self.add(NumberPlane(), mob, t)


class _03(Scene):
    def construct(self):
        mob = Square()

        mob.scale(1)
        # mob.scale(2)
        # mob.scale(3)
        # mob.scale(0.5)

        self.add(NumberPlane(), mob)

"""
__        ___ _   _           _            _       _     
\ \      / (_) |_| |__    ___| |_ _ __ ___| |_ ___| |__  
 \ \ /\ / /| | __| '_ \  / __| __| '__/ _ \ __/ __| '_ \ 
  \ V  V / | | |_| | | | \__ \ |_| | |  __/ || (__| | | |
   \_/\_/  |_|\__|_| |_| |___/\__|_|  \___|\__\___|_| |_|
"""


class _04(Scene):
    def construct(self):
        mob = Square()
        
        # mob.stretch_to_fit_height(4)
        # mob.stretch_to_fit_width(4)

        self.add(NumberPlane(), mob)


class _05(Scene):
    def construct(self):
        mob = Square()
        t = Text("2")

        # t.match_width(mob, stretch=True)
        # t.match_height(mob, stretch=True)

        self.add(NumberPlane(), mob, t)

"""
__        ___ _   _       ____       _        _   _                 
\ \      / (_) |_| |__   |  _ \ ___ | |_ __ _| |_(_) ___  _ __  ___ 
 \ \ /\ / /| | __| '_ \  | |_) / _ \| __/ _` | __| |/ _ \| '_ \/ __|
  \ V  V / | | |_| | | | |  _ < (_) | || (_| | |_| | (_) | | | \__ \
   \_/\_/  |_|\__|_| |_| |_| \_\___/ \__\__,_|\__|_|\___/|_| |_|___/
"""

class _06(Scene):
    def construct(self):
        mob = Square().scale(2)

        # mob.rotate(PI/4)
        # mob.rotate(45 * DEGREES)

        self.add(NumberPlane(), mob)

# The Star class is not defined, so I passed the
# code from ManimCE to ManimGL here ========================
def regular_vertices(n, *, radius = 1, start_angle = None):
    if start_angle is None:
        if n % 2 == 0:
            start_angle = 0
        else:
            start_angle = TAU / 4

    start_vector = rotate_vector(RIGHT * radius, start_angle)
    vertices = compass_directions(n, start_vector)

    return vertices, start_angle

class Star(Polygon):
    def __init__(
        self,
        n = 5,
        *,
        outer_radius = 1,
        inner_radius = None,
        density = 2,
        start_angle = TAU / 4,
        **kwargs,
    ):
        inner_angle = TAU / (2 * n)
        if inner_radius is None:
            if density <= 0 or density >= n / 2:
                raise ValueError(
                    f"Incompatible density {density} for number of points {n}",
                )
            outer_angle = TAU * density / n
            inverse_x = 1 - np.tan(inner_angle) * (
                (np.cos(outer_angle) - 1) / np.sin(outer_angle)
            )
            inner_radius = outer_radius / (np.cos(inner_angle) * inverse_x)

        outer_vertices, self.start_angle = regular_vertices(
            n,
            radius=outer_radius,
            start_angle=start_angle,
        )
        inner_vertices, _ = regular_vertices(
            n,
            radius=inner_radius,
            start_angle=self.start_angle + inner_angle,
        )
        vertices = []
        for pair in zip(outer_vertices, inner_vertices):
            vertices.extend(pair)
        super().__init__(*vertices, **kwargs)
# =====================================================

class _07(Scene):
    def construct(self):
        mob = Star().scale(3)

        dot1 = Dot(mob.get_center()) # same as Dot1().move_to(mob1)
        dot2 = Dot(mob.get_center_of_mass(), color=RED)

        self.add(NumberPlane(), mob, dot1, dot2)


class _08(Scene):
    def construct(self):
        mob1 = Star().scale(3)
        mob2 = Star(color=RED).scale(3)

        mob1.rotate(PI/4)
        # same as:
        # mob1.rotate(PI/4, about_point=mob1.get_center())
        mob2.rotate(PI/4, about_point=mob2.get_center_of_mass())

        self.add(NumberPlane(), mob1, mob2)


class _09(Scene):
    def construct(self):
        mob = Text("A").shift(DOWN*3)

        # mob.rotate(45*DEGREES, about_point=ORIGIN)    

        self.add(NumberPlane(), mob)

"""
 ____                  _  __ _      
/ ___| _ __   ___  ___(_)/ _(_) ___ 
\___ \| '_ \ / _ \/ __| | |_| |/ __|
 ___) | |_) |  __/ (__| |  _| | (__ 
|____/| .__/ \___|\___|_|_| |_|\___|
      |_|                           
"""

class _10(Scene):
    def construct(self):
        mob1 = Square(color=TEAL).scale(3)
        mob2 = Square(color=YELLOW).scale(3)

        ref1 = Dot()
        ref2 = Dot(mob1.get_corner(DL), color=RED)

        P = np.tan(30 * DEGREES)

        matrix = [
            [1, P, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]

        mob1.apply_matrix(matrix, about_point=ref1.get_center())
        mob2.apply_matrix(matrix, about_point=ref2.get_center())

        self.add(NumberPlane(), mob1, mob2, ref1, ref2)


# ========================================================
if __name__ == '__main__':
    from dotenv import load_dotenv
    from os import getenv
    load_dotenv()
    # ---
    SCENE = getenv("RENDER_SCENE")
    RENDER_OPTIONS = getenv("RENDER_OPTIONS")
    OUTPUT_NAME = getenv("OUTPUT_NAME")
    FLAGS = f"-{RENDER_OPTIONS} --file_name {OUTPUT_NAME}"
    if eval(getenv("PROGRESS_BARS")):
        FLAGS += " --leave_progress_bars"
    if getenv("FPS"):
        FLAGS += f" --frame_rate {getenv('FPS')}"
    if getenv("START_AT"):
        FLAGS += f" -n {getenv('START_AT')}"
    # ---
    script_name = f"{Path(__file__).resolve()}"
    COMMAND = f"manimgl {script_name} {SCENE} {FLAGS}"
    print(f"CMD:\033[1m manimgl \033[96m{script_name} \033[93m{SCENE} \033[94m{FLAGS}")
    os.system(COMMAND)
