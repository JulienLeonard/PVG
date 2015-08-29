from basics import *

#
# define a range object
#
class R:
    def __init__(self,v1,v2):
        self.mv1 = v1
        self.mv2 = v2

    def v1(self,v=""):
        if not v == "":
            self.mv1 = v
            return self
        else:
            return self.mv1

    def v2(self,v=""):
        if not v == "":
            self.mv2 = v
            return self
        else:
            return self.mv2

    def minv(self):
        return min(self.v1(),self.v2())

    def maxv(self):
        return max(self.v1(),self.v2())

    def sample(self,t):
        if t < 0.0 or t > 1.0:
            return None
        if t < 0.0:
            t = 0.0
        if t > 1.0:
            t = 1.0
        return sample((self.mv1,self.mv2),t)

    def samples(self,nsamples):
        return [self.sample(t) for t in usamples(nsamples)]

    def v(self,t):
        return sample((self.mv1,self.mv2),t)

    def abscissa(self,t):
        if t < self.minv() or t > self.maxv():
            return None
        return abscissa((self.mv1,self.mv2),t)

    def contain(self,t):
        if self.mv1 <= self.mv2:
            if self.mv1 <= t and t <= self.mv2:
                return True
            else:
                return False
        else:
            if self.mv1 >= t and t >= self.mv2:
                return True
            else:
                return False

#
# define a multi range object by spec [(a1,v1),(a2,v2),...,(an,vn)]
#
class MR:
    def __init__(self,vlist):
        self.mvlist = vlist

    def sample(self,t):
        return multisamples(self.mvlist,t)

    
    
