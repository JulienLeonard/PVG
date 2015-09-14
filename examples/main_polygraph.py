from PVG import *

render = Canvas("main_polygon.png").render()

polygon = square(P0,1.0)
render.drawpolygon(polygon,Color.black(0.5))
render.drawcircles([Circle(p,0.01) for p in polygon.points(100)],Color.black())

render.end()
