#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list only once for each integer."""
    unique_set = set()
    
    for num in my_list:
        unique_set.add(num)
    
    return sum(unique_set)
