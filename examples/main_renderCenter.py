from PVG import *

outputfilepath = defaultoutputdir() + "/" + "main_renderCenter.png"
render = RenderCenter(ImageDim(1000,1000),outputfilepath, Color.red())
render.drawcircle(Circle(Point(0.0,0.0),1.0),Color.green())
render.drawcircle(Circle(Point(2.0,0.0),1.0),Color.green())
render.drawcircle(Circle(Point(1.0,1.7),1.0),Color.green())
render.end()
