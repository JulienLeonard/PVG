from PVG                    import *
from PVGPACK                import *

canvas = Canvas()

def fdrawlayer(nodes):
    puts("nnodes",len(nodes))
    hues = R(0.0,1.0).samples(2*len(nodes))
    for (node,hue) in zip(nodes,hues):
        canvas.draw(node,Color.hue2color(hue))

poly = Circle().scale(100.0).polygon(30).close()
canvas.draw(poly,Color.black())
boundaries = poly.segments()
inodes     = BaoNode.fromcircle(Circle(Point(0.0,95.0),10.0))
baopattern = BaoPatternLayer().fdrawlayer(fdrawlayer).radiuspattern(R(5.0,5.0).samples(20))

# canvas.draw(inodes)

packing = CirclePackingBaoLayer.iter(boundaries,inodes,baopattern,500,-1.0)

canvas.save("circlepackingbaolayer.png")
