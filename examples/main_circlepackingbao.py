import sys
sys.path.append("../lib/")
from PVG           import *
from PVGPACK       import *
from canvascairo import *

canvas = Canvas()

def fdraw(node,index,style):
    canvas.draw(node,style)

boundaries = []
baopattern = BaoPattern().fdraw(fdraw).radiuspattern(R(1.0,20.0).samples(20)).colorpattern([Color.hue2color(float(index)/20.0) for index in range(20)])
inodes     = BaoNode.baonodes0()

canvas.draw(inodes)

packing = CirclePackingBao(boundaries,inodes,baopattern).iter(1000)

canvas.save("circlepackingbao.png")
