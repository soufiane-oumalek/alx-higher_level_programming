#!/usr/bin/python3
for c in range(26):
    if c % 2 == 0:
        print("{:c}".format(122 - c), end="")
    else:
        print("{:c}".format(90 - c), end="")
