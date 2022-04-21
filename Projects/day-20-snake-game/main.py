from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

## CONFIGURATION
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Guilherme's Snake Game")
screen.tracer(0)

#START GAME

snake = Snake()
food = Food()
sb = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
score = 0

while game_on:
    sb.set_score(score)
    screen.update()
    time.sleep(0.1)
    snake.move()

    ### DETECT ENCOUNTER WITH FOOD
    if snake.snake_parts[0].distance(food) < 15:
        score += 1
        sb.set_score(score)
        food.refresh()
        snake.extend()
    
    ### DETECT COLISION WITH WALL
    if snake.snake_parts[0].xcor() > 280 or snake.snake_parts[0].xcor() < -280 or snake.snake_parts[0].ycor() > 280 or snake.snake_parts[0].ycor() < -280:
        game_on = False
        sb.game_over()

    ### DETECT COLISION WITH BODY
    for seg in snake.snake_parts[1:]:
        if snake.snake_parts[0].distance(seg) <10:
            game_on = False
            sb.game_over()

screen.exitonclick()