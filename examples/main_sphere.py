import sys
sys.path.append("../lib/")
from PVG3D         import *
from canvasSunflow import *

canvas = CanvasSunflow().margin(0.5).size(10000)

canvas.draw(Sphere(Point3D(0.0,0.0,0.0),1.0),Style(Color.red()))

puts("stop draw canvas")
canvas.save("c:/PROJECTS/BALL2ART/main_sphere.sc")
