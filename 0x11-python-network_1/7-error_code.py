#!/usr/bin/python3
"""
    This script takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8)
"""

import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    data = requests.get(url)
    if data.status_code >= 400:
        print("Error code: {}".format(data.status_code))
    else:
        print(data.text)
