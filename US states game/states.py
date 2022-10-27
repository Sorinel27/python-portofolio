from turtle import Turtle


class States(Turtle):
    def __init__(self, x, y, name_of_state):
        super().__init__()
        self.x = x
        self.y = y
        self.name_of_state = name_of_state
        self.hideturtle()
        self.pu()
        self.speed("fastest")
        self.goto(self.x, self.y)
        self.write(f"{self.name_of_state}", False, "Center", font=('Congenial', 9, 'normal'))
