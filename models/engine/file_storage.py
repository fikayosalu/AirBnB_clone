#!/usr/bin/python3
"""file_storage module"""
import json
import models.base_model


class FileStorage:
    """
    Serializes instances to a JSON file and Deserializes JSON
    file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON file (path: __file_path)"""
        json_dict = {key: obj.to_dict() for key,
                     obj in self.__objects.items()}
        print(json_dict)
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(json_dict))

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(**dictionary)
        return dummy

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON)
        exists; otherwise, do nothing"""
        try:
            with open(self.__file_path, "r") as file:
                content = file.read()
                json_dict = json.loads(content)
                class_name = "BaseModel"
                cls = eval(class_name)
                self.__ojects = {key: base_model.cls.create(**obj) for key,
                                 obj in json_dict.items()}
        except (FileNotFoundError):
            pass
