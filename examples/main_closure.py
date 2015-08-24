# some_file.py
import sys
sys.path.insert(0, './../lib')

from canvas    import *
from polygon   import *
from color     import *

render = Canvas("main_closure.png").render()

polygon1 = square(P0,1.0)
polygon2 = Circle(Point(1.0,0.0),1.0).polygon()
render.drawpolygons([polygon1,polygon2],Color.red(0.5))

for ipolygon in polygon1.closures(polygon2):
    render.drawpolygon(ipolygon.reduce(0.9),Color.rand())

render.end()

