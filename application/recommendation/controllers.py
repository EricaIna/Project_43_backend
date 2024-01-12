import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import g
# from .. import db

def get_model():
    if 'model' not in g:
        g.model = train_model()
    return g.model

#make data frame availible to the flask app
# def get_df():
#     if 'df' not in g:
#         g.df = pd.read_sql(sql='movies', con=db.engine)
#     return g.df

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]


def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


def train_model():
    # df = pd.read_sql(sql='movies', con=db.engine)
    # df=get_df()
    df = pd.read_csv("movie_dataset.csv")
    features = ['keywords', 'cast', 'genres', 'director']

    def combine_features(row):
        return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]

    for feature in features:
        df[feature] = df[feature].fillna('')
    df["combined_features"] = df.apply(combine_features, axis=1)
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    print("train model")
    return cosine_sim


def recommend_movie(movie_ids):
    #doing the list from movie_ids
    list_of_movie_ids=movie_ids.split(";")
    list_of_movie_ids = [int(movie_id) for movie_id in list_of_movie_ids] #make the list integer
    #movie_index = get_index_from_title(movie_ids[0])
    cosine_sim=train_model() #delete this line
    list_of_the_best_movie=[]
    for movie_id in list_of_movie_ids:
        # similar_movies = list(enumerate(get_model()[movie_id])) #need to iterate over movie_ids instead
        similar_movies = list(enumerate(cosine_sim[movie_id]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]
        list_of_the_best_movie.append(sorted_similar_movies[0])
        
        
    # sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]
    # print(sorted_similar_movies)
    # return sorted_similar_movies[0]
    return list_of_the_best_movie

    #i = 0
    #print("Top 5 similar movies to " + movie_user_likes + " are:\n")
    #for element in sorted_similar_movies:
    #    print(get_title_from_index(element[0]))
    #    i = i + 1
    #    if i >= 5:
    #        break

# cos_sim=train_model()
# print(len(cos_sim))
movie_ids_like="7;8;9"
# print(recommend_movie(movie_ids_like))
recommend_movie(movie_ids_like)
