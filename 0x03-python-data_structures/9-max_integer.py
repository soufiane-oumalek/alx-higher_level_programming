#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list) == 0:
        return None
    else:
        int_max = my_list[0]
        for i in range(len(my_list)):
            if int_max < my_list[i]:
                int_max = my_list[i]
            else:
                continue
        return int_maxx
