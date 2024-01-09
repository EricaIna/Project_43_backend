from .. import db

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    Title = db.Column(db.String(100), unique=True)
    Content = db.Column(db.String(500))
    Timestamp = db.Column(db.DateTime)
    Rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))
