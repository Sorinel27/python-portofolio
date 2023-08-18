from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy import asc
import requests


API_KEY = "your api key"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very secret'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    Bootstrap(app)
    db = SQLAlchemy(app)

    class Movie(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        year = db.Column(db.Integer, nullable=False)
        description = db.Column(db.String(2500), nullable=False)
        rating = db.Column(db.Float, nullable=False)
        ranking = db.Column(db.Integer, nullable=False)
        review = db.Column(db.String(250), nullable=False)
        img_url = db.Column(db.String(250), nullable=False)

        def __repr__(self):
            return f'<Movie {self.title}>'

    class MovieForm(FlaskForm):
        rating = StringField('Rating', validators=[DataRequired()])
        review = StringField('Review', validators=[DataRequired()])
        title = StringField('Movie Title', validators=[DataRequired()])
        update_submit = SubmitField('Done')
        add_movie_submit = SubmitField('Add Movie')

    db.create_all()

    @app.route("/")
    def home():
        movies = db.session.query(Movie).order_by(asc(Movie.rating))
        return render_template("index.html", movies=movies)

    @app.route('/edit/<id>', methods=['GET', 'POST'])
    def edit(id):
        form = MovieForm()
        data = Movie.query.get(id)
        if data is not None:
            if request.method == 'POST':
                data.rating = request.form['rating']
                data.review = request.form['review']
                db.session.commit()
                return redirect(url_for('home'))
        else:
            if request.method == 'POST':
                url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
                headers = {
                    "accept": "application/json",
                    "Authorization": "access granted"
                }
                response = requests.get(url, headers=headers)
                movie_data = response.json()
                print(movie_data)
                new_movie = Movie(
                    title=movie_data['original_title'],
                    year=movie_data['release_date'].split('-')[0],
                    description=movie_data['overview'],
                    rating=request.form['rating'],
                    ranking='None',
                    review=request.form['review'],
                    img_url=f"https://image.tmdb.org/t/p/w500/{movie_data['poster_path']}"
                )
                db.session.add(new_movie)
                db.session.commit()
                return redirect(url_for('home'))
        return render_template('edit.html', form=form, data=data, id=id)

    @app.route('/delete/<id>')
    def delete(id):
        data = Movie.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for('home'))

    @app.route('/add', methods=['GET', 'POST'])
    def add():
        form = MovieForm()
        if request.method == 'POST':
            search = request.form['title']
            URL = f'https://api.themoviedb.org/3/search/movie?query={search}&language=en-US'
            headers = {
                "accept": "application/json",
                "Authorization": "access granted"
            }
            response = requests.get(URL, headers=headers)
            api_data = response.json()
            print(api_data)
            api_data = api_data['results']
            return render_template('select.html', api_data=api_data)
        return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
