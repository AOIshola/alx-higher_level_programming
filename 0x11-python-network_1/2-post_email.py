#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response"""


import sys
import urllib.request
import urllib.parse

val = {"email": sys.argv[2]}
data = urllib.parse.urlencode(val)
data = data.encode('ascii')
req = urllib.request.Request(sys.argv[1], data)
try: urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)
