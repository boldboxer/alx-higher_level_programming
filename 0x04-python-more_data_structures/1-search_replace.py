#!/usr/bin/python3



def search_replace(my_list, search, replace):
    """
    replaces all occurrences of an element by another in a new lis
    """
    return ([ele if ele != search else replace for ele in my_list])
