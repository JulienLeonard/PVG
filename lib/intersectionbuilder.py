from geoutils import *
from quadtree import *

class IntersectionBuilder:
    def intersectionpoints(self,segs):
        result = []
        for i in range(len(segs)):
            seg1 = segs[i]
            for j in range(i+1,len(segs)):
                seg2 = segs[j]
                inter = Segment.intersection(seg1,seg2)
                if not inter == None:
                    result.append(inter)
        return result

    def intersectionsegs(self,segs):
        seginters = {}
        for i in range(len(segs)):
            seg1 = segs[i]
            if not seg1 in seginters.keys():
                seginters[seg1] = []
            for j in range(i+1,len(segs)):
                seg2 = segs[j]
                inter = Segment.intersection(seg1,seg2)
                if not inter == None:
                    # print "new point inter",inter.coords(),"seg1",seg1.coords(),"seg2",seg2.coords()
                    if not seg2 in seginters.keys():
                        seginters[seg2] = []                        
                    seginters[seg1].append(inter)
                    seginters[seg2].append(inter)
        
        result = []
        for seg in seginters.keys():
            inters = [seg.p1()]
            inters.extend(seginters[seg])
            inters.append(seg.p2())
            inters = [(vector(seg.p1(),inter).length2(),inter) for inter in inters]
            inters.sort()
            for i1,i2 in pairs(inters):
                if vector(i2[1],i1[1]).length() > 0.0000001:
                    # print "new seg after inter",i1[1],i2[1]
                    result.append(Segment(i1[1],i2[1]))
        return Segment.sort(result)

    def intersectionsegs2(self,segs):
        seginters = {}
        quadtree = QuadTree()
        for i in range(len(segs)):
            seg1  = segs[i]
            if not seg1 in seginters.keys():
                seginters[seg1] = []
            seg2s = quadtree.colliding(seg1)
            for seg2 in seg2s:
                inter = Segment.intersection(seg1,seg2)
                if len(inter):
                    # print "new point inter",inter,"seg1",seg1,"seg2",seg2
                    if not seg2 in seginters.keys():
                        seginters[seg2] = []                        
                    seginters[seg1].append(inter)
                    seginters[seg2].append(inter)
            quadtree.add(seg1)
        
        result = []
        for seg in seginters.keys():
            inters = [seg.p1()]
            inters.extend(seginters[seg])
            inters.append(seg.p2())
            inters = [(vector(seg.p1(),inter).length2(),inter) for inter in inters]
            inters.sort()
            for i1,i2 in pairs(inters):
                if abs(i2[0]-i1[0]) > 0.000000001:
                    # print "new seg after inter",i1[1],i2[1]
                    result.append(Segment(i1[1],i2[1]))
        return result
