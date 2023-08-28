#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        element = my_list[i]
        try:
            print("{:d}".format(element), end="")
            count += 1
        except IndexError:
            break
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
