from flask import jsonify, request
from werkzeug import exceptions
from .models import UserFilmList
from .. import db


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
        user_id,fav_film_id,title = request.json.values()

        new_movie = UserFilmList(ser_id,fav_film_id,title)

        db.session.add(new_movie)
        db.session.commit()

        return jsonify({ "data": new_movie.json }), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request")



def update(id):
    data = request.json
    movie = UserFilmList.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(movie, attribute):
            setattr(movie, attribute, value)

    db.session.commit()
    return jsonify({ "data": movie.json })

def destroy(id):
    movie = UserFilmList.query.filter_by(id=id).first()
    db.session.delete(movie)
    db.session.commit()
    return "movie Deleted", 204



# Route for searching and adding a movie to the user's list

def search_and_add():
    pass
    # try:
    #     # Get the movie name from front-end
    #     movie_name = request.json.get('movie_name')

    #     movie = Movie.search_movie(movie_name)//how to use the data base?

    #     if movie:

    #         user_id = request.json.get('user_id')

    #         # Check if the movie is already in the user's list to avoid duplicates
    #         if not UserFilmList.is_movie_in_user_list(user_id, movie.id):
    #             # If not, add the movie to the user's list
    #             new_movie = UserFilmList(
    #                 fav_film_id=movie.fav_film_id,
    #                 title=movie.title,
                    
    #                 user_id=user_id  # Associate the movie with the user
    #             )

    #             db.session.add(new_movie)
    #             db.session.commit()

    #             return jsonify({"data": new_movie.json}), 201
    #         else:
    #             return jsonify({"message": "Movie already in user's list"}), 400
    #     else:
    #         return jsonify({"message": "Movie not found"}), 404
    # except IntegrityError:
    #     db.session.rollback()
    #     return jsonify({"message": "IntegrityError occurred"}), 500
    # except Exception as e:
    #     return jsonify({"message": f"We cannot process your request. Error: {str(e)}"}), 500

