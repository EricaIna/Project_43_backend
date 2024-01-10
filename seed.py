import pandas as pd
from sqlalchemy import text
from application import db,create_app
from application.auth.models import User
from application.reviews.models import Reviews

app = create_app("PROD")

db.drop_all()
print("Dropping Database")

result = db.session.execute(text('DROP TABLE IF EXISTS movies;'))
db.session.commit()


print("saving movies")
df = pd.read_csv("./movie_dataset.csv")
df.to_sql(name='movies', con=db.engine)
print("movies dataset saved")

db.create_all()
print("Creating database")

# Seed reviews data
print("Saving reviews")
# Manually create some review records and insert them into the 'reviews' table
reviews_data = [
    {"Title": "Great Movie", "Content": "I loved it!", "Rating": 5, "user_id": 1, "movie_id": 1},
    {"Title": "Average Movie", "Content": "It was okay", "Rating": 3, "user_id": 2, "movie_id": 2},
    # Add more review records as needed
]

for review_info in reviews_data:
    review = Reviews(**review_info)
    db.session.add(review)


db.session.commit()
print("commit")
