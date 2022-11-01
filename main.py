from turtle import Turtle,Screen
from buttonkey import Button
from ball import Ball
import time
from score import Score
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG GAME")
screen.tracer(0)
screen.listen()
score=Score()
r_button=Button((370,0))
l_button=Button((-370,0))
ball=Ball()
screen.onkey(r_button.upkey, "Up")
screen.onkey(r_button.downkey, "Down")
screen.onkey(l_button.upkey, "a")
screen.onkey(l_button.downkey, "z")
move_speed=0.09
game=True
while game:
    time.sleep( move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_button)<50 and ball.xcor()>350 or (ball.distance(l_button)<50 and ball.xcor()<-350):
        move_speed *=0.9
        print(move_speed)
        ball.bounce_x()

    if ball.xcor()>370:
        ball.reverse()
        score.left_score()

    if ball.xcor()<-370:
        ball.reverse()
        score.right_score()
screen.exitonclick()
