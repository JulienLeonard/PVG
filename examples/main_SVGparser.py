import sys
sys.path.insert(0, './../lib')

from utils      import *
from canvas     import *
from SVGparser  import *
import color

render = Canvas("main_SVGparser.ppm").render()
paths = svgPaths("flower.svg")
silhouettes = [path.silhouette() for path in paths]
for (silhouette,color) in lzip(silhouettes,[color.black(),color.red(),color.yellow()]):
    render.drawpolygons(silhouette.polygons(0),color)

render.end()
