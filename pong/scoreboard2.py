from turtle import Turtle


class Score2(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(50, 300)
        self.write(f"{self.player_score}", False, "Center", font=('Congenial', 35, 'normal'))

    def update(self):
        self.player_score += 1
        self.clear()
        self.write(f"{self.player_score}", False, "Center", font=('Congenial', 35, 'normal'))
