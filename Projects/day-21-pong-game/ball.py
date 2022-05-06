from turtle import Turtle



class Ball:

    def __init__(self) -> None:
        self.ball = Turtle()
        self.ball.color("red")
        self.ball.shape("square")
        self.ball.speed(0)
