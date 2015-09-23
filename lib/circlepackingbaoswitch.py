from utils            import *
from circlepackingbao import *
from baopattern       import *

def index2color(period,index):
    return color.hue2color((index%period)/(float(period)))


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


class BaoStackSwitch(BaoStack):

    def switch(self):
        self.mlastnode     = self.mlastnode
        self.mothernode    = self.mlastlastnode
        self.mlastlastnode = None
        self.mlast3node    = None
        

class CirclePackingBaoSwitch(CirclePackingBao):
    
    @staticmethod
    def iter(boundaries,nodes,baopattern,niter):
        stack       = BaoStackSwitch(nodes)
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
                newbaonode = CirclePackingBao.computenextnode(quadtree,lastnode,othernode,newr,stack.newindex())
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
