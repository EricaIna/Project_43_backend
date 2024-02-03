from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app(env=None):
    load_dotenv()
    application = Flask(__name__)
    application.json_provider_class.sort_keys = False
    CORS(application)
    
   
    application.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]
    application.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    application.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    application.config["JWT_SECRET_KEY"] = os.environ["JWT_SECRET_KEY"]

    db.init_app(application)
    
    application.app_context().push()


    from src.auth.routes import auth as auth_blueprint
    application.register_blueprint(auth_blueprint)

    from src.routes import main as main_blueprint
    application.register_blueprint(main_blueprint)


    from src.movies.routes import movies_blueprint as movies_blueprint
    application.register_blueprint(movies_blueprint)

    from src.recommendations_list.routes import recommendations_blueprint
    application.register_blueprint(recommendations_blueprint)

    from src.user_films_list.routes import user_film_list_blueprint
    application.register_blueprint(user_film_list_blueprint)

    from src.reviews.routes import reviews_bp
    application.register_blueprint(reviews_bp)


    #This is required to call methods like create_access_toke() and others from Flask-JWT-Extended
    jwt = JWTManager(application)

    return application
    # from application import routes
