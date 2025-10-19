from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(width=725, height=500)
screen.bgpic("blank_states_img.gif")
screen.title("States Quiz")

score = 0

label = Turtle()
label.penup()
label.hideturtle()

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

while len(states_list) > 0:
    guess = screen.textinput(f"{score}/50 States Correct", "Guess a state").title()
    if guess == "Exit":
        data = {
            "Missed States": states_list
        }
        df = pandas.DataFrame(data)
        df.to_csv("Missed States.csv")
        break

    for states in states_list:
        if guess == states:
            state_data = data[data.state == states]
            score += 1
            label.goto(int(state_data.x), int(state_data.y))
            label.write(f"{states}", False, "center", ("Arial", 8, "normal"))
            states_list.remove(states)


screen.exitonclick()


