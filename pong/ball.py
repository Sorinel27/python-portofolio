from turtle import Turtle
from turtle import Screen
import random

speed = 20
screen = Screen()


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        # self.setheading(random.randint(0, 359))
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

    def restart(self):
        self.speed("fastest")
        self.goto(0, 0)
        self.speed("normal")
        self.setheading(random.randint(0, 359))

