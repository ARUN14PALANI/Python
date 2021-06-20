from turtle import Turtle, Screen


from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

turtle_colors = ["red", "blue", "green", "yellow", "orange", "violet"]
turtle_position= [-90, -60, -30, 0, 30, 60]
new_turtles = []

for turtle_index in range(6):

    current_turtle = Turtle(shape="turtle")
    current_turtle.color(turtle_colors[turtle_index])
    current_turtle.penup()
    current_turtle.goto(-230, random.randint(-150, 150))

    new_turtles.append(current_turtle)

user_text = screen.textinput("Which color will won", "please enter you bet")
print(user_text)

screen.exitonclick()