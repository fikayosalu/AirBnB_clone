#!/usr/bin/python3
"""file_storage module"""
import json


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
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON)
        exists; otherwise, do nothing"""
        try:
            with open(self.__file_path, "r") as file:
                content = file.read()
                json_dict = json.loads(content)
                self.__objects = json_dict
        except (FileNotFoundError):
            pass
