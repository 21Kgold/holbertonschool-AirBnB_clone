#!/usr/bin/python3
"""
Unittests for the Console.py file
"""

import cmd
import pycodestyle
import unittest
import console
import sys
from io import StringIO
from unittest.mock import patch
from models import storage
from models.engine.file_storage import FileStorage
HBNB = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Class to test Console class
    """
    def test_prompt(self):
        """
        Test for the prompt text of the console
        """
        self.assertEqual("(hbnb)", HBNB.prompt)

    def test_empty_line(self):
        """
        Test that no output exists with an empty line and enter
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_help_quit(self):
        """
        Test for help of the quit command
        """
        help_text = ("Typing <quit> will exit the console")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help quit"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_EOF(self):
        """
        Test for help of the EOF command
        """
        help_text = ("Typing <EOF> will exit the console")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help EOF"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_create(self):
        """
        Test for help of the create command
        """
        help_text = ("Typing <create class_name> will create a new object "
                     "of class class_name, will save it (to the JSON file) "
                     "and will print it's id")
        len_text = 135
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help create"))
            self.assertEqual(len_text, len(output.getvalue().strip()))

    def test_help_show(self):
        """
        Test for help of the show command
        """
        help_text = ("Typing <show class_name object_id> prints the "
                     "string representation of the object")
        len_text = 89
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help show"))
            self.assertEqual(len_text, len(output.getvalue().strip()))

    def test_help_destroy(self):
        """
        Test for help of the destroy command
        """
        help_text = ("Typing <destroy class_name object_id> deletes "
                     "that instance and save the change into the JSON file")
        len_text = 106
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help destroy"))
            self.assertEqual(len_text, len(output.getvalue().strip()))

    def test_help_all(self):
        """
        Test for help of the all command
        """
        help_text = ("Typing <all class_name> prints the string "
                     "representation of all the objects of that "
                     "class. Typing <all> prints the string representation "
                     "of all objects")
        len_text = 167
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help all"))
            self.assertEqual(len_text, len(output.getvalue().strip()))

    def test_help_update(self):
        """
        Test for help of the update command
        """
        help_text = ("Typing <update class_name object_id attribute_name "
                     "attribute_value> updates that instance by adding or"
                     "updating attribute (saves the change into the JSON"
                     "file). If the attribute value is an string, it must"
                     "be double quoted")
        len_text = 178
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help update"))
            self.assertEqual(len_text, len(output.getvalue().strip()))

    def test_style_test(self):
        """
        Test if test_console.py passes the pycodestyle style
        """
        style = pycodestyle.StyleGuide()
        console_style_t = style.check_files(['tests/test_console.py'])
        self.assertEqual(console_style_t.total_errors, 0, "Does not com\
        ply with pycodestyle")

    def test_style(self):
        """
        Test if console.py passes the pycodestyle style
        """
        console_style = pycodestyle.StyleGuide().check_files(['console.py'])
        self.assertEqual(console_style.total_errors, 0, "Does not com\
        ply with pycodestyle")

    def test_methods_doc_exists(self):
        """
        Test if the methods in console.py have document\
        ation (test only if they exist)
        """
        self.assertIsNotNone(console.__doc__, "Console doc documentat\
        ion does not exists")
        self.assertIsNotNone(HBNB.do_quit.__doc__, "Console do_quit\
        Documentation does not exists")
        self.assertIsNotNone(HBNB.do_EOF.__doc__, "Console do_EOF\
        Documentation does not exists")
        self.assertIsNotNone(HBNB.emptyline.__doc__, "Console\
        do_emptyline Documentation does not exists")
        self.assertIsNotNone(HBNB.do_create.__doc__, "Console\
        do_create Documentation does not exists")
        self.assertIsNotNone(HBNB.do_show.__doc__, "Console do_show\
        Documentation does not exists")
        self.assertIsNotNone(HBNB.do_destroy.__doc__, "Console\
        do_destroy Documentation does not exists")
        self.assertIsNotNone(HBNB.do_all.__doc__, "Console do_all\
        Documentation does not exists")
        self.assertIsNotNone(HBNB.do_update.__doc__, "Console\
        do_update Documentation does not exists")
        self.assertIsNotNone(HBNB.default.__doc__, "Console default\
        Documentation does not exists")

    def test_methods_doc_length(self):
        """
        Test if the methods documentation in console.py have mo\
        re than 10 letters
        """
        n_con = len(console.__doc__)
        self.assertGreaterEqual(n_con, 10, "Console doc document\
        ation has less than 10 letters")
        n_con_quit = len(HBNB.do_quit.__doc__)
        self.assertGreaterEqual(n_con_quit, 10, "Console do_quit Document\
        ation has less than 10 letters")
        n_con_eof = len(HBNB.do_EOF.__doc__)
        self.assertGreaterEqual(n_con_eof, 10, "Console do_EOF Documentat\
        ion has less than 10 letters")
        n_con_emptyline = len(HBNB.emptyline.__doc__)
        self.assertGreaterEqual(n_con_emptyline, 10, "Console do_emptyline D\
        ocumentation has less than 10 letters")
        n_con_create = len(HBNB.do_create.__doc__)
        self.assertGreaterEqual(n_con_create, 10, "Console do_create Document\
        ation has less than 10 letters")
        n_con_show = len(HBNB.do_show.__doc__)
        self.assertGreaterEqual(n_con_show, 10, "Console do_show Document\
        ation has less than 10 letters")
        n_con_destroy = len(HBNB.do_destroy.__doc__)
        self.assertGreaterEqual(n_con_destroy, 10, "Console do_destroy Doc\
        umentation has less than 10 letters")
        n_con_all = len(HBNB.do_all.__doc__)
        self.assertGreaterEqual(n_con_all, 10, "Console do_all Document\
        ation has less than 10 letters")
        n_con_update = len(HBNB.do_update.__doc__)
        self.assertGreaterEqual(n_con_update, 10, "Console do_update Document\
        ation has less than 10 letters")
        n_con_default = len(HBNB.default.__doc__)
        self.assertGreaterEqual(n_con_default, 10, "Console default Document\
        ation has less than 10 letters")

    def test_HBNBCommand_class_doc_exists(self):
        """
        Test if the console HBNBCommand class in console.py have document\
        ation (test only if it exist)
        """
        self.assertIsNotNone(HBNB.__doc__, "Console HBNBCommand d\
        ocumentation does not exists")

    def test_HBNBCommand_doc_length(self):
        """
        Test if the HBNBCommand documentation in console.py has mo\
        re than 10 letters
        """
        n_con = len(HBNB.__doc__)
        self.assertGreaterEqual(n_con, 10, "Console HBNBCommand document\
        ation has less than 10 letters")

    def test_quit(self):
        """
        Test that the quit command exists
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNB().onecmd("quit"))

    def test_EOF(self):
        """
        Tests that the EOF command exists
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNB().onecmd("EOF"))

    def test_create_no_class(self):
        """
        Test the console create with no class
        """
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_create_bad_class(self):
        """
        Test the console create with bad class argument
        """
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BadClass"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_no_class(self):
        """
        Test the console show with no class
        """
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_bad_class(self):
        """
        Test the console show with bad class argument
        """
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show BadClass"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_no_id(self):
        """
        Test the console show with User class and id argument missing
        """
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show User"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_bad_id(self):
        """
        Test the console show with User class and a bad id argument
        """
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show User BadUser"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "User.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "City.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Review.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
