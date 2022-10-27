import turtle
import pandas
from states import States


def main():
    screen = turtle.Screen()
    screen.title("U.S. States")
    screen.setup(727, 493)
    image = "image.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv("50_states.csv")
    states_list = data["state"].to_list()
    no_states_guessed = 0
    answer_input = screen.textinput("Guess the state", "Type the name of a state:")
    guessed_states = []

    while no_states_guessed < 50:
        if answer_input is None:
            print("Not a correct state!")
        for st in states_list:
            if st == answer_input:
                no_states_guessed += 1
                states_list.remove(st)
                x = data[data["state"] == st].values[0][1]
                y = data[data["state"] == st].values[0][2]
                state = States(x, y, st)
                guessed_states.append(state)
        if no_states_guessed < 50:
            answer_input = screen.textinput(f"{no_states_guessed}/50 states correct", "Type the name of a state:")
    screen.exitonclick()


if __name__ == '__main__':
    main()
