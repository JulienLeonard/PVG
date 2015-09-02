from geoutils import *
from quadtree import *

class GeoMatcher:

    def checksegments(self,segs):
        pointindices = {}
        points = {} 
        index = 0
        for seg in segs:
            for p in seg:
                if not p in pointindices:
                    # print "point",p,"index",index
                    pointindices[p] = index
                    points[index] = p
                    index += 1
            
        pbbox     = points2bbox(pointindices.keys())
        differror = pbbox.size()/10000.0
        # print "differror",differror
        quadtree = QuadTree(pbbox)
        sames = {}
        for i in points.keys():
            sames[i] = [i]
        for p in pointindices.keys():
            newcircle = Circle(p,differror) 
            ccircles = quadtree.colliding(newcircle)
            # print "ccircle",p[0],p[1],ccircles
            if len(ccircles):
                i = pointindices[p]
                for ccircle in ccircles:
                    op = ccircle.center()
                    oi = pointindices[op]
                    sames[oi].append(i)
                    sames[i].append(oi)
                    # print "same",points[i],points[oi]
            quadtree.add(newcircle)
                    
        for i in points.keys():
            sames[i] = lmin(sames[i])
            # print "point",points[i],"same",points[sames[i]]

        result = []
        for seg in segs:
            p1,p2 = seg
            i1,i2 = pointindices[p1],pointindices[p2]
            s1,s2 = sames[i1],sames[i2]
            np1,np2 = points[s1],points[s2]
            # print "geomatcher seg",p1,p2,"gives",np1,np2
            result.append((np1,np2))
        return result
        
