from turtle import Screen, Turtle
from snake import SNAKE
from food import FOOD
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("My Snake Game")
segments=[]
screen.tracer(0)

snake = SNAKE()
food = FOOD()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.ext_snake()
        score.increase_score()
    if snake.head.xcor()>390 or snake.head.xcor()< -400 or snake.head.ycor()>300 or  snake.head.ycor()< -280:
        game_on = False
        score.game_over()
    for s in snake.segments:
        if s == snake.head:
            pass
        elif snake.head.distance(s)<10:
            game_on = False
            score.game_over()
screen.exitonclick()

























