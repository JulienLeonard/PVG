from geoutils import *
from circle   import *
from quadtree import *

class GeoMatcher:

    def checksegments(self,segs):
        points    = [p for seg in segs for p in seg.points()]
        # puts("GeoMatcher points",points)

        pbbox     = points2bbox(points)
        differror = pbbox.size()/5000.0

        quadtree = QuadTree(pbbox)
        sames = {}
        for point in points:
            if not point in sames:
                sames[point] = [point]
                newcircle = Circle(point,differror) 
                ccircles = quadtree.colliding(newcircle)
                for ccircle in ccircles:
                    opoint = ccircle.center()
                    sames[opoint].append(point)
                    sames[point].append(opoint)
                quadtree.add(newcircle)

        newpoints = {}
        for point in sames.keys():
            #puts("point",point,"coords",point.coords(),"same",sames[point])
            if len(sames[point]) > 1: 
                if not point in newpoints:
                    newpoint = pmiddle(sames[point])
                    for p in sames[point]:
                        newpoints[p] = newpoint
            else:
                newpoints[point] = point

        #for point in newpoints.keys():
        #    puts("point key",point,"coords",point.coords(),"newpoint",newpoints[point],"coords",newpoints[point].coords())

        segexts = {}
        for seg in segs:
            if not newpoints[seg.p1()] == seg.p1() or not newpoints[seg.p2()] == seg.p2():
                newseg = Segment(newpoints[seg.p1()],newpoints[seg.p2()])
            else:
                newseg = seg

            if not newseg.p1() == newseg.p2() and not (newseg.p1(),newseg.p2()) in segexts and not (newseg.p2(),newseg.p1()) in segexts:
                segexts[(newseg.p1(),newseg.p2())] = newseg

        return segexts.values()
        
