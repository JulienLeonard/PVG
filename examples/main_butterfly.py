import sys
sys.path.append("../lib/")
from PVG     import *
from PVGPACK import *
from canvascairo import *

#
# TODO: DEBUG as computing too long
#
def myfdraw(render,pattern,lastindex,newcolor):
    render.drawcircle( cscale( pattern.lastnode(), 0.9), newcolor )
    
render = Canvas("main_butterfly.png").render()

butterpoly = svgPaths("butterfly_sym.svg")[0].polygons()[0]

render.drawpolygon(butterpoly)

render.drawcircles([Circle(p,1.0) for p in butterpoly.samples(2000)],Color.red())

rpattern = [item for i in range(10,100) for item in [2.0] * i + [4.0]]
cpattern = [item for i in range(10,100) for item in [Color.white()] * i + [Color.red()]]

baopattern = BaoPatternSwitch().fdraw(myfdraw).sidepattern([1.0]).radiuspattern(rpattern).colorpattern(cpattern)

rootnodes = BaoNode.fromcircle(Circle(butterpoly.middle(),2.0))

render.drawcircles(rootnodes,Color.green())

result = CirclePackingBaoSwitch().iter(10900,butterpoly.segments(),rootnodes,baopattern)

render.end()
