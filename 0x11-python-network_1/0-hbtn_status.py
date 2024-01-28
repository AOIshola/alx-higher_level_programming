#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using urllib package"""


import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
#with urllib.request.urlopen("http://python.org/") as res:
    html = res.read()
utf8 = html.decode("utf-8")
output = "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
#print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(type(html), html, utf8))
print(output.format(type(html), html, utf8))
