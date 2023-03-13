#!/usr/bin/python3
def def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_1 = tuple_a[0]
    tuple_a_2 = tuple_a[1]
    tuple_b_1 = tuple_b[0]
    tuple_b_2 = tuple_b[1]
    sum_1 = tuple_a_1 + tuple_b_1
    sum_2 = tuple_a_2 + tuple_b_2
    new_tuple = (sum_1, sum_2)
    return new_tuple
