#!/usr/bin/python3
"""insert line to txt file"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
    after each line containing a specific string
    Args:
    @filename: name of the file
    @search_string: string search for inside file
    @new_string: string that to be insert
    """
    txt = ""
    with open(filename) as r:
        line = r.readline()

        while line:
            txt += line
            if search_string in line:
                txt += new_string
            line = r.readline()
    with open(filename, "w") as w:
        w.write(txt)
