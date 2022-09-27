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


def main():
    choice = True
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'n':
        choice = False
        return
    else:
        print(logo)
    while choice:
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
            print(f"Your final cards: {player_cards}, score: {player_score}")
            while computer_score <= 16:
                computer_cards = hit_card(computer_cards)
                computer_score = score(computer_cards)
            print(f"Computer's final cards: {computer_cards}, score: {computer_score}")
            if computer_score > 21:
                print("Opponent went over. You win.")
            elif 22 > computer_score > player_score:
                print("You lost.")
            elif computer_score == player_score:
                print("It's a draw.")
            else:
                print("You win!")


if __name__ == '__main__':
    main()
