from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.c_level = 1
        self.penup()
        self.hideturtle()
        self.update_lvl()

    def update_lvl(self):
        self.goto(-300, 300)
        self.write(f"Level {self.c_level}", align="center", font=("Arial", 16,"normal"))

    def next_lvl(self):
        self.c_level += 1
        self.clear()
        self.update_lvl()