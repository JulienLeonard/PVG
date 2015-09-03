from PVG              import *
from circlepackingbao import *

canvas = Canvas().size(10000).background(Color.grey(0.9))
parser = SVGParser().parse("halfbutterfly.svg")
silhouettes = [layer.silhouette() for layer in parser.layers()]
rcolor = Roller([])

sortlist = []
for silhouette in silhouettes:
    for level in range(2):
        for poly in silhouette.polygons(level):
            sortlist.append((poly.middle().x(),poly))

sortlist.sort()
symx      = sortlist[-1][0]
nosym     = sortlist[-1][1]


def lowercirclepair(circlestring):
    miny = circlestring[0].y()
    result = [circlestring[0],circlestring[1]]
    for (c1,c2) in pairs(circlestring[1:]):
        if c1.y() > miny:
            miny = c1.y()
            result = [c1,c2]
    return result


def drawcell(render,polygon,sym = True):
    puts("drawcell",polygon)
    drawings = []

    polygon = polygon.clockwise()

    def myfdraw(lastnode,lastindex,newcolor):
        newdrawing = (cscale( lastnode, 0.9),newcolor)
        drawings.append(newdrawing)
        canvas.draw( newdrawing[0], newdrawing[1] )

    # rootnodes = circle2nodepair(Circle(polygon.middle(),2.0))

    rpattern = [item for i in range(10,100) for item in [0.25] * i + [0.5]]
    cpattern = [Color.hue2color(float(index)/20.0) for index in range(20)]

    baopattern = BaoPattern().radiuspattern(rpattern).colorpattern(cpattern).fdraw(myfdraw)

    # render.drawcircles(rootnodes,Color.green())
    boundaries = [Circle(p,0.25) for p in polygon.lengthsamples(0.5)]
    rootnodes  = lreverse([c.scale(1.5) for c in lowercirclepair(boundaries)])

    canvas.draw(boundaries,Color.green())
    canvas.draw(rootnodes,Color.red())

    result = CirclePackingBao().iter(boundaries,rootnodes,baopattern,20)


for silhouette in silhouettes:

    if not len(silhouette.polygons()) == 1:

        segs = [(p1,p2) for poly in silhouette.allpolygons() for (p1,p2) in pairs(poly.lengthsamples(5.0))]

        puts("interseg computation")
        intersegs = IntersectionBuilder().intersectionsegs(segs)

        puts("edgegraph computation")
        eg = EdgeGraph().loadwithpointpairs(intersegs)
        polygons = [Polygon(points) for points in eg.closedpolygons()]

        for poly in polygons:
            drawcell(canvas,poly)
            break
    else:
        canvas.draw(silhouette.polygons()[0],Color.black())
        drawcell(canvas,silhouette.polygons()[0],False)
    break


canvas.save("main_skybutterfly.png")
