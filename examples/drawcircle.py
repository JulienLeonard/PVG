# some_file.py
import sys
sys.path.insert(0, './../lib')

from utils     import *
from drawutils import *
import color

render = RenderCenter((1000,1000),"C:/DEV/PVG/output/drawcircle.ppm")
render.drawcircle(C0)
render.end()
