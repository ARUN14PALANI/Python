from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.color("Black")
        self.player_reached()

    def player_reached(self):
        self.clear()
        self.write(f"Level : {self.score}", align="Center", font=FONT)
        self.score += 1

    def game_over(self):
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align="Center", font=FONT)
