from app.business_logic.models.Article import Article
from app.storage import app_storage


def create_new_article(article_type, owner, description=None, brand=None, occasion=None):
    app_storage.save(Article(article_type, owner, description, brand, occasion))


def list_clothing_items(brand=None, article_type=None, worn_since=None):
    pass
