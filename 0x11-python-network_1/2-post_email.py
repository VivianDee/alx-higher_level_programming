#!/usr/bin/python3
"""
    This script sends a POST request to the passed URL
    with the email as a parameter
"""

import urllib.request
import sys
if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    value = urllib.parse.urlencode(value)
    value = value.encode('ascii')
    url = sys.argv[1]
    req = urllib.request.Request(url, value)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        print(data.decode('utf-8'))
