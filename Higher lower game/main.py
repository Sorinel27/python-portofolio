import random
from game_data import data
from art import logo


def random_data():
    random.shuffle(data)
    return data[1]


def main():
    print(logo)
    score = 0
    celeb_a = random_data()
    celeb_b = random_data()
    followers_a = 0
    followers_b = 0
    for attr in celeb_a:
        if attr == 'follower_count':
            followers_a = celeb_a[attr]
    for attr in celeb_a:
        if attr == 'name':
            print(celeb_a[attr], end="")
        elif attr == 'description':
            print(f", a {celeb_a[attr]}", end="")
        elif attr == 'country':
            print(f", from {celeb_a[attr]}.")

    for attr in celeb_b:
        if attr == 'follower_count':
            followers_b = celeb_b[attr]
    for attr in celeb_b:
        if attr == 'name':
            print(celeb_b[attr], end="")
        elif attr == 'description':
            print(f", a {celeb_b[attr]}", end="")
        elif attr == 'country':
            print(f", from {celeb_b[attr]}.")
    print(f"{followers_a}, {followers_b}")


if __name__ == '__main__':
    main()
