#!/usr/bin/python3
"""This is the read_file module
"""


def read_file(filename=""):
    with open(filename, encoding='utf-8') as a_file:
        a_file.read()
