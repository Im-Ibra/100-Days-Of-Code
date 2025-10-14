from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_player = Player((-350, 0))
r_player = Player((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_player.move_up, "Up")
screen.onkey(r_player.move_down, "Down")
screen.onkey(l_player.move_up, "w")
screen.onkey(l_player.move_down, "s")

game_on = True

while game_on:
    time.sleep(.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_player) < 50 and ball.xcor() > 320 or ball.distance(l_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()


screen.exitonclick()
