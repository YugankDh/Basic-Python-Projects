import turtle as t
t.color("black","black")
t.speed(10)
t.pensize(3)
t.penup()
t.goto(0,201)
t.pendown()
t.begin_fill()
t.circle(-203)
t.end_fill()
t.color("red","red")
t.begin_fill()
t.right(125)
t.penup()
t.goto(0,202)
t.pendown()
for i in range(36):
    t.forward(12)
    t.left(2)
t.left(108)
for i in range(36):
    t.forward(12)
    t.left(2)
t.end_fill()
t.penup()
t.goto(-180,90)
t.left(170)
t.pendown()
t.begin_fill()
for i in range(36):
    t.forward(12)
    t.left(2)
t.left(108)
for i in range(36):
    t.forward(12)
    t.left(2)
t.end_fill()
t.penup()
t.goto(-179,-100)
t.right(196)
t.pendown()
t.begin_fill()
for i in range(36):
    t.forward(12)
    t.left(2)
t.left(108)
for i in range(36):
    t.forward(12)
    t.left(2)
t.end_fill()
t.penup()
t.left(115)
t.right(125)
t.color("black","black")
t.goto(0,200)
t.pensize(7)
t.pendown()
for i in range(36):
    t.forward(12)
    t.left(2)
t.left(108)
for i in range(36):
    t.forward(12)
    t.left(2)
t.penup()
t.goto(-180,90)
t.left(170)
t.pendown()
for i in range(36):
    t.forward(12)
    t.left(2)
t.left(108)
for i in range(36):
    t.forward(12)
    t.left(2)
t.penup()
t.goto(-179,-100)
t.right(196)
t.pendown()
for i in range(36):
    t.forward(12)
    t.left(2)
t.left(108)
for i in range(36):
    t.forward(12)
    t.left(2)
t.penup()
t.goto(-25,10)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()
t.hideturtle()












t.done()
