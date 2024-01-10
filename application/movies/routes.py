from flask import request, Blueprint
from werkzeug import exceptions
from application import create_app # app from __init__.py
from .controller import index, show

movies_blueprint = Blueprint('movies_blueprint', __name__)
# app = create_app()

@movies_blueprint.route('/movies', methods=["GET"])
def handle_movies():    
    if request.method == "GET": return index()

@movies_blueprint.route('/movies/<int:id>', methods=["GET"])
def handle_movie(id):
    if request.method == "GET": return show(id)


@movies_blueprint.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}" }, 404


@movies_blueprint.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err}" }, 500


@movies_blueprint.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400