from PVG import *

render = Canvas("main_closure.png").render()

# polygon1 = square(P0,1.0)
polygon1 = Circle(Point(0.0,0.0),1.0).polygon(4)
polygon2 = Circle(Point(1.0,0.0),1.0).polygon(4)
# polygon2 = square(Point(0.5,0.5),1.0)
render.drawpolygons([polygon1,polygon2],Color.red(0.5))

random.seed(0.0)
for (spoly1,spoly2) in polygon2.closures(polygon1):
    render.drawpolygons([poly.reduce(0.9) for poly in [spoly1,spoly2]],Color.rand(0.5))

render.end()

