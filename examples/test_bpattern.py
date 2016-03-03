from PVG import *
from color import *
from utils import *
from tangentutils import *
from drawutils import *
from geoutils  import *
# from bpattern2 import *
from bpatterndefs import *
# from autoclass import *

canvas = Canvas().size(10000).margin(0.9).background(Color(0.9,0.9,0.9,1.0))

quadtree   = QuadTree()


patterndef = BPatternDef().ncircles(6).angles([0.0,0.2,0.1]).rratios((1.0,1.0)).lratios([]).vangleincr(0.01).sangleincr(1.0).style({"color":Color.black(),"sizeratio":1.0})
juncgen    = JunctionGen().add(PlugSet.plug2s,JunctionDef().ratio(1.0).nextpatterndefs([patterndef])).add(PlugSet.singleext,JunctionDef().ratio(1.0).nextpatterndefs([patterndef]))

patterndef.junctiongen(juncgen)

roots = [RootPattern().junctiongen(juncgen)]

puts("starting bworld")

bworld  = BWorld(canvas,quadtree).initwithpatterns(roots)

import cProfile
cProfile.run('bworld.compute(10000,0.01).draw(canvas)')


# render.end()
canvas.save("test_bpattern.png")



