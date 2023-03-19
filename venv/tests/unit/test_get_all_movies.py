# TODO: Feature 1
from app import app
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.repositories.movie_repository import _movie_repo
from src.models.movie import Movie


def test_get_all_movies_method():    
    movie_title = [Movie("taken", "Pierre Morel", 5), Movie("taken 2", "Olivier Megaton", 4), Movie("taken 3", "Olivier Megaton", 3), Movie("takers", "John Luessenhop", 2)]   
    _movie_repo.create_movie("taken", "Pierre Morel", 5)    
    _movie_repo.create_movie("taken 2", "Olivier Megaton", 4)    
    _movie_repo.create_movie("taken 3", "Olivier Megaton", 3)    
    _movie_repo.create_movie("takers", "John Luessenhop", 2)    
    singleton_movies = _movie_repo.get_all_movies()    
    for movie in range(4):        
        assert type(singleton_movies[movie]) is Movie        
        assert singleton_movies[movie].title == movie_title[movie].title        
        assert singleton_movies[movie].director == movie_title[movie].director       
        assert singleton_movies[movie].rating == movie_title[movie].rating