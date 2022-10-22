from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        self.goto(0, -330)

    def up(self):
        self.fd(10)

    def level_up(self):
        self.speed("fastest")
        self.goto(0, -330)
        self.speed("normal")
