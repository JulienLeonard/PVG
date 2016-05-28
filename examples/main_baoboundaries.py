import sys
sys.path.append("../lib/")
from PVG              import *
from circlepackingbao import *
from baopattern       import *
from canvascairo      import *

canvas = Canvas()

def fdraw(node,index,style):
    canvas.draw(node,style)

boundaries = [Circle(p,1.0) for p in Circle(Point(0.0,98.0),100.0).samples(300)]
inodes     = BaoNode.baonodes0()
baopattern = BaoPattern().fdraw(fdraw).radiuspattern(R(1.0,3.0).samples(20)).colorpattern([Color.hue2color(float(index)/20.0) for index in range(20)])

canvas.draw(inodes)
canvas.draw(boundaries)

packing = CirclePackingBao.iter(boundaries,inodes,baopattern,5000)

canvas.save("baoboundaries.png")
