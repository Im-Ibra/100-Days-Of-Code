from turtle import Turtle

class Player(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.player = Turtle("square")
        self.player.shapesize(stretch_wid=5, stretch_len=1)
        self.player.color("white")
        self.player.penup()
        self.player.speed("fastest")
        self.player.goto(pos)

    def move_up(self):
        new_y = self.player.ycor() + 20
        self.player.goto(self.player.xcor(), new_y)

    def move_down(self):
        new_y = self.player.ycor() - 20
        self.player.goto(self.player.xcor(), new_y)