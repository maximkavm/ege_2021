import turtle

turtle = turtle.Turtle()
k = 10

turtle.right(315)
for i in range(7):
    turtle.forward(16 * k)
    turtle.right(45)
    turtle.forward(8 * k)
    turtle.right(135)

turtle.penup()

for x in range(20):
    for y in range(20):
        turtle.goto(x * k, y * k)
        turtle.dot()

turtle.done()