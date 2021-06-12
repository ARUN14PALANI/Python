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
    current_turtle.goto(-230, turtle_position[turtle_index])
    current_turtle.clear()
    new_turtles.append(current_turtle)

user_text = screen.textinput("Which color will won", "please enter you bet")
print(user_text)
is_race = True
if user_text:
    while is_race:
        for turtle in new_turtles:
            turtle.forward(random.randint(0, 10))
            turtle.clear()
            winning_color = turtle.pencolor()
            if turtle.xcor() > 230:
                is_race = False
                if user_text == winning_color:
                    print(f"you won!, {winning_color} is first..")
                else:
                    print(f"you lose!, {winning_color} is first..")

screen.exitonclick()

