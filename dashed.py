import turtle

for i in range(20):
    turtle.forward(15 * (0.1 * i))
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()

turtle.exitonclick()
