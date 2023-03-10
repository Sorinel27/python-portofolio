from flask import Flask, render_template
import requests


app = Flask(__name__)
response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
response = response.json()

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/blog')
def blog_page():
    return render_template('blog.html', posts=response, id=0)


@app.route('/post/<post_id>')
def post_page(post_id):
    return render_template('blog.html', posts=response, id=post_id)



if __name__ == '__main__':
    app.run(debug=True)