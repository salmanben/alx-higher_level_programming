#!/usr/bin/python3
if __name__ == '__main__':
    from importlib import import_module
    hidden_module = import_module('hidden_4')
    for item_name in sorted(dir(hidden_module)):
        if item_name[0:2] != '__':
            print('{:s}'.format(item_name))

