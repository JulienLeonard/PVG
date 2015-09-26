from PVG                    import *
from PVGPACK                import *

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
boundaries = poly.segments()
baopattern = BaoPatternLayer().fdraw(fdraw).fdrawlayer(fdrawlayer).radiuspattern(R(5.0,5.0).samples(20)).colorpattern([Color.hue2color(float(index)/20.0) for index in range(20)])
inodes     = BaoNode.fromcircle(Circle(Point(0.0,95.0),10.0))
# baopattern = BaoPattern().fdraw(fdraw).radiuspattern(R(5.0,5.0).samples(20)).colorpattern([Color.hue2color(float(index)/20.0) for index in range(20)])

# canvas.draw(inodes)

# packing = CirclePackingBao.iter(boundaries,inodes,baopattern,200,-1.0)
packing = CirclePackingBaoLayer(boundaries,inodes,baopattern,-1.0).iter(10000)

canvas.save("circlepackingbaolayer.png")
