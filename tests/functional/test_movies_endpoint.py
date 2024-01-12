import json

# Testing the overall functionality - is the route rendering the correct data?
def test_index_page(client):
    response = client.get("/") 
    # print("response_data=",response.data)   
    assert response.status_code == 200    
    assert response.data == b'{\n  "message": "Welcome to the Reddy 43 - Movies Application",\n  "description": "Movies API",\n  "endpoints": [\n    "GET / 200|500",\n    "GET /movies",\n    "GET /movies/<int:id>",\n    "GET /movies/top",\n    "GET /movies/upcoming"\n  ]\n}\n'
    

# GET /movies
def test_movies_page(client):
    response = client.get("/movies")
    assert response.status_code == 200
    data = json.loads(response.data)
    print("type of data=",type(data))
    assert type(data) == list
    assert len(data) > 1

    
# # GET/:id movies
def test_movie_page(client):
    response = client.get('/movies/2')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    print("data=",data, " len(data)=",len(data))
    assert len(data) == 25
    assert data['id'] == 2    
    assert data['original_language'] == "fi"
    assert data['original_title'] == 'Ariel'
   
    assert data['overview'] == "After the coal mine he works at closes and his father commits suicide, a Finnish man leaves for the city to make a living but there, he is framed and imprisoned for various crimes."
    assert data['vote_average'] == 7.086
    assert data['release_date'] == "1988-10-21"
    assert data['poster_path'] == "/ojDg0PGvs6R9xYFodRct2kdI6wC.jpg"



