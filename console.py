#!/usr/bin/python3
"""This module is the entry point of the program."""


import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
