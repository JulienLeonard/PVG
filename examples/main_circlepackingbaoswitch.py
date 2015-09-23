from PVG                    import *
from baopattern             import *
from circlepackingbaoswitch import *

canvas = Canvas()

def fdraw(node,index,style):
    canvas.draw(node,style)

poly = Circle().scale(100.0).polygon(30).close()
canvas.draw(poly,Color.black())
boundaries = poly.segments()
inodes     = baonodes0()
baopattern = BaoPatternSide().fdraw(fdraw).radiuspattern(R(1.0,2.0).samples(20)).colorpattern([Color.hue2color(float(index)/100.0) for index in range(100)]).sidepattern([1.0,-1.0] * 10 + [-1.0]*20)

canvas.draw(inodes)

packing = CirclePackingBaoSwitch.iter(boundaries,inodes,baopattern,5000)

canvas.save("circlepackingbaoswitch.png")
