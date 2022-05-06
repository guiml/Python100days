### MAIN LIBRARIES
from turtle import Screen
from bars import PuckHuman, PuckPc
from ball import Ball
import time

### LOCAL CLASSES
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Gui's pong game   |o   |")

puck_h = PuckHuman()
puck_p = PuckPc()
ball = Ball()
#puck.load_bars()


screen.listen()
screen.onkey(puck_h.up,"Up")
screen.onkey(puck_h.down,"Down")

game = True
while game:
    screen.update()


screen.exitonclick()