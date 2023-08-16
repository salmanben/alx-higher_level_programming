#!/usr/bin/python3
def custom_calculation(x, y):
    from magic_calculation_102 import addition, subtraction
    if x < y:
        result = addition(x, y)
        for num in range(4, 6):
            result = addition(result, num)
        return result
    else:
        return subtraction(x, y)

