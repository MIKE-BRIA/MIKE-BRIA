import turtle as t
from turtle import Screen as sc
import random

tom = t.Turtle()

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours


tom.speed("fastest")


def draw_spiral(size_of_spiral):
    for i in range(int(360 / size_of_spiral)):
        tom.color(random_color())
        tom.width(2)
        tom.circle(120)
        tom.setheading(tom.heading() + size_of_spiral)


draw_spiral(5)
screen = sc()
screen.exitonclick()
