#!/usr/bin/python3
"""This is the load_from_json_file module
"""


import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file function write an Object to a text file
        Args:
            filename: file name variable
            my_obj:   object file
        Return:
            reads the file
    """

    with open(filename, mode='w', encoding='utf-8') as add_item.json:
        add_item.json.write(json.dumps(my_obj))


def load_from_json_file(filename):
    """ load_from_json_file function create an Object from a text file

        Args:
            filename: file name variable
        Return:
            an object
    """

    with open(filename, encoding='utf-8') as add_item.json:
        return (json.load(add_item.json))
