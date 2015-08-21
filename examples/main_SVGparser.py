import sys
sys.path.insert(0, './../lib')

from utils      import *
from canvas     import *
from SVGparser  import *
from color      import *

render = Canvas("main_SVGparser.png").render()
paths = svgPaths("flower.svg")
silhouettes = [path.silhouette() for path in paths]
for (silhouette,color) in lzip(silhouettes,[Color.black(),Color.red(),Color.yellow()]):
    render.drawpolygons(silhouette.polygons(0),color)

render.end()
