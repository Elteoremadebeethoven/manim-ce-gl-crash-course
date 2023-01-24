# Manim CE/GL fast course

## Disclaimer

|                       | Manim Professional Course | ManimCE-GL Fast course |
| :-------------------: | :-----------------------: | :--------------------: |
|        Theory         |             ✅             |           ✅            |
|       Pro-tips        |             ✅             |           ❌            |
|       Examples        |             ✅             |           ❌            |
|       Exercises       |             ✅             |           ❌            |
| ManimGL topics (v1.2) |             ❌             |           ✅            |
|         Free          |             ❌             |           ✅            |

## Requirements to take the course:

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
[![manim installation](https://img.youtube.com/vi/CYOLQk8GpME/0.jpg)](https://www.youtube.com/watch?v=CYOLQk8GpME)

2.
[![manim installation](https://img.youtube.com/vi/CYOLQk8GpME/0.jpg)](https://www.youtube.com/watch?v=CYOLQk8GpME)


## ManimCE setup:

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


## ManimGL setup:

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
