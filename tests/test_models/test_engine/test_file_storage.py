import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from unittest.mock import patch


class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage class that handles saving \
            and loading models."""

    def setUp(self):
        """Set up the test case."""

        # Create a new instance of BaseModel for testing
        self.model = BaseModel()
        self.storage = FileStorage()
        # Load existing objects before tests
        self.storage.reload()
        self.file_path = self.storage._FileStorage__file_path

    def tearDown(self):
        """Clean up after each test."""
        # Remove file after each test to ensure a clean env for each test
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save(self):
        """Test saving a model instance to the file."""
        # Add the object to storage and save it
        self.storage.new(self.model)
        self.storage.save()

        # Ensure the file exists after saving
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test reloading saved model instances from the file."""
        self.storage.new(self.model)
        self.storage.save()

        # Create a new storage obj to simulate a fresh start
        new_storage = FileStorage()
        new_storage.reload()

        # Verify the object was reloaded correctly
        all_objects = new_storage.all()
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, all_objects)

        reloaded_obj = all_objects[key]
        self.assertEqual(self.model.id, reloaded_obj.id)
        self.assertEqual(self.model.created_at, reloaded_obj.created_at)
        self.assertEqual(self.model.updated_at, reloaded_obj.updated_at)

    def test_save_reload_multiple_objects(self):
        """Test saving and reloading multiple objects."""
        new_bm = BaseModel()
        self.storage.new(self.model)
        self.storage.new(new_bm)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        key = f"BaseModel.{self.model.id}"
        key1 = f"BaseModel.{new_bm.id}"
        self.assertIn(key, all_objects)
        self.assertIn(key1, all_objects)

        reloaded_obj1 = all_objects[key]
        reloaded_obj2 = all_objects[key1]

        self.assertEqual(self.model.id, reloaded_obj1.id)
        self.assertEqual(new_bm.id, reloaded_obj2.id)

    """
    def test_reload_no_file(self):
        #Test reloading when the file doesn't exist.
        if os.path.exists("file.json"):
            os.remove("file.json")

        # Try loading from an empty file path (should not raise an error)
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 0)
    """

    def test_instance_from_dict(self):
        """Test creating an instance from a dictionary repr."""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)

        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertEqual(self.model.to_dict(), new_model.to_dict())

    def test_json_format_in_file(self):
        """Tests saved file contains JSON formatted data."""
        self.storage.new(self.model)
        self.storage.save()

        # Ensure the file contains valid JSON format
        with open(self.file_path, 'r') as file:
            content = file.read()
            try:
                import json
                # Try to parse the content as JSON
                json.loads(content)
                is_valid_json = True
            except json.JSONDecodeError:
                is_valid_json = False

            self.assertTrue(is_valid_json)

    def test_to_dict_serialization(self):
        """Test if to dict method includes necessary fields."""
        model_dict = self.model.to_dict()

        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_attr(self):
        """Test the class attributes of the FileStorage class"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")


if __name__ == "__main__":
    unittest.main()
