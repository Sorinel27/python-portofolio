import requests
import smtplib
from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import FlaskForm, CSRFProtect
from flask_ckeditor import CKEditorField, CKEditor
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from flask_bootstrap import Bootstrap
import datetime

app = Flask(__name__)
NEWS_KEY = '4d8f01d7210c405e907159f8f8e0cd49'
GET_LINK = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_KEY}'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
csrf = CSRFProtect(app)
app.secret_key = "topsecretkey"
ckeditor = CKEditor(app)

with app.app_context():
    Bootstrap(app)
    db = SQLAlchemy(app)


    class PostForm(FlaskForm):
        title = StringField('Blog Post Title', validators=[DataRequired()])
        subtitle = StringField('Subtitle', validators=[DataRequired()])
        user = StringField('Your name', validators=[DataRequired()])
        content = CKEditorField('Content', validators=[DataRequired()])
        submit = SubmitField('Submit post')


    class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        subtitle = db.Column(db.String(250), nullable=False)
        user = db.Column(db.String(250), nullable=False)
        date = db.Column(db.String(250), nullable=False)
        text = db.Column(db.String(2500), nullable=False)

        def __repr__(self):
            return f'Book {self.title}'


    db.create_all()


    @app.route('/')
    def main_page():
        return render_template('index.html')


    @app.route('/news')
    def news_page():
        response = requests.get(GET_LINK)
        response = response.json()
        number_of_articles = len(response['articles'])
        return render_template('news.html', response=response, number_of_articles=number_of_articles)


    @app.route('/news/post/<post_id>')
    def news_post_page(post_id):
        response = requests.get(GET_LINK)
        response = response.json()
        number_of_articles = len(response['articles'])
        post_id = int(post_id)
        return render_template('news-post.html', response=response, number_of_articles=number_of_articles,
                               post_id=post_id)


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


    @app.route('/blog')
    def blog_page():
        all_posts = db.session.query(Post).all()
        return render_template('blog.html', posts=all_posts)


    @app.route('/blog/post/<id>')
    def post_page(id):
        selected_post = Post.query.get(id)
        return render_template('post.html', post=selected_post)


    @app.route('/new-post', methods=['POST', 'GET'])
    def new_post():
        form = PostForm()
        if request.method == "POST":
            d = datetime.datetime.now()
            today_date = ""
            today_date += d.strftime("%B")  # month
            today_date += " "
            today_date += d.strftime("%d")  # day
            today_date += ", "
            today_date += d.strftime("%Y")  # year
            new_post = Post(
                title=request.form['title'],
                subtitle=request.form['subtitle'],
                user=request.form['user'],
                date=today_date,
                text=request.form['content']
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('blog_page'))
        return render_template('new-post.html', form=form)


    @app.route('/edit-post/<id>', methods=['POST', 'GET'])
    def edit_page(id):
        post_data = Post.query.get(id)
        print(post_data.user)
        form = PostForm(
            title=post_data.title,
            subtitle=post_data.subtitle,
            user=post_data.user,
            content=post_data.text
        )
        if request.method == 'POST':
            post_data.title = request.form['title']
            post_data.subtitle = request.form['subtitle']
            post_data.user = request.form['user']
            post_data.text = request.form['content']
            db.session.commit()
            return redirect(url_for(f'blog_page'))
        return render_template('new-post.html', form=form, id=id)


    @app.route('/delete/<id>')
    def delete_page(id):
        data = Post.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for('blog_page'))


    @app.route('/easteregg')
    def cool_page():
        return render_template('solar.html')

if __name__ == '__main__':
    app.run(debug=True)
