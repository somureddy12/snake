from turtle import Turtle

class Button(Turtle):
    def __init__(self, position):
        super().__init__()
        y = [-300, -250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 300, 350]
        for i in range(0, len(y) - 1):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.shapesize(stretch_wid=1.5, stretch_len=0.1)
            tim.speed("fastest")
            tim.penup()
            tim.goto(0, y[i])
            tim.forward(10)
            tim.pendown()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.pendown()

    def upkey(self):
        self.penup()
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def downkey(self):
        self.penup()
        y = self.ycor() - 20
        self.goto(self.xcor(), y)






