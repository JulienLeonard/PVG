from basics import *
from geoutils import *

class R:
    def __init__(self,v1,v2):
        self.mv1 = v1
        self.mv2 = v2

    def sample(self,t):
        return sample((self.mv1,self.mv2),t)

    def v(self,t):
        return sample((self.mv1,self.mv2),t)

    def fit(self,t):
        return rangefit((self.mv1,self.mv2),t)

    def abscissa(self,t):
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

class MR:
    def __init__(self,vlist):
        self.mvlist = vlist

    def sample(self,t):
        return multisamples(self.mvlist,t)

class PR:
    def __init__(self,v1,v2):
        self.mv1 = v1
        self.mv2 = v2

    def sample(self,t):
        return psample((self.mv1,self.mv2),t)
    
    
