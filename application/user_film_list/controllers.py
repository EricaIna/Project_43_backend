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
        user_id,title = request.json.values()

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
    pass

def add_movie(id,movie_id):
    pass

def remove_movie(id,movie_id):
    pass
