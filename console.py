#!/usr/bin/python3
"""This module is the entry point of the program."""


from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from models.base_model import BaseModel
import cmd
import models


# List of valid classes
valid_classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
}


class HBNBCommand(cmd.Cmd):
    """This is the command class. It inherits cmd class."""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exits the program when 'ctrl D' is pressed."""
        return True

    def emptyline(self):
        """Overrides the behaviour for empty lines by doing nothing."""
        pass

    def val_class_name(self, class_name):
        """Validate class name."""
        for valid_class in valid_classes.keys():
            if class_name == valid_class:
                return True

        print("** class doesn't exist **")
        return False

    def parse_args(self, args, expected_count):
        """Parses arguments and validates count."""
        args_list = args.split()
        if len(args_list) < expected_count:
            return None
        return args_list

    def do_create(self, args):
        """Create an instance of Basemodel, saves it to JSON file
        and print an id.
        Usage: create <ClassName>
        """
        args_list = self.parse_args(args, 1)
        if not args_list:
            print("** class name missing **")
            return
        # Extract the classname
        class_name = args_list[0]

        if not self.val_class_name(class_name):
            return

        # Create an instance of the class
        instance = valid_classes[class_name]()

        # save to JSON file
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based
        on classname and id.
        Usage: show <ClassName> <instance id>
        """

        # Get lists of arguments
        args_list = args.split()

        if len(args_list) < 1:
            print("** class name missing **")
            return
        class_name = args_list[0]
        if not self.val_class_name(class_name):
            return

        # Check if id is missing
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        instance_id = args_list[1]
        key = f"{class_name}.{instance_id}"

        # Check if instance exist in storage
        all_obj = models.storage.all().get(key)
        if not all_obj:
            print("** no instance found **")
            return

        print(all_obj)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id.

        Usage: destroy <ClassName> <instanceId>
        """
        args_list = args.split()
        if len(args_list) < 1:
            print("** class name missing **")
            return
        class_name = args_list[0]
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = f"{class_name}.{instance_id}"

        all_obj = models.storage.all()
        if key not in all_obj:
            print("** no instance found **")
            return

        del all_obj[key]
        models.storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name.
        Usage: all <ClassName> or all
        """
        args_list = args.split()
        all_obj = models.storage.all()

        # Check if no arg was passed
        if len(args_list) == 0:
            all_instances = [str(obj) for obj in all_obj.values()]
            print(all_instances)
            return

        # class name was provided
        class_name = args_list[0]
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        # Filter all objects and print
        filtered_objs = [
            str(obj) for key, obj in all_obj.items()
            if key.startswith(class_name)
        ]
        print(filtered_objs)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
        or updating an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        # Tokenize each arg and save as a list
        args_list = args.split()

        # Check for class name
        if len(args_list) < 1:
            print("** class name missing **")
            return
        class_name = args_list[0]
        if not self.val_class_name(class_name):
            return

        # Check for instance id
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        instance_id = args_list[1]
        key = f"{class_name}.{instance_id}"

        # Check all storage and fetch key
        all_obj = models.storage.all()
        if key not in all_obj:
            print("** no instance found **")
            return

        # Check for attribute name
        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args_list[2]

        # Check for attribute value
        if len(args_list) < 4:
            print("** value missing **")
            return
        attribute_value = args_list[3]

        # Cast the value to the correct type
        if attribute_value.startswith('"') and attribute_value.endswith('"'):
            attribute_value = attribute_value.strip('"')
        elif attribute_value.isdigit():
            attribute_value = int(attribute_value)
        else:
            try:
                attribute_value = float(attribute_value)
            except ValueError:
                pass

        # Update the attribute in the instance
        obj = all_obj[key]
        setattr(obj, attribute_name, attribute_value)

        # Save obj to JSON file
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
