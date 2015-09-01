from PVG          import *
from curvebuilder import *

canvas = Canvas()

canvas.draw(Circle().polygon(6).curveRange().lines(10))

canvas.save("main_interline.png")

