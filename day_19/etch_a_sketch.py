from turtle import Turtle, Screen

brush = Turtle()
brush.width(4)
screen = Screen()

def move_forward():
    brush.forward(10)

def move_backwards():
    brush.forward(-10)

def turn_left():
    brush.left(10)

def turn_right():
    brush.right(10)

def clear_screen():
    screen.resetscreen()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")


screen.exitonclick()