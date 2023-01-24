# Manim CE/GL fast course

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
