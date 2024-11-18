import unittest
import json
import os
from models.city import City
from datetime import datetime, timedelta


class TestCity(unittest.TestCase):
    """Unit test for the City class"""

    def setUp(self):
        pass

    def test_save(self):
        """Test the save() method"""
        model = City()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertGreater(model.updated_at, old_updated_at)
        self.assertAlmostEqual(model.updated_at, datetime.now(),
                               delta=timedelta(seconds=1))

    def test_to_dict(self):
        model = City()
        instance_dict = model.to_dict()
        self.assertIn("__class__", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertEqual(instance_dict.get("__class__"), "City")
        self.assertEqual(type(instance_dict.get("created_at")), str)
        self.assertEqual(type(instance_dict.get("updated_at")), str)

    def test_str(self):
        model = City()
        self.assertEqual(str(model), f"[City] \
({model.id}) {model.__dict__}")
        my_model = City()
        my_model.name = "My First Model"
        self.assertEqual(str(my_model), f"[City] \
({my_model.id}) {my_model.__dict__}")
        new_model = City()
        new_model.name = "My new model"
        self.assertEqual(str(new_model), f"[City] ({new_model.id}) \
{new_model.__dict__}")

    def test_init(self):
        model = City()
        model_dict = model.to_dict()
        new_model = City(**model_dict)
        self.assertEqual(type(new_model), City)
        self.assertIn("created_at", new_model.__dict__)
        self.assertIn("updated_at", new_model.__dict__)
        new_dict = new_model.to_dict()
        self.assertEqual(new_dict.get("__class__"), "City")
        self.assertEqual(type(new_dict.get("created_at")), str)
        self.assertEqual(type(new_dict.get("updated_at")), str)


if __name__ == "__main__":
    unittest.main()
