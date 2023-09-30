#!/usr/bin/python3
"""
    This script displays the value of the X-Request-Id
    variable found in the header of a given url
"""

import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    data = requests.get(url)
    print(data.headers['X-Request-Id'])
