# some_file.py
import sys
sys.path.insert(0, './../lib')

from utils import *


p = Point().coords()
print p
v = Vector().coords()
print v
c = Circle().coords()
print c
print Point().coords((1.0,2.0)).addv(Vector(3.0,4.0)).coords()



