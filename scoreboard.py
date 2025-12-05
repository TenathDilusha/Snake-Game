from turtle import Turtle

def read_high_score():
    with open("data.txt") as file:
        score = file.read()
        score = int(score)
    return score

def save_high_score(data):
    with open("data.txt", mode="w") as file:
        file.write(str(data))

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.high_score = read_high_score()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.score += 1

    def game_over(self):
        if self.high_score < self.score:
            self.high_score = self.score
            save_high_score(self.high_score)
            self.write_score()
            self.goto(0, -40)
            self.write(f"New high score: {self.high_score}", align="center", font=("Arial", 20, "bold"))
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "bold"))
        self.goto(0, -250)
        self.write("Press 'space' key to play again", align="center", font=("Arial", 15, "normal"))

    def game_restart(self):
        self.clear()
        self.goto(0, 270)
        self.score = 0
        self.write_score()