import time
from turtle import Screen
from player import Player
from ball import Ball

screen = Screen()
ball = Ball()
positions2 = [(465, 30), (465, 10), (465, -10)]


def main():
    screen.title("Pong")
    screen.bgcolor("black")
    screen.setup(width=1000, height=700)
    player1 = Player()
    player2 = Player()
    i = 0
    for part in player2.parts:
        part.goto(positions2[i])
        i += 1
    screen.listen()
    ball_not_out = True
    while ball_not_out:
        screen.update()
        time.sleep(0.1)
        if ball.xcor() > 500 or ball.ycor() > 300:
            ball.setheading(ball.heading() + 90)
        if ball.xcor() < -500 or ball.ycor() < -300:
            ball.setheading(ball.heading() - 90)
        ball.move()
        screen.onkeypress(player1.up, "w")
        screen.onkeypress(player1.down, "s")
        screen.onkeypress(player2.up, "Up")
        screen.onkeypress(player2.down, "Down")
    screen.exitonclick()


if __name__ == '__main__':
    main()
