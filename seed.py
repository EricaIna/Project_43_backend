import pandas as pd
from sqlalchemy import text
from application import db,create_app
from application.auth.models import User
from application.movies.controller import index_and_seed, genres_and_seed
from application.reviews.models import Reviews
from application.user_films_list.models import UserFilmList
from sqlalchemy.sql import insert
from application.movies.models import movie_genre_association


app = create_app("PROD")
db.drop_all()
# db.session.execute(text('DROP TABLE IF EXISTS genres;'))
# db.session.execute(text('DROP TABLE IF EXISTS user_film_lists;'))
# db.session.execute(text('DROP TABLE IF EXISTS reviews;'))
# db.session.execute(text('DROP TABLE IF EXISTS movies;'))

print("Dropping Database")

result = db.session.execute(text('DROP TABLE IF EXISTS movies_dataset;'))

db.session.commit()


db.create_all()
print("Creating database")

print("Saving movies")
index_and_seed()

print("Saving genres")
genres_and_seed()

print("Saving movies dataset")
df = pd.read_csv("./movie_dataset.csv")
df.to_sql(name='movies_dataset', con=db.engine)
print("movies dataset saved")

movie_genre_data = [
    {"movie_id": 1, "genre_id": 36},
    {"movie_id": 1, "genre_id": 10752},
    {"movie_id": 1, "genre_id": 18},
    {"movie_id": 2, "genre_id": 18},
    {"movie_id": 2, "genre_id": 36},
    {"movie_id": 3, "genre_id": 28},
    {"movie_id": 3, "genre_id": 12},
    {"movie_id": 3, "genre_id": 14},
    {"movie_id": 4, "genre_id": 28},
    {"movie_id": 4, "genre_id": 53},
    {"movie_id": 5, "genre_id": 35},
    {"movie_id": 5, "genre_id": 10751},
    {"movie_id": 5, "genre_id": 14},
    {"movie_id": 6, "genre_id": 18},
    {"movie_id": 6, "genre_id": 36},
    {"movie_id": 7, "genre_id": 27},
    {"movie_id": 7, "genre_id": 53},
    {"movie_id": 7, "genre_id": 9648},
    {"movie_id": 8, "genre_id": 878},
    {"movie_id": 8, "genre_id": 18},
    {"movie_id": 8, "genre_id": 28},
    {"movie_id": 9, "genre_id": 16},
    {"movie_id": 9, "genre_id": 10751},
    {"movie_id": 9, "genre_id": 10402},
    {"movie_id": 9, "genre_id": 14},
    {"movie_id": 9, "genre_id": 35},
    {"movie_id": 10, "genre_id": 878},
    {"movie_id": 10, "genre_id": 18},
    {"movie_id": 10, "genre_id": 28},
    {"movie_id": 11, "genre_id": 28},
    {"movie_id": 11, "genre_id": 35},
    {"movie_id": 12, "genre_id": 16},
    {"movie_id": 12, "genre_id": 12},
    {"movie_id": 12, "genre_id": 35},
    {"movie_id": 12, "genre_id": 10751},
    {"movie_id": 13, "genre_id": 28},
    {"movie_id": 13, "genre_id": 53},
    {"movie_id": 14, "genre_id": 16},
    {"movie_id": 14, "genre_id": 14},
    {"movie_id": 14, "genre_id": 10751},
    {"movie_id": 14, "genre_id": 10770},
    {"movie_id": 14, "genre_id": 12},
    {"movie_id": 14, "genre_id": 35},
    {"movie_id": 15, "genre_id": 10749},
    {"movie_id": 15, "genre_id": 18},
    {"movie_id": 16, "genre_id": 16},
    {"movie_id": 16, "genre_id": 35},
    {"movie_id": 16, "genre_id": 14},
    {"movie_id": 16, "genre_id": 12},
    {"movie_id": 16, "genre_id": 10751},
    {"movie_id": 16, "genre_id": 10749},
    {"movie_id": 17, "genre_id": 28},
    {"movie_id": 17, "genre_id": 35},
    {"movie_id": 17, "genre_id": 80},
    {"movie_id": 18, "genre_id": 16},
    {"movie_id": 18, "genre_id": 12},
    {"movie_id": 18, "genre_id": 28},
    {"movie_id": 18, "genre_id": 35},
    {"movie_id": 18, "genre_id": 10751},
    {"movie_id": 19, "genre_id": 878},
    {"movie_id": 19, "genre_id": 27},
    {"movie_id": 19, "genre_id": 878},
    {"movie_id": 20, "genre_id": 27}
]
insert_statement = insert(movie_genre_association).values(movie_genre_data)

try:
    db.session.execute(insert_statement)
    db.session.commit()
    print('hello')
except Exception as e:
    print(f"An error occurred: {e}")

user_list_data = [
    {"user_id": 1, "movies_id": 2},
    {"user_id": 2, "movies_id": 199}
]

for list_info in user_list_data:
    list = UserFilmList(**list_info)
    db.session.add(list)



user_data = [
    {"email": "test@test.com", "password": "test", "name": "test"},
    {"email": "test2@test.com", "password": "test2", "name": "test2"}
]

for user_info in user_data:
    user = User(**user_info)
    db.session.add(user)

# Seed reviews data
print("Saving reviews")
# Manually create some review records and insert them into the 'reviews' table
reviews_data = [
    {"title": "Great Movie", "content": "I loved it!", "rating": 5, "user_id": 1, "movies_id": 1},
    {"title": "Average Movie", "content": "It was okay", "rating": 3, "user_id": 2, "movies_id": 2},
]

for review_info in reviews_data:
    review = Reviews(**review_info)
    db.session.add(review)


db.session.commit()
print("commit")
