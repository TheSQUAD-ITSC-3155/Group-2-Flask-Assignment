from flask import Flask, redirect, render_template, request, url_for
from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True, movie_list = movie_repository.get_all_movies())


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)

@app.post('/movies')
def create_movie():
    movie = request.form.get('movie')
    director = request.form.get('director')
    rating = request.form.get('rating')
    movie_repository.create_movie(movie, director, rating)

    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    movie = request.args.get("movie")
    searchMovie = movie_repository.get_movie_by_title(movie)

    return render_template('search_movies.html', search_active=True, searchMovie=searchMovie)