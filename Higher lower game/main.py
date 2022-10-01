import random
from game_data import data
import art


def random_data():
    random.shuffle(data)
    return data[1]


def main():
    print(art.logo)
    score = 0
    wrong_choice = False
    celeb_a = random_data()
    while not wrong_choice:
        celeb_b = random_data()
        followers_a = 0
        followers_b = 0
        for attr in celeb_a:
            if attr == 'follower_count':
                followers_a = celeb_a[attr]
        print("Compare A: ", end="")
        for attr in celeb_a:
            if attr == 'name':
                print(celeb_a[attr], end="")
            elif attr == 'description':
                print(f", a {celeb_a[attr]}", end="")
            elif attr == 'country':
                print(f", from {celeb_a[attr]}.")

        print(art.vs)

        for attr in celeb_b:
            if attr == 'follower_count':
                followers_b = celeb_b[attr]
        print("Against B:", end="")
        for attr in celeb_b:
            if attr == 'name':
                print(celeb_b[attr], end="")
            elif attr == 'description':
                print(f", a {celeb_b[attr]}", end="")
            elif attr == 'country':
                print(f", from {celeb_b[attr]}.")
        guess = input("Who has more followers? Type 'A' or 'B': ")
        if guess == 'A':
            if followers_a > followers_b:
                score += 1
                celeb_a = celeb_b
            else:
                print(f"Sorry, that's wrong. Final score = {score}.")
                wrong_choice = True
        elif guess == 'B':
            if followers_a < followers_b:
                score += 1
                celeb_a = celeb_b
            else:
                print(f"Sorry, that's wrong. Final score = {score}.")
                wrong_choice = True


if __name__ == '__main__':
    main()
