from turtle import Turtle, Screen
import random

start = False
screen = Screen()
screen.setup(500, 400)
gamble = screen.textinput(title="Who's gonna win?", prompt="Choose the turtle you think it's gonna win: ")

ninja_turtles = ["red", "blue", "purple", "orange"]
mutant_turtles = []
y_pos = -40

for teens in range(0, 4):
    ninja = Turtle(shape="turtle")
    ninja.color(ninja_turtles[teens])
    ninja.penup()
    ninja.goto(-230, y_pos)
    y_pos += 30
    mutant_turtles.append(ninja)

if gamble:
    start = True

while start:
    for member in mutant_turtles:
        if member.xcor() > 230:
            winner = member.pencolor()
            if winner == gamble:
                print(f"Congrats you've won, {winner} turtle is the winner")
                start = False
            else:
                print(f"Bummer, you lost! {winner} turtle was the winner")
                start = False
        speed = random.randint(0, 15)
        member.forward(speed)

screen.exitonclick()