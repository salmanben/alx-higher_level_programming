#!/usr/bin/python3

def magic_calculation(base, exponent):
    final_result = 0
    for iteration in range(1, 3):
        try:
            if iteration > base:
                raise Exception("Too far")
            else:
                final_result += base ** exponent / iteration
        except Exception as exception:
            final_result = exponent + base
            break
    return final_result
