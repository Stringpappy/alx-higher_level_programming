#!/usr/bin/python3
"""
A python script that Sends a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    my_url = sys.argv[1]
    my_value = {"email": sys.argv[2]}

    req = requests.post(my_url, data=my_value)
    print(req.text)
