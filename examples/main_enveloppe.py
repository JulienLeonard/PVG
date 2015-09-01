from PVG          import *
from curvebuilder import *

canvas = Canvas()

canvas.draw(square(P0,1.0))

canvas.draw(CurveBuilder.enveloppe(square(P0,1.0).points(),0.3333,5,0),Color.red(0.5))

canvas.save("main_enveloppe.png")

