from PVGPACK import *
from canvasSunflow import *

random.seed(45674567235.0)

canvas = CanvasSunflow().margin(0.5).size(10000)

packing = CirclePacking().radiusf(makeradiusminf(1.2,0.75))

# seeds = [(Circle().coords([-1.0,0.0,1.0]),Circle().coords([1.0,0.0,1.0]),1.0)]
seeds = [Seed2().seeddef([Circle(Point(0.0,-0.1),0.1),Circle(Point(0.0,0.1),0.1),1.0])]

quadtree = QuadTree()

result = packing.compute(seeds,quadtree,20000,0.001)

puts("ncircles",len(result.circles()))

puts("start draw canvas")
canvas.draw([c.scale(1.5) for c in result.circles()],Style(Color.red()))

puts("stop draw canvas")
canvas.save("c:/PROJECTS/BALL2ART/circlepacking.sc")
