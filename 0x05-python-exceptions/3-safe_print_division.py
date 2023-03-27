#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        diva = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside reslt: {}".format(diva))
