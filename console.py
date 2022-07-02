#!/usr/bin/python3
"""
console.py contains the entry point of the command interpreter
"""
import cmd
import models
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class defines all common attributes/methods for command
    interpreter
    """
    prompt = "(hbnb)"
    class_types = ["BaseModel"]

    def do_quit(self, args):
        """
        Typing <quit> will exit the console
        """
        return True

    def do_EOF(self, args):
        """
        Typing <EOF> will exit the console
        """
        return True

    def emptyline(self):
        """
        An empty line + ENTER won't execute anything
        """
        pass

    def do_create(self, class_name):
        """
        Typing <create class_name> will create a new object of class
        class_name, will save it (to the JSON file) and will print it's id
        """
        if class_name:
            if (class_name in self.class_types):
                obj = eval(class_name)()
                obj.save()
                print(f"{obj.id}")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Typing <show class_name object_id> prints the string representation
        of the object
        """
        if not line:
            print("** class name missing **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        else:
            class_name, object_id = [str(s) for s in line.split()]
            if class_name in self.class_types:
                key = class_name + "." + object_id
                if key in storage.all():
                    print(f"{storage.all()[key]}")
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Typing <destroy class_name object_id> deletes that instance and
        save the change into the JSON file
        """
        if not line:
            print("** class name missing **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        else:
            class_name, object_id = [str(s) for s in line.split()]
            if class_name in self.class_types:
                key = class_name + "." + object_id
                all_objects_dict = storage.all()
                if key in storage.all():
                    all_objects_dict.pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, class_name):
        """
        Typing <all class_name> prints the string representation of all the
        objects of that class. Typing <all> prints the string representation of
        all objects
        """
        all_objects_dict = storage.all()
        if not class_name:
            {print(attributes_dict) for key, attributes_dict in
                all_objects_dict.items()}
        else:
            if class_name in self.class_types:
                {print(attributes_dict) for key, attributes_dict in
                    all_objects_dict.items()
                    if attributes_dict.__class__.__name__ == class_name}
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """
        Typing <update class_name object_id attribute_name attribute_value>
        updates that instance by adding or updating attribute (saves the change
        into the JSON file). If the attribute value is an string, it must be
        double quoted
        """
        if not line:
            print("** class name missing **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        elif len(line.split()) < 3:
            print("** attribute name missing **")
        elif len(line.split()) < 4:
            print("** value missing **")
        else:
            class_name, object_id, attribute_name, attribute_value = \
                [str(s) for s in line.split()]
            attribute_value = attribute_value.replace('"', '')
            if class_name in self.class_types:
                key = class_name + "." + object_id
                if key in storage.all():
                    setattr(storage.all()[key], attribute_name,
                            attribute_value)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
