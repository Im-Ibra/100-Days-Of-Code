from turtle import Turtle
import random

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.m_speed = 10
        self.penup()
        self.hideturtle()

    def create_car(self):
        car_chance = random.randint(1, 6)
        if car_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(
                random.randint(1, 255),
                random.randint(1, 255),
                random.randint(1, 255)
            )
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(-300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.m_speed)