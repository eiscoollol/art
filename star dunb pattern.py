import turtle
turtle.reset()
turtle.speed(0)
turtle.title("Star with a pattern")
def startfunc():
    turtle.penup()
    turtle.setpos(-100, 0)
    turtle.pendown()
    turtle.forward(100)
    turtle.left(70)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.left(74)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.left(70)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.left(75)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.left(70)
    turtle.forward(100)
    turtle.hideturtle()
startfunc()
turtle.clear()
for i in range(50):
    startfunc()
    turtle.left(360/50)
