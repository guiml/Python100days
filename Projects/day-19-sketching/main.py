from turtle import Turtle, Screen


pointer = Turtle()
screen = Screen()

def move_w():
    pointer.forward(10)

def move_s():
    pointer.backward(10)

def move_a():
    pointer.right(10)

def move_d():
    pointer.left(10)


def clear_s():
    pointer.clear()
    pointer.penup()
    pointer.home()
    pointer.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_w)
screen.onkeypress(key="s", fun=move_s)
screen.onkeypress(key="a", fun=move_a)
screen.onkeypress(key="d", fun=move_d)
screen.onkeypress(key="c", fun=clear_s)


screen.exitonclick()
