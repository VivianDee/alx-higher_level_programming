#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""

import urllib.request
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
              .format(type(data), data, data.decode('utf-8')))
