import turtle

n = 36
y = 0
x = -200
turtle.goto(x, y)
length = 400
turtle.speed(30)
turtle.hideturtle()

for i in range(n):
    turtle.forward(length)
    turtle.left(170)

turtle.done()
