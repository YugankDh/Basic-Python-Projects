import turtle as t

t.bgcolor("black")
t.color("red","red")
t.speed(10)
t.penup()
t.goto(-50,-130)
t.pendown()
t.begin_fill()
t.circle(200)
t.end_fill()
t.penup()
t.left(90)
t.forward(30)
t.right(90)
t.color("red","white")
t.begin_fill()
t.circle(170)
t.end_fill()
t.penup()
t.left(90)
t.forward(30)
t.right(90)
t.pendown()
t.color("white","red")
t.begin_fill()
t.circle(140)
t.end_fill()
t.penup()
t.left(90)
t.forward(50)
t.right(90)
t.pendown()
t.color("blue","blue")
t.begin_fill()
t.circle(90)
t.end_fill()
t.penup()
t.color("white","white")
t.goto(-105,-1)
t.pendown()
t.begin_fill()
t.left(36)
for i in range(5):
    t.forward(170)
    t.left(144)
t.end_fill()
t.hideturtle()











t.done()