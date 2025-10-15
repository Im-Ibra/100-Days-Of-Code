from turtle import Screen
from player import Player
from cars import Cars
from level import Level
import time

screen = Screen()
screen.colormode(255)
screen.setup(700, 700)
screen.title("Frog")
screen.tracer(0)

player = Player((0, -320))
cars =  Cars()
level = Level()

screen.listen()
screen.onkey(player.move, "space")

game_on = True

while game_on:
    time.sleep(.1)
    screen.update()
    cars.create_car()
    cars.move()

    for car in cars.all_cars:
        if cars.distance(player) < 20:
            game_on = False

    if player.ycor() > 320:
        screen.clear()
        level.next_lvl()
        cars.m_speed *= 1.5

screen.exitonclick()