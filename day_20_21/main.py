from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.tracer(False)
screen.title("Snake")

snake = Snake()
apple = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(apple) < 15:
        apple.refresh()
        score.scored()
        snake.grow()

    if snake.head.xcor() > 480 or snake.head.xcor() < -480 or snake.head.ycor() > 480 or snake.head.ycor() < -480:
        score.reset()
        snake.reset()

    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()