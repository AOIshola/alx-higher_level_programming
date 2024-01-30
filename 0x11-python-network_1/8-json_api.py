#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    payload = {"q": q}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        data = req.json()
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data["id"], data["name"]))
    except ValueError:
        print("Not a valid JSON")
#    if len(data) == 0:
 #       print("No result")
  #  else:
   #     print("[{}] {}".format(data["id"], data["name"]))
