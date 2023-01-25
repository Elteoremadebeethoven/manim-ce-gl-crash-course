# Manim CE/GL fast course

Estimated time to finish it: 1 year

## Syllabus

0. Introduction
	* Requirements
	* How to ask your questions
1. Basic elements
	* How Manim works
	* Introduction to Mobjects and Animations
	* Watchexec with Manim
	* Work environment setup
2. Mobjects/VMobjects Generalities
	* Positioning
	* Transformations
	* VMobject attrs
	* Miscellaneous (V)Mobjects topics
3. Rendering Settings
	* With .cfg files (only ManimCE)
	* With Manim CLI
	* With CONFIG dict (only ManimCE)
	* With `tempconfig` (only ManimCE)
4. Rate functions
5. Layers
6. Import Assets
	* Raster images
	* SVGs
	* Sounds
	* CSV
7. Groups, VGroups and PGroups
	* Submobjects
	* `Group`
	* `VGroup`
	* `PGroup`
8. Text and $\TeX$
	* Text
	* $\TeX$
9. `Transform` animations
	* `Transform`
	* `ReplacementTransform`
	* `TransformFromCopy`
	* `TransformMatchingShapes`
	* `TransformMatchingTex`
	* `MoveToTarget`
	* `ApplyFunction`
10. More useful Mobjects and their methods
	* Code
	* Lines
	* Arcs
	* Braces
	* Polygons
	* NumberLine
	* Tables
	* Matrix
	* Boolean Mobjects
11. 2D plots
	* Cartesian plots
	* Polar plots
12. 3D plots
	* 3D scene
	* 3D axes
	* Plots
13. Basic Updaters
	* Functions as updaters
	* `ValueTracker`
	* `DecimalNumber`
	* `.become` method
	* `always_redraw`
14. `alpha` updaters
	* Allowed `alpha` values
	* `.save_state()` technique
15. Custom animations
	* `__init__` method
	* `_setup_scene`
	* `begin` method
	* With `interpolate_mobject`
	* With `interpolate_submobject`
	* With both
	* `clean_up_from_scene`
16. `dt` updaters
	* Problems with updaters
	* Animations into `dt` updaters
17. Custom Mobjects
18. `AnimationGroup`
	* `lag_ratio`
	* `AnimationGroup`
	* `LaggedStart`
	* With custom animations
29. Moving Camera and Zoom Scenes (ManimCE only)
	* `MovingCameraScene`
	* `ZoomedScene`
20. ImageMobjects in depth
	* Pixel manipulation
	* Pixel interpolation
	* Filters
21. `LinearTransformationScene`
22. Vector fields
23. Interactive scenes

## ► Disclaimer

|                       | Manim Professional Course | ManimCE-GL Fast course |
| :-------------------: | :-----------------------: | :--------------------: |
|        Theory         |             ✅             |           ✅            |
|       Pro-tips        |             ✅             |           ❌            |
|       Examples        |             ✅             |           ❌            |
|       Exercises       |             ✅             |           ❌            |
| ManimGL topics (v1.2) |             ❌             |           ✅            |
|         Free          |             ❌             |           ✅            |

## ► Requirements to take the course:

### Req-0. See if it is really necessary for you to learn Manim, in this video I explain if it is worth it for you.

[![Is it worth learning Manim?](https://img.youtube.com/vi/EONHtYkfCds/0.jpg)](https://www.youtube.com/watch?v=EONHtYkfCds)
(click in the image)

### Req-1. Basic knowledge of the terminal, preferably Bash.

* CMD (Windows): https://www.youtube.com/watch?v=qnXe1gecux
* Bash on Windows with Git Bash: https://www.youtube.com/watch?v=iGutIN5t9Mo
* Terminal for Mac: https://www.youtube.com/watch?v=aKRYQsKR46I

### Req-2. Elementary knowledge of Git, Github and Makefiles, you can learn all this in one day.

* Git and GitHub: https://www.youtube.com/watch?v=tRZGeaHPoaw
* Makefiles (you need to install gcc and make): https://www.youtube.com/watch?v=yWLkyN_Satk

### Req-3. Basic knowledge of programming with Python:

* https://www.youtube.com/watch?v=B9nFMZIYQl0

### Req-4. Basic knowledge of Object Oriented Programming (OOP) with Python:

* https://www.youtube.com/watch?v=Ej_02ICOIgs
* https://www.youtube.com/watch?v=zPFZy6wKhVA

### Req-5. Know the Manim ecosystem and its different versions:

[![manim installation](https://img.youtube.com/vi/1tqtgnawBts/0.jpg)](https://www.youtube.com/watch?v=1tqtgnawBts)
(click in the image)

### Req-6. Install ManimCE and ManimGL:

Although the video is from last year it is still valid.

[![manim installation](https://img.youtube.com/vi/CYOLQk8GpME/0.jpg)](https://www.youtube.com/watch?v=CYOLQk8GpME)
(click in the image)

### Req-7. View the following videos in the order shown.

1.
[![manim installation](https://img.youtube.com/vi/gGU823uEUXU/0.jpg)](https://www.youtube.com/watch?v=gGU823uEUXU)

2.
[![manim installation](https://img.youtube.com/vi/xs_dlmUkWDY/0.jpg)](https://www.youtube.com/watch?v=xs_dlmUkWDY)

3.
[![manim installation](https://img.youtube.com/vi/E5ot6LXcogw/0.jpg)](https://www.youtube.com/watch?v=E5ot6LXcogw)

4. Manim with `watchexec` 

[![manim installation](https://img.youtube.com/vi/pW6tGCCzMMQ/0.jpg)](https://www.youtube.com/watch?v=pW6tGCCzMMQ)

## ► Where to ask questions:

### Rules:

1. Share the code in markdown format, [here's](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) a quick tutorial. Please ***DO NOT*** share code on images.
2. Your question must be accurate, the code should not be longer than ***30 lines***.
3. Format the code so that it is easy to read, it must be in English and indented with descriptive names.

### 1. Discord: https://discord.com/invite/bYCyhM9Kz2

### 2. [Stackoverflow](https://stackoverflow.com): Use the `manim` tag.

### 3. Reddit: https://www.reddit.com/r/manim/

⚠️⚠️⚠️ ***I will not answer questions that are asked in the videos, nor in the issues of this repository*** ⚠️⚠️⚠️

## ► ManimCE setup:

Install ManimCE last version:

```bash
$ mkdir mce
$ cd mce
$ virtualenv venv
(Mac/Linux)$ source venv/bin/activate
(Windows)  $ .\venv\Scripts\activate
$ pip install manim jupyter
```

Clone repo:

```
git clone https://github.com/Elteoremadebeethoven/manim-ce-gl-fast-course.git -b mce code
```

Select the virtual environment that you have created.

![image](https://user-images.githubusercontent.com/43224662/214361758-c2cccdeb-e532-4e24-9a3d-2ae8f4bc5546.png)


## ► ManimGL setup:

Install ManimGL v1.2 version:

```bash
$ git clone https://github.com/3b1b/manim/ -b v1.2.0 mgl-v1.2 --depth=1
$ cd mgl-v1.2
$ virtualenv venv
(Mac/Linux)$ source venv/bin/activate
(Windows)  $ .\venv\Scripts\activate
$ pip install -e .
```

Remove unnecessary files:

```bash
rm -rf docs LICENSE.md logo MANIFEST.in manimgl.egg-info pyproject.toml README.md requirements.txt setup.*
```

Extra dependencies:

```
pip install python-dotenv
```

Enviroment variables (.env file):

```.env
RENDER_SCENE=Example1
RENDER_OPTIONS=om
OUTPUT_NAME=output
PROGRESS_BARS=False
FPS=
START_AT=
```

Makefile:

```make
FILE=

run:
	watchexec \
	-w $(FILE) \
	-w ".env" \
	"python $(FILE)"
```

File example:

```py
from manimlib import *

class Example1(Scene):
    def construct(self):
        t = RegularPolygon(10, color=TEAL)
        t.to_edge(RIGHT)
        self.add(t)
        self.wait()


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
```

Clone repo:

```
git clone https://github.com/Elteoremadebeethoven/manim-ce-gl-fast-course.git -b mgl code
```

# 💸 Suport this work on:

## PayPal: https://www.paypal.com/paypalme/zavdn
## Patreon: https://www.patreon.com/theoremofbeethoven
