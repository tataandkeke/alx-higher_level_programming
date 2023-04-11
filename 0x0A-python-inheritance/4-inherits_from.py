#!/usr/bin/python3
"""inherits from module
"""


def inherits_from(obj, a_class):
    """ checks if an object inherits from a subclass
    Args:
        obj: object variable
        a_class: specified class
    Return:
        True or False
    """

    return (issubclass(obj, a_class))
