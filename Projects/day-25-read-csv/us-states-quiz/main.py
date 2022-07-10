import csv
import turtle
import pandas as pd
tr = turtle.Turtle()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Projects/day-25-read-csv/us-states-quiz/blank_states_img.gif"
screen.addshape(image)

def right_answer(x_pos,y_pos,state_name):
    answer = turtle.Turtle()
    answer.penup()
    answer.hideturtle()
    answer.goto(x_pos,y_pos)
    answer.write(state_name)

tr.shape(image)


game_on = True
i = 0
known_states_list = []
while game_on == True:
    if i == 50:
        game_on = False
        result = "won"
    answer_state = screen.textinput(title="Guess the state", prompt=f"Score: {i}/50. Type in the name of the state:")
    df_states = pd.read_csv("Projects/day-25-read-csv/us-states-quiz/50_states.csv")
    lower_states = (map(lambda x: x.lower(), df_states["state"]))
    list_states = df_states["state"]
    list_lower_states = list(lower_states)
    if answer_state.lower() in list_lower_states:
        xy = df_states[df_states["state"].str.lower() == answer_state.lower()]
        x_pos = xy["x"].values[0]
        y_pos = xy["y"].values[0]
        right_answer(x_pos,y_pos,answer_state.title())
        known_states_list.append(answer_state.title())
        i += 1

    elif answer_state.lower() == "exit":
        game_on = False
        result = "exit"



if game_on == False and result == "won":
    endgame = turtle.Turtle()
    endgame.penup()
    endgame.hideturtle()
    endgame.goto(0,0)
    endgame.write("CONGRATULATIONS!")

elif game_on == False and result == "exit":
    print("exited")
    missing_states_list = list(set(list_states) - set(known_states_list))
    df_missing = pd.DataFrame()
    df_missing["Missing States"] = missing_states_list
    df_missing.to_csv("Projects/day-25-read-csv/us-states-quiz/missing_states.csv")
# turtle.mainloop()
# states_not_guessed.to_csv