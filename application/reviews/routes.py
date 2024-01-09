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

# Create review
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

# Get reviews
@app.route('/reviews/<int:movie_id>', methods=['GET'])
def get_reviews_route(movie_id):
    result = get_reviews(movie_id)
    return jsonify(result)

# Update reviews
@app.route('/reviews/<int:review_id>', methods=['PATCH'])
@login_required
def update_review_route(review_id):
    new_data = request.json
    user_id = current_user.id
    result = update_review(review_id, user_id, new_data)
    return jsonify(result)

# Delete review
@app.route('/reviews/<int:review_id>', methods=['DELETE'])
@login_required
def delete_review_route(review_id):
    user_id = current_user.id
    result = delete_review(review_id, user_id)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
    
