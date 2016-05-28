import sys
sys.path.append("../lib/")
from PVGPACK3D import *
from canvasSunflow import *

random.seed(45674567235.0)

canvas = CanvasSunflow().margin(0.5).size(10000)

packing = SpherePacking()

# seeds = [(Circle().coords([-1.0,0.0,1.0]),Circle().coords([1.0,0.0,1.0]),1.0)]
seeds = [radius2seed3D30(0.1,0.0,1.0),radius2seed3D30(0.1,0.0,-1.0)]

quadtree = QuadTree3D()

result = packing.radiusf(makeradiusmin3Df(0.95,0.99)).compute(seeds,quadtree,20000,0.0001)

puts("nspheres",len(result.spheres()))

puts("start draw canvas")
spheres = result.spheres()
sindex = 0
for sphere in spheres:
    sindex += 1
    canvas.draw(sphere.scale(1.0),Style(Color.hue2color(float(sindex)/float(len(spheres)))))
    # canvas.draw(sphere.scale(1.0),Style(Color.white()))
                

puts("stop draw canvas")
canvas.save("c:/PROJECTS/BALL2ART/main_spherepacking.sc")
