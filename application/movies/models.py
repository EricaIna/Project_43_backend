from .. import db

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    genres = db.Column(db.String(200), nullable=False)
    original_language = db.Column(db.String(3), nullable=False)
    original_title = db.Column(db.String(300), nullable=False)
    overview = db.Column(db.String(1000), nullable=False)
    vote_average = db.Column(db.Float, nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    director = db.Column(db.String(100), nullable=False)


    def __init__(self, original_title, genres, original_language, overview, vote_average, release_date, director): # constructor
        self.genres = genres
        self.original_language = original_language
        self.original_title = original_title
        self.overview = overview
        self.vote_average = vote_average
        self.release_date = release_date
        self.director = director


    def __repr__(self):
        return f"Movie(id:  {self.id}, name: {self.original_title})"

    @property
    def json(self): # create a json from of an instance
        return {
            "id": self.id,
            "original_title": self.original_title,
            "original_language": self.original_language,
            "overview": self.overview,
            "genres": self.genres,
            "vote_average": self.vote_average,
            "release_date": self.release_date,
            "director": self.director
        }