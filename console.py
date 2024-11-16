#!/usr/bin/python3
"""This module is the entry point of the program."""


from models.base_model import BaseModel
import cmd
import models


# List of valid classes
valid_classes = {
    "BaseModel": BaseModel,
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

    def do_create(self, args):
        """Create an instance of Basemodel, saves it to JSON file
        and print an id.
        Usage: create <ClassName>
        """
        if not args:
            print("** class name missing **")
            return
        # Extract the classname
        class_name = args.split()[0]

        if class_name not in valid_classes:
            print("** class doesn't exist **")
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
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        # Check if id is missing
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        instance_id = args_list[1]
        key = f"{class_name}.{instance_id}"

        # Check if instance exist in storage
        all_obj = models.storage.all()
        if key not in all_obj:
            print("** no instance found **")
            return

        print(all_obj[key])

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
