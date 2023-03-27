#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    int real = 0
    try:
        for a in range(x):
            print my_list[a]
            real = real + 1
    except NameError:
        print("There is an error")
    return real
