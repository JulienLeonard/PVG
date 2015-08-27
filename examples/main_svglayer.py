from PVG import *

canvas = Canvas()
parser = SVGParser().parse("halfbutterfly.svg")
silhouettes = [layer.silhouette() for layer in parser.layers()]
rcolor = Roller([Color.black(),Color.red(),Color.yellow()])

sortlist = []
for silhouette in silhouettes:
    for level in range(2):
        for poly in silhouette.polygons(level):
            sortlist.append((poly.middle().x(),poly))

sortlist.sort()
symx      = sortlist[-1][0]
nosym     = sortlist[-1][1]

for silhouette in silhouettes:

    if not len(silhouette.polygons()) == 1:

        segs = [(p1,p2) for poly in silhouette.allpolygons() for (p1,p2) in pairs(poly.lengthsamples(5.0))]

        puts("interseg computation")
        intersegs = IntersectionBuilder().intersectionsegs(segs)

        puts("edgegraph computation")
        eg = EdgeGraph().loadwithpointpairs(intersegs)
        polygons = [Polygon(points) for points in eg.closedpolygons()]

        for poly in polygons:
            ccolor = rcolor.next()
            canvas.draw(poly,ccolor)
            canvas.draw(poly.symx(symx),ccolor)

    else:
        canvas.draw(silhouette.polygons()[0],rcolor.next())

canvas.save("main_svglayer.png")
