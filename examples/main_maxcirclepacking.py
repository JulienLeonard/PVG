from PVG              import *
from maxcirclepacking import *

canvas = Canvas()

polygon = Circle().polygon(8).split(2)[0].close()

canvas.draw(polygon,Color.red())
canvas.draw(polygon.maxcircles(15))

canvas.save("main_maxcirclepacking.png")
