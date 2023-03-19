# TODO: Feature 3
from app import app
from src.repositories.movie_repository import _movie_repo
def test_search_movies_page():    
    test_app = app.test_client()    
    
    response = test_app.get("/movies/search")    
    assert b'<p>Nothing Found</p>' in response.data    
    
    response = test_app.get("/movies/search?title=nonexist")    
    assert b'<p>Nothing Found</p>' in response.data    
    
    _movie_repo.create_movie("Hello", "Mr. Director", 4)    
    
    response = test_app.get("/movies/search?title=Hello")    
    
    assert b'<td>Movies Found:</td>' in response.data    
    #assert b'<td>Hello</td>' in response.data    
    #assert b'<td>Movie Rating:</td>' in response.data    
    #assert b'<td>4</td>' in response.data