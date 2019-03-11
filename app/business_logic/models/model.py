import abc
import uuid


class Model(object):

    def __init__(self):
        self.db_id = uuid.UUID()

    @property
    def db_id(self):
        return self.db_id

    @abc.abstractmethod
    def to_dict(self):
        pass

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, json_dict):
        pass
