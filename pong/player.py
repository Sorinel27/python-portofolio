from turtle import Turtle
from turtle import Screen
from ball import Ball

positions = [(-465, 30), (-465, 10), (-465, -10)]
speed = 20
screen = Screen()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        parts = []
        for pos in positions:
            part = Turtle("square")
            part.color("white")
            part.speed("fastest")
            part.pu()
            part.goto(pos)
            parts.append(part)
        self.parts = parts
        self.head = self.parts[0]
        self.tail = self.parts[len(parts) - 1]

    # def move(self):
    #     for part in range(len(self.parts) - 1, 0, -1):
    #         x = self.parts[part - 1].xcor()
    #         y = self.parts[part - 1].ycor()
    #         self.parts[part].goto(x, y)
    #     self.head.forward(speed)

    def up(self):
        screen.update()
        for part in self.parts:
            x = part.xcor()
            y = part.ycor()
            part.goto(x, y + speed)
        # self.head.setheading(90)
        # for part in range(len(self.parts) - 1, 0, -1):
        #     x = self.parts[part - 1].xcor()
        #     y = self.parts[part - 1].ycor()
        #     self.parts[part].goto(x, y)
        # self.head.forward(speed)

    def down(self):
        screen.update()
        for part in self.parts:
            x = part.xcor()
            y = part.ycor()
            part.goto(x, y - speed)
        # self.tail.setheading(270)
        # for part in range(len(self.parts) - 1):
        #     x = self.parts[part + 1].xcor()
        #     y = self.parts[part + 1].ycor()
        #     self.parts[part].goto(x, y)
        # self.tail.forward(speed)
