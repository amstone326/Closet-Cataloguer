from app.business_logic.models import Brand
from app.storage import app_storage


def get_brand(brand_id):
    return app_storage.get_model_by_id(Brand, brand_id)