import sys
sys.path.append("../lib/")
from PVGPACK3D import *
from canvasSunflow import *

random.seed(45674567235.0)

canvas = CanvasSunflow().margin(0.5).size(10000)

packing = CirclePacking3D()

# seeds = [(Circle().coords([-1.0,0.0,1.0]),Circle().coords([1.0,0.0,1.0]),1.0)]
seeds = [seed20]

quadtree = QuadTree3D()

result = packing.compute(seeds,quadtree,1000000,0.01)

puts("nspheres",len(result.spheres()))

puts("start draw canvas")
canvas.draw([c.scale(0.75) for c in result.spheres()],Color.red())

puts("stop draw canvas")
canvas.save("main_spherepacking.png")
