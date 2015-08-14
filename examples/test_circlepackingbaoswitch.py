# some_file.py
import sys
sys.path.insert(0, './../lib')

from utils     import *
from drawutils import *
import color
from circlepackingbaoswitch import *

def myfdraw(render,pattern,lastindex):
    render.drawcircle( cscale( pattern.lastnode(), 0.9), index2color(300,lastindex) )
    
render = RenderCenterSVG((1000,1000),"../output/test_circlepackingbaoswitch.svg",color.black())

nradiuss = ldoublesym(samples((0.1,0.2),3))

sidepattern = [1.0] * 3 + [-1] * 3

result = CirclePackingBaoSwitch(sidepattern,nradiuss,nodes0(),myfdraw).iter(render,nodes0(),90)

render.end()
