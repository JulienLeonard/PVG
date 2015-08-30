from PVG          import *
from curvebuilder import *

canvas = Canvas()

(line1,line2) = Circle().polygon(6).close().split(2)
canvas.draw([line.line(0.1) for line in (line1,line2)],Color.green())

for t in usamples(10):
    canvas.draw(CurveBuilder.interline(line1,line2.reverse(),t).line(0.01),Color.red(0.5))

canvas.save("main_interline.png")

