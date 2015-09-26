from PVG                    import *
from PVGPACK                import *
import copy

canvas = Canvas()

rnlayer = Roller([i for i in range(20)])
def fdrawlayer(nodes):
    puts("nnodes",len(nodes))
    hues = [float(rnlayer.next() % 4)/4.0] * len(nodes)
    for (node,hue) in zip(nodes,hues):
        canvas.draw(node,Color.hue2color(hue))

def fdraw(node,index,style):
    canvas.draw(node.scale(0.5),style)

poly = Circle().scale(100.0).polygon(30).close()
canvas.draw(poly,Color.black())
boundaries  = poly.segments()
baopattern0 = BaoPatternLayer().fdraw(fdraw).fdrawlayer(fdrawlayer).radiuspattern(R(1.0,2.0).samples(20)).colorpattern([Color.hue2color(float(index)/20.0) for index in range(20)])
inodes      = BaoNode.fromcircle(Circle(Point(0.0,95.0),1.0))
# baopattern = BaoPattern().fdraw(fdraw).radiuspattern(R(5.0,5.0).samples(20)).colorpattern([Color.hue2color(float(index)/20.0) for index in range(20)])

# canvas.draw(inodes)

# packing = CirclePackingBao.iter(boundaries,inodes,baopattern,200,-1.0)
quadtree = QuadTree()
pack = CirclePackingBaoLayer(boundaries,inodes,copy.deepcopy(baopattern0),-1.0,quadtree).iter(1020)


subpackings = [CirclePackingBaoLayer(boundaries,pack.mstack.nodes()[i:i+2],copy.deepcopy(baopattern0),-1.0,quadtree) for i in [-9,-34]]

for i in range(1000):
    for subpacking in subpackings:
        subpacking.iter()


canvas.save("multiplebaolayer.png")
