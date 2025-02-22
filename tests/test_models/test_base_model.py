import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime, timedelta


class TestBaseModel(unittest.TestCase):
    """Unit test for the BaseModel class"""

    def test_save(self):
        """Test the save() method"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertGreater(model.updated_at, old_updated_at)
        self.assertAlmostEqual(model.updated_at, datetime.now(),
                               delta=timedelta(seconds=1))

    def test_to_dict(self):
        """Test the to_dict() method"""
        model = BaseModel()
        instance_dict = model.to_dict()
        self.assertIn("__class__", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertEqual(instance_dict.get("__class__"), "BaseModel")
        self.assertEqual(type(instance_dict.get("created_at")), str)
        self.assertEqual(type(instance_dict.get("updated_at")), str)

    def test_str(self):
        """Test the str method"""
        model = BaseModel()
        self.assertEqual(str(model), f"[BaseModel] \
({model.id}) {model.__dict__}")
        my_model = BaseModel()
        my_model.name = "My First Model"
        self.assertEqual(str(my_model), f"[BaseModel] \
({my_model.id}) {my_model.__dict__}")
        new_model = BaseModel()
        new_model.name = "My new model"
        self.assertEqual(str(new_model), f"[BaseModel] ({new_model.id}) \
{new_model.__dict__}")

    def test_init(self):
        """Test the init method"""
        model = BaseModel()
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(type(new_model), BaseModel)
        self.assertIn("created_at", new_model.__dict__)
        self.assertIn("updated_at", new_model.__dict__)
        new_dict = new_model.to_dict()
        self.assertEqual(new_dict.get("__class__"), "BaseModel")
        self.assertEqual(type(new_dict.get("created_at")), str)
        self.assertEqual(type(new_dict.get("updated_at")), str)


if __name__ == "__main__":
    unittest.main()
