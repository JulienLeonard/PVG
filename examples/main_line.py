from PVG          import *

canvas = Canvas()

canvas.draw(Circle().polygon(6).close().line(0.1),Color.red())

canvas.save("main_line.png")

