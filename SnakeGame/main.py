from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time



screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

sv = 0
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_game_on = True
print(type(280))
while is_game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_value()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -295:
        is_game_on = False
        score.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()


    #detect collission with tail


screen.exitonclick()

