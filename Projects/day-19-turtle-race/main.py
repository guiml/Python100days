from curses import use_default_colors
from site import USER_BASE
from turtle import Turtle, Screen
import random

pointer = Turtle()
screen = Screen()

screen.setup(width=500, height=400)


user_bet = screen.textinput("Make your bet","Which turtle will win the race? Enter a color: ")
#print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]
y_pos = [-70, -40, -10, 20, 50 , 80]
turtles_list = []


is_race_on = False

for turtle_i in range(0, 6):
    race_t = Turtle(shape="turtle")
    race_t.penup()
    race_t.color(colors[turtle_i])
    race_t.goto(x=-230, y=y_pos[turtle_i])
    turtles_list.append(race_t)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles_list:
        if t.xcor() > 228:
            is_race_on = False

            if t.pencolor() == user_bet:
                print(f"You've won! The {t.pencolor()} turtle is hte winner!")
            else:
                print(f"You've lost! The {t.pencolor()} turtle is hte winner!")

        rand_dist = random.randint(0, 10)
        t.forward(rand_dist)




# def move_w():
#     pointer.forward(10)

# def move_s():
#     pointer.backward(10)

# def move_a():
#     pointer.right(10)

# def move_d():
#     pointer.left(10)


# def clear_s():
#     pointer.clear()
#     pointer.penup()
#     pointer.home()
#     pointer.pendown()

# screen.listen()
# screen.onkeypress(key="w", fun=move_w)
# screen.onkeypress(key="s", fun=move_s)
# screen.onkeypress(key="a", fun=move_a)
# screen.onkeypress(key="d", fun=move_d)
# screen.onkeypress(key="c", fun=clear_s)


screen.exitonclick()
