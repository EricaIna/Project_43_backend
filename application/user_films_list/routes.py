from flask import request, Blueprint
from werkzeug import exceptions
from .controller import add_to_user_list, remove_from_user_list, get_user_film_list

user_film_list_blueprint = Blueprint('user_film_list_blueprint', __name__)

@user_film_list_blueprint.route('/user-film-list/add', methods=["POST"])
def handle_add_to_user_list():
    if request.method == "POST":
        data = request.json
        user_id = data.get('user_id')
        movie_id = data.get('movie_id')
        return add_to_user_list(user_id, movie_id)

@user_film_list_blueprint.route('/user-film-list/remove', methods=["DELETE"])
def handle_remove_from_user_list():
    if request.method == "DELETE":
        data = request.json
        user_id = data.get('user_id')
        movie_id = data.get('movie_id')
        return remove_from_user_list(user_id, movie_id)

@user_film_list_blueprint.route('/user-film-list/<int:user_id>', methods=["GET"])
def handle_get_user_film_list(user_id):
    if request.method == "GET":
        return get_user_film_list(user_id)

@user_film_list_blueprint.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {"error": f"Oops {err}"}, 404

@user_film_list_blueprint.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {"error": f"Oops {err}"}, 500

@user_film_list_blueprint.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {"error": f"Oops {err}"}, 400
