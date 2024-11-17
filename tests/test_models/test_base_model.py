import unittest
import json
import os
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Unit test for the BaseModel class"""

    def setUp(self):
        pass

    def test_attr(self):
        my_model = BaseModel()
        self.assertEqual(len(my_model.id), 36)
        self.assertEqual(my_model.id[14], '4')
        self.assertIn(my_model.id[19], '89ab')
        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.created_at), datetime)

    def test_save(self):
        model = BaseModel()
        model.save()
        self.assertEqual(model.updated_at, datetime.now())

    def test_str(self):
        model = BaseModel()
        model.name = "My model"
        self.assertEqual(model, f"[BaseModel] ({model.id}) {model.__dict__}")
        my_model = BaseModel()
        self.assertEqual(my_model, f"[BaseModel] ({my_model.id}) \
                {my_model.__dict__}")
        new_model = BaseModel()
        new_model.name = "My new model"
        self.assertEqual(new_model, f"[BaseModel] ({new_model.id}) \
                {new_model.__dict__}")

    def test_to_dict(self):
        model = BaseModel()
        instance_dict = model.to_dict()
        self.assertIn("__class__", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertEqual(instance_dict.get("__class__"), "BaseModel")
        self.assertEqual(type(instance_dict.get("created_at")), str)
        self.assertEqual(type(instance_dict.get("updated_at")), str)

if __name__ == "__main__":
    unittest.main()
