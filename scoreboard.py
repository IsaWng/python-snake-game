from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.round = 1
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def read_high_score(self):
        with open("score.txt", mode="r") as file:
            return int(file.read())

    def save_score(self):
        with open("score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Round {self.round}  Score: {self.score}   High Score: {self.high_score}", move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        self.round += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_score()
        self.score = 0
        self.update_scoreboard()
