#!/usr/bin/python3
"""text indentation"""


def text_indentation(text):
    """ function that prints a text with 2 new
    lines after each of these characters: ., ?
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    for ch in text:
        if ch == ' ':
            i += 1
        else:
            break

    for ch in text:
        print(ch, end="")
        if ch == "\n" or ch in ".?:":
            if ch in ".?:":
                print("\n")
            i = 0
            continue
        elif ch == ' ':
            i += 1
            if i == 2:
                print("\n")
                i = 0
                continue
        i = 0
