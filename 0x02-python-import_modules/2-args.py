#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_index = 1
    arg_count = len(sys.argv) - arg_index
    print('{:d} argument{:s}{:s}'.format(
        arg_count, 's' * (arg_count != 1),
        ':' if arg_count > 0 else '.'
        ))
    for arg in sys.argv[arg_index:]:
        print('{:d}: {:s}'.format(arg_index, arg))
        arg_index += 1

