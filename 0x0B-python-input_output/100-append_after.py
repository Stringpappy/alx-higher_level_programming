#!/usr/bin/python3
"""
python script that contains the "append after" function
"""


def append_after(filename="", search_string="", new_string=""):
    """func that contain appends "new_string" 
    after a line containing search string"""
    with open(filename, 'r', encoding='utf-8') as f:
        list_line = []
        while True:
            myline = f.readline()
            if myline == "":
                break
            list_line.append(myline)
            if search_string in myline:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelineslist_line)
