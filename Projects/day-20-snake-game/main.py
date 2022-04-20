from turtle import Turtle, Screen
import time
from snake import Snake

## CONFIGURATION
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Guilherme's Snake Game")
screen.tracer(0)

#START GAME

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



# snakes_parts[0].forward(20)
# snakes_parts[0].left(90)
screen.exitonclick()