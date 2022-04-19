###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import Screen, Turtle, pendown, penup
import random

pointer = Turtle()
screen = Screen()

screen.screensize(350,350)
screen.colormode(255)
pointer.speed("fastest")
pointer.shape("circle")

rgb_colors = []
colors = colorgram.extract('image.png', 30)
for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    rgb_colors.append((r,g,b))

color_list = rgb_colors
pointer.penup()
pointer.goto(250,-200)


pointer.pensize(20)

def draw_line(heading, c):
    pointer.pencolor(random.choice(rgb_colors))
    pointer.pendown()
    pointer.forward(1)
    pointer.setheading(heading)
    pointer.penup()
    if not c == 9:
        pointer.forward(50)

for l in range(10):
    if l %2 == 0:
        heading = 180
    else:
        heading = 0
    
    for c in range(10):
        draw_line(heading,c)
    
    if not l == 9:
        pointer.penup()
        pointer.setheading(90)
        pointer.forward(50)
        pointer.penup()




screen.exitonclick()
