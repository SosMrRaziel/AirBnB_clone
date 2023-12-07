#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.city import City
from models import storage
# from models.base_model import BaseModel as BM


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            obj = eval(arg)()  # Create a new instance of the class
            obj.save()  # Save the instance to the JSON file
            print(obj.id)  # Print the id of the instance

    def do_show(self, arg):
        """Show command to print the string representation of an instance"""
        args = arg.split()  # Split the argument into a list
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]  # Create the key for the instance
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])  # Print the string
                # representation of the instance

    def do_destroy(self, arg):
        """Destroy command to delete an instance based
        on the class name and id"""
        args = arg.split()  # Split the argument into a list
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]  # Create the key for the instance
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]  # Delete the instance from the dic
                storage.save()  # Save the change to the JSON file

    def do_all(self, arg):
        """All command to print all string representation of all instances"""
        if not arg:
            # Print all instances
            print([str(value) for value in storage.all().values()])
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            # Print only instances of the specified class
            print([str(value) for key, value in storage.all().items()
                   if key.startswith(arg)])

    def do_update(self, arg):
        """Update command to update an instance
        based on the class name and id"""
        args = arg.split()  # Split the argument into a list
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]  # Create the key for the instance
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = storage.all()[key]  # Get the instance object
                attr = args[2]  # Get the attribute name
                value = args[3]  # Get the attribute value
                # Remove the double quotes from the value
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                # Cast the value to the attribute type
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
                # Set the attribute value of the instance
                setattr(obj, attr, value)
                obj.save()  # Save the change to the JSON file

    # You can add more commands and methods as you work through tasks


if __name__ == '__main__':
    HBNBCommand().cmdloop()
