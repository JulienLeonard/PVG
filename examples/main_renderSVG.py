from PVG import *

outputfilepath = defaultoutputdir() + "/" + "main_renderSVG.svg"
render = RenderSVG(Viewport(Point(0.0,0.0),2.0),ImageDim(500,500),outputfilepath, Color.white())
render.drawcircle(Circle(Point(0.0,0.0),1.0),Color.green())
render.end()
