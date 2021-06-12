from turtle import Turtle, Screen

screen = Screen()
tom = Turtle()


def move_for():
    tom.forward(10)


def screen_clear():
    tom.goto(0, 0)
    tom.clear()


def move_c():
    tom.right(10)


def move_ac():
    tom.left(10)


def move_back():
    tom.forward(-10)


screen.listen()
screen.onkey(key="w", fun=move_for)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_ac)
screen.onkey(key="d", fun=move_c)
screen.onkey(key="c", fun=screen_clear)

screen.exitonclick()











screen.exitonclick()
