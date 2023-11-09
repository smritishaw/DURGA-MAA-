#drawing Maa Durga using Python Code
import turtle as t
t.bgcolor("white")
def pos(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#for Tika
pos(0,200)
t.color("red")
t.begin-fill()
t.circle(40)
t.end-fill()
#for left eyebrow
pos(-30,200)
t.begin-fill()
t.right(45)
for i in range(20):
    t.left(3)
    t.back(10)
for i in range(10):
    t.right(3)
    t.back(10)
t.right(18)
for i in range(13):
    t.left(3)
    t.forward(10)
for i in range(20):
    t.right(2)
    t.forward(10)
t.end-fill()
#for left eyebrow
t.left(80)
pos(0,200)
t.begin-fill()
for i in range(20):
    t.right(3)
    t.forward(10)
for i in range(10):
    t.left(3)
    t.forward(10)
t.left(18)
for i in range(13):
    t.right(3)
    t.back(10)
for i in range(20):
    t.left(2)
    t.back(10)
t.end-fill()
#for right eye
pos(40,150)
t.pensize(15)
t.left(10)
for i in range(20):
    t.right(3)
    t.forward(10)
for i in range(10):
    t.left(3)
    t.forward(5)
t.right(3)
for i in range (10):
    t.left(3)
    t.back(5)
for i in range(20):
    t.right(3)
    t.back(10)
t.pensize(1)
pos(130,130)
t.begin-fill()
t.circle(40)
t.end-fill
t.color("white")

for i in range(47):
    t.right(7)
    t.back(10)
t.hideturtle
t.exitonclick()
