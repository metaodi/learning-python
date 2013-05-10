import turtle

turtle.shape("turtle")

def draw_square(size):
    angle = 90;
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)

angle = 10
distance = 100

for x in range(0,10):
    draw_square(distance)
    turtle.left(angle)

turtle.exitonclick()
