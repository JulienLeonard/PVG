from utils     import *
from tangentutils import *

class CircleCrown:
    def __init__(self,circleadj):
        self.mcircleadj = circleadj

    def crown(self,seeds,ndeep,avoid=[]):
        fronts = seeds[:]
        avoid = seeds[:]
        for i in range(ndeep):
            newfronts = []
            for front in fronts:
                for adj in self.mcircleadj.adjcircles(front):
                    if not adj in avoid:
                        newfronts.append(adj)
                        avoid.append(adj)
            avoid = fronts[:]
            avoid.extend(newfronts[:])
            fronts = newfronts
        return fronts

    def allcrowns(self,seeds):
        result = [seeds[:]]
        fronts = seeds[:]
        avoid = seeds[:]
        while (len(fronts) != 0):
            newfronts = []
            for front in fronts:
                for adj in self.mcircleadj.adjcircles(front):
                    if not adj in avoid:
                        newfronts.append(adj)
                        avoid.append(adj)
            result.append(newfronts[:])
            avoid = fronts[:]
            avoid.extend(newfronts[:])
            fronts = newfronts
        return result

    def allcrowns2(self,seeds,nmax):
        result = [seeds[:]]
        fronts = seeds[:]
        avoid = seeds[:]
        for i in range(nmax):
            newfronts = []
            for front in fronts:
                for adj in self.mcircleadj.adjcircles(front):
                    if not adj in avoid:
                        newfronts.append(adj)
                        avoid.append(adj)
            result.append(newfronts[:])
            avoid = fronts[:]
            avoid.extend(newfronts[:])
            fronts = newfronts
        return result


class CircleAdj:
    def __init__(self):
        self.mcircles = {}
        self.mcircles["list"] = []

    def addcircleadj(self,circle1,circle2):
        if not circle1 in self.mcircles:
            self.mcircles["list"].append(circle1)
            self.mcircles[circle1] = []
        if not circle2 in self.mcircles:
            self.mcircles["list"].append(circle2)
            self.mcircles[circle2] = []
        if not circle2 in self.mcircles[circle1] and not circle1 == circle2:
            self.mcircles[circle1].append(circle2)
        if not circle1 in self.mcircles[circle2] and not circle1 == circle2:
            self.mcircles[circle2].append(circle1)

    def adjcircles(self,circle):
        if not circle in self.mcircles:
            return []
        return self.mcircles[circle]

    def circles(self,value = None):
        if value == None:
            return self.mcircles["list"][:]
        else:
            for (c1,c2) in pairs(value):
                self.addcircleadj(c1,c2)
            return self

    def completeadjacency(self,added,candidates):
        for adj in candidates:
            if arecirclestangent(adj,added) and not adj == added and not added in self.adjcircles(adj):
                self.addcircleadj(adj,added)

    def sortedadjcircles(self,circle):
        return self.adjorder(circle,self.adjcircles(circle))

    def adjorder(self,root,circles):
        # compute each angle foreach adj circle center, and order them
        sortlist = []
        for c in circles:
            v = vector(ccenter(c),ccenter(root))
            angle = vangle(v)
            if angle < 0.0:
                angle += 3.14159 * 2.0
            sortlist.append((angle,c))
        sortlist.sort()
        # puts("sortlist",sortlist)
        return [i[1] for i in sortlist]

    def alladjacencies(self):
        result = []
        for circle1 in self.mcircles["list"]:
            for circle2 in self.mcircles[circle1]:
                if not (circle2,circle1) in result:
                    result.append((circle1,circle2))
        return result

        
class CADJ:
    def __init__(self,c0,c1,side):
        self.c0 = c0
        self.c1 = c1
        self.side = side

    def newcircle(self,radius):
        return circles2tangent(self.c0,"OUT",self.c1,"OUT",radius,self.side)


def computeadj(nodes,sensitivity = 0.01):
    result = CircleAdj()
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if arecirclestangent(nodes[i],nodes[j],sensitivity):
                # puts("nodes",nodes[i],nodes[j],"adjacent")
                result.addcircleadj(nodes[i],nodes[j])
    return result
