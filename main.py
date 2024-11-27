
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard, ALIGNMENT, FONT


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game ")
screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
points = ScoreBoard()



screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)  # to slow down the action but we have to import the module time first
    snake.move()
    # to detect the collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        points.increase_score()
        points.update_score()

    # to detect the collisions with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        points.reset_score()
        snake.reset()

    # to detect collisions with tail
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) <10:
            points.reset_score()
            snake.reset()



screen.exitonclick()