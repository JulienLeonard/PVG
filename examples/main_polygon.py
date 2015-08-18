# some_file.py
import sys
sys.path.insert(0, './../lib')

from canvas    import *
from polygon   import *
import color

render = Canvas("main_polygon.ppm").render()

polygon = square(P0,1.0)
render.drawpolygon(polygon,color.black(0.5))
render.drawcircles([Circle(p,0.01) for p in polygon.points(100)],color.black())

render.end()
