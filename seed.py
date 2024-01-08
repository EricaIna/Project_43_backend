from application import db,create_app
from application.auth.models import User

app = create_app("PROD")

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating database")

#entry1 = Book(title="War and Peace", author="Leo Tolstoy", genre="Historical Fiction", publication_year=1869)
#entry2 = Book(title="Crime and Punishment", author="Fyodor Dostoevsky", genre="Psychological Thriller", publication_year=1866)
#entry3 = Book(title="Anna Karenina", author="Leo Tolstoy", genre="Romance", publication_year=1877)
#entry4 = Book(title="The Master and Margarita", author="Mikhail Bulgakov", genre="Fantasy", publication_year=1967)
#entry5 = Book(title="Doctor Zhivago", author="Boris Pasternak", genre="Epic Poetry", publication_year=1957)
#entry6 = Book(title="One Day in the Life of Ivan Denisovich", author="Aleksandr Solzhenitsyn", genre="Political Fiction", publication_year=1962)
#entry7 = Book(title="The Brothers Karamazov", author="Fyodor Dostoevsky", genre="Philosophical Novel", publication_year=1880)
#entry8 = Book(title="The Idiot", author="Fyodor Dostoevsky", genre="Tragicomedy", publication_year=1869)
#entry9 = Book(title="Quiet Flows the Don", author="Mikhail Sholokhov", genre="Historical Novel", publication_year=1928)
#entry10 = Book(title="Dead Souls", author="Nikolai Gogol", genre="Satirical Novel", publication_year=1842)

#db.session.add(entry1)
#print("add entry1")
#db.session.add_all([entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10])
#print("add entry123456")
db.session.commit()
print("commit")

