from turtle import Turtle, Screen

mikely = Turtle()
mikely.shape("turtle")
mikely.color("green3")
mikely.shapesize(2)
# mikely.forward(400)
# mikely.right(90)
# mikely.forward(400)
# mikely.right(90)
# mikely.forward(400)
# mikely.right(90)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        mikely.forward(100)
        mikely.right(angle)


for i in range(3, 38):
    draw_shape(i)

# for i in range(5):
# mikely.forward(10)
# mikely.penup()
# mikely.forward(10)
# mikely.pendown()
# # mikely.right(90)

screen = Screen()
screen.exitonclick()


import heroes

print(heroes.gen())
