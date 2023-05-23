import turtle
import time
# reset everything in turtle module
turtle.reset()
turtle.tracer(0)
turtle.pensize(2)
turtle.forward(10)
# make a circle with python
for i in range(72):
    turtle.circle(100)
    turtle.right(1)
    turtle.forward(1)
    turtle.right(4)
# hide
turtle.hideturtle()
# delay 2 second
time.sleep(2)
# delete all
turtle.clear()
# show
turtle.showturtle()
# make a square with python
for i in range(72):
    for i in range(4):
        turtle.forward(200)
        turtle.left(90)
    turtle.right(1)
    turtle.forward(1)
    turtle.right(4)
# hide
turtle.hideturtle()
# delay 2 second
time.sleep(2)
# delete all
turtle.clear()
# show
turtle.showturtle()
# make a triangle with python
for i in range(72):
    for a in range(3):
        turtle.forward(200)
        turtle.left(120)
    turtle.right(1)
    turtle.forward(1)
    turtle.right(4)
# hide
turtle.hideturtle()
# delay 2 second
time.sleep(2)
# delete all
turtle.clear()
# show
turtle.showturtle()
# make a pentagon with python
for i in range(72):
    for b in range(5):
        turtle.forward(200)
        turtle.left(72)
    turtle.right(1)
    turtle.forward(1)
    turtle.right(4)
# hide
turtle.hideturtle()
# delay 2 second
time.sleep(2)
# delete all
turtle.clear()
# show
turtle.showturtle()
# make a star parttern with python
turtle.left(180)
for b in range(72):
    for c in range(5):
        turtle.forward(250)
        turtle.left(144)
    turtle.right(1)
    turtle.forward(1)
    turtle.right(4)
# hide
turtle.hideturtle()
# delay 2 second
time.sleep(2)
# delete all
turtle.clear()
# show
turtle.showturtle()
# set the turtle to the center of the screen
turtle.left(180)
# write a sentence with python size 48 and in the middle
turtle.write("I love Python.", font=(
    "Bahnschrift Light Condensed", 48, "normal"), align="center")
# hide
turtle.hideturtle()
# delay 2 second
time.sleep(2)
# delete all
turtle.clear()
# done the script
turtle.done()
