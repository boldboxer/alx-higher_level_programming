#!/usr/bin/python3

def no_c(my_string):
    acceptable_str = ''
    for i in my_string:
        if i != 'c' and i != "C":
            acceptable_str += i
    return (acceptable_str)
