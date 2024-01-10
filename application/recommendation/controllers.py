import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import g
from .. import db

def get_model():
    if 'model' not in g:
        g.model = train_model()
    return g.model

#make data frame availible to the flask app
def get_df():
    if 'df' not in g:
        g.df = pd.read_sql(sql='movies', con=db.engine)
    return g.df

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]


def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


def train_model():
    # df = pd.read_sql(sql='movies', con=db.engine)
    df=get_df()
    features = ['keywords', 'cast', 'genres', 'director']

    def combine_features(row):
        return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]

    for feature in features:
        df[feature] = df[feature].fillna('')
    df["combined_features"] = df.apply(combine_features, axis=1)
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    return cosine_sim


def recommend_movie(movie_ids):
    #movie_index = get_index_from_title(movie_ids[0])
    similar_movies = list(enumerate(get_model()[movie_ids[0]])) #need to iterate over movie_ids instead

    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

    return sorted_similar_movies[0]

    #i = 0
    #print("Top 5 similar movies to " + movie_user_likes + " are:\n")
    #for element in sorted_similar_movies:
    #    print(get_title_from_index(element[0]))
    #    i = i + 1
    #    if i >= 5:
    #        break
