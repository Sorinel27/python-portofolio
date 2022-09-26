from art import logo
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print(logo)
    print("Welcome to the secret auction program.")
    inProgress = True
    data = {}
    while inProgress:
        name = input("What is your name? ")
        bid = int(input("What is your bid?: $"))
        bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        data[name] = bid
        if bidders == 'yes':
            clear()
        elif bidders == 'no':
            inProgress = False
    highestBid = -1
    winner = ""
    for people in data:
        if data[people] > highestBid:
            highestBid = data[people]
            winner = people
    print(f"The winner is {winner} with a bid of ${highestBid}")


if __name__ == '__main__':
    main()
