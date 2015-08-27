import sys
sys.path.insert(0, './../lib')

from utils      import *
from canvas     import *
from SVGparser  import *
from silhouette import *
from color      import *
from intersectionbuilder import *
from edgegraph import *


render = Canvas("main_wingline.png").render()

paths  = svgPaths("winglines.svg")

segs = [(p1,p2) for path in paths for (p1,p2) in pairs(path.silhouette().polygon().lengthsamples(5.0))]

puts("interseg computation")
intersegs = IntersectionBuilder().intersectionsegs(segs)

puts("edgegraph computation")
eg = EdgeGraph().loadwithpointpairs(intersegs)
polygons = [Polygon(points).reduce(0.99) for points in eg.closedpolygons()]

render.drawpolygons(polygons,Color.red(0.5))

render.end()
