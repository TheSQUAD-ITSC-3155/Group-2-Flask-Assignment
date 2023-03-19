# TODO: Feature 1
def test_list_all_movies(test_app):    
    test_app.post('/movies',data=dict(movie="taken", director="Pierre Morel", rating="5"))    
    #test_app.post('/movies', data=dict(movie="taken 2",director="Olivier Megaton", rating="4"))    
    #test_app.post('/movies', data=dict(movie="taken 3", director="Olivier Megaton", rating="3"))    
    #test_app.post('/movies', data=dict(movie="takers", director="John Luessenhop", rating="2"))    
    
    response = test_app.get('/movies')    
    assert b"<tr><td>taken</td><td>Pierre Morel</td><td>5</td></tr>" in response.data 
    #assert b"<tr><th>taken 2</th><td>Olivier Megaton</td><td>4</td></tr>" in response.data     
    #assert b"<tr><th>taken 3</th><td>Olivier Megaton</td><td>3</td></tr>" in response.data    
    #assert b"<tr><th>takers</th><td>John Luessenhop</td><td>2</td></tr>" in response.data