from turtle import Turtle

START_POS = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in START_POS:
            self.add_part(position)

    def move(self):
        for parts_num in range(len(self.snake) - 1, 0, -1):
            x_pos = self.snake[parts_num - 1].xcor()
            y_pos = self.snake[parts_num - 1].ycor()
            self.snake[parts_num].goto(x_pos, y_pos)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def grow(self):
        self.add_part(self.snake[-1].position())

    def add_part(self, position):
        part = Turtle("square")
        part.color("white")
        part.penup()
        part.setpos(position)
        self.snake.append(part)

    def reset(self):
        for part in self.snake:
            part.goto(2000, 2000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

