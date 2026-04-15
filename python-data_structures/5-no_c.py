#!/usr/bin/python3
def no_c(my_string):
    result = ""

    for herf in my_string:
        if herf != 'c' and herf != 'C':
            result += herf

    return result
