import sys
sys.path.append("../lib/")
from PVG         import *
from PVG3D         import *
from canvasSunflow import *
from math import sqrt

canvas = CanvasSunflow().margin(0.5).size(10000)

ps = Circle().scale(0.5).samples(4)


sphere1 = Sphere(Point3D(ps[0].x(),ps[0].y(),0.5),0.25*sqrt(3.0))
sphere2 = Sphere(Point3D(ps[1].x(),ps[1].y(),0.5),0.25*sqrt(3.0))
sphere3 = Sphere(Point3D(ps[2].x(),ps[2].y(),0.5),0.25*sqrt(3.0))

sphere4 = adjsphere(sphere1,sphere2,sphere3,0.25*sqrt(3.0),1.0)
sphere5 = adjsphere(sphere1,sphere2,sphere3,0.25*sqrt(3.0),-1.0)

for sphere in [sphere1,sphere2,sphere3]:
    canvas.draw(sphere,Style(Color.red()))

canvas.draw(sphere4,Style(Color.blue()))
canvas.draw(sphere5,Style(Color.blue()))

puts("stop draw canvas")
canvas.save("c:/PROJECTS/BALL2ART/main_tangent3D.sc")
