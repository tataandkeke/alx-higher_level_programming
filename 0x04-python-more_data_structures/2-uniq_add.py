#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    new_list = list(new_set)
    result = sum(new_list)
    return result
