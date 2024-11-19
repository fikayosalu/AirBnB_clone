import unittest
import json
import os
from models.user import User
from datetime import datetime, timedelta


class TestUser(unittest.TestCase):
    """Unit test for the User class"""

    def setUp(self):
        pass

    def test_save(self):
        """Test the save() method"""
        model = User()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertGreater(model.updated_at, old_updated_at)
        self.assertAlmostEqual(model.updated_at, datetime.now(),
                               delta=timedelta(seconds=1))

    def test_to_dict(self):
        model = User()
        instance_dict = model.to_dict()
        self.assertIn("__class__", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertEqual(instance_dict.get("__class__"), "User")
        self.assertEqual(type(instance_dict.get("created_at")), str)
        self.assertEqual(type(instance_dict.get("updated_at")), str)

    def test_class_attr(self):
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_str(self):
        model = User()
        self.assertEqual(str(model), f"[User] \
({model.id}) {model.__dict__}")
        my_model = User()
        my_model.name = "My First Model"
        self.assertEqual(str(my_model), f"[User] \
({my_model.id}) {my_model.__dict__}")
        new_model = User()
        new_model.name = "My new model"
        self.assertEqual(str(new_model), f"[User] ({new_model.id}) \
{new_model.__dict__}")

    def test_init(self):
        model = User()
        model_dict = model.to_dict()
        new_model = User(**model_dict)
        self.assertEqual(type(new_model), User)
        self.assertIn("created_at", new_model.__dict__)
        self.assertIn("updated_at", new_model.__dict__)
        new_dict = new_model.to_dict()
        self.assertEqual(new_dict.get("__class__"), "User")
        self.assertEqual(type(new_dict.get("created_at")), str)
        self.assertEqual(type(new_dict.get("updated_at")), str)


if __name__ == "__main__":
    unittest.main()
