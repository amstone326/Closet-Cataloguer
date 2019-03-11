import time

from .model import Model
from ..get_set.brands import get_brand
from ..get_set.users import get_user


class Article(Model):

    def __init__(self, article_type, owner, description=None, brand=None, occasion=None):
        super().__init__()
        self.article_type = article_type
        self.owner = owner
        self.description = description
        self.brand = brand
        self.occasion = occasion
        self.added_at = time.time()
        self.wears = []

    def record_wear(self):
        self.wears.append(time.time())

    def to_dict(self):
        return {
            "id": self.db_id,
            "article_type": self.article_type,
            "owner_id": self.owner.id,
            "description": self.description,
            "brand_id": self.brand.id,
            "occasion": self.occasion,
            "added_at": self.added_at,
            "wears": self.wears,
        }

    @classmethod
    def from_dict(cls, json_dict):
        owner = get_user(json_dict["owner_id"])
        brand = get_brand(json_dict["brand_id"])
        return Article(json_dict["article_type"], owner, json_dict["description"], brand, json_dict["occasion"])
