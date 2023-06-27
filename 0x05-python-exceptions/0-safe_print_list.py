#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    i = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            c += 1
        except IndexError:
            break
    print("\n", end="")
    return c
