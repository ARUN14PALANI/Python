import turtle
import pandas

screen = turtle.Screen()
screen.title("State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()

print(type(data))
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50, Guess State", prompt="What is another State?")
    answer_state = str(answer_state).title()
    print(answer_state)
    if answer_state in data_list:
        guessed_state.append(answer_state)
        print("True")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    if answer_state == "None":
        break
print(len(data_list))
for i in guessed_state:
    if i in data_list:
        data_list.remove(i)

print(len(data_list))

new_data = pandas.DataFrame(data_list)
new_data.to_csv("states_to_learn.csv")

