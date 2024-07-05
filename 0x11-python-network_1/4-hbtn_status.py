#!/usr/bin/python3
"""
the script that fetches an URL with requests package in python
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    tex = req.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(tex), tex))
