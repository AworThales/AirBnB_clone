#!/usr/bin/python3
""" Holberton AirBnB Console """
import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ This the main Class for HBNBCommand """
    prompt = '(hbnb) '
    new_classes = {'Amenity': Amenity, 'User': User,'BaseModel': BaseModel, 'City': City,
               'Place': Place, 'Review': Review, 'State': State}

    def do_quit(self, arg):
        """ Exit method for quit typing """
        exit()

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        exit()

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass

    def do_create(self, arg):
        """ Create a fresh instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        fresh = None
        if arg:
            arg_listing = arg.split()
            if len(arg_listing) == 1:
                if arg in self.new_classes.keys():
                    fresh = self.new_classes[arg]()
                    fresh.save()
                    print(fresh.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """ Method to print instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg.split()[0] not in self.new_classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                i = storage.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """ Method to delete instance with class and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_listing = arg.split()
        try:
            obj = eval(arg_listing[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_listing) == 1:
            print('** instance id missing **')
            return
        if len(arg_listing) > 1:
            key = arg_listing[0] + '.' + arg_listing[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """ Method to print all instances """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.new_classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for t, a in storage.all().items() if arg in t])

    def do_update(self, arg):
        """ Method to update JSON file"""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.new_classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
