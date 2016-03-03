from PVG import *
from color import *
from utils import *
from tangentutils import *
from drawutils import *
from geoutils  import *
# from bpattern2 import *
from bpatterndefs2 import *
# from autoclass import *

canvas = Canvas().size(10000).margin(0.9).background(Color(0.9,0.9,0.9,1.0))

quadtree   = QuadTree()


patterndef  = BPatternDef().ncircles(6).angles([0.0,0.2,0.1]).rratios((1.0,1.0)).lratios([]).vangleincr(0.02).sangleincr(1.0).style({"color":Color.black(),"sizeratio":1.0})
patterndef2 = BPatternDef().ncircles(2).angles([0.0,0.2,0.1]).rratios(()).lratios([1.0,3.0]).vangleincr(0.0).sangleincr(1.0).style({"color":Color.red(),"sizeratio":1.0})
juncgen     = JunctionGen().add(PlugSet.plug2s,JunctionDef().ratio(0.975).nextpatterndefs([patterndef2])).add(PlugSet.singleext,JunctionDef().ratio(0.975).nextpatterndefs([patterndef]))
juncgen2    = JunctionGen()
juncgenroot = JunctionGen().add(PlugSet.plug2s,JunctionDef().ratio(0.975).nextpatterndefs([patterndef]))

patterndef.junctiongen(juncgen)
patterndef2.junctiongen(juncgen2)

roots = [RootPattern().junctiongen(juncgenroot)]

puts("starting bworld")
bworld  = BWorld(canvas,quadtree).initwithpatterns(roots)

bworld.compute(5000,0.01).draw(canvas)

# render.end()
canvas.save("test_bpattern2.png")



