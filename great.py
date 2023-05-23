import turtle
import time
#reset everything in turtle module
turtle.reset()
turtle.speed(0)
turtle.pensize(2)
turtle.hideturtle()
turtle.tracer(0)
#make a circle with python
for i in range(90):
    turtle.circle(100)
    turtle.right(4)
turtle.update()
#delay 2 second
time.sleep(2)
#delete all
turtle.clear()
#make a square with python
for i in range(90):
    for i in range(4):
        turtle.forward(200)
        turtle.left(90)
    turtle.left(4)
turtle.update()
#delay 2 second
time.sleep(2)
#delete all
turtle.clear()
#make a triangle with python
for i in range(90):
    for a in range(3):
        turtle.forward(200)
        turtle.left(120)
    turtle.left(4)
turtle.update()
#delay 2 second
time.sleep(2)
#delete all
turtle.clear()
#make a pentagon with python
for i in range(90):
    for b in range(5):
        turtle.forward(200)
        turtle.left(72)
    turtle.left(4)
turtle.update()
#delay 2 second
time.sleep(2)
#delete all
turtle.clear()
#make a star parttern with python
turtle.left(180)
for b in range(90):
    for c in range(5):
        turtle.forward(250)
        turtle.left(144)
    turtle.left(4)
turtle.update()
#delay 2 second
time.sleep(2)
#delete all
turtle.clear()
#set the turtle to the center of the screen
turtle.left(180)
turtle.update()
#animation
x = 0
for a in range(100):
    for i in range(11):
        x = x - 0.5
        turtle.penup()
        turtle.setpos(x, 0)
        turtle.pendown()
        turtle.write("I love Python.", font=("Arial", 48, "normal"), align="center")
        turtle.update()
        turtle.clear()
        time.sleep(1/60)
    for j in range(11):
        x = x + 0.5
        turtle.penup()
        turtle.setpos(x, 0)
        turtle.pendown()
        turtle.write("I love Python.", font=("Arial", 48, "normal"), align="center")
        turtle.update()
        turtle.clear()
        time.sleep(1/60)
turtle.write("Click to exit",font=("Arial", 32, "normal"),align="center")
turtle.exitonclick()

