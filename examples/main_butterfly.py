# some_file.py
import sys
sys.path.insert(0, './../lib')

from utils  import *
from canvas import *
from SVGparser import *
from color  import *
from circlepackingbaoswitch import *
from baopattern import *

def myfdraw(render,pattern,lastindex,newcolor):
    render.drawcircle( cscale( pattern.lastnode(), 0.9), newcolor )
    
render = Canvas("main_butterfly.png").render()

butterpoly = svgPaths("butterfly_sym.svg")[0].silhouette().polygon()

render.drawpolygon(butterpoly)

# render.drawcircle(Circle(butterpoly.middle(),10.0),Color.red())

render.drawcircles([CircleNode().coords(Circle(p,1.0).coords()) for p in butterpoly.samples(2000)],Color.red())

rpattern = [item for i in range(10,100) for item in [2.0] * i + [4.0]]
cpattern = [item for i in range(10,100) for item in [Color.white()] * i + [Color.red()]]

baopattern = BaoPattern().sidepattern([1.0]).radiuspattern(rpattern).colorpattern(cpattern)

rootnodes = circle2nodepair(Circle(butterpoly.middle(),2.0))

render.drawcircles(rootnodes,Color.green())

result = CirclePackingBaoSwitch(rootnodes,baopattern,myfdraw).iter(render,rootnodes  + [CircleNode().coords(Circle(p,1.0).coords()) for p in butterpoly.samples(1000)],10900)

render.end()
