from PVG     import *
from geoquad import *

canvas  = Canvas()

# for (p1,p2) in pairs(Circle().points(10)):
#    canvas.draw(CurveBuilder.hump(p1,p2,heightratio = 1.0).line(),Color.black())
#    canvas.draw(CurveBuilder.hump(p1,p2,heightratio = -1.0).line(),Color.black())

geo = GeoQuad.circle()

canvas.draw(geo.polygon(),Color.red(0.5))

hump1 = CurveBuilder.hump(Point(0.0,0.0),Point(0.0,1.0),heightratio = -0.1)
hump2 = CurveBuilder.hump(Point(0.0,0.0),Point(0.0,1.0),heightratio = -0.2)

hump3 = CurveBuilder.hump(Point(0.0,0.0),Point(0.0,1.0),heightratio = -0.3)
hump4 = CurveBuilder.hump(Point(0.0,0.0),Point(0.0,1.0),heightratio = -0.4)

hump5 = CurveBuilder.hump(Point(0.0,0.0),Point(0.0,1.0),heightratio = -0.5)
hump6 = CurveBuilder.hump(Point(0.0,0.0),Point(0.0,1.0),heightratio = -0.6)

chevron1 = geo.transverses2polygon(0.05,hump1,0.1,hump2)
chevron2 = geo.transverses2polygon(0.15,hump3,0.2,hump4)
chevron3 = geo.transverses2polygon(0.25,hump5,0.3,hump6)

canvas.draw(chevron1,Color.black())
canvas.draw(chevron2,Color.black())
canvas.draw(chevron3,Color.black())

canvas.save("main_hump.png")
