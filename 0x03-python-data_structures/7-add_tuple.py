#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Use the value 0 for each missing integer in the tuples
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Take only the first two elements of each tuple
    result = (a[0] + b[0], a[1] + b[1])
    return result
