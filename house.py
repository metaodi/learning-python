import turtle
import math

turtle.shape("turtle")

side = 100
diagonal = math.sqrt(side**2 + side**2)

turtle.forward(side)
turtle.left(90)
turtle.forward(side)
turtle.left(135)
turtle.forward(diagonal) 
turtle.right(135)
turtle.forward(side)
turtle.right(90)
turtle.forward(side)
turtle.left(135)
turtle.forward(diagonal/2)
turtle.left(90)
turtle.forward(diagonal/2)
turtle.left(90)
turtle.forward(diagonal)

turtle.exitonclick()
