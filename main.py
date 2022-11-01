import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score1 = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score1.checking()
    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        # game = False
        # score1.game_over()
        snake.reverse()

    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game = False
            score1.game_over()

screen.exitonclick()
