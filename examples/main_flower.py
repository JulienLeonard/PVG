import sys
sys.path.insert(0, './../lib')

from utils      import *
from canvas     import *
from SVGparser  import *
import color

render = Canvas("main_flower.png").render()

paths  = svgPaths("flower.svg")
silhouettes = [path.silhouette() for path in paths]
for (silhouette,ccolor) in lzip(silhouettes,[Color.green(0.5),Color.red(0.5),Color.yellow(0.5)]):
    render.drawpolygons(silhouette.polygons(0),ccolor)
    

render.end()
