import sys
sys.path.insert(0, './../lib')

from canvas  import *
import color

render = Canvas("main_canvas.ppm").background(color.red()).render()
render.drawcircle(Circle())
render.end()
