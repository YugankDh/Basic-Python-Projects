import turtle as t
t.speed(20)
t.bgcolor("black")
t.hideturtle()
for i in range(5):
    t.color("red","green")
    t.begin_fill()
    t.circle(250,90)
    t.end_fill()
    t.color("red","green")
    t.left(90)
    t.begin_fill()
    t.circle(250,90)
    t.end_fill()
    t.left(18)
for i in range(110):
    t.color("red","pink")
    t.begin_fill()
    t.circle(180-i,90)
    t.end_fill()
    t.color("red","white")
    t.left(90)
    t.begin_fill()
    t.circle(180-i,90)
    t.end_fill()
    t.left(148)

t.done()












