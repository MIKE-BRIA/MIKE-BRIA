import turtle as t
import random

tim = t.Turtle()

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours


# colours = [
#     "CornflowerBlue",
#     "DarkOrchid",
#     "Red",
#     "IndianRed",
#     "wheat",
#     "SlateGray",
#     "SeaGreen",
# ]

direction = [0, 90, 180, 270]

for i in range(3000):
    tim.color(random_color())
    tim.forward(40)
    tim.setheading(random.choice(direction))
    tim.width(15)
    tim.speed("fastest")
