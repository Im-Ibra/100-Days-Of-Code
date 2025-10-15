from turtle import Turtle

class Player(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("black")
        self.goto(pos)

    def move(self):
        self.forward(20)