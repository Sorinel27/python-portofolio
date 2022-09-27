import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def shuffle_cards(n):
    c = []
    for i in range(n):
        random.shuffle(cards)
        c.append(cards[0])
    return c


def hit_card(list):
    default_score = score(list)
    random.shuffle(cards)
    if cards[0] == 11 and default_score + 11 > 21:
        cards[0] = 1
    list.append(cards[0])
    return list


def score(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def final_touch(player_cards, player_score, computer_cards, computer_score, bet, balance):
    print(f"Your final cards: {player_cards}, score: {player_score}")
    while computer_score <= 16 and player_score < 22:
        computer_cards = hit_card(computer_cards)
        computer_score = score(computer_cards)
    print(f"Computer's final cards: {computer_cards}, score: {computer_score}")
    if computer_score > 21 and player_score > 21:
        print("Both went over. Draw.")
    elif computer_score > 21:
        print("Opponent went over. You win!")
        balance = balance + bet
    elif 22 > computer_score > player_score:
        print("You lost.")
        balance = balance - bet
    elif computer_score == player_score:
        print("It's a draw.")
    elif player_score > 21 and computer_score < 22:
        print("You lost.")
        balance = balance - bet
    else:
        print("You win!")
        balance = balance + bet
    return balance


def main():
    choice = True
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'n':
        choice = False
        return
    else:
        print(logo)
        balance = int(input("Enter your balance: $"))
        print(f"Your balance is ${balance}.")
    while balance > 0:
        bet = int(input("Place your bet: $"))
        print(balance)
        if bet > balance:
            print(f"Not enough credits. Your balance is ${balance}.")
        win = False
        computer_score = 0
        player_cards = shuffle_cards(2)
        computer_cards = shuffle_cards(2)
        player_score = score(player_cards)
        computer_score = score(computer_cards)
        print(player_cards)
        print(computer_cards)
        if player_cards[0] == 11 and player_cards[1] == 11:
            player_cards[1] = 1
        if computer_cards[0] == 11 and computer_cards[1] == 11:
            computer_cards[1] = 1
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'n':
            balance = final_touch(player_cards, player_score, computer_cards, computer_score, bet, balance)
            print(f"Your balance is ${balance}.")
        elif another_card == 'y':
            while player_score < 22:
                player_cards = hit_card(player_cards)
                player_score = score(player_cards)
                print(f"Your cards: {player_cards}, current score: {player_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                if player_score < 21:
                    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
                    if another_card == 'n':
                        break
            balance = final_touch(player_cards, player_score, computer_cards, computer_score, bet, balance)
            print(f"Your balance is ${balance}.")


if __name__ == '__main__':
    main()
