from flask import request
from werkzeug import exceptions
from application import app # app from __init__.py
from .controller import index, show

@app.route('/movies', methods=["GET"])
def handle_movies():    
    if request.method == "GET": return index()

@app.route('/movies/<int:id>', methods=["GET"])
def handle_movie(id):
    if request.method == "GET": return show(id)


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}" }, 500


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err}" }, 500


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400