from turtle import Screen
from player import Player
from cars import Cars
from level import Level
import time


def main():
    screen = Screen()
    screen.setup(width=600, height=700)
    screen.bgcolor("white")
    screen.tracer(0)
    screen.listen()
    player = Player()
    cars = Cars()
    level = Level()
    screen.onkeypress(player.up, "w")
    not_dead = True
    while not_dead:
        time.sleep(0.1)
        screen.update()
        cars.move()
        if player.ycor() > 350:
            player.level_up()
            level.update()
            cars.x_speed *= 1.2
        for car in cars.cars:
            if car.xcor() < -320:
                cars.refresh(car)
            if player.distance(car) < 20:
                not_dead = False
    level.game_over()
    screen.exitonclick()


if __name__ == '__main__':
    main()
