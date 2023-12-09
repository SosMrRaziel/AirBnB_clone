#!/usr/bin/python3
"""
Defines AirBnB console module
"""
import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    contains the entry point of the command interpreter
    """
    prompt = "(hbnb) "
    dict_classes = {"BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review
                    }

    def do_quit(self, line):
        """quit command to exit the HBNB console"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the HBNB program"""
        print("")
        return True

    def emptyline(self):
        """Overrides the cmd emptyline method, do nothing"""
        pass

    def do_create(self, args):
        """Creates a new instance of any class
        usage : create <class_name>
        example: create BaseModel
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
            return
        new_instance = eval(args[0])()
        storage.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id
        usage: show <class_name> <id>
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = "{}.{}".format(args[0], args[1])
        if obj_id in storage.all().keys():
            print(storage.all()[obj_id])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        usage: destroy <class_name> <id>
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = "{}.{}".format(args[0], args[1])
        if obj_id in storage.all().keys():
            del storage.all()[obj_id]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name
        usage: all <class_name> or all
        """
        args = args.split()
        if not args:
            print([obj.__str__() for obj in storage.all().values()])
            return
        if args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
            return
        list_objs = []
        for obj in storage.all().values():
            if obj.__class__.__name__ == args[0]:
                list_objs += [obj.__str__()]
        print(list_objs)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj_id = "{}.{}".format(args[0], args[1])
        if obj_id not in storage.all().keys():
            print("** no instance found **")
            return
        my_object = storage.all()[obj_id]
        setattr(my_object, args[2], args[3])
        my_object.save()

    def precmd(self, args):
        """update precmd to handle the format : <class_name>.command()"""
        line = re.match(r"^(\w+)\.(\w+)(?:\((.*)\))$", args)
        if line:
            cls_name = line.group(1)
            command = line.group(2)
            cls_id = line.group(3)
            args = "{} {} {}".format(command, cls_name, cls_id)
        return cmd.Cmd.precmd(self, args)

    def do_count(self, args):
        """retrieve the number of instances of a class
        Usage: <class_name>.count() or count <class_name>
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
            return

        counter = [obj for obj in storage.all().values()
                   if isinstance(obj, HBNBCommand.dict_classes[args[0]])]
        print(len(counter))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
