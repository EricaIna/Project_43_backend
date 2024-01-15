from .. import db
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

movie_genre_association = Table(
    'movie_genre_association',
    db.Model.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('genre_id', Integer, ForeignKey('genres.api_id'))
)

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    original_language = db.Column(db.String(3), nullable=False)
    original_title = db.Column(db.String(300), nullable=False)
    overview = db.Column(db.String(1000), nullable=False)
    vote_average = db.Column(db.Float, nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    poster_path = db.Column(db.String(200), nullable=True)
    # Define the many-to-many relationship
    genres = db.relationship('Genre', secondary=movie_genre_association, back_populates='movies', uselist=True)


    def __init__(self, original_title, original_language, overview, vote_average, release_date, poster_path, genres): # constructor
        self.original_language = original_language
        self.original_title = original_title
        self.overview = overview
        self.vote_average = vote_average
        self.release_date = release_date
        self.poster_path = poster_path
        self.genres = genres


    def __repr__(self):
        return f"Movie(id:  {self.id}, name: {self.original_title})"
    
    @property
    def poster_url(self):
        base_url = "https://image.tmdb.org/t/p/w500"
        return f"{base_url}{self.poster_path}" if self.poster_path else None

    @property
    def json(self): # create a json from of an instance
        return {
            "id": self.id,
            "original_title": self.original_title,
            "original_language": self.original_language,
            "overview": self.overview,
            "vote_average": self.vote_average,
            "release_date": self.release_date,
            "poster_path": self.poster_path,
            "genres": self.genres
        }



class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True)
    api_id = db.Column(db.Integer, unique=True, nullable=True)
    name = db.Column(db.String(200), nullable=False)
    # Define the many-to-many relationship
    movies = db.relationship('Movie', secondary=movie_genre_association, back_populates='genres')


    def __init__(self, api_id, name, movies): # constructor
        self.api_id = api_id
        self.name = name  
        self.movies = movies     


    def __repr__(self):
        return f"Genre(id:  {self.id}, api_id: {self.api_id}, name: {self.name})"

    @property
    def json(self): # create a json from of an instance
        return {
            "id": self.id,
            "api_id": self.api_id,
            "name": self.name
        }
    
# db.ForeignKeyConstraint(['genres_id'], ['genres.api_id'])
