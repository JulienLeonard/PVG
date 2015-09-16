from PVG     import *
from geoquad import *

canvas  = Canvas()

canvas.draw(Polygon.Unitary,Color.black())

geo2 = GeoQuad.circle()

for i in usamples(50):
    canvas.draw(geo2.xcurve(i).line(0.001),Color.red())
    canvas.draw(geo2.ycurve(i).line(0.001),Color.red())


poly1 = Polygon(Circle.Unitary.scale(0.95).polygon(4).close().points(200))

canvas.draw(poly1,Color.red(0.5))

unmappoly = geo2.unmappolygon(poly1)

canvas.draw(unmappoly,Color.green(0.5))

canvas.save("main_geounmap.png")
