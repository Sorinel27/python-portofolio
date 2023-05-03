from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)
NEWS_KEY = '4d8f01d7210c405e907159f8f8e0cd49'
GET_LINK = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_KEY}'


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/blog')
def blog_page():
    response = requests.get(GET_LINK)
    response = response.json()
    number_of_articles = len(response['articles'])
    return render_template('blog.html', response=response, number_of_articles=number_of_articles)


@app.route('/blog/post/<post_id>')
def post_page(post_id):
    response = requests.get(GET_LINK)
    response = response.json()
    number_of_articles = len(response['articles'])
    return render_template('post.html', response=response, number_of_articles=number_of_articles, post_id=post_id)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
