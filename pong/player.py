from turtle import Turtle
from turtle import Screen
from ball import Ball

pos = (-465, 10)
speed = 20
screen = Screen()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        part = Turtle("square")
        part.color("white")
        part.speed("fastest")
        part.pu()
        part.goto(pos)
        part.shapesize(5, 1)
        self.part = part

    # def move(self):
    #     for part in range(len(self.parts) - 1, 0, -1):
    #         x = self.parts[part - 1].xcor()
    #         y = self.parts[part - 1].ycor()
    #         self.parts[part].goto(x, y)
    #     self.head.forward(speed)

    def up(self):
        y = self.part.ycor() + 20
        self.part.goto(self.part.xcor(), y)

    def down(self):
        y = self.part.ycor() - 20
        self.part.goto(self.part.xcor(), y)
