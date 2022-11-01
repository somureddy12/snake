from turtle import Turtle

MOVE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add(i)

    def add(self, i):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(i)
        self.segment.append(tim)

    def extend(self):
        i = self.segment[-1].position()
        self.add(i)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            newx = self.segment[seg - 1].xcor()
            newy = self.segment[seg - 1].ycor()
            self.segment[seg].goto(newx, newy)
        self.head.forward(MOVE)
 
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

       
    def reverse(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if y==0:
            self.segment[0].goto(-x, y)
        if x and y > 0:

            if x >= y:
                self.segment[0].goto(-x, y)
            else:
                self.segment[0].goto(x, -y)

        if x > 0 and y < 0:
            if -y >= x:
                print(x, y)
                self.head.goto(x, -y)
            elif x >= y:
                print(x, y)
                self.head.goto(-x, y)

        if x < 0 and y > 0:
            if y >= -x:
                print(x,y)
                self.head.goto(x, -y)
            elif x <= y:
                print(x,y)
                self.head.goto(-x, y)


        if x and y < 0:

            if x <= y:
                self.segment[0].goto(-x, y)
            else:
                self.segment[0].goto(x, -y)


# def q1(self):
    #     x = self.head.xcor()
    #     y = self.head.ycor()
    #     if y>=x:
    #         self.segment[0].goto(x, -y)
    #     else:
    #         self.segment[0].goto(-x, y)
    #
    # def q3(self):
    #     x = self.head.xcor()
    #     y = self.head.ycor()
    #     if x>=y:
    #         self.segment[0].goto(x, -y)
    #     else:
    #         self.segment[0].goto(-x, y)
    #
    # def q2(self):
    #     x = self.head.xcor()
    #     y = self.head.ycor()
    #     if y>x:
    #         self.segment[0].goto(x, -y)
    #     else:
    #         self.segment[0].goto(-x, y)
    # def q4(self):
    #     x = self.head.xcor()
    #     y = self.head.ycor()
    #     if x>y:
    #         self.segment[0].goto(x, -y)
    #     else:
    #         self.segment[0].goto(-x, y)
