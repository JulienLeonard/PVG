from PVG     import *
from PVGPACK import *
import copy

canvas = Canvas()

quadtree   = QuadTree()
poly       = Circle().scale(20).polygon(5).close()
baonodess  = [BaoNode.fromsegment(segment=seg,radius=1.0) for seg in poly.segments()]

canvas.draw(poly)
for nodes in baonodess:
    canvas.draw(nodes,Color.red())

rnlayer = Roller([i for i in range(20)])
def fdrawlayer(nodes):
    puts("nnodes",len(nodes))
    hues = [float(rnlayer.next() % 4)/4.0] * len(nodes)
    for (node,hue) in zip(nodes,hues):
        canvas.draw(node,Color.hue2color(hue))

baopattern  = BaoPatternLayer().fdrawlayer(fdrawlayer).radiuspattern(R(1.0,2.0).samples(20)).colorpattern([Color.hue2color(float(index)/20.0) for index in range(20)])
packings    = [CirclePackingBaoLayer([],baonodes,copy.deepcopy(baopattern),-1.0,quadtree) for baonodes in baonodess]
sequencer   = CirclePackingSequencer(packings,quadtree)

sequencer.iter(5000)

canvas.save("circlepackingsequencer.png")
