#!/usr/bin/python3
"""akes in a URL, sends a request to the URL and displays
the body of the response"""


import sys
import urllib.request

req = urllib.request.Request(sys.argv[1])
try:
    with urllib.request.urlopen(req) as res:
        print(res.read())
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
