#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using urllib package"""


import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        html = res.read()
    utf8 = html.decode("utf-8")
    out = "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
    print(out.format(type(html), html, utf8))
