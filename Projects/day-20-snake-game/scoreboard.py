from turtle import Turtle
ALIGNMENT = "center"
TUPLE_FONT = ('Courier',20,'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("light grey")
        self.goto(0,275)

    def set_score(self, sc):
        self.clear()
        self.write(f"Score: {sc} ", False, align= ALIGNMENT, font= TUPLE_FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER!", False, align= ALIGNMENT, font= TUPLE_FONT)

