from PVG import *

render = Canvas("main_perfimage.png").size(18000).render()

for i in range(100):
    render.drawcircle(Circle(Point(rand(),rand()),0.1),Color.rand(0.1))

render.end()
