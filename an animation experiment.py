from turtle import forward, backward, right, update, clear, tracer, hideturtle, pensize
from time import sleep
tracer(3,100); hideturtle(); pensize(3)
while True: forward(250); backward(250); right(1); update(); clear(); sleep(1/60)
