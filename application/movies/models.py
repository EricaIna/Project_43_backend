# from .. import db

# class Movies(db.Model):
#     __tablename__ = "movies"
#     id = db.Column(db.Integer, primary_key=True)
#     index = db.Column(db.Integer, nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     population = db.Column(db.Integer, nullable=False)
#     capital_city = db.Column(db.String(100), nullable=False)

#     def __init__(self, name, population, capital_city): # constructor
#         self.name = name
#         self.population = population
#         self.capital_city = capital_city


#     def __repr__(self):
#         return f"Character(id:  {self.id}, name: {self.name})"

#     @property
#     def json(self): # create a json from of an instance
#         return {
#             "id": self.id,
#             "name": self.name,
#             "population": self.population,
#             "capital_city": self.capital_city
#         }