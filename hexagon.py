import turtle
import math

turtle.shape("turtle")

def draw_polygon(side, number_of_edges):
    for i in range(0, number_of_edges):
        turtle.forward(side)
        turtle.left(360/number_of_edges)

def move_to_new_honeycomb(side, number_of_edges):
    turtle.forward(side)
    turtle.right(360/number_of_edges)

side = 100
edges = 6
for i in range(edges):
    draw_polygon(side, edges)
    move_to_new_honeycomb(side, edges)


turtle.exitonclick()
