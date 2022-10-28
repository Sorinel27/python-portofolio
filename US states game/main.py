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
    guessed_states = []

    while no_states_guessed < 50:
        answer_input = screen.textinput(f"{no_states_guessed}/50 states correct", "Type the name of a state:")
        if answer_input == "Exit":
            missing_states = [st for st in states_list if st not in guessed_states]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("missed_states.csv")
            break
        for st in states_list:
            if st == answer_input:
                no_states_guessed += 1
                states_list.remove(st)
                x = data[data["state"] == st].values[0][1]
                y = data[data["state"] == st].values[0][2]
                state = States(x, y, st)
                guessed_states.append(state)
    screen.exitonclick()


if __name__ == '__main__':
    main()
