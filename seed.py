import pandas as pd
from application import db,create_app
from application.auth.models import User

app = create_app("PROD")

db.drop_all()
print("Dropping Database")

#Need to add explicit drop of movies table

db.create_all()
print("Creating database")

print("saving movies")
df = pd.read_csv("../movie_dataset.csv")
df.to_sql(name='movies', con=db.engine)
print("movies dataset saved")

#print("add entry123456")
db.session.commit()
print("commit")


