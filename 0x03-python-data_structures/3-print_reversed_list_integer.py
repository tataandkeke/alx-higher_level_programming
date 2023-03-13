#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rv_list = my_list.reverse()
    for x in rv_list:
        print("{:d}".format(x))
