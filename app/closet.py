import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from auth import login_required
from db import get_db

bp = Blueprint('closet', __name__)


@bp.route('/')
@login_required
def index():
    db = get_db()
    curr_user_id = session['user_id']

    three_weeks_ago = datetime.datetime.now() - datetime.timedelta(weeks=3)
    not_recently_worn = db.execute(
        'SELECT short_desc, article_type, user_id, last_wear, brandname '
        'FROM articles JOIN brands ON articles.brand_id = brands.id '
        'WHERE user_id = ? AND last_wear < ?',
        (curr_user_id, three_weeks_ago,)).fetchall()

    #one_week_ago = datetime.datetime.now() - datetime.timedelta(weeks=1)
    #new_outfits = db.execute('SELECT * FROM outfits WHERE user_id = ? AND added > ?',
     #                        (curr_user_id, one_week_ago,)).fetchall()

    return render_template('closet/landing.html', articles=not_recently_worn)#, outfits=new_outfits)


@bp.route('/clothing')
def clothing():
    pass

