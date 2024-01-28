#!/usr/bin/python3
"""Takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally
displays the body of the response"""

import requests
import sys

req = requests.post(sys.argv[1], data={"email": sys.argv[2]})
print(req.content.decode("utf-8"))
