# TODO: Feature 2
from src.repositories.movie_repository import _movie_repo
def test_create_movies(test_app):    
    movie_list = {        
        'movie': 'moonfall',        
        'director': 'Roland Emmerich',        
        'rating': '1'    
        }    
    response = test_app.post('/movies', data=movie_list)    
    assert _movie_repo.get_movie_by_title('moonfall') != None    
    assert response.status_code == 302    
    assert response.request.path == "/movies"