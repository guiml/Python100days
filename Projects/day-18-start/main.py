from ast import Num
from locale import currency
from os import NGROUPS_MAX
from turtle import Screen, Turtle, pendown, penup
import random

pointer = Turtle()
#timmy_the_turtle.shape("turtle")

pointer.right(90)
pointer.color("blue")


## DRAW SQUARE
# for _ in range(4):
#     pointer.forward(100)s
#     pointer.right(90)

## DRAW DOTTED SQUARE
# def dash_walk():
#     for _ in range(10):
#         pointer.forward(8)
#         pointer.penup()
#         pointer.forward(8)
#         pointer.pendown()
#         pointer.forward(8)
#     pointer.right(90)
# for _ in range(4):
#     dash_walk()

#num_sides = 5

## DRAW UP TO 10 SHAPES
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         pointer.forward(50)
#         pointer.right(angle)
# for shape_side_n in range(3,16):
#     pointer.color(random.choice(colors))
#     draw_shape(shape_side_n)


## RANDOM WALK
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)


# pointer.pensize(10)
# pointer.speed("fastest")
# screen =  Screen()
# screen.colormode(255)

# for _ in range(100):
#     pointer.pencolor(random_color())
#     direction = random.choice([90,180,270,0])
#     pointer.setheading(direction)
#     pointer.forward(20)

# screen = Screen()
# screen.exitonclick()

## CIRCLE
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


screen = Screen()
screen.colormode(255)
pointer.speed("fastest")

def draw_spirograph(size_gap):

    for _ in range(int(360 / size_gap)):
        pointer.pencolor(random_color())
        pointer.circle(100)
        pointer.setheading(pointer.heading() + size_gap)

draw_spirograph(5)
screen.exitonclick()