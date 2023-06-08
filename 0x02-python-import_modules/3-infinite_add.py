#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    c = 0
    for i in range(1, len(argv)):
        c = int(argv[i]) + c
    print(c)
