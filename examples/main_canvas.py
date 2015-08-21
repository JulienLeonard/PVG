import sys
sys.path.insert(0, './../lib')

from canvas import *
from color  import *

render = Canvas("main_canvas.png").background(Color.red()).render()
render.drawcircle(Circle())
render.end()
