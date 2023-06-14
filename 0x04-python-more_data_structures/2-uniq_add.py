#!/usr/bin/python3
def uniq_add(my_list=[]):
    u_add = set()
    for n in my_list:
        if isinstance(n, int):
            u_add.add(n)
    return sum(u_add)
