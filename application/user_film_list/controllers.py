from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from werkzeug import exceptions
from .models import UserFilmList
from .. import db
from ..movies.models import Movie


def index():
    try:
        movies = UserFilmList.query.filter_by(user_id=get_jwt_identity())
        return jsonify({ "data": [c.json for c in movies] }), 200
    except Exception as e:
        print(e)
        raise exceptions.InternalServerError(f"We are working on it")

def show(id):
    movie_list = UserFilmList.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": movie_list.json }), 200
    except Exception as e:
        print(e)
        raise exceptions.NotFound(f"You get it")

 
def create():
    try:
        title = request.json.get("title", None)
        print()
        # new_movie_list = UserFilmList(get_jwt_identity(),title,[])
        new_movie_list = UserFilmList(get_jwt_identity(),title,"")
        
        db.session.add(new_movie_list)
        db.session.commit()

        return jsonify({ "data": new_movie_list.json }), 201
    except Exception as e:
        print(e)
        raise exceptions.BadRequest(f"We cannot process your request")


def update(id):
    try:
        data = request.json
        movie_list = UserFilmList.query.filter_by(id=id, user_id=get_jwt_identity()).first()
        if movie_list is None:
            return jsonify({"message": "Movie list is not found"}), 404

        for (attribute, value) in data.items():
            if hasattr(movie_list, attribute):
                setattr(movie_list, attribute, value)

        db.session.commit()
        return jsonify({ "data": movie_list.json }), 201
    except Exception as e:
        print(e)
        raise exceptions.BadRequest(f"We cannot update")

def destroy(id):
    try:
        movie_list = UserFilmList.query.filter_by(id=id, user_id=get_jwt_identity()).first()
        if movie_list is None:
            return jsonify({"message": "Movie list is not found"}), 404

        db.session.delete(movie_list)
        db.session.commit()
        return jsonify({"message": "Movie list Deleted"}), 204
    except Exception as e:
        print(e)
        raise exceptions.BadRequest(f"We cannot delete the list of movies")


#not done
def recommend(id):
    movie_list = UserFilmList.query.filter_by(id=id).first()
#Add a new movie to the movie_list, based on the result of 'recommend_movie' result


#?????? need to change the Movie, use what df?
def show_movie_details(id,movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    if movie:
        return jsonify({"details": movie.original_title}), 200
    else:
        return jsonify({"message": f"Movie with movie_id {movie_id} not found"}), 404

#worked
def add_movie(id,movie_id):
    movie_list = UserFilmList.query.filter_by(id=id, user_id=get_jwt_identity()).first()
    if movie_list is None:
        return jsonify({"message": "Movie list is not found"}), 404

    print("before movie_list.movie_ids=", movie_list.movie_ids)
    # movie_list.movie_ids.append(movie_id)
    movie_list.movie_ids=movie_list.movie_ids+str(movie_id)+";"
    print("after movie_list.movie_ids=", movie_list.movie_ids)

    db.session.add(movie_list)

    db.session.commit()
    return jsonify({"message": "Movie added successfully"}), 200

#its worked
def remove_movie(id,movie_id):
    user_film_instance = UserFilmList.query.get(id)
    
    if user_film_instance:
        movie_id_str=str(movie_id)+";"
        user_film_instance.movie_ids=user_film_instance.movie_ids.replace(movie_id_str,"")
        db.session.commit()
        return jsonify({"message": "Movie removed successfully"}), 200

    else:
        return jsonify({"message": "UserFilmList not found"}), 404
