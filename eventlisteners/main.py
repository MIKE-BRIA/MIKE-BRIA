from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def move_forward():
    tom.forward(30)


screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()
