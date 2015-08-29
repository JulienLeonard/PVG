from PVG              import *
from circlepackingbao import *

canvas = Canvas()

def fdraw(canvas,node,index,style):
    canvas.draw(node,style)

boundaries = []
inodes     = baonodes0()
baopattern = BaoPattern().radiuspattern(R(1.0,3.0).samples(10)).colorpattern([Color.hue2color(float(index)/100.0) for index in range(100)])

canvas.draw(inodes)

packing = CirclePackingBao.iter(canvas,fdraw,boundaries,inodes,baopattern,10000)

canvas.save("circlepackingbao.png")
