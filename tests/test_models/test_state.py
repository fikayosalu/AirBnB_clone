import unittest
import json
import os
from models.state import State
from datetime import datetime, timedelta


class TestState(unittest.TestCase):
    """Unit test for the State class"""

    def setUp(self):
        pass

    def test_save(self):
        """Test the save() method"""
        model = State()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertGreater(model.updated_at, old_updated_at)
        self.assertAlmostEqual(model.updated_at, datetime.now(),
                               delta=timedelta(seconds=1))

    def test_to_dict(self):
        model = State()
        instance_dict = model.to_dict()
        self.assertIn("__class__", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertEqual(instance_dict.get("__class__"), "State")
        self.assertEqual(type(instance_dict.get("created_at")), str)
        self.assertEqual(type(instance_dict.get("updated_at")), str)

    def test_class_attr(self):
        self.assertTrue(hasattr(State, "name"))
        self.assertEqual(State.name, "")

    def test_str(self):
        model = State()
        self.assertEqual(str(model), f"[State] \
({model.id}) {model.__dict__}")
        my_model = State()
        my_model.name = "My First Model"
        self.assertEqual(str(my_model), f"[State] \
({my_model.id}) {my_model.__dict__}")
        new_model = State()
        new_model.name = "My new model"
        self.assertEqual(str(new_model), f"[State] ({new_model.id}) \
{new_model.__dict__}")

    def test_init(self):
        model = State()
        model_dict = model.to_dict()
        new_model = State(**model_dict)
        self.assertEqual(type(new_model), State)
        self.assertIn("created_at", new_model.__dict__)
        self.assertIn("updated_at", new_model.__dict__)
        new_dict = new_model.to_dict()
        self.assertEqual(new_dict.get("__class__"), "State")
        self.assertEqual(type(new_dict.get("created_at")), str)
        self.assertEqual(type(new_dict.get("updated_at")), str)


if __name__ == "__main__":
    unittest.main()
