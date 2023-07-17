#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.state import State


def parse(arg):
    curlly_braced = re.search(r"\{(.*?)\}", arg)
    bracketed = re.search(r"\[(.*?)\]", arg)
    if curlly_braced is None:
        if bracketed is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:bracketed.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(bracketed.group())
            return retl
    else:
        lexer = split(arg[:curlly_braced.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curlly_braced.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    new_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdicts = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argu = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argu[1])
            if match is not None:
                command = [argu[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdicts.keys():
                    call = "{} {}".format(argu[0], command[1])
                    return argdicts[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, line):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argu = parse(arg)
        objdicts = storage.all()
        if len(argu) == 0:
            print("** class name missing **")
        elif argu[0] not in HBNBCommand.new_classes:
            print("** class doesn't exist **")
        elif len(argu) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argu[0], argu[1]) not in objdicts:
            print("** no instance found **")
        else:
            print(objdicts["{}.{}".format(argu[0], argu[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argu = parse(arg)
        objdicts = storage.all()
        if len(argu) == 0:
            print("** class name missing **")
        elif argu[0] not in HBNBCommand.new_classes:
            print("** class doesn't exist **")
        elif len(argu) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argu[0], argu[1]) not in objdicts.keys():
            print("** no instance found **")
        else:
            del objdicts["{}.{}".format(argu[0], argu[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argu = parse(arg)
        if len(argu) > 0 and argu[0] not in HBNBCommand.new_classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argu) > 0 and argu[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argu) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argu = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argu[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argu = parse(arg)
        objdicts = storage.all()

        if len(argu) == 0:
            print("** class name missing **")
            return False
        if argu[0] not in HBNBCommand.new_classes:
            print("** class doesn't exist **")
            return False
        if len(argu) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argu[0], argu[1]) not in objdicts.keys():
            print("** no instance found **")
            return False
        if len(argu) == 2:
            print("** attribute name missing **")
            return False
        if len(argu) == 3:
            try:
                type(eval(argu[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argu) == 4:
            obj = objdicts["{}.{}".format(argu[0], argu[1])]
            if argu[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argu[2]])
                obj.__dict__[argu[2]] = valtype(argu[3])
            else:
                obj.__dict__[argu[2]] = argu[3]
        elif type(eval(argu[2])) == dict:
            obj = objdicts["{}.{}".format(argu[0], argu[1])]
            for k, v in eval(argu[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
