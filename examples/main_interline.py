from PVG          import *
from curvebuilder import *

canvas = Canvas()

(line1,line2) = Circle().polygon(17).close().split(2)

canvas.draw([CurveBuilder.interline(line1,line2.reverse(),t).line() for t in usamples(10)])

canvas.save("main_interline.png")

