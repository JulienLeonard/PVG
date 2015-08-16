# some_file.py
import sys
sys.path.insert(0, './../lib')

from utils     import *
from drawutils import *
import color
from circlepackingbaoswitch import *
from baopattern import *

def myfdraw(render,pattern,lastindex,newcolor):
    render.drawcircle( cscale( pattern.lastnode(), 0.9), newcolor )
    
render = RenderCenter((1000,1000),"C:/DEV/PVG/output/test_circlepackingbaoswitch.ppm")

rpattern = [item for i in range(10,100) for item in [1.0] * i + [2.0]]
cpattern = [item for i in range(10,100) for item in [color.black()] * i + [color.red()]]

baopattern = BaoPattern().sidepattern([1.0]).radiuspattern(rpattern).colorpattern(cpattern)

result = CirclePackingBaoSwitch(nodes0(),baopattern,myfdraw).iter(render,nodes0(),900)

render.end()
