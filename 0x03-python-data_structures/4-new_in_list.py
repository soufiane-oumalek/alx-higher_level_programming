#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            new_list = []
            for i, item in enumerate(my_list):
                if i == idx:
                    new_list.append(element)
                else:
                    new_list.append(item)
            return new_list
