import sys
sys.path.append("../lib/")
from PVG import *
from PVGPACK import *
from canvasSunflow import *

canvas = CanvasSunflow()

def fdraw(node,index,style):
    if style == None:
        style = Style()
    canvas.draw(node.scale(1.25),style)

boundaries = []
baopattern = BaoPattern().fdraw(fdraw).radiuspattern(R(0.01,0.2).samples(5000)).colorpattern([Color.hue2color(float(index)/5000.0) for index in range(5000)])
inodes     = [BaoNode(None,Circle().coords((0.0,0.0,0.1)),0,0),BaoNode(None,Circle().coords((0.2,0.0,0.1)),1,1)]
#inodes = BaoNode.baonodes0()

canvas.draw(inodes)

packing = CirclePackingBao(boundaries,inodes,baopattern).iter(5000)

canvas.save("c:/PROJECTS/BALL2ART/circlepacking.sc")
