from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        # self.setheading(random.randint(0, 359))
        self.move_speed = 0.1
        self.x_speed = 10
        self.y_speed = 10

    def move(self):
        x = self.xcor() + self.x_speed
        y = self.ycor() + self.y_speed
        self.goto(x, y)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.speed("fastest")
        self.goto(0, 0)
        self.speed("normal")
        self.bounce_x()
        self.setheading(random.randint(0, 359))

