from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
        
    __tablename__ = 'authors'

    def __init__(self, name, birth_date=None, date_of_death=None):
        self.name = name
        self.birth_date = birth_date
        self.date_of_death = date_of_death

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)

    def __repr__(self):
        return f"author={self.name} birth_date={self.birth_date}, date_of_death={self.date_of_death}"
    
    def __str__(self) -> str:
        return f"Authors name is {self.name} born {self.birth_date} and died {self.date_of_death}"

class Book(db.Model):
    
    __tablename__ = 'books'
    
    def __init__(self, title, author_id=None, publication_year=None, isbn=None):
        self.title = title
        self.author_id = author_id
        self.publication_year = publication_year
        self.isbn = isbn

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    title = db.Column(db.String)
    publication_year = db.Column(db.Integer)
    isbn = db.Column(db.String)

    author = db.relationship('Author', backref=db.backref('books', lazy=True))

    def __repr__(self):
        return f"title={self.title}, publication_year={self.publication_year}, ISBN={self.isbn}"
    
    def __str__(self) -> str:
        return f"Book title is {self.title} published in {self.publication_year} with ISBN {self.isbn}"
