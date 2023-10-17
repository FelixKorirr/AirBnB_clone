#!/usr/bin/python3
"""Define HBnB console."""
import cmd
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Define HBnB command interpreter.

    Attributes:
        (hbnb): The custom prompt.
    """

    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "State",
                 "City", "Place", "Amenity", "Review"}

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing."""
        pass

    def do_create(self, arg):
        """Create a new instance of basemodel, save and print its id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Print the string representation of an instance
        based on class name of a given id.
        """
        args = shlex.split(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Delete an instance based on id and class name."""
        args = shlex.split(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Print string representations of all instances based
        or not on class name"""
        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            my_obj = []
            for obj in storage.all().values():
                my_class = obj.__class__.__name__
                if len(args) > 0 and args[0] == my_class:
                    my_obj.append(obj.__str__())
                elif len(args) == 0:
                    my_obj.append(obj.__str__())
            print(my_obj)

    def do_update(self, arg):
        """
        Update a class instance by adding or updating
        a given attribute."""
        args = shlex.split(arg)
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            for i, j in eval(args[2]).items():
                if (i in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[i]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[i])
                    obj.__dict__[i] = valtype(j)
                else:
                    obj.__dict__[i] = j
        storage.save()

    def default(self, arg):
        """behavior of cmd module when input is invalid"""
        my_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        i = re.search(r"\.", arg)
        if i is not None:
            args = [arg[:i.span()[0]], arg[i.span()[1]:]]
            i = re.search(r"\((.*?)\)", args[1])
            if i is not None:
                command = [args[1][:i.span()[0]], i.group()[1:-1]]
                if command[0] in my_dict.keys():
                    call = "{} {}".format(args[0], command[1])
                    return my_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """
        Find the number of instances of a class.
        """
        args = shlex.split(arg)
        i = 0
        for j in storage.all().values():
            my_class = j.__class__.__name__
            if args[0] == my_class:
                i += 1
        print(i)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
