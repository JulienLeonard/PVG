from basics import *

#
# object to define an infinite circular enum for a list
#
class Roller:
    def __init__(self,input):
        self.minput = input
        self.mindex = 0

    def next(self):
        self.mindex += 1
        return circular(self.minput,self.mindex-1)
