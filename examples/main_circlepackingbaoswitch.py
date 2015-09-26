from PVG                    import *
from PVGPACK                import *

canvas = Canvas()

def fdraw(node,index,style):
    canvas.draw(node,style)

poly = Circle().scale(100.0).polygon(30).close()
canvas.draw(poly,Color.black())
boundaries = poly.segments()
baopattern = BaoPatternSwitch().fdraw(fdraw).radiuspattern(R(1.0,2.0).samples(20)).colorpattern([Color.hue2color(float(index)/20.0) for index in range(20)]).sidepattern([1.0] * 10 + [-1.0]*10)
inodes     = baonodes0()

canvas.draw(inodes)

packing = CirclePackingBaoSwitch(boundaries,inodes,baopattern).iter(5000)

canvas.save("circlepackingbaoswitch.png")
