from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

with open("data.txt", mode="r") as file:
    point = file.read()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(point)
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                point = file.write(str(self.high_score))
        self.score =0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()








