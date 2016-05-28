from utils     import *
from tangentutils3D import *

# class CircleCrown:
#     def __init__(self,circleadj):
#         self.mcircleadj = circleadj

#     def crown(self,seeds,ndeep,avoid=[]):
#         fronts = seeds[:]
#         avoid = seeds[:]
#         for i in range(ndeep):
#             newfronts = []
#             for front in fronts:
#                 for adj in self.mcircleadj.adjcircles(front):
#                     if not adj in avoid:
#                         newfronts.append(adj)
#                         avoid.append(adj)
#             avoid = fronts[:]
#             avoid.extend(newfronts[:])
#             fronts = newfronts
#         return fronts

#     def allcrowns(self,seeds):
#         result = [seeds[:]]
#         fronts = seeds[:]
#         avoid = seeds[:]
#         while (len(fronts) != 0):
#             newfronts = []
#             for front in fronts:
#                 for adj in self.mcircleadj.adjcircles(front):
#                     if not adj in avoid:
#                         newfronts.append(adj)
#                         avoid.append(adj)
#             result.append(newfronts[:])
#             avoid = fronts[:]
#             avoid.extend(newfronts[:])
#             fronts = newfronts
#         return result

#     def allcrowns2(self,seeds,nmax):
#         result = [seeds[:]]
#         fronts = seeds[:]
#         avoid = seeds[:]
#         for i in range(nmax):
#             newfronts = []
#             for front in fronts:
#                 for adj in self.mcircleadj.adjcircles(front):
#                     if not adj in avoid:
#                         newfronts.append(adj)
#                         avoid.append(adj)
#             result.append(newfronts[:])
#             avoid = fronts[:]
#             avoid.extend(newfronts[:])
#             fronts = newfronts
#         return result


class SphereAdj:
    def __init__(self):
        self.mspheres = {}
        self.mspheres["list"] = []

    def addsphereadj(self,sphere1,sphere2):
        if not sphere1 in self.mspheres:
            self.mspheres["list"].append(sphere1)
            self.mspheres[sphere1] = []
        if not sphere2 in self.mspheres:
            self.mspheres["list"].append(sphere2)
            self.mspheres[sphere2] = []
        if not sphere2 in self.mspheres[sphere1] and not sphere1 == sphere2:
            self.mspheres[sphere1].append(sphere2)
        if not sphere1 in self.mspheres[sphere2] and not sphere1 == sphere2:
            self.mspheres[sphere2].append(sphere1)

    def adjspheres(self,sphere):
        if not sphere in self.mspheres:
            return []
        return self.mspheres[sphere]

    def spheres(self,value = None):
        if value == None:
            return self.mspheres["list"][:]
        else:
            for (c1,c2) in pairs(value):
                self.addsphereadj(c1,c2)
            return self

    def completeadjacency(self,added,candidates):
        for adj in candidates:
            if arespherestangent(adj,added) and not adj == added and not added in self.adjspheres(adj):
                self.addsphereadj(adj,added)

    # def sortedadjspheres(self,sphere):
    #     return self.adjorder(sphere,self.adjspheres(sphere))

    # def adjorder(self,root,spheres):
    #     # compute each angle foreach adj sphere center, and order them
    #     sortlist = []
    #     for c in circles:
    #         v = vector(ccenter(c),ccenter(root))
    #         angle = vangle(v)
    #         if angle < 0.0:
    #             angle += 3.14159 * 2.0
    #         sortlist.append((angle,c))
    #     sortlist.sort()
    #     # puts("sortlist",sortlist)
    #     return [i[1] for i in sortlist]

    def alladjacencies(self):
        result = []
        for sphere1 in self.mspheres["list"]:
            for sphere2 in self.mspheres[sphere1]:
                if not (sphere2,sphere1) in result:
                    result.append((sphere1,sphere2))
        return result

        
class CADJ3D:
    def __init__(self,s0,s1,s2,side):
        self.s0 = s0
        self.s1 = s1
        self.s2 = s2
        self.side = side

    def newsphere(self,radius):
        return adjsphere(self.s0,self.s1,self.s2,radius,self.side)


def computeadj3D(nodes,sensitivity = 0.01):
    result = SphereAdj()
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if arespherestangent(nodes[i],nodes[j],sensitivity):
                # puts("nodes",nodes[i],nodes[j],"adjacent")
                result.addsphereadj(nodes[i],nodes[j])
    return result
