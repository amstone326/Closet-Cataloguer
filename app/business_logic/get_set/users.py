from app.business_logic.models import User
from app.storage import app_storage


def create_user():
    app_storage.save(User())


def get_user(user_id):
    return app_storage.get_model_by_id(User, user_id)