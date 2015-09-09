from PVG import *
from polyface import *

canvas = Canvas()
eg = EdgeGraph().loadwithsegments(Circle().polygon(10).close().segments() + [Segment(Point(-1.0,0.0),Point(1.0,0.0))])

#for edge in eg.edges():
#    canvas.draw(Polygon(edge.points()).line(),Color.rand())

for polyface in eg.polyfaces():
    for longitude in polyface.longitudes()[0]:
        canvas.draw(longitude.line(),Color.rand())

canvas.save("main_polyface.png")
