from flask import Flask
import random

app = Flask(__name__)

RANDOM_NUMBER = random.randint(0, 101)


def bold(function):
    def nested():
        return f'<b>{function()}</b>'

    return nested


@app.route('/')
@bold
def home_page():
    return '<u><h1 style="size: 20px; text-align:center; font-family: Arial, Helvetica, sans-serif;">Welcome to the higher lower game!</h1></u>' \
           '<h2 style="color:darkblue; text-align: center; font-family: Arial, Helvetica, sans-serif;">Guess a number between 0 and 100</h2>' \
           '<img style="display:block; margin-left: auto; margin-right: auto;" src="https://static.tnn.in/photo/msid-96383100,imgsize-491555,width-100,height-200,resizemode-75/96383100.jpg">'


@app.route('/<user_input>')
def guess(user_input):
    try:
        user_input = int(user_input)
        if user_input > 100 or user_input < 0:
            return f'<h2 style="color:darkpurple; text-align: center; font-family: Arial, Helvetica, sans-serif;">The number {user_input} is not in 0, 100 range.</h2>' \
                   f'<br><img style="display:block; margin-left: auto; margin-right: auto;" src="https://media.tenor.com/wHs3JITWApsAAAAd/galaxy-brain-meme.gif">'
        if user_input > RANDOM_NUMBER:
            return f'<h2 style="color:darkred; text-align: center; font-family: Arial, Helvetica, sans-serif;">The number {user_input} is higher, guess low.</h2>' \
                   f'<br><img style="display:block; margin-left: auto; margin-right: auto;" src="https://media.tenor.com/94SQAXziRiEAAAAC/spicy-chili.gif">'
        if user_input < RANDOM_NUMBER:
            return f'<h2 style="color:darkblue; text-align: center; font-family: Arial, Helvetica, sans-serif;">The number {user_input} is lower, guess high.</h2>' \
                   f'<br><img style="display:block; margin-left: auto; margin-right: auto;" src="https://media.tenor.com/3DY3OCcwhWkAAAAC/frozen-cold.gif">'
        return '<h2 style="color:darkgreen; text-align: center; font-family: Arial, Helvetica, sans-serif;">You guessed the number! Congrats!</h2>' \
               '<br><img style="display:block; margin-left: auto; margin-right: auto;" src="https://media.tenor.com/cuwj6gJLLW8AAAAd/victory-royale-winner.gif">'
    except:
        return f'<h2 style="color:darkred; text-align: center; font-family: Arial, Helvetica, sans-serif;">Error on guessing! Your input: {user_input}</h2>' \
               f'<iframe style="display:block; margin-left: auto; margin-right: auto;" src="https://giphy.com/embed/lPopSkL3auzOujW3eO" width="680" height="470" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'


if __name__ == '__main__':
    print(RANDOM_NUMBER)
    app.run(debug=True)
