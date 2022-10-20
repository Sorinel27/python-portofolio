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
        self.setheading(random.randint(0, 359))

    def move(self):
        screen.update()
        self.forward(speed)


