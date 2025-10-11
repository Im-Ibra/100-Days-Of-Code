from turtle import Turtle, Screen
import random
"""import colorgram

colors = colorgram.extract("image.jpg", 20)
rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)"""

ninja = Turtle()
ninja.hideturtle()
ninja.speed("fastest")
screen = Screen()
screen.colormode(255)
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77)]

count = 0
gap = 50
while count < 10:
    for _ in range(10):
        ninja.pendown()
        ninja.dot(20, random.choice(color_list))
        ninja.penup()
        ninja.forward(50)

    ninja.setpos(0, gap)
    gap += 50
    count += 1

screen.exitonclick()