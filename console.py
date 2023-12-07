#!/usr/bin/python3
import cmd
from models.base_model import BaseModel as BM

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    new_inst = BM()
    new_inst.save()

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        class_str = "BaseModel"
        if arg:
            if arg == class_str:
                self.new_inst = BM()
                self.new_inst.save()
                print(self.new_inst.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg,):
        tokens = arg.split()
        if arg:
            if tokens[0] == "BaseModel":
                if len(tokens) > 1:
                    if tokens[1] == self.new_inst.id:
                        print(BM())
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg,):
        tokens = arg.split()
        if arg:
            if tokens[0] == "BaseModel":
                if len(tokens) > 1:
                    if tokens[1] == self.new_inst.id:
                        self.new_inst.id = BM().id
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()