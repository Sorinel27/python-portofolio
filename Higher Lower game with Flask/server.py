from flask import Flask

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
