from turtle import Turtle
import time
from types import BuiltinMethodType

MOVE_DISTANCE = 20

class PuckHuman:

    def __init__(self) -> None:
        self.pad = Turtle(shape="square", visible=False)
        self.pad.color("blue")
        self.pad.shapesize(stretch_wid=5,stretch_len=1)
        self.pad.speed(0)
        self.pad.penup()
        self.pad.goto(-360,0)
        self.pad.showturtle()

    def up(self):
        curr_ycor = self.pad.ycor()
        self.pad.sety(curr_ycor + MOVE_DISTANCE)
        
    
    def down(self):
        curr_ycor = self.pad.ycor()
        self.pad.sety(curr_ycor - MOVE_DISTANCE)
        


class PuckPc:

    def __init__(self) -> None:
        self.pad = Turtle(shape="square", visible=False)
        self.pad.color("grey")
        self.pad.shapesize(stretch_wid=5,stretch_len=1)
        self.pad.speed(0)
        self.pad.penup()
        self.pad.goto(360,0)
        self.pad.showturtle()

    def up(self):
        curr_ycor = self.pad.ycor()
        self.pad.sety(curr_ycor + MOVE_DISTANCE)
        
    
    def down(self):
        curr_ycor = self.pad.ycor()
        self.pad.sety(curr_ycor - MOVE_DISTANCE)     
