import unittest
import json
import os
from models.review import Review
from datetime import datetime, timedelta


class TestReview(unittest.TestCase):
    """Unit test for the Review class"""

    def setUp(self):
        pass

    def test_save(self):
        """Test the save() method"""
        model = Review()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertGreater(model.updated_at, old_updated_at)
        self.assertAlmostEqual(model.updated_at, datetime.now(),
                               delta=timedelta(seconds=1))

    def test_to_dict(self):
        model = Review()
        instance_dict = model.to_dict()
        self.assertIn("__class__", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertEqual(instance_dict.get("__class__"), "Review")
        self.assertEqual(type(instance_dict.get("created_at")), str)
        self.assertEqual(type(instance_dict.get("updated_at")), str)

    def test_str(self):
        model = Review()
        self.assertEqual(str(model), f"[Review] \
({model.id}) {model.__dict__}")
        my_model = Review()
        my_model.name = "My First Model"
        self.assertEqual(str(my_model), f"[Review] \
({my_model.id}) {my_model.__dict__}")
        new_model = Review()
        new_model.name = "My new model"
        self.assertEqual(str(new_model), f"[Review] ({new_model.id}) \
{new_model.__dict__}")

    def test_init(self):
        model = Review()
        model_dict = model.to_dict()
        new_model = Review(**model_dict)
        self.assertEqual(type(new_model), Review)
        self.assertIn("created_at", new_model.__dict__)
        self.assertIn("updated_at", new_model.__dict__)
        new_dict = new_model.to_dict()
        self.assertEqual(new_dict.get("__class__"), "Review")
        self.assertEqual(type(new_dict.get("created_at")), str)
        self.assertEqual(type(new_dict.get("updated_at")), str)


if __name__ == "__main__":
    unittest.main()
