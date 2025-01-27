from turtle import Turtle, Screen


screen = Screen()

screen.setup(width=800, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
color = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
y_position = [-70, -40, -10, 29, 50, 80, 110, 140]

n = 0
for n in range(0, 7):
    tom = Turtle(shape="turtle")
    tom.color(color[n])
    tom.penup()
    tom.goto(x=-370, y=y_position[n])


print(user_bet)

screen.exitonclick()
