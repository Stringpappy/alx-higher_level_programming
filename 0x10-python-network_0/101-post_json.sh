#!/bin/bash
#a script that  curl a json file
curl -s -H "content-type:application/json"  -d @"$2" -X POST "$1"
