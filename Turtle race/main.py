import random
import turtle as t

t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()
screen = t.Screen()


def main():
    t.listen()
    bet = t.textinput("Make your bet", "Who will win the race? Enter a colour:")
    t1.shape("turtle")
    t2.shape("turtle")
    t3.shape("turtle")
    t4.shape("turtle")
    t5.shape("turtle")
    t6.shape("turtle")

    t1.color("red")
    t2.color("orange")
    t3.color("yellow")
    t4.color("green")
    t5.color("blue")
    t6.color("purple")

    t1.pu()
    t2.pu()
    t3.pu()
    t4.pu()
    t5.pu()
    t6.pu()

    height = screen.window_height()
    width = screen.window_width()

    part = height / 6

    pos_x = (-(width / 2 - 20))

    t1.setposition(pos_x, 144)
    t2.setposition(pos_x, 72)
    t3.setposition(pos_x, 0)
    t4.setposition(pos_x, -72)
    t5.setposition(pos_x, -144)
    t6.setposition(pos_x, -216)
    turtles = [t1, t2, t3, t4, t5, t6]
    is_winner = False

    while not is_winner:
        random.shuffle(turtles)
        speed = random.randint(1, 5)
        for i in turtles:
            if i.xcor() > width / 2:
                is_winner = True
                print(f"The winner is {i.color()[0]}!")
                if bet.lower() == i.color()[0]:
                    print("You win the bet. Congrats!")
                else:
                    print("You lost. :(")
                break
        turtles[0].forward(speed)
    screen.listen()
    screen.exitonclick()


if __name__ == '__main__':
    main()
