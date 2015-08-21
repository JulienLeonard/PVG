# some_file.py
import sys
sys.path.insert(0, './../lib')

from   utils       import *
from   renderCairo import *
import color

outputfilepath = defaultoutputdir() + "/" + "drawcircle.png"
render = RenderCenter(ImageDim(1000,1000),outputfilepath)
render.drawcircle(C0)
render.end()
