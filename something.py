import turtle
a = 10
turtle.speed(0)
turtle.pensize(0.1)
turtle.bgcolor("black")
turtle.pencolor("cyan")
for i in range(360):
    turtle.circle(a)
    a = a + 1
    turtle.left(5)
turtle.hideturtle()
