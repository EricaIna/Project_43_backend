from flask import Flask, request, jsonify
from flask_login import login_required, current_user
from .models import Movies
from .controllers import (
    create_review,
    get_reviews,
    update_review,
    delete_review
)

app = Flask(__name__)

@app.route('/reviews', methods=['POST'])
@login_required
def create_review_route():
    data = request.json
    movie_id = data.get('movie_id')
    title = data.get('title')
    content = data.get('content')
    rating = data.get('rating')
    user_id = current_user.id
    result = create_review(movie_id, title, content, rating, user_id)
    return jsonify(result)

@app.route('/reviews/<int:movie_id>', methods=['GET'])
def get_reviews_route(movie_id):
    result = get_reviews(movie_id)
    return jsonify(result)

@app.route('/reviews/<int:review_id>', methods=['PATCH'])
@login_required
def update_review_route(review_id):
    new_data = request.json
    
