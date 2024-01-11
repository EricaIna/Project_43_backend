from flask import jsonify
from werkzeug import exceptions
from .models import Movie
import requests
from .. import db

def index_and_seed():
    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OWRlYzM5ZWEzOTk3ZWRlNzJkOGJmYmE3ODliNmNhMSIsInN1YiI6IjY1OWZjMTI2NTI5NGU3MDEyYmM1OTRhMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-BESHu0oI5-ndoVrFpgPq3FUd5Hs1cVyu7JLugdsHzE" 
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # Clear existing data in the movies table
    Movie.query.delete()

    # Seed movies into the database
    for movie_data in data.get('results', []):
        movie = Movie(
            original_title=movie_data.get('original_title'),
            original_language=movie_data.get('original_language'),
            overview=movie_data.get('overview'),
            vote_average=movie_data.get('vote_average'),
            release_date=movie_data.get('release_date'),
        )
        db.session.add(movie)

    # Commit the changes to the database
    db.session.commit()

    return jsonify(data)



def index():
    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OWRlYzM5ZWEzOTk3ZWRlNzJkOGJmYmE3ODliNmNhMSIsInN1YiI6IjY1OWZjMTI2NTI5NGU3MDEyYmM1OTRhMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-BESHu0oI5-ndoVrFpgPq3FUd5Hs1cVyu7JLugdsHzE"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def top_rated():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OWRlYzM5ZWEzOTk3ZWRlNzJkOGJmYmE3ODliNmNhMSIsInN1YiI6IjY1OWZjMTI2NTI5NGU3MDEyYmM1OTRhMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-BESHu0oI5-ndoVrFpgPq3FUd5Hs1cVyu7JLugdsHzE"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def upcoming():
    url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OWRlYzM5ZWEzOTk3ZWRlNzJkOGJmYmE3ODliNmNhMSIsInN1YiI6IjY1OWZjMTI2NTI5NGU3MDEyYmM1OTRhMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-BESHu0oI5-ndoVrFpgPq3FUd5Hs1cVyu7JLugdsHzE"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def genres():
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OWRlYzM5ZWEzOTk3ZWRlNzJkOGJmYmE3ODliNmNhMSIsInN1YiI6IjY1OWZjMTI2NTI5NGU3MDEyYmM1OTRhMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-BESHu0oI5-ndoVrFpgPq3FUd5Hs1cVyu7JLugdsHzE"
    }

    response = requests.get(url, headers=headers)

    return response.json()    

def show(id):
    base_url = "https://api.themoviedb.org/3/movie/{id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OWRlYzM5ZWEzOTk3ZWRlNzJkOGJmYmE3ODliNmNhMSIsInN1YiI6IjY1OWZjMTI2NTI5NGU3MDEyYmM1OTRhMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-BESHu0oI5-ndoVrFpgPq3FUd5Hs1cVyu7JLugdsHzE"
    }

    url = base_url.format(id=id)

    response = requests.get(url, headers=headers)

    return response.json()




# def show(movie_id):
#     base_url = "https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
#     api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OWRlYzM5ZWEzOTk3ZWRlNzJkOGJmYmE3ODliNmNhMSIsInN1YiI6IjY1OWZjMTI2NTI5NGU3MDEyYmM1OTRhMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-BESHu0oI5-ndoVrFpgPq3FUd5Hs1cVyu7JLugdsHzE"

#     headers = {
#         "Accept": "application/json",
#         "Authorization": f"Bearer {api_key}",
#     }

#     url = base_url.format(movie_id=movie_id)
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         movie_data = response.json()
#         # Process the movie_data as needed (e.g., print specific information)
#         print("Movie Title:", movie_data.get("title"))
#     else:
#         print("Error:", response.status_code)
