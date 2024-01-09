from flask import jsonify
from werkzeug import exceptions
import psycopg2

conn = psycopg2.connect(
    dbname='project43',
    user='project43_user',
    password='9Hsx4-UterQiMEW013_UILMAMqIcMAXf',
    host='83.229.75.156',
    port='4000'
)

cursor = conn.cursor()


def index():
     movies = cursor.fetchall()
     print(movies)
     try:
        data = []
        for movie in movies:
            data.append(movie.json)

        return jsonify({
            "data": [m.json for m in movies] }), 200
     except:
        raise exceptions.InternalServerError(f"We are working on it")

def show(id):
    print('id', type(id))
    movie = cursor.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": movie.json }), 200
    except:
        raise exceptions.NotFound(f"You get it")