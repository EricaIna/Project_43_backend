from flask import request, Blueprint
from werkzeug import exceptions
from .controllers import index, create, show, update, destroy

movies_list = Blueprint("movies_list", __name__)

@movies_list.route('/movies_list', methods=["GET", "POST"])
def handle_movies():
    if request.method == "POST": return create()
    if request.method == "GET": return index()

@movies_list.route('/movies_list/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_movie_list(id):
    if request.method == "GET": return show(id)
    if request.method == "PATCH": return update(id)
    if request.method == "DELETE": return destroy(id)


@movies_list.route('/movies_list_manage/<int:id>/<int:movie_id>', methods=["GET", "PATCH", "DELETE"])
def handle_movie(id):
    if request.method == "GET": return show_movie_details(id,movie_id)
    if request.method == "PATCH": return add_movie(id,movie_id)
    if request.method == "DELETE": return remove_movie(id,movie_id)


@movies_list.route('/movies_list_recommend/<int:id>', methods=["PATCH"])
def recommend_movie():
    if request.method == "PATCH": return recommend(id)


@movies_list.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404

@movies_list.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500

@movies_list.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400

# Route for searching and adding a movie to the user's list
@movies_list.route('/search-and-add', methods=['POST'])
def handle_search_and_add():
    return search_and_add()
