import json
from flask import Flask, request, Blueprint
from flask_jwt_extended import jwt_required, JWTManager
from .controllers import refresh_expiring_jwts, create_token, my_profile, logout, user_signup

auth = Blueprint('auth', __name__)
#jwt = JWTManager(auth)


@auth.after_request
def handle_after_auth_request(request):
    return refresh_expiring_jwts(request)


@auth.route('/signup', methods=["POST"])
def handle_signup():
    return user_signup()


@auth.route('/login', methods=["POST"])
def handle_login():
    return create_token()


@auth.route('/profile')
@jwt_required()
def handle_my_profile():
    return my_profile()


@auth.route("/logout", methods=["POST"])
def handle_logout_post():
    return logout()
