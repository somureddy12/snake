from turtle import  Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.xa=10
        self.ya=10

    def move(self):
        x=self.xcor()+self.xa
        y=self.ycor()+self.ya
        self.goto(x,y)
    def bounce_y(self):
        self.ya *=-1

    def bounce_x(self):
        self.xa *=-1

    def reverse(self):
        self.goto(0,0)
        self.bounce_x()
