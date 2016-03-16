from PVGPACK   import *
from canvasSVG import *

random.seed(45674567235.0)

canvas = CanvasSVG().margin(1.0).size(1000)

packing = CirclePacking()

# seeds = [(Circle().coords([-1.0,0.0,1.0]),Circle().coords([1.0,0.0,1.0]),1.0)]
seeds = [seed20]

quadtree = QuadTree()

import cProfile
cProfile.run('result = packing.compute(seeds,quadtree,1000000,0.01)')

puts("ncircles",len(result.circles()))

puts("start draw canvas")
canvas.draw(result.circles(),Style(color=Color.red(),sizeratio=0.75))

puts("stop draw canvas")
canvas.save("main_circlepacking.svg")
