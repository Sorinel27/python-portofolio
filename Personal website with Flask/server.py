from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<user_input>')
def old_version(user_input):
    if user_input == 'old':
        return render_template('old_web.html')
    else:
        return f'<h2 style="color:darkred; text-align: center; font-family: Arial, Helvetica, sans-serif;">Your input: {user_input} does not exist :(.\nClick the gif to return home.</h2>' \
               f'<br><a href="/"><img style="display:block; margin-left: auto; margin-right: auto;" src="https://media.tenor.com/gB6z2hBaWi8AAAAC/goofing-off-edd-gould.gif"></a>'


if __name__ == '__main__':
    app.run(debug=True)
