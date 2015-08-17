import sys
sys.path.insert(0, './../lib')

from utils      import *
from drawutils  import *
from SVGparser  import *
from silhouette import *
import color

render = RenderCenter((1000,1000),"C:/DEV/CVG/output/main_SVGparser.ppm")
paths = svgPaths("flower.svg")
puts("paths",paths)
silhouettes = [Silhouette(path) for path in paths]
for (silhouette,color) in lzip(silhouettes,[color.black(),color.red(),color.yellow()]):
    render.drawpolygons(silhouette.polygons(0),color)

render.end()
