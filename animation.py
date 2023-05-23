from turtle import *
from time import sleep
title("Simple animation"); tracer(0); hideturtle(); pensize(3); radius = 5
while True:
    if radius != 150:
        begin_fill()
        circle(radius)
        end_fill()
        update()
        radius = radius + 1
        clear()
        sleep(1/60)
    if radius == 150:
        for b in range(146):
            begin_fill()
            circle(radius)
            end_fill()
            update()
            radius = radius - 1
            clear()
            sleep(1/60)
