from turtle import Turtle

pos = (-465, 10)
speed = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.pu()
        self.goto(pos)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
