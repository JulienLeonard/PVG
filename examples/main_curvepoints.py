# some_file.py
import sys
sys.path.insert(0, './../lib')

from utils      import *
from canvas     import *
from SVGparser  import *
from color      import *

render = Canvas("main_curvepoints.png").render()

paths  = svgPaths("flower.svg")
silhouettes = [path.silhouette() for path in paths]
for (silhouette,ccolor) in lzip(silhouettes,[Color.green(0.5),Color.red(0.5),Color.yellow(0.5)]):
    render.drawpolygon(silhouette.polygon(),ccolor)
    render.drawcircles([Circle(p,10.0) for p in silhouette.polygon().points(100)],ccolor.a(1.0))


render.end()
