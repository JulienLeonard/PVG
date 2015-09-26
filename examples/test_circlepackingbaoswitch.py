from PVG     import *
from PVGPACK import *

render = Canvas("test_circlepackingbaoswitch.png").render()

def myfdraw(node,index,style):
    render.drawcircle( cscale( node, 0.9), style )
    

rpattern = [item for i in range(10,100) for item in [1.0] * i + [2.0]]
cpattern = [item for i in range(10,100) for item in [Color.black()] * i + [Color.red()]]

baopattern = BaoPatternSwitch().fdraw(myfdraw).sidepattern([1.0]).radiuspattern(rpattern).colorpattern(cpattern)

result = CirclePackingBaoSwitch().iter(900,[],baonodes0(),baopattern)

render.end()
