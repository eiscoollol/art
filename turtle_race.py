import turtle as t, random as r, time as tm
t.tracer(0)
t.penup()
t.hideturtle()
t1 = t.Turtle()
t2 = t.Turtle()
t2.penup()
t1.penup()
t2.setpos(0, -100)
t2.shape("turtle")
t1.shape("turtle")
t1.color("green")
t2.color("blue")
t.setpos(500, 100)
t.right(90)
t.pendown()
t.forward(300)
t.update()
t.tracer(1)
i = 1
while i == 1:
        if t1.xcor() >= 500:
                t.clearscreen()
                t.write("Green turtle win!", font=("Arial", 32, "normal"), align="center")
                i += i
        if t2.xcor() >= 500:
                t.clearscreen()
                t.write("Blue turtle win!", font=("Arial", 32, "normal"), align="center")
                i += i
        tm.sleep(0.5)
        for k in range(r.randint(1, 10)):
                t1.forward(1)
        tm.sleep(0.5)
        for j in range(r.randint(1, 10)):
                t2.forward(1)
t.exitonclick()
