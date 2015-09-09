from PVG          import *
from voronoiutils import *

canvas = Canvas()
canvas.draw(Circle().polygon(5),Color.black(0.5))
polygons = Voronoi(Circle().polygon(5).points() + Circle().scale(0.5).polygon(15).points() + [Point.P0()]).polygons()
puts("len polygons",len(polygons))
canvas.draw([p.reduce(0.99) for p in polygons],Color.red())
canvas.save("main_voronoi.png")
