from flask import Flask, render_template, url_for, request, redirect
import requests, smtplib

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
    post_id = int(post_id)
    return render_template('post.html', response=response, number_of_articles=number_of_articles, post_id=post_id)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/messageSend/<name>/<email>/<message>')
def message_send(name, email, message):
    print(name)
    visitor_mail = email
    print(visitor_mail)
    visitor_message = message
    print(visitor_message)
    email = "soringrape@gmail.com"
    password = "weirfhnbhgkmsuxd"
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email,
                        to_addrs="sorin78910@gmail.com",
                        msg=f"Subject:A new message from {name}!\n\nName: {name}\n\nEmail: {visitor_mail}\n\nMessage: {visitor_message}")
    connection.close()
    return render_template('message.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact_page():
    data = []
    if request.method == 'POST':
        data.append(request.form['name'])
        name = request.form['name']
        data.append(request.form['email'])
        email = request.form['email']
        data.append(request.form['message'])
        message = request.form['message']
        return redirect(url_for('message_send', name=name, email=email, message=message))
    return render_template('contact.html')


@app.route('/easteregg')
def cool_page():
    return render_template('solar.html')


if __name__ == '__main__':
    app.run(debug=True)
