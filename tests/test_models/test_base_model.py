import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Unit test for the BaseModel class"""

    def setUp(self):
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if an instance of a Basemodel is
        created correctly.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertTrue(uuid.UUID(self.model.id)) # Check if it's a valid uuid
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_unique_ids(self):
        """Test if each instance has a unique id."""
        BM = BaseModel()
        self.assertNotEqual(self.model.id, BM.id)

    def test_str_rep(self):
        """Tests the __str__ method."""
        expected = f"[BaseModel] ({self.model.id} {self.model.__dict__})"
        self.assertEqual(str(self.model), expected) # I stopped here

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
