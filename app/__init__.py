import os
from flask import Flask


def create_app(test_config=None):
    # __name__ is always the name of the current python module (this arg is telling the app object where it's located)
    # instance_relative_config tells the app that config files are relative to the instance/ folder
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DB_FILE =os.path.join(app.instance_path, 'app.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.add_db_commands(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import closet
    app.register_blueprint(closet.bp)

    return app
