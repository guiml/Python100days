from turtle import Turtle
import random


class Ball:

    def __init__(self) -> None:
        self.ball = Turtle()
        self.ball.color("red")
        self.ball.shape("square")
        self.ball.speed(1)
        self.ball.penup()
        self.ball.seth(random.randint(174,175))

    def move(self):
        self.ball.forward(10)

    def changedir(self,hdg):
        self.ball.seth(hdg)
