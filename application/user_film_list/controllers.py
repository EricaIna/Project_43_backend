from flask import jsonify, request
from werkzeug import exceptions
from .models import UserFilmList
from .. import db
from ..movies.models import Movie



def index():
    movies = UserFilmList.query.all()
    try:
        return jsonify({ "data": [c.json for c in movies] }), 200
    except:
        raise exceptions.InternalServerError(f"We are working on it")

def show(id):
    print("id", type(id))
    movie = UserFilmList.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": movie.json }), 200
    except:
        raise exceptions.NotFound(f"You get it")


def create():
    try:
        user_id,title = request.json.values()
        print("Enter in create function")

        new_movie_list = UserFilmList(user_id,title)
        
        db.session.add(new_movie_list)
        db.session.commit()

        return jsonify({ "data": new_movie_list.json }), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request")



def update(id):
    data = request.json
    movie_list = UserFilmList.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(movie_list, attribute):
            setattr(movie_list, attribute, value)

    db.session.commit()
    return jsonify({ "data": movie_list.json })


def destroy(id):
    movie_list = UserFilmList.query.filter_by(id=id).first()
    db.session.delete(movie_list)
    db.session.commit()
    return "movie list Deleted", 204


def recommend(id):
    movie_list = UserFilmList.query.filter_by(id=id).first()
#Add a new movie to the movie_list, based on the result of 'recommend_movie' result



def show_movie_details(id,movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    if movie:
        return jsonify({"details": movie.original_title}), 200
    else:
        return jsonify({"message": f"Movie with movie_id {movie_id} not found"}), 404


def add_movie(id,movie_id):
    print("Enter in add_movie function")
    print("ID",type(id)) 
    # user_film_instance = UserFilmList.query.get(id)
    user_film_instance = UserFilmList.query.filter_by(id=id).first()
    
    # user_film_instance=db.session.query(UserFilmList).get(1)
    print("user_film_instance=",user_film_instance) 

    

    if user_film_instance:
        print("user_film_instance.movie_ids",user_film_instance.movie_ids)
        user_film_instance.movie_ids.append(movie_id)
        db.session.commit()
        return jsonify({"message": "Movie added successfully"}), 200
    else:
        return jsonify({"message": "UserFilmList not found"}), 404


def remove_movie(id,movie_id):
    user_film_instance = UserFilmList.query.get(id)
    
    if user_film_instance:
        if movie_id in user_film_instance.movie_ids:
            user_film_instance.movie_ids.remove(movie_id)
            db.session.commit()
            return jsonify({"message": "Movie removed successfully"}), 200
        else:
            return jsonify({"message": "Movie not found in user's list"}), 404
    else:
        return jsonify({"message": "UserFilmList not found"}), 404
