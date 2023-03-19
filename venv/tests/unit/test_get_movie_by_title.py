# TODO: Feature 3
from app import app
from src.repositories.movie_repository import _movie_repo
def test_get_movie_by_title():    
    list_of_movies = _movie_repo    
    assert None == list_of_movies.get_movie_by_title("moonfall")    
    list_of_movies.create_movie("moonfall", "Roland Emmerich", 4)    
    result_1 = list_of_movies.get_movie_by_title("moonfall")    
    assert result_1.title == "moonfall"    
    assert result_1.director == "Roland Emmerich"    
    assert result_1.rating == 4