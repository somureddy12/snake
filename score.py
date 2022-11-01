from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 225)
        self.color("white")
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("arial", 15, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("arial", 15, "bold"))

    def checking(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("arial", 15, "bold"))
