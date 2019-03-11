import json

from app.storage.storage_interface import StorageInterface
from app.business_logic.models import Article

MODEL_CLASS_TO_FILENAME = {
    Article: "articles.json",
}


def file_for_model(model_class):
    assert model_class in MODEL_CLASS_TO_FILENAME, "Unexpected model class: {}".format(model_class)
    return "files/{}".format(MODEL_CLASS_TO_FILENAME[model_class])


def get_stored_objects_for_model(model_class):
    return json.loads(open(file_for_model(model_class)).read())


def get_object_with_id(json_objects, model_id):
    return json_objects[model_id] if model_id in json_objects else None


class JsonStorageInterface(StorageInterface):

    def get_model_by_id(self, model_class, model_id):
        json_obj = get_object_with_id(get_stored_objects_for_model(model_class), model_id)
        return model_class.from_dict(json_obj) if json_obj else None

    def save(self, model_object):
        stored_objects = get_stored_objects_for_model(type(model_object))
        stored_objects[model_object.db_id] = model_object.to_dict()
        f = open(file_for_model(type(model_object)), "w")
        f.write(stored_objects)
