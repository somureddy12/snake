from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.scoreboard()
    def scoreboard(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.r_score, False, "center", ("arial", 50, "bold"))
        self.goto(-100, 200)
        self.write(self.l_score, False, "center", ("arial", 50, "bold"))
    def right_score(self):

        self.r_score += 1
        self.scoreboard()

    def left_score(self):

        self.l_score += 1
        self.scoreboard()


