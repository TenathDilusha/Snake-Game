from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "bold"))