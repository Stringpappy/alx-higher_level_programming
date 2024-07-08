#!/bin/bash
# Bash script that takes in a URL, sends a GET request 
[ $# -eq 0 ] && { echo "Usage: $0 <URL>"; exit 1; }; curl -s -o /dev/null -w "%{http_code}\n" $1 | grep -q 200 && curl -s $1
