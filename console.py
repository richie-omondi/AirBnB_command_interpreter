#!/usr/bin/env python
""" The entry point of the command interpreter """
import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ The command processor """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the interpreter """
        print("")
        return True

    def help_help(self):
        """ Prints the help command description """
        print("Gives description of a given command")

    def emptyline(self):
        """ Do nothing when an empty line is entered """
        pass

    def do_create(self, arg):
        """
        Usage: create <class>
        Create a new class instance and print its id.
        """
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                if args_array[0] == "BaseModel":
                    obj = BaseModel()
                    obj.save()

                    print(obj.id)
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                if args_array[0] == "BaseModel":
                    if len(args_array) > 1:
                        objs_dict = models.storage.all()
                        search_string = "BaseModel.{}".format(args_array[1])
                        if search_string in objs_dict:
                            print(objs_dict[search_string])
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        Usage: destroys <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id
        """
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                if args_array[0] == "BaseModel":
                    if len(args_array) > 1:
                        objs_dict = models.storage.all()
                        search_string = "BaseModel.{}".format(args_array[1])
                        if search_string in objs_dict:
                            del(objs_dict[search_string])
                            models.storage.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")           
    
    def do_all(self, arg):
        """
        Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects
        """
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                if args_array[0] == "BaseModel":
                    final_list = []
                    for key, value in models.storage.all().items():
                        if ("BaseModel" in key):
                            final_list.append(str(value))
                    print(final_list)
                else:
                    print("** class doesn't exist **")
        else:
            final_list = []
            for key, value in models.storage.all().items():
                final_list.append(str(value))
            print(final_list)

    def do_update(self, arg):
        """
        Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary
        """
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                if args_array[0] == "BaseModel":
                    if len(args_array) > 1:
                        objs_dict = models.storage.all()
                        search_string = "BaseModel.{}".format(args_array[1])
                        if search_string in objs_dict:
                            if len(args_array) > 2:
                                if len(args_array) > 3:
                                    if (args_array[3] not in ["created_at", "updated_at", "id"]):
                                        setattr(objs_dict[search_string], str(args_array[2]), str(args_array[3])) 
                                else:
                                    print("** value missing **")
                            else:
                                print("** attribute name missing **")
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
