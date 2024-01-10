import pandas as pd
from sqlalchemy import text
from application import db,create_app
from application.auth.models import User

app = create_app("PROD")

db.drop_all()
print("Dropping Database")

result = db.session.execute(text('DROP TABLE IF EXISTS movies;'))
db.session.commit()

db.create_all()
print("Creating database")

print("saving movies")
df = pd.read_csv("../movie_dataset.csv")
df.to_sql(name='movies', con=db.engine)
print("movies dataset saved")

db.session.commit()
print("commit")

