from turtle import Turtle

Score = 0

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color('white')
        self.goto(0, 260)
        self.score_value()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        style = ('Courier', 20, 'italic')
        self.write(f'Score:{self.score}', font=style, align='center')

    def game_over(self):
        self.goto(0, 0)
        style = ('Courier', 20, 'italic')
        self.write(f'Game Over', font=style, align='center')

    def score_value(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


