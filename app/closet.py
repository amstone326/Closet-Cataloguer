import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from auth import login_required
from db import get_db


bp = Blueprint('closet', __name__)
ARTICLE_TYPES = ["pants", "blouses", "tshirts", "sweaters", "cardigans", "skirts", "dresses"]


@bp.route('/')
@login_required
def index():
    db = get_db()
    curr_user_id = session['user_id']

    three_weeks_ago = datetime.datetime.now() - datetime.timedelta(weeks=3)
    not_recently_worn = db.execute(
        'SELECT short_desc, article_type, user_id, last_wear, brandname '
        'FROM articles JOIN brands ON articles.brand_id = brands.id '
        'WHERE (user_id = ?) AND (last_wear is null OR last_wear < ?)',
        (curr_user_id, three_weeks_ago,)).fetchall()

    #one_week_ago = datetime.datetime.now() - datetime.timedelta(weeks=1)
    #new_outfits = db.execute('SELECT * FROM outfits WHERE user_id = ? AND added > ?',
     #                        (curr_user_id, one_week_ago,)).fetchall()

    return render_template('closet/landing.html', articles=not_recently_worn)#, outfits=new_outfits)


@bp.route('/clothing')
@login_required
def clothing():
    db = get_db()
    curr_user_id = session['user_id']

    all_articles = db.execute('SELECT * FROM articles WHERE user_id = ?', (curr_user_id,)).fetchall()
    brand_names = db.execute('SELECT brandname FROM brands').fetchall()
    all_brands = db.execute('SELECT * FROM brands').fetchall()

    return render_template('closet/articles.html',
                           articles=all_articles, brands=all_brands,
                           type_options=ARTICLE_TYPES, brand_options=brand_names)


@bp.route('/add_article')
def add_article():
    pass
