from PVG import *

outputfilepath = defaultoutputdir() + "/" + "main_rendCairo.png"
render = RenderCairo(Viewport(Point(0.0,0.0),5.0),ImageDim(1000,1000),outputfilepath, Color.red())
render.drawcircle(Circle(Point(0.0,0.0),1.0),Color.green())
render.end()
