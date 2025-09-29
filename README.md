
# MyOwnLibrary

MyOwnLibrary ist eine einfache Flask-Webanwendung zur Verwaltung einer persönlichen Bibliothek. Sie ermöglicht das Hinzufügen, Anzeigen, Suchen, Sortieren und Löschen von Büchern und Autoren.

## Features
- Bücher und Autoren hinzufügen
- Bücher nach Titel, Jahr oder Autor sortieren
- Suche nach Büchern (auch mit Substrings)
- Bücher löschen mit Bestätigung und Erfolgsmeldung
- SQLite-Datenbank mit SQLAlchemy
- Übersichtliche Weboberfläche

## Installation
1. Repository klonen:
	```bash
	git clone https://github.com/BabelShallBurn/MyOwnLibrary.git
	cd MyOwnLibrary
	```
2. Python-Umgebung erstellen und aktivieren:
	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```
3. Abhängigkeiten installieren:
	```bash
	pip install flask flask_sqlalchemy
	```

## Nutzung
1. Starte die Anwendung:
	```bash
	python app.py
	```
2. Öffne im Browser: [http://localhost:5001/home](http://localhost:5001/home)

## Projektstruktur
```
app.py                # Hauptanwendung
README.md             # Diese Anleitung
requirements.txt      # (optional) Python-Abhängigkeiten
/data/library.sqlite  # SQLite-Datenbank
/templates/           # HTML-Templates
data_models.py        # Datenbankmodelle
```

