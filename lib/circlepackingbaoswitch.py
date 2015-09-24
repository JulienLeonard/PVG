from utils            import *
from circlepackingbao import *
from baopattern       import *

def index2color(period,index):
    return color.hue2color((index%period)/(float(period)))

#
# TODO: do proper inheritance of constructor
#
class BaoPatternSwitch(BaoPattern):
    def __init__(self):
        self.msidepattern   = [1.0]
        self.mradiuspattern = [1.0]
        self.mcolorpattern  = [Color.black()]
        self.mindex   = 0

    #
    # return (Side,RatioRadius,Color)
    #
    def next(self):
        self.mindex += 1
        return self

    def side(self):
        return lcircular(self.msidepattern,self.mindex)    

    def sidepattern(self,sidepattern):
        self.msidepattern = sidepattern
        return self


class BS:
    def __init__(self):
        self.mlist = []

    def push(self,ntimes):
        lastside = 1.0
        if len(self.mlist) > 0:
            lastside = -self.mlist[-1]
        self.mlist = lconcat(self.mlist,lrepeat([lastside],ntimes))
        return self

    def list(self):
        return self.mlist

    def alts(self,list):
        for item in list:
            self.push(item)
        return self
        

class CirclePackingBaoSwitch(CirclePackingBao):
    
    @staticmethod
    def iter(boundaries,nodes,baopattern,niter):
        stack       = BaoStack(nodes)
        lastindex   = stack.lastindex()
        quadtree    = QuadTree().adds( boundaries + nodes )
        lastside    = None

        for iiter in range(niter):
            ifputs(iiter % 1000 == 0,"niter",iiter)

            # get current paramaters
            newside              = baopattern.next().side()
            if not (newside == lastside or lastside == None):
                stack.switch()
            (lastnode,othernode) = stack.lastseed()
            newr                 = baopattern.radius()

            # compute new node if possible
            newbaonode = None

            for othernode in CirclePackingBao.genothernodes(othernode,quadtree,lastnode,stack,newr):
                # puts("genothernodes",lastnode,othernode)
                newbaonode = CirclePackingBao.computenextnode(quadtree,lastnode,othernode,newr,stack.newindex(),newside)
                if not newbaonode == None:
                    break

            # update according to result
            if newbaonode == None:
                lastnode.notfound(True)
                lastindex = stack.rewindtofreenode(lastindex)
            else:
                othernode.retouch(True)
                quadtree.add(newbaonode)
                baopattern.draw(newbaonode,newbaonode.colorindex())
                lastindex = stack.stack(newbaonode,othernode)

            if lastindex < 1:
                break

            lastside = newside
            
        return stack.nodes()
