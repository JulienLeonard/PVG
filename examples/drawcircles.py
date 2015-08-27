from PVG import *

Canvas().draw([Circle(P0,r) for r in usamples(10)],Color.black(0.1)).save("circles.png")

