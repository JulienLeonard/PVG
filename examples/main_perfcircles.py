from PVG import *

render = Canvas("main_perfcircles.png").render()

for i in range(100000):
    if i % 1000 == 0:
        puts("i",i)
    render.drawcircle(Circle(Point(rand(),rand()),0.1),Color.rand(0.1))

puts("dump picture")
render.end()
