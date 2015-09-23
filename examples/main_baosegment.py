from PVG      import *
from PVGPACK  import *   

canvas = Canvas()

def fdraw(node,index,style):
    canvas.draw(node,style)

polyboundary = Circle().scale(100.0).polygon(30).close()
canvas.draw(polyboundary.line(),Color.black())
boundaries = polyboundary.segments()
inodes     = baonodes0()
baopattern = BaoPattern().fdraw(fdraw).radiuspattern(R(1.0,2.0).samples(20)).colorpattern([Color.hue2color(float(index)/20.0) for index in range(20)])

canvas.draw(inodes)

packing = CirclePackingBao.iter(boundaries,inodes,baopattern,10000)

canvas.save("baosegment.png")
