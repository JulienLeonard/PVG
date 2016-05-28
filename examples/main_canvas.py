import sys
sys.path.append("../lib/")
from PVG import *
from canvascairo import *
render = Canvas("main_canvas.png").background(Color.red()).render()
render.drawcircle(Circle())
render.end()
