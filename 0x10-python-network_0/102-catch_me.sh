#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the 
curl -sLX PUT -H "origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me#server to respond with a message containing You got me!, in the body of the response.
