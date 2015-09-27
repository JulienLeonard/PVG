from PVG     import *
from PVGPACK import *
import copy

canvas = Canvas().margin(1.0).background(Color.black())

quadtree   = QuadTree()
poly       = Circle().scale(20).polygon(5).close()
baonodess  = [BaoNode.fromsegment(segment=seg,radius=1.0) for seg in poly.segments()]

def fdrawlayer(nodes,ilayer):
    puts("nnodes",len(nodes))
    # hues = [R(0.0,0.25).sample(float(ilayer % 4)/4.0)] * len(nodes)
    hues = R(0.0,0.2).symsamples(len(nodes) * 2)
    for (node,hue) in zip(nodes,hues):
        canvas.draw(node.scale(0.9),Color.hue2color(hue))

baopattern  = BaoPatternLayer().fdrawlayer(fdrawlayer).radiuspattern(R(1.0,3.0).symsamples(20)).colorpattern([Color.hue2color(float(index)/20.0) for index in range(20)])
packings    = [CirclePackingBaoLayer([],baonodes,copy.deepcopy(baopattern),-1.0,quadtree) for baonodes in baonodess]
sequencer   = CirclePackingSequencer(packings,quadtree)

sequencer.iter(2000)

canvas.save("circlepackingsequencer.png")
