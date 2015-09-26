from PVG import *

render = Canvas("main_SVGparser.png").render()
paths = svgPaths("flower.svg")
silhouettes = [path.hierarchy() for path in paths]
for (silhouette,color) in lzip(silhouettes,[Color.black(),Color.red(),Color.yellow()]):
    render.drawpolygons(silhouette.shapes(),color)

render.end()
