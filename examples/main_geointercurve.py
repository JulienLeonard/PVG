from PVG           import *
from geointercurve import *

canvas  = Canvas()

polygon = Circle().polygon(100).close()

geo = GeoIntercurve(polygon.subline(0.0,0.5).reverse(),polygon.subline(0.5,1.0))

canvas.draw(polygon)

#canvas.draw(polygon.line(0.11),Color.blue())
#for curve in [geo.mlong1,geo.mlong2]:
#    canvas.draw(curve.line(0.1),Color.green())


# canvas.draw(Circle().scale(0.5).polygon(4),Color.red())

#for i in usamples(10):
#    canvas.draw(geo._ycurve(i).line(),Color.red())

canvas.draw(geo.mappolygon(Polygon(Circle(Point(0.5,0.5)).scale(0.4).polygon(3).close().points(1000))),Color.red())

canvas.save("main_geointercurve.png")
