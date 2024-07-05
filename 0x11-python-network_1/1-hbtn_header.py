#!/usr/bin/python3
"""
python script that Displays the X-Request-Id
header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    my_request = urllib.request.Request(url)
    with urllib.request.urlopen(my_request) as response:
        print(dict(response.headers).get("X-Request-Id"))
