# some_file.py
import sys
sys.path.insert(0, './../lib')

from canvas    import *
from polygon   import *
from color     import *

render = Canvas("main_closure.png").render()

polygon1 = square(P0,1.0)
polygon2 = Circle(Point(1.0,0.0),1.0).polygon()

random.seed(0.0)
for (spoly1,spoly2) in polygon2.closures(polygon1):
    render.drawpolygons([poly.reduce(0.9) for poly in [spoly1,spoly2]],Color.rand(0.5))

render.end()

