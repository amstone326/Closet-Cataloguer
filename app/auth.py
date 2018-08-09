
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from db import get_db


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', method=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Missing username.'
        if not password:
            error = 'Missing password.'

        if error is None:
            db = get_db()
            db.execute(
                'INSERT INTO users (username, password) VALUES (?, ?)', (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))
        else:
            flash(error)  # stores the error message such that it can be retrieved when rendering the template

    return render_template('auth/register.html')


@bp.route('/login', method=('GET', 'POST'))
def login():
    return render_template('auth/login.html')

