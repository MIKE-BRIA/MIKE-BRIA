from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def move_forward():
    tom.forward(30)


def move_back():
    tom.back(30)


def move_right():
    tom.right(90)


def move_left():
    tom.left(90)


screen.listen()
tom.width(5)
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_right)
screen.onkey(key="d", fun=move_left)
screen.exitonclick()
