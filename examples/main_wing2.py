from PVG import *

render = Canvas("main_wing2.png").render()

paths  = svgPaths("wing2.svg")
silhouette = svgpaths2silhouette(paths)
render.drawpolygons(silhouette.polygons(0),Color.black())
render.drawpolygons(silhouette.polygons(1),Color.red())
render.drawpolygons(silhouette.polygons(2),Color.green())
render.end()
