# some_file.py
import sys
sys.path.insert(0, './../lib')

from utils      import *
from canvas     import *
from SVGparser  import *
import color

render = Canvas("main_curvepoints.ppm").render()

paths  = svgPaths("flower.svg")
silhouettes = [path.silhouette() for path in paths]
for (silhouette,ccolor) in lzip(silhouettes,[color.green(0.5),color.red(0.5),color.yellow(0.5)]):
    render.drawpolygon(silhouette.polygon(),ccolor)
    render.drawcircles([Circle(p,10.0) for p in silhouette.polygon().points(100)],color.a(ccolor,1.0))


render.end()
