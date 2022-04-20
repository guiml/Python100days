from turtle import Turtle, Screen
XY_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()

    def create_snake(self):
        for pos in XY_POS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(pos)
            self.snake_parts.append(snake)

    def move(self):
        for seg_n in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[seg_n - 1].xcor()
            new_y = self.snake_parts[seg_n - 1].ycor()
            self.snake_parts[seg_n].goto(new_x, new_y)
        self.snake_parts[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_parts[0].heading() != 270:
            self.snake_parts[0].setheading(90)

    def down(self):
        if self.snake_parts[0].heading() != 90:
            self.snake_parts[0].setheading(270)

    def left(self):
        if self.snake_parts[0].heading() != 0:
            self.snake_parts[0].setheading(180)

    def right(self):
        if self.snake_parts[0].heading() != 180:
            self.snake_parts[0].setheading(0)
