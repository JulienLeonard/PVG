import sys
sys.path.insert(0, './../lib')

from utils      import *
from canvas     import *
from SVGparser  import *
from silhouette import *
from color      import *

render = Canvas("main_perfimage.png").size(18000).render()

for i in range(100):
    render.drawcircle(Circle(Point(rand(),rand()),0.1),Color.rand(0.1))

render.end()
