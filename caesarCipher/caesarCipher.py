from asciiArt import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    if direction == 'encode':
        word = []
        for i in range(len(text)):
            check = False
            for j in range(len(alphabet)):
                if text[i] == alphabet[j]:
                    check = True
                    limit = j + shift
                    if limit >= len(alphabet):
                        word.append(alphabet[limit - len(alphabet)])
                    else:
                        word.append(alphabet[j + shift])
            if not check:
                word.append(text[i])
        word = ''.join(word)
        print(f"The encoded text is {word}")
    elif direction == 'decode':
        word = []
        for i in range(len(text)):
            check = False
            for j in range(len(alphabet)):
                if text[i] == alphabet[j]:
                    check = True
                    word.append(alphabet[j - shift])
            if not check:
                word.append(text[i])
        word = ''.join(word)
        print(f"The decoded text is {word}")


def main():
    print(logo)
    choice = True
    while choice:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift > 26:
            shift = shift % 26
        caesar(text, shift, direction)
        c = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if c == 'yes':
            choice = True
        elif c == 'no':
            choice = False
    print("Bye")


if __name__ == '__main__':
    main()
