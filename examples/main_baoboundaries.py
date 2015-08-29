from PVG              import *
from circlepackingbao import *

canvas = Canvas()

def fdraw(node,index,style):
    canvas.draw(node,style)

boundaries = [Circle(p,1.0) for p in C0.scale(100.0).samples(usamples(300))]
inodes     = baonodes0()
baopattern = BaoPattern().fdraw(fdraw).radiuspattern(R(1.0,3.0).samples(20)).colorpattern([Color.hue2color(float(index)/20.0) for index in range(20)])

canvas.draw(inodes)

packing = CirclePackingBao.iter(boundaries,inodes,baopattern,3000)

canvas.save("baoboundaries.png")
