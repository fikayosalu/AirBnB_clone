import unittest
import json
import os
from models.place import Place
from datetime import datetime, timedelta


class TestPlace(unittest.TestCase):
    """Unit test for the Place class"""

    def setUp(self):
        pass

    def test_save(self):
        """Test the save() method"""
        model = Place()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertGreater(model.updated_at, old_updated_at)
        self.assertAlmostEqual(model.updated_at, datetime.now(),
                               delta=timedelta(seconds=1))

    def test_to_dict(self):
        model = Place()
        instance_dict = model.to_dict()
        self.assertIn("__class__", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertEqual(instance_dict.get("__class__"), "Place")
        self.assertEqual(type(instance_dict.get("created_at")), str)
        self.assertEqual(type(instance_dict.get("updated_at")), str)

    def test_class_attr(self):
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

    def test_str(self):
        model = Place()
        self.assertEqual(str(model), f"[Place] \
({model.id}) {model.__dict__}")
        my_model = Place()
        my_model.name = "My First Model"
        self.assertEqual(str(my_model), f"[Place] \
({my_model.id}) {my_model.__dict__}")
        new_model = Place()
        new_model.name = "My new model"
        self.assertEqual(str(new_model), f"[Place] ({new_model.id}) \
{new_model.__dict__}")

    def test_init(self):
        model = Place()
        model_dict = model.to_dict()
        new_model = Place(**model_dict)
        self.assertEqual(type(new_model), Place)
        self.assertIn("created_at", new_model.__dict__)
        self.assertIn("updated_at", new_model.__dict__)
        new_dict = new_model.to_dict()
        self.assertEqual(new_dict.get("__class__"), "Place")
        self.assertEqual(type(new_dict.get("created_at")), str)
        self.assertEqual(type(new_dict.get("updated_at")), str)


if __name__ == "__main__":
    unittest.main()
