import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player() # STEP1: Create Turtle
car_manager = CarManager() # STEP2: Create cars
scoreboard = Scoreboard()

screen.listen() # STEP 1.2: Move turtle 
screen.onkey(player.go_up, "Up") #STEP 1.2 Move turlte 



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #STEP 3: detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            game_is_on = False


    #STEP 4: Detect when turtle reaches other side
    if player.is_at_finish():
        player.restart_game()
        car_manager.level_up()
        scoreboard.increase_level() #STEP 5: Scoreboard



screen.exitonclick()