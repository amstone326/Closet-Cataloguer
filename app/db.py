import sqlite3

# g is a special Flask object that is unique for each request, and therefore can be used to store data that might be
# accessed by multiple functions during the handling of a single request
# current_app points to the Flask object handling the current request
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DB_FILE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # tells the db connection to return rows that behave like dicts
        g.db.row_factory=sqlite3.Row

    return g.db


def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()