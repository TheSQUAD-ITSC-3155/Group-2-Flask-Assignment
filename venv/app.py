from flask import Flask, redirect, render_template, request, url_for

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movieList = []
directorList = []
ratingList = []

movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    movie = request.form.get('movie',"")
    director = request.form.get('director', '')
    rating = request.form.get('rating', '')
    if (movie != ""):
        movieList.append(movie)
        directorList.append(director)
        ratingList.append(rating)
    return render_template('list_all_movies.html', list_movies_active=True,movie=movieList,director=directorList,rating=ratingList)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')

@app.post('/submit')
def submit():
    movie = request.form.get('movie', 'Nothing')
    director = request.form.get('director', 'Nothing')
    rating = request.form.get('rating', 'Nothing')

    movieList.append(movie)
    directorList.append(director)
    ratingList.append(rating)
    return render_template('list_all_movies.html',movie=movieList,director=directorList,rating=ratingList)
#,movie=movieList

@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
