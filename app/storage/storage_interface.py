import abc


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def save(self, model_object):
        pass

    @abc.abstractmethod
    def get_model_by_id(self, model_class, model_id):
        pass
