# TODO: Feature 2
from app import app
from src.repositories.movie_repository import _movie_repo
from src.models.movie import Movie
def test_create_movie():    
    movie_title = _movie_repo.create_movie("ITSC", "The Squad", 5)    
    assert type(movie_title) == Movie    
    assert movie_title.title == 'ITSC'   
    assert movie_title.director == 'The Squad'    
    assert movie_title.rating == 5    
    assert _movie_repo.get_movie_by_title('ITSC') != None