import json
from pathlib import Path
from datetime import datetime
from book_library_app import app, db
from book_library_app.models import Author


@app.cli.group()
def db_manage():
    """Database management commands
    """
    pass


@db_manage.command()
def add_data():
    """Add sample data to the database
    """
    authors_path = Path(__file__).parent / 'samples' / 'authors.json'
    with open(authors_path) as file:
        data_json = json.load(file)
    for item in data_json:
        item['birth_date'] = datetime.strptime(
            item['birth_date'], '%d-%m-%Y').date()
        author = Author(**item)
        db.session.add(author)
    db.session.commit


@db_manage.command()
def remove_data():
    """Remove all data from the database
    """
    pass