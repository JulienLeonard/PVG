import sys
sys.path.insert(0, './../lib')

from utils      import *
from canvas     import *
from SVGparser  import *
import color

render = Canvas("main_flower.ppm").render()

paths  = svgPaths("flower.svg")
silhouettes = [path.silhouette() for path in paths]
for (silhouette,ccolor) in lzip(silhouettes,[color.green(0.5),color.red(0.5),color.yellow(0.5)]):
    render.drawpolygons(silhouette.polygons(0),ccolor)
    

render.end()
