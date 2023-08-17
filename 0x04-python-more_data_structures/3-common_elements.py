#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_items = []
    
    for item in set_1:
        if item in set_2:
            common_items.append(item)
            
    return set(common_items)

