from application.movies.models import Genre

def test_new_genre():
    genre = Genre(api_id=28, name='Action', movies=[])
    
    assert genre.api_id == 28
    assert genre.name == 'Action'
    assert genre.movies == []