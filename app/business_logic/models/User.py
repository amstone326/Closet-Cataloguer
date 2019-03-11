from app.business_logic.models.model import Model


# TODO: start here
class User(Model):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, json_dict):
        pass
