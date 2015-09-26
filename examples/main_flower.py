from PVG import *

render = Canvas("main_flower.png").render()

paths  = svgPaths("flower.svg")
silhouettes = [path.hierarchy() for path in paths]
for (silhouette,ccolor) in lzip(silhouettes,[Color.green(0.5),Color.red(0.5),Color.yellow(0.5)]):
    render.drawpolygons(silhouette.shapes(),ccolor)
    

render.end()
