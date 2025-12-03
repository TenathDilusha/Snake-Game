from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("Snake game")

my_screen.tracer(0)
snake = Snake()
snake_food = Food()
my_score = Scoreboard()
game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    my_screen.listen()
    my_screen.onkey(snake.up, "Up")
    my_screen.onkey(snake.down, "Down")
    my_screen.onkey(snake.left, "Left")
    my_screen.onkey(snake.right, "Right")

    for seg in snake.snake:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10 :
            game_on = False

    if snake.head.distance(snake_food) < 20:
        snake_food.refresh()
        snake.extend()
        my_score.update_score()
        my_score.clear()
        my_score.write_score()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() > 280:
        game_on = False

my_score.game_over()








my_screen.exitonclick()