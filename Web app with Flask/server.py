import requests
import smtplib
import os
import datetime
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm, CSRFProtect
from flask_ckeditor import CKEditorField, CKEditor
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, EmailField
from flask_bootstrap import Bootstrap
from PIL import Image


app = Flask(__name__)
NEWS_KEY = '4d8f01d7210c405e907159f8f8e0cd49'
GET_LINK = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_KEY}'
UPLOAD_FOLDER = f'static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
csrf = CSRFProtect(app)
app.secret_key = "topsecretkey"
ckeditor = CKEditor(app)
login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
    Bootstrap(app)
    db = SQLAlchemy(app)


    class ContactForm(FlaskForm):
        name = StringField('Your name', validators=[DataRequired()])
        email = EmailField('Your e-mail', validators=[DataRequired()])
        text = StringField('Your message', validators=[DataRequired()])
        submit = SubmitField('Send')


    class PostForm(FlaskForm):
        title = StringField('Blog Post Title', validators=[DataRequired()])
        subtitle = StringField('Subtitle', validators=[DataRequired()])
        user = StringField('Your name', validators=[DataRequired()])
        content = CKEditorField('Content', validators=[DataRequired()])
        submit = SubmitField('Submit post')


    class CommentForm(FlaskForm):
        content = CKEditorField('Content', validators=[DataRequired()])
        submit = SubmitField('Add new comment')


    class User(UserMixin, db.Model):
        __tablename__ = "user"
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(100), unique=True, nullable=False)
        password = db.Column(db.String(100), nullable=False)
        name = db.Column(db.String(100), unique=True, nullable=False)
        profile_views = db.Column(db.Integer, nullable=False)
        picture_url = db.Column(db.String(3000))
        has_functions = db.Column(db.Boolean, nullable=False)
        is_admin = db.Column(db.Boolean, nullable=False)
        is_developer = db.Column(db.Boolean, nullable=False)
        posts = relationship("BlogPosts", back_populates="author")
        comment = relationship("Comments", back_populates="author")


    class BlogPosts(UserMixin, db.Model):
        __tablename__ = "posts"
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        author = relationship("User", back_populates="posts")
        comment = relationship("Comments", back_populates="posts")
        title = db.Column(db.String(250), unique=True, nullable=False)
        subtitle = db.Column(db.String(250), nullable=False)
        date = db.Column(db.String(250), nullable=False)
        text = db.Column(db.Text, nullable=False)
        post_views = db.Column(db.Integer, nullable=False)


    class Comments(UserMixin, db.Model):
        __tablename__ = "comment"
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
        author = relationship("User", back_populates="comment")
        posts = relationship("BlogPosts", back_populates="comment")
        text = db.Column(db.Text, nullable=False)
        date = db.Column(db.String(250), nullable=False)
        time = db.Column(db.String(250), nullable=False)


    # class User(UserMixin, db.Model):
    #     id = db.Column(db.Integer, primary_key=True)
    #     email = db.Column(db.String(100), unique=True)
    #     password = db.Column(db.String(100))
    #     name = db.Column(db.String(1000), unique=True)
    #
    # class Post(db.Model):
    #     id = db.Column(db.Integer, primary_key=True)
    #     title = db.Column(db.String(250), unique=True, nullable=False)
    #     subtitle = db.Column(db.String(250), nullable=False)
    #     user = db.Column(db.String(250), nullable=False)
    #     date = db.Column(db.String(250), nullable=False)
    #     text = db.Column(db.String(2500), nullable=False)
    #
    #     def __repr__(self):
    #         return f'Book {self.title}'

    db.create_all()


    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=user_id).first()


    @app.route('/')
    def main_page():
        return render_template('index.html', current_user=current_user)


    @app.route('/news')
    def news_page():
        response = requests.get(GET_LINK)
        response = response.json()
        number_of_articles = len(response['articles'])
        return render_template('news.html', response=response, number_of_articles=number_of_articles,
                               is_logged=current_user.is_authenticated)


    @app.route('/news/post/<post_id>')
    def news_post_page(post_id):
        response = requests.get(GET_LINK)
        response = response.json()
        number_of_articles = len(response['articles'])
        post_id = int(post_id)
        return render_template('news-post.html', response=response, number_of_articles=number_of_articles,
                               post_id=post_id, )


    @app.route('/about')
    def about_page():
        return render_template('about.html', is_logged=current_user.is_authenticated)


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
        if current_user.is_authenticated:
            form = ContactForm()
            if request.method == 'POST':
                name = current_user.name
                email = current_user.email
                message = request.form['text']
                return redirect(url_for('message_send', name=name, email=email, message=message))
        else:
            form = ContactForm()
            if request.method == 'POST':
                name = request.form['name']
                email = request.form['email']
                message = request.form['text']
                return redirect(url_for('message_send', name=name, email=email, message=message))
        return render_template('contact.html', form=form)


    @app.route('/blog')
    def blog_page():
        all_posts = db.session.query(BlogPosts).all()
        return render_template('blog.html', posts=all_posts, is_logged=current_user.is_authenticated)


    @app.route('/blog/post/<id>', methods=['POST', 'GET'])
    def post_page(id):
        selected_post = BlogPosts.query.filter_by(id=id).first()
        if current_user.id != selected_post.user_id:
            selected_post.post_views += 1
            db.session.commit()
        post_comments = Comments.query.filter_by(post_id=id).all()
        form = CommentForm()
        if request.method == "POST" and request.form['content'] != '':
            d = datetime.datetime.now()
            today_date = ""
            today_date += d.strftime("%B")  # month
            today_date += " "
            today_date += d.strftime("%d")  # day
            today_date += ", "
            today_date += d.strftime("%Y")  # year
            new_comment = Comments(
                user_id=current_user.id,
                post_id=selected_post.id,
                text=request.form['content'],
                date=today_date,
                time=d.strftime("%X")
            )
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('post_page', id=id))
        return render_template('post.html', comments=post_comments, form=form, post=selected_post,
                               current_user=current_user)


    @app.route('/new-post', methods=['POST', 'GET'])
    @login_required
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
            new_post = BlogPosts(
                title=request.form['title'],
                subtitle=request.form['subtitle'],
                user_id=current_user.id,
                date=today_date,
                text=request.form['content'],
                post_views=0
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('blog_page'))
        return render_template('new-post.html', form=form)


    @app.route('/edit-post/<id>', methods=['POST', 'GET'])
    @login_required
    def edit_page(id):
        post_data = BlogPosts.query.get(id)
        if current_user.id == 1 or current_user.id == post_data.user_id:
            form = PostForm(
                title=post_data.title,
                subtitle=post_data.subtitle,
                user=post_data.author.name,
                content=post_data.text
            )
            if request.method == 'POST':
                post_data.title = request.form['title']
                post_data.subtitle = request.form['subtitle']
                post_data.user = current_user.name
                post_data.text = request.form['content']
                db.session.commit()
                return redirect(url_for(f'blog_page'))
            return render_template('new-post.html', form=form, id=id)
        else:
            return f'<h1>FORBIDDEN</h1>', 403


    @app.route('/delete/<id>')
    def delete_page(id):
        data = BlogPosts.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for('blog_page'))


    @app.route('/login', methods=['GET', 'POST'])
    def login_page():
        form = PostForm()
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            try:
                user = db.session.query(User).filter_by(email=email).first()
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(url_for('blog_page'))
                else:
                    flash('Password incorrect, please try again.')
            except:
                flash('This email does not exist, please try again.')
        return render_template('login.html', form=form)


    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('main_page'))


    @app.route('/register', methods=['GET', 'POST'])
    def register_page():
        form = PostForm()
        if request.method == 'POST':
            # try:
            name = request.form['text']
            email = request.form['email']
            password = request.form['password']
            if name == '' or email == '' or password == '':
                flash("Please fill in all the forms")
                return redirect(url_for('register_page'))
            else:
                if len(email.split('.')) != 2:
                    flash('Please enter a valid email address!')
                    return redirect(url_for('register_page'))
                else:
                    password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
                    new_user = User(
                        name=name,
                        email=email,
                        password=password,
                        profile_views=0,
                        picture_url=None,
                        has_functions=False,
                        is_admin=False,
                        is_developer=False
                    )
                    db.session.add(new_user)
                    db.session.commit()
                    return redirect(url_for('login_page'))
            # except:
            #     flash("You've already registered with that email, log in instead!")
            #     return redirect(url_for('login_page'))
        return render_template('register.html', form=form)


    @app.route('/delete/post/comment/<id>')
    @login_required
    def delete_comment(id):
        selected_comment = Comments.query.get(id)
        if current_user.id == selected_comment.user_id or current_user.id == 1:
            post_id = selected_comment.post_id
            db.session.delete(selected_comment)
            db.session.commit()
            return redirect(url_for('post_page', id=post_id))
        else:
            return f'<h1 style="color: red;">FORBIDDEN</h1>', 403


    @app.route('/profile/<name>')
    def user_profile(name):
        wrong_name = False
        user = User.query.filter_by(name=name).first()
        img_route = None
        if user.picture_url is not None:
            im = Image.open(f'static/img/{user.picture_url}')
            width, height = im.size
            if width > 700:
                width = 700
            if height > 1300:
                height = 1300
            size = width, height
            im_resized = im.resize(size, Image.ANTIALIAS)
            im_resized.save(f'static/img/{user.picture_url}')
            if user.picture_url is not None:
                img_route = f'img/{user.picture_url}'
        user_posts = BlogPosts.query.filter_by(user_id=user.id).all()
        if current_user.is_authenticated:
            try:
                if current_user.id != user.id:
                    user.profile_views += 1
                    db.session.commit()
            except:
                wrong_name = True
                return render_template('profile.html', wrong_name=wrong_name, name=name)
        user = User.query.filter_by(name=name).first()
        return render_template('profile.html',
                               user=user,
                               wrong_name=wrong_name,
                               name=name,
                               user_posts=user_posts,
                               number_of_posts=len(user_posts),
                               route=img_route
                               )


    @app.route('/profile/<name>/edit', methods=['GET', 'POST'])
    @login_required
    def edit_profile(name):
        user = User.query.filter_by(name=name).first()
        print(user.picture_url)
        form = PostForm()
        if current_user.id == user.id or current_user.id == 1:
            if request.method == 'POST':
                file = request.files['file']
                if file.filename == '':
                    flash('No selected file')
                    return redirect(request.url)
                if file and allowed_file(file.filename):
                    extension = file.filename.split('.')[1]
                    file.filename = f'{user.name}.{extension}'
                    user.picture_url = file.filename
                    db.session.commit()
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    return redirect(url_for('user_profile', name=name))
            else:
                # flash('Error adding profile photo')
                return render_template('edit-profile.html', form=form)
        else:
            return f'<h1 style="color: red; text-align:center;">403 FORBIDDEN</h1>', 403

    @app.route('/panel', methods=['POST', 'GET'])
    @login_required
    def panel_page():
        if current_user.id != 1:
            return f'<h2 style="color: crimson;">YOU ARE NOT ALLOWED!</h2>', 403
        else:
            form = PostForm()
            if request.method == 'POST':
                name = request.form['name']
                user = User.query.filter_by(name=name).first()
                if user is not None:
                    if request.form.get('adm_check') is not None:
                        user.is_admin = True
                        user.has_functions = True
                    else:
                        user.is_admin = False
                    if request.form.get('dev_check') is not None:
                        user.is_developer = True
                        user.has_functions = True
                    else:
                        user.is_developer = False
                    if request.form.get('adm_check') is None and request.form.get('dev_check') is None:
                        user.has_functions = False
                    db.session.commit()
                    return redirect(url_for('user_profile', name=user.name))
                else:
                    flash('Wrong name!')
                    return redirect(url_for('panel_page'))
            return render_template('panel.html', form=form)


    @app.route('/easteregg')
    def cool_page():
        return render_template('solar.html')

if __name__ == '__main__':
    app.run(debug=True)
