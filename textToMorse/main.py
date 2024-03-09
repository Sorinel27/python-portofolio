from flask import Flask, render_template, request

app = Flask(__name__)
morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}


@app.route('/', methods=['GET', 'POST'])
def main_page():
    """
    This function is the main function of the app. It will render the index.html page and will handle the POST request.
    Converts the text to morse code.
    :return:
    """
    text = ""
    encodedText = ""
    if request.method == 'POST':
        text = request.form['text']
        og = text
        print(text)
        text = text.lower()
        for char in text:
            if char == " ":
                encodedText += "   "
            elif char in morse_code_dict:
                if encodedText == "":
                    encodedText = encodedText + morse_code_dict[char]
                else:
                    encodedText = encodedText + " " + morse_code_dict[char]
        # return render_template('index.html', result="ceva de txt")
    print(encodedText)
    return render_template('index.html', text=text, encodedText=encodedText, encode=1)

@app.route('/decode', methods=['GET', 'POST'])
def decode_page():
    """
    This function will decode the morse code to text.
    :return:
    """
    text = ""
    decodedText = ""
    if request.method == 'POST':
        text = request.form['text']
        print(text)
        reversed_dict = {value: key for key, value in morse_code_dict.items()}
        index = 0
        # to do: refactor this part
        for i in range(1, len(text)):
            if text[i] == " " and text[i - 1] != " ":
                if text.split(" ")[index] in reversed_dict:
                    decodedText += reversed_dict[text.split(" ")[index]]
                index += 1
            else:
                index += 1
    print(decodedText)
    return render_template('index.html', text=text, decodedText=decodedText, encode=0)

if __name__ == '__main__':
    app.run(debug=True)
