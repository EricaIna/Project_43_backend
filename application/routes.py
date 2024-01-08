from flask import jsonify, Blueprint

main = Blueprint("main", __name__)

@main.route('/')
def hello():
    return jsonify({
        "message": "Welcome to the La Fosse final project application",
    }), 200

@main.route('/profile')
def profile():
    return 'Profile'
