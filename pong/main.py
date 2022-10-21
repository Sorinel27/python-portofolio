import time
from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Score1
from scoreboard2 import Score2

screen = Screen()
ball = Ball()
player1 = Player()
player2 = Player()
pos2 = (465, 10)
score_player1 = Score1()
score_player2 = Score2()


def main():
    screen.title("Pong")
    screen.bgcolor("black")
    screen.setup(width=1000, height=700)
    player2.goto(pos2)
    screen.listen()
    screen.onkeypress(player1.up, "w")
    screen.onkeypress(player1.down, "s")
    screen.onkeypress(player2.up, "Up")
    screen.onkeypress(player2.down, "Down")
    print(ball.heading())
    ball_not_out = True
    while ball_not_out:
        time.sleep(0.1)
        screen.update()
        ball.move()
        if ball.ycor() > 340 or ball.ycor() < -340:
            ball.bounce_y()
        if ball.distance(player1) < 50 and ball.xcor() > 455 or ball.distance(player2) < 50 and ball.xcor() < -455:
            ball.bounce_x()
        if ball.xcor() > 500:
            score_player1.update()
            ball.restart()
        elif ball.xcor() < -500:
            score_player2.update()
            ball.restart()

    screen.exitonclick()


if __name__ == '__main__':
    main()
