#!/usr/bin/python3
"""Defines the HBnB console module."""
import cmd
import re
import json
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    arg_list = []
    if arg:
        if re.search(r'\((.*?)\)', arg):
            cls_name = arg.split('.')
            arg_list.append(cls_name[0])
            if len(cls_name) > 1:
                lexer = shlex.shlex(cls_name[1])
                lexer.whitespace += '(,)"{:}\''
                [arg_list.append(token) for token in lexer]
        else:
            [arg_list.append(elm) for elm in arg.split()]
    return arg_list


class HBNBCommand(cmd.Cmd):
    """Defines class for the AiRBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Commands to exit from the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit from the program."""
        print("")
        return True

    def emptyline(self):
        """No action is required for empty line received."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_p = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_p[1])
            if match is not None:
                command = [arg_p[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_p[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """Creates a new instance and print its id.
        Usage: create <class name>
        """
        arg_p = parse(arg)
        if len(arg_p) == 0:
            print("** class name missing **")
        elif arg_p[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_p[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string instance based on the class name and id.
        Usage: show <class name> <id>
        """
        arg_p = parse(arg)
        obj_dict = storage.all()
        if len(arg_p) == 0:
            print("** class name missing **")
        elif arg_p[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_p) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_p[0], arg_p[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_p[0], arg_p[1])].__str__())

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        arg_p = parse(arg)
        obj_dict = storage.all()
        if len(arg_p) == 0:
            print("** class name missing **")
        elif arg_p[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_p) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_p[0], arg_p[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_p[0], arg_p[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        Usage: all or all <class name>
        """
        arg_p = parse(arg)
        if len(arg_p) > 0 and arg_p[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_tmp = []
            for obj in storage.all().values():
                if len(arg_p) > 0 and arg_p[0] == obj.__class__.__name__:
                    obj_tmp.append(obj.__str__())
                elif len(arg_p) == 0:
                    obj_tmp.append(obj.__str__())
            print(obj_tmp)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        arg_p = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_p[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        Usage: update <class> <id> <attribute_name> <attribute_value>
        """
        arg_p = parse(arg)
        obj_dict = storage.all()

        if len(arg_p) == 0:
            print("** class name missing **")
            return False
        if arg_p[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_p) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_p[0], arg_p[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_p) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_p) == 3:
            try:
                type(eval(arg_p[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_p) == 4:
            obj = obj_dict["{}.{}".format(arg_p[0], arg_p[1])]
            if arg_p[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[arg_p[2]])
                obj.__dict__[arg_p[2]] = val_type(arg_p[3])
            else:
                obj.__dict__[arg_p[2]] = arg_p[3]
        elif type(eval(arg_p[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_p[0], arg_p[1])]
            for key, val in eval(arg_p[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    val_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = val_type(val)
                else:
                    obj.__dict__[key] = val
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
