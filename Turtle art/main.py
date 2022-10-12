import turtle as t
import random
import colorgram

marcel = t.Turtle()
screen = t.Screen()
screen.colormode(255)
marcel.pensize(20)


def turn_right():
    marcel.forward(1)
    marcel.right(90)
    marcel.pd()
    marcel.forward(1)
    marcel.pu()
    marcel.forward(50)
    marcel.right(90)
    marcel.forward(1)
    marcel.pu()


def turn_left():
    marcel.forward(1)
    marcel.left(90)
    marcel.pd()
    marcel.forward(1)
    marcel.pu()
    marcel.forward(50)
    marcel.left(90)
    marcel.forward(1)
    marcel.pu()


def main():
    colors = colorgram.extract('image.jpg', 100)
    rgb = []
    for color in colors:
        rgb.append(color.rgb)
    # marcel.speed("fastest")
    marcel.pu()
    marcel.setx(-230)
    marcel.sety(-220)
    marcel.pd()
    step = 1
    for i in range(100):
        print(step)
        random.shuffle(rgb)
        marcel.pencolor(rgb[0])
        if step % 10 == 0 and step / 10 % 2 != 0:
            turn_left()
        elif step % 10 == 0 and step / 10 % 2 == 0:
            turn_right()
        else:
            marcel.pd()
            marcel.forward(1)
            marcel.pu()
            marcel.forward(50)
        step += 1
    screen.exitonclick()


if __name__ == '__main__':
    main()
