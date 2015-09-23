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

    def middle(self):
        return (self.mv1+self.mv2)/2.0

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

    def samples(self,nsamples=None,abscissas=None):
        if not nsamples == None:
            return [self.sample(t) for t in usamples(nsamples)]
        if not abscissas == None:
            return [self.sample(t) for t in abscissas]
        return None

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

    def rand(self,niter = None):
        if niter == None:
            return self.sample(rand())
        else:
            return [self.sample(rand()) for i in range(niter)]

    def trim(self,v):
        if v < self.minv():
            return self.minv()
        if v > self.maxv():
            return self.maxv()
        return v

    def symsample(self,t):
        if t <= 0.5:
            return self.sample(t * 2.0)
        else:
            return self.sample(2.0 * (1.0 - t))

    def symsamples(self,nsamples=None,abscissas=None):
        if not nsamples == None:
            return [self.symsample(t) for t in usamples(nsamples)]
        if not abscissas == None:
            return [self.symsample(t) for t in abscissas]
        return None
        

    #
    # define angle range
    #
    @staticmethod
    def angle():
        return R(0.0,2* math.pi)


#
# define a multi range object by spec [(a1,v1),(a2,v2),...,(an,vn)]
#
class MR:
    def __init__(self,vlist):
        self.mvlist = vlist

    def sample(self,t):
        return multisamples(self.mvlist,t)

    
    
