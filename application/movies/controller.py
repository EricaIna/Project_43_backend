from flask import jsonify
from werkzeug import exceptions
from .models import Movie
from .. import db


def index():
  movies = Movie.query.all()
  try:
      return jsonify({ "data": [m.json for m in movies] }), 200
  except:
      raise exceptions.InternalServerError(f"We are working on it")

def show(id):
    print('id', type(id))
    movie = Movie.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": movie.json }), 200
    except:
        raise exceptions.NotFound(f"You get it")