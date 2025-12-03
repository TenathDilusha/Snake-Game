from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake = []
        for i in range(3):
            snake_head = Turtle("square")
            snake_head.penup()
            snake_head.color("white")
            snake_head.goto(0 - i * 20, 0)
            self.snake.append(snake_head)
        self.head = self.snake[0]

    def extend(self):
        tail = Turtle("square")
        tail.penup()
        tail.color("white")
        tail.goto(self.snake[-1].xcor(), self.snake[-1].ycor())
        self.snake.append(tail)

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            x_value = self.snake[seg - 1].xcor()
            y_value = self.snake[seg - 1].ycor()
            self.snake[seg].goto(x_value, y_value)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)