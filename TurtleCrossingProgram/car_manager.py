from turtle import Turtle
from player import Player
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(1, 2)
            random_y = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(250, random_y)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def move_fast(self):
        self.speed += MOVE_INCREMENT







