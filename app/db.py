import sqlite3
import click

# g is a special Flask object that is unique for each request, and therefore can be used to store data that might be
# accessed by multiple functions during the handling of a single request
# current_app points to the Flask object handling the current request
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DB_FILE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # tells the db connection to return rows that behave like dicts
        g.db.row_factory=sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as schema_file:
        db.executescript(schema_file.read().decode('utf-8'))


@click.command('init-db')
@with_appcontext  # this just makes the app context available when the command is executed
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


def add_db_commands(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)  # this enables us to run init_db from the terminal using `$ flask init_db`
