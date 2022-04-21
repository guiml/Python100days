from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.goto(random.randint(-270,270),random.randint(-270,270))
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-270,270),random.randint(-270,270))
