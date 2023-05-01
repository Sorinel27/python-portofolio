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


@app.route('/blog/post/<id>')
def post_page(id):
    global response
    info = []
    id = int(id)
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    response = response.json()
    for item in response:
        if int(item['id']) == id:
            info.append(item['title'])
            info.append(item['subtitle'])
            info.append(item['body'])
    return render_template('blog.html', title=info[0], subtitle=info[1], body=info[2], id=1)


if __name__ == '__main__':
    app.run(debug=True)
