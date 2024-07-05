#!/usr/bin/python3
"""
 pyscript that Sends a request to a given URL &  displays the response body.
Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    my_url = sys.argv[1]

    r = requests.get(my_url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
