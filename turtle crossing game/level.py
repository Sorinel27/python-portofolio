from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.player_level = 1
        self.hideturtle()
        self.pu()
        self.goto(-280, 300)
        self.write(f"Level: {self.player_level}", False, 'Left', font=('Congenial', 15, 'normal'))

    def update(self):
        self.player_level += 1
        self.clear()
        self.write(f"Level: {self.player_level}", False, 'Left', font=('Congenial', 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, 'Center', font=('Congenial', 15, 'normal'))