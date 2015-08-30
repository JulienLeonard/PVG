from PVG          import *

canvas = Canvas()

paths  = svgPaths("flower.svg")
silhouettes = [path.silhouette() for path in paths]
for (silhouette,ccolor) in lzip(silhouettes,[Color.green(0.5),Color.red(0.5),Color.yellow(0.5)]):
    canvas.draw(silhouette.polygon(),ccolor)
    canvas.draw([Circle(p,10.0) for p in silhouette.polygon().points(100)],ccolor.a(1.0))


canvas.save("main_curvepoints.png")
