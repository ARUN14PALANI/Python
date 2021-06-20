import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True

car_manager = CarManager()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 280:
        car_manager.move_fast()
        player.player_reset()
        scoreboard.player_reached()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()







