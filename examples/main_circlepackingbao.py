from PVG              import *
from baopattern       import *
from circlepackingbao import *

canvas = Canvas()

def fdraw(node,index,style):
    canvas.draw(node,style)

boundaries = []
baopattern = BaoPattern().fdraw(fdraw).radiuspattern(R(1.0,20.0).samples(20)).colorpattern([Color.hue2color(float(index)/20.0) for index in range(20)])
inodes     = baonodes0()

canvas.draw(inodes)

packing = CirclePackingBao().iter(1000,boundaries,inodes,baopattern)

canvas.save("circlepackingbao.png")
