import sys
sys.path.append("../lib/")
from PVGPACK import *
from canvascairo import *

random.seed(45674567235.0)

canvas = Canvas().margin(0.5).size(10000)

packing = CirclePacking()

# seeds = [(Circle().coords([-1.0,0.0,1.0]),Circle().coords([1.0,0.0,1.0]),1.0)]
seeds = [seed20]

quadtree = QuadTree()

result = packing.compute(seeds,quadtree,1000000,0.01)

puts("ncircles",len(result.circles()))

puts("start draw canvas")
canvas.draw([c.scale(0.75) for c in result.circles()],Color.red())

puts("stop draw canvas")
canvas.save("main_circlepacking.png")
