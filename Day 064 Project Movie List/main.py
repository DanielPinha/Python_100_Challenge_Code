from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# #CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)


db.create_all()


# Create editing rating Form
class RatingForm(FlaskForm):
    rating = StringField(label="Your Rating out of 10", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    update = SubmitField(label='Done')


# Create add movie form
class AddMovieForm(FlaskForm):
    movie_title = StringField(label='Movie Title', validators=[DataRequired()])
    year = IntegerField(label='Movie Year', validators=[DataRequired()])
    description = StringField(label='Movie Synopsis', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movie_list=all_movies)


@app.route("/EditRating<int:movie_id>", methods=["GET", "POST"])
def edit_rating(movie_id):
    form = RatingForm()
    if form.validate_on_submit():
        movie = Movie.query.get(movie_id)
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form)


@app.route("/delete<int:movie_id>")
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        new_movie = Movie(
            title=form.movie_title.data,
            year=form.year.data,
            description=form.description.data,
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit_rating', movie_id=new_movie.id))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
