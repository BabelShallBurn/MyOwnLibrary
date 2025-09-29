

# MyOwnLibrary

MyOwnLibrary is a simple Flask web application for managing a personal library. It allows you to add, view, search, sort, and delete books and authors.

## Features
- Add books and authors
- Sort books by title, year, or author
- Search for books (including substrings)
- Delete books with confirmation and success message
- SQLite database using SQLAlchemy
- User-friendly web interface

## Installation
1. Clone the repository:
	```bash
	git clone https://github.com/BabelShallBurn/MyOwnLibrary.git
	cd MyOwnLibrary
	```
2. Create and activate a Python virtual environment:
	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```
3. Install dependencies:
	```bash
	pip install flask flask_sqlalchemy
	```

## Usage
1. Start the application:
	```bash
	python app.py
	```
2. Open in your browser: [http://localhost:5001/home](http://localhost:5001/home)

## Project Structure
```
app.py                # Main application
README.md             # This guide
requirements.txt      # (optional) Python dependencies
/data/library.sqlite  # SQLite database
/templates/           # HTML templates
data_models.py        # Database models
```

