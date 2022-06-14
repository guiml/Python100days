## UNFINISHED PROPERLY


### MAIN LIBRARIES
from turtle import Screen
from bars import PuckHuman, PuckPc
from ball import Ball
import random

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

screen.onkey(puck_p.up,"w")
screen.onkey(puck_p.down,"s")

game = True
while game:
    ball.move()
    screen.update()
    #print(puck_h.pad.distance(ball.ball))
    print(ball.ball.heading())
    if puck_h.pad.distance(ball.ball) < 50 and ball.ball.xcor() < -355 :
        print("touched")
        ball.changedir(abs(360-ball.ball.heading())-ball.ball.heading())

    if puck_p.pad.distance(ball.ball) < 50 and ball.ball.xcor() > 355 :
        print("touched")
        ball.changedir(abs(ball.ball.heading()-180))

    if ball.ball.ycor() > 280 or ball.ball.ycor() < -280:
        ball.changedir(abs(360-ball.ball.heading())-ball.ball.heading())

screen.exitonclick()