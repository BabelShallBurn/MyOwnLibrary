import os
from flask import flash, Flask, jsonify, request, redirect, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book
from datetime import datetime

app = Flask(__name__)
"""
Flask application for managing a personal library.
Provides routes for adding authors, adding books, viewing the library, and deleting books.
Uses SQLite as the database backend via SQLAlchemy.
"""
app.secret_key = "my_super_secret_key_123456789!"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"

db.init_app(app)

with app.app_context():
    db.create_all()
 
@app.route('/add_author', methods=['POST', 'GET'])
def add_author():
    """
    Route for adding a new author to the database.
    Handles GET (form display) and POST (form submission).
    Converts date strings to Python date objects.
    Redirects to the homepage after successful addition.
    """
    if request.method == 'POST':
        name = request.form['name']
        birth_date = request.form['birthdate']
        date_of_death = request.form['date_of_death']

        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date() if birth_date else None
        date_of_death = datetime.strptime(date_of_death, "%Y-%m-%d").date() if date_of_death else None

        new_author = Author(name=name, birth_date=birth_date, date_of_death=date_of_death)
        db.session.add(new_author)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add_author.html')


@app.route('/add_book', methods=['POST', 'GET'])
def add_book():
    """
    Route for adding a new book to the database.
    Handles GET (form display) and POST (form submission).
    Converts year and author_id to integers.
    Redirects to the homepage after successful addition.
    """
    authors = Author.query.all()
    if request.method == 'POST':
        title = request.form['title']
        author_id = request.form['author_id']
        publication_year = request.form['publication_year']
        isbn = request.form['isbn']

        publication_year = int(publication_year) if publication_year else None
        author_id = int(author_id) if author_id else None

        new_book = Book(title=title, author_id=author_id, publication_year=publication_year, isbn=isbn)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add_book.html', authors=authors)


@app.route('/home')
def home():
    """
    Homepage route displaying all books and authors.
    Supports sorting by year, author, or title via GET parameters.
    Supports searching for books by substring in the title.
    """
    sort = request.args.get('sort')
    search = request.args.get('search')
    query = db.session.query(Book, Author).join(Author, Book.author_id == Author.id)
    if search:
        query = query.filter(Book.title.ilike(f"%{search}%"))
    if sort == 'year':
        query = query.order_by(Book.publication_year)
    elif sort == 'author':
        query = query.order_by(Author.name)
    elif sort == 'title':
        query = query.order_by(Book.title)
    books_with_authors = query.all()
    return render_template('home.html', books_with_authors=books_with_authors)


@app.route('/book/<int:book_id>/delete', methods=['POST'])
def book_delete(book_id):
    """
    Route for deleting a specific book from the database.
    Handles POST requests only.
    Redirects to the homepage and displays a success or error message.
    """
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        flash(f"Book '{book.title}' deleted successfully!", "success")
    else:
        flash("Book not found.", "error")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)



