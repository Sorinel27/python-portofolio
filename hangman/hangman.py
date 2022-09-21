import random


def main():
    hangman_pics = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    logo = ''' 
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/    '''
    mistakes = 0
    is_solved = False
    gameProgress = []
    print(logo)
    print(hangman_pics[mistakes])
    words = ('monstrous insurance expand pawn front information mask constant boom care agriculture '
             'sneeze small rat consider support resist like drop pat beef adaptable '
             'sink classy cross journey friends speed eminent grubby son efficient alluring '
             'oranges shake sense poison crackers testy endanger worship unit loose slam '
             'parched game drawer break able insure hurt quick sand blood lyrical art miscreant '
             'sophisticated underwear integrate stick dive praise aboriginal obedient summon boot lunchroom '
             'branch vegetable ').split()
    random.shuffle(words)
    chosen_word = words[0]
    print("Welcome to Hangman! Try and guess the next word:")
    for i in range(len(chosen_word)):
        print("_", end=" ")
        gameProgress.append("_")
    while mistakes != len(hangman_pics) - 1:
        letter = input("\nType a letter: ").lower()
        ok = False
        for i in range(len(chosen_word)):
            if letter == chosen_word[i]:
                gameProgress[i] = letter
                ok = True
        if not ok:
            mistakes += 1
            print("Your guess " + letter + " is not in the word.")
            print(hangman_pics[mistakes])
            print("Word: ")
            for i in range(len(gameProgress)):
                print(gameProgress[i], end=" ")
        else:
            print("Word: ")
            for i in range(len(gameProgress)):
                print(gameProgress[i], end=" ")
            join = ''.join(gameProgress)
            if join == chosen_word:
                is_solved = True
        if is_solved:
            break
    if not is_solved:
        print("\nGame Over! You lose.")
        print("The word was: " + chosen_word)
    else:
        print("\nGame Over! You won!")


if __name__ == '__main__':
    main()
