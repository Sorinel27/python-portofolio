import random
from art import logo


def get_random_number():
    return random.randint(0, 101)


def main():
    attempts = 0
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    random_number = get_random_number()
    print(f"You chose the {difficulty} difficulty. {attempts} attempts left.")
    while attempts:
        guess = int(input("Make a guess: "))
        if guess == random_number:
            attempts -= 1
            print(f"You guessed the number {random_number} with {attempts} attempt(s) left. Congrats!")
            return 0
        elif guess > random_number:
            attempts -= 1
            print("Too high!")
        elif guess < random_number:
            attempts -= 1
            print("Too low!")
        if attempts != 0 and guess != random_number:
            print(f"You have {attempts} attempt(s) left.")
        else:
            continue
    print(f"You ran out of attempts. The random number was {random_number}.")


if __name__ == '__main__':
    main()
